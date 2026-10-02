/* Les deux nouvelles épreuves : anglais (3 sections / 10 min / « ? ») et motivation (blocs de 3, 6 points) */
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

  /* ── les deux sections sont proposées ── */
  const liste = await page.evaluate(() => CORE.SECTIONS.map(s => s.id + ':' + s.mode).join(' '));
  ok('section English proposée (mode QCM)', /english:mc/.test(liste), liste.match(/english:\w+/)[0]);
  ok('section Motivation en mode blocs', /motivation:block/.test(liste), liste.match(/motivation:\w+/)[0]);

  /* ── ANGLAIS ── */
  await page.evaluate(() => { location.hash = '#/section/english'; }); await wait(500);
  await page.evaluate(() => { document.querySelector('#startBtn').click(); }); await wait(700);
  const e1 = await page.evaluate(() => {
    const b = document.querySelector('#qbody');
    return { inter: !!b.querySelector('.inter'), titre: (b.querySelector('.inter-k') || {}).textContent,
             sous: (b.querySelector('.qtext') || {}).textContent,
             chrono: (document.querySelector('#qTimer') || {}).textContent,
             bouton: (document.querySelector('#goSec') || {}).textContent };
  });
  ok('section 1 : intertitre avant les exemples', e1.inter && /Section 1 \/ 3/.test(e1.titre), e1.titre + ' · ' + e1.bouton);
  ok('la consigne annonce 2 exemples puis 10 phrases', /2 exemples, puis 10 phrases/.test(e1.sous || ''), e1.sous);

  await page.evaluate(() => document.querySelector('#goSec').click()); await wait(400);
  const ex = await page.evaluate(() => {
    const b = document.querySelector('#qbody');
    return { bandeau: (b.querySelector('.qex') || {}).textContent,
             options: [...b.querySelectorAll('.opt')].map(o => o.textContent.replace(/\d$/, '').trim()),
             ph: (b.querySelector('.qtext') || {}).textContent };
  });
  ok('exemple signalé par un bandeau', /EXEMPLE/.test(ex.bandeau || ''), (ex.bandeau || '').slice(0, 28));
  ok('4 options + l’option « ? »', ex.options.length === 5 && ex.options[4].includes('?'), ex.options.join(' | '));
  ok('phrase à trous', /_{3,}/.test(ex.ph || ''), ex.ph.slice(0, 58) + '…');

  /* répondre mal à l'exemple : il ne doit pas compter */
  await page.evaluate(() => { document.querySelectorAll('.opt')[0].click(); document.querySelector('#okBtn').click(); });
  await wait(400);
  const apresEx = await page.evaluate(() => ({ hud: document.querySelector('#hud').textContent, fb: !!document.querySelector('.fb') }));
  ok('l’exemple ne compte pas dans le score', /✔ 0/.test(apresEx.hud) && /✘ 0/.test(apresEx.hud), apresEx.hud.replace(/\s+/g, ' ').slice(0, 60));

  /* passer au 2e exemple, y répondre, puis avancer vers la 1re question */
  await page.evaluate(() => { const b = document.querySelector('#nextBtn'); if (b) b.click(); }); await wait(350);
  await page.evaluate(() => { document.querySelectorAll('.opt')[0].click(); document.querySelector('#okBtn').click(); }); await wait(400);
  await page.evaluate(() => { const b = document.querySelector('#nextBtn'); if (b) b.click(); }); await wait(400);
  const q1 = await page.evaluate(() => ({ qex: !!document.querySelector('.qex'), n: document.querySelectorAll('.opt').length }));
  ok('après les 2 exemples, question normale (sans bandeau)', !q1.qex && q1.n === 5, (q1.n) + ' options');

  /* l'option « ? » est enregistrée comme telle */
  await page.evaluate(() => { document.querySelectorAll('.opt')[4].click(); document.querySelector('#okBtn').click(); }); await wait(500);
  const rep = await page.evaluate(() => ({
    hud: document.querySelector('#hud').textContent.replace(/\s+/g, ' '),
    fb: (document.querySelector('.fb') || {}).textContent || '',
    marque: [...document.querySelectorAll('.opt')].some(o => o.classList.contains('ko')),
  }));
  ok('cliquer « ? » enregistre « je ne sais pas »', /✘ 1/.test(rep.hud) && rep.marque, rep.hud.slice(0, 44) + ' · option marquée : ' + rep.marque);

  /* ── MOTIVATION ── */
  await page.evaluate(() => { location.hash = '#/run/motivation?t=0'; }); await wait(300);
  await page.evaluate(() => { location.hash = '#/section/motivation'; }); await wait(500);
  await page.evaluate(() => { document.querySelector('#startBtn').click(); }); await wait(700);
  const m1 = await page.evaluate(() => {
    const b = document.querySelector('#qbody');
    return { lignes: b.querySelectorAll('.blk-row').length, affirmations: [...b.querySelectorAll('.blk-t')].map(x => x.textContent.slice(0, 34)),
             points: b.querySelectorAll('.blk-row .dot').length,
             restants: (document.querySelector('#blkRest') || {}).textContent,
             chrono: (document.querySelector('#qTimer') || {}).textContent,
             valider: document.querySelector('#okBtn').disabled };
  });
  ok('bloc de 3 affirmations', m1.lignes === 3 && m1.points === 21, m1.lignes + ' affirmations · ' + m1.points + ' points cliquables');
  ok('pas de limite de temps (chrono neutralisé)', m1.chrono === '—', 'chrono = ' + m1.chrono);
  ok('validation impossible sans point distribué', m1.valider === true, 'bouton ' + (m1.valider ? 'désactivé' : 'actif'));

  /* distribuer 4 points puis tenter 4 de plus : impossible, plafond 6 */
  const bloc = await page.evaluate(() => {
    const clic = (row, val) => document.querySelectorAll('.blk-row')[row].querySelectorAll('.dot')[val].click();
    clic(0, 4);                       /* 4 points sur la 1re */
    const apres4 = document.querySelector('#blkRest').textContent;
    clic(1, 4);                       /* 8 > 6 : doit être refusé */
    const apres8 = document.querySelector('#blkRest').textContent;
    clic(1, 2);                       /* 4 + 2 = 6 : accepté */
    return { apres4, apres8, final: document.querySelector('#blkRest').textContent,
             somme: [...document.querySelectorAll('.blk-row')].map(r => {
               const on = [...r.querySelectorAll('.dot')].findIndex(d => d.classList.contains('on'));
               return [...r.querySelectorAll('.dot')].findIndex(d => d.classList.contains('on'));
             }) };
  });
  ok('plafond de 6 points respecté', bloc.apres4 === '2' && bloc.apres8 === '2' && bloc.final === '0',
     '4 pts → reste ' + bloc.apres4 + ' · +4 refusé → reste ' + bloc.apres8 + ' · +2 → reste ' + bloc.final);
  ok('répartition lisible (4 + 2 + 0)', bloc.somme.join('+') === '4+2+0', 'points par affirmation : ' + bloc.somme.join(' + '));

  await page.evaluate(() => document.querySelector('#okBtn').click()); await wait(500);
  const m2 = await page.evaluate(() => ({ hud: document.querySelector('#hud').textContent,
    reste: (document.querySelector('#blkRest') || {}).textContent,
    bloc: document.querySelector('#hud .pill.mono').textContent }));
  ok('le bloc est enregistré et le suivant s’affiche', /2\/36/.test(m2.bloc) && m2.reste === '6',
     m2.bloc + ' · points remis à ' + m2.reste);

  /* aucune minuterie par item : attendre 13 s ne doit pas soumettre */
  const avant = await page.evaluate(() => document.querySelector('#hud .pill.mono').textContent);
  await wait(13000);
  const apres = await page.evaluate(() => document.querySelector('#hud .pill.mono').textContent);
  ok('aucune soumission automatique sur un bloc', avant === apres, avant + ' → ' + apres + ' après 13 s');

  ok('aucune erreur JS', errs.length === 0, errs.slice(0, 2).join(' · '));

  console.log(out.join('\n'));
  console.log('\n' + (ko === 0 && !errs.length ? '🎉 ANGLAIS + MOTIVATION : TOUT OK' : '⚠ ' + ko + ' échec(s)'));
  await browser.close();
  process.exit(ko || errs.length ? 1 : 0);
})().catch(e => { console.error('FAIL', e.message); process.exit(1); });
