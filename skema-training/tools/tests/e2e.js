/* Non-régression complète : accès, numerical réel, verbal, feedback, progression, i18n, livrables */
const puppeteer = require('puppeteer-core');
const out = []; let ko = 0;
const ok = (l, c, x = '') => { out.push((c ? '✅' : '❌') + ' ' + l + (x ? ' — ' + x : '')); if (!c) ko++; return c; };
const wait = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files'],
    executablePath: '/tmp/chromium', headless: 'shell', defaultViewport: { width: 1366, height: 1000 },
  });
  const ctx = await browser.createBrowserContext();
  const page = await ctx.newPage();
  const errs = [];
  page.on('pageerror', e => errs.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !/net::|ERR_CONNECTION_CLOSED/.test(m.text())) errs.push('console: ' + m.text()); });
  page.on('dialog', async d => { await d.accept(); });

  /* ── accès : code PUIS prénom ── */
  await page.goto('http://127.0.0.1:8080/', { waitUntil: 'networkidle2' });
  await page.evaluate(() => localStorage.clear());
  await page.reload({ waitUntil: 'networkidle2' });
  ok('écran d’accès : code + prénom', await page.$('#lgCode') !== null && await page.$('#lgName') !== null);
  await page.type('#lgCode', 'MAUVAIS'); await page.type('#lgName', 'Calvin'); await page.click('#lgGo'); await wait(300);
  const refuse = await page.evaluate(() => ({ ov: !!document.querySelector('#loginOverlay'), err: (document.querySelector('#lgErr') || {}).textContent || '' }));
  ok('code erroné refusé, message affiché', refuse.ov && /incorrect/i.test(refuse.err), refuse.err.trim());
  await page.evaluate(() => { document.querySelector('#lgCode').value = ''; });
  await page.type('#lgCode', 'CM2026'); await page.click('#lgGo'); await wait(700);
  const acc = await page.evaluate(() => ({
    gone: document.querySelector('#loginOverlay') === null,
    rows: document.querySelectorAll('.trow').length,
    mcq: !!document.querySelector('[data-id="numericalMCQ"]'),
    profil: (document.querySelector('#userName') || {}).textContent || '',
  }));
  ok('accès CM2026 accepté, profils séparés', acc.gone && acc.profil.trim() === 'Calvin', 'profil « ' + acc.profil.trim() + ' »');
  ok('accueil : 15 tâches', acc.rows === 15, acc.rows + ' lignes');
  ok('variante QCM masquée de l’accueil (format réel imposé)', !acc.mcq);

  /* ── bug gris : jamais de voile modal bloquant ── */
  const veil = await page.evaluate(() => {
    const m = document.querySelector('.modal-back[hidden]');
    return { present: !!m, display: m ? getComputedStyle(m).display : 'n/a' };
  });
  ok('voile modal invisible = display:none', !veil.present || veil.display === 'none', veil.display);

  /* ── numerical au format réel ── */
  await page.evaluate(() => { location.hash = '#/run/numerical'; }); await wait(900);
  const nv = await page.evaluate(() => ({
    tabs: document.querySelectorAll('.nvt').length,
    btns: [...document.querySelectorAll('.nvbtn')].map(b => b.textContent).join('/'),
    timer: (document.querySelector('#qTimer') || {}).textContent,
    nav: document.querySelectorAll('.nvnav').length,
    total: NUMVERB.ITEMS.length,
  }));
  ok('numerical : 6 onglets, 37 énoncés', nv.tabs === 6 && nv.total === 37, nv.tabs + ' onglets · ' + nv.total + ' items');
  ok('numerical : true / false / cannot say', nv.btns === 'true/false/cannot say', nv.btns);
  ok('numerical : chrono global 12:00', /^1[12]:\d\d$/.test(nv.timer), nv.timer);
  ok('numerical : navigation ‹ ▦ ›', nv.nav === 3);
  const seq = await page.evaluate(async () => {
    const r = [];
    for (let i = 0; i < 9; i++) {
      r.push((document.querySelector('.nvt.on') || {}).textContent);
      const b = document.querySelector('.nvbtn'); if (b) b.click();
      const n = document.querySelector('#nvNext'); if (n) n.click();
      await new Promise(s => setTimeout(s, 60));
    }
    return r;
  });
  const attendu = await page.evaluate(() => NUMVERB.ITEMS.slice(0, 9).map(i => NUMVERB.tabOf(i.tab).short));
  ok('numerical : bascule automatique d’onglet à chaque question', JSON.stringify(seq) === JSON.stringify(attendu), seq.join(' → '));
  const manuel = await page.evaluate(async () => {
    const sleep = ms => new Promise(r => setTimeout(r, ms));
    [...document.querySelectorAll('.nvt')].find(b => /Outlook/.test(b.textContent)).click();
    await sleep(200);
    const consult = (document.querySelector('.nvt.on') || {}).textContent;
    document.querySelector('#nvNext').click();
    await sleep(250);
    const qno = (document.querySelector('.nv-qno') || {}).textContent.match(/(\d+) \/ 37/);
    const tab = NUMVERB.tabOf(NUMVERB.ITEMS[+qno[1] - 1].tab).short;
    return { consult, after: (document.querySelector('.nvt.on') || {}).textContent, att: tab, qno: qno[0] };
  });
  ok('onglet consultable à la main, retour auto à la question suivante', manuel.consult === 'Outlook' && manuel.after === manuel.att,
     'consultation « ' + manuel.consult + ' » puis ' + manuel.qno + ' → ' + manuel.after);
  const t2 = await page.evaluate(() => (document.querySelector('#qTimer') || {}).textContent);
  await wait(1200);
  const t3 = await page.evaluate(() => (document.querySelector('#qTimer') || {}).textContent);
  ok('numerical : le chrono décompte (jamais remis à 12:00)', t3 !== '12:00' && t3 !== t2, t2 + ' → ' + t3);
  const nvSum = await page.evaluate(async () => {
    for (let i = 0; i < 40; i++) { const b = document.querySelector('#nvNext'); if (b) b.click(); await new Promise(s => setTimeout(s, 25)); }
    await new Promise(s => setTimeout(s, 700));
    return { rows: document.querySelectorAll('.qtbl2 tbody tr').length, tabs: document.querySelectorAll('.qtbl2 .tabtag').length, score: !!document.querySelector('.scorebig') };
  });
  ok('numerical : résumé 37 lignes + onglet de chaque question', nvSum.rows === 37 && nvSum.tabs === 37 && nvSum.score, nvSum.rows + ' lignes / ' + nvSum.tabs + ' étiquettes');

  /* ── variante QCM par l'URL ── */
  await page.evaluate(() => { location.hash = '#/run/numericalMCQ?paper=B'; }); await wait(700);
  const mcq = await page.evaluate(() => ({ opts: document.querySelectorAll('#opts .opt').length, ok: !!document.querySelector('#okBtn') }));
  ok('variante QCM (Paper B) accessible par l’URL', mcq.opts >= 3 && mcq.ok, mcq.opts + ' options');

  /* ── verbal + feedback immédiat ── */
  await page.evaluate(() => { location.hash = '#/'; }); await wait(500);
  await page.evaluate(() => { const r = [...document.querySelectorAll('.trow')].find(x => x.dataset.id === 'verbal'); r.querySelector('.tstart').click(); }); await wait(800);
  const v1 = await page.evaluate(() => ({
    passage: !!document.querySelector('.qpassage'),
    opts: [...document.querySelectorAll('#opts .opt')].map(o => o.textContent.replace(/\s+/g, ' ').trim()),
    hud: (document.querySelector('#hud') || {}).textContent.replace(/\s+/g, ' '),
  }));
  ok('verbal : passage + options True/False/Cannot say', v1.passage && v1.opts.length === 3, v1.opts.join(' | '));
  ok('verbal : compteur HUD', /(?:Item|Ítem)\s*1\//.test(v1.hud), v1.hud);
  const fb = await page.evaluate(async () => {
    document.querySelector('#opts .opt').click();
    await new Promise(s => setTimeout(s, 120));
    document.querySelector('#okBtn').click();
    await new Promise(s => setTimeout(s, 350));
    return { fb: !!document.querySelector('.fb'), why: (document.querySelector('.fb') || {}).textContent.length > 10 };
  });
  ok('verbal : correction immédiate expliquée', fb.fb && fb.why, 'feedback + méthode');
  await page.evaluate(() => document.querySelector('#nextBtn').click()); await wait(400);
  const v2 = await page.evaluate(() => (document.querySelector('#hud') || {}).textContent.replace(/\s+/g, ' '));
  ok('verbal : passage à l’item suivant', /(?:Item|Ítem)\s*2\//.test(v2), v2);

  /* ── résumé + détail + CSV + horodatage ── */
  await page.evaluate(() => document.querySelector('#btnQuit').click()); await wait(900);
  const sum2 = await page.evaluate(() => ({
    score: !!document.querySelector('.scorebig'),
    detail: document.querySelectorAll('.qtbl2 tbody tr').length,
    date: document.body.textContent.replace(/\s+/g, ' ').match(/\d{2}\/\d{2}\/\d{4}(\s+\d{2}:\d{2})?/),
  }));
  ok('résumé de session affiché', sum2.score);
  ok('détail question par question', sum2.detail >= 1, sum2.detail + ' ligne(s)');
  ok('tentative horodatée (jour + heure)', !!sum2.date, sum2.date ? sum2.date[0] : 'introuvable');
  const stamp = await page.evaluate(() => { const a = CORE.P.attempts().slice(-1)[0]; return a.date + ' ' + a.time; });
  ok('horodatage complet dans la tentative', /^\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}:\d{2}$/.test(stamp), stamp);
  const csv = await page.evaluate(async () => {
    const a = CORE.P.attempts().slice(-1)[0];
    const orig = URL.createObjectURL, oc = HTMLAnchorElement.prototype.click;
    let cap = null; URL.createObjectURL = b => { cap = b; return 'blob:x'; }; HTMLAnchorElement.prototype.click = function () { };
    try { CORE.P.csv(a.id); } catch (e) { return 'ERR ' + e.message; }
    URL.createObjectURL = orig; HTMLAnchorElement.prototype.click = oc;
    return cap ? (await cap.text()) : null;
  });
  ok('export CSV : en-tête complet', typeof csv === 'string' && /"Profil";"Session";"Date";"Heure";"Section";"N°";"Question"/.test(csv), typeof csv === 'string' ? csv.split('\r\n')[0].slice(0, 60) : String(csv));
  const att = await page.evaluate(() => {
    const a = CORE.P.attempts().slice(-1)[0];
    return { date: a.date, time: a.time, user: a.user, section: a.section, det: CORE.P.sessionLog(a.id).length };
  });
  ok('profil + date/heure + détail conservés', !!att.date && !!att.time && att.user === 'Calvin' && att.det > 0, att.date + ' ' + att.time + ' · ' + att.section + ' · ' + att.det + ' détails');

  /* ── progression + persistance ── */
  await page.evaluate(() => { location.hash = '#/progression'; }); await wait(700);
  const prog = await page.evaluate(() => ({ rows: document.querySelectorAll('#view [data-det]').length }));
  ok('vue Progression : sessions listées', prog.rows >= 1, prog.rows + ' session(s)');
  await page.evaluate(() => { location.hash = '#/'; });
  await page.reload({ waitUntil: 'networkidle2' }); await wait(900);
  const persist = await page.evaluate(() => ({
    gate: document.querySelector('#loginOverlay') === null,
    rows: document.querySelectorAll('.trow').length,
    n: CORE.P.attempts().length,
    profil: (document.querySelector('#userName') || {}).textContent || '',
  }));
  ok('rechargement : profil + historique conservés', persist.gate && persist.rows === 15 && persist.n >= 1, persist.profil + ' · ' + persist.n + ' tentative(s)');

  /* ── profils : plateforme pour une seule personne, suppression complète ── */
  const profils = await page.evaluate(async () => {
    const sleep = ms => new Promise(r => setTimeout(r, ms));
    CORE.PROFILES.set('Profil2');
    CORE.P.add({ id: 'TEST' + Date.now(), at: new Date().toISOString(), date: '01/01/2026', time: '10:00:00',
                 user: 'Profil2', section: 'verbal', items: 1, answered: 1, correct: 1, wrong: 0, skipped: 0,
                 accuracy: 1, avgMs: 1000, ms: 1000, paper: null, mode: 'immediate' }, []);
    CORE.P.PROFILES.set('Calvin');
    document.querySelector('#userBtn').click();
    await sleep(300);
    const avant = [...document.querySelectorAll('[data-del]')].map(b => b.dataset.del);
    const n = document.querySelector('[data-del="Profil2"]');
    if (n) n.click();
    await sleep(400);
    const apres = CORE.P.PROFILES.list();
    return { avant, apres, hist: U.store.get('attempts::Profil2', null) };
  });
  ok('deuxième profil visible et supprimable', profils.avant.includes('Profil2'), profils.avant.join(', '));
  ok('suppression : profil ET historique effacés', !profils.apres.includes('Profil2') && profils.hist == null, 'profils restants : ' + profils.apres.join(', '));

  /* ── multilingue ── */
  const langTest = async (lg, attendu) => {
    await page.evaluate(l => { CORE.P.saveSettings(Object.assign(CORE.P.settings(), { langUI: l })); location.reload(); }, lg);
    await wait(1000);
    const txt = await page.evaluate(() => document.body.textContent.replace(/\s+/g, ' '));
    return new RegExp(attendu).test(txt);
  };
  ok('anglais : interface traduite', await langTest('en', 'Home|Tasks to complete|Settings'));
  ok('espagnol : interface traduite', await langTest('es', 'Progreso|Tareas|Ajustes|Inicio'));
  ok('portugais : interface traduite', await langTest('pt', 'Progresso|Tarefas|Ajustes|Início'));
  ok('retour au français', await langTest('fr', 'Accueil|Tâches|Progression'));

  /* ── thème sombre ── */
  const dark = await page.evaluate(async () => {
    document.querySelector('#themeSw').click();
    await new Promise(s => setTimeout(s, 250));
    const on = document.documentElement.getAttribute('data-theme') === 'dark' || document.body.classList.contains('dark');
    document.querySelector('#themeSw').click();
    await new Promise(s => setTimeout(s, 250));
    const off = document.documentElement.getAttribute('data-theme') !== 'dark';
    return { on, off };
  });
  ok('thème sombre activable puis réversible', dark.on && dark.off);

  /* ── livrables publiés ── */
  const stand = await ctx.newPage();
  await stand.goto('http://127.0.0.1:8080/standalone/index.html', { waitUntil: 'networkidle2' });
  const st = await stand.evaluate(() => ({
    app: document.querySelectorAll('.trow').length,
    scripts: document.querySelectorAll('script[src]').length,
    locaux: [...document.querySelectorAll('script[src],link[rel=stylesheet]')].filter(e => /^(assets|\.\.?\/)/.test(e.getAttribute('src') || e.getAttribute('href') || '')).length,
    externes: [...document.querySelectorAll('link[href^="http"],script[src^="http"]')].length,
  }));
  ok('version standalone : fichier unique, aucune ressource externe', st.app === 15 && st.scripts === 0 && st.locaux === 0 && st.externes === 0, st.app + ' tâches · ' + st.scripts + ' script externe · ' + st.externes + ' ressource externe');
  const docs = await ctx.newPage();
  await docs.goto('file:///home/user/SKEMA-FRONT/docs/index.html', { waitUntil: 'networkidle2' });
  await wait(800);
  const dc = await docs.evaluate(() => ({
    gate: !!document.querySelector('#lgCode'),
    fig: typeof NUMVERB !== 'undefined' ? NUMVERB.ITEMS.length : 0,
    perso: typeof NUMVERB !== 'undefined' ? NUMVERB.isPerso() : true,
  }));
  ok('copie docs opérationnelle (accès + numerique réel, sans contenu perso)', dc.gate && dc.fig === 37 && !dc.perso, dc.fig + ' énoncés intégrés');

  console.log(out.join('\n'));
  console.log('\nerreurs JS :', errs.length ? errs.slice(0, 5) : 'aucune');
  console.log('\n' + (ko === 0 && errs.length === 0 ? '🎉 NON-RÉGRESSION : TOUT OK (' + out.length + ' vérifications)' : '⚠ ' + ko + ' échec(s) sur ' + out.length));
  await browser.close();
  process.exit(ko || errs.length ? 1 : 0);
})().catch(e => { console.error('FAIL', e.message); process.exit(1); });
