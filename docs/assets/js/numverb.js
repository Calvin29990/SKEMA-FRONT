/* ═══════════════════════════════════════════════════════════════
   numverb.js — Numerical Reasoning au format cut-e / Maki :
   6 sous-onglets de figures, 37 énoncés true / false / cannot say,
   12 minutes, bascule automatique vers l'onglet de la question.
   Les figures sont paramétriques (SVG généré) : jamais déformées.
   ═══════════════════════════════════════════════════════════════ */
'use strict';

const NUMVERB = (() => {
  const PAL = { 1: '#e08a1e', 2: '#1565c0', 3: '#0d6f78', 4: '#5b3d8f', 5: '#0a8a3c' };
  const INK = '#5a656e', LINE = '#cdd4da', GRID = '#e2e6ea';
  const esc = (s) => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

  /* ── brique SVG ── */
  const svg = (w, h, inner) => '<svg class="nvsvg" viewBox="0 0 ' + w + ' ' + h + '" width="100%" ' +
    'preserveAspectRatio="xMidYMid meet" role="img">' + inner + '</svg>';
  const txt = (x, y, s, o) => {
    o = o || {};
    return '<text x="' + x + '" y="' + y + '" font-size="' + (o.size || 11) + '" fill="' + (o.fill || INK) + '" ' +
      'text-anchor="' + (o.anchor || 'middle') + '"' + (o.bold ? ' font-weight="700"' : '') +
      (o.mono ? ' font-family="monospace"' : '') + '>' + esc(s) + '</text>';
  };
  /* légende : fragment SVG à insérer DANS un <svg> (sinon les <rect>/<text> ne sont pas rendus) */
  const legend = (items, y) => items.map((it, i) => {
    const x = 40 + (i % 3) * 200, yy = y + Math.floor(i / 3) * 22;
    return '<rect x="' + x + '" y="' + (yy - 10) + '" width="13" height="13" rx="2" fill="' + PAL[it.color] + '"/>' +
      txt(x + 6.5, yy, it.n, { size: 9, fill: '#fff', bold: true }) +
      txt(x + 20, yy, it.name, { size: 11, anchor: 'start', fill: '#23282c' });
  }).join('');
  const legendBox = (items, y, cols) => {
    cols = cols || 3;
    const rows = Math.ceil(items.length / cols), h = y + Math.ceil(items.length / cols) * 22;
    return '<svg class="nvlegsvg" width="620" height="' + h + '" viewBox="0 0 620 ' + h + '">' + legend(items, y) + '</svg>';
  };

  /* ── 1. tableau ── */
  function table(t) {
    const body = t.rows.map(r => '<tr' + (t.strong && t.strong.indexOf(r[0]) > -1 ? ' class="s"' : '') + '>' +
      '<td class="k">' + esc(r[0]) + '</td>' +
      r.slice(1).map(v => '<td class="n">' + esc(String(v).replace('-', ' -')) + '</td>').join('') + '</tr>').join('');
    return '<table class="nvtbl"><thead><tr>' + t.head.map((c, i) => '<th class="' + (i ? 'n' : 'k') + '">' + esc(c) + '</th>').join('') +
      '</tr></thead><tbody>' + body + '</tbody></table>' + (t.note ? '<div class="nvnote">' + esc(t.note) + '</div>' : '');
  }

  /* ── 2. camembert ── */
  function pie(d) {
    const cx = 190, cy = 150, r = 108;
    let a0 = -Math.PI / 2, inner = '';
    const S = d.slices;
    /* ordre visuel du test réel pour 4 parts ; tout autre nombre est rendu tel quel */
    const order = (S.length === 4) ? [S[1], S[3], S[0], S[2]] : S.slice();
    order.forEach(s => {
      const a1 = a0 + (s.pct / 100) * 2 * Math.PI;
      const x0 = cx + r * Math.cos(a0), y0 = cy + r * Math.sin(a0);
      const x1 = cx + r * Math.cos(a1), y1 = cy + r * Math.sin(a1);
      const large = (a1 - a0) > Math.PI ? 1 : 0;
      inner += '<path d="M' + cx + ' ' + cy + ' L' + x0.toFixed(1) + ' ' + y0.toFixed(1) +
        ' A' + r + ' ' + r + ' 0 ' + large + ' 1 ' + x1.toFixed(1) + ' ' + y1.toFixed(1) + ' Z" fill="' + PAL[s.color] +
        '" stroke="#fff" stroke-width="1.5"/>';
      const am = (a0 + a1) / 2, lx = cx + (r * 1.22) * Math.cos(am), ly = cy + (r * 1.22) * Math.sin(am);
      inner += txt(lx, ly + 4, s.pct + '%', { size: 12, bold: true, fill: '#23282c' });
      const bx = cx + (r * 0.62) * Math.cos(am), by = cy + (r * 0.62) * Math.sin(am);
      inner += '<rect x="' + (bx - 7) + '" y="' + (by - 7) + '" width="14" height="14" rx="2" fill="rgba(0,0,0,.25)"/>' +
        txt(bx, by + 4, s.color, { size: 10, fill: '#fff', bold: true });
      a0 = a1;
    });
    return svg(620, 300, inner) +
      '<div class="nvcap">' + esc(d.title) + '</div>' +
      '<div class="nvlegend">' + legendBox(d.slices.map(s => ({ color: s.color, n: s.color, name: s.label })), 16) + '</div>' +
      '<div class="nvnote">' + esc(d.total) + '</div>';
  }

  /* ── 3. colonnes empilées ── */
  function stacked(d) {
    const W = 640, H = 300, x0 = 70, x1 = 600, y0 = 34, y1 = 240, max = d.ymax;
    let g = '';
    for (let v = 0; v <= max; v += 10) {
      const y = y1 - (v / max) * (y1 - y0);
      g += '<line x1="' + x0 + '" x2="' + x1 + '" y1="' + y + '" y2="' + y + '" stroke="' + GRID + '"/>' +
        txt(x0 - 8, y + 4, v, { size: 10, anchor: 'end' });
    }
    const n = d.xlabels.length, gw = (x1 - x0) / n, bw = 46;
    d.xlabels.forEach((lab, i) => {
      const cx = x0 + gw * (i + 0.5);
      let acc = 0;
      d.series.forEach(s => {
        const v = s.values[i], h = (v / max) * (y1 - y0);
        const y = y1 - acc - h;
        g += '<rect x="' + (cx - bw / 2) + '" y="' + y.toFixed(1) + '" width="' + bw + '" height="' + h.toFixed(1) +
          '" fill="' + PAL[s.color] + '" stroke="#fff" stroke-width="1"/>' +
          txt(cx, y + h / 2 + 3.5, v, { size: 9.5, fill: '#fff', bold: true });
        acc += h;
      });
      g += txt(cx, y1 + 16, lab, { size: 11, fill: '#23282c' });
    });
    g += '<line x1="' + x0 + '" x2="' + x1 + '" y1="' + y1 + '" y2="' + y1 + '" stroke="' + LINE + '"/>';
    g += txt((x0 + x1) / 2, y1 + 36, d.xaxis, { size: 11, fill: '#23282c' });
    g += txt(16, (y0 + y1) / 2, d.yaxis.replace('\n', ' '), { size: 11, fill: '#23282c', anchor: 'middle' });
    return svg(W, H + 46, g) +
      '<div class="nvlegend">' + legendBox(d.series.map(s => ({ color: s.color, n: s.color, name: s.name })), 16) + '</div>';
  }

  /* ── 4. courbes ── */
  function lines(d) {
    const W = 640, H = 300, x0 = 70, x1 = 600, y0 = 34, y1 = 240, max = d.ymax;
    let g = '';
    for (let v = 0; v <= max + 1e-9; v += 0.5) {
      const y = y1 - (v / max) * (y1 - y0);
      g += '<line x1="' + x0 + '" x2="' + x1 + '" y1="' + y + '" y2="' + y + '" stroke="' + GRID + '"/>' +
        txt(x0 - 8, y + 4, v.toFixed(1), { size: 10, anchor: 'end' });
    }
    const n = d.xlabels.length, gw = (x1 - x0) / n;
    d.series.forEach(s => {
      const pts = s.values.map((v, i) => [x0 + gw * (i + 0.5), y1 - (v / max) * (y1 - y0)]);
      g += '<polyline points="' + pts.map(p => p[0].toFixed(1) + ',' + p[1].toFixed(1)).join(' ') +
        '" fill="none" stroke="' + PAL[s.color] + '" stroke-width="2"/>';
      pts.forEach((p, i) => {
        g += '<circle cx="' + p[0].toFixed(1) + '" cy="' + p[1].toFixed(1) + '" r="4" fill="' + PAL[s.color] + '"/>' +
          txt(p[0], p[1] - 9, s.values[i].toFixed(2).replace(/0$/, '').replace(/\.$/, ''), { size: 10, fill: '#23282c' });
      });
    });
    d.xlabels.forEach((lab, i) => { g += txt(x0 + gw * (i + 0.5), y1 + 16, lab, { size: 11, fill: '#23282c' }); });
    g += '<line x1="' + x0 + '" x2="' + x1 + '" y1="' + y1 + '" y2="' + y1 + '" stroke="' + LINE + '"/>';
    g += txt((x0 + x1) / 2, y1 + 36, d.xaxis, { size: 11, fill: '#23282c' });
    g += txt(16, (y0 + y1) / 2, d.yaxis, { size: 11, fill: '#23282c' });
    return svg(W, H + 46, g) +
      '<div class="nvlegend">' + legendBox(d.series.map(s => ({ color: s.color, n: s.color, name: s.name })), 16) + '</div>';
  }

  /* ── 5. barres horizontales ── */
  function hbars(d) {
    const W = 640, H = 300, x0 = 92, x1 = 600, y0 = 26, y1 = 236, max = d.xmax;
    let g = '';
    for (let v = 0; v <= max; v += 5) {
      const x = x0 + (v / max) * (x1 - x0);
      g += '<line x1="' + x + '" x2="' + x + '" y1="' + y0 + '" y2="' + y1 + '" stroke="' + GRID + '"/>' +
        txt(x, y1 + 18, v, { size: 10 });
    }
    const n = d.xlabels.length, gh = (y1 - y0) / n;
    d.xlabels.forEach((lab, i) => {
      const cy = y0 + gh * (i + 0.5);
      g += txt(x0 - 12, cy + 10, lab, { size: 11, anchor: 'end', fill: '#23282c' });
      d.series.forEach((s, k) => {
        const v = s.values[i], h = 15, y = cy - (d.series.length * (h + 4)) / 2 + k * (h + 4);
        const w = (v / max) * (x1 - x0);
        g += '<rect x="' + x0 + '" y="' + y.toFixed(1) + '" width="' + w.toFixed(1) + '" height="' + h +
          '" fill="' + PAL[s.color] + '" stroke="#fff"/>' +
          txt(x0 + w + 8, y + 12, v, { size: 10, anchor: 'start', fill: '#23282c', bold: true }) +
          '<rect x="' + (x0 + w / 2 - 7) + '" y="' + (y + h / 2 - 7) + '" width="14" height="14" rx="2" fill="rgba(0,0,0,.18)"/>' +
          txt(x0 + w / 2, y + h / 2 + 4, s.color, { size: 10, fill: '#fff', bold: true });
      });
    });
    g += txt((x0 + x1) / 2, y1 + 38, d.xaxis, { size: 11, fill: '#23282c' });
    return svg(W, H + 46, g) +
      '<div class="nvlegend">' + legendBox(d.series.map(s => ({ color: s.color, n: s.color, name: s.name })), 16) + '</div>';
  }

  const FIG = {
    income: () => table({ head: ["", "Year 7", "Year 6", "Year 5"], rows: [["Revenues", 41260, 37480, 34910], ["Costs", 33008, 30732, 29118], ["Gross profit", 8252, 6748, 5792], ["Other costs", 2314, 1906, 1388], ["Operating income", 5938, 4842, 4404], ["Skin care products", 4148, 3762, 3508], ["Personal care products", 4902, 4128, 3946], ["Fragrances", 1206, 918, 806], ["Revenues from selected product lines", 10256, 8808, 8260], ["Profit/loss share from corporate investments", 486, 214, -298], ["Total revenues", 22402, 19978, 18138]], note: "All amounts stated in million euros", strong: ["Revenues", "Gross profit", "Operating income", "Total revenues"] }),
    costs: () => table({ head: ["", "Year 7", "Year 6", "Year 5"], rows: [["Personnel costs", 12486, 11902, 11340], ["Material costs", 1208, 1142, 1004], ["Energy costs", 384, 312, 268], ["Depreciation of production facilities", 2214, 2086, 1998], ["Costs of external services", 742, 806, 918], ["General administrative costs", 688, 702, 664], ["Research and development costs", 1246, 1388, 1502], ["Marketing and distribution costs", 3104, 2988, 2862], ["EDP expenditures", 96, 78, 64], ["Restructuring costs", 214, 128, 96], ["Total costs", 22382, 21532, 20716]], note: "All amounts stated in million euros", strong: ["Total costs"] }),
    shares: () => pie({"title": "Segment 'Skincare and personal care for women'", "slices": [{"label": "Solvan Group", "pct": 46, "color": 1}, {"label": "Alba Inc.", "pct": 41, "color": 3}, {"label": "Corvus Ltd", "pct": 8, "color": 2}, {"label": "Deltara SA", "pct": 5, "color": 4}], "total": "Total segment revenue: 8.4 billion euros"}),
    employees: () => stacked({"title": null, "series": [{"name": "Germany", "color": 1, "values": [34, 27, 19, 17, 15]}, {"name": "Europe (excluding Germany)", "color": 2, "values": [12, 14, 22, 25, 26]}, {"name": "America", "color": 3, "values": [15, 18, 20, 24, 23]}, {"name": "Asia/Pacific", "color": 4, "values": [6, 7, 8, 10, 11]}, {"name": "Others", "color": 5, "values": [2, 3, 4, 6, 5]}], "xlabels": ["3", "4", "5", "6", "7"], "xaxis": "Financial year", "yaxis": "Number of employees\nin thousand", "ymax": 90}),
    roe: () => lines({"series": [{"name": "Solvan Group", "color": 2, "values": [1.6, 0.92, 1.4, 2.2, 1.6]}, {"name": "Alba Inc.", "color": 1, "values": [0.54, 1.2, 1.72, 1.3, 1.3]}, {"name": "Corvus Ltd", "color": 3, "values": [0.5, 2.76, 2.0, 0.27, 0.64]}], "xlabels": ["3", "4", "5", "6", "7"], "xaxis": "Financial year", "yaxis": "Return percentage", "ymax": 3.0}),
    outlook: () => hbars({"title": "Estimated future market shares of the cosmetics line", "series": [{"name": "'Young Beauty'", "color": 1, "values": [19, 21, 21.5]}, {"name": "'Man'", "color": 2, "values": [21, 20, 23.5]}], "xlabels": ["FY", "FY+1", "FY+2"], "xaxis": "Percentage of market share", "xmax": 25})
  };

  /* ── jeu de données courant ────────────────────────────────────────
     Le contenu intégré sert de démonstration. Un fichier local choisi par
     l'utilisateur (chargeur « perso ») le remplace à chaud : rien n'est
     envoyé ni enregistré ailleurs que dans le navigateur.              */
  const BUILTIN = {
    title: 'Numerical Reasoning',
    totalSec: 12 * 60,
    prompt: 'Looking at the figures, is each statement true, false, or cannot say?',
    tabs: [{"id": "income", "fr": "Revenus", "short": "Income"}, {"id": "costs", "fr": "Coûts", "short": "Costs"}, {"id": "shares", "fr": "Parts de marché", "short": "Market shares"}, {"id": "employees", "fr": "Effectifs", "short": "Employees"}, {"id": "roe", "fr": "Rentabilité des fonds propres", "short": "Return on equity"}, {"id": "outlook", "fr": "Perspectives", "short": "Outlook"}],
    items: [{"id": "NV01", "tab": "income", "kind": "numverb", "q": "The revenues in Year 7 were more than 40 000 million euros.", "ans": 0, "why": "Revenues Year 7 = 41 260 million euros, above 40 000."}, {"id": "NV02", "tab": "income", "kind": "numverb", "q": "The gross profit in Year 5 was higher than the gross profit in Year 6.", "ans": 1, "why": "Gross profit: 5 792 (Year 5) < 6 748 (Year 6)."}, {"id": "NV03", "tab": "income", "kind": "numverb", "q": "The operating income increased from Year 6 to Year 7.", "ans": 0, "why": "Operating income: 4 842 (Year 6) → 5 938 (Year 7)."}, {"id": "NV04", "tab": "income", "kind": "numverb", "q": "The costs in Year 5 exceeded 30 000 million euros.", "ans": 1, "why": "Costs Year 5 = 29 118 million euros, below 30 000."}, {"id": "NV05", "tab": "income", "kind": "numverb", "q": "The total revenues in Year 7 were more than 10% higher than in Year 6.", "ans": 0, "why": "22 402 / 19 978 = +12.1% (above 10%)."}, {"id": "NV06", "tab": "income", "kind": "numverb", "q": "The operating income is expected to decrease in Year 8.", "ans": 2, "why": "The table gives no forecast for Year 8."}, {"id": "NV07", "tab": "costs", "kind": "numverb", "q": "Personnel costs were the largest single cost item in Year 7.", "ans": 0, "why": "12 486 — far above material costs (1 208), marketing (3 104) or depreciation (2 214)."}, {"id": "NV08", "tab": "costs", "kind": "numverb", "q": "Research and development costs fell between Year 5 and Year 7.", "ans": 0, "why": "R&D: 1 502 (Year 5) → 1 388 → 1 246 (Year 7)."}, {"id": "NV09", "tab": "costs", "kind": "numverb", "q": "Energy costs more than trebled between Year 5 and Year 7.", "ans": 1, "why": "Energy costs: 268 → 384, i.e. ×1.43, not ×3."}, {"id": "NV10", "tab": "costs", "kind": "numverb", "q": "Depreciation of production facilities was higher in Year 6 than in Year 7.", "ans": 1, "why": "Depreciation: 2 086 (Year 6) < 2 214 (Year 7)."}, {"id": "NV11", "tab": "costs", "kind": "numverb", "q": "Total costs decreased between Year 5 and Year 7.", "ans": 1, "why": "Total costs rose: 20 716 (Year 5) → 22 382 (Year 7)."}, {"id": "NV12", "tab": "costs", "kind": "numverb", "q": "Energy costs are stated per unit produced.", "ans": 2, "why": "The table states amounts in million euros, not per unit produced."}, {"id": "NV13", "tab": "shares", "kind": "numverb", "q": "Solvan Group holds the largest share of this segment.", "ans": 0, "why": "Solvan Group 46%, ahead of Alba Inc. 41%."}, {"id": "NV14", "tab": "shares", "kind": "numverb", "q": "Alba Inc. and Corvus Ltd together account for more than half of the segment.", "ans": 1, "why": "41% + 8% = 49%, below half."}, {"id": "NV15", "tab": "shares", "kind": "numverb", "q": "The four companies share the segment equally.", "ans": 1, "why": "The shares are 46%, 41%, 8% and 5%."}, {"id": "NV16", "tab": "shares", "kind": "numverb", "q": "Deltara SA accounts for 5% of the segment.", "ans": 0, "why": "Pie chart: 5%."}, {"id": "NV17", "tab": "shares", "kind": "numverb", "q": "The segment revenue is stated in million euros.", "ans": 1, "why": "The chart states 8.4 billion euros (not millions)."}, {"id": "NV18", "tab": "shares", "kind": "numverb", "q": "The number of employees of Corvus Ltd increased in Year 7.", "ans": 2, "why": "The chart only gives market shares, not headcounts."}, {"id": "NV19", "tab": "employees", "kind": "numverb", "q": "The number of employees in Germany fell every year from FY 3 to FY 7.", "ans": 0, "why": "34 → 27 → 19 → 17 → 15 (thousand)."}, {"id": "NV20", "tab": "employees", "kind": "numverb", "q": "In FY 7, Europe (excluding Germany) had more employees than America.", "ans": 0, "why": "26 against 23 (thousand)."}, {"id": "NV21", "tab": "employees", "kind": "numverb", "q": "The total number of employees was higher in FY 5 than in FY 7.", "ans": 1, "why": "FY 5: 19+22+20+8+4 = 73; FY 7: 15+26+23+11+5 = 80."}, {"id": "NV22", "tab": "employees", "kind": "numverb", "q": "Asia/Pacific had the smallest number of employees in every year shown.", "ans": 1, "why": "Others is smaller every year (2, 3, 4, 6, 5 against 6, 7, 8, 10, 11)."}, {"id": "NV23", "tab": "employees", "kind": "numverb", "q": "The number of employees in Asia/Pacific more than doubled between FY 3 and FY 7.", "ans": 1, "why": "6 → 11 thousand, i.e. ×1.8, less than double."}, {"id": "NV24", "tab": "employees", "kind": "numverb", "q": "The employee figures are given in thousands.", "ans": 0, "why": "The axis is labelled \"Number of employees in thousand\"."}, {"id": "NV25", "tab": "employees", "kind": "numverb", "q": "In FY 7, more employees worked outside Germany than in Germany.", "ans": 0, "why": "Outside Germany: 26+23+11+5 = 65 thousand against 15 thousand in Germany."}, {"id": "NV26", "tab": "roe", "kind": "numverb", "q": "Solvan Group's return on equity decreased from FY 6 to FY 7.", "ans": 0, "why": "2.2% (FY 6) → 1.6% (FY 7)."}, {"id": "NV27", "tab": "roe", "kind": "numverb", "q": "Corvus Ltd's return on equity was higher than Solvan Group's in FY 4.", "ans": 0, "why": "FY 4: Corvus 2.76% against Solvan 0.92%."}, {"id": "NV28", "tab": "roe", "kind": "numverb", "q": "Alba Inc.'s return on equity was the lowest of the three companies in FY 7.", "ans": 1, "why": "FY 7: Alba 1.3%, Solvan 1.6%, Corvus 0.64% — Corvus is the lowest."}, {"id": "NV29", "tab": "roe", "kind": "numverb", "q": "Corvus Ltd's return on equity was below 1% in both FY 6 and FY 7.", "ans": 0, "why": "FY 6: 0.27%; FY 7: 0.64%."}, {"id": "NV30", "tab": "roe", "kind": "numverb", "q": "Return on equity is stated as a percentage.", "ans": 0, "why": "The vertical axis is \"Return percentage\"."}, {"id": "NV31", "tab": "roe", "kind": "numverb", "q": "Alba Inc. had the highest return on equity of the three companies in FY 5.", "ans": 1, "why": "FY 5: Corvus 2.0% against Alba 1.72% and Solvan 1.4%."}, {"id": "NV32", "tab": "roe", "kind": "numverb", "q": "Corvus Ltd's return on equity will stay below 1% in FY 8.", "ans": 2, "why": "No data for FY 8 on the chart."}, {"id": "NV33", "tab": "outlook", "kind": "numverb", "q": "The forecast market share of 'Man' rises in every period shown.", "ans": 1, "why": "It falls from FY (21%) to FY+1 (20%) before rising to 23.5% in FY+2."}, {"id": "NV34", "tab": "outlook", "kind": "numverb", "q": "In FY+2, the forecast market share of 'Man' exceeds that of 'Young Beauty'.", "ans": 0, "why": "FY+2: 23.5% against 21.5%."}, {"id": "NV35", "tab": "outlook", "kind": "numverb", "q": "The forecast market share of 'Young Beauty' in FY+2 is above 20%.", "ans": 0, "why": "FY+2: 21.5%."}, {"id": "NV36", "tab": "outlook", "kind": "numverb", "q": "The forecast market share of 'Man' in FY+1 is lower than in FY.", "ans": 0, "why": "FY: 21%; FY+1: 20%."}, {"id": "NV37", "tab": "outlook", "kind": "numverb", "q": "The figures in this chart are stated in million euros.", "ans": 1, "why": "The horizontal axis is \"Percentage of market share\"."}],
    figures: FIG
  };
  let D = BUILTIN, SOURCE = 'builtin', LABEL = '';

  const FIGTYPES = ['table', 'pie', 'stacked', 'lines', 'hbars'];
  const renderFig = (spec) => {
    if (typeof spec === 'function') return spec();
    if (!spec || FIGTYPES.indexOf(spec.type) < 0) return '';
    return ({ table: table, pie: pie, stacked: stacked, lines: lines, hbars: hbars })[spec.type](spec);
  };

  /* validation stricte : un fichier incomplet est refusé avec la liste des erreurs */
  function validate(data) {
    const errs = [];
    const push = (n, s) => { errs.push(n + ' — ' + s); };
    if (!data || typeof data !== 'object' || Array.isArray(data)) return { ok: false, errors: ['Fichier illisible : un objet JSON est attendu.'] };
    const tabs = data.tabs;
    if (!Array.isArray(tabs) || !tabs.length) push('tabs', 'au moins un onglet est requis.');
    else tabs.forEach((t, i) => {
      if (!t || typeof t.id !== 'string' || !t.id.trim()) push('tabs[' + i + '].id', 'identifiant manquant.');
      if (!t || typeof t.short !== 'string' || !t.short.trim()) push('tabs[' + i + '].short', 'libellé d’onglet manquant.');
    });
    const ids = (Array.isArray(tabs) ? tabs : []).map(t => (t && typeof t.id === 'string') ? t.id.trim() : null);
    const figs = data.figures;
    if (!figs || typeof figs !== 'object' || Array.isArray(figs)) push('figures', 'objet attendu, avec une figure par onglet.');
    else ids.forEach(id => {
      if (!id) return;
      const f = figs[id];
      if (!f) { push('figures.' + id, 'figure manquante pour cet onglet.'); return; }
      if (FIGTYPES.indexOf(f.type) < 0) { push('figures.' + id + '.type', 'doit être : ' + FIGTYPES.join(' | ') + '.'); return; }
      if (f.type === 'table' && !(Array.isArray(f.rows) && f.rows.length)) push('figures.' + id + '.rows', 'tableau sans lignes.');
      if (f.type === 'pie' && !(Array.isArray(f.slices) && f.slices.length)) push('figures.' + id + '.slices', 'camembert sans parts.');
      if (f.type !== 'table' && f.type !== 'pie' && !(Array.isArray(f.series) && f.series.length)) push('figures.' + id + '.series', 'séries manquantes.');
    });
    const items = data.items;
    if (!Array.isArray(items) || !items.length) push('items', 'au moins un énoncé est requis.');
    else items.forEach((it, i) => {
      const n = 'items[' + i + ']';
      if (!it || typeof it !== 'object') { push(n, 'objet attendu.'); return; }
      if (typeof it.q !== 'string' || !it.q.trim()) push(n + '.q', 'texte de l’énoncé manquant.');
      if (ids.indexOf(it.tab) < 0) push(n + '.tab', 'doit être un des onglets : ' + ids.join(', ') + '.');
      if ([0, 1, 2].indexOf(it.ans) < 0) push(n + '.ans', 'doit valoir 0 (true), 1 (false) ou 2 (cannot say).');
    });
    const dur = data.totalSec == null ? 12 * 60 : Number(data.totalSec);
    if (!isFinite(dur) || dur < 30) push('totalSec', 'durée invalide (au moins 30 secondes).');
    if (errs.length) return { ok: false, errors: errs.slice(0, 14), more: Math.max(0, errs.length - 14), count: errs.length };
    return { ok: true, errors: [], data: {
      title: typeof data.title === 'string' && data.title.trim() ? data.title.trim() : 'Numerical Reasoning',
      totalSec: Math.round(dur),
      prompt: typeof data.prompt === 'string' && data.prompt.trim() ? data.prompt.trim() : BUILTIN.prompt,
      tabs: tabs.map(t => ({ id: String(t.id).trim(), short: String(t.short).trim(), fr: String(t.fr || t.short).trim() })),
      items: items.map((it, i) => ({
        id: typeof it.id === 'string' && it.id.trim() ? it.id.trim() : 'P' + String(i + 1).padStart(2, '0'),
        tab: it.tab, kind: 'numverb', q: String(it.q).trim(), ans: it.ans | 0,
        why: typeof it.why === 'string' ? it.why.trim() : ''
      })),
      figures: figs
    } };
  }

  /* gabarit vierge à remplir : évite de deviner la structure du fichier */
  function template() {
    const t = BUILTIN.tabs.map(x => ({ id: x.id, short: x.short, fr: x.fr }));
    const fig = {};
    t.forEach(x => { fig[x.id] = { type: 'table', head: ['', 'Year 7'], rows: [['Exemple', 0]], note: '' }; });
    return {
      title: 'Numerical Reasoning — mon fichier',
      totalSec: 720,
      prompt: BUILTIN.prompt,
      tabs: t,
      figures: fig,
      items: [
        { id: 'P01', tab: t[0].id, q: 'Exemple d’énoncé à remplacer.', ans: 0, why: 'Justification courte (facultative).' },
        { id: 'P02', tab: t[1].id, q: 'Deuxième exemple.', ans: 2, why: '' }
      ]
    };
  }

  const api = {
    PAL: PAL,
    FIGTYPES: FIGTYPES,
    get TABS() { return D.tabs; },
    get ITEMS() { return D.items; },
    get totalSec() { return D.totalSec; },
    get prompt() { return D.prompt; },
    get title() { return D.title; },
    get source() { return SOURCE; },
    get label() { return LABEL; },
    isPerso: () => SOURCE === 'perso',
    figure: (id) => renderFig(D.figures[id]),
    tabOf: (id) => D.tabs.filter(t => t.id === id)[0] || D.tabs[0],
    validate: validate,
    template: template,
    load(data, label) {
      const v = validate(data);
      if (!v.ok) return v;
      D = v.data; SOURCE = 'perso'; LABEL = label || '';
      return { ok: true, errors: [], count: D.items.length, tabs: D.tabs.length, totalSec: D.totalSec, title: D.title };
    },
    reset() { D = BUILTIN; SOURCE = 'builtin'; LABEL = ''; return { ok: true, count: D.items.length, tabs: D.tabs.length }; }
  };
  return api;
})();
