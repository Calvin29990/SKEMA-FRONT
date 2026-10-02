/* Numerical au format réel : 6 onglets, 37 énoncés, 12:00, bascule auto + consultation manuelle */
const puppeteer = require('puppeteer-core');
const out = []; let ko = 0;
const ok = (l, c, x = '') => { out.push((c ? '✅' : '❌') + ' ' + l + (x ? ' — ' + x : '')); if (!c) ko++; return c; };
const wait = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--hide-scrollbars'],
    executablePath: '/tmp/chromium', headless: 'shell', defaultViewport: { width: 1280, height: 1050 },
  });
  const ctx = await browser.createBrowserContext();
  const page = await ctx.newPage();
  const errs = [];
  page.on('pageerror', e => errs.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/fonts\.googleapis|ERR_CONNECTION_CLOSED|net::/.test(m.text())) errs.push('console: ' + m.text()); });

  await page.goto('http://127.0.0.1:8080/', { waitUntil: 'networkidle2' });
  await page.evaluate(() => localStorage.clear());
  await page.reload({ waitUntil: 'networkidle2' });
  await page.type('#lgCode', 'CM2026'); await page.type('#lgName', 'Calvin'); await page.click('#lgGo'); await wait(700);

  ok('14 tâches affichées', (await page.$$('.trow')).length === 14);
  const rowTxt = await page.evaluate(() => [...document.querySelectorAll('.trow')].find(r => r.dataset.id === 'numerical').textContent);
  ok('ligne numerical : 6 onglets + true/false/cannot say', /6 onglets/.test(rowTxt) && /true \/ false \/ cannot say/.test(rowTxt), rowTxt.replace(/\s+/g, ' ').slice(0, 80));

  await page.evaluate(() => { location.hash = '#/run/numerical'; }); await wait(900);
  const st = await page.evaluate(() => ({
    tabs: [...document.querySelectorAll('.nvt')].map(b => b.textContent),
    actif: (document.querySelector('.nvt.on') || {}).textContent,
    fig: !!document.querySelector('.nv-fig svg, .nv-fig table'),
    boutons: [...document.querySelectorAll('.nvbtn')].map(b => b.textContent),
    timer: (document.querySelector('#qTimer') || {}).textContent,
    nav: document.querySelectorAll('.nvnav').length,
    hud: (document.querySelector('#hud') || {}).textContent.replace(/\s+/g, ' '),
  }));
  ok('6 onglets', st.tabs.length === 6, st.tabs.join(' | '));
  ok('onglet initial = Income (1re question)', st.actif === 'Income', st.actif);
  ok('figure rendue (tableau)', st.fig);
  ok('3 boutons true / false / cannot say', st.boutons.join('/') === 'true/false/cannot say', st.boutons.join('/'));
  ok('chrono global 12:00', /^1[12]:\d\d$/.test(st.timer), st.timer);
  ok('navigation ‹ ▦ ›', st.nav === 3);
  ok('HUD : 1/37', /1\/37/.test(st.hud), st.hud);

  const map = await page.evaluate(() => NUMVERB.ITEMS.map(i => i.tab));
  await page.evaluate(() => { const o = document.querySelector('.nvbtn'); if (o) o.click(); }); await wait(200);
  const seq = [];
  for (let i = 0; i < 37; i++) {
    const s = await page.evaluate(() => ({
      tab: (document.querySelector('.nvt.on') || {}).textContent,
      qno: (document.querySelector('.nv-qno') || {}).textContent,
      stmt: (document.querySelector('.nv-stmt') || {}).textContent.replace(/\s+/g, ' ').slice(0, 60),
      timer: (document.querySelector('#qTimer') || {}).textContent,
    }));
    seq.push(s);
    if (i === 36) break;
    await page.evaluate(() => { const b = document.querySelector('#nvNext'); if (b) b.click(); }); await wait(110);
  }
  const tabNames = ['Income', 'Costs', 'Market shares', 'Employees', 'Return on equity', 'Outlook'];
  const expected = map.map(t => tabNames[['income', 'costs', 'shares', 'employees', 'roe', 'outlook'].indexOf(t)]);
  ok('bascule automatique sur le bon onglet pour les 37 questions', JSON.stringify(seq.map(s => s.tab)) === JSON.stringify(expected));
  ok('compteur de question 1 → 37', seq[0].qno.includes('1 / 37') && seq[36].qno.includes('37 / 37'), seq[36].qno);
  ok('chrono qui décompte', seq[36].timer !== '12:00', seq[0].timer + ' → ' + seq[36].timer);
  ok('énoncés rendus (37 distincts)', new Set(seq.map(s => s.stmt)).size === 37, new Set(seq.map(s => s.stmt)).size + ' énoncés distincts');

  /* l'élève peut consulter un autre onglet ; la question suivante ramène au sien */
  await page.evaluate(() => { [...document.querySelectorAll('.nvt')].find(b => b.textContent === 'Income').click(); }); await wait(300);
  const manual = await page.evaluate(() => (document.querySelector('.nvt.on') || {}).textContent);
  ok('consultation manuelle d’un autre onglet possible', manual === 'Income', manual);
  await page.evaluate(() => { document.querySelector('#nvPrev').click(); }); await wait(300);
  const back = await page.evaluate(() => ({
    tab: (document.querySelector('.nvt.on') || {}).textContent,
    q: (document.querySelector('.nv-qno') || {}).textContent,
    attendu: NUMVERB.tabOf(NUMVERB.ITEMS[35].tab).short,
  }));
  ok('la question affichée ramène à son propre onglet', back.tab === back.attendu && /36 \/ 37/.test(back.q), back.q + ' → ' + back.tab);
  await page.evaluate(() => { document.querySelector('#nvNext').click(); }); await wait(250);

  await page.evaluate(() => { const b = document.querySelector('#nvNext'); if (b) b.click(); }); await wait(900);
  const sum = await page.evaluate(() => ({
    score: !!document.querySelector('.scorebig'),
    rows: document.querySelectorAll('.qtbl2 tbody tr').length,
    tabs: document.querySelectorAll('.qtbl2 .tabtag').length,
  }));
  ok('résumé affiché', sum.score);
  ok('37 lignes de détail', sum.rows === 37, sum.rows + ' lignes');
  ok('onglet indiqué sur chaque ligne', sum.tabs === 37, sum.tabs + ' étiquettes');

  const att = await page.evaluate(() => CORE.P.attempts().slice(-1)[0]);
  ok('tentative horodatée', !!att.date && !!att.time && att.section === 'numerical', att.date + ' ' + att.time + ' · ' + att.section);
  await page.evaluate(() => { location.hash = '#/run/numericalMCQ?paper=B'; }); await wait(800);
  const mcq = await page.evaluate(() => !!document.querySelector('#opts .opt'));
  ok('variante QCM classique toujours disponible', mcq);

  console.log(out.join('\n'));
  console.log('\nerreurs JS :', errs.length ? errs.slice(0, 4) : 'aucune');
  console.log('\n' + (ko === 0 && errs.length === 0 ? '🎉 NUMERICAL FORMAT RÉEL : TOUT OK' : '⚠ ' + ko + ' échec(s)'));
  await browser.close();
  process.exit(ko || errs.length ? 1 : 0);
})().catch(e => { console.error('FAIL', e.message); process.exit(1); });
