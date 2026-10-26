/* ==========================================================================
   AMPLIFYME TRAINER — simulation engine
   Pure logic, no DOM. Exposed as window.Engine.
   ========================================================================== */
(function (global) {
  'use strict';

  var COMM_BPS = 8;              // commission client, en bps du notionnel
  var MARKET_HALF_BPS = 3.2;     // demi-spread du carnet (chaque côté)
  var POS_LIMIT = 100000;        // limite par ligne
  var TICK = 0.01;

  var STOCK_DEFS = [
    { t: 'BABA', name: 'Alibaba ADR', ref: 483.99, vol: 1.00 },
    { t: 'MSFT', name: 'Microsoft', ref: 515.43, vol: 0.95 },
    { t: 'VW',   name: 'Volkswagen', ref: 49.55,  vol: 1.10 },
    { t: 'HSBC', name: 'HSBC Holdings', ref: 39.01, vol: 1.15 },
    { t: 'BP',   name: 'BP plc', ref: 37.73,  vol: 1.20 }
  ];

  var CLIENTS = [
    { id: 'HF1', label: 'HF1 — 123 4547 89 00', short: 'HF1', trust: 74 },
    { id: 'HF2', label: 'HF2 — 987 2210 44 10', short: 'HF2', trust: 70 },
    { id: 'HF3', label: 'HF3 — 552 8891 03 77', short: 'HF3', trust: 66 }
  ];

  var NEWS_POOL = [
    { tag: 'MACRO', text: 'US Government announce a record breaking $2 trillion economic rescue package.', all: 1,  mag: 0.0075 },
    { tag: 'MACRO', text: 'Fed signals faster-than-expected rate cuts as inflation cools.', all: 1,  mag: 0.0060 },
    { tag: 'MACRO', text: 'US inflation print comes in hotter than expected. Risk-off across equities.', all: -1, mag: 0.0068 },
    { tag: 'MACRO', text: 'Middle East tensions escalate — oil rallies, risk assets sell off.', all: -1, mag: 0.0080, oil: 1 },
    { tag: 'MACRO', text: 'Surprise China stimulus package announced overnight.', all: 1, mag: 0.0055, china: 1 },
    { tag: 'MACRO', text: 'UK Government cuts the bank windfall tax as the UK recovers faster than expected.', all: 0.4, mag: 0.0060, banks: 1 },
    { tag: 'BABA', text: 'Alibaba: Chinese regulators approve a new cross-border e-commerce framework.', target: 'BABA', dir: 1, mag: 0.013 },
    { tag: 'BABA', text: 'Alibaba: ADR delisting concerns resurface after a US audit setback.', target: 'BABA', dir: -1, mag: 0.014 },
    { tag: 'BABA', text: 'Alibaba beats on cloud revenue, announces $4bn buyback.', target: 'BABA', dir: 1, mag: 0.011 },
    { tag: 'MSFT', text: 'Microsoft announce they are in the final stages of purchasing TikTok\'s US operations.', target: 'MSFT', dir: 1, mag: 0.009 },
    { tag: 'MSFT', text: 'US President signals his approval of the Microsoft / TikTok US deal.', target: 'MSFT', dir: 1, mag: 0.007 },
    { tag: 'MSFT', text: 'Microsoft: Azure outage affects enterprise customers across three regions.', target: 'MSFT', dir: -1, mag: 0.008 },
    { tag: 'MSFT', text: 'Microsoft guides Q4 cloud revenue below consensus.', target: 'MSFT', dir: -1, mag: 0.010 },
    { tag: 'VW',   text: 'VW announces a new battery supplier to coincide with 5-star reviews for its new SUV.', target: 'VW', dir: 1, mag: 0.012 },
    { tag: 'VW',   text: 'VW recalls 120,000 vehicles over a software fault in the brake system.', target: 'VW', dir: -1, mag: 0.013 },
    { tag: 'VW',   text: 'EU delays the combustion engine ban — autos rally.', target: 'VW', dir: 1, mag: 0.010 },
    { tag: 'HSBC', text: 'HSBC CEO resigns with immediate effect. UK Gov announces full enquiry into money laundering scandal.', target: 'HSBC', dir: -1, mag: 0.016 },
    { tag: 'HSBC', text: 'HSBC announces a $2bn share buyback after a strong capital print.', target: 'HSBC', dir: 1, mag: 0.010 },
    { tag: 'HSBC', text: 'HSBC credit rating outlook cut to negative by a major agency.', target: 'HSBC', dir: -1, mag: 0.011 },
    { tag: 'BP',   text: 'BP announces a major oil discovery in the North Sea.', target: 'BP', dir: 1, mag: 0.013 },
    { tag: 'BP',   text: 'BP: fire at a major refinery forces a 15% output cut.', target: 'BP', dir: -1, mag: 0.014 },
    { tag: 'BP',   text: 'OPEC+ announces surprise production cuts — crude rallies.', target: 'BP', dir: 1, mag: 0.012 },
    { tag: 'BP',   text: 'BP takes a $1.2bn impairment charge on its downstream business.', target: 'BP', dir: -1, mag: 0.009 }
  ];

  var S = null;

  /* ---------------------------------------------------------------- utils */
  function rand(a, b) { return a + Math.random() * (b - a); }
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function mean(a) { return a.length ? a.reduce(function (x, y) { return x + y; }, 0) / a.length : 0; }
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

  /* ---------------------------------------------------------------- events */
  function emit(type, data) {
    if (!S) return;
    for (var i = 0; i < S.listeners.length; i++) {
      try { S.listeners[i](type, data); } catch (e) { console.error(e); }
    }
  }

  /* ---------------------------------------------------------------- init */
  function init(opts) {
    opts = Object.assign({
      rounds: 2,
      roundSec: 180,
      difficulty: 'normal',
      wheels: true,
      sound: true
    }, opts || {});

    S = {
      opts: opts,
      stocks: STOCK_DEFS.map(function (d) {
        return {
          t: d.t, name: d.name, ref: d.ref, vol: d.vol,
          mid: d.ref, pos: 0, avg: 0, realised: 0,
          hist: [d.ref], drift: 0, lastDir: 0
        };
      }),
      clients: CLIENTS.map(function (c) { return Object.assign({}, c); }),
      chat: { DEAL: [], HF1: [], HF2: [], HF3: [] },
      news: [],
      quotes: [],
      rfqs: [],
      blotter: [],
      listeners: [],
      round: 1,
      phase: 'idle',            // idle | live | roundEnd | done
      running: false,
      paused: false,
      ms: 0,
      elapsedMs: 0,
      clockMs: 0,
      priceAcc: 0,
      rfqTimer: 4200,
      newsTimer: 12000,
      rfqSeq: 1,
      quoteSeq: 1,
      commission: 0,
      ffc: 0,
      trades: 0,
      answered: 0,
      missed: 0,
      rfqTotal: 0,
      respTimes: [],
      sniped: 0,
      newsSeq: 0,
      settlementCost: 0,
      riskSum: 0,
      riskTime: 0,
      breachMs: 0,
      maxUtil: 0,
      roundRiskSum: 0,
      roundRiskTime: 0,
      snap: null,
      roundLog: [],
      timers: []
    };

    bootChat();
    return api;
  }

  function bootChat() {
    push('DEAL', 'SYS', 'Welcome to the Investment Bank simulation — Single User Mode / all roles.');
    push('DEAL', 'SYS', 'Round 1 of the simulation has now started.');
    push('HF1', 'SYS', 'You are on the desk. Clients will ask you for two-way prices.');
  }

  function push(channel, from, text, kind) {
    var msg = { from: from, text: text, t: S.ms, clock: fmtClock(S.clockMs), kind: kind || 'normal' };
    (S.chat[channel] || (S.chat[channel] = [])).push(msg);
    if (S.chat[channel].length > 200) S.chat[channel].shift();
    emit('chat', { channel: channel, msg: msg });
    return msg;
  }

  /* ---------------------------------------------------------------- stocks */
  function stock(t) {
    for (var i = 0; i < S.stocks.length; i++) if (S.stocks[i].t === t) return S.stocks[i];
    return null;
  }

  function halfSpreadBps(st) {
    var extra = S.opts.difficulty === 'chaos' ? 1.4 : S.opts.difficulty === 'calme' ? -0.4 : 0;
    return MARKET_HALF_BPS + extra;
  }

  function quoteMarket(st) {
    var hs = st.mid * halfSpreadBps(st) / 10000;
    return { bid: r2(st.mid - hs), offer: r2(st.mid + hs) };
  }

  function depthFor(t, side, qty) {
    var st = stock(t);
    if (!st) return null;
    var m = st.mid, hs = halfSpreadBps(st);
    var sgn = side === 'BUY' ? 1 : -1;
    var levels = [
      { px: r2(m * (1 + sgn * hs / 10000)), size: 25000 },
      { px: r2(m * (1 + sgn * (hs + 3) / 10000)), size: 45000 },
      { px: r2(m * (1 + sgn * (hs + 7) / 10000)), size: 80000 }
    ];
    var remaining = qty || 0, notional = 0, filled = 0, parts = [];
    for (var i = 0; i < levels.length && remaining > 0; i++) {
      var take = Math.min(remaining, levels[i].size);
      notional += take * levels[i].px;
      filled += take;
      remaining -= take;
      parts.push({ px: levels[i].px, qty: take });
    }
    if (remaining > 0) {
      var worst = levels[levels.length - 1].px * (1 + sgn * 0.0015);
      notional += remaining * worst;
      filled += remaining;
      parts.push({ px: r2(worst), qty: remaining });
    }
    return {
      side: side,
      avg: filled ? notional / filled : levels[0].px,
      levels: levels,
      parts: parts,
      slipBps: filled ? Math.abs(notional / filled - m) / m * 10000 : 0
    };
  }

  /* ---------------------------------------------------------------- price */
  function priceTick() {
    var diffMult = S.opts.difficulty === 'chaos' ? 1.7 : S.opts.difficulty === 'calme' ? 0.65 : 1;
    var sigma = 0.00042 * diffMult;
    S.stocks.forEach(function (st) {
      var r = st.drift + n2() * sigma * st.vol;
      st.drift *= 0.88;
      st.mid = Math.max(0.5, st.mid * (1 + r));
      st.hist.push(st.mid);
      if (st.hist.length > 900) st.hist.shift();
    });
  }

  /* ---------------------------------------------------------------- fills */
  function applyFill(st, ourSide, qty, price) {
    var signed = ourSide === 'BUY' ? qty : -qty;
    var oldPos = st.pos;
    var newPos = oldPos + signed;
    var realised = 0;
    if (oldPos !== 0 && (oldPos > 0) !== (signed > 0)) {
      var closed = Math.min(Math.abs(signed), Math.abs(oldPos));
      var dir = oldPos > 0 ? 1 : -1;
      realised = (price - st.avg) * closed * dir;
      st.realised += realised;
      if (Math.abs(signed) > Math.abs(oldPos)) st.avg = price;
    } else {
      var ao = Math.abs(oldPos), an = Math.abs(newPos);
      st.avg = an > 0 ? (st.avg * ao + price * qty) / an : 0;
    }
    if (newPos === 0) st.avg = 0;
    st.pos = newPos;
    return realised;
  }

  function clientFill(st, clientSide, qty, price, meta) {
    var ourSide = clientSide === 'BUY' ? 'SELL' : 'BUY';
    var notional = qty * price;
    var comm = notional * COMM_BPS / 10000;
    S.commission += comm;
    S.trades++;
    applyFill(st, ourSide, qty, price);
    S.blotter.unshift({
      t: S.ms, clock: fmtClock(S.clockMs), sec: st.t, side: ourSide,
      qty: qty, price: r2(price), notional: notional,
      src: meta && meta.src ? meta.src : 'CLIENT'
    });
    if (S.blotter.length > 300) S.blotter.pop();
    return { ourSide: ourSide, notional: notional, comm: comm };
  }

  /* ---------------------------------------------------------------- news */
  function spawnNews() {
    var pool = NEWS_POOL.slice();
    var n = pick(pool);
    var dirApplied = n.all ? n.all : n.dir;
    var impacts = {};

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
        st.mid = Math.max(0.5, st.mid * (1 + mag));
        st.drift += mag * 0.13;
        st.lastDir = mag > 0 ? 1 : -1;
        impacts[st.t] = mag * 10000;
      }
    });

    var item = {
      id: 'N' + (S.news.length + 1),
      tag: n.tag,
      text: n.text,
      dir: dirApplied,
      all: !!n.all,
      impacts: impacts,
      clock: fmtClock(S.clockMs),
      t: S.ms
    };
    S.newsSeq++;
    S.news.unshift(item);
    if (S.news.length > 60) S.news.pop();
    emit('news', item);
    push('DEAL', 'SYS', n.tag + ' — ' + n.text, 'alert');

    // A live quote left in the market becomes a free option for the client.
    var delay = S.opts.difficulty === 'chaos' ? 500 : 900;
    at(S.ms + delay, function () { snipeStaleQuotes(item); });
  }

  function snipeStaleQuotes(news) {
    if (!S || S.phase !== 'live') return;
    var maxSnipe = S.opts.difficulty === 'chaos' ? 3 : S.opts.difficulty === 'calme' ? 1 : 2;
    var count = 0;
    for (var i = 0; i < S.quotes.length && count < maxSnipe; i++) {
      var q = S.quotes[i];
      if (q.dead) continue;
      // seule une quote postée AVANT la dernière news est "stale"
      if (q.newsSeq >= S.newsSeq) continue;
      var st = stock(q.ticker);
      if (!st) continue;
      var m = st.mid;
      var hitBuy = q.offer < m * (1 - 0.0007);   // notre offer est devenue bon marché
      var hitSell = q.bid > m * (1 + 0.0007);    // notre bid est devenu cher
      if (!hitBuy && !hitSell) continue;
      var gap = Math.max(Math.abs(q.bid - m), Math.abs(q.offer - m)) / m;
      if (gap > 0.012) {
        // erreur évidente : le client ne tape pas, la ligne est retirée
        q.dead = true;
        push(q.client || 'DEAL', 'CLIENT', 'That price is miles off the market — pull it. I won\'t trade an obvious error.', 'alert');
        emit('busted', { ticker: st.t, quote: q });
        continue;
      }
      var clientSide = hitBuy ? 'BUY' : 'SELL';
      var price = hitBuy ? q.offer : q.bid;
      var qty = hitBuy ? q.offerVol : q.bidVol;
      qty = Math.min(qty, 60000, Math.max(500, Math.round(2500000 / price / 500) * 500));
      if (qty < 100) continue;
      q.dead = true;
      var client = q.client || pick(S.clients).id;
      var res = clientFill(st, clientSide, qty, price, { src: 'STALE' });
      S.sniped++;
      push(client, 'CLIENT', (clientSide === 'BUY'
        ? 'I\'ll take your offer — ' + fmtInt(qty) + ' ' + st.t + ' at ' + price.toFixed(2) + '.'
        : 'I\'ll hit your bid — ' + fmtInt(qty) + ' ' + st.t + ' at ' + price.toFixed(2) + '.'), 'alert');
      push('DEAL', 'SYS', 'Quote picked off on the ' + st.t + ' news. You were showing a stale price.', 'alert');
      emit('picked', { ticker: st.t, qty: qty, price: price, clientSide: clientSide, client: client, fill: res });
      toast('PICK-OFF — ' + fmtInt(qty) + ' ' + st.t + ' à ' + price.toFixed(2) + ' : ta quote était trop loin du nouveau mid.', 'bad');
      count++;
    }
  }

  /* ---------------------------------------------------------------- RFQ */
  function spawnRfq() {
    if (S.phase !== 'live') return;
    var open = S.rfqs.filter(function (r) { return r.status === 'open'; });
    if (open.length >= 3) { S.rfqTimer = 5000; return; }

    var client = pick(S.clients);
    var st = pick(S.stocks);
    var size = st.mid > 200 ? pick([1000, 2500, 5000])
      : st.mid > 60 ? pick([5000, 10000, 20000])
      : pick([10000, 25000, 50000]);
    var buyBias = st.lastDir >= 0 ? 0.62 : 0.38;
    if (Math.abs(st.lastDir) === 0) buyBias = 0.5;
    var side = Math.random() < buyBias ? 'BUY' : 'SELL';
    var hint = Math.random() < 0.35;

    var rfq = {
      id: 'R' + (S.rfqSeq++),
      client: client.id,
      ticker: st.t,
      size: size,
      side: side,
      hint: hint,
      createdAt: S.ms,
      deadline: S.ms + 20000,
      status: 'open',
      attempts: 0,
      quoted: false,
      quotedAt: 0,
      decideAt: 0
    };
    S.rfqs.push(rfq);
    if (S.rfqs.length > 40) S.rfqs.shift();
    S.rfqTotal++;

    var text;
    if (hint) {
      text = side === 'BUY'
        ? 'I\'m a buyer of ' + fmtInt(size) + ' ' + st.t + ' — can you show me a price?'
        : 'I need to sell ' + fmtInt(size) + ' ' + st.t + ' — what\'s your bid?';
    } else {
      text = 'Can you make me a price for ' + fmtInt(size) + ' ' + st.t + ' please?';
    }
    push(client.id, 'CLIENT', text, 'rfq');
    emit('rfq', rfq);
    toast('RFQ ' + client.id + ' · ' + fmtInt(size) + ' ' + st.t + ' · 20 s pour quoter', 'warn');

    var mult = S.round > 1 ? 0.82 : 1;
    var cfg = S.opts.difficulty === 'calme' ? [13500, 19000]
      : S.opts.difficulty === 'chaos' ? [6500, 10000] : [9500, 14500];
    S.rfqTimer = rand(cfg[0], cfg[1]) * mult;
  }

  function expireRfqs() {
    S.rfqs.forEach(function (r) {
      if (r.status === 'open' && S.ms >= r.deadline) {
        r.status = 'missed';
        S.missed++;
        var c = clientById(r.client);
        if (c) c.trust = clamp(c.trust - 9, 0, 100);
        push(r.client, 'CLIENT', 'Forget it — I\'ll go elsewhere.', 'alert');
        toast('RFQ manquée — ' + r.client + ' · ' + fmtInt(r.size) + ' ' + r.ticker + ' sans réponse', 'bad');
        emit('missed', r);
      }
    });
  }

  function clientById(id) {
    for (var i = 0; i < S.clients.length; i++) if (S.clients[i].id === id) return S.clients[i];
    return null;
  }

  /* ---------------------------------------------------------------- quotes */
  function sendQuote(p) {
    if (!S || S.phase !== 'live') return { ok: false, error: 'Marché fermé' };
    var st = stock(p.ticker);
    if (!st) return { ok: false, error: 'Ticker inconnu' };

    var bid = Number(p.bid), offer = Number(p.offer);
    var bv = Math.round(Number(p.bidVol)), ov = Math.round(Number(p.offerVol));
    var valid = clamp(Number(p.valid) || 45, 5, 120);

    if (!isFinite(bid) || !isFinite(offer) || bid <= 0 || offer <= 0) {
      return { ok: false, error: 'Prix manquant ou invalide' };
    }
    if (bid >= offer) {
      S.ffc++;
      return { ok: false, error: 'Bid ≥ Offer — marché croisé (Fat Finger)', ffc: true };
    }
    if (!isFinite(bv) || !isFinite(ov) || bv < 100 || ov < 100) {
      return { ok: false, error: 'Volume minimum : 100 actions' };
    }
    if (bv > 500000 || ov > 500000) {
      S.ffc++;
      return { ok: false, error: 'Volume > 500 000 — Fat Finger bloqué', ffc: true };
    }
    var dev = Math.max(Math.abs(bid - st.mid), Math.abs(offer - st.mid)) / st.mid;
    if (dev > 0.08) {
      S.ffc++;
      return { ok: false, error: 'Prix à ' + (dev * 100).toFixed(1) + '% du mid — Fat Finger bloqué', ffc: true };
    }

    var openRfq = null;
    for (var i = S.rfqs.length - 1; i >= 0; i--) {
      if (S.rfqs[i].status === 'open' && S.rfqs[i].ticker === p.ticker) { openRfq = S.rfqs[i]; break; }
    }

    if (openRfq && Math.max(bv, ov) >= openRfq.size * 2.5) {
      S.ffc++;
      toast('Volume ' + fmtInt(Math.max(bv, ov)) + ' pour une demande de ' + fmtInt(openRfq.size) + ' — fat finger ?', 'warn');
    }

    var quote = {
      id: 'Q' + (S.quoteSeq++),
      ticker: p.ticker,
      midAtQuote: st.mid,
      newsSeq: S.newsSeq,
      bid: r2(bid),
      offer: r2(offer),
      bidVol: bv,
      offerVol: ov,
      valid: valid,
      createdAt: S.ms,
      expiresAt: S.ms + valid * 1000,
      client: openRfq ? openRfq.client : null,
      rfqId: openRfq ? openRfq.id : null,
      dead: false
    };
    S.quotes.push(quote);

    if (openRfq) {
      if (!openRfq.quoted) {
        openRfq.quoted = true;
        openRfq.quotedAt = S.ms;
        S.answered++;
        S.respTimes.push(S.ms - openRfq.createdAt);
        var c = clientById(openRfq.client);
        if (c) {
          var secs = (S.ms - openRfq.createdAt) / 1000;
          c.trust = clamp(c.trust + (secs <= 6 ? 4 : secs <= 12 ? 1 : -2), 0, 100);
        }
      }
      openRfq.status = 'quoted';
      openRfq.decideAt = S.ms + rand(1700, 3800);
    }

    push(openRfq ? openRfq.client : 'DEAL', 'ME',
      'Quote: ' + p.ticker + ' bid ' + quote.bid.toFixed(2) + ' / offer ' + quote.offer.toFixed(2) +
      ' — ' + fmtInt(bv) + ' x ' + fmtInt(ov) + ', valid ' + valid + 's', 'normal');
    emit('quote', quote);
    return { ok: true, quote: quote, rfq: openRfq };
  }

  function cancelQuote(id) {
    for (var i = 0; i < S.quotes.length; i++) {
      if (S.quotes[i].id === id && !S.quotes[i].dead) {
        S.quotes[i].dead = true;
        emit('quoteCancel', S.quotes[i]);
        return true;
      }
    }
    return false;
  }

  function cancelAll() {
    var n = 0;
    S.quotes.forEach(function (q) { if (!q.dead) { q.dead = true; n++; } });
    if (n) { emit('quoteCancelAll', n); toast(n + ' quote(s) annulée(s).', 'good'); }
    return n;
  }

  function liveQuotes() {
    return S.quotes.filter(function (q) { return !q.dead && q.expiresAt > S.ms; });
  }

  /* ---------------------------------------------------------------- client reaction */
  function processClientDecisions() {
    S.rfqs.forEach(function (rfq) {
      if (rfq.status !== 'quoted' || !rfq.decideAt) return;
      if (S.ms < rfq.decideAt) return;
      rfq.decideAt = 0;
      var q = null;
      for (var i = S.quotes.length - 1; i >= 0; i--) {
        if (S.quotes[i].rfqId === rfq.id && !S.quotes[i].dead) { q = S.quotes[i]; break; }
      }
      if (!q || q.expiresAt <= S.ms) {
        rfq.status = 'expired-quote';
        push(rfq.client, 'CLIENT', 'Your quote has expired — I need a fresh price.', 'alert');
        return;
      }
      decide(rfq, q);
    });
  }

  function decide(rfq, q) {
    var st = stock(rfq.ticker);
    var side = rfq.side;
    var px = side === 'BUY' ? q.offer : q.bid;
    var vol = side === 'BUY' ? q.offerVol : q.bidVol;
    var client = clientById(rfq.client);
    var trust = client ? client.trust : 60;

    // Le client juge le prix par rapport au marché au moment de la quote.
    var mid = q.midAtQuote || st.mid;
    var movedBps = Math.abs(st.mid - mid) / mid * 10000;
    if (movedBps > 8) {
      rfq.status = 'open';
      rfq.deadline = S.ms + 9000;
      rfq.decideAt = 0;
      push(rfq.client, 'CLIENT', 'Your price is off the market — send me a fresh one.', 'alert');
      toast('Le marché a bougé de ' + movedBps.toFixed(0) + ' bps depuis ta quote. Reprice-la.', 'warn');
      emit('stale', { rfq: rfq, quote: q, movedBps: movedBps });
      return;
    }

    var fairHalf = 0.0005 + (S.opts.difficulty === 'chaos' ? 0.0002 : 0);
    var fair = side === 'BUY' ? mid * (1 + fairHalf) : mid * (1 - fairHalf);
    var edgeBps = (side === 'BUY' ? (fair - px) : (px - fair)) / mid * 10000;
    var giftBps = (side === 'BUY' ? (mid - px) : (px - mid)) / mid * 10000;

    var p;
    if (giftBps > 1) p = 0.99;
    else if (edgeBps >= 6) p = 0.94;
    else if (edgeBps >= 0) p = 0.80;
    else if (edgeBps >= -6) p = 0.54;
    else if (edgeBps >= -14) p = 0.24;
    else p = 0.05;
    p += (trust - 70) / 900;

    if (vol < rfq.size * 0.3) {
      rfq.status = 'rejected';
      push(rfq.client, 'CLIENT', 'You\'re only showing ' + fmtInt(vol) + ' on a ' + fmtInt(rfq.size) + ' order? Not helpful.', 'alert');
      if (client) client.trust = clamp(client.trust - 4, 0, 100);
      emit('pass', { rfq: rfq, quote: q, reason: 'size' });
      return;
    }

    if (Math.random() > p) {
      // pass / ask to tighten — la quote reste vivante tant que tu ne l'annules pas
      if (edgeBps < -14) {
        rfq.status = 'rejected';
        push(rfq.client, 'CLIENT', 'That\'s way too wide. Your offer is off the market.', 'alert');
        if (client) client.trust = clamp(client.trust - 3, 0, 100);
        emit('pass', { rfq: rfq, quote: q, reason: 'wide' });
      } else if (rfq.attempts < 1 && Math.random() < 0.4) {
        rfq.attempts++;
        rfq.status = 'open';
        rfq.deadline = S.ms + 9000;
        push(rfq.client, 'CLIENT', 'Can you tighten that? I\'m still working the order.', 'alert');
        emit('tighten', { rfq: rfq });
      } else {
        rfq.status = 'rejected';
        push(rfq.client, 'CLIENT', 'Your price is too wide for me, I\'ll pass.', 'normal');
        toast('Le client passe. Ta quote reste en vie : annule-la avec X.', 'warn');
        emit('pass', { rfq: rfq, quote: q, reason: 'wide' });
      }
      return;
    }

    // ---- trade
    q.dead = true;
    var qty = Math.min(vol, rfq.size);
    var res = clientFill(st, side, qty, px, { src: 'CLIENT' });
    rfq.status = 'done';

    if (giftBps > 3) {
      S.ffc++;
      toast('Prix sous le mid de ' + giftBps.toFixed(0) + ' bps — tu as payé le spread au client (FFC).', 'bad');
    }

    push(rfq.client, 'CLIENT',
      (side === 'BUY' ? 'Done — I bought ' : 'Done — I sold ') + fmtInt(qty) + ' ' + st.t +
      ' at ' + px.toFixed(2) + '. Thanks.', 'normal');
    push('DEAL', 'SYS',
      rfq.client + ' ' + (side === 'BUY' ? 'bought ' : 'sold ') + fmtInt(qty) + ' ' + st.t + ' at ' + px.toFixed(2) +
      '. Your position is now ' + fmtSigned(st.pos) + '.', 'normal');
    emit('fill', {
      rfq: rfq, quote: q, ticker: st.t, side: side, qty: qty, price: px,
      ourSide: res.ourSide, notional: res.notional, comm: res.comm, pos: st.pos
    });
    toast('FILL ' + (side === 'BUY' ? 'client achète' : 'client vend') + ' ' + fmtInt(qty) + ' ' + st.t +
      ' @ ' + px.toFixed(2) + ' · position ' + fmtSigned(st.pos), 'good');
  }

  /* ---------------------------------------------------------------- hedging */
  function hedge(ticker, side, qty) {
    if (!S || S.phase !== 'live') return { ok: false, error: 'Marché fermé' };
    var st = stock(ticker);
    if (!st) return { ok: false, error: 'Ticker inconnu' };
    qty = Math.round(Number(qty));
    if (!isFinite(qty) || qty <= 0) return { ok: false, error: 'Quantité invalide' };

    var newPos = st.pos + (side === 'BUY' ? qty : -qty);
    if (Math.abs(newPos) > POS_LIMIT && Math.abs(newPos) > Math.abs(st.pos)) {
      return { ok: false, error: 'Limite de risque : ' + fmtInt(POS_LIMIT) + ' par ligne. Réduis d\'abord.' };
    }

    var d = depthFor(ticker, side, qty);
    applyFill(st, side, qty, d.avg);
    S.blotter.unshift({
      t: S.ms, clock: fmtClock(S.clockMs), sec: st.t, side: side, qty: qty,
      price: r2(d.avg), notional: qty * d.avg, src: 'EXCH'
    });
    if (S.blotter.length > 300) S.blotter.pop();

    // market impact
    var imp = (qty / 100000) * 0.00022;
    st.mid = Math.max(0.5, st.mid * (1 + (side === 'BUY' ? imp : -imp)));
    st.hist.push(st.mid);

    emit('hedge', { ticker: ticker, side: side, qty: qty, price: d.avg, pos: st.pos, slip: d.slipBps });
    return { ok: true, price: d.avg, pos: st.pos, slip: d.slipBps };
  }

  function flatten(ticker) {
    var st = stock(ticker);
    if (!st) return { ok: false, error: 'Ticker inconnu' };
    if (st.pos === 0) return { ok: false, error: 'Déjà flat' };
    var side = st.pos > 0 ? 'SELL' : 'BUY';
    return hedge(ticker, side, Math.abs(st.pos));
  }

  function flattenAll() {
    var n = 0;
    S.stocks.forEach(function (st) { if (st.pos !== 0) { flatten(st.t); n++; } });
    if (n) toast('Flat sur ' + n + ' ligne(s).', 'good');
    return n;
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

    S.rfqTimer -= dt;
    if (S.rfqTimer <= 0) spawnRfq();

    S.newsTimer -= dt;
    if (S.newsTimer <= 0) {
      spawnNews();
      var cfg = S.opts.difficulty === 'calme' ? [38000, 52000]
        : S.opts.difficulty === 'chaos' ? [14000, 21000] : [23000, 33000];
      S.newsTimer = rand(cfg[0], cfg[1]) * (S.round > 1 ? 0.8 : 1);
    }

    processClientDecisions();
    expireRfqs();

    // quote expiry
    S.quotes.forEach(function (q) {
      if (!q.dead && S.ms >= q.expiresAt) {
        q.dead = true;
        emit('quoteExpired', q);
      }
    });

    // risk sampling
    var util = 0;
    S.stocks.forEach(function (st) { util = Math.max(util, Math.abs(st.pos) / POS_LIMIT); });
    S.riskSum += util * dt;
    S.riskTime += dt;
    S.roundRiskSum += util * dt;
    S.roundRiskTime += dt;
    if (util > S.maxUtil) S.maxUtil = util;
    if (util > 1) S.breachMs += dt;

    // deferred timers
    if (S.timers.length) {
      var due = S.timers.filter(function (x) { return x.at <= S.ms; });
      S.timers = S.timers.filter(function (x) { return x.at > S.ms; });
      due.forEach(function (x) { try { x.fn(); } catch (e) { console.error(e); } });
    }

    if (S.ms >= S.opts.roundSec * 1000) endRound();
  }

  function at(ms, fn) { S.timers.push({ at: ms, fn: fn }); }

  /* ---------------------------------------------------------------- rounds */
  function start() {
    if (!S) return;
    S.phase = 'live';
    S.running = true;
    S.paused = false;
    S.ms = 0;
    S.snap = snapshot();
  }

  function nextRound() {
    if (!S) return;
    S.round++;
    S.ms = 0;
    S.phase = 'live';
    S.running = true;
    S.paused = false;
    S.quotes = [];
    S.rfqs = S.rfqs.filter(function (r) { return r.status === 'open'; });
    S.rfqs.forEach(function (r) { r.status = 'closed'; });
    S.rfqs = [];
    S.timers = [];
    S.rfqTimer = 3800;
    S.newsTimer = 8000;
    S.roundRiskSum = 0;
    S.roundRiskTime = 0;
    S.snap = snapshot();
    push('DEAL', 'SYS', 'Round ' + S.round + ' of the simulation has now started.', 'normal');
    emit('roundStart', { round: S.round });
  }

  function snapshot() {
    return {
      commission: S.commission, trades: S.trades, ffc: S.ffc, answered: S.answered,
      missed: S.missed, rfqTotal: S.rfqTotal, sniped: S.sniped,
      realised: totalRealised(), clockMs: S.clockMs
    };
  }

  function endRound() {
    if (S.phase !== 'live') return;
    S.phase = 'roundEnd';
    S.running = false;

    var closeCost = 0, openLines = [];
    S.stocks.forEach(function (st) {
      if (st.pos !== 0) {
        var mark = (st.mid - st.avg) * st.pos;
        var cost = Math.abs(st.pos) * st.mid * 0.0002;
        st.realised += mark - cost;
        closeCost += cost;
        openLines.push({ t: st.t, pos: st.pos });
        st.pos = 0;
        st.avg = 0;
      }
    });
    S.settlementCost += closeCost;
    S.quotes = [];
    S.rfqs.forEach(function (r) { if (r.status === 'open') { r.status = 'closed'; } });

    push('DEAL', 'SYS', 'Round ' + S.round + ' of the simulation has now ended.', 'alert');

    var roundStats = {
      round: S.round,
      trades: S.trades - (S.snap ? S.snap.trades : 0),
      commission: S.commission - (S.snap ? S.snap.commission : 0),
      ffc: S.ffc - (S.snap ? S.snap.ffc : 0),
      rfqTotal: S.rfqTotal - (S.snap ? S.snap.rfqTotal : 0),
      answered: S.answered - (S.snap ? S.snap.answered : 0),
      sniped: S.sniped - (S.snap ? S.snap.sniped : 0),
      closeCost: closeCost,
      openLines: openLines,
      avgUtil: S.roundRiskTime ? S.roundRiskSum / S.roundRiskTime : 0
    };
    S.roundLog.push(roundStats);

    if (S.round >= S.opts.rounds) S.phase = 'done';
    emit('roundEnd', { roundStats: roundStats, score: score(), isLast: S.round >= S.opts.rounds });
  }

  /* ---------------------------------------------------------------- P&L / score */
  function totalRealised() {
    return S.stocks.reduce(function (a, st) { return a + st.realised; }, 0);
  }
  function totalUnrealised() {
    return S.stocks.reduce(function (a, st) { return a + st.pos * (st.mid - st.avg); }, 0);
  }
  function totalPnl() {
    return totalRealised() + totalUnrealised() + S.commission;
  }

  function score() {
    var scale = Math.max(0.4, Math.min(4, S.elapsedMs / 180000));
    var commTarget = 15500 * scale;
    var pnlTarget = 5000 * scale;
    var pnl = totalPnl();
    var commScore = clamp(S.commission / commTarget * 100, 0, 100);
    var pnlScore = clamp(50 + (pnl / pnlTarget) * 50, 0, 100);
    var avgUtil = S.riskTime ? S.riskSum / S.riskTime : 0;
    var riskScore = clamp(100 - avgUtil * 105 - (S.breachMs / 1000) * 1.4, 0, 100);
    var answeredRatio = S.rfqTotal ? S.answered / S.rfqTotal : 1;
    var avgResp = S.respTimes.length ? mean(S.respTimes) / 1000 : 0;
    var speedScore = S.respTimes.length ? clamp(100 - Math.max(0, avgResp - 4) * 6.5, 0, 100) : 100;
    var trust = mean(S.clients.map(function (c) { return c.trust; }));
    var relScore = clamp(answeredRatio * 52 + speedScore * 0.28 + trust * 0.20, 0, 100);
    var ffcScore = clamp(100 - 16 * S.ffc, 0, 100);

    var total = 0.30 * commScore + 0.25 * pnlScore + 0.20 * riskScore + 0.15 * relScore + 0.10 * ffcScore;

    return {
      total: Math.round(total * 10) / 10,
      comm: Math.round(commScore),
      pnlScore: Math.round(pnlScore),
      risk: Math.round(riskScore),
      rel: Math.round(relScore),
      ffcScore: Math.round(ffcScore),
      grade: total >= 85 ? 'A' : total >= 70 ? 'B' : total >= 55 ? 'C' : total >= 40 ? 'D' : 'E',
      metrics: {
        pnl: pnl,
        realised: totalRealised(),
        unrealised: totalUnrealised(),
        commission: S.commission,
        trades: S.trades,
        numt: S.trades,
        ffc: S.ffc,
        ssrm: Math.round(riskScore),
        avgUtil: avgUtil,
        breachSec: Math.round(S.breachMs / 1000),
        rfqTotal: S.rfqTotal,
        answered: S.answered,
        missed: S.missed,
        answeredRatio: answeredRatio,
        avgResp: avgResp,
        trust: trust,
        sniped: S.sniped,
        settlement: S.settlementCost,
        maxUtil: S.maxUtil
      },
      targets: { comm: commTarget, pnl: pnlTarget }
    };
  }

  function fixes(sc) {
    var out = [];
    var m = sc.metrics;
    if (m.answeredRatio < 0.9) out.push('Réponds à <b>100 % des RFQ</b> : ' + m.answered + '/' + m.rfqTotal + ' répondues, ' + m.missed + ' manquées. Chaque RFQ ignorée coupe le flux et la relation.');
    if (m.ffc > 0) out.push('<b>' + m.ffc + ' fat finger(s)</b> : vérifie bid &lt; offer, un volume de 10k–75k, et un prix à moins de 2 % du mid avant d\'envoyer.');
    if (m.sniped > 0) out.push('<b>' + m.sniped + ' pick-off(s)</b> : annule tes quotes (<kbd>X</kbd>) dès qu\'une news tombe, puis reprice. Une quote en vie est une option gratuite pour le client.');
    if (m.maxUtil > 0.85) out.push('Exposition max <b>' + Math.round(m.maxUtil * 100) + '%</b> de la limite : hedges plus tôt, par blocs de 25–50k.');
    if (m.avgResp > 10) out.push('Temps de réponse moyen <b>' + m.avgResp.toFixed(1) + ' s</b> : vise moins de 8 s. Le client part ailleurs après 20 s.');
    if (m.trades < Math.max(4, Math.round(m.rfqTotal * 0.5))) out.push('Seulement <b>' + m.trades + ' trades</b> pour ' + m.rfqTotal + ' RFQ : ton spread est trop large. 8–12 bps, pas 30.');
    if (m.commission < sc.targets.comm * 0.5) out.push('Commission <b>faible</b> : plus de flux client = plus de COMM. Priorité au taux de réponse avant le P&amp;L.');
    if (!out.length) out.push('Rien de structurel. Rejoue en <b>Chaos</b> et sans roues stabilisatrices pour verrouiller les réflexes.');
    return out.slice(0, 4);
  }

  function toast(text, kind) { emit('toast', { text: text, kind: kind || 'info' }); }

  function fmtInt(n) { return Math.round(n).toLocaleString('en-US'); }
  function fmtSigned(n) { return (n > 0 ? '+' : '') + fmtInt(n); }

  /* ---------------------------------------------------------------- API */
  var api = {
    init: init,
    start: start,
    step: step,
    nextRound: nextRound,
    sendQuote: sendQuote,
    cancelQuote: cancelQuote,
    cancelAll: cancelAll,
    hedge: hedge,
    flatten: flatten,
    flattenAll: flattenAll,
    score: score,
    fixes: fixes,
    on: function (fn) { if (S) S.listeners.push(fn); return api; },
    get: function () { return S; },
    stock: stock,
    quoteMarket: quoteMarket,
    depthFor: depthFor,
    liveQuotes: liveQuotes,
    totalPnl: totalPnl,
    totalRealised: totalRealised,
    totalUnrealised: totalUnrealised,
    fmtClock: fmtClock,
    fmtInt: fmtInt,
    fmtSigned: fmtSigned,
    POS_LIMIT: POS_LIMIT,
    COMM_BPS: COMM_BPS,
    push: push
  };

  global.Engine = api;
  global.EngineData = { STOCK_DEFS: STOCK_DEFS, NEWS_POOL: NEWS_POOL, CLIENTS: CLIENTS };
})(window);
