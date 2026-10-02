/* Déductif (grille 4×4, 6 min) et inductif (2 grilles parmi 4, 6 min) : formats réels */
const puppeteer = require('puppeteer-core');
const out = []; let ko = 0;
const ok = (l, c, x = '') => { out.push((c ? '✅' : '❌') + ' ' + l + (x ? ' — ' + x : '')); if (!c) ko++; return c; };
const wait = ms => new Promise(r => setTimeout(r, ms));

/* les mêmes règles que le moteur, pour vérifier les grilles générées */
const RULE_OK = {
  corners: g => g[0] === g[2] && g[0] === g[6] && g[0] === g[8],
  row: g => [0, 3, 6].some(r => g[r] === g[r + 1] && g[r] === g[r + 2]),
  col: g => [0, 1, 2].some(c => g[c] === g[c + 3] && g[c] === g[c + 6]),
  centre: g => g[4] === g[0] && g[4] === g[2] && g[4] === g[6] && g[4] === g[8],
  mirror: g => [0, 3, 6].every(r => g[r] === g[r + 2]),
  diag: g => g[0] === g[4] && g[4] === g[8] && g[2] === g[4] && g[6] === g[4],
};

(async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--hide-scrollbars'],
    executablePath: '/tmp/chromium', headless: 'shell', defaultViewport: { width: 1366, height: 1050 }, protocolTimeout: 240000,
  });
  const page = await (await browser.createBrowserContext()).newPage();
  const errs = [];
  page.on('pageerror', e => errs.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
  page.on('dialog', d => d.accept());

  await page.goto('http://127.0.0.1:8080/', { waitUntil: 'networkidle2' });
  await page.evaluate(() => localStorage.clear());
  await page.reload({ waitUntil: 'networkidle2' });
  await page.type('#lgCode', 'CM2026'); await page.type('#lgName', 'Calvin'); await page.click('#lgGo'); await wait(600);

  /* ── DÉDUCTIF ── */
  await page.evaluate(() => { location.hash = '#/run/deductive?count=12'; }); await wait(900);
  const d = await page.evaluate(() => {
    const S = CORE.current, it = S.items[0];
    const t = document.querySelectorAll('.ggrid.g4 .gtile');
    return {
      kind: it.kind, cases: t.length, trou: document.querySelectorAll('.gtile.hole').length,
      options: document.querySelectorAll('#gopts .gopt').length,
      symParLigne: it.grid.map(r => new Set(r).size), symParCol: [0, 1, 2, 3].map(c => new Set(it.grid.map(r => r[c])).size),
      ansDonnee: it.grid[it.hole[0]][it.hole[1]],
      ansOption: CORE.current.items[0].options[CORE.current.items[0].ans] && true,
      titre: document.querySelector('.qtext.sm').textContent.trim(),
      total: S.items.length, chrono: (document.querySelector('#qTimer') || {}).textContent,
    };
  });
  ok('déductif : grille 4×4 avec une case « ? »', d.cases === 16 && d.trou === 1, d.cases + ' cases · ' + d.trou + ' trou');
  ok('chaque symbole présent une fois par ligne et par colonne', d.symParLigne.every(x => x === 4) && d.symParCol.every(x => x === 4), 'lignes ' + d.symParLigne + ' · colonnes ' + d.symParCol);
  ok('4 symboles proposés en réponse', d.options === 4, d.options + ' options');
  ok('consigne anglaise du test réel', /Please choose the correct answer/.test(d.titre), d.titre);
  ok('12 grilles pour 6 minutes', d.total === 12, d.total + ' grilles · chrono ' + d.chrono);

  /* une bonne réponse doit être comptée juste */
  const dOk = await page.evaluate(() => {
    const S = CORE.current, it = S.items[S.i];
    document.querySelectorAll('#gopts .gopt')[it.ans].click();
    return { hud: document.querySelector('#hud').textContent.replace(/\s+/g, ' '), marque: document.querySelectorAll('#gopts .gopt.ok').length };
  });
  await wait(400);
  const d2 = await page.evaluate(() => ({ hud: document.querySelector('#hud').textContent.replace(/\s+/g, ' '), item: document.querySelector('#hud .pill.mono').textContent }));
  ok('la bonne réponse est comptée juste', /✔ 1/.test(d2.hud), d2.hud.slice(0, 40) + ' · ' + d2.item);
  ok('le symbole choisi est marqué correct', dOk.marque === 1, dOk.marque + ' symbole marqué');

  /* ── INDUCTIF ── */
  await page.evaluate(() => { location.hash = '#/run/inductive?count=8'; }); await wait(900);
  const i1 = await page.evaluate(() => {
    const S = CORE.current, it = S.items[0];
    return {
      kind: it.kind, exemple: document.querySelectorAll('.i2-side')[0].querySelectorAll('.ggrid.g3').length,
      cands: document.querySelectorAll('#cands .cand').length,
      tailles: [...document.querySelectorAll('.ggrid.g3')].map(g => g.children.length),
      titreG: document.querySelector('.i2-t').textContent.trim(),
      titreD: document.querySelectorAll('.i2-t')[1].textContent.trim(),
      total: S.items.length, why: it.why, good: it.good.slice(),
    };
  });
  ok('inductif : 2 grilles d’exemple + 4 candidates', i1.exemple === 2 && i1.cands === 4, i1.exemple + ' exemples · ' + i1.cands + ' candidates');
  ok('grilles 3×3', i1.tailles.length === 6 && i1.tailles.every(x => x === 9), 'tailles ' + [...new Set(i1.tailles)].join(','));
  ok('consignes du test réel', /These two grids follow a rule/.test(i1.titreG) && /Which two of these grids/.test(i1.titreD), i1.titreG + ' | ' + i1.titreD);
  ok('8 séries pour 6 minutes', i1.total === 8, i1.total + ' séries');

  /* le moteur doit générer exactement 2 candidates conformes à la règle annoncée */
  const verif = await page.evaluate(() => {
    const R = { corners: g => g[0] === g[2] && g[0] === g[6] && g[0] === g[8],
      row: g => [0, 3, 6].some(r => g[r] === g[r + 1] && g[r] === g[r + 2]),
      col: g => [0, 1, 2].some(c => g[c] === g[c + 3] && g[c] === g[c + 6]),
      centre: g => g[4] === g[0] && g[4] === g[2] && g[4] === g[6] && g[4] === g[8],
      mirror: g => [0, 3, 6].every(r => g[r] === g[r + 2]),
      diag: g => g[0] === g[4] && g[4] === g[8] && g[2] === g[4] && g[6] === g[4] };
    const nom = { 'les quatre coins portent le même symbole': 'corners', 'une ligne entière porte le même symbole': 'row',
      'une colonne entière porte le même symbole': 'col', 'la case du centre porte le même symbole que les quatre coins': 'centre',
      'la grille est symétrique de gauche à droite': 'mirror', 'les deux diagonales portent le même symbole': 'diag' };
    const items = [];
    for (let s = 1; s <= 20; s++) items.push(...CORE.buildItems(CORE.byId('inductive'), { count: 2, seed: s * 977 }));
    return items.map(it => {
      const cle = Object.keys(nom).find(k => it.why.indexOf(k) === 8);
      const r = R[nom[cle]] || (() => true);
      const bons = it.candidates.filter(r).length;
      const exemplesOk = it.examples.every(r);
      const goodOk = it.good.every(i => r(it.candidates[i]));
      return { bons, exemplesOk, goodOk, n: it.good.length };
    });
  });
  const tous = verif.every(v => v.bons === 2 && v.exemplesOk && v.goodOk && v.n === 2);
  ok('les 2 grilles d’exemple suivent bien la règle', verif.every(v => v.exemplesOk), verif.length + ' séries vérifiées');
  ok('exactement 2 candidates conformes, et ce sont les bonnes', tous,
     'par série : ' + [...new Set(verif.map(v => v.bons))].join(',') + ' conforme(s) · réponses correctes alignées : ' + verif.every(v => v.goodOk));

  /* sélection et validation */
  const rep = await page.evaluate(() => {
    const S = CORE.current, it = S.items[S.i];
    const bad = [0, 1, 2, 3].find(i => !it.good.includes(i));
    document.querySelectorAll('#cands .cand')[bad].click();
    const apresMauvais = { sel: document.querySelectorAll('#cands .cand.sel').length, valider: document.querySelector('#okBtn').disabled, msg: document.querySelector('#pickMsg').textContent };
    document.querySelectorAll('#cands .cand')[it.good[0]].click();
    const apresDeux = { sel: document.querySelectorAll('#cands .cand.sel').length, valider: document.querySelector('#okBtn').disabled };
    return { apresMauvais, apresDeux, good: it.good };
  });
  ok('la validation s’active seulement à 2 grilles', rep.apresMauvais.valider === true && rep.apresDeux.valider === false,
     rep.apresMauvais.sel + ' puis ' + rep.apresDeux.sel + ' sélection(s) · message « ' + rep.apresMauvais.msg + ' »');

  await page.evaluate(() => document.querySelector('#okBtn').click()); await wait(500);
  const fb = await page.evaluate(() => ({ hud: document.querySelector('#hud').textContent.replace(/\s+/g, ' '),
    ok: document.querySelectorAll('#cands .cand.ok').length, ko: document.querySelectorAll('#cands .cand.ko').length,
    why: (document.querySelector('.fb .small') || {}).textContent || '' }));
  ok('sélection incomplète = erreur signalée, bonnes grilles montrées', /✘ 1/.test(fb.hud) && fb.ok === 2, 'marquées bonnes : ' + fb.ok + ' · choix erroné : ' + fb.ko);
  ok('la règle est expliquée après coup', /Règle :/.test(fb.why), fb.why.slice(0, 78));

  /* les 3 suites d'entraînement restent accessibles */
  const old = await page.evaluate(() => ({ mat: !!CORE.byId('deductiveMat'), serie: !!CORE.byId('inductiveSerie'), mix: CORE.SECTIONS.length }));
  ok('anciens entraînements conservés (matrices, séries)', old.mat && old.serie, old.mix + ' sections au total');

  ok('aucune erreur JS', errs.length === 0, errs.slice(0, 2).join(' · '));

  console.log(out.join('\n'));
  console.log('\n' + (ko === 0 && !errs.length ? '🎉 DÉDUCTIF + INDUCTIF (FORMATS RÉELS) : TOUT OK' : '⚠ ' + ko + ' échec(s)'));
  await browser.close();
  process.exit(ko || errs.length ? 1 : 0);
})().catch(e => { console.error('FAIL', e.stack); process.exit(1); });
