/* UBS practice modules — original questions and fictional data inspired by the
   three assessment formats described in the user-provided reference documents.
   No screenshot, live-test item, or official answer key is reproduced. */
'use strict';

(() => {
  const esc = (value) => String(value).replace(/[&<>"']/g, (ch) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[ch]));
  const intro = (fr, en) => ({ fr, en });
  const pair = (fr, en) => ({ fr, en });

  function tableHtml(title, headers, rows, note) {
    return '<div class="ubs-sheet"><h3 class="ubs-sheet-title">' + esc(title) + '</h3>' +
      (note ? '<p class="ubs-sheet-note">' + esc(note) + '</p>' : '') +
      '<div class="ubs-table-wrap"><table class="nvtbl"><thead><tr>' +
      headers.map((h, i) => '<th' + (i === 0 ? ' class="k" scope="col"' : ' scope="col"') + '>' + esc(h) + '</th>').join('') +
      '</tr></thead><tbody>' + rows.map((row) => '<tr' + (row.strong ? ' class="s"' : '') + '>' +
        row.cells.map((cell, i) => '<td' + (i === 0 ? ' class="k"' : '') + '>' + esc(cell) + '</td>').join('') +
        '</tr>').join('') + '</tbody></table></div></div>';
  }

  function tableSheet(id, nameFr, nameEn, titleFr, titleEn, headersFr, headersEn, rowsFr, rowsEn, noteFr, noteEn) {
    const rows = (source) => source.map((cells) => ({ cells, strong: !!cells.strong }));
    return {
      id, nameFr, nameEn,
      fr: tableHtml(titleFr, headersFr, rows(rowsFr), noteFr),
      en: tableHtml(titleEn, headersEn, rows(rowsEn), noteEn)
    };
  }

  function marketBars(lang) {
    const fr = lang === 'fr';
    const title = fr ? 'Part du marché européen des soins personnels — FY24' : 'European personal-care market share — FY24';
    const note = fr ? 'Part en valeur ; marché total : 12,5 Md€.' : 'Share by value; total market: €12.5bn.';
    const labels = fr ? ['Valen & Co', 'Northstar', 'Solace', 'Mira', 'Autres'] : ['Valen & Co', 'Northstar', 'Solace', 'Mira', 'Others'];
    const values = [29, 24, 18, 14, 15];
    const colors = ['#9aa6b2', '#ec0000', '#6588a5', '#c8a85a', '#d7dce1'];
    const bars = values.map((value, i) => '<div class="ubs-bar-row"><span class="ubs-bar-name">' + esc(labels[i]) +
      '</span><span class="ubs-bar-track"><i style="width:' + (value / 32 * 100) + '%;background:' + colors[i] + '"></i></span>' +
      '<b class="ubs-bar-value">' + value + '%</b></div>').join('');
    const headers = fr ? ['Entreprise', 'Part FY24'] : ['Company', 'FY24 share'];
    const rows = labels.map((label, i) => ({ cells: [label, values[i] + '%'] }));
    return '<div class="ubs-sheet"><h3 class="ubs-sheet-title">' + esc(title) + '</h3><p class="ubs-sheet-note">' + esc(note) +
      '</p><div class="ubs-bars" role="img" aria-label="' + esc(title) + '">' + bars + '</div>' +
      '<div class="ubs-table-wrap"><table class="nvtbl"><thead><tr>' + headers.map((h, i) => '<th' + (i === 0 ? ' class="k"' : '') + '>' + esc(h) + '</th>').join('') +
      '</tr></thead><tbody>' + rows.map((r) => '<tr><td class="k">' + esc(r.cells[0]) + '</td><td>' + esc(r.cells[1]) + '</td></tr>').join('') +
      '</tbody></table></div></div>';
  }

  function equityChart(lang) {
    const fr = lang === 'fr';
    const years = ['FY21', 'FY22', 'FY23', 'FY24'];
    const series = [
      { label: fr ? 'Northstar (groupe)' : 'Northstar (group)', values: [12.1, 13.5, 11.8, 14.2], color: '#ec0000' },
      { label: fr ? 'Indice sectoriel' : 'Sector benchmark', values: [10.7, 11.6, 12.0, 12.9], color: '#36759b' },
      { label: fr ? 'Personal Care' : 'Personal Care division', values: [8.9, 9.6, 10.2, 10.8], color: '#80934c' }
    ];
    const W = 620, H = 270, L = 46, R = 18, T = 18, B = 44;
    const plotW = W - L - R, plotH = H - T - B, max = 16;
    const x = (i) => L + (plotW * i / (years.length - 1));
    const y = (v) => T + plotH * (max - v) / max;
    const grid = [0, 4, 8, 12, 16].map((tick) => '<line x1="' + L + '" y1="' + y(tick) + '" x2="' + (W - R) + '" y2="' + y(tick) + '" stroke="#e4e8eb"/>' +
      '<text x="' + (L - 8) + '" y="' + (y(tick) + 4) + '" text-anchor="end" font-size="11" fill="#75808a">' + tick + '%</text>').join('');
    const xLabels = years.map((year, i) => '<text x="' + x(i) + '" y="' + (H - 15) + '" text-anchor="middle" font-size="11" fill="#5a656e">' + year + '</text>').join('');
    const lines = series.map((s) => '<polyline fill="none" stroke="' + s.color + '" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" points="' +
      s.values.map((v, i) => x(i) + ',' + y(v)).join(' ') + '"/>' + s.values.map((v, i) => '<circle cx="' + x(i) + '" cy="' + y(v) + '" r="4" fill="' + s.color + '"/>' +
        '<text x="' + x(i) + '" y="' + (y(v) - 9) + '" text-anchor="middle" font-size="10" fill="#38434b">' + v.toFixed(1) + '</text>').join('')).join('');
    const legend = series.map((s) => '<span class="ubs-legend-item"><i style="background:' + s.color + '"></i>' + esc(s.label) + '</span>').join('');
    const headers = fr ? ['Série', ...years] : ['Series', ...years];
    const rows = series.map((s) => '<tr><td class="k">' + esc(s.label) + '</td>' + s.values.map((v) => '<td>' + v.toFixed(1) + '%</td>').join('') + '</tr>').join('');
    return '<div class="ubs-sheet"><h3 class="ubs-sheet-title">' + (fr ? 'Rendement des capitaux propres' : 'Return on equity') +
      '</h3><p class="ubs-sheet-note">' + (fr ? 'Rendement annuel en pourcentage.' : 'Annual return, percent.') + '</p>' +
      '<svg class="ubs-line-chart" viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="' + (fr ? 'Rendement annuel des capitaux propres' : 'Annual return on equity') + '" xmlns="http://www.w3.org/2000/svg">' +
      grid + lines + xLabels + '</svg><div class="ubs-chart-legend">' + legend + '</div>' +
      '<div class="ubs-table-wrap"><table class="nvtbl"><thead><tr>' + headers.map((h, i) => '<th' + (i === 0 ? ' class="k"' : '') + '>' + esc(h) + '</th>').join('') +
      '</tr></thead><tbody>' + rows + '</tbody></table></div></div>';
  }

  function forecastSheet(lang) {
    const fr = lang === 'fr';
    const title = fr ? 'Prévision de la répartition des revenus par activité' : 'Forecast revenue mix by division';
    const note = fr ? 'Prévision en pourcentage du revenu total.' : 'Forecast as a percentage of total revenue.';
    const labels = fr ? ['Home Care', 'Personal Care', 'Nutrition'] : ['Home Care', 'Personal Care', 'Nutrition'];
    const data = [[32, 34], [38, 39], [30, 27]];
    const colors = ['#8aa1b5', '#ec0000', '#b0a16a'];
    const bars = data.map((values, i) => '<div class="ubs-forecast-row"><span>' + esc(labels[i]) + '</span>' + values.map((v, j) =>
      '<span class="ubs-forecast-cell"><small>FY' + (25 + j) + '</small><i class="ubs-bar-track"><b style="width:' + v + '%;background:' + colors[i] + '"></b></i><strong>' + v + '%</strong></span>').join('') + '</div>').join('');
    const headers = fr ? ['Division', 'FY25', 'FY26'] : ['Division', 'FY25', 'FY26'];
    const rows = labels.map((label, i) => '<tr><td class="k">' + esc(label) + '</td><td>' + data[i][0] + '%</td><td>' + data[i][1] + '%</td></tr>').join('');
    return '<div class="ubs-sheet"><h3 class="ubs-sheet-title">' + esc(title) + '</h3><p class="ubs-sheet-note">' + esc(note) + '</p>' +
      '<div class="ubs-forecast">' + bars + '</div><div class="ubs-table-wrap"><table class="nvtbl"><thead><tr>' +
      headers.map((h, i) => '<th' + (i === 0 ? ' class="k"' : '') + '>' + esc(h) + '</th>').join('') + '</tr></thead><tbody>' + rows + '</tbody></table></div></div>';
  }

  const sheets = [
    tableSheet('revenue', 'Revenus', 'Revenues', 'Chiffre d’affaires', 'Revenue by product line',
      ['Ligne de produits', 'FY22', 'FY23', 'FY24'], ['Product line', 'FY22', 'FY23', 'FY24'],
      [['Revenu total', '18 400', '19 760', '21 300'], ['Gammes sous licence', '3 200', '3 080', '2 950'], ['Gammes détenues', '15 200', '16 680', '18 350'], ['Home Care', '6 300', '6 850', '7 250'], ['Personal Care', '5 600', '6 170', '6 900'], ['Nutrition', '3 300', '3 660', '4 200']],
      [['Total revenue', '18 400', '19 760', '21 300'], ['Licensed ranges', '3 200', '3 080', '2 950'], ['Owned ranges', '15 200', '16 680', '18 350'], ['Home Care', '6 300', '6 850', '7 250'], ['Personal Care', '5 600', '6 170', '6 900'], ['Nutrition', '3 300', '3 660', '4 200']],
      'Montants en millions d’euros (€m).', 'Amounts in millions of euros (€m).'),
    tableSheet('costs', 'Coûts', 'Costs', 'Coûts par catégorie', 'Costs by category',
      ['Catégorie', 'FY22', 'FY23', 'FY24'], ['Cost category', 'FY22', 'FY23', 'FY24'],
      [['Matières premières', '4 200', '4 360', '4 610'], ['Personnel', '3 100', '3 220', '3 340'], ['Distribution', '2 700', '2 790', '2 940'], ['Recherche & développement', '920', '1 020', '1 090'], ['Marketing', '1 180', '1 230', '1 280'], ['Énergie', '520', '480', '460'], ['Administration', '1 170', '1 260', '1 430'], ['Coûts totaux', '13 790', '14 360', '15 150']],
      [['Raw materials', '4 200', '4 360', '4 610'], ['Personnel', '3 100', '3 220', '3 340'], ['Distribution', '2 700', '2 790', '2 940'], ['Research & development', '920', '1 020', '1 090'], ['Marketing', '1 180', '1 230', '1 280'], ['Energy', '520', '480', '460'], ['Administration', '1 170', '1 260', '1 430'], ['Total costs', '13 790', '14 360', '15 150']],
      'Montants en millions d’euros (€m).', 'Amounts in millions of euros (€m).'),
    {
      id: 'market', nameFr: 'Parts de marché', nameEn: 'Market shares',
      fr: marketBars('fr'), en: marketBars('en')
    },
    tableSheet('employees', 'Effectifs', 'Employees', 'Effectifs par région', 'Headcount by region',
      ['Région', 'FY22', 'FY23', 'FY24'], ['Region', 'FY22', 'FY23', 'FY24'],
      [['Royaume-Uni', '1 240', '1 290', '1 330'], ['Europe hors Royaume-Uni', '870', '930', '975'], ['Amériques', '630', '610', '650'], ['Asie-Pacifique', '410', '450', '485'], ['Total', '3 150', '3 280', '3 440']],
      [['United Kingdom', '1 240', '1 290', '1 330'], ['Europe excl. UK', '870', '930', '975'], ['Americas', '630', '610', '650'], ['Asia-Pacific', '410', '450', '485'], ['Total', '3 150', '3 280', '3 440']],
      'Effectif à la clôture de chaque exercice.', 'Headcount at the end of each financial year.'),
    {
      id: 'equity', nameFr: 'Rendement des capitaux propres', nameEn: 'Equity return',
      fr: equityChart('fr'), en: equityChart('en')
    },
    {
      id: 'forecast', nameFr: 'Prévisions', nameEn: 'Forecast',
      fr: forecastSheet('fr'), en: forecastSheet('en')
    }
  ];

  const numerical = [
    { tab: 'revenue', q: pair('Le chiffre d’affaires total du groupe a augmenté à chaque exercice, de FY22 à FY24.', 'Group revenue increased in every financial year from FY22 to FY24.'), a: 0,
      why: pair('Le revenu total passe de 18 400 à 19 760 puis à 21 300 M€.', 'Total revenue moves from €18,400m to €19,760m and then to €21,300m.') },
    { tab: 'revenue', q: pair('Les revenus des gammes sous licence ont dépassé 3 000 M€ en FY24.', 'Revenue from licensed ranges exceeded €3,000m in FY24.'), a: 1,
      why: pair('Le montant FY24 est de 2 950 M€, donc inférieur à 3 000 M€.', 'FY24 licensed-range revenue is €2,950m, below €3,000m.') },
    { tab: 'revenue', q: pair('La marge bénéficiaire des gammes sous licence s’est améliorée entre FY22 et FY24.', 'The profit margin on licensed ranges improved between FY22 and FY24.'), a: 2,
      why: pair('La feuille donne le revenu, mais ni le bénéfice ni la marge par gamme.', 'The sheet gives revenue, but not profit or margin by product range.') },
    { tab: 'costs', q: pair('En FY24, les coûts de matières premières représentaient au moins cinq fois les coûts d’énergie.', 'In FY24, raw-material costs were at least five times energy costs.'), a: 0,
      why: pair('4 610 ÷ 460 ≈ 10,0 ; le seuil de cinq fois est dépassé.', '€4,610m ÷ €460m is about 10.0, which is above five times.') },
    { tab: 'costs', q: pair('Les coûts totaux de FY24 étaient inférieurs à ceux de FY22.', 'Total costs in FY24 were lower than in FY22.'), a: 1,
      why: pair('Les coûts totaux passent de 13 790 M€ en FY22 à 15 150 M€ en FY24.', 'Total costs rise from €13,790m in FY22 to €15,150m in FY24.') },
    { tab: 'costs', q: pair('Les coûts administratifs de FY25 devraient augmenter.', 'Administrative costs are expected to increase in FY25.'), a: 2,
      why: pair('La feuille ne contient que les données historiques FY22–FY24 et aucune prévision des coûts.', 'The sheet contains only FY22–FY24 historical costs and no cost forecast.') },
    { tab: 'market', q: pair('Northstar détenait la plus grande part du marché en FY24.', 'Northstar held the largest market share in FY24.'), a: 1,
      why: pair('Valen & Co mène avec 29 %, contre 24 % pour Northstar.', 'Valen & Co leads with 29%, compared with Northstar at 24%.') },
    { tab: 'market', q: pair('Les parts de Solace et Mira représentaient ensemble plus de 30 % du marché.', 'Solace and Mira together accounted for more than 30% of the market.'), a: 0,
      why: pair('18 % + 14 % = 32 %.', '18% + 14% = 32%.') },
    { tab: 'market', q: pair('Northstar a vendu plus d’unités que Valen & Co en FY24.', 'Northstar sold more units than Valen & Co in FY24.'), a: 2,
      why: pair('Les parts sont calculées en valeur. La feuille ne donne pas le nombre d’unités vendues.', 'Market shares are by value; the sheet does not give the number of units sold.') },
    { tab: 'employees', q: pair('L’effectif total a augmenté à chaque exercice, de FY22 à FY24.', 'Total headcount increased in every financial year from FY22 to FY24.'), a: 0,
      why: pair('Le total progresse de 3 150 à 3 280 puis à 3 440.', 'Total headcount rises from 3,150 to 3,280 and then to 3,440.') },
    { tab: 'employees', q: pair('En FY24, le Royaume-Uni comptait plus d’employés que toutes les autres régions réunies.', 'In FY24, the UK had more employees than all other regions combined.'), a: 1,
      why: pair('Le Royaume-Uni compte 1 330 employés ; les autres régions en totalisent 2 110.', 'The UK has 1,330 employees; the other regions total 2,110.') },
    { tab: 'employees', q: pair('L’effectif Asie-Pacifique a augmenté à chaque exercice.', 'Asia-Pacific headcount increased in every financial year.'), a: 0,
      why: pair('Il passe de 410 à 450 puis à 485.', 'It rises from 410 to 450 and then to 485.') },
    { tab: 'equity', q: pair('Le rendement des capitaux propres de Northstar a dépassé l’indice sectoriel à chaque exercice.', 'Northstar’s return on equity exceeded the sector benchmark in every year shown.'), a: 1,
      why: pair('En FY23, Northstar est à 11,8 %, sous l’indice sectoriel à 12,0 %.', 'In FY23, Northstar is at 11.8%, below the sector benchmark at 12.0%.') },
    { tab: 'equity', q: pair('Le rendement des capitaux propres de Northstar a atteint son niveau le plus élevé en FY24.', 'Northstar’s return on equity was highest in FY24.'), a: 0,
      why: pair('La série Northstar culmine à 14,2 % en FY24.', 'Northstar’s series peaks at 14.2% in FY24.') },
    { tab: 'equity', q: pair('Le rendement du dividende de Northstar était supérieur à celui de l’indice sectoriel.', 'Northstar’s dividend yield was higher than the sector benchmark’s.'), a: 2,
      why: pair('La feuille porte sur le rendement des capitaux propres, pas sur le rendement du dividende.', 'The sheet shows return on equity, not dividend yield.') },
    { tab: 'forecast', q: pair('Personal Care devrait conserver la plus grande part des revenus en FY25 et FY26.', 'Personal Care is forecast to remain the largest revenue division in FY25 and FY26.'), a: 0,
      why: pair('Personal Care est à 38 % puis 39 %, devant Home Care et Nutrition les deux années.', 'Personal Care is at 38% and 39%, ahead of Home Care and Nutrition in both years.') },
    { tab: 'forecast', q: pair('La part de Nutrition devrait augmenter entre FY25 et FY26.', 'Nutrition’s forecast share is expected to increase between FY25 and FY26.'), a: 1,
      why: pair('La part diminue de 30 % à 27 %.', 'The share decreases from 30% to 27%.') },
    { tab: 'forecast', q: pair('La part de Home Care devrait gagner deux points de pourcentage entre FY25 et FY26.', 'Home Care’s share is forecast to gain two percentage points between FY25 and FY26.'), a: 0,
      why: pair('La part progresse de 32 % à 34 %, soit deux points de pourcentage.', 'The share rises from 32% to 34%, a two-percentage-point increase.') }
  ].map((item, i) => Object.assign({ id: 'UBSN' + (i + 1), kind: 'numverb' }, item));

  const examples = [
    { id: 'UBSX1', kind: 'numverb', tab: 'revenue', q: pair('Le revenu total était supérieur à 20 000 M€ en FY24.', 'Total revenue was above €20,000m in FY24.'), a: 0,
      why: pair('Le tableau affiche 21 300 M€ en FY24.', 'The table shows €21,300m for FY24.') },
    { id: 'UBSX2', kind: 'numverb', tab: 'employees', q: pair('L’effectif des Amériques a augmenté de FY22 à FY23.', 'Headcount in the Americas increased from FY22 to FY23.'), a: 1,
      why: pair('Il passe de 630 à 610.', 'It falls from 630 to 610.') },
    { id: 'UBSX3', kind: 'numverb', tab: 'market', q: pair('La part de marché de Northstar était supérieure à 20 % en FY24.', 'Northstar’s market share was above 20% in FY24.'), a: 0,
      why: pair('La part de Northstar est de 24 %.', 'Northstar’s share is 24%.') }
  ];

  const culturePractice = {
    scenario: pair(
      'Un collègue risque de manquer une échéance parce qu’un fichier de données est incomplet. Comment réagissez-vous ?',
      'A colleague may miss a deadline because a data file is incomplete. What do you do?'
    ),
    actions: [
      pair('Clarifier ce qui manque, convenir d’un plan rapide et signaler tôt tout risque de livraison.', 'Clarify what is missing, agree a quick plan, and flag any delivery risk early.'),
      pair('Terminer uniquement votre propre partie et supposer que le collègue trouvera une solution.', 'Finish only your own part and assume the colleague will find a solution.'),
      pair('Prévenir immédiatement le manager que ce collègue n’est pas fiable.', 'Tell the manager immediately that the colleague is unreliable.')
    ],
    best: 0, least: 2,
    why: pair('Une réponse efficace traite le blocage et rend le risque visible sans rejeter la faute sur quelqu’un.', 'An effective response addresses the blocker and makes the risk visible without blaming someone.')
  };

  const culture = [
    {
      scenario: pair('Un client vous demande d’envoyer une version préliminaire d’une analyse avant la validation requise par la procédure.', 'A client asks you to send a draft analysis before the review required by procedure.'),
      actions: [
        pair('Expliquer le délai de validation, proposer une heure de retour réaliste et signaler tout impact sur l’échéance.', 'Explain the review step, give a realistic return time, and flag any impact on the deadline.'),
        pair('Envoyer le document en précisant oralement qu’il n’est pas encore validé.', 'Send the document and mention verbally that it has not yet been reviewed.'),
        pair('Retirer les contrôles en attente pour répondre plus vite au client.', 'Remove the outstanding checks so you can answer the client faster.')
      ], best: 0, least: 2,
      why: pair('La transparence et une échéance claire protègent la qualité. Contourner les contrôles crée un risque de conformité.', 'Transparency and a clear deadline protect quality. Bypassing checks creates a compliance risk.')
    },
    {
      scenario: pair('Vous repérez une erreur dans une présentation déjà transmise à votre responsable.', 'You spot an error in a presentation that has already been sent to your manager.'),
      actions: [
        pair('Vérifier le chiffre, prévenir rapidement votre responsable et transmettre une version corrigée avec l’impact expliqué.', 'Verify the figure, tell your manager promptly, and send a corrected version explaining the impact.'),
        pair('Attendre la réunion de suivi pour voir si quelqu’un remarque l’erreur.', 'Wait for the next review meeting to see whether anyone notices the error.'),
        pair('Modifier votre copie sans informer les personnes qui ont reçu la présentation.', 'Change your own copy without informing anyone who received the presentation.')
      ], best: 0, least: 1,
      why: pair('Il faut confirmer l’erreur puis corriger rapidement la version partagée. La dissimuler retarde la résolution.', 'Confirm the error, then correct the shared version promptly. Concealing it delays resolution.')
    },
    {
      scenario: pair('Pendant une réunion, une collègue plus discrète semble avoir une information utile, mais n’a pas encore parlé.', 'In a meeting, a quieter colleague appears to have useful information but has not spoken yet.'),
      actions: [
        pair('Lui laisser un espace pour intervenir et lui demander si elle souhaite compléter un point précis.', 'Make space for her to contribute and ask whether she would like to add to a specific point.'),
        pair('Résumer à sa place ce que vous pensez qu’elle voulait dire.', 'Summarise on her behalf what you think she was going to say.'),
        pair('Poursuivre l’ordre du jour sans l’inviter à intervenir.', 'Continue the agenda without inviting her to contribute.')
      ], best: 0, least: 1,
      why: pair('Inviter la collègue à s’exprimer directement respecte son expertise. Parler à sa place peut déformer son avis.', 'Inviting the colleague to speak directly respects her expertise. Speaking for her may misrepresent her view.')
    },
    {
      scenario: pair('Une demande de votre responsable manque de précision sur le périmètre et le format attendus.', 'A request from your manager is unclear about the scope and expected format.'),
      actions: [
        pair('Poser deux ou trois questions ciblées, confirmer le livrable et convenir d’un point d’avancement.', 'Ask a few focused questions, confirm the deliverable, and agree a progress check-in.'),
        pair('Faire une hypothèse sur le besoin et produire immédiatement une analyse complète.', 'Guess what is needed and immediately produce a full analysis.'),
        pair('Ne rien commencer tant que votre responsable n’a pas envoyé une nouvelle consigne écrite.', 'Do not start until your manager sends a new written instruction.')
      ], best: 0, least: 1,
      why: pair('Clarifier tôt évite le travail inutile et permet d’avancer. Une hypothèse non vérifiée augmente le risque d’erreur.', 'Early clarification avoids rework while keeping momentum. An unverified assumption increases the risk of error.')
    },
    {
      scenario: pair('Un fichier contenant des informations client a été envoyé par erreur à une liste interne trop large.', 'A file containing client information was mistakenly sent to an overly broad internal mailing list.'),
      actions: [
        pair('Suivre la procédure d’incident, avertir rapidement le responsable désigné et limiter tout nouvel accès au fichier.', 'Follow the incident process, promptly alert the designated contact, and limit any further access to the file.'),
        pair('Demander aux destinataires de supprimer le message puis attendre de voir si le problème persiste.', 'Ask recipients to delete the message, then wait to see whether the issue continues.'),
        pair('Transférer le fichier à un collègue de confiance pour demander son avis.', 'Forward the file to a trusted colleague for advice.')
      ], best: 0, least: 2,
      why: pair('Un incident de confidentialité doit être déclaré par les canaux prévus. Le transférer étend l’exposition.', 'A confidentiality incident must be reported through the proper channel. Forwarding it expands exposure.')
    },
    {
      scenario: pair('Deux équipes vous demandent des livrables urgents pour des échéances qui se chevauchent.', 'Two teams request urgent deliverables with overlapping deadlines.'),
      actions: [
        pair('Comparer l’impact et les délais, puis aligner les interlocuteurs et votre responsable sur un ordre de priorité.', 'Compare impact and deadlines, then align the requesters and your manager on a priority order.'),
        pair('Choisir seul la demande qui semble la plus intéressante et ignorer l’autre.', 'Choose the request that seems more interesting and ignore the other.'),
        pair('Accepter les deux échéances sans prévenir, même si elles ne sont pas réalisables.', 'Accept both deadlines without warning anyone, even if they are not achievable.')
      ], best: 0, least: 2,
      why: pair('Une priorisation explicite permet de gérer les attentes. Promettre l’impossible masque le risque jusqu’à l’échéance.', 'Explicit prioritisation manages expectations. An impossible promise hides risk until the deadline.')
    },
    {
      scenario: pair('Un relecteur critique la structure de votre note et vous demande de rendre la recommandation plus claire.', 'A reviewer criticises the structure of your note and asks you to make the recommendation clearer.'),
      actions: [
        pair('Demander quel passage manque de clarté, revoir le fil logique et renvoyer une version améliorée.', 'Ask which passage is unclear, revisit the logic, and send an improved version.'),
        pair('Défendre immédiatement votre première version sans examiner les remarques.', 'Immediately defend your first version without examining the comments.'),
        pair('Appliquer tous les changements proposés sans vérifier s’ils modifient le sens de l’analyse.', 'Apply every suggested change without checking whether it changes the meaning of the analysis.')
      ], best: 0, least: 1,
      why: pair('Le retour précis permet d’améliorer le livrable tout en gardant la responsabilité du fond.', 'Specific feedback helps improve the deliverable while preserving responsibility for its substance.')
    },
    {
      scenario: pair('Un membre de l’équipe défend une méthode différente de la vôtre pour estimer un risque.', 'A teammate supports a different method from yours for estimating a risk.'),
      actions: [
        pair('Comparer les hypothèses et les données des deux méthodes, puis convenir d’un test ou d’une revue commune.', 'Compare the assumptions and evidence behind both methods, then agree on a joint test or review.'),
        pair('Présenter votre méthode comme définitive avant d’avoir examiné son raisonnement.', 'Present your method as final before examining their reasoning.'),
        pair('Écarter les deux approches et laisser le désaccord sans décision.', 'Discard both approaches and leave the disagreement unresolved.')
      ], best: 0, least: 1,
      why: pair('Une comparaison fondée sur les preuves transforme le désaccord en décision exploitable.', 'Evidence-based comparison turns disagreement into a useful decision.')
    },
    {
      scenario: pair('Un client souhaite que votre prévision aboutisse à un résultat plus favorable que ne le suggèrent les données.', 'A client would like your forecast to produce a more favourable result than the evidence supports.'),
      actions: [
        pair('Présenter les hypothèses et les limites, puis montrer des scénarios alternatifs clairement étiquetés.', 'Explain the assumptions and limitations, then show clearly labelled alternative scenarios.'),
        pair('Ajuster discrètement une hypothèse pour atteindre le résultat demandé.', 'Quietly adjust an assumption to reach the requested result.'),
        pair('Refuser toute discussion sur la prévision et clore l’échange.', 'Refuse any discussion of the forecast and end the conversation.')
      ], best: 0, least: 1,
      why: pair('Des scénarios transparents répondent au besoin du client sans déformer l’analyse.', 'Transparent scenarios address the client’s need without distorting the analysis.')
    },
    {
      scenario: pair('Vous devez présenter à un comité un sujet dont vous ne maîtrisez qu’une partie.', 'You need to brief a committee on a topic where you understand only part of the detail.'),
      actions: [
        pair('Présenter les faits confirmés, préciser les points à vérifier et proposer un suivi après validation.', 'Present confirmed facts, identify what still needs checking, and offer a follow-up after validation.'),
        pair('Répondre avec assurance à toutes les questions pour ne pas donner l’impression d’hésiter.', 'Answer every question confidently so you do not appear uncertain.'),
        pair('Laisser un collègue présenter à votre place sans lui transmettre les éléments déjà vérifiés.', 'Let a colleague present for you without sharing the points you have already verified.')
      ], best: 0, least: 1,
      why: pair('Distinguer les faits confirmés des incertitudes protège la qualité de la décision.', 'Separating confirmed facts from uncertainty protects decision quality.')
    },
    {
      scenario: pair('Un collègue vous propose d’utiliser une adresse personnelle pour envoyer un document confidentiel, car le système sécurisé est lent.', 'A colleague suggests using a personal email address for a confidential file because the secure system is slow.'),
      actions: [
        pair('Refuser ce canal et utiliser le moyen approuvé, en signalant le délai si celui-ci affecte le projet.', 'Decline that channel and use the approved method, flagging the delay if it affects the project.'),
        pair('Envoyer le fichier une seule fois puis supprimer le message envoyé.', 'Send the file once and then delete the sent message.'),
        pair('Envoyer le document à un autre collègue pour qu’il choisisse le canal à utiliser.', 'Send the document to another colleague and let them choose the channel.')
      ], best: 0, least: 1,
      why: pair('Les règles de sécurité s’appliquent même sous pression de délai ; il faut ensuite gérer l’impact avec transparence.', 'Security rules still apply under time pressure; manage any resulting delay transparently.')
    },
    {
      scenario: pair('Une nouvelle application interne vient d’être déployée et vous ne connaissez pas encore toutes ses fonctions.', 'A new internal application has just been launched, and you do not know all of its functions yet.'),
      actions: [
        pair('Consulter le guide, tester sur un exemple sans risque et demander de l’aide sur les étapes non maîtrisées.', 'Review the guide, test on a safe example, and ask for help on steps you do not understand.'),
        pair('Traiter tout de suite une opération importante en supposant que l’interface fonctionne comme l’ancienne.', 'Process an important transaction immediately, assuming the interface works like the old one.'),
        pair('Éviter l’application et conserver votre méthode locale sans en informer l’équipe.', 'Avoid the application and keep using your own local method without telling the team.')
      ], best: 0, least: 1,
      why: pair('Une prise en main guidée réduit le risque tout en permettant de progresser rapidement.', 'A guided first use reduces risk while helping you get up to speed.')
    },
    {
      scenario: pair('Votre projet prend du retard après qu’une dépendance externe a été livrée en retard.', 'Your project is falling behind after an external dependency arrived late.'),
      actions: [
        pair('Identifier les tâches bloquées, recalibrer le plan avec l’équipe et informer tôt les personnes concernées.', 'Identify blocked tasks, replan with the team, and inform affected stakeholders early.'),
        pair('Masquer le retard jusqu’à ce que vous puissiez présenter une solution complète.', 'Hide the delay until you can present a complete solution.'),
        pair('Continuer le plan initial sans vérifier si les échéances restent réalistes.', 'Continue the original plan without checking whether the deadlines remain realistic.')
      ], best: 0, least: 1,
      why: pair('La visibilité précoce permet de réduire l’impact et d’ajuster les attentes.', 'Early visibility helps reduce the impact and reset expectations.')
    },
    {
      scenario: pair('Une équipe partenaire n’a pas fourni les informations nécessaires à votre analyse.', 'A partner team has not provided information needed for your analysis.'),
      actions: [
        pair('La contacter directement pour comprendre le blocage et convenir d’un nouveau délai ; escalader si le risque persiste.', 'Contact them directly to understand the blocker and agree a new time; escalate if the risk persists.'),
        pair('Envoyer une copie de votre demande à toute l’équipe dirigeante en indiquant qu’ils bloquent le projet.', 'Copy the entire leadership team on your request and say the team is blocking the project.'),
        pair('Remplacer les données manquantes par une estimation non vérifiée afin de tenir le délai.', 'Replace the missing data with an unverified estimate to meet the deadline.')
      ], best: 0, least: 2,
      why: pair('Un échange direct règle souvent le blocage ; une estimation non validée fragilise les conclusions.', 'Direct discussion often resolves the blocker; an unverified estimate weakens the conclusions.')
    },
    {
      scenario: pair('Vous entendez une rumeur non confirmée au sujet d’un client sensible.', 'You hear an unverified rumour about a sensitive client.'),
      actions: [
        pair('Ne pas la diffuser, vérifier auprès d’une source autorisée et signaler tout risque concret par le canal adapté.', 'Do not circulate it; check with an authorised source and report any concrete risk through the right channel.'),
        pair('En parler de façon informelle à plusieurs collègues pour savoir s’ils ont entendu la même chose.', 'Discuss it informally with several colleagues to see whether they heard the same thing.'),
        pair('La transmettre au client pour lui donner l’occasion de répondre.', 'Forward it to the client to give them a chance to respond.')
      ], best: 0, least: 1,
      why: pair('La discrétion et la vérification protègent la confidentialité et évitent d’amplifier une information incertaine.', 'Discretion and verification protect confidentiality and prevent an uncertain claim from spreading.')
    },
    {
      scenario: pair('On vous confie une tâche urgente qui dépasse votre niveau d’expertise actuel.', 'You are assigned an urgent task that is beyond your current level of expertise.'),
      actions: [
        pair('Expliquer ce que vous pouvez traiter, demander une revue experte sur les points sensibles et proposer un délai réaliste.', 'Explain what you can handle, request expert review on sensitive points, and propose a realistic timeline.'),
        pair('Produire seul le livrable complet et le transmettre sans mentionner vos limites.', 'Produce the complete deliverable alone and send it without mentioning your limitations.'),
        pair('Refuser immédiatement la tâche sans chercher à clarifier les attentes ou à demander du soutien.', 'Immediately refuse the task without clarifying expectations or asking for support.')
      ], best: 0, least: 1,
      why: pair('La transparence sur les limites, combinée à une solution de revue, permet d’avancer sans sacrifier la qualité.', 'Being transparent about your limits while arranging a review preserves momentum and quality.')
    },
    {
      scenario: pair('De nouvelles informations reçues avant une réunion client remettent en question votre recommandation initiale.', 'New information received before a client meeting calls your initial recommendation into question.'),
      actions: [
        pair('Vérifier l’information, expliquer l’impact potentiel à votre responsable et mettre à jour la recommandation avant de la présenter.', 'Verify the information, explain its potential impact to your manager, and update the recommendation before presenting.'),
        pair('Maintenir la recommandation initiale pour éviter de compliquer la réunion.', 'Keep the original recommendation to avoid complicating the meeting.'),
        pair('Présenter la nouvelle information comme certaine avant d’en vérifier la source.', 'Present the new information as certain before checking its source.')
      ], best: 0, least: 1,
      why: pair('La recommandation doit refléter les faits validés ; vérifier puis actualiser est plus responsable que cacher ou extrapoler.', 'A recommendation should reflect verified facts; checking and updating is better than hiding or overstating.')
    },
    {
      scenario: pair('Vous remarquez qu’une tâche répétitive ralentit l’équipe, mais une échéance importante approche.', 'You notice a repetitive task is slowing the team down, but an important deadline is approaching.'),
      actions: [
        pair('Sécuriser d’abord le livrable attendu, puis proposer une amélioration documentée après l’échéance.', 'Secure the required deliverable first, then propose a documented improvement after the deadline.'),
        pair('Remplacer immédiatement le processus par votre propre méthode sans consulter l’équipe.', 'Replace the process immediately with your own method without consulting the team.'),
        pair('Ne jamais soulever le sujet, puisque le processus existe déjà.', 'Never raise the issue because the process is already in place.')
      ], best: 0, least: 1,
      why: pair('Cette approche protège l’échéance tout en ouvrant la voie à une amélioration concertée.', 'This approach protects the deadline while leaving room for a considered improvement.')
    }
  ];

  BANK.ubsNumericalSheets = sheets;
  BANK.ubsNumerical = numerical;
  BANK.ubsNumericalExamples = examples;
  BANK.ubsCulturePractice = culturePractice;
  BANK.ubsCulture = culture.map((item, i) => Object.assign({ id: 'UBSC' + (i + 1) }, item));

  BANK.INTRO['ubs-num-18'] = [
    intro(
      '<p>Ce test d’entraînement mesure votre capacité à lire des tableaux et des graphiques puis à évaluer des affirmations sur la seule base des données affichées.</p><p>Pour chaque affirmation, choisissez <b>TRUE</b> si elle est nécessairement vraie, <b>FALSE</b> si elle est nécessairement fausse, ou <b>CANNOT SAY</b> si la feuille ne permet pas de trancher. Six feuilles de données restent consultables pendant l’épreuve.</p><p>Les noms, chiffres et questions de cette version sont fictifs et ont été écrits pour l’entraînement ; ils ne reproduisent pas le contenu du test UBS.</p>',
      '<p>This practice test checks how quickly you can read tables and charts and evaluate statements using only the displayed data.</p><p>For each statement, choose <b>TRUE</b> if it must be true, <b>FALSE</b> if it must be false, or <b>CANNOT SAY</b> if the sheet does not provide enough information. Six data sheets remain available throughout the test.</p><p>All names, figures, and questions in this practice version are fictional and original; they do not reproduce UBS test content.</p>'
    ),
    intro(
      '<p>Veuillez noter :</p><ul><li>Le test comprend <b>18 affirmations en 6 minutes</b>.</li><li>Chaque affirmation se rapporte à une feuille de données ; vous pouvez changer d’onglet sans quitter la question.</li><li>Une seule réponse est correcte ; les réponses peuvent être modifiées avec les flèches ou la grille de navigation.</li><li>Le chronomètre démarre avec la première question. Vous pouvez terminer plus tôt une fois toutes les réponses données.</li><li>Une calculatrice et du papier peuvent vous aider.</li></ul>',
      '<p>Please note:</p><ul><li>The test contains <b>18 statements in 6 minutes</b>.</li><li>Each statement relates to a data sheet; you can switch sheets without leaving the question.</li><li>There is one correct answer per statement; answers can be changed with the arrows or question grid.</li><li>The timer starts with the first question. You can finish early once every answer is recorded.</li><li>A calculator and scratch paper may help.</li></ul>'
    )
  ];
  BANK.INTRO['ubs-cult-action'] = [
    intro(
      '<p>Ce module d’entraînement présente des situations professionnelles et trois réactions possibles. Pour chaque situation, sélectionnez l’action <b>la plus efficace</b> et celle <b>la moins efficace</b>.</p><p>Évaluez les options au regard de la collaboration, de l’intégrité, de la qualité du travail, du service client et de la gestion des risques. Les scénarios sont originaux et les résultats constituent un repère d’entraînement, pas une notation officielle UBS.</p>',
      '<p>This practice module presents workplace scenarios and three possible actions. For each scenario, choose the <b>most effective</b> and the <b>least effective</b> response.</p><p>Consider collaboration, integrity, work quality, client service, and risk management. The scenarios are original, and the results are practice guidance rather than an official UBS score.</p>'
    ),
    intro(
      '<p>Le parcours comporte <b>18 scénarios</b> et prend environ <b>20 minutes</b>. Il n’y a pas de limite de temps.</p><ul><li>Choisissez une action différente pour « la plus efficace » et « la moins efficace ».</li><li>Validez chaque scénario pour continuer ; vous ne pourrez pas revenir aux précédents.</li><li>Un scénario d’exemple vous permet d’essayer les deux sélections avant le test.</li><li>À la fin, consultez le score indicatif et le feedback détaillé dans « Feedback ».</li></ul>',
      '<p>The exercise contains <b>18 scenarios</b> and takes around <b>20 minutes</b>. There is no time limit.</p><ul><li>Select a different action for “most effective” and “least effective”.</li><li>Submit each scenario to continue; you cannot return to earlier scenarios.</li><li>A practice scenario lets you try both selections before the test.</li><li>At the end, review the indicative score and detailed feedback in “Feedback”.</li></ul>'
    )
  ];
  BANK.INTRO['ubs-ind'] = [
    intro(
      '<p>Ce test d’entraînement mesure la découverte de règles dans des grilles de symboles. Deux grilles d’exemple partagent une règle ; sélectionnez les <b>deux grilles</b> parmi quatre candidates qui respectent la même règle.</p><p>La règle concerne le nombre et la position des formes. Regardez d’abord les deux modèles, puis vérifiez chaque candidate avec la même hypothèse. Plusieurs exemples non notés précèdent le test chronométré.</p>',
      '<p>This practice test measures how quickly you can identify a rule in symbol grids. Two example grids share a rule; select the <b>two grids</b> from four candidates that follow the same rule.</p><p>The rule relates to the number and position of shapes. Study the examples first, then check each candidate against the same hypothesis. Unscored examples come before the timed test.</p>'
    ),
    intro(
      '<p>Veuillez noter :</p><ul><li>Le test dure <b>6 minutes</b>.</li><li>Chaque tâche demande exactement deux sélections parmi quatre candidates.</li><li>Utilisez « valider » pour soumettre ; une sélection vide compte comme une question passée.</li><li>Le chronomètre démarre à la première question et le test ne peut pas être mis en pause.</li></ul>',
      '<p>Please note:</p><ul><li>The test lasts <b>6 minutes</b>.</li><li>Each task asks you to select exactly two of the four candidate grids.</li><li>Use “submit” to answer; an empty selection counts as a skipped question.</li><li>The timer starts with the first question and the test cannot be paused.</li></ul>'
    )
  ];
})();
