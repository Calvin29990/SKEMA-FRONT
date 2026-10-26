/* ==========================================================================
   AMPLIFYME TRAINER — reflex drills (question generators)
   window.Drills.meta  /  window.Drills.make(type) -> question
   ========================================================================== */
(function (global) {
  'use strict';

  var TICKERS = ['BABA', 'MSFT', 'VW', 'HSBC', 'BP'];
  var PRICES = [37.73, 39.01, 49.55, 52.40, 118.60, 245.30, 483.99, 515.43];

  function r(a, b) { return a + Math.random() * (b - a); }
  function ri(a, b) { return Math.floor(r(a, b + 1)); }
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function r2(v) { return Math.round(v * 100) / 100; }
  function fmt(n) { return Math.round(n).toLocaleString('en-US'); }
  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  var meta = [
    { id: 'twoway', name: 'Bid / Offer', ico: '01', desc: 'Mid + spread → les deux prix, en 5 secondes.' },
    { id: 'hedge', name: 'Hedge', ico: '02', desc: 'Le client tape : dans quel sens es-tu, et que fais-tu ?' },
    { id: 'pnl', name: 'P&L', ico: '03', desc: 'Achat / vente, long / short : le calcul de tête.' },
    { id: 'notional', name: 'Notionnel & COMM', ico: '04', desc: 'Prix × quantité, puis 8 bps de commission.' },
    { id: 'fatfinger', name: 'Fat finger', ico: '05', desc: 'Repérer le ticket impossible avant de l\'envoyer.' },
    { id: 'limit', name: 'Limite de risque', ico: '06', desc: 'Position + flux client vs 100 000 : tu quotes combien ?' }
  ];

  function twoWay() {
    var mid = pick(PRICES) * (Math.random() < 0.3 ? r(0.9, 1.1) : 1);
    mid = r2(mid);
    var centsMode = Math.random() < 0.3;
    var half, label, answerBid, answerOffer;
    if (centsMode) {
      half = pick([0.02, 0.05, 0.10, 0.15]);
      label = 'spread total ' + (half * 2).toFixed(2);
      answerBid = r2(mid - half);
      answerOffer = r2(mid + half);
    } else {
      var bps = pick([8, 10, 12, 16, 20]);
      half = mid * (bps / 2) / 10000;
      label = 'spread ' + bps + ' bps';
      answerBid = r2(mid - half);
      answerOffer = r2(mid + half);
    }
    return {
      type: 'twoway',
      prompt: 'Mid ' + mid.toFixed(2) + ' — ' + label + '.',
      sub: 'Donne ton bid et ton offer. Rappel : bid &lt; mid &lt; offer.',
      fields: [
        { key: 'bid', label: 'BID', kind: 'price' },
        { key: 'offer', label: 'OFFER', kind: 'price' }
      ],
      answer: { bid: answerBid, offer: answerOffer },
      tol: 0.03,
      explain: 'Bid = mid − (spread/2), offer = mid + (spread/2). Ici : ' + answerBid.toFixed(2) + ' / ' + answerOffer.toFixed(2) + '.'
    };
  }

  function hedge() {
    var t = pick(TICKERS);
    var qty = pick([10000, 25000, 40000, 50000, 75000]);
    var clientBuys = Math.random() < 0.5;
    var ourPos = clientBuys ? -qty : qty;
    var correct = clientBuys
      ? 'Short ' + fmt(qty) + ' → j\'achète ' + fmt(qty) + ' au marché'
      : 'Long ' + fmt(qty) + ' → je vends ' + fmt(qty) + ' au marché';
    var wrong = [
      (clientBuys ? 'Long ' : 'Short ') + fmt(qty) + ' → je ' + (clientBuys ? 'vends' : 'achète') + ' ' + fmt(qty) + ' au marché',
      'Flat — le trade client ne change pas ma position',
      (clientBuys ? 'Short ' : 'Long ') + fmt(qty) + ' → je garde la position jusqu\'à la fin du round'
    ];
    var opts = shuffle([correct].concat(wrong));
    return {
      type: 'hedge',
      prompt: 'Le client ' + (clientBuys ? 'achète' : 'vend') + ' ' + fmt(qty) + ' ' + t + ' sur ton prix.',
      sub: 'Ta position devient quoi, et quel est le hedge correct ?',
      options: opts,
      correct: opts.indexOf(correct),
      explain: clientBuys
        ? 'Le client achète → tu vends → ta position est <b>short ' + fmt(qty) + '</b>. Tu rachètes au marché pour revenir flat, en payant le spread.'
        : 'Le client vend → tu achètes → ta position est <b>long ' + fmt(qty) + '</b>. Tu revends au marché pour revenir flat.'
    };
  }

  function pnl() {
    var qty = pick([10000, 20000, 25000, 40000, 50000, 75000]);
    var entry = r2(pick(PRICES) * r(0.9, 1.1));
    var diff = r2(r(0.02, 0.45) * (Math.random() < 0.25 ? -1 : 1));
    var isShort = Math.random() < 0.4;
    var exit = r2(entry + (isShort ? -diff : diff));
    var pl = isShort ? (entry - exit) * qty : (exit - entry) * qty;
    var prompt = isShort
      ? 'Vente ' + fmt(qty) + ' @ ' + entry.toFixed(2) + ', rachat @ ' + exit.toFixed(2) + '.'
      : 'Achat ' + fmt(qty) + ' @ ' + entry.toFixed(2) + ', vente @ ' + exit.toFixed(2) + '.';
    return {
      type: 'pnl',
      prompt: prompt,
      sub: 'Quel est le P&amp;L réalisé, en dollars ? (négatif si perte)',
      fields: [{ key: 'val', label: 'P&L ($)', kind: 'int' }],
      answer: { val: pl },
      tol: 1,
      explain: 'P&amp;L = ' + (isShort ? '(entrée − sortie)' : '(sortie − entrée)') + ' × quantité = ' +
        (isShort ? '(' + entry.toFixed(2) + ' − ' + exit.toFixed(2) + ')' : '(' + exit.toFixed(2) + ' − ' + entry.toFixed(2) + ')') +
        ' × ' + fmt(qty) + ' = <b>' + (pl >= 0 ? '+' : '') + fmt(pl) + ' $</b>.'
    };
  }

  function notional() {
    var qty = pick([10000, 20000, 30000, 40000, 50000, 75000]);
    var px = r2(pick(PRICES) * r(0.92, 1.08));
    var notional = qty * px;
    var comm = notional * 0.0008;
    var askComm = Math.random() < 0.45;
    if (askComm) {
      return {
        type: 'notional',
        prompt: fmt(qty) + ' actions ' + ' @ ' + px.toFixed(2) + ' — commission 8 bps.',
        sub: 'Quelle commission encaisses-tu, en dollars ?',
        fields: [{ key: 'val', label: 'COMMISSION ($)', kind: 'int' }],
        answer: { val: comm },
        tol: 3,
        explain: 'Notionnel = ' + fmt(qty) + ' × ' + px.toFixed(2) + ' = <b>' + fmt(notional) + ' $</b>. Commission = notionnel × 0,0008 = <b>' + fmt(comm) + ' $</b>.'
      };
    }
    return {
      type: 'notional',
      prompt: fmt(qty) + ' actions à ' + px.toFixed(2) + '.',
      sub: 'Quel est le notionnel du trade, en dollars ?',
      fields: [{ key: 'val', label: 'NOTIONNEL ($)', kind: 'int' }],
      answer: { val: notional },
      tol: 2,
      explain: 'Notionnel = quantité × prix = ' + fmt(qty) + ' × ' + px.toFixed(2) + ' = <b>' + fmt(notional) + ' $</b>. À 8 bps, la commission serait de ' + fmt(comm) + ' $.'
    };
  }

  function fatfinger() {
    var good = [];
    var base = r2(pick(PRICES) * r(0.9, 1.1));
    var t = pick(TICKERS);
    var vol = pick([10000, 25000, 50000, 75000]);
    var half = base * 0.0005;
    for (var i = 0; i < 4; i++) {
      var mid = r2(base * r(0.98, 1.02));
      good.push({
        t: pick(TICKERS),
        bid: r2(mid - half),
        offer: r2(mid + half),
        vol: vol
      });
    }
    var badIdx = ri(0, 3);
    var kind = pick(['cross', 'vol', 'px']);
    if (kind === 'cross') {
      good[badIdx].bid = r2(good[badIdx].offer + 0.20);
    } else if (kind === 'vol') {
      good[badIdx].vol = 500000;
    } else {
      good[badIdx].offer = r2(good[badIdx].offer * 10);
    }
    var opts = ['1', '2', '3', '4'];
    var explain = kind === 'cross'
      ? 'Le ticket ' + (badIdx + 1) + ' a un <b>bid au-dessus de l\'offer</b> : marché croisé, impossible à envoyer.'
      : kind === 'vol'
        ? 'Le ticket ' + (badIdx + 1) + ' demande <b>500 000</b> alors que la RFQ est à ' + fmt(vol) + ' : volume ×10, fat finger.'
        : 'Le ticket ' + (badIdx + 1) + ' a un prix à <b>10×</b> le mid : fat finger de décimale.';
    return {
      type: 'fatfinger',
      prompt: 'Quel ticket est un fat finger ?',
      sub: 'Un seul est impossible ou absurde. Lequel refuses-tu d\'envoyer ?',
      table: {
        head: ['#', 'SEC', 'BID', 'OFFER', 'VOL'],
        rows: good.map(function (g, i) {
          return [(i + 1) + '', g.t, g.bid.toFixed(2), g.offer.toFixed(2), fmt(g.vol)];
        })
      },
      options: opts,
      optionLabels: opts,
      correct: badIdx,
      explain: explain
    };
  }

  function limit() {
    var limit = 100000;
    var sign = Math.random() < 0.5 ? -1 : 1;
    var pos = sign * pick([60000, 70000, 80000, 90000]);
    var flow = pick([30000, 40000, 50000, 60000]);
    var room = limit - Math.abs(pos);
    var correct = 'Je quote ' + fmt(room) + ' maximum, puis je hedge';
    var opts = shuffle([
      correct,
      'Je quote les ' + fmt(flow) + ' en entier : le flux avant tout',
      'Je ne réponds pas à la RFQ',
      'Je quote ' + fmt(flow) + ' puis j\'attends la fin du round'
    ]);
    return {
      type: 'limit',
      prompt: 'Position ' + (pos > 0 ? '+' : '−') + fmt(Math.abs(pos)) + ' · limite ' + fmt(limit) + ' par ligne.',
      sub: 'Le client veut ' + (pos < 0 ? 'VENDRE' : 'ACHETER') + ' ' + fmt(flow) + ' de plus (même sens que ta position). Tu quotes combien ?',
      options: opts,
      correct: opts.indexOf(correct),
      explain: 'Il te reste <b>' + fmt(room) + '</b> avant la limite. Au-delà, tu tombes en breach : tu ne peux plus hedger dans le sens qui augmente le risque. Tu quotes ' + fmt(room) + ', tu hedges, puis tu peux ré-ouvrir.'
    };
  }

  var makers = { twoway: twoWay, hedge: hedge, pnl: pnl, notional: notional, fatfinger: fatfinger, limit: limit };

  global.Drills = {
    meta: meta,
    make: function (type) {
      var fn = makers[type] || twoWay;
      var q = fn();
      q.type = type;
      return q;
    }
  };
})(window);
