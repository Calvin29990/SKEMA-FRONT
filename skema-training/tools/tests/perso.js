/* Test du chargeur « perso » : fichier local -> moteur au format réel, sans aucun envoi réseau */
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');
const FIX = (n) => path.join(__dirname, 'fixtures', n);
const out = []; let ko = 0;
const ok = (l, c, x = '') => { out.push((c ? '✅' : '❌') + ' ' + l + (x ? ' — ' + x : '')); if (!c) ko++; return c; };
const wait = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--hide-scrollbars'],
    executablePath: '/tmp/chromium', headless: 'shell', defaultViewport: { width: 1366, height: 1000 },
  });
  const ctx = await browser.createBrowserContext();
  const page = await ctx.newPage();
  const errs = [], externes = [];
  page.on('pageerror', e => errs.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/fonts\.googleapis|ERR_CONNECTION_CLOSED|net::/.test(m.text())) errs.push('console: ' + m.text()); });
  page.on('request', r => { const u = r.url(); if (!/^http:\/\/(127\.0\.0\.1|localhost):8080\//.test(u) && !u.startsWith('data:') && !u.startsWith('blob:')) externes.push(u); });

  await page.goto('http://127.0.0.1:8080/', { waitUntil: 'networkidle2' });
  await page.evaluate(() => localStorage.clear());
  await page.reload({ waitUntil: 'networkidle2' });
  await page.type('#lgCode', 'CM2026'); await page.type('#lgName', 'Calvin'); await page.click('#lgGo'); await wait(600);
  await page.evaluate(() => { location.hash = '#/section/numerical'; }); await wait(600);

  ok('page de la tâche : bouton « Ouvrir mon fichier »', !!await page.$('#nvFileOpen'), 'bouton présent');
  const st0 = await page.evaluate(() => document.querySelector('#nvFileStatus').textContent.trim());
  ok('statut initial = banque intégrée', /intégrée/i.test(st0), st0.slice(0, 60));

  /* 1. fichier invalide : refusé, liste d'erreurs, aucun chargement */
  fs.writeFileSync(FIX('mauvais.json'), JSON.stringify({ tabs: [{ id: 'a' }], items: [{ q: 'x', tab: 'a', ans: 9 }] }));
  let alerte = '';
  page.on('dialog', async d => { alerte = d.message(); await d.accept(); });
  const inp = await page.$('#nvFileOpen');
  await inp.click(); await wait(300);
  const fileInput = await page.$('input[type=file]');
  await fileInput.uploadFile(FIX('mauvais.json')); await wait(600);
  ok('fichier incomplet refusé avec la liste des erreurs', /refusé/i.test(alerte) && /ans/.test(alerte), alerte.split('\n')[1] || alerte.slice(0, 60));

  /* 2. fichier valide : le moteur bascule sur le contenu local */
  await page.evaluate(() => { location.hash = '#/'; }); await wait(400);
  await page.evaluate(() => { location.hash = '#/section/numerical'; }); await wait(500);
  const inp2 = await page.$('#nvFileOpen'); await inp2.click(); await wait(300);
  const fi2 = await page.$('input[type=file]');
  await fi2.uploadFile(FIX('perso-test.json')); await wait(700);
  const st1 = await page.evaluate(() => ({
    txt: document.querySelector('#nvFileStatus').textContent.replace(/\s+/g, ' ').trim(),
    items: NUMVERB.ITEMS.length, tabs: NUMVERB.TABS.map(t => t.short), sec: NUMVERB.totalSec,
    perso: NUMVERB.isPerso(), titre: NUMVERB.title,
  }));
  ok('fichier valide chargé (8 énoncés, 6 onglets)', st1.perso && st1.items === 8 && st1.tabs.length === 6, st1.items + ' énoncés · ' + st1.tabs.join('/'));
  ok('statut affiché sur la page', /Fichier perso chargé/.test(st1.txt) && /8 énoncé/.test(st1.txt), st1.txt.slice(0, 80));
  ok('durée reprise du fichier (5 min)', st1.sec === 300, st1.sec + ' s');

  /* 3. la session utilise bien le contenu du fichier, avec l'ergonomie du test réel */
  const go = await page.evaluate(() => { location.hash = '#/run/numerical'; return true; }); await wait(900);
  const run = await page.evaluate(() => ({
    tabs: [...document.querySelectorAll('.nvt')].map(b => b.textContent),
    q: (document.querySelector('.nv-stmt') || {}).textContent.replace(/\s+/g, ' '),
    qno: (document.querySelector('.nv-qno') || {}).textContent,
    btns: [...document.querySelectorAll('.nvbtn')].map(b => b.textContent).join('/'),
    timer: (document.querySelector('#qTimer') || {}).textContent,
    fig: !!document.querySelector('.nv-fig svg, .nv-fig table'),
  }));
  ok('6 onglets du fichier affichés', run.tabs.join('|') === st1.tabs.join('|'), run.tabs.join(' | '));
  ok('énoncé du fichier affiché', /chiffre d'affaires/.test(run.q), run.q.slice(0, 60));
  ok('compteur + boutons true/false/cannot say', /1 \/ 8/.test(run.qno) && run.btns === 'true/false/cannot say', run.qno + ' · ' + run.btns);
  ok('chrono global à 5:00', /^(4:5\d|5:00)$/.test(run.timer), run.timer);
  ok('figure rendue (tableau du fichier)', run.fig);

  const seq = await page.evaluate(async () => {
    const r = [];
    for (let i = 0; i < 8; i++) {
      r.push((document.querySelector('.nvt.on') || {}).textContent);
      const b = document.querySelector('.nvbtn'); if (b) b.click();
      const n = document.querySelector('#nvNext'); if (n) n.click();
      await new Promise(s => setTimeout(s, 60));
    }
    return r;
  });
  const attendu = await page.evaluate(() => NUMVERB.ITEMS.map(i => NUMVERB.tabOf(i.tab).short));
  ok('bascule automatique sur l’onglet de chaque énoncé', JSON.stringify(seq) === JSON.stringify(attendu), seq.join(' → '));

  const sum = await page.evaluate(async () => {
    await new Promise(s => setTimeout(s, 700));
    return { rows: document.querySelectorAll('.qtbl2 tbody tr').length, score: !!document.querySelector('.scorebig'),
             content: (CORE.P.attempts().slice(-1)[0] || {}).content };
  });
  ok('résumé : 8 lignes de détail', sum.rows === 8 && sum.score, sum.rows + ' lignes');
  ok('tentative marquée « perso »', sum.content === 'perso', String(sum.content));

  /* 4. rien ne fuit : aucun appel réseau hors du serveur local */
  ok('aucun envoi réseau externe', externes.length === 0, externes.slice(0, 2).join(' · ') || 'aucune requête sortante');

  /* 5. retour à la banque intégrée */
  await page.evaluate(() => { location.hash = '#/section/numerical'; }); await wait(600);
  await page.evaluate(() => { const a = document.querySelector('#nvFileReset'); if (a) a.click(); }); await wait(400);
  const back = await page.evaluate(() => ({ perso: NUMVERB.isPerso(), items: NUMVERB.ITEMS.length, txt: document.querySelector('#nvFileStatus').textContent.trim() }));
  ok('retour à la banque intégrée (37 énoncés)', !back.perso && back.items === 37, back.items + ' énoncés · ' + back.txt.slice(0, 40));

  console.log(out.join('\n'));
  console.log('\nerreurs JS :', errs.length ? errs.slice(0, 4) : 'aucune');
  console.log('\n' + (ko === 0 && errs.length === 0 ? '🎉 CHARGEUR PERSO : TOUT OK' : '⚠ ' + ko + ' échec(s)'));
  await browser.close();
  process.exit(ko || errs.length ? 1 : 0);
})().catch(e => { console.error('FAIL', e.message); process.exit(1); });
