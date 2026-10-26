/* ==========================================================================
   AMPLIFYME TRAINER v2 — engine sell-side
   Modèle calibré sur les métriques officielles AmplifyME :
     NUMT  number of client trades        (flux client)
     COMM  commission                     (8 bps du notionnel)
     FFC   fat finger count               (erreurs de prix / taille)
     SSRM  sell-side risk management      (limites + inventory)
     ETM   exchange trade metric          (qualité de dé-risquage au marché)
   Le flux dépend de la COMPÉTITIVITÉ du quote board contre des banques rivales.
   ========================================================================== */
(function (global) {
  'use strict';

  var COMM_BPS = 8;
  var POS_LIMIT = 100000;
  var RIVALS = 4;                 // banques concurrentes sur chaque ligne

  var STOCK_DEFS = [
    { t: 'BABA', name: 'Alibaba ADR', ref: 483.99, vol: 1.00 },
    { t: 'MSFT', name: 'Microsoft', ref: 515.43, vol: 0.95 },
    { t: 'VW',   name: 'Volkswagen', ref: 49.55,  vol: 1.10 },
    { t: 'HSBC', name: 'HSBC Holdings', ref: 39.01, vol: 1.15 },
    { t: 'BP',   name: 'BP plc', ref: 37.73,  vol: 1.20 }
  ];

  var CLIENTS = [
    { id: 'HF1', label: 'HF1 — 123 4547 89 00', short: 'HF1', trust: 72 },
    { id: 'HF2', label: 'HF2 — 987 2210 44 10', short: 'HF2', trust: 70 },
    { id: 'HF3', label: 'HF3 — 552 8891 03 77', short: 'HF3', trust: 68 }
  ];

  var NEWS_POOL = [
    { tag: 'MACRO', text: 'US Government announce a record breaking $2 trillion economic rescue package.', all: 1, mag: 0.0075 },
    { tag: 'MACRO', text: 'Fed signals faster-than-expected rate cuts as inflation cools.', all: 1, mag: 0.0060 },
    { tag: 'MACRO', text: 'US inflation print comes in hotter than expected. Risk-off across equities.', all: -1, mag: 0.0068 },
    { tag: 'MACRO', text: 'Oil rallies on Middle East escalation — risk assets sell off.', all: -0.6, mag: 0.0080, oil: 1 },
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
  function r4(v) { return Math.round(v * 10000) / 10000; }
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
  function fmtInt(n) { return Math.round(n).toLocaleString('en-US'); }
  function fmtSigned(n) { return (n > 0 ? '+' : '') + fmtInt(n); }

  function emit(type, data) {
    if (!S) return;
    for (var i = 0; i < S.listeners.length; i++) {
      try { S.listeners[i](type, data); } catch (e) { console.error(e); }
    }
  }
  function toast(text, kind) { emit('toast', { text: text, kind: kind || 'info' }); }

  /* ---------------------------------------------------------------- init */
  function init(opts) {
    opts = Object.assign({ rounds: 2, roundSec: 180, difficulty: 'normal', wheels: true, sound: true }, opts || {});
    S = {
      opts: opts,
      stocks: STOCK_DEFS.map(function (d) {
        return {
          t: d.t, name: d.name, ref: d.ref, vol: d.vol,
          mid: d.ref, pos: 0, avg: 0, realised: 0, hist: [d.ref],
          drift: 0, lastDir: 0,
          rivalBid: 0, rivalOffer: 0, rivalSpread: 0,
          riskAt: 0, riskQty: 0, riskLots: [],
          axeShare: 0, axeTime: 0
        };
      }),
      clients: CLIENTS.map(function (c) { return Object.assign({}, c); }),
      chat: { DEAL: [], HF1: [], HF2: [], HF3: [] },
      news: [],
      board: {},            // quote board : { TICKER: {bid, offer, bidVol, offerVol, ts, expiresAt, id, midAtPost, newsSeq} }
      rfqs: [],
      blotter: [],
      listeners: [],
      round: 1,
      phase: 'idle',
      running: false,
      paused: false,
      ms: 0,
      elapsedMs: 0,
      clockMs: 0,
      priceAcc: 0,
      rivalTimer: 900,
      flowTimer: 3200,
      rfqTimer: 9000,
      newsTimer: 14000,
      rfqSeq: 1,
      quoteSeq: 1,
      newsSeq: 0,
      commission: 0,
      ffc: 0,
      trades: 0,
      answered: 0,
      missed: 0,
      rfqTotal: 0,
      lostToRivals: 0,
      respTimes: [],
      sniped: 0,
      settlementCost: 0,
      riskSum: 0,
      riskTime: 0,
      breachMs: 0,
      maxUtil: 0,
      etm: { clientQty: 0, unwoundQty: 0, timeWeighted: 0, clips: 0, goodClips: 0 },
      roundRiskSum: 0,
      roundRiskTime: 0,
      snap: null,
      roundLog: [],
      timers: []
    };

    S.stocks.forEach(function (st) { refreshRival(st, true); });
    bootChat();
    return api;
  }

  function bootChat() {
    push('DEAL', 'SYS', 'Welcome to the Investment Bank simulation — Single User Mode / all roles.');
    push('DEAL', 'SYS', 'Round 1 of the simulation has now started.');
    push('DEAL', 'SYS', 'Post two-way prices on the quote board (<kbd>M</kbd> then <kbd>↵</kbd>). Clients hit the best price in the market.');
    push('HF1', 'SYS', 'You are on the desk. Send me your axes when you have them.');
  }

  function push(channel, from, text, kind) {
    var msg = { from: from, text: text, t: S.ms, clock: fmtClock(S.clockMs), kind: kind || 'normal' };
    (S.chat[channel] || (S.chat[channel] = [])).push(msg);
    if (S.chat[channel].length > 200) S.chat[channel].shift();
    emit('chat', { channel: channel, msg: msg });
    return msg;
  }

  function stock(t) {
    for (var i = 0; i < S.stocks.length; i++) if (S.stocks[i].t === t) return S.stocks[i];
    return null;
  }
  function clientById(id) {
    for (var i = 0; i < S.clients.length; i++) if (S.clients[i].id === id) return S.clients[i];
    return null;
  }
  function at(ms, fn) { S.timers.push({ at: ms, fn: fn }); }

  /* ---------------------------------------------------------------- market */
  function marketHalfBps(st) {
    var extra = S.opts.difficulty === 'chaos' ? 1.2 : S.opts.difficulty === 'calme' ? -0.5 : 0;
    return 2.6 + extra;
  }

  function quoteMarket(st) {
    var hs = st.mid * marketHalfBps(st) / 10000;
    return { bid: r2(st.mid - hs), offer: r2(st.mid + hs) };
  }

  // Les banques concurrentes : spread 3–7 bps, bougent toutes les ~2,5 s
  function refreshRival(st, initial) {
    var base = STOCK_DEFS.filter(function (d) { return d.t === st.t; })[0];
    var spreadBps = rand(3.2, 6.6) + (initial ? 0 : rand(-0.6, 0.6));
    var skew = rand(-0.35, 0.35) * spreadBps;
    var half = st.mid * (spreadBps / 2) / 10000;
    st.rivalSpread = spreadBps;
    st.rivalBid = r2(st.mid - half - st.mid * skew / 10000);
    st.rivalOffer = r2(st.mid + half - st.mid * skew / 10000);
    if (st.rivalBid >= st.rivalOffer) st.rivalOffer = r2(st.rivalBid + 0.02);
  }

  function bestBid(st) {
    var q = S.board[st.t];
    var mine = q && !q.dead ? q.bid : null;
    return mine !== null && mine > st.rivalBid ? { px: mine, src: 'YOU' } : { px: st.rivalBid, src: 'RIVAL' };
  }
  function bestOffer(st) {
    var q = S.board[st.t];
    var mine = q && !q.dead ? q.offer : null;
    return mine !== null && mine < st.rivalOffer ? { px: mine, src: 'YOU' } : { px: st.rivalOffer, src: 'RIVAL' };
  }

  function depthFor(t, side, qty) {
    var st = stock(t);
    if (!st) return null;
    var m = st.mid, hs = marketHalfBps(st);
    var sgn = side === 'BUY' ? 1 : -1;
    var levels = [
      { px: r2(m * (1 + sgn * hs / 10000)), size: 25000 },
      { px: r2(m * (1 + sgn * (hs + 2.6) / 10000)), size: 45000 },
      { px: r2(m * (1 + sgn * (hs + 6) / 10000)), size: 80000 }
    ];
    var remaining = qty || 0, notional = 0, filled = 0;
    for (var i = 0; i < levels.length && remaining > 0; i++) {
      var take = Math.min(remaining, levels[i].size);
      notional += take * levels[i].px;
      filled += take;
      remaining -= take;
    }
    if (remaining > 0) {
      var worst = levels[levels.length - 1].px * (1 + sgn * 0.0015);
      notional += remaining * worst;
      filled += remaining;
    }
    return {
      side: side,
      avg: filled ? notional / filled : levels[0].px,
      levels: levels,
      slipBps: filled ? Math.abs(notional / filled - m) / m * 10000 : 0
    };
  }

  /* ---------------------------------------------------------------- prices */
  function priceTick() {
    var mult = S.opts.difficulty === 'chaos' ? 1.7 : S.opts.difficulty === 'calme' ? 0.65 : 1;
    var sigma = 0.00042 * mult;
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
    if (oldPos !== 0 && (oldPos > 0) !== (signed > 0)) {
      var closed = Math.min(Math.abs(signed), Math.abs(oldPos));
      st.realised += (price - st.avg) * closed * (oldPos > 0 ? 1 : -1);
      if (Math.abs(signed) > Math.abs(oldPos)) st.avg = price;
    } else {
      var ao = Math.abs(oldPos), an = Math.abs(newPos);
      st.avg = an > 0 ? (st.avg * ao + price * qty) / an : 0;
    }
    if (newPos === 0) st.avg = 0;
    st.pos = newPos;
    return newPos;
  }

  function bookTrade(st, side, qty, price, src, meta) {
    S.blotter.unshift({
      t: S.ms, clock: fmtClock(S.clockMs), sec: st.t, side: side, qty: qty,
      price: r2(price), notional: qty * price, src: src
    });
    if (S.blotter.length > 400) S.blotter.pop();
  }

  // Le client tape TON prix : tu prends l'autre côté.
  function clientFill(st, clientSide, qty, price, meta) {
    var ourSide = clientSide === 'BUY' ? 'SELL' : 'BUY';
    var notional = qty * price;
    var comm = notional * COMM_BPS / 10000;
    var before = st.pos;
    S.commission += comm;
    S.trades++;
    applyFill(st, ourSide, qty, price);
    bookTrade(st, ourSide, qty, price, meta && meta.src ? meta.src : 'CLIENT');

    // ETM : le risque client doit être dénoué au marché, vite et en clips raisonnables
    if (Math.abs(st.pos) > Math.abs(before)) {
      if (st.riskAt === 0) st.riskAt = S.ms;
      st.riskQty += qty;
      st.riskLots.push({ qty: qty, at: S.ms });
      S.etm.clientQty += qty;
    }
    if (meta && meta.client) {
      var c = clientById(meta.client);
      if (c) c.trust = clamp(c.trust + 0.4, 0, 100);
    }
    return { ourSide: ourSide, notional: notional, comm: comm };
  }

  function exchangeFill(st, side, qty, price) {
    var before = Math.abs(st.pos);
    applyFill(st, side, qty, price);
    var after = Math.abs(st.pos);
    bookTrade(st, side, qty, price, 'EXCH');
    if (after < before) {
      var unwound = before - after;
      S.etm.unwoundQty += unwound;
      S.etm.clips++;
      // un clip “propre” : 5–75k, soit un bloc qui ne défonce pas le carnet
      if (qty >= 5000 && qty <= 75000) S.etm.goodClips++;
      // FIFO : on associe chaque action dénouée au lot de risque client le plus ancien
      var remaining = unwound;
      while (remaining > 0 && st.riskLots.length) {
        var lot = st.riskLots[0];
        var take = Math.min(lot.qty, remaining);
        S.etm.timeWeighted += take * (S.ms - lot.at);
        lot.qty -= take;
        remaining -= take;
        if (lot.qty <= 0) st.riskLots.shift();
      }
      if (after === 0) { st.riskAt = 0; st.riskQty = 0; st.riskLots = []; }
    }
  }

  /* ---------------------------------------------------------------- news */
  function spawnNews() {
    var n = pick(NEWS_POOL);
    var impacts = {};
    S.stocks.forEach(function (st) {
      var mag = 0;
      if (n.all) {
        mag = n.all * n.mag * rand(0.75, 1.25);
        if (n.china && (st.t === 'BABA' || st.t === 'VW')) mag *= 1.6;
        if (n.oil && st.t === 'BP') mag = Math.abs(mag) * 1.5 * (n.oil > 0 ? 1 : -1);
        if (n.banks && st.t === 'HSBC') mag = Math.abs(mag) * 1.8 * (n.banks > 0 ? 1 : -1);
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
    S.newsSeq++;
    var item = {
      id: 'N' + (S.news.length + 1),
      tag: n.tag, text: n.text, dir: n.all ? n.all : n.dir, all: !!n.all,
      impacts: impacts, clock: fmtClock(S.clockMs), t: S.ms
    };
    S.news.unshift(item);
    if (S.news.length > 60) S.news.pop();
    emit('news', item);
    push('DEAL', 'SYS', n.tag + ' — ' + n.text, 'alert');
    at(S.ms + (S.opts.difficulty === 'chaos' ? 500 : 900), function () { pickOffStale(item); });
  }

  function pickOffStale(news) {
    if (!S || S.phase !== 'live') return;
    var maxHits = S.opts.difficulty === 'chaos' ? 3 : S.opts.difficulty === 'calme' ? 1 : 2;
    var hits = 0;
    S.stocks.forEach(function (st) {
      if (hits >= maxHits) return;
      var q = S.board[st.t];
      if (!q || q.dead) return;
      if (q.newsSeq >= S.newsSeq) return;              // postée après la news → pas stale
      var m = st.mid;
      var hitBuy = q.offer < m * (1 - 0.0007);
      var hitSell = q.bid > m * (1 + 0.0007);
      if (!hitBuy && !hitSell) return;
      var gap = Math.max(Math.abs(q.bid - m), Math.abs(q.offer - m)) / m;
      if (gap > 0.012) {
        q.dead = true;
        push(q.client || 'HF1', 'CLIENT', 'That price is miles off the market — pull it. I won\'t trade an obvious error.', 'alert');
        emit('busted', { ticker: st.t, quote: q });
        return;
      }
      var clientSide = hitBuy ? 'BUY' : 'SELL';
      var price = hitBuy ? q.offer : q.bid;
      var qty = hitBuy ? q.offerVol : q.bidVol;
      qty = Math.min(qty, 60000);
      if (qty < 100) return;
      q.dead = true;
      var client = q.client || pick(S.clients).id;
      clientFill(st, clientSide, qty, price, { src: 'STALE', client: client });
      S.sniped++;
      push(client, 'CLIENT', (clientSide === 'BUY'
        ? 'I\'ll take your offer — ' + fmtInt(qty) + ' ' + st.t + ' at ' + price.toFixed(2) + '.'
        : 'I\'ll hit your bid — ' + fmtInt(qty) + ' ' + st.t + ' at ' + price.toFixed(2) + '.'), 'alert');
      push('DEAL', 'SYS', 'Quote picked off on the ' + st.t + ' news. You were showing a stale price.', 'alert');
      emit('picked', { ticker: st.t, qty: qty, price: price, clientSide: clientSide, client: client });
      toast('PICK-OFF — ' + fmtInt(qty) + ' ' + st.t + ' à ' + price.toFixed(2) + ' : quote trop loin du nouveau mid.', 'bad');
      hits++;
    });
  }

  /* ---------------------------------------------------------------- quote board */
  function postQuote(p) {
    if (!S || S.phase !== 'live') return { ok: false, error: 'Marché fermé' };
    var st = stock(p.ticker);
    if (!st) return { ok: false, error: 'Ticker inconnu' };

    var bid = Number(p.bid), offer = Number(p.offer);
    var bv = Math.round(Number(p.bidVol)), ov = Math.round(Number(p.offerVol));
    var valid = clamp(Number(p.valid) || 30, 5, 120);

    if (!isFinite(bid) || !isFinite(offer) || bid <= 0 || offer <= 0) return { ok: false, error: 'Prix manquant ou invalide' };
    if (bid >= offer) { S.ffc++; return { ok: false, error: 'Bid ≥ Offer — marché croisé (Fat Finger)', ffc: true }; }
    if (!isFinite(bv) || !isFinite(ov) || bv < 100 || ov < 100) return { ok: false, error: 'Volume minimum : 100 actions' };
    if (bv > 500000 || ov > 500000) { S.ffc++; return { ok: false, error: 'Volume > 500 000 — Fat Finger bloqué', ffc: true }; }
    var dev = Math.max(Math.abs(bid - st.mid), Math.abs(offer - st.mid)) / st.mid;
    if (dev > 0.08) { S.ffc++; return { ok: false, error: 'Prix à ' + (dev * 100).toFixed(1) + '% du mid — Fat Finger bloqué', ffc: true }; }

    var openRfq = null;
    for (var i = S.rfqs.length - 1; i >= 0; i--) {
      if (S.rfqs[i].status === 'open' && S.rfqs[i].ticker === p.ticker) { openRfq = S.rfqs[i]; break; }
    }

    var q = {
      id: 'Q' + (S.quoteSeq++),
      ticker: p.ticker,
      bid: r2(bid), offer: r2(offer),
      bidVol: bv, offerVol: ov,
      valid: valid,
      ts: S.ms,
      expiresAt: S.ms + valid * 1000,
      midAtPost: st.mid,
      newsSeq: S.newsSeq,
      client: openRfq ? openRfq.client : null,
      rfqId: openRfq ? openRfq.id : null,
      dead: false
    };
    var prev = S.board[p.ticker];
    if (prev && !prev.dead) prev.dead = true;
    S.board[p.ticker] = q;

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
      openRfq.decideAt = S.ms + rand(1600, 3400);
    }

    push(openRfq ? openRfq.client : 'DEAL', 'ME',
      'Quote: ' + p.ticker + ' bid ' + q.bid.toFixed(2) + ' / offer ' + q.offer.toFixed(2) +
      ' — ' + fmtInt(bv) + ' x ' + fmtInt(ov) + ', valid ' + valid + 's', 'normal');

    emit('quote', q);
    return { ok: true, quote: q, rfq: openRfq };
  }

  function cancelQuote(ticker) {
    var q = S.board[ticker];
    if (q && !q.dead) { q.dead = true; emit('quoteCancel', q); return true; }
    return false;
  }
  function cancelAll() {
    var n = 0;
    Object.keys(S.board).forEach(function (k) {
      if (!S.board[k].dead) { S.board[k].dead = true; n++; }
    });
    if (n) { emit('quoteCancelAll', n); toast(n + ' quote(s) retirée(s) du board.', 'good'); }
    return n;
  }
  function liveQuotes() {
    return Object.keys(S.board).map(function (k) { return S.board[k]; })
      .filter(function (q) { return q && !q.dead && q.expiresAt > S.ms; });
  }
  function boardFor(t) {
    var q = S.board[t];
    return q && !q.dead && q.expiresAt > S.ms ? q : null;
  }

  /* ---------------------------------------------------------------- RFQ (blocks) */
  function spawnRfq() {
    if (S.phase !== 'live') return;
    var open = S.rfqs.filter(function (r) { return r.status === 'open'; });
    if (open.length >= 2) { S.rfqTimer = 6000; return; }

    var client = pick(S.clients);
    var st = pick(S.stocks);
    var size = st.mid > 200 ? pick([1000, 2500, 5000])
      : st.mid > 60 ? pick([5000, 10000, 20000])
      : pick([10000, 25000, 50000]);
    var buyBias = st.lastDir >= 0 ? 0.62 : 0.38;
    if (st.lastDir === 0) buyBias = 0.5;
    var side = Math.random() < buyBias ? 'BUY' : 'SELL';

    var rfq = {
      id: 'R' + (S.rfqSeq++),
      client: client.id, ticker: st.t, size: size, side: side,
      createdAt: S.ms, deadline: S.ms + 20000,
      status: 'open', attempts: 0, quoted: false, quotedAt: 0, decideAt: 0
    };
    S.rfqs.push(rfq);
    if (S.rfqs.length > 40) S.rfqs.shift();
    S.rfqTotal++;

    push(client.id, 'CLIENT',
      'Can you make me a two-way price for ' + fmtInt(size) + ' ' + st.t + ' please?', 'rfq');
    emit('rfq', rfq);
    toast('RFQ ' + client.id + ' · ' + fmtInt(size) + ' ' + st.t + ' · 20 s pour répondre', 'warn');

    var mult = S.round > 1 ? 0.85 : 1;
    var cfg = S.opts.difficulty === 'calme' ? [16000, 22000]
      : S.opts.difficulty === 'chaos' ? [8000, 12000] : [12000, 17000];
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
        toast('RFQ manquée — ' + r.client + ' · ' + fmtInt(r.size) + ' ' + r.ticker, 'bad');
        emit('missed', r);
      }
    });
  }

  /* ---------------------------------------------------------------- client decisions */
  function decide(rfq, q) {
    var st = stock(rfq.ticker);
    var side = rfq.side;
    var px = side === 'BUY' ? q.offer : q.bid;
    var vol = side === 'BUY' ? q.offerVol : q.bidVol;
    var client = clientById(rfq.client);
    var trust = client ? client.trust : 60;

    // référence = marché au moment où la quote a été postée
    var mid = q.midAtPost || st.mid;
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

    if (vol < rfq.size * 0.3) {
      rfq.status = 'rejected';
      push(rfq.client, 'CLIENT', 'You\'re only showing ' + fmtInt(vol) + ' on a ' + fmtInt(rfq.size) + ' order? Not helpful.', 'alert');
      if (client) client.trust = clamp(client.trust - 4, 0, 100);
      emit('pass', { rfq: rfq, quote: q, reason: 'size' });
      return;
    }

    // compétitivité vs les banques rivales
    var rivalPx = side === 'BUY' ? st.rivalOffer : st.rivalBid;
    var edgeBps = (side === 'BUY' ? (rivalPx - px) : (px - rivalPx)) / st.mid * 10000;
    var p;
    if (edgeBps >= 2) p = 0.93;
    else if (edgeBps >= 0) p = 0.72;
    else if (edgeBps >= -2) p = 0.42;
    else if (edgeBps >= -6) p = 0.14;
    else p = 0.03;
    p += (trust - 70) / 700;

    if (Math.random() > p) {
      S.lostToRivals++;
      rfq.status = 'lost';
      if (edgeBps < -2) {
        push(rfq.client, 'CLIENT', 'Your price is away from the market — I got a better one. Nothing done.', 'alert');
        if (client) client.trust = clamp(client.trust - 2, 0, 100);
        emit('pass', { rfq: rfq, quote: q, reason: 'wide' });
        toast('Flux perdu : ta quote était ' + Math.abs(edgeBps).toFixed(1) + ' bps moins bonne que le marché.', 'warn');
      } else if (rfq.attempts < 1 && Math.random() < 0.45) {
        rfq.attempts++;
        rfq.status = 'open';
        rfq.deadline = S.ms + 9000;
        push(rfq.client, 'CLIENT', 'Can you tighten that? I\'m still working the order.', 'alert');
        emit('tighten', { rfq: rfq });
      } else {
        rfq.status = 'rejected';
        push(rfq.client, 'CLIENT', 'I\'ll pass at that level.', 'normal');
        emit('pass', { rfq: rfq, quote: q, reason: 'wide' });
      }
      return;
    }

    var qty = Math.min(vol, rfq.size);
    clientFill(st, side, qty, px, { src: 'CLIENT', client: rfq.client });
    rfq.status = 'done';

    push(rfq.client, 'CLIENT',
      (side === 'BUY' ? 'Done — I bought ' : 'Done — I sold ') + fmtInt(qty) + ' ' + st.t +
      ' at ' + px.toFixed(2) + '. Thanks.', 'normal');
    push('DEAL', 'SYS',
      rfq.client + ' ' + (side === 'BUY' ? 'bought ' : 'sold ') + fmtInt(qty) + ' ' + st.t + ' at ' + px.toFixed(2) +
      '. Position ' + fmtSigned(st.pos) + '.', 'normal');
    emit('fill', { rfq: rfq, quote: q, ticker: st.t, side: side, qty: qty, price: px, pos: st.pos, client: rfq.client });
    toast('FILL ' + (side === 'BUY' ? 'client achète' : 'client vend') + ' ' + fmtInt(qty) + ' ' + st.t +
      ' @ ' + px.toFixed(2) + ' · position ' + fmtSigned(st.pos), 'good');
  }

  function processClientDecisions() {
    S.rfqs.forEach(function (rfq) {
      if (rfq.status !== 'quoted' || !rfq.decideAt) return;
      if (S.ms < rfq.decideAt) return;
      rfq.decideAt = 0;
      var q = null;
      var cand = S.board[rfq.ticker];
      if (cand && !cand.dead && cand.rfqId === rfq.id) q = cand;
      if (!q || q.expiresAt <= S.ms) {
        rfq.status = 'expired-quote';
        push(rfq.client, 'CLIENT', 'Your quote has expired — I need a fresh price.', 'alert');
        return;
      }
      decide(rfq, q);
    });
  }

  /* ---------------------------------------------------------------- board flow */
  // Les clients tapent en continu le meilleur prix du board (flux “axe”).
  function boardFlow() {
    if (S.phase !== 'live') return;
    var st = pick(S.stocks);
    var q = boardFor(st.t);
    var side = Math.random() < (st.lastDir >= 0 ? 0.6 : 0.4) ? 'BUY' : 'SELL';
    var qty;
    if (side === 'BUY') {
      if (!q) return;                                  // pas d'axe → le client va chez un rival
      if (q.offer > st.rivalOffer) return;
      qty = Math.min(q.offerVol, Math.round(rand(0.25, 1) * q.offerVol));
      if (qty < 100) return;
      var beat = st.rivalOffer - q.offer > 0.01;
      if (Math.random() > (beat ? 0.82 : 0.45)) return; // parfois il préfère la contrepartie rivale
      clientFill(st, 'BUY', qty, q.offer, { src: 'BOARD', client: pick(S.clients).id });
      S.board[st.t].offerVol = Math.max(0, q.offerVol - qty);
      if (S.board[st.t].offerVol < 100) S.board[st.t].dead = true;
      emit('fill', { ticker: st.t, side: 'BUY', qty: qty, price: q.offer, pos: st.pos, src: 'BOARD' });
      toast('FLUX — ' + fmtInt(qty) + ' ' + st.t + ' tapé sur ton offer ' + q.offer.toFixed(2), 'good');
    } else {
      if (!q) return;
      if (q.bid < st.rivalBid) return;
      qty = Math.min(q.bidVol, Math.round(rand(0.25, 1) * q.bidVol));
      if (qty < 100) return;
      var beat2 = q.bid - st.rivalBid > 0.01;
      if (Math.random() > (beat2 ? 0.82 : 0.45)) return;
      clientFill(st, 'SELL', qty, q.bid, { src: 'BOARD', client: pick(S.clients).id });
      S.board[st.t].bidVol = Math.max(0, q.bidVol - qty);
      if (S.board[st.t].bidVol < 100) S.board[st.t].dead = true;
      emit('fill', { ticker: st.t, side: 'SELL', qty: qty, price: q.bid, pos: st.pos, src: 'BOARD' });
      toast('FLUX — ' + fmtInt(qty) + ' ' + st.t + ' tapé sur ton bid ' + q.bid.toFixed(2), 'good');
    }
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
    exchangeFill(st, side, qty, d.avg);
    var imp = (qty / 100000) * 0.00018;
    st.mid = Math.max(0.5, st.mid * (1 + (side === 'BUY' ? imp : -imp)));
    st.hist.push(st.mid);
    emit('hedge', { ticker: ticker, side: side, qty: qty, price: d.avg, pos: st.pos, slip: d.slipBps });
    return { ok: true, price: d.avg, pos: st.pos, slip: d.slipBps };
  }

  function flatten(ticker) {
    var st = stock(ticker);
    if (!st) return { ok: false, error: 'Ticker inconnu' };
    if (st.pos === 0) return { ok: false, error: 'Déjà flat' };
    return hedge(ticker, st.pos > 0 ? 'SELL' : 'BUY', Math.abs(st.pos));
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
    S.ms += dt; S.elapsedMs += dt; S.clockMs += dt;

    S.priceAcc += dt;
    while (S.priceAcc >= 620) { S.priceAcc -= 620; priceTick(); }

    S.rivalTimer -= dt;
    if (S.rivalTimer <= 0) { S.stocks.forEach(function (st) { refreshRival(st, false); }); S.rivalTimer = rand(2200, 3200); }

    S.flowTimer -= dt;
    if (S.flowTimer <= 0) { boardFlow(); S.flowTimer = rand(2600, 4200) * (S.round > 1 ? 0.85 : 1); }

    S.rfqTimer -= dt;
    if (S.rfqTimer <= 0) spawnRfq();

    S.newsTimer -= dt;
    if (S.newsTimer <= 0) {
      spawnNews();
      var cfg = S.opts.difficulty === 'calme' ? [38000, 52000]
        : S.opts.difficulty === 'chaos' ? [15000, 22000] : [24000, 34000];
      S.newsTimer = rand(cfg[0], cfg[1]) * (S.round > 1 ? 0.82 : 1);
    }

    processClientDecisions();
    expireRfqs();

    // quotes expirées
    Object.keys(S.board).forEach(function (k) {
      var q = S.board[k];
      if (!q.dead && S.ms >= q.expiresAt) { q.dead = true; emit('quoteExpired', q); }
    });

    // axe : part du temps où ton prix est le meilleur
    S.stocks.forEach(function (st) {
      var q = boardFor(st.t);
      st.axeTime += dt;
      if (q && q.bid > st.rivalBid) st.axeShare += dt;
    });

    // risque
    var util = 0;
    S.stocks.forEach(function (st) { util = Math.max(util, Math.abs(st.pos) / POS_LIMIT); });
    S.riskSum += util * dt; S.riskTime += dt;
    S.roundRiskSum += util * dt; S.roundRiskTime += dt;
    if (util > S.maxUtil) S.maxUtil = util;
    if (util > 1) S.breachMs += dt;

    if (S.timers.length) {
      var due = S.timers.filter(function (x) { return x.at <= S.ms; });
      S.timers = S.timers.filter(function (x) { return x.at > S.ms; });
      due.forEach(function (x) { try { x.fn(); } catch (e) { console.error(e); } });
    }

    if (S.ms >= S.opts.roundSec * 1000) endRound();
  }

  /* ---------------------------------------------------------------- rounds */
  function start() {
    S.phase = 'live'; S.running = true; S.paused = false; S.ms = 0;
    S.snap = snapshot();
  }
  function nextRound() {
    S.round++;
    S.ms = 0; S.phase = 'live'; S.running = true; S.paused = false;
    S.board = {}; S.rfqs = []; S.timers = [];
    S.rfqTimer = 5000; S.newsTimer = 10000; S.flowTimer = 3000;
    S.roundRiskSum = 0; S.roundRiskTime = 0;
    S.snap = snapshot();
    push('DEAL', 'SYS', 'Round ' + S.round + ' of the simulation has now started.', 'normal');
    emit('roundStart', { round: S.round });
  }
  function snapshot() {
    return {
      commission: S.commission, trades: S.trades, ffc: S.ffc, answered: S.answered,
      missed: S.missed, rfqTotal: S.rfqTotal, sniped: S.sniped,
      etmClient: S.etm.clientQty, etmUnwound: S.etm.unwoundQty
    };
  }
  function endRound() {
    if (S.phase !== 'live') return;
    S.phase = 'roundEnd';
    S.running = false;
    var closeCost = 0, openLines = [];
    S.stocks.forEach(function (st) {
      if (st.pos !== 0) {
        st.realised += (st.mid - st.avg) * st.pos;
        var cost = Math.abs(st.pos) * st.mid * 0.0002;
        st.realised -= cost;
        closeCost += cost;
        openLines.push({ t: st.t, pos: st.pos });
        st.pos = 0; st.avg = 0;
      }
    });
    S.settlementCost += closeCost;
    S.board = {};
    S.rfqs.forEach(function (r) { if (r.status === 'open') r.status = 'closed'; });
    push('DEAL', 'SYS', 'Round ' + S.round + ' of the simulation has now ended.', 'alert');

    var roundStats = {
      round: S.round,
      trades: S.trades - (S.snap ? S.snap.trades : 0),
      commission: S.commission - (S.snap ? S.snap.commission : 0),
      ffc: S.ffc - (S.snap ? S.snap.ffc : 0),
      rfqTotal: S.rfqTotal - (S.snap ? S.snap.rfqTotal : 0),
      answered: S.answered - (S.snap ? S.snap.answered : 0),
      sniped: S.sniped - (S.snap ? S.snap.sniped : 0),
      closeCost: closeCost, openLines: openLines,
      avgUtil: S.roundRiskTime ? S.roundRiskSum / S.roundRiskTime : 0
    };
    S.roundLog.push(roundStats);
    if (S.round >= S.opts.rounds) S.phase = 'done';
    emit('roundEnd', { roundStats: roundStats, score: score(), isLast: S.round >= S.opts.rounds });
  }

  /* ---------------------------------------------------------------- P&L */
  function totalRealised() { return S.stocks.reduce(function (a, st) { return a + st.realised; }, 0); }
  function totalUnrealised() { return S.stocks.reduce(function (a, st) { return a + st.pos * (st.mid - st.avg); }, 0); }
  function totalPnl() { return totalRealised() + totalUnrealised() + S.commission; }
  function netExposure() { return S.stocks.reduce(function (a, st) { return a + st.pos * st.mid; }, 0); }
  function grossExposure() { return S.stocks.reduce(function (a, st) { return a + Math.abs(st.pos * st.mid); }, 0); }

  /* ---------------------------------------------------------------- ETM / SSRM */
  function etmScore() {
    var e = S.etm;
    // Aucun risque client pris = aucun crédit ETM (un desk passif ne marque pas de points).
    if (e.clientQty <= 0) return { score: 0, unwound: 0, speed: 0, clip: 0 };
    var unwoundShare = clamp(e.unwoundQty / e.clientQty, 0, 1.15);
    var avgMs = e.unwoundQty > 0 ? e.timeWeighted / e.unwoundQty : 30000;
    var speed = clamp(1 - (avgMs / 1000) / 40, 0.25, 1);
    var clip = e.clips ? clamp(e.goodClips / e.clips, 0, 1) : 1;
    var openRisk = 0;
    S.stocks.forEach(function (st) { openRisk += Math.abs(st.pos); });
    var score = 100 * clamp(unwoundShare, 0, 1) * (0.55 + 0.25 * speed + 0.20 * clip);
    if (openRisk > 0) score *= 0.85;
    return { score: clamp(score, 0, 100), unwound: unwoundShare, speed: speed, clip: clip, openRisk: openRisk };
  }

  function ssrmScore() {
    var avgUtil = S.riskTime ? S.riskSum / S.riskTime : 0;
    return clamp(100 - avgUtil * 100 - (S.breachMs / 1000) * 1.4 - (S.maxUtil > 0.9 ? 12 : 0), 0, 100);
  }

  /* ---------------------------------------------------------------- score */
  var PCT_CURVE = [   // [score composite, percentile estimé]
    [20, 2], [30, 8], [40, 20], [50, 38], [60, 58], [70, 75], [78, 86],
    [85, 93], [90, 97], [94, 99], [100, 99.9]
  ];
  function percentileOf(total) {
    for (var i = 1; i < PCT_CURVE.length; i++) {
      if (total <= PCT_CURVE[i][0]) {
        var a = PCT_CURVE[i - 1], b = PCT_CURVE[i];
        var t = (total - a[0]) / (b[0] - a[0] || 1);
        return a[1] + t * (b[1] - a[1]);
      }
    }
    return 99.9;
  }

  function score() {
    var scale = Math.max(0.45, Math.min(4, S.elapsedMs / 180000));
    var commTarget = 100000 * scale;            // ~10 blocs de 30k actions à 8 bps
    var commScore = clamp(S.commission / commTarget * 100, 0, 100);

    var numtTarget = 18 * scale;                // ~1 trade client / 10 s
    var numtScore = clamp(S.trades / numtTarget * 100, 0, 100);

    var etm = etmScore();
    var ssrm = ssrmScore();
    var ffcScore = clamp(100 - 16 * S.ffc, 0, 100);

    var total = 0.25 * numtScore + 0.25 * commScore + 0.20 * etm.score + 0.20 * ssrm + 0.10 * ffcScore;
    var pct = percentileOf(total);

    return {
      total: Math.round(total * 10) / 10,
      numt: Math.round(numtScore),
      comm: Math.round(commScore),
      etm: Math.round(etm.score),
      ssrm: Math.round(ssrm),
      ffcScore: Math.round(ffcScore),
      grade: total >= 85 ? 'A' : total >= 70 ? 'B' : total >= 55 ? 'C' : total >= 40 ? 'D' : 'E',
      percentile: Math.round(pct * 10) / 10,
      metrics: {
        pnl: totalPnl(),
        realised: totalRealised(),
        unrealised: totalUnrealised(),
        commission: S.commission,
        numt: S.trades,
        ffc: S.ffc,
        etm: Math.round(etm.score),
        ssrm: Math.round(ssrm),
        unwound: etm.unwound,
        speed: etm.speed,
        clip: etm.clip,
        avgUtil: S.riskTime ? S.riskSum / S.riskTime : 0,
        maxUtil: S.maxUtil,
        breachSec: Math.round(S.breachMs / 1000),
        rfqTotal: S.rfqTotal,
        answered: S.answered,
        answeredRatio: S.rfqTotal ? S.answered / S.rfqTotal : 1,
        missed: S.missed,
        lostToRivals: S.lostToRivals,
        avgResp: S.respTimes.length ? mean(S.respTimes) / 1000 : 0,
        trust: mean(S.clients.map(function (c) { return c.trust; })),
        sniped: S.sniped,
        settlement: S.settlementCost,
        axeShare: S.stocks.reduce(function (a, st) { return a + st.axeShare; }, 0) /
          Math.max(1, S.stocks.reduce(function (a, st) { return a + st.axeTime; }, 0)),
        netExposure: netExposure(),
        grossExposure: grossExposure()
      },
      targets: { comm: commTarget, numt: numtTarget }
    };
  }

  function fixes(sc) {
    var m = sc.metrics, out = [];
    if (m.answeredRatio < 0.9) out.push('Réponds à <b>100 % des RFQ</b> : ' + m.answered + '/' + m.rfqTotal + '. Chaque bloc ignoré coupe le flux et la relation.');
    if (m.lostToRivals > 0) out.push('<b>' + m.lostToRivals + ' bloc(s) perdu(s)</b> contre les banques rivales : ton prix était dehors. Vise 0–2 bps au-dessus du meilleur offre concurrent.');
    if (m.ffc > 0) out.push('<b>' + m.ffc + ' fat finger(s)</b> : vérifie bid &lt; offer, 10k–50k de volume, prix à moins de 2 % du mid.');
    if (m.sniped > 0) out.push('<b>' + m.sniped + ' pick-off(s)</b> : retire tes quotes (<kbd>X</kbd>) à chaque news, puis repose. Une quote en vie est une option gratuite.');
    if (m.unwound < 0.9) out.push('ETM : seulement <b>' + Math.round(m.unwound * 100) + ' %</b> du risque client dénoué au marché. Hedge tout de suite, pas « après ».');
    else if (m.speed < 0.6) out.push('ETM : tu dénoues mais <b>trop lentement</b>. Un client sent ta position : hedge dans les 10 secondes.');
    if (m.maxUtil > 0.85) out.push('Exposition max <b>' + Math.round(m.maxUtil * 100) + ' %</b> de la limite : coupe en blocs de 25–50k.');
    if (m.avgResp > 10) out.push('Temps de réponse <b>' + m.avgResp.toFixed(1) + ' s</b> : vise moins de 8 s.');
    if (sc.numt < 60) out.push('<b>' + m.numt + ' trades</b> seulement : garde des axes permanents sur 3–4 lignes, le flux vient du board.');
    if (!out.length) out.push('Profil propre sur les 5 métriques. Rejoue en <b>Chaos</b> pour verrouiller.');
    return out.slice(0, 4);
  }

  /* ---------------------------------------------------------------- API */
  var api = {
    init: init, start: start, step: step, nextRound: nextRound,
    sendQuote: postQuote, cancelQuote: cancelQuote, cancelAll: cancelAll,
    hedge: hedge, flatten: flatten, flattenAll: flattenAll,
    score: score, fixes: fixes,
    on: function (fn) { if (S) S.listeners.push(fn); return api; },
    get: function () { return S; },
    stock: stock, quoteMarket: quoteMarket, depthFor: depthFor,
    liveQuotes: liveQuotes, boardFor: boardFor,
    bestBid: bestBid, bestOffer: bestOffer,
    totalPnl: totalPnl, totalRealised: totalRealised, totalUnrealised: totalUnrealised,
    netExposure: netExposure, grossExposure: grossExposure,
    etmScore: etmScore, ssrmScore: ssrmScore, percentileOf: percentileOf,
    fmtClock: fmtClock, fmtInt: fmtInt, fmtSigned: fmtSigned,
    POS_LIMIT: POS_LIMIT, COMM_BPS: COMM_BPS, push: push
  };

  global.Engine = api;
  global.EngineData = { STOCK_DEFS: STOCK_DEFS, NEWS_POOL: NEWS_POOL, CLIENTS: CLIENTS };
})(window);
