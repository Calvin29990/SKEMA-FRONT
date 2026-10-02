/* ═══════════════════════════════════════════════════════════════
   drills.js — Générateurs déterministes + corpus visuels
   ▸ Banques LIMITÉES (contenu figé, seed fixe) :
       numerical (48 items figés), inductif, concentration,
       learning efficiency, switch challenge, mémoire de travail
   ▸ Banque ILLIMITÉE : verbal anglais (conjecture à l'infini,
       même style, mêmes règles de logique V/F/CS)
   ═══════════════════════════════════════════════════════════════ */
'use strict';

const DRILL = (() => {

  /* ─────────── Formatage numérique FR ─────────── */
  const nf = (n, d = 0) => {
    const s = Math.abs(n).toFixed(d).replace('.', ',');
    const [i, f] = s.split(',');
    const t = i.replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    return (n < 0 ? '−' : '') + t + (f ? ',' + f : '');
  };
  const money = (n, d = 0) => nf(n, d) + ' €';
  const pctS = (n, d = 1) => nf(n, d) + ' %';

  /** Construit une liste de 4 options dont 1 correcte, mélangées de façon déterministe. */
  function buildOpts(seed, correct, distractors, fmt = nf) {
    const seen = new Set([fmt(correct)]);
    const ds = [];
    for (const d of distractors) {
      const k = fmt(d);
      if (!seen.has(k) && isFinite(d)) { seen.add(k); ds.push(d); }
      if (ds.length === 3) break;
    }
    let guard = 1;
    while (ds.length < 3) { ds.push(correct * (1 + 0.13 * guard)); guard++; }
    const r = U.rng(seed);
    const all = [{ v: fmt(correct), ok: true }, ...ds.map(d => ({ v: fmt(d), ok: false }))];
    const sh = U.shuffle(r, all);
    return { options: sh.map(o => o.v), ans: sh.findIndex(o => o.ok) };
  }

  /* ══════════════════════════════════════════════════════════════
     A. NUMERICAL — 48 items figés (Paper A) / 37 (Paper B)
     Chaque item est calculé depuis sa table : la clé est exacte.
     ══════════════════════════════════════════════════════════════ */
  const NUM_SCEN = [
    { id: 'N1', title: 'Ventes par région', unit: 'k€',
      cols: ['Région', '2024', '2025', 'Marge nette'],
      rows: [['Nord', 4820, 5310, '12 %'], ['Sud', 3960, 3710, '9,5 %'], ['Est', 2410, 2980, '14 %'], ['Ouest', 3180, 3450, '11 %']],
      vals: [[4820, 5310], [3960, 3710], [2410, 2980], [3180, 3450]],
      margins: [12, 9.5, 14, 11],
      qs: [
        { t: (d) => `Quelle est la variation en pourcentage des ventes de la région ${d.nom} entre 2024 et 2025 ?`, f: (d) => (d.b - d.a) / d.a * 100, fmt: pctS, dist: (d, v) => [v * 0.9, v * 1.1, (d.b - d.a) / d.b * 100] },
        { t: () => `Quelle est la part de la région Nord dans les ventes totales 2025 ?`, f: (d) => 5310 / d.tot25 * 100, fmt: pctS, dist: (d, v) => [v * 1.15, v * 0.85, 100 - v] },
        { t: () => `Quel est le total des ventes 2025 des quatre régions ?`, f: (d) => d.tot25, fmt: (x) => nf(x) + ' k€', dist: (d, v) => [d.tot24, v * 1.04, v * 0.96] },
        { t: () => `Quelle région a la marge nette la plus élevée en 2025 ?`, f: () => 'Est', fmt: (x) => x, dist: () => ['Nord', 'Sud', 'Ouest'] },
        { t: (d) => `Quel est le montant de la marge nette 2025 de la région ${d.nom} ?`, f: (d) => d.b * d.mi / 100, fmt: (x) => nf(x) + ' k€', dist: (d, v) => [v * 1.1, v * 0.9, d.b] },
        { t: () => `En supposant une croissance de 5 % en 2026 par rapport à 2025, quel serait le total 2026 ?`, f: (d) => d.tot25 * 1.05, fmt: (x) => nf(x) + ' k€', dist: (d, v) => [v * 1.05, v * 0.95, d.tot25 + 500] }
      ]
    },
    { id: 'N2', title: 'Effectifs et masse salariale', unit: 'k€',
      cols: ['Service', 'Effectif', 'Salaire moyen', 'Ancienneté moy.'],
      rows: [['Front office', 42, 88000, '4,2 ans'], ['Middle office', 31, 54000, '6,1 ans'], ['IT', 24, 71000, '3,4 ans'], ['Support', 18, 43000, '7,8 ans']],
      vals: [[42, 88000], [31, 54000], [24, 71000], [18, 43000]],
      qs: [
        { t: () => `Quelle est la masse salariale annuelle totale ?`, f: (d) => d.sum, fmt: (x) => nf(x) + ' €', dist: (d, v) => [v * 1.08, v * 0.92, d.sum / 2] },
        { t: () => `Quel service représente la part la plus élevée de la masse salariale ?`, f: () => 'Front office', fmt: (x) => x, dist: () => ['Middle office', 'IT', 'Support'] },
        { t: () => `Quel est le salaire moyen de l’ensemble du personnel (pondéré) ?`, f: (d) => d.sum / d.head, fmt: (x) => nf(x) + ' €', dist: (d, v) => [v * 1.07, v * 0.93, (88000 + 43000) / 2] },
        { t: () => `Combien de personnes comptent le front office et le middle office réunis ?`, f: () => 73, fmt: (x) => x + ' personnes', dist: () => [62, 66, 85] },
        { t: () => `De combien le salaire moyen du front office dépasse-t-il celui du support ?`, f: (d) => 88000 - 43000, fmt: (x) => nf(x) + ' €', dist: (d, v) => [v * 1.2, v * 0.82, 43000] },
        { t: () => `Si l’effectif IT augmente de 25 % et que le salaire moyen reste identique, quelle sera la nouvelle masse salariale IT ?`, f: (d) => 24 * 71000 * 1.25, fmt: (x) => nf(x) + ' €', dist: (d, v) => [v / 1.25, v * 1.1, 24 * 71000] }
      ]
    },
    { id: 'N3', title: 'Cours et volumes', unit: '€',
      cols: ['Titre', 'Cours J-1', 'Cours J', 'Volume'],
      rows: [['ALPHA', 142.5, 148.2, 1250000], ['BETA', 88.4, 85.1, 830000], ['GAMMA', 231.0, 244.9, 410000], ['DELTA', 56.7, 58.9, 2100000]],
      vals: [[142.5, 148.2, 1250000], [88.4, 85.1, 830000], [231.0, 244.9, 410000], [56.7, 58.9, 2100000]],
      qs: [
        { t: (d) => `Quelle est la variation en % du titre ${d.nom} entre J-1 et J ?`, f: (d) => (d.b - d.a) / d.a * 100, fmt: pctS, dist: (d, v) => [v * 0.9, v * 1.1, (d.b - d.a) / d.b * 100] },
        { t: () => `Quel est le montant total échangé sur ALPHA (cours J × volume) ?`, f: (d) => d.pick('ALPHA')[1] * d.pick('ALPHA')[2], fmt: (x) => nf(x) + ' €', dist: (d, v) => [v * 1.05, v * 0.95, v / 2] },
        { t: () => `Quel titre enregistre la plus forte hausse relative ?`, f: () => 'GAMMA', fmt: (x) => x, dist: () => ['ALPHA', 'DELTA', 'BETA'] },
        { t: () => `Quelle est la capitalisation implicite si DELTA compte 42 000 000 de titres ?`, f: (d) => d.pick('DELTA')[1] * 42000000, fmt: (x) => nf(x) + ' €', dist: (d, v) => [v * 1.1, v * 0.9, d.pick('DELTA')[1] * 2100000] },
        { t: () => `Quel est le volume total échangé sur les quatre titres ?`, f: (d) => d.sumVol, fmt: (x) => nf(x), dist: (d, v) => [v * 1.1, v * 0.9, v / 4] },
        { t: () => `Si GAMMA réalise la même variation relative qu’aujourd’hui lors de la séance suivante, quel sera son cours ?`, f: (d) => { const g = d.pick('GAMMA'); return g[2] * (g[2] / g[1]); }, fmt: (x) => nf(x, 2) + ' €', dist: (d, v) => [v * 1.02, v * 0.98, d.pick('GAMMA')[2]] }
      ]
    },
    { id: 'N4', title: 'Budget marketing par canal', unit: 'k€',
      cols: ['Canal', 'Budget', 'Coût par contact', 'Contacts'],
      rows: [['Digital', 240, 1.2, 200000], ['Presse', 180, 4.5, 40000], ['Événementiel', 320, 26.0, 12300], ['Sponsoring', 150, 9.0, 16666]],
      vals: [[240, 1.2, 200000], [180, 4.5, 40000], [320, 26.0, 12300], [150, 9.0, 16666]],
      qs: [
        { t: () => `Quel est le budget marketing total ?`, f: (d) => d.sum, fmt: (x) => nf(x) + ' k€', dist: (d, v) => [v * 1.08, v * 0.92, v * 0.5] },
        { t: () => `Quel canal génère le plus grand nombre de contacts ?`, f: () => 'Digital', fmt: (x) => x, dist: () => ['Presse', 'Événementiel', 'Sponsoring'] },
        { t: () => `Quel est le coût total des contacts du canal Événementiel ?`, f: (d) => 12300 * 26, fmt: (x) => nf(x) + ' €', dist: (d, v) => [320, v * 1.1, v * 0.9] },
        { t: () => `Quelle part du budget représente le Digital ?`, f: (d) => 240 / d.sum * 100, fmt: pctS, dist: (d, v) => [v * 1.2, v * 0.8, 100 - v] },
        { t: () => `Quel est le coût moyen par contact tous canaux confondus ?`, f: (d) => d.sum * 1000 / d.totContacts, fmt: (x) => nf(x, 2) + ' €', dist: (d, v) => [v * 1.15, v * 0.85, v * 2] },
        { t: () => `Si l’on transfère 40 k€ du budget Presse vers le Digital, quel est le nouveau budget Presse ?`, f: () => 140, fmt: (x) => nf(x) + ' k€', dist: () => [180, 200, 100] }
      ]
    },
    { id: 'N5', title: 'Production et coûts', unit: 'unités',
      cols: ['Atelier', 'Production', 'Coût unitaire', 'Défauts'],
      rows: [['Lyon', 12500, 42, '1,8 %'], ['Lille', 9800, 39, '2,4 %'], ['Nantes', 7400, 47, '1,1 %'], ['Metz', 6100, 44, '3,2 %']],
      vals: [[12500, 42], [9800, 39], [7400, 47], [6100, 44]],
      qs: [
        { t: () => `Quel est le coût de production total de l’atelier Lyon ?`, f: () => 12500 * 42, fmt: (x) => nf(x) + ' €', dist: (d, v) => [v * 1.1, v * 0.9, 12500 + 42] },
        { t: () => `Quel atelier a le coût unitaire le plus bas ?`, f: () => 'Lille', fmt: (x) => x, dist: () => ['Lyon', 'Nantes', 'Metz'] },
        { t: () => `Quelle est la production totale des quatre ateliers ?`, f: () => 35800, fmt: (x) => nf(x) + ' u.', dist: () => [32000, 38400, 34100] },
        { t: () => `Combien d’unités défectueuses produit l’atelier Metz ?`, f: () => Math.round(6100 * 0.032), fmt: (x) => nf(x) + ' u.', dist: (d, v) => [Math.round(v * 1.15), Math.round(v * 0.85), 6100] },
        { t: () => `Quel est le coût de production total de l’ensemble des ateliers ?`, f: () => 12500 * 42 + 9800 * 39 + 7400 * 47 + 6100 * 44, fmt: (x) => nf(x) + ' €', dist: (d, v) => [v * 1.05, v * 0.95, v / 4] },
        { t: () => `Si Nantes réduit son coût unitaire de 10 %, quel sera son nouveau coût ?`, f: () => 47 * 0.9, fmt: (x) => nf(x, 1) + ' €', dist: () => [47, 42, 40.5] }
      ]
    },
    { id: 'N6', title: 'Portefeuille clients', unit: 'clients',
      cols: ['Segment', 'Clients 2025', 'Revenu moyen', 'Taux de rétention'],
      rows: [['Grands comptes', 42, 850000, '97 %'], ['PME', 310, 62000, '88 %'], ['Institutionnels', 28, 1400000, '95 %'], ['Particuliers', 4200, 1250, '76 %']],
      vals: [[42, 850000], [310, 62000], [28, 1400000], [4200, 1250]],
      qs: [
        { t: () => `Quel segment génère le revenu total le plus élevé ?`, f: (d) => d.best, fmt: (x) => x, dist: () => ['Grands comptes', 'PME', 'Particuliers'] },
        { t: () => `Quel est le revenu total des institutionnels ?`, f: () => 28 * 1400000, fmt: (x) => nf(x) + ' €', dist: (d, v) => [v * 1.1, v * 0.9, 1400000] },
        { t: () => `Combien de clients PME seront conservés l’an prochain au vu du taux de rétention ?`, f: () => Math.round(310 * 0.88), fmt: (x) => nf(x) + ' clients', dist: (d, v) => [Math.round(v * 1.1), Math.round(v * 0.9), 310] },
        { t: (d) => `Quel est le revenu moyen par client tous segments confondus ?`, f: (d) => d.sum / d.head, fmt: (x) => nf(x) + ' €', dist: (d, v) => [v * 1.2, v * 0.8, v / 3] },
        { t: () => `Quel est le revenu total du portefeuille ?`, f: (d) => d.sum, fmt: (x) => nf(x) + ' €', dist: (d, v) => [v * 1.04, v * 0.96, v * 2] },
        { t: () => `Quel segment a le taux de rétention le plus faible ?`, f: () => 'Particuliers', fmt: (x) => x, dist: () => ['PME', 'Grands comptes', 'Institutionnels'] }
      ]
    },
    { id: 'N7', title: 'Délais de livraison', unit: 'jours',
      cols: ['Transporteur', 'Colis', 'Délai moyen', 'Retards'],
      rows: [['Axa-Log', 18400, 2.1, '3,1 %'], ['Bekka', 12300, 3.4, '5,2 %'], ['Corio', 9100, 1.8, '1,4 %'], ['Delta-Trans', 6800, 4.2, '7,9 %']],
      vals: [[18400, 2.1], [12300, 3.4], [9100, 1.8], [6800, 4.2]],
      qs: [
        { t: () => `Quel transporteur livrait le plus de colis ?`, f: () => 'Axa-Log', fmt: (x) => x, dist: () => ['Bekka', 'Corio', 'Delta-Trans'] },
        { t: () => `Combien de colis ont été livrés en retard par Delta-Trans ?`, f: () => Math.round(6800 * 0.079), fmt: (x) => nf(x) + ' colis', dist: (d, v) => [Math.round(v * 1.12), Math.round(v * 0.88), 6800] },
        { t: () => `Quel est le nombre total de colis traités ?`, f: () => 46600, fmt: (x) => nf(x) + ' colis', dist: () => [44000, 49000, 42000] },
        { t: () => `Quel est le délai moyen pondéré par le nombre de colis ?`, f: (d) => d.wavg, fmt: (x) => nf(x, 2) + ' j', dist: (d, v) => [v * 1.1, v * 0.9, 2.88] },
        { t: () => `Combien de colis ne sont pas en retard chez Corio ?`, f: () => 9100 - Math.round(9100 * 0.014), fmt: (x) => nf(x) + ' colis', dist: (d, v) => [v * 1.05, 9100, Math.round(9100 * 0.014)] },
        { t: () => `Si Bekka ramène son taux de retard à 2 %, combien de retards en moins ?`, f: () => Math.round(12300 * (0.052 - 0.02)), fmt: (x) => nf(x) + ' colis', dist: (d, v) => [Math.round(v * 1.4), Math.round(v * 0.6), Math.round(12300 * 0.052)] }
      ]
    },
    { id: 'N8', title: 'Coûts énergétiques par site', unit: 'MWh',
      cols: ['Site', 'Consommation', 'Prix MWh', 'Objectif réduction'],
      rows: [['Rouen', 2400, 78, '12 %'], ['Toulouse', 3100, 74, '8 %'], ['Lyon', 1900, 81, '15 %'], ['Lille', 2700, 69, '10 %']],
      vals: [[2400, 78], [3100, 74], [1900, 81], [2700, 69]],
      qs: [
        { t: () => `Quel site a la facture énergétique la plus élevée ?`, f: () => 'Toulouse', fmt: (x) => x, dist: () => ['Rouen', 'Lyon', 'Lille'] },
        { t: () => `Quelle est la facture d’énergie du site Lyon ?`, f: () => 1900 * 81, fmt: (x) => nf(x) + ' €', dist: (d, v) => [v * 1.1, v * 0.9, 1900 + 81] },
        { t: () => `Quelle est la consommation totale des quatre sites ?`, f: () => 10100, fmt: (x) => nf(x) + ' MWh', dist: () => [9500, 10500, 10100 / 2] },
        { t: () => `Quel est le prix moyen du MWh toutes usines confondues ?`, f: (d) => d.wprice, fmt: (x) => nf(x, 2) + ' €', dist: (d, v) => [v * 1.05, v * 0.95, 75.5] },
        { t: () => `Si Rouen atteint son objectif de réduction, quelle sera sa consommation ?`, f: () => 2400 * 0.88, fmt: (x) => nf(x) + ' MWh', dist: (d, v) => [v * 1.06, v * 0.94, 2400 * 0.12] },
        { t: () => `Quel est le montant total des factures énergétiques des quatre sites ?`, f: (d) => d.sum, fmt: (x) => nf(x) + ' €', dist: (d, v) => [v * 1.05, v * 0.95, v / 4] }
      ]
    }
  ];

  /** Construit les 48 items figés du numerical (ordre stable, seed fixe). */
  function numericalFixed() {
    const items = [];
    NUM_SCEN.forEach((sc, si) => {
      /* données dérivées */
      const d = {
        margins: sc.margins || [], bestM: 0, tot24: 0, tot25: 0, sum: 0, head: 0,
        sumVol: 0, totContacts: 0, wavg: 0, wprice: 0, best: '',
        nom: '', a: 0, b: 0, mi: 0,
        pick(name) { return sc.rows.find(r => r[0] === name); }
      };
      if (sc.id === 'N1') {
        d.tot24 = sc.vals.reduce((a, v) => a + v[0], 0);
        d.tot25 = sc.vals.reduce((a, v) => a + v[1], 0);
        d.bestM = 14;
        d.margins.forEach((m, i) => { if (m > d.bestM) d.bestM = m; });
      }
      if (sc.id === 'N2') { d.sum = sc.vals.reduce((a, v) => a + v[0] * v[1], 0); d.head = sc.vals.reduce((a, v) => a + v[0], 0); }
      if (sc.id === 'N3') { d.sumVol = sc.vals.reduce((a, v) => a + v[2], 0); }
      if (sc.id === 'N4') { d.sum = sc.vals.reduce((a, v) => a + v[0], 0); d.totContacts = sc.vals.reduce((a, v) => a + v[2], 0); }
      if (sc.id === 'N5') { d.sum = sc.vals.reduce((a, v) => a + v[0] * v[1], 0); }
      if (sc.id === 'N6') {
        const revs = sc.vals.map(v => v[0] * v[1]);
        d.sum = revs.reduce((a, b) => a + b, 0);
        d.head = sc.vals.reduce((a, v) => a + v[0], 0);
        d.best = sc.rows[revs.indexOf(Math.max(...revs))][0];
      }
      if (sc.id === 'N7') {
        const tot = sc.vals.reduce((a, v) => a + v[0], 0);
        d.wavg = sc.vals.reduce((a, v) => a + v[0] * v[1], 0) / tot;
      }
      if (sc.id === 'N8') {
        d.sum = sc.vals.reduce((a, v) => a + v[0] * v[1], 0);
        d.wprice = d.sum / sc.vals.reduce((a, v) => a + v[0], 0);
      }
      sc.qs.forEach((q, qi) => {
        const row = sc.rows[qi % sc.rows.length];
        const dd = Object.assign({}, d, { nom: row[0], a: row[1], b: row[2], mi: sc.margins ? sc.margins[qi % sc.rows.length] : 0 });
        const correct = q.f(dd);
        const seed = U.hash(sc.id + '#' + qi);
        /* distracteurs spécifiques si fournis, sinon dérivés */
        let opt;
        if (typeof correct === 'string') {
          opt = { options: U.shuffle(U.rng(seed), [correct, ...q.dist(dd, correct)]), ans: 0 };
          opt.ans = opt.options.indexOf(correct);
        } else {
          const ds = q.dist(dd, correct) || [];
          opt = buildOpts(seed, correct, ds, q.fmt || nf);
        }
        items.push({
          id: sc.id + '.' + (qi + 1), sec: 'numerical',
          scenario: sc.title, unit: sc.unit, cols: sc.cols, rows: sc.rows,
          q: q.t(dd), options: opt.options, ans: opt.ans,
          why: 'Calcul direct sur le tableau « ' + sc.title + ' ».',
          time: 75
        });
      });
    });
    return items;   /* 8 scénarios × 6 = 48 items */
  }

  /* ══════════════════════════════════════════════════════════════
     B. VERBAL ANGLAIS — banque ILLIMITÉE (conjecture d'une suite)
     Moteur : scénarios + faits → 3 affirmations dont les réponses
     sont dérivables du texte (T/F/CS), jamais ambiguës.
     ══════════════════════════════════════════════════════════════ */
  /* Chaque blueprint produit un passage UNIQUE : les valeurs (%, montants,
     compteurs, périodes) sont tirées au sort, donc la batterie est infinie.
     Invariant garanti : 1 affirmation VRAIE, 1 FAUSSE, 1 IMPOSSIBLE À DIRE. */
  function VGEN(r) {
    const p1 = U.int(r, 6, 28), p2 = p1 + U.int(r, 2, 14);
    const m1 = U.int(r, 12, 90) * 10, m2 = m1 + U.int(r, 3, 40) * 5;
    const n1 = U.int(r, 3, 48), n2 = n1 + U.int(r, 1, 22);
    const d1 = (U.int(r, 22, 48) / 10), d2 = (U.int(r, 8, 21) / 10);
    return {
      p1, p2, p3: U.int(r, 3, 22), p0: U.int(r, 1, 12),
      m1, m2, n1, n2, d1: d1.toFixed(1).replace('.', ','), d2: d2.toFixed(1).replace('.', ','),
      period: U.pick(r, ['the fourth quarter', 'the first half of the year', 'the past twelve months',
        'the current financial year', 'the second quarter', 'the last fiscal year']),
      month: U.pick(r, ['January', 'March', 'June', 'September', 'November']),
      city: U.pick(r, ['Lyon', 'Rotterdam', 'Milan', 'Hamburg', 'Leeds', 'Valencia', 'Antwerp']),
      ratio: U.pick(r, ['two to one', 'three to one', 'four to one', 'five to one'])
    };
  }

  const VB_BLUEPRINTS = [
    { name: 'asset-management',
      build: (V) => ({
        passage: 'Northgate Asset Management increased the share of its portfolios held in short-dated government bonds from ' + V.p1 + '% to ' + V.p2 + '% during ' + V.period + '. The investment committee explained that it expected policy rate cuts to be delayed. Northgate also confirmed that the change had been approved by its risk committee before implementation.',
        S: [
          { t: 'The share of portfolios held in short-dated government bonds reached ' + V.p2 + '%.', a: 'true', w: 'Le passage donne explicitement ce niveau final.' },
          { t: 'The investment committee expected policy rate cuts to be delayed.', a: 'true', w: 'Cause explicitement indiquée.' },
          { t: 'Northgate cut its allocation to short-dated government bonds.', a: 'false', w: 'Le passage décrit une augmentation, pas une réduction.' },
          { t: 'The risk committee approved the change after it was implemented.', a: 'false', w: 'Le texte dit « before implementation ».' },
          { t: 'Northgate is the largest asset manager in its domestic market.', a: 'cannot say', w: 'Aucune comparaison de taille dans le passage.' },
          { t: 'The change was motivated by client redemptions.', a: 'cannot say', w: 'Aucune mention de rachats de clients.' }
        ]
      })
    },
    { name: 'logistics',
      build: (V) => ({
        passage: 'Halden Logistics reduced the average delivery time on its northern routes from ' + V.d1 + ' days to ' + V.d2 + ' days over ' + V.period + '. The company attributed the improvement to routing software introduced at its ' + V.city + ' hub. Halden stated that the measure had no effect on the number of delivery vehicles it operates.',
        S: [
          { t: 'The average delivery time on northern routes fell to ' + V.d2 + ' days.', a: 'true', w: 'Valeur finale donnée explicitement.' },
          { t: 'The improvement was attributed to routing software.', a: 'true', w: 'Cause donnée par l’entreprise.' },
          { t: 'Halden reduced the number of delivery vehicles it operates.', a: 'false', w: 'Le texte dit explicitement le contraire.' },
          { t: 'The average delivery time increased on northern routes.', a: 'false', w: 'Une réduction est décrite.' },
          { t: 'Halden operates the largest fleet of vehicles in its market.', a: 'cannot say', w: 'Aucune donnée comparative.' },
          { t: 'The new software cost more than the previous system.', a: 'cannot say', w: 'Aucun coût mentionné.' }
        ]
      })
    },
    { name: 'pharma',
      build: (V) => ({
        passage: 'Cordell Pharmaceuticals raised its research budget by ' + V.p3 + '% for ' + V.period + ', after expanding two late-stage clinical trials. The company confirmed that the additional spending would be funded from existing cash resources and that no external financing was required.',
        S: [
          { t: 'The research budget was increased by ' + V.p3 + '%.', a: 'true', w: 'Chiffre donné explicitement.' },
          { t: 'Two late-stage trials were expanded.', a: 'true', w: 'Explicitement indiqué.' },
          { t: 'The company borrowed to fund the additional research spending.', a: 'false', w: 'Le texte exclut tout financement externe.' },
          { t: 'Cordell cancelled one of its late-stage trials.', a: 'false', w: 'Les essais ont été élargis, pas annulés.' },
          { t: 'The company’s competitors also increased their research budgets.', a: 'cannot say', w: 'Aucune mention des concurrents.' },
          { t: 'The trials are expected to produce positive results.', a: 'cannot say', w: 'Aucun résultat n’est évoqué.' }
        ]
      })
    },
    { name: 'industry',
      build: (V) => ({
        passage: 'Vermont Steel closed one of its blast furnaces at its ' + V.city + ' site, reducing total output by about ' + V.p3 + '%. Management explained that energy costs had remained above budget for three consecutive quarters. The company said the closure was temporary and that the site’s workforce would be retained.',
        S: [
          { t: 'Total output fell by roughly ' + V.p3 + '%.', a: 'true', w: 'Le passage donne cette ampleur.' },
          { t: 'Energy costs were above budget for three consecutive quarters.', a: 'true', w: 'Explicitement indiqué.' },
          { t: 'The company dismissed the workforce at the site.', a: 'false', w: 'Le texte indique que les effectifs sont conservés.' },
          { t: 'The closure is permanent.', a: 'false', w: 'Le passage qualifie la fermeture de temporaire.' },
          { t: 'Vermont Steel is the largest producer in the region.', a: 'cannot say', w: 'Aucune comparaison.' },
          { t: 'Energy costs are expected to fall next quarter.', a: 'cannot say', w: 'Aucune prévision énergétique donnée.' }
        ]
      })
    },
    { name: 'retail',
      build: (V) => ({
        passage: 'Lakeside Retail Group opened ' + V.n1 + ' new stores and reported like-for-like sales growth of ' + V.p3 + '% in ' + V.period + '. The group stated that the new stores had reached profitability earlier than planned and that no further openings were scheduled for the current quarter.',
        S: [
          { t: 'Like-for-like sales grew by ' + V.p3 + '%.', a: 'true', w: 'Chiffre explicite.' },
          { t: 'The new stores became profitable earlier than planned.', a: 'true', w: 'Explicitement indiqué.' },
          { t: 'Further store openings are planned for the current quarter.', a: 'false', w: 'Le groupe indique le contraire.' },
          { t: 'Like-for-like sales declined during the period.', a: 'false', w: 'Une croissance est mentionnée.' },
          { t: 'The new stores are located in city centres.', a: 'cannot say', w: 'Aucun emplacement n’est précisé.' },
          { t: 'Lakeside plans to open stores abroad.', a: 'cannot say', w: 'Aucune mention d’international.' }
        ]
      })
    },
    { name: 'insurance',
      build: (V) => ({
        passage: 'Aurelia Insurance tightened its underwriting standards for commercial property policies, which raised premiums written by ' + V.p3 + '% over ' + V.period + '. The insurer reported that claims frequency had increased in coastal regions and added that the new standards apply to new policies only.',
        S: [
          { t: 'Premiums written rose by ' + V.p3 + '%.', a: 'true', w: 'Chiffre explicite.' },
          { t: 'Claims frequency increased in coastal regions.', a: 'true', w: 'Explicitement indiqué.' },
          { t: 'The new standards apply to existing policies as well.', a: 'false', w: 'Le texte limite l’application aux nouvelles polices.' },
          { t: 'Aurelia loosened its underwriting standards.', a: 'false', w: 'Les standards ont été renforcés.' },
          { t: 'The insurer will exit the commercial property market.', a: 'cannot say', w: 'Aucune décision de retrait évoquée.' },
          { t: 'The premium increase was driven by higher interest rates.', a: 'cannot say', w: 'Aucune mention des taux.' }
        ]
      })
    },
    { name: 'energy',
      build: (V) => ({
        passage: 'Brightwell Energy signed a power purchase agreement covering ' + V.n1 + ' TWh per year for the next decade, at a price that is fixed for the first five years. The company said the agreement hedges part of its exposure to wholesale electricity prices and that the contracted volume represents about ' + V.p3 + '% of its output.',
        S: [
          { t: 'The agreement covers ' + V.n1 + ' TWh per year.', a: 'true', w: 'Volume explicitement indiqué.' },
          { t: 'The price is fixed for the first five years.', a: 'true', w: 'Explicitement indiqué.' },
          { t: 'The contract hedges the company’s entire exposure to wholesale prices.', a: 'false', w: 'Le texte parle d’une PART de l’exposition.' },
          { t: 'The agreement runs for three years.', a: 'false', w: 'La durée est d’une décennie.' },
          { t: 'The counterparty is a state-owned utility.', a: 'cannot say', w: 'L’identité de la contrepartie n’est pas donnée.' },
          { t: 'Electricity prices will rise over the contract period.', a: 'cannot say', w: 'Aucune prévision de prix.' }
        ]
      })
    },
    { name: 'banking',
      build: (V) => ({
        passage: 'Pellham Bank reduced its branch network from ' + V.n1 + ' to ' + V.n2 + ' branches over ' + V.period + '. The bank explained that customer transactions had migrated to digital channels and stated that no further closures were planned before the end of the financial year.',
        S: [
          { t: 'The branch network fell to ' + V.n2 + ' branches.', a: 'true', w: 'Valeur finale explicite.' },
          { t: 'Customer transactions migrated to digital channels.', a: 'true', w: 'Cause indiquée par la banque.' },
          { t: 'The bank opened new branches during the period.', a: 'false', w: 'Le réseau a été réduit.' },
          { t: 'More closures are planned before the year-end.', a: 'false', w: 'La banque indique le contraire.' },
          { t: 'The bank is the largest in its country by deposits.', a: 'cannot say', w: 'Aucune donnée de classement.' },
          { t: 'The closures resulted in redundancies.', a: 'cannot say', w: 'Aucune information sur l’emploi.' }
        ]
      })
    },
    { name: 'food',
      build: (V) => ({
        passage: 'Sundale Foods reformulated three of its best-selling products, cutting average sugar content by ' + V.p3 + '% over ' + V.period + '. The company said the reformulation followed new labelling rules and that consumer testing had been conducted before launch. It confirmed that prices were unchanged.',
        S: [
          { t: 'Average sugar content was cut by ' + V.p3 + '%.', a: 'true', w: 'Chiffre explicite.' },
          { t: 'The reformulation followed new labelling rules.', a: 'true', w: 'Explicitement indiqué.' },
          { t: 'Prices of the reformulated products were increased.', a: 'false', w: 'Le texte indique que les prix sont inchangés.' },
          { t: 'The company changed the packaging of its products.', a: 'cannot say', w: 'Aucune mention du conditionnement.' },
          { t: 'Consumer testing took place after the launch.', a: 'false', w: 'Le texte dit « before launch ».' },
          { t: 'The reformulated products will be exported.', a: 'cannot say', w: 'Aucune mention d’export.' }
        ]
      })
    },
    { name: 'capital',
      build: (V) => ({
        passage: 'Fairbrook Capital launched a secondaries strategy with a target size of ' + V.m1 + ' million euros, to be invested over three years. The firm stated that the strategy had been created because limited partners needed liquidity, and that it had already received commitments from existing investors.',
        S: [
          { t: 'The target size of the strategy is ' + V.m1 + ' million euros.', a: 'true', w: 'Montant explicite.' },
          { t: 'Limited partners needed liquidity.', a: 'true', w: 'Motif donné par la société.' },
          { t: 'The strategy will be invested over five years.', a: 'false', w: 'La durée indiquée est de trois ans.' },
          { t: 'The strategy had not yet attracted any commitment.', a: 'false', w: 'Des engagements ont déjà été reçus.' },
          { t: 'The strategy will focus on infrastructure assets.', a: 'cannot say', w: 'Aucune classe d’actifs précisée.' },
          { t: 'Fairbrook will raise a larger fund next year.', a: 'cannot say', w: 'Aucune annonce de levée future.' }
        ]
      })
    },
    { name: 'airports',
      build: (V) => ({
        passage: 'Trentvale Airports will increase passenger charges by ' + V.p3 + '% over the next regulatory period, after the regulator authorised additional investment in terminal capacity. The operator stated that the investment programme would be reviewed annually and that charges for transfer passengers would remain unchanged.',
        S: [
          { t: 'Passenger charges will rise by ' + V.p3 + '%.', a: 'true', w: 'Chiffre explicite.' },
          { t: 'The regulator authorised additional investment in terminal capacity.', a: 'true', w: 'Explicitement indiqué.' },
          { t: 'Transfer passenger charges will increase as well.', a: 'false', w: 'Le texte les dit inchangés.' },
          { t: 'The investment programme will be reviewed every five years.', a: 'false', w: 'Revue annuelle indiquée.' },
          { t: 'Passenger numbers are expected to grow next year.', a: 'cannot say', w: 'Aucune prévision de trafic.' },
          { t: 'The airport will build a new runway.', a: 'cannot say', w: 'Aucune mention de piste.' }
        ]
      })
    },
    { name: 'media',
      build: (V) => ({
        passage: 'Osprey Media merged two of its newsrooms, reducing editorial headcount by ' + V.n1 + ' positions in ' + V.period + '. The group said the decision followed a continued decline in advertising revenue and that subscription revenue had grown over the same period.',
        S: [
          { t: 'Editorial headcount was reduced by ' + V.n1 + ' positions.', a: 'true', w: 'Chiffre explicite.' },
          { t: 'Advertising revenue continued to decline.', a: 'true', w: 'Motif donné par le groupe.' },
          { t: 'Subscription revenue declined over the same period.', a: 'false', w: 'La croissance des abonnements est indiquée.' },
          { t: 'The two newsrooms were merged.', a: 'true', w: 'Explicitement indiqué.' },
          { t: 'The group plans to launch a new print title.', a: 'cannot say', w: 'Aucune annonce de lancement.' },
          { t: 'The journalism union opposed the merger.', a: 'cannot say', w: 'Aucune mention des syndicats.' }
        ]
      })
    },
    { name: 'utilities',
      build: (V) => ({
        passage: 'Grantham Utilities deferred part of its capital expenditure programme, postponing about ' + V.m1 + ' million euros of spending to ' + V.period + '. The utility explained that supply chain constraints had delayed equipment delivery, and confirmed that the deferral would not affect its service obligations.',
        S: [
          { t: 'About ' + V.m1 + ' million euros of spending has been postponed.', a: 'true', w: 'Montant explicite.' },
          { t: 'Supply chain constraints delayed equipment delivery.', a: 'true', w: 'Explication donnée par l’opérateur.' },
          { t: 'The deferral will affect the utility’s service obligations.', a: 'false', w: 'Le texte dit explicitement le contraire.' },
          { t: 'The capital expenditure programme was cancelled.', a: 'false', w: 'Il a été reporté, non annulé.' },
          { t: 'The delayed equipment comes from a single supplier.', a: 'cannot say', w: 'Aucun fournisseur identifié.' },
          { t: 'The programme will be reviewed by the regulator.', a: 'cannot say', w: 'Aucune revue réglementaire mentionnée.' }
        ]
      })
    },
    { name: 'investment-bank',
      build: (V) => ({
        passage: 'Kestrel Securities reported that equities revenue grew by ' + V.p3 + '% while fixed income revenue fell by ' + V.p1 + '% over ' + V.period + '. The bank said the shift reflected lower volatility in rates and higher client activity in cash equities, and added that headcount in fixed income was unchanged.',
        S: [
          { t: 'Equities revenue grew by ' + V.p3 + '%.', a: 'true', w: 'Chiffre explicite.' },
          { t: 'Fixed income revenue declined.', a: 'true', w: 'Baisse indiquée dans le passage.' },
          { t: 'Headcount in fixed income was reduced.', a: 'false', w: 'Le texte le dit inchangé.' },
          { t: 'Lower volatility in rates contributed to the shift.', a: 'true', w: 'Explication de la banque.' },
          { t: 'The bank plans to hire more equities traders.', a: 'cannot say', w: 'Aucun plan de recrutement évoqué.' },
          { t: 'Kestrel gained market share from competitors.', a: 'cannot say', w: 'Aucune donnée de part de marché.' }
        ]
      })
    },
    { name: 'real-estate',
      build: (V) => ({
        passage: 'Ashcombe REIT reported that occupancy across its portfolio rose to ' + V.p2 + '% and that rents on renewed leases increased by ' + V.p3 + '%. The REIT stated that it had sold ' + V.n1 + ' properties during ' + V.period + ' and that no acquisitions were under negotiation.',
        S: [
          { t: 'Portfolio occupancy rose to ' + V.p2 + '%.', a: 'true', w: 'Valeur explicite.' },
          { t: 'Rents on renewed leases increased by ' + V.p3 + '%.', a: 'true', w: 'Chiffre explicite.' },
          { t: 'The REIT acquired ' + V.n1 + ' properties during the period.', a: 'false', w: 'Il s’agit de cessions, pas d’acquisitions.' },
          { t: 'Acquisitions are currently under negotiation.', a: 'false', w: 'Le texte l’exclut.' },
          { t: 'Occupancy fell across the portfolio.', a: 'false', w: 'Une hausse est indiquée.' },
          { t: 'The REIT will pay a higher dividend.', a: 'cannot say', w: 'Aucune information sur le dividende.' }
        ]
      })
    },
    { name: 'market-infrastructure',
      build: (V) => ({
        passage: 'A trading venue will migrate to a new data centre over a weekend, reducing latency by approximately ' + V.p3 + '%. Members will have to certify their connectivity before the migration, and the venue confirmed that fees would remain unchanged for at least twelve months.',
        S: [
          { t: 'Latency will be reduced by approximately ' + V.p3 + '%.', a: 'true', w: 'Chiffre explicite.' },
          { t: 'Members must certify their connectivity before the migration.', a: 'true', w: 'Explicitement indiqué.' },
          { t: 'Fees will be raised after the migration.', a: 'false', w: 'Les frais restent inchangés pendant au moins douze mois.' },
          { t: 'The migration will take place during a trading day.', a: 'false', w: 'Elle aura lieu un week-end.' },
          { t: 'The data centre is located in the same city as the previous one.', a: 'cannot say', w: 'Aucune localisation précisée.' },
          { t: 'Other venues will follow the same approach.', a: 'cannot say', w: 'Aucune mention des autres plateformes.' }
        ]
      })
    }
  ];

  /** Génère un item verbal (passage + 3 affirmations V/F/CS) + justification. */
  function verbalItem(seed) {
    const r = U.rng(seed);
    const V = VGEN(r);
    const bp = U.pick(r, VB_BLUEPRINTS);
    const built = bp.build(V);
    const all = built.S;
    const trues = all.filter(x => x.a === 'true');
    const falses = all.filter(x => x.a === 'false');
    const css = all.filter(x => x.a === 'cannot say');
    const chosen = [];
    if (trues.length) chosen.push(U.pick(r, trues));
    if (falses.length) chosen.push(U.pick(r, falses));
    if (css.length) chosen.push(U.pick(r, css));
    while (chosen.length < 3) chosen.push(U.pick(r, all));
    const q = U.shuffle(r, chosen);
    return {
      id: 'VI' + (seed % 100000).toString(36).toUpperCase(), sec: 'verbalX',
      passage: built.passage, q, theme: bp.name, seed
    };
  }

  /* ══════════════════════════════════════════════════════════════
     C. INDUCTIF — séries de figures (banque limitée, seed fixe)
     ══════════════════════════════════════════════════════════════ */
  const SHAPES = ['circle', 'square', 'tri-up', 'tri-down', 'diamond', 'cross', 'star', 'plus', 'disc', 'square-rot', 'chev-up', 'dot-ring'];
  const ROT_MAP = { 'circle': 'circle', 'square': 'square', 'tri-up': 'tri-right', 'tri-down': 'tri-left', 'diamond': 'diamond', 'cross': 'plus', 'star': 'star', 'plus': 'cross', 'disc': 'dot-ring', 'square-rot': 'square-half', 'chev-up': 'chev-down', 'dot-ring': 'disc' };

  function inductiveSet(n = 30) {
    const items = [];
    for (let i = 0; i < n; i++) {
      const r = U.rng(1000 + i * 7);
      const sh = U.pick(r, SHAPES);
      const col = U.pick(r, ['grn', 'amb', 'blu', 'pur', 'teal', 'red']);
      const ruleKind = i % 5;
      const series = [];
      let opts;
      if (ruleKind === 0) {           /* rotation de la forme */
        series.push(sh, ROT_MAP[sh], sh, ROT_MAP[sh], sh);
        opts = [ROT_MAP[sh], sh, U.pick(r, SHAPES)].filter((v, idx, a) => a.indexOf(v) === idx);
        while (opts.length < 3) opts.push(U.pick(r, SHAPES));
        opts = U.shuffle(r, opts.slice(0, 3));
      } else if (ruleKind === 1) {    /* nombre croissant de points */
        series.push('dot-1', 'dot-2', 'dot-3', 'dot-1', 'dot-2');
        opts = ['dot-3', 'dot-1', 'dot-ring'];
        opts = U.shuffle(U.rng(1000 + i * 13), opts);
      } else if (ruleKind === 2) {    /* alternance plein / vide */
        series.push('disc', 'circle', 'disc', 'circle', 'disc');
        opts = U.shuffle(U.rng(1000 + i * 17), ['circle', 'disc', 'square-full']);
      } else if (ruleKind === 3) {    /* taille/motif croissant */
        series.push('chev-up', 'chev-up', 'plus', 'chev-up', 'chev-up');
        opts = U.shuffle(U.rng(1000 + i * 19), ['plus', 'cross', 'chev-down']);
      } else {                        /* figure tournante */
        series.push('tri-up', 'tri-right', 'tri-down', 'tri-left', 'tri-up');
        opts = U.shuffle(U.rng(1000 + i * 23), ['tri-right', 'tri-down', 'tri-left']);
      }
      let correct = { 0: ROT_MAP[sh], 1: 'dot-3', 2: 'circle', 3: 'plus', 4: 'tri-right' }[ruleKind];
      if (ruleKind === 2) correct = series[4] === 'disc' ? 'circle' : 'disc';
      items.push({
        id: 'IND' + (i + 1), sec: 'inductive', series, opts, color: col, ans: opts.indexOf(correct),
        why: ['La forme alterne entre deux états qui se succèdent.',
          'Le nombre de points augmente puis recommence.',
          'L’état plein et l’état vide alternent.',
          'Le motif change toutes les trois cases et revient.',
          'La forme tourne d’un quart de tour vers la droite.'][ruleKind],
        time: 30
      });
    }
    return items;
  }

  /* ══════════════════════════════════════════════════════════════
     D. CONCENTRATION — paires de figures : identiques ou différentes
     ══════════════════════════════════════════════════════════════ */
  function concentrationSet(n = 60) {
    const items = [];
    const base = ['circle', 'square', 'tri-up', 'diamond', 'star', 'plus', 'cross', 'dot-ring', 'square-half', 'chev-up', 'disc', 'square-rot'];
    const variants = {
      'circle': ['disc', 'dot-ring'], 'square': ['square-rot', 'square-half'], 'tri-up': ['tri-down', 'tri-left'],
      'diamond': ['square-rot', 'tri-up'], 'star': ['plus', 'cross'], 'plus': ['cross', 'star'],
      'cross': ['plus', 'star'], 'dot-ring': ['disc', 'circle'], 'square-half': ['square-full', 'square'],
      'chev-up': ['chev-down', 'tri-up'], 'disc': ['circle', 'dot-ring'], 'square-rot': ['square', 'diamond']
    };
    for (let i = 0; i < n; i++) {
      const r = U.rng(5000 + i * 31);
      const k = U.pick(r, base);
      const col = U.pick(r, ['grn', 'amb', 'blu', 'pur', 'teal', 'red', 'ink']);
      const same = r() < 0.5;
      const k2 = same ? k : U.pick(r, variants[k]);
      /* variation de rotation/couleur uniquement si différent */
      const col2 = same ? col : (r() < 0.45 ? U.pick(r, ['grn', 'amb', 'blu', 'pur', 'teal', 'red', 'ink'].filter(c => c !== col)) : col);
      items.push({
        id: 'CON' + (i + 1), sec: 'concentration',
        left: { kind: k, color: col }, right: { kind: (same && col2 === col) ? k : k2, color: col2 },
        same: (same && col2 === col), time: 2500
      });
    }
    return items;
  }

  /* ══════════════════════════════════════════════════════════════
     E. LEARNING EFFICIENCY — grille 5×5, 5 cases clignotantes
     ══════════════════════════════════════════════════════════════ */
  function learningSet(n = 20) {
    const out = [];
    for (let i = 0; i < n; i++) {
      const r = U.rng(9000 + i * 41);
      const N = 5, cells = [];
      while (cells.length < 5) { const c = U.int(r, 0, 24); if (!cells.includes(c)) cells.push(c); }
      const color = ['grn', 'blu', 'amb', 'pur', 'teal'][i % 5];
      out.push({
        id: 'LEA' + (i + 1), sec: 'learning', size: N, cells, color,
        /* temps d'affichage adaptatif : diminue par palier (entraînement à la vitesse) */
        show: [9000, 8000, 7000, 6000, 5000][Math.min(4, Math.floor(i / 4))],
        time: 60
      });
    }
    return out;
  }

  /* ══════════════════════════════════════════════════════════════
     F. SWITCH CHALLENGE — retrouver la suite d'échanges appliquée
     ══════════════════════════════════════════════════════════════ */
  const SWAP_GLYPH = (a, b) => '⇄ ' + (a + 1) + '·' + (b + 1);

  function applyPerm(arr, perm) { return perm.map(i => arr[i]); }

  function switchSet(n = 30) {
    const items = [];
    const SWAPS = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]];
    for (let i = 0; i < n; i++) {
      const r = U.rng(13000 + i * 53);
      const input = U.shuffle(r, [1, 2, 3, 4]);
      /* on construit une séquence valide de 1 à 3 échanges */
      const nSwaps = 1 + Math.floor(i / 10);
      const chosen = [];
      let perm = [0, 1, 2, 3];
      for (let s = 0; s < nSwaps; s++) {
        const sw = U.pick(r, SWAPS);
        chosen.push(sw);
        const p = [0, 1, 2, 3]; const t = p[sw[0]]; p[sw[0]] = p[sw[1]]; p[sw[1]] = t;
        perm = applyPerm(perm, p);
      }
      /* éviter la permutation identité (énoncé trivial) */
      if (perm.every((v, idx) => v === idx)) {
        const sw = U.pick(r, SWAPS);
        chosen.push(sw);
        const p = [0, 1, 2, 3]; const t = p[sw[0]]; p[sw[0]] = p[sw[1]]; p[sw[1]] = t;
        perm = applyPerm(perm, p);
      }
      const output = applyPerm(input, perm);
      /* options : la bonne (les échanges choisis) + 3 leurres dont la composition ≠ perm */
      const key = (arr) => arr.map(s => s.join('-')).join('|');
      const opts = [{ swaps: chosen, ok: true }];
      let guard = 0;
      while (opts.length < 4 && guard < 200) {
        guard++;
        const cand = [];
        let cp = [0, 1, 2, 3];
        const k = nSwaps === 1 ? 1 : (r() < 0.5 ? 1 : 2);
        for (let s = 0; s < k; s++) {
          const sw = U.pick(r, SWAPS);
          cand.push(sw);
          const p = [0, 1, 2, 3]; const t = p[sw[0]]; p[sw[0]] = p[sw[1]]; p[sw[1]] = t;
          cp = applyPerm(cp, p);
        }
        if (key(cand) === key(chosen)) continue;
        if (cp.join() === perm.join()) continue;   /* composition identique → on écarte */
        if (opts.some(o => key(o.swaps) === key(cand))) continue;
        opts.push({ swaps: cand, ok: false });
      }
      const sh = U.shuffle(r, opts);
      items.push({
        id: 'SW' + (i + 1), sec: 'switch', input, output,
        options: sh.map(o => ({ label: o.swaps.map(s => SWAP_GLYPH(s[0], s[1])).join('  '), swaps: o.swaps })),
        ans: sh.findIndex(o => o.ok),
        why: 'La bonne option reproduit exactement la permutation observée.',
        time: nSwaps === 1 ? 25 : (nSwaps === 2 ? 35 : 45)
      });
    }
    return items;
  }

  /* ══════════════════════════════════════════════════════════════
     G. MÉMOIRE DE TRAVAIL — grille, cases colorées à mémoriser
     ══════════════════════════════════════════════════════════════ */
  function memorySet(n = 15) {
    const out = [];
    for (let i = 0; i < n; i++) {
      const r = U.rng(21000 + i * 67);
      const size = 5, k = 4 + (i % 2);
      const cells = [];
      while (cells.length < k) { const c = U.int(r, 0, size * size - 1); if (!cells.includes(c)) cells.push(c); }
      out.push({ id: 'MEM' + (i + 1), sec: 'memory', size, cells, show: 3000, time: 45 });
    }
    return out;
  }

  /* ══════════════════════════════════════════════════════════════
     H. RAISONNEMENT MÉCANIQUE — scènes SVG paramétriques
     ══════════════════════════════════════════════════════════════ */
  function mechScene(kind) {
    const c = '#9aa7b8', hl = '#2ecc8f', amb = '#e3b341';
    const gear = (cx, cy, r, col, label) =>
      '<g><circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="none" stroke="' + (col || c) + '" stroke-width="4"/>' +
      Array.from({ length: 10 }, (_, i) => {
        const a = i * 36 * Math.PI / 180;
        return '<rect x="' + (cx + (r + 4) * Math.cos(a) - 4) + '" y="' + (cy + (r + 4) * Math.sin(a) - 4) + '" width="8" height="8" fill="' + (col || c) + '"/>';
      }).join('') +
      '<text x="' + cx + '" y="' + (cy + 5) + '" font-size="16" font-weight="800" fill="' + (col || c) + '" text-anchor="middle" font-family="Inter">' + label + '</text></g>';
    const pulley = (cx, cy, r, col, label) =>
      '<g><circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="none" stroke="' + (col || c) + '" stroke-width="4"/>' +
      '<circle cx="' + cx + '" cy="' + cy + '" r="4" fill="' + (col || c) + '"/>' +
      '<text x="' + cx + '" y="' + (cy + 5) + '" font-size="15" font-weight="800" fill="' + (col || c) + '" text-anchor="middle" font-family="Inter">' + label + '</text></g>';
    const line = (x1, y1, x2, y2) => '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="' + c + '" stroke-width="3" stroke-dasharray="7 5"/>';
    switch (kind) {
      case 'gears2': return '<svg viewBox="0 0 420 200">' + gear(120, 100, 52, hl, 'A') + gear(240, 100, 52, amb, 'B') + '</svg>';
      case 'gears3': return '<svg viewBox="0 0 420 200">' + gear(90, 100, 42, hl, 'A') + gear(200, 100, 42, amb, 'B') + gear(310, 100, 42, c, 'C') + '</svg>';
      case 'gears4': return '<svg viewBox="0 0 520 200">' + gear(80, 100, 36, hl, 'A') + gear(190, 100, 36, amb, 'B') + gear(300, 100, 36, c, 'C') + gear(410, 100, 36, c, 'D') + '</svg>';
      case 'gears2size': return '<svg viewBox="0 0 460 200">' + gear(110, 100, 34, hl, 'A') + gear(300, 100, 74, amb, 'B') + '</svg>';
      case 'belt': return '<svg viewBox="0 0 440 220">' + pulley(120, 110, 62, hl, 'A') + pulley(320, 110, 62, amb, 'B') +
        '<path d="M120 48 L320 48 M120 172 L320 172" stroke="' + c + '" stroke-width="4"/>' + '</svg>';
      case 'beltcross': return '<svg viewBox="0 0 440 240">' + pulley(120, 120, 62, hl, 'A') + pulley(320, 120, 62, amb, 'B') +
        '<path d="M120 58 L320 182 M120 182 L320 58" stroke="' + c + '" stroke-width="4"/>' + '</svg>';
      case 'lever': return '<svg viewBox="0 0 480 200">' +
        '<path d="M40 150 L440 150" stroke="' + c + '" stroke-width="8"/>' +
        '<path d="M240 150 L240 190" stroke="' + amb + '" stroke-width="8"/>' +
        '<rect x="30" y="106" width="52" height="40" fill="' + hl + '" rx="4"/><text x="56" y="132" font-size="14" font-weight="800" fill="#04120d" text-anchor="middle">CH</text>' +
        '<path d="M420 150 L420 120" stroke="' + amb + '" stroke-width="6"/><path d="M410 128 L420 108 L430 128 Z" fill="' + amb + '"/>' +
        '<text x="240" y="188" font-size="13" fill="' + c + '" text-anchor="middle">pivot</text></svg>';
      case 'pulley1': return '<svg viewBox="0 0 320 240">' + pulley(160, 60, 46, hl, 'P') +
        '<line x1="160" y1="106" x2="160" y2="180" stroke="' + c + '" stroke-width="3"/>' +
        '<rect x="130" y="180" width="60" height="42" fill="' + amb + '" rx="4"/><text x="160" y="207" font-size="13" font-weight="800" fill="#1a1400" text-anchor="middle">Q</text></svg>';
      case 'pulley2': return '<svg viewBox="0 0 340 260">' + pulley(110, 50, 34, c, 'F') + pulley(210, 50, 34, c, 'F') +
        '<path d="M110 84 L110 190 M210 84 L210 190" stroke="' + c + '" stroke-width="3"/>' + '<rect x="120" y="190" width="80" height="46" fill="' + amb + '" rx="4"/>' +
        '<text x="160" y="220" font-size="13" font-weight="800" fill="#1a1400" text-anchor="middle">Q</text></svg>';
      case 'pulley3': return '<svg viewBox="0 0 400 260">' + pulley(90, 46, 30, c, 'F') + pulley(190, 46, 30, c, 'F') + pulley(290, 46, 30, c, 'F') +
        '<path d="M90 76 L90 190 M190 76 L190 190 M290 76 L290 190" stroke="' + c + '" stroke-width="3"/>' +
        '<rect x="120" y="190" width="140" height="46" fill="' + amb + '" rx="4"/><text x="190" y="220" font-size="13" font-weight="800" fill="#1a1400" text-anchor="middle">Q</text></svg>';
      case 'spring': return '<svg viewBox="0 0 300 240">' +
        '<path d="M60 40 L240 40" stroke="' + c + '" stroke-width="6"/>' +
        '<path d="M150 40 ' + Array.from({ length: 9 }, (_, i) => 'L' + (i % 2 ? 120 : 180) + ' ' + (52 + i * 12)).join(' ') + '" stroke="' + hl + '" stroke-width="4" fill="none"/>' +
        '<rect x="110" y="160" width="80" height="44" fill="' + amb + '" rx="4"/><text x="150" y="189" font-size="13" font-weight="800" fill="#1a1400" text-anchor="middle">Q</text></svg>';
      case 'axle': return '<svg viewBox="0 0 420 220">' + pulley(140, 110, 70, hl, 'G') + pulley(300, 110, 26, amb, 'P') +
        '<line x1="140" y1="110" x2="300" y2="110" stroke="' + c + '" stroke-width="4"/>' +
        '<text x="140" y="204" font-size="12" fill="' + c + '" text-anchor="middle">même axe</text></svg>';
      default: return '<svg viewBox="0 0 300 160">' + gear(150, 80, 48, hl, '·') + '</svg>';
    }
  }

  /* ══════════════════════════════════════════════════════════════
     I. Correspondance figure → rendu SVG (banque déductive)
     ══════════════════════════════════════════════════════════════ */
  const FIGMAP = {
    'circle': 'circle', 'square': 'square', 'triangle': 'tri-up', 'dot': 'dot-1',
    'd1': 'dot-1', 'd2': 'dot-2', 'd3': 'dot-3',
    'arr-r': 'arr-right', 'arr-l': 'arr-left', 'arr-u': 'arr-up', 'arr-d': 'arr-down',
    'full': 'disc', 'empty': 'circle', 'full2': 'dot-ring',
    'gp': 'plus', 'gm': 'cross', 'gh': 'star',
    'c-tl': 'circle', 's-t': 'square', 't-tr': 'tri-up', 't-r': 'tri-right', 'c-br': 'dot-ring', 's-b': 'square-half', 's-bl': 'square-rot', 't-l': 'tri-left', 's-br': 'square-full',
    'thin': 'circle', 'mid': 'dot-ring', 'thick': 'disc',
    'ht': 'half-top', 'hl': 'half-left', 'hb': 'half-top',
    'a': 'circle', 'b': 'square', 'ab': 'dot-ring',
    'fl': 'chev-up', 'fr': 'chev-down', 'f2': 'tri-down',
    'h1': 'diamond', 'h2': 'square-rot', 'h3': 'tri-left', 'h4': 'square-diag'
  };
  const COLORMAP = { grn: '#0a8a3c', amb: '#b58100', red: '#c62828', blu: '#1565c0', pur: '#5b3d8f', teal: '#0d6f78', ink: '#23282c', gray: '#5a656e' };

  /** Rend une case de la banque déductive (spec = {shape,color} ou clé). */
  function dedTile(spec, colKey, cls) {
    const kindKey = typeof spec === 'string' ? spec : spec.shape;
    const colK = typeof spec === 'string' ? colKey : spec.color;
    const kind = FIGMAP[kindKey] || 'square';
    const color = COLORMAP[colK] || COLORMAP.ink;
    const isQ = kindKey === '??' || spec === '??';
    return '<div class="sym ' + (cls || '') + (isQ ? ' unknown' : '') + '">' + (isQ ? '' : U.shape(kind, color)) + '</div>';
  }

  return { nf, money, pctS, numericalFixed, verbalItem, VB_BLUEPRINTS, inductiveSet, concentrationSet,
           learningSet, switchSet, memorySet, mechScene, dedTile, FIGMAP, COLORMAP, NUM_SCEN };
})();
