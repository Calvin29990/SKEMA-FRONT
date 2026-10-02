/* Verbal au format réel : 6 onglets de textes, 49 énoncés (ici 3), 12 min, true/false/cannot say */
const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');
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
  page.on('console', m => { if (m.type() === 'error' && !/net::|ERR_CONNECTION_CLOSED/.test(m.text())) errs.push('console: ' + m.text()); });
  page.on('request', r => { const u = r.url(); if (!/^http:\/\/(127\.0\.0\.1|localhost):8080\//.test(u) && !u.startsWith('data:') && !u.startsWith('blob:')) externes.push(u); });

  await page.goto('http://127.0.0.1:8080/', { waitUntil: 'networkidle2' });
  await page.evaluate(() => localStorage.clear());
  await page.reload({ waitUntil: 'networkidle2' });
  await page.type('#lgCode', 'CM2026'); await page.type('#lgName', 'Calvin'); await page.click('#lgGo'); await wait(600);

  /* le fichier verbal est placé dans fixtures/ par le harnais */
  await page.evaluate(() => { location.hash = '#/section/numerical'; }); await wait(500);
  await (await page.$('#nvFileOpen')).click(); await wait(300);
  await (await page.$('input[type=file]')).uploadFile(path.join(__dirname, 'fixtures', 'verbal-neutral.json')); await wait(700);

  const st = await page.evaluate(() => ({
    perso: NUMVERB.isPerso(), items: NUMVERB.ITEMS.length, src: NUMVERB.source,
    tabs: NUMVERB.TABS.map(t => t.short), kinds: NUMVERB.TABS.map(t => NUMVERB.kindOf(t.id)),
  }));
  ok('fichier verbal chargé (3 énoncés, 3 onglets)', st.perso && st.items === 3 && st.tabs.length === 3, st.items + ' énoncés');
  ok('les onglets du fichier', st.tabs.join('|') === 'Structure|Strategy|Principles', st.tabs.join(' · '));
  ok('onglets reconnus comme panneaux de texte', st.kinds.every(k => k === 'text'), st.kinds.join(','));

  await page.evaluate(() => { location.hash = '#/run/numerical'; }); await wait(900);
  const run = await page.evaluate(() => {
    const fig = document.querySelector('#nvFig');
    return {
      cols: !!document.querySelector('.nv-cols'),
      texte: !!document.querySelector('.nvtext'),
      contenu: (fig || {}).textContent.replace(/\s+/g, ' ').slice(0, 90),
      q: (document.querySelector('.nv-stmt') || {}).textContent.replace(/\s+/g, ' ').slice(0, 70),
      btns: [...document.querySelectorAll('.nvbtn')].map(b => b.textContent).join('/'),
      timer: (document.querySelector('#qTimer') || {}).textContent,
      qno: (document.querySelector('.nv-qno') || {}).textContent,
    };
  });
  ok('mise en page à deux colonnes (texte + énoncé)', run.cols, 'grille .nv-cols');
  ok('texte du fichier affiché', run.texte && /Blue Harbour/.test(run.contenu), run.contenu.slice(0, 60) + '…');
  ok('énoncé + boutons true/false/cannot say', /Question 1 \/ 3/.test(run.qno) && run.btns === 'true/false/cannot say', run.qno + ' · ' + run.btns);
  ok('chrono global 12:00', /^1[12]:\d\d$/.test(run.timer), run.timer);

  /* bascule : la question 3 est dans Strategy */
  await page.evaluate(() => { document.querySelector('.nvbtn').click(); document.querySelector('#nvNext').click(); }); await wait(200);
  await page.evaluate(() => { document.querySelector('.nvbtn').click(); document.querySelector('#nvNext').click(); }); await wait(300);
  const q3 = await page.evaluate(() => ({
    tab: (document.querySelector('.nvt.on') || {}).textContent,
    texte: (document.querySelector('#nvFig') || {}).textContent.replace(/\s+/g, ' ').slice(0, 70),
    qno: (document.querySelector('.nv-qno') || {}).textContent,
  }));
  ok('bascule automatique vers Strategy à la question 3', q3.tab === 'Strategy' && /3 \/ 3/.test(q3.qno), q3.qno + ' → ' + q3.tab);
  ok('le texte affiché suit l’onglet', /Croissance externe/.test(q3.texte), q3.texte.slice(0, 55) + '…');

  /* capture d'écran de contrôle */
  await page.evaluate(() => { location.hash = '#/run/numerical'; }); await wait(500);
  await page.evaluate(() => { document.querySelector('.nvt').click(); }); await wait(300);

  ok('aucun envoi réseau externe', externes.length === 0, externes.slice(0, 2).join(' · ') || 'aucune requête sortante');

  console.log(out.join('\n'));
  console.log('\nerreurs JS :', errs.length ? errs.slice(0, 4) : 'aucune');
  console.log('\n' + (ko === 0 && errs.length === 0 ? '🎉 VERBAL FORMAT RÉEL : TOUT OK' : '⚠ ' + ko + ' échec(s)'));
  await browser.close();
  process.exit(ko || errs.length ? 1 : 0);
})().catch(e => { console.error('FAIL', e.message); process.exit(1); });
