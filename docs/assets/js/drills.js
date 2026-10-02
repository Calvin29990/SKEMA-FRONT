/* ═══════════════════════════════════════════════════════════════
   drills.js — générateurs déterministes (déductif clairsemé,
   inductif non ambigu, concentration E+points, switch codes,
   multi-tâches, learning) + banque numérique (6 feuilles, 37 énoncés).
   Assessment Trainer — Calvin MINANG — usage personnel.
   ═══════════════════════════════════════════════════════════════ */
'use strict';

const DRILL = (() => {

  const rng = U.rng, int = U.int, pick = U.pick, shuffle = U.shuffle;

  /* ══════════════════ DÉDUCTIF — grille 4×4 clairsemée ══════════════════
     Une ligne complète + la colonne du trou (sauf le trou) sont révélées :
     la case « ? » admet alors une solution unique (contrainte de colonne). */
  function dedItem(seed, i) {
    const r = rng(seed);
    const sym = shuffle(r, [0, 1, 2, 3]);
    const rows = shuffle(r, [0, 1, 2, 3]);
    const cols = shuffle(r, [0, 1, 2, 3]);
    const g = [];
    for (let y = 0; y < 4; y++) { g.push([]); for (let x = 0; x < 4; x++) g[y].push(sym[(rows[y] + cols[x]) % 4]); }
    const hr = int(r, 0, 3), hc = int(r, 0, 3);
    const fullRow = (hr + int(r, 1, 3)) % 4;                 /* ligne révélée ≠ ligne du trou */
    const shown = {};
    for (let x = 0; x < 4; x++) shown[fullRow + ',' + x] = g[fullRow][x];
    for (let y = 0; y < 4; y++) if (y !== hr && y !== fullRow) shown[y + ',' + hc] = g[y][hc];
    if (r() < 0.5) {                                        /* indice supplémentaire occasionnel */
      let y = int(r, 0, 3), x = int(r, 0, 3), guard = 0;
      while ((y === hr && x === hc) || shown[y + ',' + x] != null || y === fullRow || x === hc) { y = int(r, 0, 3); x = int(r, 0, 3); if (++guard > 20) break; }
      if (guard <= 20) shown[y + ',' + x] = g[y][x];
    }
    const ans = g[hr][hc];
    const opts = shuffle(r, [0, 1, 2, 3]);
    return { id: 'D' + i, kind: 'latin', grid: g, shown, hole: [hr, hc], options: opts, ans: opts.indexOf(ans) };
  }

  /* ══════════════════ INDUCTIF — 2 exemples / 4 candidates ══════════════════ */
  const IRULES = [
    { id: 'corners', ok: g => g[0] === g[2] && g[0] === g[6] && g[0] === g[8] },
    { id: 'row',     ok: g => [0, 3, 6].some(y => g[y] === g[y + 1] && g[y] === g[y + 2]) },
    { id: 'col',     ok: g => [0, 1, 2].some(x => g[x] === g[x + 3] && g[x] === g[x + 6]) },
    { id: 'mirror',  ok: g => [0, 3, 6].every(y => g[y] === g[y + 2]) },
    { id: 'ring',    ok: g => g[0] === g[1] && g[1] === g[2] && g[2] === g[5] && g[5] === g[8] && g[8] === g[7] && g[7] === g[6] && g[6] === g[3] }
  ];
  function gridFor(rule, r) {
    const g = new Array(9).fill(int(r, 0, 3));
    const k = () => int(r, 0, 3);
    if (rule.id === 'corners') { const c = k(); [0, 2, 6, 8].forEach(i => g[i] = c); g[4] = (c + 1 + int(r, 0, 2)) % 4; [1, 3, 5, 7].forEach(i => g[i] = k()); }
    else if (rule.id === 'row') { const y = pick(r, [0, 3, 6]), c = k(); [0, 1, 2].forEach(d => g[y + d] = c); g.forEach((v, i) => { if (i < y || i > y + 2) g[i] = k(); }); }
    else if (rule.id === 'col') { const x = pick(r, [0, 1, 2]), c = k(); [0, 3, 6].forEach(d => g[x + d] = c); g.forEach((v, i) => { if (i % 3 !== x) g[i] = k(); }); }
    else if (rule.id === 'mirror') { const a = k(), b = k(), c = k(), d = k(), e = k(); g[0] = a; g[2] = a; g[3] = b; g[5] = b; g[6] = c; g[8] = c; g[1] = d; g[7] = e; g[4] = k(); }
    else if (rule.id === 'ring') { const c = k(); [0, 1, 2, 3, 5, 6, 7, 8].forEach(i => g[i] = c); g[4] = (c + 1 + int(r, 0, 2)) % 4; }
    return g;
  }
  function breakRule(rule, g, r) {
    for (let e = 0; e < 80; e++) {
      const c = g.slice();
      const n = 1 + int(r, 0, 1);
      for (let q = 0; q < n; q++) { const j = int(r, 0, 8); let v = int(r, 0, 3); if (v === c[j]) v = (v + 1) % 4; c[j] = v; }
      if (!rule.ok(c)) return c;
    }
    return null;
  }
  function indItem(seed, i) {
    for (let attempt = 0; attempt < 60; attempt++) {
      const r = rng(seed + attempt * 7919);
      const rule = IRULES[int(r, 0, IRULES.length - 1)];
      const ex = [gridFor(rule, r), gridFor(rule, r)];
      const good = [gridFor(rule, r), gridFor(rule, r)];
      const bad = [];
      while (bad.length < 2) { const b = breakRule(rule, gridFor(rule, r), r); if (b) bad.push(b); }
      const cands = shuffle(r, [{ g: good[0], ok: true }, { g: good[1], ok: true }, { g: bad[0], ok: false }, { g: bad[1], ok: false }]);
      /* unicité : une seule règle du catalogue colle aux 2 exemples ET donne exactement la bonne paire */
      const keys = cands.map(c => c.g.join(''));
      if (new Set(keys).size < 4) continue;
      let fitting = 0, goodPair = null;
      for (const ru of IRULES) {
        if (!ex.every(ru.ok)) continue;
        const valid = cands.map((c, idx) => ru.ok(c.g) ? idx : -1).filter(idx => idx >= 0);
        if (valid.length !== 2) continue;
        fitting++;
        if (ru === rule) goodPair = valid;
        else if (valid.join(',') === cands.map((c, idx) => c.ok ? idx : -1).filter(idx => idx >= 0).join(',')) { /* même paire : acceptable */ }
        else { fitting = 99; break; }
      }
      const intended = cands.map((c, idx) => c.ok ? idx : -1).filter(idx => idx >= 0);
      if (fitting !== 1 || !goodPair || goodPair.join(',') !== intended.join(',')) continue;
      return { id: 'I' + i, kind: 'pick2', examples: ex, candidates: cands.map(c => c.g), good: intended };
    }
    /* filet : règle « coins » simple, vérifiée à nouveau */
    const r = rng(seed);
    const rule = IRULES[0];
    const ex = [gridFor(rule, r), gridFor(rule, r)];
    const good = [gridFor(rule, r), gridFor(rule, r)];
    const bad = [breakRule(rule, gridFor(rule, r), r) || new Array(9).fill(0), breakRule(rule, gridFor(rule, r), r) || new Array(9).fill(1)];
    const cands = shuffle(r, [{ g: good[0], ok: true }, { g: good[1], ok: true }, { g: bad[0], ok: false }, { g: bad[1], ok: false }]);
    return { id: 'I' + i, kind: 'pick2', examples: ex, candidates: cands.map(c => c.g), good: cands.map((c, idx) => c.ok ? idx : -1).filter(idx => idx >= 0) };
  }

  /* ══════════════════ CONCENTRATION — E + points ══════════════════ */
  function concItem(seed, i) {
    const r = rng(seed);
    const shapes = ['E', 'E', 'E', 'mirror', 'F', 'nomiddle'];
    const shape = pick(r, shapes);
    const isE = shape === 'E';
    let dots;
    const want = r() < 0.5;
    dots = (isE && want) ? 3 : pick(r, [0, 1, 2, 4, 4, 3]);
    if (!isE && dots === 3) dots = pick(r, [2, 4]);
    const anchors = [[26, 22], [74, 22], [26, 88], [74, 88], [50, 12], [50, 96]];
    const pos = shuffle(r, anchors.map((_, idx) => idx)).slice(0, dots);
    const correct = isE && dots === 3;
    return { id: 'C' + i, kind: 'edots', shape, dots: pos.map(p => anchors[p]), correct };
  }
  function concSVG(shape, dots) {
    const S = 'stroke="#111" stroke-width="9" stroke-linecap="round"';
    let bars = '';
    const vb = 'M28 18 V92';
    const vbM = 'M72 18 V92';
    const h = y => (shape === 'mirror' ? 'M72 ' + y + ' H34' : 'M28 ' + y + ' H66');
    if (shape === 'mirror') {
      bars = '<path d="' + vbM + '" ' + S + '/><path d="' + h(22) + '" ' + S + '/><path d="' + h(55) + '" ' + S + '/><path d="' + h(88) + '" ' + S + '/>';
    } else if (shape === 'F') {
      bars = '<path d="' + vb + '" ' + S + '/><path d="' + h(22) + '" ' + S + '/><path d="' + h(55) + '" ' + S + '/>';
    } else if (shape === 'nomiddle') {
      bars = '<path d="' + vb + '" ' + S + '/><path d="' + h(22) + '" ' + S + '/><path d="' + h(88) + '" ' + S + '/>';
    } else {
      bars = '<path d="' + vb + '" ' + S + '/><path d="' + h(22) + '" ' + S + '/><path d="' + h(55) + '" ' + S + '/><path d="' + h(88) + '" ' + S + '/>';
    }
    const d = dots.map(p => '<circle cx="' + (p[0] * 1.0 + 10) + '" cy="' + (p[1] * 1.0 + 4) + '" r="7" fill="#111"/>').join('');
    return '<svg viewBox="0 0 120 112" xmlns="http://www.w3.org/2000/svg">' + bars + d + '</svg>';
  }

  /* ══════════════════ SWITCH — codes de permutation ══════════════════ */
  const applyCode = (input, code) => code.map(d => input[d - 1]);
  function swItem(seed, i) {
    const r = rng(seed);
    const level = 1 + Math.floor(i / 10);                    /* 1..3 */
    const input = shuffle(r, [0, 1, 2, 3]);
    let code;
    for (let e = 0; e < 40; e++) {
      code = shuffle(r, [1, 2, 3, 4]);
      const moved = code.filter((d, idx) => d !== idx + 1).length;
      if (moved >= level + 1) break;
    }
    const output = applyCode(input, code);
    const opts = [code];
    let guard = 0;
    while (opts.length < 3 && guard++ < 200) {
      const c = shuffle(r, [1, 2, 3, 4]);
      if (c.join('') === code.join('')) continue;
      if (applyCode(input, c).join('') === output.join('')) continue;
      if (opts.some(o => o.join('') === c.join(''))) continue;
      opts.push(c);
    }
    while (opts.length < 3) opts.push(shuffle(r, [1, 2, 3, 4]));
    const sh = shuffle(r, opts);
    return { id: 'S' + i, kind: 'switchcode', input, output, codes: sh, ans: sh.findIndex(c => c.join('') === code.join('')), level };
  }

  /* ══════════════════ MULTI-TÂCHES — switch de consignes ══════════════════ */
  const MT_LETTERS = [['A', 'consonant'], ['E', 'vowel'], ['I', 'vowel'], ['O', 'vowel'], ['U', 'vowel'], ['R', 'consonant'], ['T', 'consonant'], ['M', 'consonant']];
  function mtItem(seed, i) {
    const r = rng(seed);
    const cue = r() < 0.5 ? 'letter' : 'digit';
    const L = pick(r, MT_LETTERS);
    const d = int(r, 1, 9);
    const ans = cue === 'letter' ? L[1] : (d % 2 ? 'odd' : 'even');
    return { id: 'MT' + i, kind: 'mt', cue, letter: L[0], digit: d, ans };
  }

  /* ══════════════════ LEARNING — ordres de sections ══════════════════ */
  function leOrder(seed, sec) { return shuffle(rng(seed + sec * 104729), Array.from({ length: 12 }, (_, i) => i)); }

  /* ══════════════════ NUMÉRIQUE — 6 feuilles + 37 énoncés ══════════════════ */
  const esc = U.esc;
  function table(t) {
    return '<table class="nvtbl"><thead><tr>' + t.head.map((c, i) => '<th class="' + (i ? 'n' : 'k') + '">' + esc(c) + '</th>').join('') + '</tr></thead><tbody>' +
      t.rows.map(r => '<tr' + (t.strong && t.strong.includes(r[0]) ? ' class="s"' : '') + '><td class="k">' + esc(r[0]) + '</td>' +
        r.slice(1).map(v => '<td class="n">' + esc(String(v)) + '</td>').join('') + '</tr>').join('') + '</tbody></table>' +
      (t.note ? '<div class="nvnote">' + esc(t.note) + '</div>' : '');
  }
  const sv = (w, h, inner) => '<svg class="nvsvg" viewBox="0 0 ' + w + ' ' + h + '" width="100%" preserveAspectRatio="xMidYMid meet" role="img">' + inner + '</svg>';
  const PAL = { 1: '#e08a1e', 2: '#1565c0', 3: '#0d6f78', 4: '#5b3d8f', 5: '#0a8a3c' };
  function pie(segs, note) {
    let a0 = -Math.PI / 2, inner = '';
    segs.forEach((s, i) => {
      const a1 = a0 + s.v / 100 * 2 * Math.PI;
      const x0 = 160 + 95 * Math.cos(a0), y0 = 130 + 95 * Math.sin(a0);
      const x1 = 160 + 95 * Math.cos(a1), y1 = 130 + 95 * Math.sin(a1);
      inner += '<path d="M160 130 L' + x0.toFixed(1) + ' ' + y0.toFixed(1) + ' A95 95 0 ' + (s.v > 50 ? 1 : 0) + ' 1 ' + x1.toFixed(1) + ' ' + y1.toFixed(1) + ' Z" fill="' + PAL[s.c] + '"/>';
      const am = (a0 + a1) / 2;
      inner += '<text x="' + (160 + 62 * Math.cos(am)).toFixed(1) + '" y="' + (130 + 62 * Math.sin(am)).toFixed(1) + '" font-size="12" fill="#fff" text-anchor="middle" font-weight="700">' + s.v + '%</text>';
      a0 = a1;
    });
    inner += segs.map((s, i) => '<rect x="300" y="' + (60 + i * 24) + '" width="13" height="13" fill="' + PAL[s.c] + '"/><text x="320" y="' + (71 + i * 24) + '" font-size="12" fill="#23282c">' + esc(s.n) + '</text>').join('');
    return sv(470, 260, inner) + (note ? '<div class="nvnote">' + esc(note) + '</div>' : '');
  }
  function stacked(series, xl, ylab) {
    const W = 560, H = 300, L = 60, B = 250, top = 30;
    const totals = xl.map((_, i) => series.reduce((a, s) => a + s.v[i], 0));
    const max = Math.ceil(Math.max(...totals) / 2000) * 2000;
    let inner = '<line x1="' + L + '" y1="' + B + '" x2="' + (W - 20) + '" y2="' + B + '" stroke="#cdd4da"/><line x1="' + L + '" y1="' + top + '" x2="' + L + '" y2="' + B + '" stroke="#cdd4da"/>';
    for (let g = 0; g <= 5; g++) { const y = B - (B - top) * g / 5; inner += '<text x="' + (L - 6) + '" y="' + (y + 4) + '" font-size="10" fill="#8a949c" text-anchor="end">' + (max * g / 5 / 1000) + 'k</text><line x1="' + L + '" y1="' + y + '" x2="' + (W - 20) + '" y2="' + y + '" stroke="#eef1f3"/>'; }
    const bw = 62;
    xl.forEach((x, i) => {
      const cx = L + 40 + i * ((W - L - 60) / xl.length);
      let y = B;
      series.forEach(s => {
        const h = (B - top) * s.v[i] / max;
        inner += '<rect x="' + cx + '" y="' + (y - h) + '" width="' + bw + '" height="' + h + '" fill="' + PAL[s.c] + '"/>';
        y -= h;
      });
      inner += '<text x="' + (cx + bw / 2) + '" y="' + (B + 16) + '" font-size="11" fill="#5a656e" text-anchor="middle">' + esc(x) + '</text>';
    });
    inner += series.map((s, i) => '<rect x="' + (L + 10 + i * 130) + '" y="' + (H - 18) + '" width="12" height="12" fill="' + PAL[s.c] + '"/><text x="' + (L + 27 + i * 130) + '" y="' + (H - 8) + '" font-size="11" fill="#23282c">' + esc(s.n) + '</text>').join('');
    inner += '<text x="14" y="' + (top + 4) + '" font-size="10" fill="#8a949c">' + esc(ylab) + '</text>';
    return sv(W, H, inner);
  }
  function lines(series, xl, ylab, ymax) {
    const W = 560, H = 290, L = 52, B = 235, top = 26;
    let inner = '<line x1="' + L + '" y1="' + B + '" x2="' + (W - 20) + '" y2="' + B + '" stroke="#cdd4da"/><line x1="' + L + '" y1="' + top + '" x2="' + L + '" y2="' + B + '" stroke="#cdd4da"/>';
    for (let g = 0; g <= 4; g++) { const y = B - (B - top) * g / 4; inner += '<text x="' + (L - 6) + '" y="' + (y + 4) + '" font-size="10" fill="#8a949c" text-anchor="end">' + (ymax * g / 4).toFixed(0) + '</text><line x1="' + L + '" y1="' + y + '" x2="' + (W - 20) + '" y2="' + y + '" stroke="#eef1f3"/>'; }
    const px = i => L + 40 + i * ((W - L - 80) / (xl.length - 1));
    const py = v => B - (B - top) * v / ymax;
    series.forEach(s => {
      inner += '<polyline points="' + s.v.map((v, i) => px(i) + ',' + py(v)).join(' ') + '" fill="none" stroke="' + PAL[s.c] + '" stroke-width="2.5"/>';
      s.v.forEach((v, i) => { inner += '<circle cx="' + px(i) + '" cy="' + py(v) + '" r="3.5" fill="' + PAL[s.c] + '"/>'; });
    });
    xl.forEach((x, i) => { inner += '<text x="' + px(i) + '" y="' + (B + 16) + '" font-size="11" fill="#5a656e" text-anchor="middle">' + esc(x) + '</text>'; });
    inner += series.map((s, i) => '<rect x="' + (L + 10 + i * 150) + '" y="' + (H - 16) + '" width="12" height="12" fill="' + PAL[s.c] + '"/><text x="' + (L + 27 + i * 150) + '" y="' + (H - 6) + '" font-size="11" fill="#23282c">' + esc(s.n) + '</text>').join('');
    inner += '<text x="14" y="' + (top + 2) + '" font-size="10" fill="#8a949c">' + esc(ylab) + '</text>';
    return sv(W, H, inner);
  }
  function hbars(series, xl, xmax) {
    const W = 560, H = 250, L = 110, B = 200;
    const bh = 26, gap = 14;
    let inner = '<line x1="' + L + '" y1="20" x2="' + L + '" y2="' + B + '" stroke="#cdd4da"/>';
    let y = 30;
    series.forEach(s => {
      inner += '<text x="' + (L - 8) + '" y="' + (y + bh / 2 + 4) + '" font-size="11" fill="#23282c" text-anchor="end">' + esc(s.n) + '</text>';
      s.v.forEach((v, i) => {
        const w = (W - L - 60) * v / xmax;
        inner += '<rect x="' + L + '" y="' + (y + i * (bh / 2 + 2)) + '" width="' + w + '" height="' + (bh / 2 - 2) + '" fill="' + PAL[s.c] + '" opacity="' + (1 - i * 0.28) + '"/>' +
          '<text x="' + (L + w + 5) + '" y="' + (y + i * (bh / 2 + 2) + 9) + '" font-size="10" fill="#5a656e">' + v + '</text>';
      });
      y += bh + gap;
    });
    inner += xl.map((x, i) => '<rect x="' + (L + i * 90) + '" y="' + (H - 16) + '" width="12" height="12" fill="#333" opacity="' + (1 - i * 0.28) + '"/><text x="' + (L + 17 + i * 90) + '" y="' + (H - 6) + '" font-size="11" fill="#23282c">' + esc(x) + '</text>').join('');
    return sv(W, H, inner);
  }

  const NV = {
    totalSec: 12 * 60,
    tabs: [
      { id: 'income', name: 'Income' }, { id: 'costs', name: 'Costs' }, { id: 'shares', name: 'Market shares' },
      { id: 'employees', name: 'Employees' }, { id: 'roe', name: 'Return on equity' }, { id: 'outlook', name: 'Outlook' }
    ],
    figures: {
      income: () => table({
        head: ['Financial year', 'FY 5', 'FY 6', 'FY 7'],
        rows: [
          ['Revenues', '38 210', '41 905', '44 360'],
          ['Total costs', '27 040', '28 590', '30 085'],
          ['Operating income', '11 170', '13 315', '14 275'],
          ['Home Care', '15 240', '16 300', '17 120'],
          ['Personal Care', '14 890', '16 705', '18 040'],
          ['Foods', '8 080', '8 900', '9 200']
        ],
        strong: ['Revenues', 'Operating income'],
        note: 'Revenues by division. All amounts stated in million euros.'
      }),
      costs: () => table({
        head: ['Financial year', 'FY 5', 'FY 6', 'FY 7'],
        rows: [
          ['Personnel costs', '12 480', '13 210', '13 890'],
          ['Material costs', '4 120', '4 380', '4 610'],
          ['Energy costs', '610', '720', '845'],
          ['Depreciation', '2 240', '2 310', '2 395'],
          ['External services', '980', '1 105', '1 180'],
          ['Administration', '860', '905', '940'],
          ['Research & development', '1 420', '1 560', '1 690'],
          ['Marketing & distribution', '3 480', '3 720', '3 980'],
          ['IT expenditure', '310', '420', '465'],
          ['Restructuring', '540', '260', '90'],
          ['Total costs', '27 040', '28 590', '30 085']
        ],
        strong: ['Total costs'],
        note: 'All amounts stated in million euros.'
      }),
      shares: () => pie([
        { n: 'Halden & Roe', v: 44, c: 1 }, { n: 'Corline', v: 39, c: 2 },
        { n: 'Bruma', v: 12, c: 3 }, { n: 'Others', v: 5, c: 4 }
      ], 'Segment revenue in the reporting year: 6.2 billion euros.'),
      employees: () => stacked([
        { n: 'United Kingdom', c: 1, v: [4200, 4350, 4480] },
        { n: 'Continental Europe', c: 2, v: [3100, 3260, 3410] },
        { n: 'North America', c: 3, v: [1800, 1750, 1900] },
        { n: 'Australia', c: 4, v: [700, 720, 760] }
      ], ['FY 5', 'FY 6', 'FY 7'], 'Employees'),
      roe: () => lines([
        { n: 'Halden & Roe group', c: 1, v: [12.4, 14.1, 13.2, 15.6] },
        { n: 'Peer average', c: 2, v: [10.8, 11.2, 11.9, 12.4] },
        { n: 'Corline division', c: 3, v: [8.9, 9.4, 10.8, 11.7] }
      ], ['FY 4', 'FY 5', 'FY 6', 'FY 7'], 'Return (%)', 18),
      outlook: () => hbars([
        { n: 'Home Care', c: 1, v: [18, 19] }, { n: 'Personal Care', c: 2, v: [21, 23] }, { n: 'Foods', c: 3, v: [12, 12] }
      ], ['FY 8', 'FY 9'], 26)
    },
    items: [
      { tab: 'income', q: 'Revenues increased in every year shown.', a: 0, why: '38 210 → 41 905 → 44 360.' },
      { tab: 'income', q: 'Operating income in FY 7 was lower than in FY 6.', a: 1, why: '14 275 > 13 315.' },
      { tab: 'income', q: 'Personal Care revenues grew by more than Home Care revenues between FY 5 and FY 7.', a: 0, why: '+3 150 versus +1 880 million euros.' },
      { tab: 'income', q: 'Foods revenues fell in FY 6.', a: 1, why: '8 080 → 8 900: they rose.' },
      { tab: 'income', q: 'Revenues in FY 7 were more than 15% higher than in FY 5.', a: 0, why: '44 360 / 38 210 = +16.1%.' },
      { tab: 'income', q: 'The group expects revenues above 46 000 million euros in FY 8.', a: 2, why: 'The income sheet gives no FY 8 figure.' },
      { tab: 'costs', q: 'Personnel costs were the largest single cost item in every year.', a: 0, why: '12 480 / 13 210 / 13 890: far above any other line.' },
      { tab: 'costs', q: 'Energy costs more than doubled between FY 5 and FY 7.', a: 1, why: '610 → 845 = ×1.39, not ×2.' },
      { tab: 'costs', q: 'Restructuring costs fell in every year shown.', a: 0, why: '540 → 260 → 90.' },
      { tab: 'costs', q: 'Marketing & distribution costs exceeded research & development costs in every year.', a: 0, why: '3 480 > 1 420; 3 720 > 1 560; 3 980 > 1 690.' },
      { tab: 'costs', q: 'Total costs in FY 7 amounted to 30 085 million euros.', a: 0, why: 'Stated in the table.' },
      { tab: 'costs', q: 'External service costs are stated per subsidiary.', a: 2, why: 'The table states group totals only.' },
      { tab: 'shares', q: 'Halden & Roe holds the largest share of the segment.', a: 0, why: '44%, ahead of Corline (39%).' },
      { tab: 'shares', q: 'Corline and Bruma together hold more than half of the segment.', a: 0, why: '39% + 12% = 51%.' },
      { tab: 'shares', q: 'The four players shown share the segment equally.', a: 1, why: '44 / 39 / 12 / 5%.' },
      { tab: 'shares', q: 'Others account for 5% of the segment.', a: 0, why: 'Pie chart: 5%.' },
      { tab: 'shares', q: 'Segment revenue is stated in million euros.', a: 1, why: 'The note states 6.2 billion euros.' },
      { tab: 'shares', q: 'Corline’s share increased over the previous year.', a: 2, why: 'The pie chart is a single point in time.' },
      { tab: 'employees', q: 'Total headcount increased in every year shown.', a: 0, why: '9 800 → 10 080 → 10 550.' },
      { tab: 'employees', q: 'Headcount in North America fell between FY 5 and FY 6.', a: 0, why: '1 800 → 1 750.' },
      { tab: 'employees', q: 'In FY 7 the United Kingdom employed more people than all other regions together.', a: 1, why: '4 480 versus 6 070 elsewhere.' },
      { tab: 'employees', q: 'Australia had the smallest headcount in every year shown.', a: 0, why: '700 / 720 / 760: smallest each year.' },
      { tab: 'employees', q: 'In FY 7 the average headcount per production plant exceeded 1 000.', a: 0, why: '10 550 employees / 9 plants ≈ 1 172.' },
      { tab: 'employees', q: 'The group plans to hire in Australia during FY 8.', a: 2, why: 'No FY 8 headcount plan is given.' },
      { tab: 'roe', q: 'Group return on equity exceeded the peer average in every year shown.', a: 0, why: '12.4>10.8; 14.1>11.2; 13.2>11.9; 15.6>12.4.' },
      { tab: 'roe', q: 'Group return on equity rose in every year shown.', a: 1, why: 'It dipped from 14.1 (FY 5) to 13.2 (FY 6).' },
      { tab: 'roe', q: 'The Corline division’s return on equity stayed below 10% in FY 4 and FY 5.', a: 0, why: '8.9 and 9.4.' },
      { tab: 'roe', q: 'Group return on equity reached 15.6% in FY 7.', a: 0, why: 'Stated on the chart.' },
      { tab: 'roe', q: 'The peer average includes Halden & Roe.', a: 2, why: 'The chart does not say how the peer average is computed.' },
      { tab: 'outlook', q: 'The forecast personal care share rises from FY 8 to FY 9.', a: 0, why: '21 → 23.' },
      { tab: 'outlook', q: 'The forecast foods share is unchanged between FY 8 and FY 9.', a: 0, why: '12 and 12.' },
      { tab: 'outlook', q: 'Home Care will overtake Personal Care by FY 9.', a: 1, why: '19 versus 23: it will not.' },
      { tab: 'outlook', q: 'The outlook chart covers three financial years.', a: 1, why: 'FY 8 and FY 9 only.' },
      { tab: 'costs', q: 'Total costs grew more slowly than revenues between FY 5 and FY 7.', a: 0, why: 'Costs +11.3% versus revenues +16.1%.' },
      { tab: 'income', q: 'The operating margin (operating income / revenues) improved between FY 5 and FY 7.', a: 0, why: '29.2% → 32.2%.' },
      { tab: 'employees', q: 'In FY 7 the group employed more people in North America than in Australia.', a: 0, why: '1 900 versus 760.' },
      { tab: 'shares', q: 'The Halden & Roe share equals the combined shares of Corline and Bruma.', a: 1, why: '44% versus 51%.' }
    ].map((x, i) => Object.assign({ id: 'NV' + (i + 1), kind: 'numverb' }, x))
  };

  return { dedItem, indItem, concItem, concSVG, swItem, applyCode, mtItem, leOrder, NV, table, pie, stacked, lines, hbars };
})();

if (typeof window !== 'undefined') window.DRILL = DRILL; else globalThis.DRILL = DRILL;
