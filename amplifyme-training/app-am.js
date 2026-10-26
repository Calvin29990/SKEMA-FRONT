/* ==========================================================================
   AMPLIFYME TRAINER — Asset Manager UI (buy-side desk)
   window.AM.start(settings, { chained, onContinue, onFinish })
   ========================================================================== */
(function () {
  'use strict';

  var A = window.EngineAM;
  var C = window.AppCore;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  var M = {
    sel: 'BP', tf: 240, mode: 'line', amount: 1000000, side: 'BUY',
    loop: null, last: 0, started: false,
    opts: null, callbacks: {}, paused: false
  };

  /* ---------------------------------------------------------------- start */
  function start(settings, callbacks) {
    M.callbacks = callbacks || {};
    M.opts = settings || {};
    M.sel = 'BP';
    M.amount = 1000000;
    M.paused = false;
    M.started = true;

    var roundSec = M.opts.roundSec === 180 ? 240 : M.opts.roundSec === 120 ? 150 : M.opts.roundSec || 240;
    A.init({ roundSec: roundSec, difficulty: M.opts.difficulty || 'normal' });
    A.on(onEvent);
    A.start();

    $('#amTicker').value = M.sel;
    $('#amAmount').value = M.amount;
    $$('#amSizeChips button').forEach(function (b) { b.classList.toggle('on', Number(b.dataset.amt) === M.amount); });
    $('#amNewsList').innerHTML = '<div class="news-empty">Les headlines tombent toutes les 20–28 s. Achète la bonne, coupe la mauvaise — vite.</div>';
    $('#amBlotterBody').innerHTML = '';
    $('#amStatus').textContent = 'DESK OUVERT';
    $('#amBtnPause').textContent = '❚❚';

    renderAll();
    if (M.loop) clearInterval(M.loop);
    M.last = performance.now();
    M.loop = setInterval(tick, 150);

    var S0 = A.get();
    S0.paused = true;
    C.showIntro({
      title: 'Round 1 — Asset Manager',
      lead: 'Tu gères <b>20 M$</b> sur 5 actions. Le benchmark, c\'est les 5 lignes à poids égal : ton score, c\'est l\'<b>alpha</b>, pas le P&amp;L brut.',
      points: [
        '<b>Investis dans les 30 premières secondes</b> : reste 70–95 % investi, sinon la première news macro te fait perdre.',
        '<b>15 à 25 % maximum par ligne.</b> Un titre à 60 % = un headline et tu sors du top 300.',
        'News positive → <b>renforce</b>. News négative → <b>coupe</b>. En moins de 10 secondes.',
        'Ordres de <b>250k à 1M</b> : au-delà, l\'impact et les frais mangent l\'alpha.'
      ],
      keys: [
        ['<kbd>1</kbd>–<kbd>5</kbd>', 'choisir le ticker'],
        ['<kbd>B</kbd>', 'acheter à l\'offer'],
        ['<kbd>S</kbd>', 'vendre au bid'],
        ['<kbd>F</kbd>', 'solder la ligne']
      ],
      resume: function () { var s2 = A.get(); if (s2) s2.paused = false; M.paused = false; }
    });
    C.toast('Round 1 — Asset Manager. $20M à investir. Achète la news avant les autres.', 'good');
  }

  function stop() {
    if (M.loop) { clearInterval(M.loop); M.loop = null; }
    M.started = false;
    var S = A.get();
    if (S) S.running = false;
  }

  /* ---------------------------------------------------------------- events */
  function onEvent(type, data) {
    if (type === 'toast') { C.toast(data.text, data.kind); return; }
    if (type === 'news') { C.beep('news'); flashNews(); return; }
    if (type === 'trade') { C.beep('fill'); return; }
    if (type === 'roundEnd') {
      if (M.loop) { clearInterval(M.loop); M.loop = null; }
      C.beep('end');
      endRound(data);
      return;
    }
  }

  function flashNews() {
    var p = $('.am-news');
    if (!p) return;
    p.style.transition = 'none';
    p.style.boxShadow = '0 0 0 2px rgba(255,176,32,.7)';
    setTimeout(function () { p.style.transition = '.5s'; p.style.boxShadow = 'none'; }, 450);
  }

  /* ---------------------------------------------------------------- loop */
  function tick() {
    var S = A.get();
    if (!S) return;
    var now = performance.now();
    var dt = Math.min(500, now - M.last);
    M.last = now;
    A.step(dt);
    renderAll();
  }

  function renderAll() {
    var S = A.get();
    if (!S) return;
    var sc = A.score();

    /* top bar */
    $('#amClock').textContent = A.fmtClock(S.clockMs);
    $('#amValue').textContent = C.fmt(A.portfolioValue());
    var pnl = A.portfolioValue() - S.capital;
    var pnlEl = $('#amPnl');
    pnlEl.textContent = (pnl > 0 ? '+' : pnl < 0 ? '-' : '') + '$' + C.fmt(Math.abs(pnl));
    pnlEl.className = C.cls(pnl);
    var ret = A.portfolioReturn();
    var retEl = $('#amRet');
    retEl.textContent = (ret >= 0 ? '+' : '') + (ret * 100).toFixed(2) + '%';
    retEl.className = C.cls(ret);
    var al = A.alpha();
    var alEl = $('#amAlpha');
    alEl.textContent = (al >= 0 ? '+' : '') + (al * 100).toFixed(2) + '%';
    alEl.className = C.cls(al);
    $('#amCash').textContent = C.fmt(S.cash);

    var rem = Math.max(0, S.opts.roundSec * 1000 - S.ms);
    var rc = $('#amRoundClock');
    rc.textContent = C.mmss(rem);
    rc.className = 'rc-clock' + (rem < 10000 ? ' danger' : rem < 30000 ? ' warn' : '');

    /* watchlist */
    var html = '';
    S.stocks.forEach(function (st) {
      var m = A.market(st.t);
      var chg = (st.mid / st.ref - 1) * 100;
      html += '<tr data-amticker="' + st.t + '" class="' + (M.sel === st.t ? 'sel' : '') + '">' +
        '<td>' + st.t + '</td>' +
        '<td class="r num-pos">' + m.bid.toFixed(2) + '</td>' +
        '<td class="r num-neg">' + m.offer.toFixed(2) + '</td>' +
        '<td class="r ' + C.cls(chg) + '">' + (chg >= 0 ? '+' : '') + chg.toFixed(2) + '%</td>' +
        '<td class="r ' + C.cls(st.pos) + '">' + (st.pos === 0 ? '—' : C.fmt(st.pos)) + '</td></tr>';
    });
    $('#amWatchBody').innerHTML = html;

    /* positions */
    var v = A.portfolioValue();
    var posHtml = '', count = 0;
    S.stocks.forEach(function (st) {
      if (st.pos === 0) return;
      count++;
      var pl = st.pos * (st.mid - st.avg);
      var w = Math.abs(st.pos * st.mid) / Math.max(1, v);
      posHtml += '<tr data-amticker="' + st.t + '" class="' + (M.sel === st.t ? 'sel' : '') + '">' +
        '<td>' + st.t + '</td><td class="r">' + C.fmt(st.pos) + '</td>' +
        '<td class="r">' + st.avg.toFixed(2) + '</td>' +
        '<td class="r ' + C.cls(pl) + '">' + C.numSigned(Math.round(pl)) + '</td>' +
        '<td class="r">' + Math.round(w * 100) + '%<div class="am-weight-bar"><i style="width:' + Math.min(100, w * 100) + '%"></i></div></td></tr>';
    });
    if (!posHtml) posHtml = '<tr><td colspan="5" class="muted" style="padding:8px;font-family:var(--sans)">Aucune position. Achète une news, pas un graphe.</td></tr>';
    $('#amPosBody').innerHTML = posHtml;
    $('#amPosCount').textContent = count + ' ligne(s)';
    var exposure = A.investedValue() / Math.max(1, v);
    $('#amExposure').textContent = Math.round(exposure * 100) + ' % investi';

    /* blotter */
    $('#amBlotterBody').innerHTML = S.blotter.slice(0, 20).map(function (b) {
      return '<tr><td class="muted">' + b.clock + '</td><td>' + b.sec + '</td>' +
        '<td class="' + (b.side === 'BUY' ? 'side-buy' : 'side-sell') + '">' + b.side + '</td>' +
        '<td class="r">' + C.fmt(b.qty) + '</td><td class="r">' + b.price.toFixed(2) + '</td>' +
        '<td class="r">' + b.slip.toFixed(1) + '</td></tr>';
    }).join('');
    $('#amFeeTxt').textContent = 'frais ' + C.money(S.fees);

    /* perf bar */
    var bench = A.benchReturn();
    $('#amPerf').innerHTML =
      '<span>portefeuille <b class="' + (ret >= 0 ? 'up' : 'down') + '">' + (ret >= 0 ? '+' : '') + (ret * 100).toFixed(2) + '%</b></span>' +
      '<span>benchmark <b class="' + (bench >= 0 ? 'up' : 'down') + '">' + (bench >= 0 ? '+' : '') + (bench * 100).toFixed(2) + '%</b></span>' +
      '<span>alpha <b class="' + (al >= 0 ? 'up' : 'down') + '">' + (al >= 0 ? '+' : '') + (al * 100).toFixed(2) + '%</b></span>' +
      '<span>drawdown <b>' + (S.maxDD * 100).toFixed(1) + '%</b></span>' +
      '<span>trades <b>' + S.trades + '</b></span>';

    /* ticket */
    var m2 = A.market(M.sel);
    $('#amBuyPx').textContent = m2.offer.toFixed(2);
    $('#amSellPx').textContent = m2.bid.toFixed(2);
    var st2 = A.stock(M.sel);
    var px = M.side === 'SELL' ? m2.bid : m2.offer;
    var qty = px ? Math.floor(M.amount / px) : 0;
    $('#amQty').textContent = C.fmt(qty);
    var slip = A.slipBps(M.amount);
    $('#amSlip').textContent = slip.toFixed(1) + ' bps';
    var after = (Math.abs(st2.pos * st2.mid) + (M.side === 'SELL' ? -M.amount : M.amount)) / Math.max(1, v);
    $('#amWeight').textContent = Math.round(after * 100) + '%';

    /* news */
    if (S.news.length) {
      $('#amNewsCount').textContent = S.news.length;
      $('#amNewsList').innerHTML = S.news.map(function (n) {
        var k = n.all ? 'macro' : n.dir > 0 ? 'up' : 'down';
        var fresh = (S.ms - n.t) < 2600 ? ' fresh' : '';
        return '<div class="news-item' + fresh + '"><div class="news-time">' + n.clock.slice(3) + '</div>' +
          '<div class="news-main"><span class="news-tag ' + k + '">' + n.tag + '</span>' +
          '<div class="news-text">' + C.esc(n.text) + '</div></div></div>';
      }).join('');
    }

    /* status */
    var stt = $('#amStatus');
    if (S.phase !== 'live') { stt.textContent = 'ROUND TERMINÉ'; stt.className = 'foot-right warn'; }
    else if (M.paused) { stt.textContent = 'PAUSE'; stt.className = 'foot-right warn'; }
    else { stt.textContent = 'DESK OUVERT'; stt.className = 'foot-right'; }

    drawChart(S);
  }

  /* ---------------------------------------------------------------- chart */
  function drawChart(S) {
    var c = $('#amChart');
    if (!c) return;
    var wrap = c.parentElement;
    var w = wrap.clientWidth, h = wrap.clientHeight;
    if (!w || !h) return;
    var dpr = window.devicePixelRatio || 1;
    if (c.width !== Math.round(w * dpr) || c.height !== Math.round(h * dpr)) {
      c.width = Math.round(w * dpr);
      c.height = Math.round(h * dpr);
    }
    var ctx = c.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);

    var st = A.stock(M.sel);
    if (!st) return;
    $('#amChartTitle').textContent = st.t + ' · ' + st.mid.toFixed(2) + ' · ' +
      ((st.mid / st.ref - 1) * 100 >= 0 ? '+' : '') + ((st.mid / st.ref - 1) * 100).toFixed(2) + '%';

    var n = M.tf >= 600 ? st.hist.length : Math.min(st.hist.length, Math.round(M.tf / 0.62));
    n = Math.max(2, Math.min(n, st.hist.length));
    var data = st.hist.slice(st.hist.length - n);
    var padL = 6, padR = 58, padT = 10, padB = 18;
    var pw = w - padL - padR, ph = h - padT - padB;
    var min = Math.min.apply(null, data), max = Math.max.apply(null, data);
    if (st.ref < min) min = st.ref;
    if (st.ref > max) max = st.ref;
    var padv = (max - min) * 0.12 || 0.1;
    min -= padv; max += padv;
    var y = function (v) { return padT + ph - (v - min) / (max - min) * ph; };
    var x = function (i) { return padL + (i / (data.length - 1)) * pw; };

    ctx.strokeStyle = 'rgba(28,66,92,.55)';
    ctx.font = '9px ui-monospace, Menlo, monospace';
    ctx.fillStyle = '#5b768c';
    for (var g = 0; g <= 4; g++) {
      var gy = padT + (ph / 4) * g;
      ctx.beginPath(); ctx.moveTo(padL, gy); ctx.lineTo(padL + pw, gy); ctx.stroke();
      ctx.fillText((max - (max - min) * (g / 4)).toFixed(2), padL + pw + 5, gy + 3);
    }
    // ref line
    ctx.save();
    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = 'rgba(160,190,210,.35)';
    ctx.beginPath(); ctx.moveTo(padL, y(st.ref)); ctx.lineTo(padL + pw, y(st.ref)); ctx.stroke();
    ctx.restore();

    if (M.mode === 'candle') {
      var group = Math.max(2, Math.floor(data.length / 32));
      for (var ci = 0; ci < data.length; ci += group) {
        var ch = data.slice(ci, ci + group);
        if (ch.length < 2) break;
        var o = ch[0], cl = ch[ch.length - 1];
        var hi = Math.max.apply(null, ch), lo = Math.min.apply(null, ch);
        var cw = Math.max(2, (pw / (data.length / group)) * 0.6);
        var cx = x(ci + ch.length / 2);
        ctx.strokeStyle = cl >= o ? '#35d07f' : '#ff5f6d';
        ctx.fillStyle = cl >= o ? 'rgba(53,208,127,.5)' : 'rgba(255,95,109,.5)';
        ctx.beginPath(); ctx.moveTo(cx, y(hi)); ctx.lineTo(cx, y(lo)); ctx.stroke();
        ctx.fillRect(cx - cw / 2, y(Math.max(o, cl)), cw, Math.max(1, y(Math.min(o, cl)) - y(Math.max(o, cl))));
      }
    } else {
      var grad = ctx.createLinearGradient(0, padT, 0, padT + ph);
      grad.addColorStop(0, 'rgba(157,140,255,.22)');
      grad.addColorStop(1, 'rgba(157,140,255,0)');
      ctx.beginPath();
      ctx.moveTo(x(0), y(data[0]));
      for (var i = 1; i < data.length; i++) ctx.lineTo(x(i), y(data[i]));
      ctx.lineTo(x(data.length - 1), padT + ph);
      ctx.lineTo(x(0), padT + ph);
      ctx.closePath();
      ctx.fillStyle = grad; ctx.fill();
      ctx.beginPath();
      ctx.moveTo(x(0), y(data[0]));
      for (var j = 1; j < data.length; j++) ctx.lineTo(x(j), y(data[j]));
      ctx.strokeStyle = '#b3a6ff';
      ctx.lineWidth = 1.6;
      ctx.shadowColor = 'rgba(157,140,255,.5)'; ctx.shadowBlur = 6;
      ctx.stroke();
      ctx.shadowBlur = 0;
    }

    var lastPx = data[data.length - 1];
    ctx.fillStyle = 'rgba(157,140,255,.16)';
    ctx.fillRect(padL + pw + 1, y(lastPx) - 8, 54, 16);
    ctx.fillStyle = '#d8d1ff';
    ctx.font = '600 10px ui-monospace, Menlo, monospace';
    ctx.fillText(lastPx.toFixed(2), padL + pw + 5, y(lastPx) + 3.5);
  }

  /* ---------------------------------------------------------------- actions */
  function select(t) {
    M.sel = t;
    $('#amTicker').value = t;
  }

  function buy() { order('BUY'); }
  function sell() { order('SELL'); }

  function order(side) {
    M.side = side;
    var amount = Number($('#amAmount').value) || M.amount;
    M.amount = amount;
    var res = A.trade(M.sel, side, amount);
    if (!res.ok) { C.beep('bad'); C.toast('✕ ' + res.error, 'bad'); return; }
    C.beep('fill');
    C.toast((side === 'BUY' ? 'Acheté ' : 'Vendu ') + C.fmt(res.qty) + ' ' + M.sel +
      ' @ ' + res.price.toFixed(2) + ' · ' + C.money(res.notional) + ' · impact ' + res.slip.toFixed(1) + ' bps', 'good');
    renderAll();
  }

  function sellAll() {
    var res = A.sellAll(M.sel);
    if (!res.ok) { C.toast(res.error, 'warn'); return; }
    C.beep('fill');
    C.toast('Ligne ' + M.sel + ' soldée : ' + C.fmt(res.qty) + ' @ ' + res.price.toFixed(2), 'good');
    renderAll();
  }

  function togglePause() {
    var S = A.get();
    if (!S || S.phase !== 'live') return;
    S.paused = !S.paused;
    M.paused = S.paused;
    $('#amBtnPause').textContent = S.paused ? '▶' : '❚❚';
    if (S.paused) C.toast('Pause — le marché est arrêté.', 'warn');
  }

  /* ---------------------------------------------------------------- end */
  function endRound(data) {
    var sc = data.score, m = sc.metrics;
    var S = A.get();
    var fixes = A.fixes(sc).map(function (f) { return '<li>' + f + '</li>'; }).join('');
    var chained = !!M.callbacks.onContinue;

    var btn = chained
      ? '<button class="btn btn-teal btn-lg" data-am-action="to-ib">Passer au desk Investment Bank →</button>'
      : '<button class="btn btn-teal btn-lg" data-am-action="finish">Voir le débrief →</button>';

    $('#roundModal').innerHTML =
      '<div class="modal-h"><h3>Round 1 — Asset Manager terminé</h3></div>' +
      '<div class="modal-b am-modal">' +
      '<div class="score-hero">' +
      '<div class="score-ring ' + (sc.total >= 70 ? '' : sc.total >= 50 ? 'mid' : 'low') + '">' +
      '<b>' + Math.round(sc.total) + '</b><span>SCORE BUY-SIDE</span></div>' +
      '<h2>' + (m.roiPct >= 90 ? 'Niveau top 100.' : m.roiPct >= 70 ? 'Bon round, encore une marche.' : 'Le ROI score est un percentile : il faut prendre plus de risque juste.') + '</h2>' +
      '<p>ROI <b>' + (m.ret >= 0 ? '+' : '') + (m.ret * 100).toFixed(2) + '%</b> · benchmark ' +
      (m.bench >= 0 ? '+' : '') + (m.bench * 100).toFixed(2) + '% · alpha ' +
      (m.alpha >= 0 ? '+' : '') + (m.alpha * 100).toFixed(2) + '% · <b>percentile ' + m.roiPct + '</b></p></div>' +
      '<div class="rank-band"><div><label>ROI SCORE</label><b>' + Math.round(sc.roi) + '</b></div>' +
      '<div><label>EXECUTION</label><b>' + Math.round(sc.execution) + '</b></div>' +
      '<div><label>BSRM</label><b>' + Math.round(sc.bsrm) + '</b></div>' +
      '<div><label>SCORE</label><b>' + Math.round(sc.total) + '</b></div></div>' +
      '<div class="score-grid"><div class="score-card"><h4>LES 3 MÉTRIQUES BUY-SIDE</h4>' +
      bar('ROI %ile', sc.roi) + bar('EXECUTION', sc.execution) + bar('BSRM', sc.bsrm) +
      '<div class="muted" style="font-size:10px;margin-top:8px">ROI 40 % · EXECUTION 30 % · BSRM 30 %</div></div>' +
      '<div class="score-card"><h4>DÉTECTION</h4>' +
      '<div class="srow"><span class="nm">VALEUR</span><b style="font-family:var(--mono);margin-left:auto;font-size:12px">' + C.money(m.value) + '</b></div>' +
      '<div class="srow"><span class="nm">P&amp;L</span><b style="font-family:var(--mono);margin-left:auto;font-size:12px;color:' + (m.pnl >= 0 ? 'var(--green)' : 'var(--red)') + '">' + C.signedMoney(m.pnl) + '</b></div>' +
      '<div class="srow"><span class="nm">DD MAX</span><b style="font-family:var(--mono);margin-left:auto;font-size:12px">' + (m.maxDD * 100).toFixed(1) + '%</b></div>' +
      '<div class="srow"><span class="nm">EXPO</span><b style="font-family:var(--mono);margin-left:auto;font-size:12px">' + Math.round(m.exposure * 100) + '%</b></div>' +
      '<div class="srow"><span class="nm">TRADES</span><b style="font-family:var(--mono);margin-left:auto;font-size:12px">' + m.trades + '</b></div>' +
      '<div class="srow"><span class="nm">SLIP MOY.</span><b style="font-family:var(--mono);margin-left:auto;font-size:12px">' + m.avgSlip.toFixed(1) + ' bps</b></div>' +
      '<div class="srow"><span class="nm">CLIP MOY.</span><b style="font-family:var(--mono);margin-left:auto;font-size:12px">' + Math.round(m.avgClip * 100) + ' %</b></div>' +
      '<div class="srow"><span class="nm">SOUS STOP</span><b style="font-family:var(--mono);margin-left:auto;font-size:12px">' + m.breachSec + ' s</b></div>' +
      '<div class="srow"><span class="nm">EXPO MOY.</span><b style="font-family:var(--mono);margin-left:auto;font-size:12px">' + Math.round(m.expoAvg * 100) + ' %</b></div>' +
      '<div class="srow"><span class="nm">FRAIS</span><b style="font-family:var(--mono);margin-left:auto;font-size:12px">' + C.money(m.fees) + '</b></div>' +
      '</div></div>' +
      '<div class="score-fixes"><h4>Ce que le buy-side te reproche</h4><ol>' + fixes + '</ol></div>' +
      '<div class="score-actions">' + btn + '</div>' +
      '</div>';

    C.showOverlay('overlayRound');
    M.pending = { score: sc };
    M.roundOver = true;
  }

  function bar(name, v) {
    var k = v >= 70 ? '' : v >= 45 ? 'warn' : 'bad';
    return '<div class="srow"><span class="nm">' + name + '</span><span class="bar"><i class="' + k + '" style="width:' + v + '%"></i></span><span class="vl">' + v + '</span></div>';
  }

  /* ---------------------------------------------------------------- clicks */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-am-action]');
    if (a) {
      var act = a.dataset.amAction;
      C.closeAllOverlays();
      if (act === 'to-ib') {
        stop();
        if (M.callbacks.onContinue) M.callbacks.onContinue({ score: M.pending.score, phase: 'am' });
        return;
      }
      if (act === 'finish') {
        stop();
        if (M.callbacks.onFinish) M.callbacks.onFinish({ score: M.pending.score, phase: 'am' });
        C.setChainAM({ score: M.pending.score, phase: 'am' });
        C.renderScore();
        C.go('score');
        return;
      }
      return;
    }

    var tk = e.target.closest('[data-amticker]');
    if (tk) { select(tk.dataset.amticker); renderAll(); return; }

    var amt = e.target.closest('[data-amt]');
    if (amt) {
      var S = A.get();
      var val = amt.dataset.amt === 'pct15'
        ? Math.round(A.portfolioValue() * 0.15 / 50000) * 50000
        : Number(amt.dataset.amt);
      M.amount = val;
      $('#amAmount').value = val;
      $$('#amSizeChips button').forEach(function (b) { b.classList.toggle('on', b === amt); });
      renderAll();
      return;
    }

    var tfc = e.target.closest('[data-amtf]');
    if (tfc) {
      M.tf = Number(tfc.dataset.amtf);
      $$('[data-amtf]').forEach(function (b) { b.classList.toggle('on', b === tfc); });
      return;
    }
    var md = e.target.closest('[data-ammode]');
    if (md) {
      M.mode = md.dataset.ammode;
      $$('[data-ammode]').forEach(function (b) { b.classList.toggle('on', b === md); });
      return;
    }
  });

  $('#amBuyBtn').addEventListener('click', buy);
  $('#amSellBtn').addEventListener('click', sell);
  $('#amSellAll').addEventListener('click', sellAll);
  $('#amTicker').addEventListener('change', function () { select(this.value); renderAll(); });
  $('#amAmount').addEventListener('input', function () {
    M.amount = Number(this.value) || 0;
    $$('#amSizeChips button').forEach(function (b) { b.classList.remove('on'); });
  });
  $('#amBtnPause').addEventListener('click', togglePause);
  $('#amBtnHelp').addEventListener('click', function () { C.showOverlay('overlayHelp'); });
  $('#amBtnQuit').addEventListener('click', function () {
    if (!confirm('Quitter la session ? Le score en cours sera perdu.')) return;
    stop();
    C.setChainAM(null);
    C.go('hub');
  });

  /* keyboard */
  document.addEventListener('keydown', function (e) {
    var active = document.querySelector('#screen-am.active');
    if (!active) return;
    var tag = e.target.tagName;
    if (tag === 'INPUT' || tag === 'SELECT') {
      if (e.key === 'Enter') { e.preventDefault(); (M.side === 'SELL' ? sell : buy)(); }
      return;
    }
    if (e.key >= '1' && e.key <= '5') {
      var S = A.get();
      if (S && S.stocks[Number(e.key) - 1]) { select(S.stocks[Number(e.key) - 1].t); renderAll(); }
      e.preventDefault();
      return;
    }
    var k = e.key.toLowerCase();
    if (k === 'b') buy();
    else if (k === 's') sell();
    else if (k === 'f') sellAll();
    else if (e.code === 'Space') { e.preventDefault(); togglePause(); }
  });

  window.AM = { start: start, stop: stop };
})();
