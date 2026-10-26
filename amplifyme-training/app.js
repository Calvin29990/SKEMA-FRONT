/* ==========================================================================
   AMPLIFYME TRAINER — UI layer
   ========================================================================== */
(function () {
  'use strict';

  var E = window.Engine;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  var settings = { rounds: 2, roundSec: 180, difficulty: 'normal', wheels: true, sound: true };
  var UI = {
    screen: 'hub', sel: 'BP', chat: 'DEAL', posTab: 'positions',
    tf: 180, mode: 'line', sma: true, unread: {}, chatSig: '', last: 0,
    audio: null, newsRendered: -1, loop: null, qtyTouched: false
  };

  /* ---------------------------------------------------------------- utils */
  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function fmt(n) { return Math.round(n).toLocaleString('en-US'); }
  function money(n) {
    var s = n < 0 ? '-' : '';
    return s + '$' + fmt(Math.abs(n));
  }
  function signedMoney(n) {
    return (n > 0 ? '+' : n < 0 ? '-' : '') + '$' + fmt(Math.abs(n));
  }
  function numSigned(n) { return (n > 0 ? '+' : '') + fmt(n); }
  function mmss(ms) {
    var t = Math.max(0, Math.ceil(ms / 1000));
    var m = Math.floor(t / 60), s = t % 60;
    return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
  }
  function cls(n) { return n > 0 ? 'num-pos' : n < 0 ? 'num-neg' : 'muted'; }

  function toast(text, kind) {
    var wrap = $('#toastWrap');
    var el = document.createElement('div');
    el.className = 'toast ' + (kind || '');
    el.innerHTML = text;
    wrap.appendChild(el);
    while (wrap.children.length > 3) wrap.removeChild(wrap.firstChild);
    setTimeout(function () { if (el.parentNode) el.parentNode.removeChild(el); }, kind === 'bad' ? 4200 : 3200);
  }

  function tone(freq, at, dur, type, vol) {
    try {
      var ctx = UI.audio;
      var o = ctx.createOscillator(), g = ctx.createGain();
      o.type = type || 'sine';
      o.frequency.value = freq;
      o.connect(g); g.connect(ctx.destination);
      var t0 = ctx.currentTime + at;
      g.gain.setValueAtTime(0.0001, t0);
      g.gain.exponentialRampToValueAtTime(vol || 0.07, t0 + 0.012);
      g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
      o.start(t0); o.stop(t0 + dur + 0.02);
    } catch (e) { /* ignore */ }
  }
  function beep(kind) {
    if (!settings.sound) return;
    try {
      if (!UI.audio) UI.audio = new (window.AudioContext || window.webkitAudioContext)();
      if (UI.audio.state === 'suspended') UI.audio.resume();
    } catch (e) { return; }
    if (kind === 'rfq') { tone(880, 0, 0.10, 'triangle', 0.06); tone(1180, 0.11, 0.10, 'triangle', 0.055); }
    else if (kind === 'fill') { tone(620, 0, 0.12, 'sine', 0.06); }
    else if (kind === 'bad') { tone(190, 0, 0.28, 'sawtooth', 0.05); }
    else if (kind === 'news') { tone(440, 0, 0.09, 'square', 0.035); tone(330, 0.10, 0.14, 'square', 0.03); }
    else if (kind === 'end') { tone(520, 0, 0.14, 'sine', 0.06); tone(390, 0.16, 0.22, 'sine', 0.05); }
  }

  /* ---------------------------------------------------------------- nav */
  function go(id) {
    if (UI.screen === 'drills' && id !== 'drills') stopDrill(false);
    UI.screen = id;
    $$('.screen').forEach(function (s) { s.classList.remove('active'); });
    var el = $('#screen-' + id);
    if (el) el.classList.add('active');
    if (id !== 'sim') closeAllOverlays();
    window.scrollTo(0, 0);
    if (id === 'cheat' || id === 'hub') {
      var sc = $('#screen-' + id);
      if (sc) sc.scrollTop = 0;
    }
  }
  function closeAllOverlays() {
    $$('.overlay').forEach(function (o) { o.classList.remove('show'); });
  }
  function showOverlay(id) { $('#' + id).classList.add('show'); }

  /* ---------------------------------------------------------------- setup */
  function seg(id, key, numeric) {
    var el = $('#' + id);
    if (!el) return;
    el.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      $$('button', el).forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
      if (key === 'wheels' || key === 'sound') settings[key] = b.dataset.val === 'on';
      else settings[key] = numeric ? Number(b.dataset.val) : b.dataset.val;
      if (key === 'sound') $('#btnSound').textContent = settings.sound ? '🔊' : '🔇';
    });
  }
  seg('optRounds', 'rounds', true);
  seg('optDuration', 'roundSec', true);
  seg('optDiff', 'difficulty');
  seg('optWheels', 'wheels');
  seg('optSound', 'sound');

  /* ---------------------------------------------------------------- session */
  var sessionStarted = false;

  function startIB() {
    E.init(settings);
    E.on(onEngineEvent);
    E.start();
    UI.sel = 'BP';
    UI.chat = 'DEAL';
    UI.unread = {};
    UI.newsRendered = -1;
    UI.chatSig = '';
    UI.tf = settings.roundSec === 300 ? 300 : 180;
    sessionStarted = true;

    $('#qTicker').value = 'BP';
    $('#xTicker').value = 'BP';
    $('#xQty').value = 0;
    $('#qBid').value = '';
    $('#qOffer').value = '';
    $('#qValid').value = 45;
    $('#qBidVol').value = 50000;
    $('#qOfferVol').value = 50000;
    $('#newsList').innerHTML = '';
    $('#blotterBody').innerHTML = '';
    $('#btnSound').textContent = settings.sound ? '🔊' : '🔇';
    $('#roundTot').textContent = settings.rounds;

    renderNews();
    renderChat();
    setChartChips();
    go('sim');
    startLoop();
    E.get().paused = true;
    showIntro({
      title: 'Round — Investment Bank',
      lead: 'Tu es le desk. Les clients t\'envoient des RFQ dans le chat, tu leur donnes un prix à deux sens, ils tapent, tu hedges.',
      points: [
        'Une <b>RFQ arrive</b> (chat + bannière ambre) : tu quotes <b>bid &lt; mid &lt; offer</b> en moins de 10 s.',
        'Le client tape : tu prends la position. <b><kbd>B</kbd> / <kbd>S</kbd></b> pour te hedger au marché, <kbd>F</kbd> pour flat.',
        '<b>News = reprice.</b> <kbd>X</kbd> annule toutes tes quotes avant qu\'elles ne soient snipées.',
        'Objectif : <b>100 % des RFQ répondues</b>, zéro fat finger, <b>flat à la cloche</b>.'
      ],
      keys: [
        ['<kbd>1</kbd>–<kbd>5</kbd>', 'choisir le ticker'],
        ['<kbd>M</kbd>', 'prix au mid ± 5 bps'],
        ['<kbd>↵</kbd>', 'envoyer la quote'],
        ['<kbd>X</kbd>', 'tout annuler']
      ],
      resume: function () { var S2 = E.get(); if (S2) S2.paused = false; $('#btnPause').textContent = '❚❚'; setTimeout(function () { $('#qBid').focus(); }, 60); }
    });
    toast('Desk Investment Bank — réponds à la première RFQ. <kbd>M</kbd> centre ton prix sur le mid.', 'good');
  }

  var chainAM = null;

  function startSession() {
    stopSession();
    go('am');
    window.AM.start(settings, {
      chained: true,
      onContinue: function (res) { chainAM = res; startIB(); },
      onFinish: function (res) { chainAM = res; }
    });
  }

  function startAMOnly() {
    stopSession();
    go('am');
    window.AM.start(settings, {
      chained: false,
      onContinue: null,
      onFinish: function (res) { chainAM = res; }
    });
  }

  function stopSession() {
    var S = E.get();
    if (S) S.running = false;
    if (UI.loop) { clearInterval(UI.loop); UI.loop = null; }
    sessionStarted = false;
    if (window.AM) window.AM.stop();
  }

  function startLoop() {
    if (UI.loop) return;
    UI.last = performance.now();
    UI.loop = setInterval(uiTick, 150);
  }

  function uiTick() {
    var now = performance.now();
    var dt = Math.min(500, now - UI.last);
    UI.last = now;
    var S = E.get();
    if (!S) return;
    E.step(dt);
    if (UI.screen !== 'sim') return;

    renderTop(S);
    renderEquities(S);
    renderPositions(S);
    renderBlotter(S);
    renderLiveQuotes(S);
    renderRfqBanner(S);
    renderTicketCalc(S);
    renderDepth(S);
    renderChart(S);
    $('#xNotional').textContent = money((Number($('#xQty').value) || 0) * (E.stock(UI.sel) ? E.stock(UI.sel).mid : 0));
    renderChatIfDirty(S);
  }

  /* ---------------------------------------------------------------- engine events */
  function onEngineEvent(type, data) {
    if (type === 'toast') { toast(data.text, data.kind); return; }
    if (type === 'chat') { UI.chatSig = ''; return; }
    if (type === 'news') {
      beep('news');
      renderNews();
      var np = $('.panel.news');
      np.style.transition = 'none'; np.style.boxShadow = '0 0 0 2px rgba(255,176,32,.7)';
      setTimeout(function () { np.style.transition = '.5s'; np.style.boxShadow = 'none'; }, 450);
      return;
    }
    if (type === 'rfq') {
      beep('rfq');
      UI.unread[data.client] = (UI.unread[data.client] || 0) + 1;
      UI.chatSig = '';
      selectTicker(data.ticker, true);
      $('#qValid').value = 45;
      $('#qBidVol').value = data.size;
      $('#qOfferVol').value = data.size;
      if (settings.wheels) fillFromMid(10);
      else { $('#qBid').value = ''; $('#qOffer').value = ''; }
      UI.qtyTouched = false;
      var panel = $('#panelTicket');
      panel.classList.remove('flash'); void panel.offsetWidth; panel.classList.add('flash');
      if (!settings.wheels) setTimeout(function () { $('#qBid').focus(); }, 60);
      return;
    }
    if (type === 'fill') {
      beep('fill');
      selectTicker(data.ticker, false);
      $('#xQty').value = Math.abs(data.pos);
      UI.qtyTouched = false;
      if (data.pos === 0) $('#xQty').value = 0;
      return;
    }
    if (type === 'picked') { beep('bad'); return; }
    if (type === 'pass') { toast('Le client passe — quote trop large. Tightens de 2–3 bps.', 'warn'); return; }
    if (type === 'tighten') { toast('Le client demande de resserrer — tu as 9 secondes.', 'warn'); beep('rfq'); return; }
    if (type === 'missed') { beep('bad'); return; }
    if (type === 'hedge') {
      $('#xQty').value = Math.abs(data.pos);
      return;
    }
    if (type === 'quoteCancelAll') { return; }
    if (type === 'roundEnd') {
      beep('end');
      showRoundModal(data);
      return;
    }
    if (type === 'roundStart') {
      closeAllOverlays();
      toast('Round ' + data.round + ' — positions remises à zéro. Le flux accélère.', 'good');
      return;
    }
  }

  /* ---------------------------------------------------------------- render: top */
  function renderTop(S) {
    $('#marketClock').textContent = E.fmtClock(S.clockMs);
    var real = E.totalRealised(), un = E.totalUnrealised(), comm = S.commission, tot = E.totalPnl();
    var mr = $('#mRealised'), mu = $('#mUnrealised'), mc = $('#mCommission'), mt = $('#mTotal');
    mr.textContent = numSigned(real); mr.className = cls(real);
    mu.textContent = numSigned(un); mu.className = cls(un);
    mc.textContent = numSigned(comm);
    mt.textContent = numSigned(tot); mt.className = 'c-amber';

    var rem = Math.max(0, S.opts.roundSec * 1000 - S.ms);
    var rc = $('#roundClock');
    rc.textContent = mmss(rem);
    rc.className = 'rc-clock' + (rem < 10000 ? ' danger' : rem < 30000 ? ' warn' : '');
    $('#roundNo').textContent = S.round;

    var maxUtil = 0;
    S.stocks.forEach(function (st) { maxUtil = Math.max(maxUtil, Math.abs(st.pos) / E.POS_LIMIT); });
    var stTxt = $('#deskStatus');
    if (S.phase === 'roundEnd' || S.phase === 'done') { stTxt.textContent = 'ROUND TERMINÉ'; stTxt.className = 'foot-right warn'; }
    else if (maxUtil > 1) { stTxt.textContent = '⚠ LIMITE DÉPASSÉE'; stTxt.className = 'foot-right danger'; }
    else if (S.paused) { stTxt.textContent = 'PAUSE'; stTxt.className = 'foot-right warn'; }
    else { stTxt.textContent = 'DESK OUVERT'; stTxt.className = 'foot-right'; }
  }

  /* ---------------------------------------------------------------- render: equities */
  function renderEquities(S) {
    var html = '';
    S.stocks.forEach(function (st) {
      var m = E.quoteMarket(st);
      var chg = (st.mid / st.ref - 1) * 100;
      var posTxt = st.pos === 0 ? '—' : numSigned(st.pos);
      html += '<tr data-ticker="' + st.t + '" class="' + (UI.sel === st.t ? 'sel' : '') + '">' +
        '<td>' + st.t + '</td>' +
        '<td class="r num-pos">' + m.bid.toFixed(2) + '</td>' +
        '<td class="r num-neg">' + m.offer.toFixed(2) + '</td>' +
        '<td class="r ' + cls(chg) + '">' + (chg >= 0 ? '+' : '') + chg.toFixed(2) + '%</td>' +
        '<td class="r ' + cls(st.pos) + '">' + posTxt + '</td></tr>';
    });
    $('#equitiesBody').innerHTML = html;
    $('#eqClock').textContent = E.fmtClock(S.clockMs).slice(0, 5);
    var total = S.stocks.reduce(function (a, st) { return a + st.pos * st.mid; }, 0);
    $('#eqFoot').innerHTML = '<span>' + S.stocks.length + ' lignes · spread ~6 bps</span><span>NET ' + numSigned(total) + '</span>';
  }

  /* ---------------------------------------------------------------- render: positions */
  function renderPositions(S) {
    var html = '', count = 0, maxUtil = 0, gross = 0;
    S.stocks.forEach(function (st) {
      var un = st.pos * (st.mid - st.avg);
      var util = Math.abs(st.pos) / E.POS_LIMIT;
      maxUtil = Math.max(maxUtil, util);
      gross += Math.abs(st.pos * st.mid);
      if (st.pos !== 0) count++;
      html += '<tr class="' + (UI.sel === st.t ? 'sel' : '') + '">' +
        '<td>' + st.t + '</td>' +
        '<td class="r ' + cls(st.pos) + '">' + (st.pos === 0 ? '—' : numSigned(st.pos)) + '</td>' +
        '<td class="r ' + (st.pos === 0 ? 'muted' : '') + '">' + (st.pos === 0 ? '—' : st.avg.toFixed(2)) + '</td>' +
        '<td class="r ' + cls(un) + '">' + (st.pos === 0 ? '—' : numSigned(Math.round(un))) + '</td>' +
        '<td class="r ' + cls(st.realised) + '">' + (st.realised === 0 ? '—' : numSigned(Math.round(st.realised))) + '</td>' +
        '<td class="r ' + (util > 1 ? 'num-neg' : util > 0.7 ? '' : 'muted') + '">' + (st.pos === 0 ? '0%' : Math.round(util * 100) + '%') + '</td></tr>';
    });
    $('#positionsBody').innerHTML = html;
    $('#posCount').textContent = count + ' open';
    $('#riskBar').style.width = Math.min(100, maxUtil * 100) + '%';
    $('#riskLimitTxt').textContent = fmt(E.POS_LIMIT) + ' / ligne';
    $('#exposureTxt').textContent = money(gross);
  }

  function renderBlotter(S) {
    var rows = S.blotter.slice(0, 60).map(function (b) {
      return '<tr><td class="muted">' + b.clock + '</td><td>' + b.sec + '</td>' +
        '<td class="' + (b.side === 'BUY' ? 'side-buy' : 'side-sell') + '">' + b.side + '</td>' +
        '<td class="r">' + fmt(b.qty) + '</td><td class="r">' + b.price.toFixed(2) + '</td>' +
        '<td class="r">' + fmt(b.notional) + '</td></tr>';
    }).join('');
    if (!rows) rows = '<tr><td colspan="6" class="muted" style="padding:12px;font-family:var(--sans)">Aucun trade. Réponds à la RFQ en cours.</td></tr>';
    $('#blotterBody').innerHTML = rows;
  }

  /* ---------------------------------------------------------------- render: quotes */
  function renderLiveQuotes(S) {
    var qs = E.liveQuotes();
    $('#liveCount').textContent = qs.length;
    if (!qs.length) {
      $('#liveQuotesBody').innerHTML = '';
      $('#liveEmpty').style.display = 'block';
      return;
    }
    $('#liveEmpty').style.display = 'none';
    var html = qs.map(function (q) {
      var left = Math.max(0, (q.expiresAt - S.ms) / 1000);
      var pct = Math.max(0, Math.min(100, (q.expiresAt - S.ms) / (q.valid * 1000) * 100));
      return '<tr><td>' + q.ticker + '</td><td class="r">' + fmt(q.bidVol) + '</td>' +
        '<td class="r num-pos">' + q.bid.toFixed(2) + '</td><td class="r num-neg">' + q.offer.toFixed(2) + '</td>' +
        '<td class="r">' + fmt(q.offerVol) + '</td>' +
        '<td class="r">' + Math.ceil(left) + 's<div class="valid-bar"><i style="width:' + pct + '%"></i></div></td>' +
        '<td><button class="live-x" data-cancel="' + q.id + '" title="Annuler">✕</button></td></tr>';
    }).join('');
    $('#liveQuotesBody').innerHTML = html;
  }

  function renderRfqBanner(S) {
    var open = S.rfqs.filter(function (r) { return r.status === 'open'; })
      .sort(function (a, b) { return a.deadline - b.deadline; });
    var b = $('#rfqBanner');
    if (!open.length) {
      b.classList.remove('live');
      $('#rbText').textContent = 'Aucune RFQ en cours — surveille le chat.';
      $('#rbBar').style.width = '0%';
      return;
    }
    var r = open[0];
    b.classList.add('live');
    var left = Math.max(0, (r.deadline - S.ms) / 1000);
    var pct = Math.max(0, Math.min(100, (r.deadline - S.ms) / 20000 * 100));
    var sideTxt = r.hint ? (r.side === 'BUY' ? ' · ACHETEUR' : ' · VENDEUR') : '';
    $('#rbText').innerHTML = '<b>' + r.client + '</b> · ' + fmt(r.size) + ' ' + r.ticker + sideTxt + ' · <b>' + Math.ceil(left) + 's</b>' +
      (open.length > 1 ? ' <span class="muted">(+' + (open.length - 1) + ')</span>' : '');
    $('#rbBar').style.width = pct + '%';
  }

  function renderTicketCalc(S) {
    var st = E.stock($('#qTicker').value) || E.stock(UI.sel);
    if (!st) return;
    var bid = Number($('#qBid').value), offer = Number($('#qOffer').value);
    var bv = Number($('#qBidVol').value), ov = Number($('#qOfferVol').value);
    var parts = [];
    if (bid > 0 && offer > 0 && offer > bid) {
      var spreadBps = (offer - bid) / st.mid * 10000;
      parts.push('<span>spread ' + spreadBps.toFixed(1) + ' bps</span>');
      var warn = '';
      if (bid >= st.mid) warn = 'BID AU-DESSUS DU MID';
      else if (offer <= st.mid) warn = 'OFFER SOUS LE MID';
      else if (spreadBps < 3) warn = 'TROP SERRÉ';
      else if (spreadBps > 30) warn = 'TROP LARGE';
      if (warn) parts.push('<span class="' + (warn === 'TROP LARGE' ? '' : 'danger') + '">⚠ ' + warn + '</span>');
    } else if (bid > 0 && offer > 0 && bid >= offer) {
      parts.push('<span class="danger">⚠ BID ≥ OFFER — CROISÉ</span>');
    }
    parts.push('<span>mid ' + st.mid.toFixed(2) + '</span>');
    parts.push('<span>notionnel ' + money((bv || 0) * st.mid) + '</span>');
    $('#tkCalc').innerHTML = parts.join('');
    $('#ticketHint').textContent = $('#qTicker').value + ' · ' + st.mid.toFixed(2);
  }

  function renderDepth(S) {
    var st = E.stock(UI.sel);
    if (!st) return;
    var m = E.quoteMarket(st);
    var dBid = E.depthFor(UI.sel, 'SELL', 0);
    var dAsk = E.depthFor(UI.sel, 'BUY', 0);
    var rows = ['<div class="depth-row head"><span class="dsz r">BID SZ</span><span>BID</span><span>ASK</span><span class="dsz">ASK SZ</span></div>'];
    for (var i = 0; i < 3; i++) {
      var lvB = dBid.levels[i];
      var lvA = dAsk.levels[i];
      rows.push('<div class="depth-row">' +
        '<span class="dsz r">' + fmt(lvB.size) + '</span>' +
        '<span class="dpx bid">' + lvB.px.toFixed(2) + '</span>' +
        '<span class="dpx ask">' + lvA.px.toFixed(2) + '</span>' +
        '<span class="dsz">' + fmt(lvA.size) + '</span></div>');
    }
    $('#depth').innerHTML = rows.join('');
    $('#xSell').textContent = m.bid.toFixed(2);
    $('#xBuy').textContent = m.offer.toFixed(2);
    var qty = Number($('#xQty').value) || 0;
    if (qty > 0) {
      var bd = E.depthFor(UI.sel, 'SELL', qty);
      var ad = E.depthFor(UI.sel, 'BUY', qty);
      $('#xImpact').textContent = 'S ' + (bd.slipBps).toFixed(1) + ' / B ' + (ad.slipBps).toFixed(1) + ' bps';
    } else {
      $('#xImpact').textContent = '—';
    }
  }

  /* ---------------------------------------------------------------- render: chart */
  function renderChart(S) {
    var canvas = $('#chartCanvas');
    if (!canvas) return;
    var wrap = canvas.parentElement;
    var w = wrap.clientWidth, h = wrap.clientHeight;
    if (!w || !h) return;
    var dpr = window.devicePixelRatio || 1;
    if (canvas.width !== Math.round(w * dpr) || canvas.height !== Math.round(h * dpr)) {
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
    }
    var ctx = canvas.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);

    var st = E.stock(UI.sel);
    if (!st) return;
    $('#chartTitle').textContent = st.t + ' · ' + st.mid.toFixed(2);

    var n = UI.tf >= 600 ? st.hist.length : Math.min(st.hist.length, Math.round(UI.tf / 0.62));
    n = Math.max(2, Math.min(n, st.hist.length));
    var data = st.hist.slice(st.hist.length - n);

    var padL = 6, padR = 62, padT = 12, padB = 20;
    var plotW = w - padL - padR, plotH = h - padT - padB;
    var volH = Math.max(16, plotH * 0.16);
    var priceH = plotH - volH - 6;

    var min = Math.min.apply(null, data), max = Math.max.apply(null, data);
    if (st.ref < min) min = st.ref; if (st.ref > max) max = st.ref;
    var pad = (max - min) * 0.12 || 0.1;
    min -= pad; max += pad;
    var y = function (v) { return padT + priceH - (v - min) / (max - min) * priceH; };
    var x = function (i) { return padL + (i / (data.length - 1)) * plotW; };

    // grid
    ctx.strokeStyle = 'rgba(28,66,92,.55)'; ctx.lineWidth = 1;
    ctx.font = '9px ui-monospace, Menlo, monospace';
    ctx.fillStyle = '#5b768c';
    for (var g = 0; g <= 4; g++) {
      var gy = padT + (priceH / 4) * g;
      ctx.beginPath(); ctx.moveTo(padL, gy); ctx.lineTo(padL + plotW, gy); ctx.stroke();
      var val = max - (max - min) * (g / 4);
      ctx.fillText(val.toFixed(2), padL + plotW + 6, gy + 3);
    }
    for (var gx = 0; gx <= 4; gx++) {
      var xx = padL + (plotW / 4) * gx;
      ctx.beginPath(); ctx.moveTo(xx, padT); ctx.lineTo(xx, padT + priceH); ctx.stroke();
      var idx = Math.round((data.length - 1) * (gx / 4));
      var tBack = (data.length - 1 - idx) * 0.62;
      var backMs = Math.max(0, S.clockMs - tBack * 1000);
      ctx.fillText(E.fmtClock(backMs).slice(3), xx + 3, padT + priceH + 13);
    }

    // previous close
    if (st.ref >= min && st.ref <= max) {
      ctx.save();
      ctx.setLineDash([4, 4]); ctx.strokeStyle = 'rgba(160,190,210,.35)';
      ctx.beginPath(); ctx.moveTo(padL, y(st.ref)); ctx.lineTo(padL + plotW, y(st.ref)); ctx.stroke();
      ctx.restore();
    }

    // volume (activity proxy)
    ctx.fillStyle = 'rgba(59,142,234,.22)';
    for (var vi = 1; vi < data.length; vi++) {
      var act = Math.abs(data[vi] - data[vi - 1]) / (max - min);
      var bh = Math.max(1, act * volH * 4);
      var bw = Math.max(1, plotW / data.length - 0.4);
      ctx.fillRect(x(vi), h - padB - bh, bw, bh);
    }

    if (UI.mode === 'candle') {
      var group = Math.max(2, Math.floor(data.length / 34));
      for (var ci = 0; ci < data.length; ci += group) {
        var chunk = data.slice(ci, ci + group);
        if (chunk.length < 2) break;
        var o = chunk[0], c = chunk[chunk.length - 1];
        var hi = Math.max.apply(null, chunk), lo = Math.min.apply(null, chunk);
        var cw = Math.max(2, (plotW / (data.length / group)) * 0.62);
        var cx = x(ci + chunk.length / 2);
        ctx.strokeStyle = c >= o ? '#35d07f' : '#ff5f6d';
        ctx.fillStyle = c >= o ? 'rgba(53,208,127,.55)' : 'rgba(255,95,109,.55)';
        ctx.beginPath(); ctx.moveTo(cx, y(hi)); ctx.lineTo(cx, y(lo)); ctx.stroke();
        var y1 = y(Math.max(o, c)), y2 = y(Math.min(o, c));
        ctx.fillRect(cx - cw / 2, y1, cw, Math.max(1, y2 - y1));
      }
    } else {
      var grad = ctx.createLinearGradient(0, padT, 0, padT + priceH);
      grad.addColorStop(0, 'rgba(47,227,196,.20)');
      grad.addColorStop(1, 'rgba(47,227,196,0)');
      ctx.beginPath();
      ctx.moveTo(x(0), y(data[0]));
      for (var i = 1; i < data.length; i++) ctx.lineTo(x(i), y(data[i]));
      ctx.lineTo(x(data.length - 1), padT + priceH);
      ctx.lineTo(x(0), padT + priceH);
      ctx.closePath();
      ctx.fillStyle = grad; ctx.fill();

      ctx.beginPath();
      ctx.moveTo(x(0), y(data[0]));
      for (var j = 1; j < data.length; j++) ctx.lineTo(x(j), y(data[j]));
      ctx.strokeStyle = '#2fe3c4'; ctx.lineWidth = 1.6;
      ctx.shadowColor = 'rgba(47,227,196,.5)'; ctx.shadowBlur = 6;
      ctx.stroke();
      ctx.shadowBlur = 0;

      if (UI.sma && data.length > 12) {
        var period = 20, sum = 0;
        ctx.beginPath();
        for (var k = 0; k < data.length; k++) {
          sum += data[k];
          if (k >= period) sum -= data[k - period];
          if (k >= period - 1) {
            var avg = sum / period;
            if (k === period - 1) ctx.moveTo(x(k), y(avg)); else ctx.lineTo(x(k), y(avg));
          }
        }
        ctx.strokeStyle = 'rgba(255,176,32,.85)'; ctx.lineWidth = 1;
        ctx.stroke();
      }
    }

    // last price
    var last = data[data.length - 1];
    ctx.fillStyle = '#2fe3c4';
    ctx.beginPath(); ctx.arc(x(data.length - 1), y(last), 2.6, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = 'rgba(47,227,196,.14)';
    ctx.fillRect(padL + plotW + 2, y(last) - 8, 56, 16);
    ctx.fillStyle = '#7ff5e2';
    ctx.font = '600 10px ui-monospace, Menlo, monospace';
    ctx.fillText(last.toFixed(2), padL + plotW + 6, y(last) + 3.5);
  }

  /* ---------------------------------------------------------------- render: chat */
  function renderChatIfDirty(S) {
    var msgs = S.chat[UI.chat] || [];
    var sig = UI.chat + '|' + msgs.length + '|' + (msgs.length ? msgs[msgs.length - 1].t : 0);
    if (sig !== UI.chatSig) { UI.chatSig = sig; renderChat(); }
  }

  function renderChat() {
    var S = E.get();
    if (!S) return;
    var chans = [{ id: 'DEAL', label: 'Deal Room' }].concat(S.clients.map(function (c) {
      return { id: c.id, label: c.short };
    }));
    $('#chatTabs').innerHTML = chans.map(function (c) {
      var un = UI.unread[c.id] || 0;
      return '<button class="chat-tab ' + (UI.chat === c.id ? 'on' : '') + '" data-chat="' + c.id + '">' +
        c.label + (un ? '<span class="badge">' + un + '</span>' : '') + '</button>';
    }).join('');

    var msgs = S.chat[UI.chat] || [];
    $('#chatList').innerHTML = msgs.map(function (m) {
      if (m.from === 'SYS') return '<div class="msg sys">' + esc(m.text) + '</div>';
      var name = m.from === 'ME' ? 'YOU' : m.from;
      var klass = m.from === 'ME' ? 'me' : (m.kind === 'rfq' ? 'rfq' : (m.kind === 'alert' ? 'alert' : ''));
      return '<div class="msg ' + klass + '"><div class="msg-name" style="color:' +
        (m.from === 'ME' ? 'var(--teal)' : m.from === 'HF1' ? '#5fa8f5' : m.from === 'HF2' ? '#c39bff' : '#ffb020') + '">' +
        name + '<span class="t">' + E.fmtClock(m.t) + '</span></div>' +
        '<div class="msg-text">' + esc(m.text) + '</div></div>';
    }).join('');

    var body = $('#chatBody');
    body.scrollTop = body.scrollHeight;
    var quick = $('#chatQuick');
    if (quick) quick.style.display = UI.chat === 'DEAL' ? 'none' : 'flex';
  }

  function sendChat(text) {
    var S = E.get();
    if (!S) return;
    text = (text || '').trim();
    if (!text) return;
    E.push(UI.chat, 'ME', text);
    $('#chatInput').value = '';
    UI.chatSig = '';
    renderChat();
  }

  /* ---------------------------------------------------------------- render: news */
  function renderNews() {
    var S = E.get();
    if (!S) return;
    if (!S.news.length) {
      $('#newsList').innerHTML = '<div class="news-empty">Les headlines arrivent ici. Chaque news déplace le mid — et peut sniper tes quotes laissées en vie.</div>';
      return;
    }
    $('#newsList').innerHTML = S.news.map(function (n) {
      var target = n.all ? null : Object.keys(n.impacts).sort(function (a, b) { return Math.abs(n.impacts[b]) - Math.abs(n.impacts[a]); })[0];
      var imp = target ? n.impacts[target] : n.dir;
      var k = n.all ? 'macro' : imp > 0 ? 'up' : 'down';
      var fresh = (S.ms - n.t) < 2600 ? ' fresh' : '';
      var move = target ? ' <span class="muted">(' + target + ' ' + (n.impacts[target] >= 0 ? '+' : '') + n.impacts[target].toFixed(0) + ' bps)</span>' : '';
      return '<div class="news-item' + fresh + '"><div class="news-time">' + n.clock.slice(3) + '</div>' +
        '<div class="news-main"><span class="news-tag ' + k + '">' + n.tag + '</span>' +
        '<div class="news-text">' + esc(n.text) + move + '</div></div></div>';
    }).join('');
    $('#newsCount').textContent = S.news.length;
  }

  /* ---------------------------------------------------------------- ticket actions */
  function selectTicker(t, keepQty) {
    UI.sel = t;
    $('#qTicker').value = t;
    $('#xTicker').value = t;
    $('#chartTitle').textContent = t;
    if (!keepQty && !UI.qtyTouched) {
      var st = E.stock(t);
      $('#xQty').value = st ? Math.abs(st.pos) : 0;
    }
    renderChart(E.get());
  }

  function fillFromMid(spreadBps) {
    var st = E.stock($('#qTicker').value);
    if (!st) return;
    var hs = st.mid * (spreadBps / 2) / 10000;
    var bid = Math.round((st.mid - hs) * 100) / 100;
    var offer = Math.round((st.mid + hs) * 100) / 100;
    if (bid >= offer) { bid = st.mid - 0.01; offer = st.mid + 0.01; }
    $('#qBid').value = bid.toFixed(2);
    $('#qOffer').value = offer.toFixed(2);
    if (!Number($('#qBidVol').value)) $('#qBidVol').value = 50000;
    if (!Number($('#qOfferVol').value)) $('#qOfferVol').value = 50000;
  }

  function sendQuote() {
    var st = E.get();
    if (!st || st.phase !== 'live') { toast('Le round est terminé.', 'warn'); return; }
    var res = E.sendQuote({
      ticker: $('#qTicker').value,
      bid: $('#qBid').value,
      offer: $('#qOffer').value,
      bidVol: $('#qBidVol').value,
      offerVol: $('#qOfferVol').value,
      valid: $('#qValid').value
    });
    if (!res.ok) {
      beep('bad');
      toast('✕ ' + res.error, 'bad');
      return;
    }
    beep('fill');
    $('#qBid').value = '';
    $('#qOffer').value = '';
    // enchaîne sur la RFQ suivante
    var S = E.get();
    var next = S.rfqs.filter(function (r) { return r.status === 'open'; })
      .sort(function (a, b) { return a.deadline - b.deadline; })[0];
    if (next) {
      selectTicker(next.ticker, true);
      $('#qBidVol').value = next.size;
      $('#qOfferVol').value = next.size;
      if (settings.wheels) fillFromMid(10);
      toast('Quote envoyée. RFQ suivante : ' + next.client + ' · ' + fmt(next.size) + ' ' + next.ticker, 'good');
    } else {
      toast('Quote envoyée — en vie ' + $('#qValid').value + ' s.', 'good');
    }
    setTimeout(function () { $('#qBid').focus(); }, 40);
  }

  function hedge(side) {
    var qty = Math.round(Number($('#xQty').value));
    if (!qty) {
      var st = E.stock(UI.sel);
      qty = st ? Math.abs(st.pos) : 0;
    }
    if (!qty) { toast('Renseigne une quantité dans EXCHANGE.', 'warn'); return; }
    var res = E.hedge(UI.sel, side, qty);
    if (!res.ok) { beep('bad'); toast('✕ ' + res.error, 'bad'); return; }
    beep('fill');
    var st = E.stock(UI.sel);
    $('#xQty').value = Math.abs(st.pos);
    toast((side === 'BUY' ? 'Acheté ' : 'Vendu ') + fmt(qty) + ' ' + UI.sel + ' @ ' + res.price.toFixed(2) +
      ' · slip ' + res.slip.toFixed(1) + ' bps', 'good');
  }

  function flattenSel() {
    var res = E.flatten(UI.sel);
    if (!res.ok) { toast(res.error, 'warn'); return; }
    beep('fill');
    $('#xQty').value = 0;
    toast('Flat sur ' + UI.sel + '.', 'good');
  }

  /* ---------------------------------------------------------------- overlays / modals */
  function ringClass(v) { return v >= 70 ? '' : v >= 50 ? 'mid' : 'low'; }
  function scoreBars(sc) {
    var rows = [
      ['COMM', sc.comm], ['P&L', sc.pnlScore], ['RISK', sc.risk], ['REL', sc.rel], ['FFC', sc.ffcScore]
    ];
    return rows.map(function (r) {
      var c = r[1] >= 70 ? '' : r[1] >= 45 ? 'warn' : 'bad';
      return '<div class="srow"><span class="nm">' + r[0] + '</span><span class="bar"><i class="' + c + '" style="width:' + r[1] + '%"></i></span><span class="vl">' + r[1] + '</span></div>';
    }).join('');
  }

  function showRoundModal(data) {
    var sc = data.score, rs = data.roundStats;
    var openTxt = rs.openLines.length
      ? '<b>' + rs.openLines.map(function (l) { return fmt(Math.abs(l.pos)) + ' ' + l.t + (l.pos > 0 ? ' long' : ' short'); }).join(', ') + '</b> clôturée(s) au mid — coût ' + money(rs.closeCost) + '.'
      : 'Aucune position ouverte à la cloche. <b>Parfait.</b>';
    var btn = data.isLast
      ? '<button class="btn btn-teal btn-lg" data-action="final">Voir le débrief final →</button>'
      : '<button class="btn btn-teal btn-lg" data-action="next-round">Lancer le round ' + (rs.round + 1) + ' →</button>';

    $('#roundModal').innerHTML =
      '<div class="modal-h"><h3>Round ' + rs.round + ' / ' + E.get().opts.rounds + ' terminé</h3></div>' +
      '<div class="modal-b">' +
      '<div class="score-hero"><div class="score-ring ' + ringClass(sc.total) + '"><b>' + Math.round(sc.total) + '</b><span>SCORE CUMULÉ</span></div>' +
      '<h2>' + (sc.total >= 70 ? 'Propre.' : sc.total >= 50 ? 'Correct, mais il y a du gras.' : 'Trop de points laissés.') + '</h2>' +
      '<p>Ce round : ' + rs.trades + ' trades · ' + money(rs.commission) + ' de commission · ' + rs.ffc + ' FFC · ' +
      rs.answered + '/' + rs.rfqTotal + ' RFQ répondues</p></div>' +
      '<div class="round-banner">' + openTxt + '</div>' +
      '<div class="score-grid"><div class="score-card"><h4>COMPOSANTES DU SCORE</h4>' + scoreBars(sc) + '</div>' +
      '<div class="score-card"><h4>DÉTECTION DU ROUND</h4>' +
      '<div class="srow"><span class="nm">RFQ</span><span class="bar"><i class="' + (rs.answered / Math.max(1, rs.rfqTotal) > .9 ? '' : 'warn') + '" style="width:' + Math.round(rs.answered / Math.max(1, rs.rfqTotal) * 100) + '%"></i></span><span class="vl">' + rs.answered + '/' + rs.rfqTotal + '</span></div>' +
      '<div class="srow"><span class="nm">SNIPES</span><span class="bar"><i class="' + (rs.sniped ? 'bad' : '') + '" style="width:' + Math.min(100, rs.sniped * 25) + '%"></i></span><span class="vl">' + rs.sniped + '</span></div>' +
      '<div class="srow"><span class="nm">RISK</span><span class="bar"><i class="' + (rs.avgUtil > .6 ? 'warn' : '') + '" style="width:' + Math.round(Math.min(1, rs.avgUtil) * 100) + '%"></i></span><span class="vl">' + Math.round(rs.avgUtil * 100) + '%</span></div>' +
      '<div class="srow"><span class="nm">FFC</span><span class="bar"><i class="' + (rs.ffc ? 'bad' : '') + '" style="width:' + Math.min(100, rs.ffc * 30) + '%"></i></span><span class="vl">' + rs.ffc + '</span></div>' +
      '</div></div>' +
      '<div class="score-fixes"><h4>À corriger au prochain round</h4><ol>' +
      E.fixes(sc).map(function (f) { return '<li>' + f + '</li>'; }).join('') + '</ol></div>' +
      '<div class="score-actions">' + btn + '</div>' +
      '</div>';
    showOverlay('overlayRound');
  }

  function renderScore() {
    if (!E.get() || !E.get().elapsedMs) {
      if (chainAM && chainAM.score) { renderAmOnlyScore(chainAM.score); return; }
      go('hub'); return;
    }
    var sc = E.score(), S = E.get();
    var amHtml = '';
    if (chainAM && chainAM.score) {
      var am = chainAM.score, amm = am.metrics;
      amHtml = '<div class="round-banner" style="border-left-color:var(--violet);background:linear-gradient(90deg,rgba(157,140,255,.14),transparent)">' +
        '<b>ROUND 1 — ASSET MANAGER</b> · score <b>' + Math.round(am.total) + '/100</b> (note ' + am.grade + ') · ' +
        'return <b>' + (amm.ret >= 0 ? '+' : '') + (amm.ret * 100).toFixed(2) + '%</b> · benchmark ' +
        (amm.bench >= 0 ? '+' : '') + (amm.bench * 100).toFixed(2) + '% · alpha <b>' + (amm.alpha >= 0 ? '+' : '') +
        (amm.alpha * 100).toFixed(2) + '%</b> · drawdown ' + (amm.maxDD * 100).toFixed(1) + '% · ' + amm.trades + ' trades</div>';
    }
    var m = sc.metrics;
    var fixList = E.fixes(sc).map(function (f) { return '<li>' + f + '</li>'; }).join('');
    var verdict = m.answeredRatio >= 0.95 ? 'Flux maîtrisé' : m.answeredRatio >= 0.7 ? 'Flux partiel' : 'Flux perdu';
    $('#scoreContent').innerHTML =
      '<a class="back" data-go="hub">← Hub</a>' +
      '<div class="kicker">DÉBRIEF DE SESSION</div>' + amHtml +
      '<div class="score-hero">' +
      '<div class="score-ring ' + ringClass(sc.total) + '"><b>' + Math.round(sc.total) + '</b><span>SCORE / 100</span></div>' +
      '<h2>Note ' + sc.grade + ' — ' + verdict + '</h2>' +
      '<p>' + S.round + ' round(s) · ' + Math.round(S.elapsedMs / 1000) + ' s de marché · ' +
      m.trades + ' trades client · ' + money(m.commission) + ' de commission</p></div>' +
      '<div class="score-grid">' +
      '<div class="score-card"><h4>TES 5 COMPOSANTES</h4>' + scoreBars(sc) +
      '<div class="muted" style="font-size:10px;margin-top:8px">COMM 30 % · P&L 25 % · RISK 20 % · REL 15 % · FFC 10 %</div></div>' +
      '<div class="score-card"><h4>LES MÉTRIQUES AMPLIFYME</h4>' +
      '<div class="srow"><span class="nm">NUMT</span><b style="font-family:var(--mono);font-size:15px">' + m.numt + '</b><span class="muted" style="font-size:10px;margin-left:auto">trades client</span></div>' +
      '<div class="srow"><span class="nm">COMM</span><b style="font-family:var(--mono);font-size:15px">' + money(m.commission) + '</b><span class="muted" style="font-size:10px;margin-left:auto">8 bps / trade</span></div>' +
      '<div class="srow"><span class="nm">FFC</span><b style="font-family:var(--mono);font-size:15px;color:' + (m.ffc ? 'var(--red)' : 'var(--green)') + '">' + m.ffc + '</b><span class="muted" style="font-size:10px;margin-left:auto">fat fingers</span></div>' +
      '<div class="srow"><span class="nm">SSRM</span><b style="font-family:var(--mono);font-size:15px">' + m.ssrm + '/100</b><span class="muted" style="font-size:10px;margin-left:auto">risque sell-side</span></div>' +
      '</div></div>' +
      '<div class="score-grid">' +
      '<div class="score-card"><h4>P&L &amp; EXÉCUTION</h4>' +
      kv('P&L total', money(m.pnl), m.pnl >= 0) +
      kv('Réalisé', money(m.realised), m.realised >= 0) +
      kv('Unrealised', money(m.unrealised), m.unrealised >= 0) +
      kv('Commission', money(m.commission), true) +
      kv('Coût de clôture', money(m.settlement), false) +
      '</div>' +
      '<div class="score-card"><h4>RELATION &amp; RISQUE</h4>' +
      kv('RFQ répondues', m.answered + ' / ' + m.rfqTotal, m.answeredRatio > 0.9) +
      kv('Temps moyen', m.avgResp ? m.avgResp.toFixed(1) + ' s' : '—', m.avgResp < 10) +
      kv('Pick-offs', m.sniped, m.sniped === 0) +
      kv('Exposition moy.', Math.round(m.avgUtil * 100) + ' %', m.avgUtil < 0.5) +
      kv('Exposition max', Math.round(m.maxUtil * 100) + ' %', m.maxUtil < 1) +
      kv('Confiance clients', Math.round(m.trust) + ' / 100', m.trust > 60) +
      '</div></div>' +
      '<div class="score-fixes" style="border-left-color:var(--teal)"><h4 style="color:var(--teal)">Objectif top 100 — la barre à passer demain</h4>' +
      '<ol style="margin-left:18px;font-size:12.5px;line-height:1.8;color:#b9cfdf">' +
      '<li>Score ≥ <b>85/100</b> ici, avec <b>0 fat finger</b> et <b>100 % des RFQ</b> répondues.</li>' +
      '<li><b>Flat à la cloche</b> sur toutes les lignes, à chaque round.</li>' +
      '<li>Côté buy-side : <b>alpha positif</b> et drawdown &lt; 1 %.</li>' +
      '</ol></div>' +
      '<div class="score-fixes"><h4>Les 4 choses à corriger avant demain</h4><ol>' + fixList + '</ol></div>' +
      '<div class="score-actions">' +
      '<button class="btn btn-teal btn-lg" data-action="replay">Refaire une session</button>' +
      '<button class="btn btn-ghost btn-lg" data-go="drills">10 min de drills</button>' +
      '<button class="btn btn-ghost btn-lg" data-go="cheat">Relire la fiche</button>' +
      '</div>' +
      '<p class="muted" style="text-align:center;font-size:11px;margin-top:24px">Score absolu calibré pour l\'entraînement — AmplifyME classe en percentile face aux autres candidats, pas sur cette échelle.</p>';
  }

  function renderAmOnlyScore(am) {
    var m = am.metrics;
    var fixes = window.EngineAM.fixes(am).map(function (f) { return '<li>' + f + '</li>'; }).join('');
    var bar = function (name, v) {
      var k = v >= 70 ? '' : v >= 45 ? 'warn' : 'bad';
      return '<div class="srow"><span class="nm">' + name + '</span><span class="bar"><i class="' + k + '" style="width:' + v + '%"></i></span><span class="vl">' + v + '</span></div>';
    };
    $('#scoreContent').innerHTML =
      '<a class="back" data-go="hub">← Hub</a>' +
      '<div class="kicker">DÉBRIEF · ASSET MANAGER</div>' +
      '<div class="score-hero">' +
      '<div class="score-ring ' + (am.total >= 70 ? '' : am.total >= 50 ? 'mid' : 'low') + '"><b>' + Math.round(am.total) + '</b><span>SCORE BUY-SIDE</span></div>' +
      '<h2>Note ' + am.grade + ' — ' + (m.alpha > 0.001 ? 'alpha positif' : m.alpha > -0.001 ? 'flat' : 'le marché gagne') + '</h2>' +
      '<p>Return ' + (m.ret >= 0 ? '+' : '') + (m.ret * 100).toFixed(2) + '% · benchmark ' +
      (m.bench >= 0 ? '+' : '') + (m.bench * 100).toFixed(2) + '% · alpha ' +
      (m.alpha >= 0 ? '+' : '') + (m.alpha * 100).toFixed(2) + '% · ' + m.trades + ' trades</p></div>' +
      '<div class="score-grid"><div class="score-card"><h4>COMPOSANTES</h4>' +
      bar('ALPHA', am.alphaScore) + bar('RISQUE', am.risk) + bar('ACTIVITÉ', am.activity) + bar('DISCIPLINE', am.discipline) + '</div>' +
      '<div class="score-card"><h4>DÉTECTION</h4>' +
      kv('Valeur', money(m.value), m.pnl >= 0) + kv('P&L', signedMoney(m.pnl), m.pnl >= 0) +
      kv('Drawdown max', (m.maxDD * 100).toFixed(1) + ' %', m.maxDD < 0.01) +
      kv('Exposition', Math.round(m.exposure * 100) + ' %', m.exposure > 0.6) +
      kv('Concentration', Math.round(m.concentration * 100) + ' %', m.concentration < 0.4) +
      kv('Frais', money(m.fees), m.fees < 6000) + '</div></div>' +
      '<div class="score-fixes"><h4>À corriger</h4><ol>' + fixes + '</ol></div>' +
      '<div class="score-actions">' +
      '<button class="btn btn-teal btn-lg" data-start="am">Refaire le round buy-side</button>' +
      '<button class="btn btn-ghost btn-lg" data-go="brief">Session complète (AM + IB)</button>' +
      '</div>';
    go('score');
  }

  function kv(k, v, good) {
    return '<div class="srow"><span class="nm" style="width:104px;font-size:10px">' + k + '</span>' +
      '<b style="font-family:var(--mono);font-size:12px;margin-left:auto;color:' + (good ? 'var(--green)' : 'var(--muted)') + '">' + v + '</b></div>';
  }

  /* ---------------------------------------------------------------- drills */
  var Drill = null;
  var drillTimer = null;

  function renderDrillMenu() {
    $('#drillGrid').innerHTML = window.Drills.meta.map(function (m) {
      return '<button class="drill-card" data-drill="' + m.id + '"><div class="di">' + m.ico + '</div>' +
        '<h4>' + m.name + '</h4><p>' + m.desc + '</p></button>';
    }).join('');
  }

  function startDrill(mode) {
    if (Drill && Drill.timer) clearInterval(Drill.timer);
    var types = mode === 'all' ? window.Drills.meta.map(function (m) { return m.id; }) : [mode];
    Drill = {
      mode: mode, types: types, i: 0, endAt: performance.now() + 60000,
      score: 0, streak: 0, best: 0, correct: 0, total: 0, times: [],
      byType: {}, locked: false, q: null, qStart: 0, timer: null
    };
    $('#drillMenu').style.display = 'none';
    $('#drillResult').style.display = 'none';
    $('#drillRun').style.display = 'block';
    $('#drillName').textContent = mode === 'all' ? 'Circuit complet' : window.Drills.meta.filter(function (m) { return m.id === mode; })[0].name;
    $('#drillScore').textContent = '0';
    $('#drillStreak').textContent = '0';
    nextDrillQ();
    Drill.timer = setInterval(function () {
      if (!Drill) return;
      var left = Math.max(0, Drill.endAt - performance.now());
      var el = $('#drillClock');
      el.textContent = Math.ceil(left / 1000);
      el.className = 'drill-clock' + (left < 10000 ? ' warn' : '');
      if (left <= 0) finishDrill();
    }, 100);
  }

  function drillTypeStats(type) {
    if (!Drill.byType[type]) Drill.byType[type] = { total: 0, correct: 0 };
    return Drill.byType[type];
  }

  function nextDrillQ() {
    if (!Drill) return;
    if (performance.now() >= Drill.endAt) { finishDrill(); return; }
    var type = Drill.types[Drill.i % Drill.types.length];
    Drill.i++;
    var q = window.Drills.make(type);
    Drill.q = q;
    Drill.qStart = performance.now();
    Drill.locked = false;
    var meta = window.Drills.meta.filter(function (m) { return m.id === type; })[0];
    $('#drillName').textContent = meta.name;

    var html = '<div class="drill-q">' + q.prompt + (q.sub ? '<span class="sub">' + q.sub + '</span>' : '') + '</div>';
    if (q.table) {
      html += '<div class="drill-table"><table><thead><tr>' + q.table.head.map(function (h) { return '<th>' + h + '</th>'; }).join('') + '</tr></thead><tbody>' +
        q.table.rows.map(function (row) {
          return '<tr>' + row.map(function (c, i) { return '<td>' + (i === 0 ? '<b>' + c + '</b>' : c) + '</td>'; }).join('') + '</tr>';
        }).join('') + '</tbody></table></div>';
    }
    if (q.fields) {
      html += '<div class="drill-inputs">' + q.fields.map(function (f) {
        return '<div class="fi"><label>' + f.label + '</label><input data-dk="' + f.key + '" type="text" inputmode="decimal" autocomplete="off" placeholder="0.00"></div>';
      }).join('') + '</div>';
      html += '<button class="btn btn-teal btn-lg" id="btnDrillSubmit">VALIDER ↵</button>';
    } else {
      html += '<div class="drill-opts">' + q.options.map(function (o, idx) {
        return '<button class="drill-opt" data-opt="' + idx + '"><span class="k">' + (idx + 1) + '</span><span>' + o + '</span></button>';
      }).join('') + '</div>';
    }
    html += '<div id="drillFeedback"></div>';
    $('#drillStage').innerHTML = html;
    $('#drillFoot').innerHTML = '<span class="muted" style="font-family:var(--mono);font-size:10px">' +
      (Drill.mode === 'all' ? 'RÉPONSE RAPIDE = BONUS. Mauvaise réponse = série remise à zéro.' : 'OBJECTIF : 100 % À 60 S.') + '</span>';

    var first = $('#drillStage input');
    if (first) setTimeout(function () { first.focus(); }, 30);
  }

  function drillGrade(q, vals) {
    if (q.options) return vals.opt === q.correct;
    if (q.type === 'twoway') {
      return Math.abs(vals.bid - q.answer.bid) <= q.tol && Math.abs(vals.offer - q.answer.offer) <= q.tol;
    }
    return Math.abs(vals.val - q.answer.val) <= q.tol;
  }

  function submitDrill(vals) {
    if (!Drill || Drill.locked) return;
    Drill.locked = true;
    var q = Drill.q;
    var elapsed = (performance.now() - Drill.qStart) / 1000;
    var ok = drillGrade(q, vals);
    Drill.total++;
    var ts = drillTypeStats(q.type);
    ts.total++;
    var fb = $('#drillFeedback');
    var pts = 0;
    if (ok) {
      Drill.correct++; ts.correct++;
      Drill.streak++;
      Drill.best = Math.max(Drill.best, Drill.streak);
      pts = 10 + (elapsed < 4 ? 5 : elapsed < 7 ? 3 : 0) + Math.min(10, (Drill.streak - 1) * 2);
      Drill.score += pts;
      Drill.times.push(elapsed);
      fb.className = 'drill-feedback ok';
      fb.innerHTML = '✓ <b>Correct</b> (+' + pts + ') — ' + q.explain;
      beep('fill');
    } else {
      Drill.streak = 0;
      fb.className = 'drill-feedback ko';
      var good = q.options ? q.options[q.correct] : (q.type === 'twoway' ? q.answer.bid.toFixed(2) + ' / ' + q.answer.offer.toFixed(2) : fmt(q.answer.val));
      fb.innerHTML = '✕ <b>Raté</b> — bonne réponse : <b>' + good + '</b>.<br>' + q.explain;
      beep('bad');
    }
    $('#drillScore').textContent = Drill.score;
    $('#drillStreak').textContent = Drill.streak;
    $$('#drillStage input').forEach(function (i) { i.disabled = true; });
    var sub = $('#btnDrillSubmit'); if (sub) sub.disabled = true;
    if (q.options) {
      $$('#drillStage .drill-opt').forEach(function (b, idx) {
        b.disabled = true;
        if (idx === q.correct) b.classList.add('right');
        else if (vals.opt === idx) b.classList.add('wrong');
        else b.classList.add('dim');
      });
    }
    setTimeout(function () {
      if (!Drill) return;
      if (performance.now() >= Drill.endAt) finishDrill();
      else nextDrillQ();
    }, ok ? 1050 : 1900);
  }

  function finishDrill() {
    if (!Drill) return;
    if (Drill.timer) clearInterval(Drill.timer);
    Drill.timer = null;
    var d = Drill;
    Drill = null;
    $('#drillRun').style.display = 'none';
    $('#drillResult').style.display = 'block';
    var acc = d.total ? d.correct / d.total : 0;
    var avg = d.times.length ? d.times.reduce(function (a, b) { return a + b; }, 0) / d.times.length : 0;
    var weakest = Object.keys(d.byType).sort(function (a, b) {
      var ra = d.byType[a].correct / Math.max(1, d.byType[a].total);
      var rb = d.byType[b].correct / Math.max(1, d.byType[b].total);
      return ra - rb;
    })[0];
    var nameOf = function (id) {
      var m = window.Drills.meta.filter(function (x) { return x.id === id; })[0];
      return m ? m.name : id;
    };
    var advice = acc >= 0.9
      ? 'Solide. Passe en revue la fiche demain matin, puis une session <b>Chaos</b> sans roues.'
      : 'Refais 60 s sur <b>' + nameOf(weakest) + '</b> : c\'est là que tu perds le plus de points.';
    $('#drillResult').innerHTML =
      '<div class="drill-result">' +
      '<div class="kicker">RÉSULTAT · 60 S</div>' +
      '<h3>' + (acc >= 0.85 ? 'Réflexes prêts.' : acc >= 0.6 ? 'Ça vient.' : 'À travailler.') + '</h3>' +
      '<div class="stat-row">' +
      '<div class="stat"><b>' + d.score + '</b><span>points</span></div>' +
      '<div class="stat"><b>' + Math.round(acc * 100) + '%</b><span>précision</span></div>' +
      '<div class="stat"><b>' + d.correct + '/' + d.total + '</b><span>correct</span></div>' +
      '<div class="stat"><b>' + (avg ? avg.toFixed(1) + ' s' : '—') + '</b><span>temps / réponse</span></div>' +
      '</div>' +
      '<div class="advice">' + advice + '</div>' +
      '<div style="margin:22px 0">' + Object.keys(d.byType).map(function (k) {
        var t = d.byType[k];
        return '<div class="srow"><span class="nm" style="width:130px">' + nameOf(k) + '</span><span class="bar"><i class="' + (t.correct / t.total >= .8 ? '' : 'warn') + '" style="width:' + Math.round(t.correct / t.total * 100) + '%"></i></span><span class="vl">' + t.correct + '/' + t.total + '</span></div>';
      }).join('') + '</div>' +
      '<div class="score-actions">' +
      '<button class="btn btn-teal" data-drill-again="' + d.mode + '">Rejouer 60 s</button>' +
      '<button class="btn btn-ghost" data-drill="' + (d.mode === 'all' ? 'twoway' : 'all') + '">' + (d.mode === 'all' ? 'Bid / Offer' : 'Circuit complet') + '</button>' +
      '<button class="btn btn-ghost" data-go="brief">Session complète</button>' +
      '</div></div>';
  }

  function stopDrill(silent) {
    if (Drill && Drill.timer) clearInterval(Drill.timer);
    Drill = null;
    if (!silent) {
      $('#drillRun').style.display = 'none';
      $('#drillMenu').style.display = 'block';
      $('#drillResult').style.display = 'none';
    }
  }

  /* ---------------------------------------------------------------- keyboard */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      if ($('#overlayRound').classList.contains('show')) return;
      if ($('#overlayPause').classList.contains('show')) { togglePause(); return; }
      closeAllOverlays();
      return;
    }
    if (UI.screen === 'drills' && Drill) {
      if (e.target.tagName === 'INPUT') {
        if (e.key === 'Enter') { e.preventDefault(); const v = readDrillVals(); submitDrill(v); }
        return;
      }
      if (/^[1-4]$/.test(e.key) && Drill.q && Drill.q.options) {
        var idx = Number(e.key) - 1;
        if (idx < Drill.q.options.length) submitDrill({ opt: idx });
        e.preventDefault();
      }
      return;
    }
    if (UI.screen !== 'sim') return;
    var tag = e.target.tagName;
    if (tag === 'INPUT' || tag === 'SELECT' || tag === 'TEXTAREA') {
      if (e.key === 'Enter') {
        if (e.target.id === 'chatInput') { e.preventDefault(); sendChat($('#chatInput').value); }
        else if (['qBid', 'qOffer', 'qBidVol', 'qOfferVol', 'qValid'].indexOf(e.target.id) >= 0) { e.preventDefault(); sendQuote(); }
        else if (e.target.id === 'xQty') { e.preventDefault(); $('#xQty').blur(); }
      }
      return;
    }
    if (e.key >= '1' && e.key <= '5') {
      var idx2 = Number(e.key) - 1;
      var st = E.get().stocks[idx2];
      if (st) selectTicker(st.t);
      e.preventDefault();
      return;
    }
    var k = e.key.toLowerCase();
    if (k === 'm') { fillFromMid(10); toast('Bid/offer centrés sur le mid (± 5 bps).', 'good'); }
    else if (k === 'x') { E.cancelAll(); UI.chatSig = ''; }
    else if (k === 'b') hedge('BUY');
    else if (k === 's') hedge('SELL');
    else if (k === 'f') flattenSel();
    else if (k === '?') showOverlay('overlayHelp');
    else if (e.code === 'Space') { e.preventDefault(); togglePause(); }
  });

  function readDrillVals() {
    var v = {};
    $$('#drillStage input').forEach(function (i) {
      var raw = String(i.value).trim().replace(/\s/g, '');
      var key = i.dataset.dk;
      if (raw.indexOf(',') >= 0 && raw.indexOf('.') < 0) {
        raw = raw.split(',').length === 2 ? raw.replace(',', '.') : raw.replace(/,/g, '');
      } else {
        raw = raw.replace(/,/g, '');
      }
      v[key] = Number(raw);
    });
    return v;
  }

  /* ---------------------------------------------------------------- pause */
  function togglePause() {
    var S = E.get();
    if (!S || S.phase !== 'live') return;
    S.paused = !S.paused;
    if (S.paused) showOverlay('overlayPause'); else $('#overlayPause').classList.remove('show');
    $('#btnPause').textContent = S.paused ? '▶' : '❚❚';
  }

  /* ---------------------------------------------------------------- clicks */
  document.addEventListener('click', function (e) {
    var goEl = e.target.closest('[data-go]');
    if (goEl) { go(goEl.dataset.go); return; }

    var stEl = e.target.closest('[data-start]');
    if (stEl) { if (stEl.dataset.start === 'am') startAMOnly(); return; }

    var act = e.target.closest('[data-action]');
    if (act) {
      var a = act.dataset.action;
      if (a === 'next-round') { closeAllOverlays(); E.nextRound(); return; }
      if (a === 'final') { closeAllOverlays(); renderScore(); go('score'); return; }
      if (a === 'replay') { chainAM = null; startSession(); return; }
      return;
    }

    var drillEl = e.target.closest('[data-drill]');
    if (drillEl) { startDrill(drillEl.dataset.drill); return; }
    var again = e.target.closest('[data-drill-again]');
    if (again) { startDrill(again.dataset.drillAgain); return; }

    var ch = e.target.closest('[data-chat]');
    if (ch) { UI.chat = ch.dataset.chat; UI.unread[UI.chat] = 0; UI.chatSig = ''; renderChat(); return; }

    var tab = e.target.closest('[data-tab]');
    if (tab) {
      UI.posTab = tab.dataset.tab;
      $$('#posTabs .tab').forEach(function (t) { t.classList.toggle('on', t === tab); });
      $('#positionsView').style.display = UI.posTab === 'positions' ? 'block' : 'none';
      $('#blotterView').style.display = UI.posTab === 'blotter' ? 'table' : 'none';
      return;
    }

    var eq = e.target.closest('[data-ticker]');
    if (eq) { selectTicker(eq.dataset.ticker); return; }

    var cx = e.target.closest('[data-cancel]');
    if (cx) { E.cancelQuote(cx.dataset.cancel); uiTick(); return; }

    var opt = e.target.closest('[data-opt]');
    if (opt) { submitDrill({ opt: Number(opt.dataset.opt) }); return; }

    var close = e.target.closest('[data-close]');
    if (close) { $('#' + close.dataset.close).classList.remove('show'); return; }
  });

  /* buttons */
  $('#btnStartSim').addEventListener('click', startSession);
  $('#btnSendQuote').addEventListener('click', sendQuote);
  $('#btnMid').addEventListener('click', function () { fillFromMid(10); });
  $('#xSellBtn').addEventListener('click', function () { hedge('SELL'); });
  $('#xBuyBtn').addEventListener('click', function () { hedge('BUY'); });
  $('#xFlatten').addEventListener('click', flattenSel);
  $('#btnResume').addEventListener('click', togglePause);
  $('#btnPause').addEventListener('click', togglePause);
  $('#btnHelp').addEventListener('click', function () { showOverlay('overlayHelp'); });
  $('#btnSound').addEventListener('click', function () {
    settings.sound = !settings.sound;
    this.textContent = settings.sound ? '🔊' : '🔇';
    var segs = $$('#optSound button');
    segs.forEach(function (b) { b.classList.toggle('on', (b.dataset.val === 'on') === settings.sound); });
  });
  $('#btnQuit').addEventListener('click', function () {
    if (!confirm('Quitter la session ? Le score en cours sera perdu.')) return;
    stopSession();
    chainAM = null;
    go('hub');
  });
  $('#btnDrillAll').addEventListener('click', function () { startDrill('all'); });
  $('#btnDrillQuit').addEventListener('click', function () { stopDrill(false); });
  $('#chatSend').addEventListener('click', function () { sendChat($('#chatInput').value); });
  $('#chatInput').addEventListener('keydown', function (e) {
    if (e.key === 'Enter') { e.preventDefault(); sendChat(this.value); }
  });
  $('#qTicker').addEventListener('change', function () { selectTicker(this.value, true); });
  $('#xTicker').addEventListener('change', function () { selectTicker(this.value); });
  $('#xQty').addEventListener('input', function () { UI.qtyTouched = true; });
  $('#qBid').addEventListener('input', function () { UI.qtyTouched = true; });

  // chart chips
  $$('.chart-tools [data-tf]').forEach(function (b) {
    b.addEventListener('click', function () {
      UI.tf = Number(b.dataset.tf);
      $$('.chart-tools [data-tf]').forEach(function (x) { x.classList.toggle('on', x === b); });
    });
  });
  $$('.chart-tools [data-mode]').forEach(function (b) {
    b.addEventListener('click', function () {
      UI.mode = b.dataset.mode;
      $$('.chart-tools [data-mode]').forEach(function (x) { x.classList.toggle('on', x === b); });
    });
  });
  $$('.chart-tools [data-sma]').forEach(function (b) {
    b.addEventListener('click', function () {
      UI.sma = !UI.sma;
      b.classList.toggle('on', UI.sma);
    });
  });

  function setChartChips() {
    UI.tf = settings.roundSec === 480 ? 600 : 180;
    $$('.chart-tools [data-tf]').forEach(function (x) {
      x.classList.toggle('on', Number(x.dataset.tf) === UI.tf);
    });
    $$('.chart-tools [data-mode]').forEach(function (x) { x.classList.toggle('on', x.dataset.mode === 'line'); });
    $$('.chart-tools [data-sma]').forEach(function (x) { x.classList.add('on'); });
  }

  /* chat quick replies */
  var quick = document.createElement('div');
  quick.className = 'chat-quick';
  quick.id = 'chatQuick';
  quick.innerHTML = ['Coming up.', 'Working on it.', 'Done.', 'I have to pull my quote.'].map(function (t) {
    return '<button data-quick="' + t + '">' + t + '</button>';
  }).join('');
  $('.chat-input-row').parentNode.insertBefore(quick, $('.chat-input-row'));
  quick.addEventListener('click', function (e) {
    var b = e.target.closest('[data-quick]');
    if (b) sendChat(b.dataset.quick);
  });

  /* ---------------------------------------------------------------- intro */
  function showIntro(cfg) {
    $('#introModal').innerHTML =
      '<div class="modal-h"><h3>' + cfg.title + '</h3></div>' +
      '<div class="modal-b">' +
      (cfg.lead ? '<p class="modal-note" style="margin-top:0;margin-bottom:14px">' + cfg.lead + '</p>' : '') +
      '<ol class="intro-list">' + cfg.points.map(function (p) { return '<li>' + p + '</li>'; }).join('') + '</ol>' +
      (cfg.keys ? '<div class="keys-grid" style="margin-top:14px">' + cfg.keys.map(function (k) {
        return '<div>' + k[0] + '<span>' + k[1] + '</span></div>';
      }).join('') + '</div>' : '') +
      '<div class="score-actions" style="margin-top:18px">' +
      '<button class="btn btn-teal btn-lg" id="introStart">' + (cfg.cta || 'Je suis prêt — lancer le round') + '</button>' +
      '</div></div>';
    showOverlay('overlayIntro');
    $('#introStart').addEventListener('click', function () {
      $('#overlayIntro').classList.remove('show');
      if (cfg.resume) cfg.resume();
    }, { once: true });
  }

  /* ---------------------------------------------------------------- AppCore */
  window.AppCore = {
    go: go,
    toast: toast,
    beep: beep,
    settings: settings,
    esc: esc,
    fmt: fmt,
    money: money,
    signedMoney: signedMoney,
    numSigned: numSigned,
    mmss: mmss,
    cls: cls,
    showOverlay: showOverlay,
    closeAllOverlays: closeAllOverlays,
    renderScore: renderScore,
    startIB: startIB,
    showIntro: showIntro,
    getChainAM: function () { return chainAM; },
    setChainAM: function (v) { chainAM = v; }
  };

  /* ---------------------------------------------------------------- boot */
  renderDrillMenu();
  $$('.overlay').forEach(function (o) {
    o.addEventListener('click', function (e) { if (e.target === o && o.id !== 'overlayRound') o.classList.remove('show'); });
  });
  go('hub');
})();
