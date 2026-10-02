/* Examen blanc : 3 épreuves tirées au hasard, enchaînées, comme le jour J */
const puppeteer = require('puppeteer-core');
const out = []; let ko = 0;
const ok = (l, c, x = '') => { out.push((c ? '✅' : '❌') + ' ' + l + (x ? ' — ' + x : '')); if (!c) ko++; return c; };
const wait = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--hide-scrollbars'],
    executablePath: '/tmp/chromium', headless: 'shell', defaultViewport: { width: 1366, height: 1000 },
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

  const carte = await page.evaluate(() => {
    const r = document.querySelector('[data-id="_exam3"]');
    return r ? { txt: r.textContent.replace(/\s+/g, ' ').slice(0, 80), bouton: !!r.querySelector('.tstart') } : null;
  });
  ok('carte « Examen blanc » sur l’accueil', !!carte && carte.bouton, carte ? carte.txt : 'absente');

  /* lancer via le bouton de la carte */
  await page.evaluate(() => document.querySelector('[data-id="_exam3"] .tstart').click());
  await wait(900);
  const s1 = await page.evaluate(() => {
    const S = CORE.current;
    return {
      hash: location.hash.replace(/[?].*/, ''),
      ep: S.items.filter(i => i.ex).map(i => i.title),
      sections: [...new Set(S.items.map(i => i.secId).filter(Boolean))],
      total: S.items.length,
      hud: document.querySelector('#hud .pill').textContent.replace(/\s+/g, ' ').trim(),
      entete: document.querySelector('.runner .qtext, #qbody .inter-k').textContent.trim(),
      chrono: !!document.querySelector('#qTimer'),
    };
  });
  ok('3 épreuves tirées', s1.ep.length === 3 && s1.sections.length === 3, s1.ep.join(' · '));
  ok('chaque épreuve est annoncée', /^ÉPREUVE 1 \/ 3 — /.test(s1.ep[0]), s1.entete);
  const attendu = s1.ep[0].replace(/^ÉPREUVE 1 \/ 3 — /, '');
  ok('la barre du haut affiche l’épreuve en cours', s1.hud.replace('Section', '').trim() === attendu, s1.hud + ' (attendu : ' + attendu + ')');
  ok('aucun retour en arrière sur le tirage', s1.total > 20, s1.total + ' items au total');

  /* avancer jusqu'à la 2e épreuve */
  await page.evaluate(() => document.querySelector('#goSec').click()); await wait(400);
  const tirage2 = await page.evaluate(() => {
    /* on passe les items avec le bouton « Passer » jusqu'à l'épreuve 2 */
    return new Promise(done => {
      let n = 0;
      const pas = () => {
        const S = CORE.current;
        const it = S.items[S.i];
        if (!it || (it.ex && /ÉPREUVE 2 \/ 3/.test(it.title))) {
          return done({ titre: it ? it.title : '(fin)', hud: (document.querySelector('#hud .pill') || {}).textContent || '' });
        }
        if (n++ > 90) return done({ titre: 'trop long', hud: '' });
        const b = document.querySelector('#btnSkip');
        if (b) b.click(); else document.querySelector('.opt').click();
        setTimeout(pas, 20);
      };
      pas();
    });
  });
  ok('l’épreuve 2 s’enchaîne automatiquement', /ÉPREUVE 2 \/ 3 — /.test(tirage2.titre), tirage2.titre + ' · barre : ' + tirage2.hud);

  /* le tirage change d'une session à l'autre */
  const tirages = await page.evaluate(() => {
    const set = new Set();
    for (let i = 0; i < 12; i++) set.add(CORE.buildExam3({ seed: i * 7919 }).filter(x => x.ex).map(x => x.title).join('|'));
    return { distincts: set.size, exemple: [...set][0] };
  });
  ok('le tirage change selon la session', tirages.distincts >= 8, tirages.distincts + ' combinaisons différentes sur 12 tirages');

  /* le journal rattache chaque item à sa vraie épreuve (journal en mémoire) */
  const log = await page.evaluate(() => {
    const S = CORE.current, l = S.log || [];
    const cur = S.items[S.i] || {};
    return { n: l.length, dernier: [...new Set(l.slice(-4).map(x => x.section))], courante: cur.secId, total: [...new Set(S.items.map(i => i.secId).filter(Boolean))].length };
  });
  ok('chaque question est rattachée à sa vraie épreuve',
     log.n > 0 && log.dernier.length === 1 && log.dernier[0] !== log.courante && log.total === 3,
     log.n + ' réponses rattachées à « ' + log.dernier.join(',') + ' » puis passage à « ' + log.courante + ' » · 3 épreuves distinctes');

  ok('aucune erreur JS', errs.length === 0, errs.slice(0, 2).join(' · '));

  console.log(out.join('\n'));
  console.log('\n' + (ko === 0 && !errs.length ? '🎉 EXAMEN BLANC (3 ÉPREUVES AU HASARD) : TOUT OK' : '⚠ ' + ko + ' échec(s)'));
  await browser.close();
  process.exit(ko || errs.length ? 1 : 0);
})().catch(e => { console.error('FAIL', e.stack); process.exit(1); });
