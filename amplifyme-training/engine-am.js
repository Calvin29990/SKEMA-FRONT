/* ==========================================================================
   AMPLIFYME TRAINER — Asset Manager (buy-side) engine
   $20M portfolio, 5 names, news-driven. Exposed as window.EngineAM.
   ========================================================================== */
(function (global) {
  'use strict';

  var COMM_BPS = 5;          // coût d'exécution buy-side (5 bps)
  var START_CAPITAL = 20000000;
  var HALF_SPREAD_BPS = 3.2;
  var TICK = 0.01;

  var S = null;
  var STOCKS = (global.EngineData && global.EngineData.STOCK_DEFS) || [];
  var NEWS = (global.EngineData && global.EngineData.NEWS_POOL) || [];

  function rand(a, b) { return a + Math.random() * (b - a); }
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function r2(v) { return Math.round(v * 100) / 100; }
  function n2() {
    var u = 0, v = 0;
    while (u === 0) u = Math.random();
    while (v === 0) v = Math.random();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  }
  function fmtClock(ms) {
    var base = 13 * 3600 + 22 * 60 + Math.floor(ms / 1000);
    var h = Math.floor(base / 3600) % 24, m = Math.floor((base % 3600) / 60), s = base % 60;
    return (h < 10 ? '0' : '') + h + ':' + (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
  }
  function emit(type, data) {
    if (!S) return;
    for (var i = 0; i < S.listeners.length; i++) {
      try { S.listeners[i](type, data); } catch (e) { console.error(e); }
    }
  }

  function init(opts) {
    opts = Object.assign({ roundSec: 240, difficulty: 'normal', capital: START_CAPITAL }, opts || {});
    S = {
      opts: opts,
      capital: opts.capital,
      cash: opts.capital,
      stocks: STOCKS.map(function (d) {
        return {
          t: d.t, name: d.name, ref: d.ref, ref0: d.ref, vol: d.vol,
          mid: d.ref, pos: 0, avg: 0, realised: 0,
          hist: [d.ref], drift: 0, lastDir: 0
        };
      }),
      news: [],
      blotter: [],
      listeners: [],
      ms: 0,
      elapsedMs: 0,
      clockMs: 0,
      phase: 'idle',
      running: false,
      paused: false,
      priceAcc: 0,
      newsTimer: 9000,
      newsSeq: 0,
      trades: 0,
      fees: 0,
      peak: opts.capital,
      maxDD: 0,
      benchStart: 1,
      bench: 1,
      benchHist: [],
      valueHist: [],
      oversize: 0,
      timers: []
    };
    S.benchStart = benchLevel();
    S.bench = S.benchStart;
    S.benchHist.push(1);
    S.valueHist.push(1);
    return api;
  }

  function stock(t) {
    for (var i = 0; i < S.stocks.length; i++) if (S.stocks[i].t === t) return S.stocks[i];
    return null;
  }

  /* ---------------------------------------------------------------- value */
  function portfolioValue() {
    var v = S.cash;
    S.stocks.forEach(function (st) { v += st.pos * st.mid; });
    return v;
  }
  function investedValue() {
    var v = 0;
    S.stocks.forEach(function (st) { v += Math.abs(st.pos * st.mid); });
    return v;
  }
  function benchLevel() {
    var sum = 0;
    S.stocks.forEach(function (st) { sum += st.mid / st.ref0; });
    return sum / S.stocks.length;
  }
  function benchReturn() { return benchLevel() / S.benchStart - 1; }
  function portfolioReturn() { return portfolioValue() / S.capital - 1; }
  function alpha() { return portfolioReturn() - benchReturn(); }

  /* ---------------------------------------------------------------- prices */
  function priceTick() {
    var mult = S.opts.difficulty === 'chaos' ? 1.7 : S.opts.difficulty === 'calme' ? 0.65 : 1;
    var sigma = 0.00048 * mult;
    S.stocks.forEach(function (st) {
      var r = st.drift + n2() * sigma * st.vol;
      st.drift *= 0.88;
      st.mid = Math.max(0.5, st.mid * (1 + r));
      st.hist.push(st.mid);
      if (st.hist.length > 1200) st.hist.shift();
    });
  }

  function market(t) {
    var st = stock(t);
    var hs = st.mid * HALF_SPREAD_BPS / 10000;
    return { bid: r2(st.mid - hs), offer: r2(st.mid + hs) };
  }

  function newsTick() {
    var n = pick(NEWS);
    S.stocks.forEach(function (st) {
      var mag = 0;
      if (n.all) {
        mag = n.all * n.mag * rand(0.75, 1.25);
        if (n.china && (st.t === 'BABA' || st.t === 'VW')) mag *= 1.6;
        if (n.oil && st.t === 'BP') mag = Math.abs(mag) * 1.5;
        if (n.banks && st.t === 'HSBC') mag = Math.abs(mag) * 1.8;
      } else if (n.target === st.t) {
        mag = n.dir * n.mag * rand(0.85, 1.15);
      } else {
        mag = n.dir * n.mag * 0.12 * rand(-0.5, 0.5);
      }
      if (mag !== 0) {
        // le prix bouge par palier : tu as le temps de réagir
        st.mid = Math.max(0.5, st.mid * (1 + mag));
        st.drift += mag * 0.11;
        st.lastDir = mag > 0 ? 1 : -1;
      }
    });
    S.newsSeq++;
    S.news.unshift({
      tag: n.tag, text: n.text, dir: n.all ? n.all : n.dir,
      all: !!n.all, clock: fmtClock(S.clockMs), t: S.ms
    });
    if (S.news.length > 60) S.news.pop();
    emit('news', S.news[0]);
  }

  /* ---------------------------------------------------------------- orders */
  function slipBps(notional) {
    var v = portfolioValue();
    var w = notional / v;
    return 1.2 + w * 40;     // au-delà de ~10 % du portefeuille, l'impact devient cher
  }

  function trade(ticker, side, notional) {
    if (!S || S.phase !== 'live') return { ok: false, error: 'Marché fermé' };
    var st = stock(ticker);
    if (!st) return { ok: false, error: 'Ticker inconnu' };
    notional = Number(notional);
    if (!isFinite(notional) || notional <= 0) return { ok: false, error: 'Montant invalide' };

    var m = market(ticker);
    var px = side === 'BUY' ? m.offer : m.bid;
    var qty = Math.round(notional / px);
    if (qty <= 0) return { ok: false, error: 'Montant trop petit' };

    var v = portfolioValue();
    var slip = slipBps(qty * px);
    px = side === 'BUY' ? px * (1 + slip / 10000) : px * (1 - slip / 10000);
    px = r2(px);
    var gross = qty * px;
    var fee = gross * COMM_BPS / 10000;

    if (side === 'BUY' && gross + fee > S.cash) {
      qty = Math.floor(S.cash / (px * (1 + COMM_BPS / 10000)));
      if (qty <= 0) return { ok: false, error: 'Cash insuffisant' };
      gross = qty * px;
      fee = gross * COMM_BPS / 10000;
    }
    if (side === 'SELL' && qty > st.pos) {
      return { ok: false, error: 'Pas de position à vendre. Vends ' + Math.max(0, st.pos) + ' max.' };
    }

    if (gross > v * 0.35) S.oversize++;

    var signed = side === 'BUY' ? qty : -qty;
    var oldPos = st.pos;
    var newPos = oldPos + signed;
    if (oldPos !== 0 && (oldPos > 0) !== (signed > 0)) {
      var closed = Math.min(Math.abs(signed), Math.abs(oldPos));
      st.realised += (px - st.avg) * closed * (oldPos > 0 ? 1 : -1);
      if (Math.abs(signed) > Math.abs(oldPos)) st.avg = px;
    } else {
      var ao = Math.abs(oldPos), an = Math.abs(newPos);
      st.avg = an > 0 ? (st.avg * ao + px * qty) / an : 0;
    }
    st.pos = newPos;
    if (st.pos === 0) st.avg = 0;

    S.cash += side === 'BUY' ? -(gross + fee) : (gross - fee);
    S.fees += fee;
    S.trades++;
    S.blotter.unshift({
      t: S.ms, clock: fmtClock(S.clockMs), sec: st.t, side: side,
      qty: qty, price: px, notional: gross, slip: slip
    });
    if (S.blotter.length > 200) S.blotter.pop();

    emit('trade', { ticker: st.t, side: side, qty: qty, price: px, notional: gross, slip: slip, cash: S.cash });
    return { ok: true, qty: qty, price: px, notional: gross, slip: slip };
  }

  function sellAll(ticker) {
    var st = stock(ticker);
    if (!st || st.pos <= 0) return { ok: false, error: 'Pas de position' };
    return trade(ticker, 'SELL', st.pos * st.mid * 0.995);
  }

  /* ---------------------------------------------------------------- step */
  function step(dt) {
    if (!S || !S.running || S.paused || S.phase !== 'live') return;
    dt = Math.min(dt, 400);
    S.ms += dt;
    S.elapsedMs += dt;
    S.clockMs += dt;

    S.priceAcc += dt;
    while (S.priceAcc >= 620) { S.priceAcc -= 620; priceTick(); }

    S.newsTimer -= dt;
    if (S.newsTimer <= 0) {
      newsTick();
      var cfg = S.opts.difficulty === 'calme' ? [34000, 46000]
        : S.opts.difficulty === 'chaos' ? [12000, 18000] : [20000, 28000];
      S.newsTimer = rand(cfg[0], cfg[1]);
    }

    var v = portfolioValue();
    if (v > S.peak) S.peak = v;
    var dd = (S.peak - v) / S.peak;
    if (dd > S.maxDD) S.maxDD = dd;
    S.valueHist.push(v / S.capital);
    S.benchHist.push(benchLevel() / S.benchStart);
    if (S.valueHist.length > 4000) { S.valueHist.shift(); S.benchHist.shift(); }

    if (S.ms >= S.opts.roundSec * 1000) endRound();
  }

  function start() {
    S.phase = 'live'; S.running = true; S.paused = false; S.ms = 0;
  }
  function endRound() {
    S.phase = 'done';
    S.running = false;
    emit('roundEnd', { score: score() });
  }

  /* ---------------------------------------------------------------- score */
  function score() {
    var ret = portfolioReturn();
    var alp = alpha();
    var bench = benchReturn();
    var v = portfolioValue();

    // 55 % : alpha vs benchmark (l'égal-pondéré des 5 lignes)
    var alphaScore = clamp(50 + (alp / 0.006) * 50, 0, 100);

    // 25 % : risque — drawdown + concentration
    var conc = 0;
    S.stocks.forEach(function (st) { conc = Math.max(conc, Math.abs(st.pos * st.mid) / Math.max(1, v)); });
    var riskScore = clamp(100 - (S.maxDD / 0.012) * 65 - Math.max(0, conc - 0.35) * 120, 0, 100);

    // 10 % : activité — il faut prendre des décisions
    var actScore = S.trades === 0 ? 0 : clamp(30 + S.trades * 7, 0, 100);

    // 10 % : discipline — pas de trades géants, pas de cash drag, pas de levier
    var expo = investedValue() / Math.max(1, v);
    var discScore = clamp(100 - S.oversize * 22
      - Math.max(0, expo - 0.98) * 200
      - Math.max(0, 0.65 - expo) * 90, 0, 100);

    var total = 0.55 * alphaScore + 0.25 * riskScore + 0.10 * actScore + 0.10 * discScore;
    return {
      total: Math.round(total * 10) / 10,
      alphaScore: Math.round(alphaScore),
      risk: Math.round(riskScore),
      activity: Math.round(actScore),
      discipline: Math.round(discScore),
      grade: total >= 85 ? 'A' : total >= 70 ? 'B' : total >= 55 ? 'C' : total >= 40 ? 'D' : 'E',
      metrics: {
        value: v,
        pnl: v - S.capital,
        ret: ret,
        bench: bench,
        alpha: alp,
        cash: S.cash,
        exposure: investedValue() / Math.max(1, v),
        maxDD: S.maxDD,
        concentration: conc,
        trades: S.trades,
        fees: S.fees,
        oversize: S.oversize
      }
    };
  }

  function fixes(sc) {
    var m = sc.metrics, out = [];
    if (m.trades === 0) out.push('Tu n\'as <b>rien tradé</b> : un gérant doit prendre des décisions. 3 à 8 positions sur la session.');
    if (m.alpha < 0) out.push('Alpha <b>négatif (' + (m.alpha * 100).toFixed(2) + ' %)</b> : tu as acheté après le mouvement au lieu d\'anticiper la news. Achète la bonne nouvelle <b>dans les 5 secondes</b>.');
    if (m.alpha > 0.002) out.push('Alpha <b>+' + (m.alpha * 100).toFixed(2) + ' %</b> : tu battrais le marché. Garde ce rythme de lecture des headlines.');
    if (m.maxDD > 0.008) out.push('Drawdown max <b>' + (m.maxDD * 100).toFixed(1) + ' %</b> : tu gardes trop longtemps une position qui va contre toi. Coupe vite.');
    if (m.concentration > 0.4) out.push('Concentration <b>' + Math.round(m.concentration * 100) + ' %</b> sur une ligne : 25 % max par titre, sinon un seul headline te tue.');
    if (m.exposure < 0.4) out.push('Tu es <b>' + Math.round(m.exposure * 100) + ' %</b> investi : trop de cash, tu ne captures pas le beta. Vise 70–95 %.');
    if (m.exposure > 1.02) out.push('Exposition <b>>100 %</b> : tu es en levier, ça multiplie le risque sans être demandé.');
    if (m.fees > 8000) out.push('Frais d\'exécution <b>' + Math.round(m.fees) + ' $</b> : tu trades trop gros / trop souvent. Blocs de 250k–1M.');
    if (!out.length) out.push('Profil propre : alpha positif, risque maîtrisé. Rejoue en <b>Chaos</b> pour valider.');
    return out.slice(0, 4);
  }

  function toast(text, kind) { emit('toast', { text: text, kind: kind || 'info' }); }

  var api = {
    init: init,
    start: start,
    step: step,
    trade: trade,
    sellAll: sellAll,
    score: score,
    fixes: fixes,
    on: function (fn) { if (S) S.listeners.push(fn); return api; },
    get: function () { return S; },
    stock: stock,
    market: market,
    slipBps: slipBps,
    portfolioValue: portfolioValue,
    investedValue: investedValue,
    portfolioReturn: portfolioReturn,
    benchReturn: benchReturn,
    alpha: alpha,
    fmtClock: fmtClock,
    toast: toast
  };

  global.EngineAM = api;
})(window);
