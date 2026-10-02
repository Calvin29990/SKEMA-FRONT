/* Captures : page de la tâche numerical (bloc Contenu) et session issue d'un fichier perso */
const puppeteer = require('puppeteer-core');
const path = require('path');
const wait = ms => new Promise(r => setTimeout(r, ms));
const FIX = (n) => path.join(__dirname, 'fixtures', n);

(async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--hide-scrollbars'],
    executablePath: '/tmp/chromium', headless: 'shell',
  });
  const ctx = await browser.createBrowserContext();
  const page = await ctx.newPage();
  page.on('dialog', d => d.accept());
  await page.setViewport({ width: 1280, height: 1000, deviceScaleFactor: 1.4 });
  await page.goto('http://127.0.0.1:8080/', { waitUntil: 'networkidle2' });
  await page.evaluate(() => localStorage.clear());
  await page.reload({ waitUntil: 'networkidle2' });
  await page.type('#lgCode', 'CM2026'); await page.type('#lgName', 'Calvin'); await page.click('#lgGo');
  await wait(700);

  /* page de la tâche, banque intégrée */
  await page.evaluate(() => { location.hash = '#/section/numerical'; }); await wait(700);
  await page.screenshot({ path: '/home/user/apercu/perso-1-section.png' });

  /* fichier perso chargé */
  await (await page.$('#nvFileOpen')).click(); await wait(300);
  await (await page.$('input[type=file]')).uploadFile(FIX('perso-test.json')); await wait(800);
  await page.screenshot({ path: '/home/user/apercu/perso-2-charge.png' });

  /* session issue du fichier : onglets et énoncés du fichier, chrono de sa durée */
  await page.evaluate(() => { location.hash = '#/run/numerical'; }); await wait(900);
  await page.screenshot({ path: '/home/user/apercu/perso-3-session.png' });

  /* grille d'ensemble */
  await page.evaluate(() => { document.querySelector('#nvGrid').click(); }); await wait(400);
  await page.screenshot({ path: '/home/user/apercu/perso-4-grille.png' });

  /* gestion des profils : suppression d'un profil et de son historique */
  await page.evaluate(() => { document.querySelector('#nvClose').click(); location.hash = '#/'; }); await wait(600);
  await page.evaluate(() => {
    CORE.PROFILES.set('Soeur');
    CORE.P.add({ id: 'S1', at: new Date().toISOString(), date: '01/01/2026', time: '10:00:00', user: 'Soeur', section: 'verbal',
                 items: 1, answered: 1, correct: 1, wrong: 0, skipped: 0, accuracy: 1, avgMs: 900, ms: 900, paper: null, mode: 'immediate' }, []);
    CORE.P.PROFILES.set('Calvin');
    document.querySelector('#userBtn').click();
  });
  await wait(500);
  await page.screenshot({ path: '/home/user/apercu/perso-5-profils.png' });

  await browser.close();
  console.log('captures ok');
})().catch(e => { console.error('FAIL', e.message); process.exit(1); });
