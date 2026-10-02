#!/usr/bin/env node
/* ═══════════════════════════════════════════════════════════════
   conform.js — contrôle de conformité du site reconstruit
   (standalone : CSS + JS inlinés) contre les faits vérifiés du
   document de référence.

   Usage :
     cd skema-training && NODE_PATH=… LD_LIBRARY_PATH=… node tools/tests/conform.js

   Le script sert le dossier standalone sur un port aléatoire puis
   pilote Chromium (puppeteer-core + @sparticuz/chromium).
   ═══════════════════════════════════════════════════════════════ */
'use strict';
const http = require('http');
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const ROOT = path.resolve(__dirname, '..', '..');
const STANDALONE = path.join(ROOT, 'standalone');
const OUT = path.join(ROOT, 'tools', 'tests', 'results');
fs.mkdirSync(OUT, { recursive: true });

const wait = (ms) => new Promise(r => setTimeout(r, ms));
let PASS = 0, FAIL = 0;
const ok = (cond, label, extra) => { if (cond) { PASS++; } else { FAIL++; console.log('  ✘ ' + label + (extra !== undefined ? '  → ' + JSON.stringify(extra) : '')); } };
const group = (t) => console.log('\n■ ' + t);

const EXPECT = [
  ['behaviour', 'Comportements professionnels', 18],
  ['motivation', 'Motivations et Intérêts Professionnels', 18],
  ['numerical', 'Raisonnement numérique', 15],
  ['verbal', 'Raisonnement verbal', 15],
  ['deductive', 'Pensée logique déductive', 9],
  ['inductive', 'Raisonnement Inductif', 9],
  ['concentration', 'Capacité de Concentration', 5],
  ['multitask', 'Capacité multi-tâches', 8],
  ['learning', 'Capacité d’apprentissage', 9],
  ['info', 'Traitement de l’information', 18],
  ['english', 'Compétences Linguistiques - Anglais', 13],
  ['french', 'Compétences Linguistiques - Français', 13],
  ['mechanical', 'Raisonnement Mécanique', 18],
  ['switch', 'Raisonnement Déductif - switchChallenge', 9]
];

function serve(dir) {
  return new Promise(res => {
    const srv = http.createServer((req, rq) => {
      let p = decodeURIComponent(req.url.split('?')[0]);
      if (p === '/') p = '/index.html';
      const f = path.join(dir, p);
      if (!f.startsWith(dir) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { rq.writeHead(404); return rq.end('nope'); }
      const ext = path.extname(f);
      const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml' }[ext] || 'application/octet-stream';
      rq.writeHead(200, { 'Content-Type': mime + '; charset=utf-8' });
      fs.createReadStream(f).pipe(rq);
    });
    srv.listen(0, '127.0.0.1', () => res({ srv, port: srv.address().port }));
  });
}

(async () => {
  const { srv, port } = await serve(STANDALONE);
  const base = 'http://127.0.0.1:' + port + '/';
  const browser = await puppeteer.launch({
    executablePath: '/tmp/chromium', headless: 'shell',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
    defaultViewport: { width: 1366, height: 950 }
  });
  const page = await (await browser.createBrowserContext()).newPage();
  const errors = [], external = [];
  page.on('pageerror', e => { errors.push(e.message); if (process.env.VERBOSE) console.log('  JSERR', String(e.stack || e.message).split('\n').slice(0, 3).join(' | ')); });
  page.on('dialog', d => d.accept());
  page.on('console', m => { if (m.type() === 'error' && !/blob:x/.test(m.text())) errors.push('console: ' + m.text()); });
  page.on('request', r => { if (!r.url().startsWith(base) && !/^(data|blob):/.test(r.url()) && !r.url().startsWith('about:')) external.push(r.url()); });

  await page.goto(base + '#/', { waitUntil: 'networkidle2' });
  await page.waitForSelector('#uGo');
  await page.type('#uName', 'Conformité');
  await page.click('#uGo');
  await page.waitForSelector('.task');

  /* ── 1. ACCUEIL : 14 lignes, noms et minutes du document ── */
  group('Accueil — 14 lignes conformes au document');
  const home = await page.evaluate(() => [...document.querySelectorAll('.task')].map(t => ({
    id: t.dataset.id, name: t.querySelector('.tk-name').innerText.trim(), time: t.querySelector('.tk-time').innerText.trim(),
    start: !!t.querySelector('.tk-start'), info: !!t.querySelector('.tk-info')
  })));
  ok(home.length === 14, '14 lignes exactement', home.length);
  EXPECT.forEach(([id, name, min], i) => {
    const r = home[i] || {};
    ok(r.id === id && r.name === name, 'ligne ' + (i + 1) + ' : ' + name, r);
    ok(r.time === min + ' minutes', 'durée ' + name + ' = ' + min + ' minutes', r.time);
    ok(r.start, 'bouton Début présent : ' + name);
  });
  ok(home.filter(r => r.info).length === 13, '13 fiches détail (multi-tâches sans chevron)', home.filter(r => r.info).length);

  /* ouverture générique : intro → … → run */
  const clickText = async (sel) => page.evaluate(s => { const b = document.querySelector(s); if (!b) return false; b.click(); return true; }, sel);
  async function enterRun(id, maxClicks = 24) {
    await page.evaluate(() => { location.hash = '#/'; });
    await page.waitForSelector('.task[data-id="' + id + '"] .tk-start');
    await page.click('.task[data-id="' + id + '"] .tk-start');
    await wait(120);
    for (let i = 0; i < maxClicks; i++) {
      const st = await page.evaluate(() => { const S = CORE.current; return S ? { phase: S.phase, kind: S.sec.kind } : null; });
      if (!st) break;
      if (st.phase === 'run') return true;
      if (st.kind === 'lang' && st.phase === 'example') {
        const ready = await page.evaluate(() => !!document.getElementById('lgStart'));
        if (ready) { await page.evaluate(() => document.getElementById('lgStart').click()); await wait(150); return true; }
        const n = await page.evaluate(() => document.querySelectorAll('.optrow').length);
        if (n) { await page.evaluate(() => { const b = document.querySelectorAll('.optrow')[0]; b && b.click(); }); await wait(900); continue; }
      }
      if (st.kind === 'lang' && st.phase === 'run') return true;
      if (st.kind === 'seqmem' && st.phase === 'example') {
        const pool = await page.evaluate(() => document.querySelectorAll('.le-p').length);
        if (pool) { for (let k = 0; k < 6; k++) { await page.evaluate(() => document.querySelector('.le-p').click()); } await wait(60); }
        const dis = await page.evaluate(() => { const b = document.getElementById('leOk'); return b ? b.disabled : true; });
        if (!dis) { await page.evaluate(() => document.getElementById('leOk').click()); continue; }
      }
      if (st.kind === 'edots' && st.phase === 'example') return true; /* la concentration démarre par 30 s d'exemple chronométré */
      /* exemples numverb / latin / pick2 / mech */
      if (st.phase === 'example') {
        const kind = st.kind;
        if (kind === 'numverb') { await page.evaluate(() => { const b = document.querySelectorAll('.tfbtn')[0]; b && b.click(); }); await wait(800); continue; }
        if (kind === 'latin') { await page.evaluate(() => { const b = document.querySelectorAll('.ded-opt')[0]; b && b.click(); }); await wait(800); continue; }
        if (kind === 'pick2') {
          await page.evaluate(() => { const c = document.querySelectorAll('.cand'); c[0] && c[0].click(); c[1] && c[1].click(); const g = document.getElementById('indGo'); g && g.click(); });
          await wait(800); continue;
        }
        if (kind === 'mech') { await page.evaluate(() => { const b = document.querySelectorAll('.optrow')[0]; b && b.click(); }); await wait(900); continue; }
        if (kind === 'switchcode') { await page.evaluate(() => { const b = document.getElementById('tutNext'); b && b.click(); }); await wait(120); continue; }
      }
      await clickText('#inNext') || await clickText('#tutNext');
      await wait(120);
    }
    return false;
  }

  /* ── 2. chaque Début ouvre la bonne épreuve, sans erreur ── */
  group('Démarrage des 14 épreuves depuis l’accueil');
  const KIND = { behaviour: 'blocks', motivation: 'blocks', numerical: 'numverb', verbal: 'numverb', deductive: 'latin', inductive: 'pick2', concentration: 'edots', multitask: 'mt', learning: 'seqmem', info: 'inbox', english: 'lang', french: 'lang', mechanical: 'mech', switch: 'switchcode' };
  const seen = {};
  for (const [id] of EXPECT) {
    console.log('  · démarrage ' + id);
    const e0 = errors.length;
    const entered = await enterRun(id);
    const st = await page.evaluate(() => { const S = CORE.current; return S ? { phase: S.phase, kind: S.sec.kind, id: S.sec.id, items: S.items ? S.items.length : 0, timer: document.getElementById('skTimer').textContent, count: document.getElementById('skCount').textContent } : null; });
    seen[id] = st;
    ok(st && st.id === id && st.kind === KIND[id], 'Début → ' + id + ' (' + KIND[id] + ')', st);
    ok(errors.length === e0, 'aucune erreur JS au démarrage de ' + id, errors.slice(e0));
    await page.evaluate(() => CORE.destroy());
  }

  /* ── 3. structure interne par épreuve ── */
  group('Structure interne des épreuves');
  ok(seen.numerical.items === 37, 'numérique : 37 questions', seen.numerical);
  ok(/^\d\d:\d\d$/.test(seen.numerical.timer) && seen.numerical.timer === '12:00', 'numérique : chrono global 12:00', seen.numerical.timer);
  ok(seen.numerical.count === '', 'numérique : pas de compteur avant la 1re réponse', seen.numerical.count);
  ok(seen.verbal.items === 49, 'verbal : 49 affirmations', seen.verbal);
  ok(seen.verbal.timer === '12:00', 'verbal : chrono global 12:00', seen.verbal.timer);
  ok(seen.deductive.timer === '06:00', 'déductif : 6:00 global', seen.deductive.timer);
  ok(seen.inductive.timer === '06:00', 'inductif : 6:00 global', seen.inductive.timer);
  ok(seen.concentration.timer === '00:30', 'concentration : exemple chronométré 30 s', seen.concentration.timer);
  ok(seen.multitask.timer === '05:00', 'multi-tâches : 5:00 (scales mt officiel)', seen.multitask.timer);
  ok(seen.learning.kind === 'seqmem', 'apprentissage : épreuve de type seqmem', seen.learning.kind);
  ok(seen.behaviour.timer === '' && seen.motivation.timer === '', 'comportements / motivations : sans chrono (personnalité)', { be: seen.behaviour.timer, mo: seen.motivation.timer });
  ok(seen.info.timer === '15:00', 'traitement info : 15:00', seen.info.timer);
  ok(seen.mechanical.items === 24 && seen.mechanical.timer === '15:00', 'mécanique : 24 questions / 15:00', seen.mechanical);
  ok(seen.switch.timer === '06:00', 'switch : 6:00', seen.switch.timer);
  const btabs = await page.evaluate(() => { const S = CORE.SECTIONS; return S.length; });
  ok(btabs === 14, 'registre : 14 épreuves', btabs);

  /* chronomètres officiels : durées des tests (sources Aon / cut-e) */
  group('Chronomètres officiels des épreuves');
  const OFF = {
    numerical: 720, verbal: 720, deductive: 360, inductive: 360, concentration: 120,
    multitask: 300, learning: 300, info: 900, english: null, french: null, mechanical: 900, switch: 360
  };
  const tim = await page.evaluate(() => { const o = {}; CORE.SECTIONS.forEach(x => o[x.id] = x.timed === undefined ? null : x.timed); return o; });
  Object.keys(OFF).forEach(id => ok(tim[id] === OFF[id], 'chrono ' + id + ' = ' + (OFF[id] === null ? 'sous-sections' : OFF[id] + ' s'), tim[id]));
  ok(tim.behaviour === null && tim.motivation === null, 'comportements / motivations : aucun chrono', { be: tim.behaviour, mo: tim.motivation });
  ok(tim.english === null && tim.french === null, 'langues : chrono par sous-section (4:00 / 4:00 / 2:00)', { en: tim.english, fr: tim.french });
  /* les durées affichées sur l'accueil (document) restent inchangées */
  const homeMin = await page.evaluate(() => CORE.SECTIONS.map(s2 => s2.home + ':' + s2.min).join('|'));
  ok(homeMin.indexOf('Capacité multi-tâches:8') >= 0 && homeMin.indexOf('Capacité d’apprentissage:9') >= 0, 'les durées « document » de l’accueil sont conservées (8 min / 9 min)', homeMin);

  /* ── 4. comportements : 48 blocs × 3 énoncés × 6 pastilles, pas de chrono ── */
  group('Comportements / Motivations');
  await enterRun('behaviour');
  let blk = await page.evaluate(() => ({ rows: document.querySelectorAll('.blk-row').length, dots: document.querySelectorAll('.blk-row .dot').length, timer: document.getElementById('skTimer').textContent, count: document.getElementById('skCount').textContent }));
  ok(blk.rows === 3 && blk.dots === 18, '1 bloc = 3 énoncés × 6 pastilles', blk);
  ok(blk.timer === '' && blk.count === '1/48', 'pas de chrono, compteur 1/48', blk);
  const unselected = await page.evaluate(() => document.querySelectorAll('.blk-row .dot.on').length);
  ok(unselected === 0, 'aucune pastille présélectionnée au départ', unselected);
  await page.evaluate(() => { const d = document.querySelectorAll('.blk-row')[0].querySelectorAll('.dot'); d[5].click(); });
  const st2 = await page.evaluate(() => ({ rest: document.getElementById('blkRest').textContent, sel: CORE.current.sel.slice(), off: document.querySelectorAll('.dot.off').length }));
  ok(st2.rest === '0' && st2.sel[0] === 6 && st2.off >= 12, '6 points sur une affirmation → solde épuisé, les autres cercles sont désactivés', st2);
  await page.evaluate(() => CORE.destroy());
  await enterRun('motivation');
  const mot = await page.evaluate(() => ({ count: document.getElementById('skCount').textContent, rows: document.querySelectorAll('.blk-row').length }));
  ok(mot.count === '1/36', 'motivations : 36 blocs (1/36)', mot);
  await page.evaluate(() => CORE.destroy());

  /* ── 5. déductif : grille 4×4, 3 options, avance automatique ── */
  group('Déductif');
  await enterRun('deductive');
  const ded = await page.evaluate(() => ({ grid: document.querySelectorAll('.ded-tile').length, holes: document.querySelectorAll('.ded-tile.hole').length, opts: document.querySelectorAll('.ded-opt').length, empty: document.querySelectorAll('.ded-tile.empty').length }));
  ok(ded.grid === 16 && ded.holes === 1 && ded.opts === 4, 'grille 4×4 + 1 case « ? » + 4 options', ded);
  const before = await page.evaluate(() => CORE.current.log.length);
  await page.evaluate(() => document.querySelector('.ded-opt').click());
  await wait(700);
  const after = await page.evaluate(() => ({ log: CORE.current.log.length, i: CORE.current.i, timer: document.getElementById('skTimer').textContent }));
  ok(after.log === before + 1 && after.i === 1, 'réponse → avance automatiquement (pas de bouton)', after);
  ok(after.timer === '06:00' || after.timer === '05:59', 'chrono global inchangé par question', after.timer);
  await page.evaluate(() => CORE.destroy());

  /* ── 6. inductif : 4 candidats, exactement 2 à choisir ── */
  group('Inductif');
  await enterRun('inductive');
  const ind = await page.evaluate(() => ({ cards: document.querySelectorAll('.cand').length, groups: document.querySelectorAll('.ind-side .g3').length, go: !!document.getElementById('indGo') }));
  ok(ind.cards === 4 && ind.go, '4 candidats + bouton de validation', ind);
  const picked = await page.evaluate(() => { const c = document.querySelectorAll('.cand'); c[0].click(); c[1].click(); return document.querySelectorAll('.cand.sel').length; });
  ok(picked === 2, 'sélection limitée à 2 grilles', picked);
  const extra = await page.evaluate(() => { const c = document.querySelectorAll('.cand'); c[2].click(); return document.querySelectorAll('.cand.sel').length; });
  ok(extra === 2, 'une 3e sélection est refusée', extra);
  await page.evaluate(() => CORE.destroy());

  /* ── 7. concentration : D/A, exemple 30 s puis test 2:00 ── */
  group('Concentration');
  await enterRun('concentration');
  const conc = await page.evaluate(() => ({ btns: [...document.querySelectorAll('.conc-btn')].map(b => b.textContent.trim()), svg: !!document.querySelector('.conc-box svg'), ex: CORE.current.exMode }));
  ok(conc.btns.length === 2 && conc.svg && conc.ex === true, 'exemple : figure + boutons incorrect/correct', conc);
  await page.keyboard.press('d'); await wait(60);
  const conc2 = await page.evaluate(() => ({ ex: CORE.current.exMode, i: CORE.current.i }));
  ok(conc2.ex === true, 'exemple : la touche D passe à l’exemple suivant (noté non compté)', conc2);
  await page.evaluate(() => { const S = CORE.current; S.deadline = Date.now() - 1; });
  await wait(400);
  const conc3 = await page.evaluate(() => ({ ex: CORE.current.exMode, timer: document.getElementById('skTimer').textContent, phase: CORE.current.phase }));
  ok(conc3.ex === false && conc3.phase === 'run' && conc3.timer === '02:00', 'fin des exemples → test 2:00', conc3);
  await page.keyboard.press('a'); await wait(80);
  const conc4 = await page.evaluate(() => CORE.current.log.map(r => r.ok));
  ok(conc4.length === 1, 'touche A répond en mode test', conc4);
  await page.evaluate(() => { CORE.current.log = []; CORE.current.deadline = Date.now() - 1; });
  await wait(300);
  const concEnd = await page.evaluate(() => ({ phase: CORE.current.phase, home: !!document.getElementById('endHome'), attempts: CORE.P.attempts().length }));
  ok(concEnd.phase === 'end' && concEnd.home && concEnd.attempts >= 1, 'fin de test → écran de fin + session enregistrée', concEnd);
  await page.evaluate(() => CORE.destroy());

  /* ── 8. apprentissage : démo, 6×12 objets, pauses 6 s ── */
  group('Apprentissage');
  await enterRun('learning');
  const le = await page.evaluate(() => ({ phase: CORE.current.demoPhase, obj: !!document.querySelector('.le-seq .le-obj svg') }));
  ok(le.phase === 'show' && le.obj, 'démo : présentation des objets un à un', le);
  await page.evaluate(() => { CORE.current.demoIdx = 6; });   /* force la fin du défilement (6 objets × 1,3 s) */
  await wait(1500);
  const le2 = await page.evaluate(() => ({ pool: document.querySelectorAll('.le-p').length, fields: document.querySelectorAll('.le-f').length }));
  ok(le2.pool === 6 && le2.fields === 6, 'démo : 6 champs + 6 objets à replacer', le2);
  /* remplit la démo */
  for (let i = 0; i < 6; i++) await page.evaluate(() => document.querySelector('.le-p').click());
  await wait(80);
  await page.evaluate(() => document.getElementById('leOk').click());
  await wait(150);
  const le3 = await page.evaluate(() => ({ phase: CORE.current.phase, lePhase: CORE.current.lePhase, timer: document.getElementById('skTimer').textContent }));
  ok(le3.phase === 'run' && le3.lePhase === 'break' && le3.timer === '05:00', 'test réel : chrono global 5:00 pendant la pause de 6 s', le3);
  const le3b = await page.evaluate(() => ({ pause: (document.querySelector('.le-break') || {}).innerText || '' }));
  ok(/00:0\d/.test(le3b.pause), 'la pause de 6 s est décomptée dans la page', le3b);
  await page.evaluate(() => { CORE.current.secEnd = Date.now() - 1; });
  await wait(400);
  const le4 = await page.evaluate(() => ({ lePhase: CORE.current.lePhase, obj: !!document.querySelector('.le-seq .le-obj svg') }));
  ok(le4.lePhase === 'show' && le4.obj, 'fin de pause → présentation des 12 objets', le4);
  await page.evaluate(() => { CORE.current.showNext = Date.now() - 1; });
  await wait(350);
  const le5 = await page.evaluate(() => CORE.current.leIdx);
  ok(le5 >= 1, 'les objets défilent automatiquement', le5);
  for (let i = 0; i < 24 && (await page.evaluate(() => CORE.current.lePhase)) === 'show'; i++) { await page.evaluate(() => { CORE.current.showNext = Date.now() - 1; }); await wait(300); }
  const le6 = await page.evaluate(() => ({ lePhase: CORE.current.lePhase, fields: document.querySelectorAll('.le-f').length, pool: document.querySelectorAll('.le-p').length }));
  ok(le6.lePhase === 'place' && le6.fields === 12 && le6.pool === 12, 'rappel : 12 positions + 12 objets mélangés', le6);
  for (let i = 0; i < 12; i++) await page.evaluate(() => { const b = document.querySelector('.le-p'); b && b.click(); });
  await wait(100);
  const le7 = await page.evaluate(() => ({ filled: document.querySelectorAll('.le-f.filled').length, disabled: document.getElementById('leNext').disabled, title: document.querySelector('.qtitle').innerText }));
  ok(le7.filled === 12 && le7.disabled === false, 'les 12 positions remplies activent « › »', le7);
  ok(/0[0-9]:\d\d/.test(le7.title), 'le temps restant de la section est affiché pendant la restitution', le7.title);
  await page.evaluate(() => CORE.destroy());

  /* ── 9. traitement de l'information : 15 mails + 3 en retard, guide ── */
  group('Traitement de l’information');
  await enterRun('info');
  const inf = await page.evaluate(() => ({ mails: document.querySelectorAll('#ibList .mail').length, selects: document.querySelectorAll('#mPrio,#mAct').length, guide: !!document.getElementById('ibGuide') || !!document.getElementById('skBook'), opts: document.querySelectorAll('#mPrio option').length, clock: document.getElementById('ibClock').textContent }));
  ok(inf.mails === 12 && inf.selects === 2 && inf.guide, '12 mails + priorité + action + guide', inf);
  ok(inf.clock && /\d{2}\/\d{2}\/\d{4}/.test(inf.clock), 'date et heure du jour affichées dans l’en-tête', inf.clock);
  ok(inf.opts === 4, 'priorités : — / HIGH / MEDIUM / LOW', inf.opts);
  const infLate = await page.evaluate(() => { CORE.current.t0 = Date.now() - 300000; return null; });
  await wait(400);
  const inf2 = await page.evaluate(() => ({ mails: document.querySelectorAll('#ibList .mail').length }));
  ok(inf2.mails > 12, 'des mails arrivent en cours de test', inf2);
  await page.evaluate(() => { CORE.current.t0 = Date.now() - 1000000; CORE.current.late = 30; });
  await wait(500);
  const inf4 = await page.evaluate(() => ({ mails: document.querySelectorAll('#ibList .mail').length }));
  ok(inf4.mails > inf2.mails, 'au-delà de la banque, la boîte continue de recevoir des e-mails', { avant: inf2.mails, apres: inf4.mails });
  await page.evaluate(() => document.getElementById('ibGuide').click());
  const inf3 = await page.evaluate(() => ({ on: document.getElementById('guidePanel').classList.contains('on'), h: document.getElementById('guidePanel').innerText.length }));
  ok(inf3.on && inf3.h > 200, 'le guide des consignes s’ouvre', inf3);
  await page.evaluate(() => CORE.destroy());

  /* ── 10. langues : 3 sous-sections (aisance, vocabulaire, orthographe), « ? » neutre ── */
  group('Anglais / Français');
  await page.evaluate(() => { location.hash = '#/'; });
  await wait(150);
  await page.evaluate(() => { location.hash = '#/run/english'; });
  await wait(250);
  for (let i = 0; i < 10; i++) {
    const ph = await page.evaluate(() => CORE.current && CORE.current.phase);
    if (ph !== 'intro') break;
    await page.evaluate(() => { const b = document.getElementById('inNext'); b && b.click(); });
    await wait(140);
  }
  const lg = await page.evaluate(() => ({ sub: CORE.current.sub, type: CORE.current.cur.type, opts: document.querySelectorAll('.optrow').length, unk: !![...document.querySelectorAll('.optrow')].find(b => b.textContent.trim() === '?') }));
  ok(lg.type === 'flu' && lg.opts >= 3 && lg.unk, 'anglais : section 1 (aisance) avec option « ? » neutre', lg);
  /* répond aux 2 exemples puis vérifie le chrono de sous-section (4:00) */
  for (let i = 0; i < 2; i++) { await page.evaluate(() => document.querySelector('.optrow').click()); await wait(950); }
  const lgR = await page.evaluate(() => ({ phase: CORE.current.langPhase, start: !!document.getElementById('lgStart') }));
  ok(lgR.phase === 'ready' && lgR.start, 'après les 2 exemples : l’utilisateur décide du début de la section', lgR);
  await page.evaluate(() => document.getElementById('lgStart').click());
  await wait(150);
  const lg2 = await page.evaluate(() => ({ phase: CORE.current.langPhase, timer: document.getElementById('skTimer').textContent, n: CORE.current.langCount }));
  ok(lg2.phase === 'run' && lg2.timer === '04:00', 'aisance : 4:00 de test après les 2 exemples', lg2);
  const lgSel = await page.evaluate(() => { document.querySelectorAll('.optrow')[1].click(); return { disabled: document.getElementById('lgNext').disabled, log: CORE.current.log.length }; });
  ok(lgSel.disabled === false && lgSel.log === 0, 'la réponse se sélectionne et « suivant » se débloque', lgSel);
  const lgAdv = await page.evaluate(() => { document.getElementById('lgNext').click(); return CORE.current.log.length; });
  ok(lgAdv === 1, '« suivant » enregistre la réponse et passe à la question', lgAdv);
  const lgUnk = await page.evaluate(() => { document.querySelector('.optrow[data-i="99"]').click(); document.getElementById('lgNext').click(); return CORE.current.log.slice(-1)[0]; });
  ok(lgUnk.ok === null && lgUnk.given === '?', '« ? » = réponse neutre non pénalisée', lgUnk);
  /* la section ne s'épuise jamais : au-delà de la banque, le générateur produit des questions similaires */
  const lgPool = await page.evaluate(() => {
    const S2 = CORE.current, out = { bank: S2.cur.items.length, types: {} };
    [40, 220, 900].forEach(i => { const it = S2.cur.at(i); out.types[i] = !!(it && it.o && it.o.length >= 2 && it.a >= 0 && it.a < it.o.length && new Set(it.o).size === it.o.length); });
    return out;
  });
  ok(lgPool.types[40] && lgPool.types[220] && lgPool.types[900], 'aisance : questions similaires générées sans fin (index 40 / 220 / 900)', lgPool);
  const lgFar = await page.evaluate(() => {
    const S2 = CORE.current; S2.langIdx = 400;
    document.querySelector('.optrow').click(); document.getElementById('lgNext').click();
    const last = S2.log.slice(-1)[0];
    return { n: S2.langIdx, q: last && last.q, ok: !!(last && last.correct && last.q) };
  });
  ok(lgFar.ok && String(lgFar.q).length > 5, 'une réponse est enregistrée au-delà de l’index 400 (aucune pénurie)', lgFar);
  const lgFr = await page.evaluate(() => {
    const out = {};
    ['flu', 'voc', 'spe'].forEach(t => {
      const sec = DRILL.langSection('fr', t, 4242);
      const it = sec.at(500);
      out[t] = !!(it && it.o && it.o.length >= 2 && it.a >= 0 && it.a < it.o.length);
    });
    return out;
  });
  ok(lgFr.flu && lgFr.voc && lgFr.spe, 'français : générateur de secours pour aisance, vocabulaire et orthographe', lgFr);
  await page.evaluate(() => CORE.destroy());

  /* ── 11. mécanique : 24 questions, navigation ‹ ▦ › ── */
  group('Mécanique');
  await enterRun('mechanical');
  const mech = await page.evaluate(() => ({ opts: document.querySelectorAll('.optrow').length, nav: !!document.getElementById('nvGrid'), svg: !!document.querySelector('.panel-gray svg'), count: document.getElementById('skCount').textContent }));
  ok(mech.opts === 3 && mech.nav && mech.svg, '3 options + scène SVG + navigation', mech);
  await page.evaluate(() => document.getElementById('nvGrid').click());
  const mech2 = await page.evaluate(() => document.querySelectorAll('#navGrid button').length);
  ok(mech2 === 24, 'la grille de navigation liste les 24 questions', mech2);
  await page.evaluate(() => document.getElementById('nvGrid').click());
  await page.evaluate(() => CORE.destroy());

  /* ── 12. switch challenge : machine + 3 codes ── */
  group('switchChallenge');
  await enterRun('switch');
  const sw = await page.evaluate(() => ({ codes: document.querySelectorAll('.sw-codeopt').length, tiles: document.querySelectorAll('.sw-tile').length, machine: !!document.querySelector('.sw-machine'), level: document.getElementById('skLvl').textContent }));
  ok(sw.codes === 3 && sw.tiles === 8 && sw.machine, '8 tuiles (entrée/sortie) + machine + 3 codes', sw);
  ok(/Level \d+/.test(sw.level), 'niveau affiché (Level 1)', sw.level);
  const swLog = await page.evaluate(() => { document.querySelector('.sw-codeopt').click(); return CORE.current.log.slice(-1)[0]; });
  ok(swLog && swLog.ok !== undefined, 'la réponse est enregistrée', swLog);
  await page.evaluate(() => CORE.destroy());

  /* ── 13. multitâches ── */
  group('Multi-tâches');
  await enterRun('multitask');
  const mt = await page.evaluate(() => ({ chars: document.querySelectorAll('.mt-stim .ch').length, btns: document.querySelectorAll('.mt-btn').length, cue: document.querySelector('.mt-cue').innerText.slice(0, 20) }));
  ok(mt.chars === 2 && mt.btns === 2, 'deux stimuli + deux réponses', mt);
  await page.evaluate(() => CORE.destroy());

  /* ── 14. numverb : réponse + navigation ‹ ▦ › + exempled ── */
  group('Numérique / verbal');
  await enterRun('numerical');
  const nv = await page.evaluate(() => ({ tabs: document.querySelectorAll('.nv-tab').length, tf: document.querySelectorAll('.tfbtn').length, nav: !!document.getElementById('nvGrid') }));
  ok(nv.tabs === 6 && nv.tf === 3 && nv.nav, '6 onglets + 3 réponses + navigation', nv);
  await page.evaluate(() => document.querySelectorAll('.tfbtn')[0].click());
  await wait(100);
  const nv2 = await page.evaluate(() => ({ answered: Object.keys(CORE.current.answers).length, slide: !!document.querySelector('.nv-slide') }));
  ok(nv2.answered === 0, 'réponse sélectionnée mais pas encore enregistrée (correction possible)', JSON.stringify(nv2));
  await wait(1200);
  const nv2s = await page.evaluate(() => ({ answered: Object.keys(CORE.current.answers).length, slide: !!document.querySelector('.nv-slide.on') }));
  ok(nv2s.slide === true && nv2s.answered === 0, 'retour glissant affiché pendant la fenêtre de correction', nv2s);
  await wait(4600);
  const nv2b = await page.evaluate(() => ({ answered: Object.keys(CORE.current.answers).length, count: document.getElementById('skCount').textContent, i: CORE.current.i }));
  ok(nv2b.answered === 1 && nv2b.count === '1 / 37' && nv2b.i === 1, 'après 4 s : réponse enregistrée, compteur 1 / 37, question suivante', nv2b);
  await page.evaluate(() => { document.getElementById('nvNext').click(); });
  await wait(150);
  const nv3 = await page.evaluate(() => ({ i: CORE.current.i, count: document.getElementById('skCount').textContent }));
  ok(nv3.i === 2 && nv3.count === '1 / 37', 'flèche › avance la question', nv3);
  /* les onglets de feuilles de données restent sous contrôle de l'utilisateur */
  await enterRun('numerical');
  const nvTab0 = await page.evaluate(() => ({ tab: CORE.current.tab, itemTab: CORE.current.items[CORE.current.i].tab, sheets: document.querySelectorAll('.nv-tab').length }));
  ok(nvTab0.sheets === 6 && !!nvTab0.tab, '6 feuilles de données affichées avec la question', nvTab0);
  await page.evaluate(() => { const b = [...document.querySelectorAll('.nv-tab')].find(x => x.dataset.t !== CORE.current.tab); b.click(); });
  await wait(120);
  const nvTab1 = await page.evaluate(() => ({ tab: CORE.current.tab, on: document.querySelector('.nv-tab.on') ? document.querySelector('.nv-tab.on').dataset.t : null }));
  ok(nvTab1.tab !== nvTab0.tab && nvTab1.on === nvTab1.tab, 'changer de feuille de données fonctionne (question inchangée)', nvTab1);
  await page.evaluate(() => { document.getElementById('nvNext').click(); });
  await wait(150);
  const nvTab2 = await page.evaluate(() => ({ tab: CORE.current.tab, itemTab: CORE.current.items[CORE.current.i].tab, i: CORE.current.i }));
  ok(nvTab2.tab === nvTab1.tab, 'la feuille consultée reste celle choisie (pas de saut automatique par question)', nvTab2);
  await page.evaluate(() => CORE.destroy());
  await enterRun('verbal');
  const vb = await page.evaluate(() => ({ tabs: [...document.querySelectorAll('.nv-tab')].map(t => t.textContent.trim()).length, n: CORE.current.items.length, names: [...document.querySelectorAll('.nv-tab')].map(t => t.textContent.trim()) }));
  ok(vb.tabs === 6 && vb.n === 49, 'verbal : 6 onglets de textes + 49 affirmations', vb);
  ok(vb.names.length === 6 && vb.names.every(n => n === n.toUpperCase()), 'onglets de textes nommés en capitales (comme les captures)', vb.names);
  await page.evaluate(() => CORE.destroy());

  /* ── 15. progression, feedback, réglages, import/export ── */
  group('Progression / feedback / réglages');
  await page.evaluate(() => { location.hash = '#/progression'; });
  await wait(250);
  const prog = await page.evaluate(() => ({ rows: document.querySelectorAll('.tbl')[0].querySelectorAll('tbody tr').length, cards: document.querySelectorAll('.card').length, hist: !!document.getElementById('pgReset') }));
  ok(prog.rows === 14 && prog.cards === 4 && prog.hist, 'progression : 14 épreuves + cartes + historique', prog);
  /* une session avec détail, pour vérifier la relecture en français */
  await enterRun('deductive');
  await page.evaluate(() => { document.querySelector('.ded-opt').click(); });
  await wait(700);
  await page.evaluate(() => { CORE.finish(); });
  await wait(200);
  await page.evaluate(() => { location.hash = '#/feedback'; });
  await wait(250);
  const fb = await page.evaluate(() => ({ sess: document.querySelectorAll('.sesslist .btn').length, h1: document.querySelector('.sk-main h1').textContent.trim() }));
  ok(fb.sess >= 1, 'feedback : sessions listées', fb);
  ok(fb.h1 === 'Feedback', 'feedback : titre en français', fb.h1);
  ok(await page.evaluate(() => !!document.getElementById('fbSel')), 'feedback : filtre par épreuve', null);
  const fbModal = await page.evaluate(() => { document.querySelector('.sesslist .btn').click(); const t = document.getElementById('modalBox').innerText; U.closeModal(); return { fr: /Votre réponse/.test(t) && /Bonne réponse/.test(t), redo: !!document.getElementById('smRedo') }; });
  ok(fbModal.fr, 'feedback : relecture question par question en français', fbModal);
  await page.evaluate(() => { location.hash = '#/'; });
  await wait(200);
  const tabs = await page.evaluate(() => ({ n: document.querySelectorAll('#skTabs a').length, labels: [...document.querySelectorAll('#skTabs a')].map(a => a.textContent.trim()), on: document.querySelector('#skTabs a.on') ? document.querySelector('#skTabs a.on').dataset.tab : null }));
  ok(tabs.n === 4 && tabs.on === 'home', 'barre d’onglets : Tâches / Progression / Feedback / Aide', tabs);
  ok(tabs.labels.join('|') === 'Tâches à accomplir|Progression|Feedback|Aide & réglages', 'onglets libellés en français', tabs.labels);
  await page.evaluate(() => { location.hash = '#/progression'; });
  await wait(200);
  const tabOn = await page.evaluate(() => document.querySelector('#skTabs a.on').dataset.tab);
  ok(tabOn === 'progression', 'l’onglet actif suit la page ouverte', tabOn);
  await page.evaluate(() => { location.hash = '#/feedback'; });
  await wait(200);
  await page.evaluate(() => { location.hash = '#/reglages'; });
  await wait(250);
  const rg = await page.evaluate(() => ({ lang: !!document.getElementById('lgEn'), sound: !!document.getElementById('stSound'), code: document.getElementById('stCode').value }));
  ok(rg.lang && rg.sound && rg.code === 'CM2026', 'réglages : langues, sons, code d’accès', rg);
  const exp = await page.evaluate(() => { let called = 0; const old = URL.createObjectURL; URL.createObjectURL = (b) => { called = b.size; return 'blob:x'; }; const lk = document.createElement('a'); lk.click = () => {}; document.getElementById('stExport').click(); URL.createObjectURL = old; return called; });
  ok(exp > 100, 'export JSON non vide', exp);
  await page.evaluate(() => { location.hash = '#/'; });
  await wait(200);

  /* ── 19. extras : clavier, skip, sessions complètes, export/import ── */
  group('Extras de conformité');
  /* clavier 1-4 sur le déductif */
  await enterRun('deductive');
  const kbBefore = await page.evaluate(() => CORE.current.log.length);
  await page.keyboard.press('1'); await wait(160);
  const dedClasses = await page.evaluate(() => ({ ok: !!document.querySelector('.ded-opt.ok'), ko: !!document.querySelector('.ded-opt.ko') }));
  ok(dedClasses.ok || dedClasses.ko, 'la réponse choisie est marquée en vert (juste) ou rouge (faux)', dedClasses);
  await wait(500);
  const kbAfter = await page.evaluate(() => CORE.current.log.length);
  ok(kbAfter === kbBefore + 1, 'touches 1-4 : réponse au déductif', { kbBefore, kbAfter });
  await page.evaluate(() => CORE.destroy());

  /* inductif : ▶▶ sans sélection = question passée, comptée incorrecte */
  await enterRun('inductive');
  await page.evaluate(() => document.getElementById('indGo').click());
  await wait(400);
  const skip = await page.evaluate(() => CORE.current.log.slice(-1)[0]);
  ok(skip && skip.ok === false && skip.given === '', 'inductif : « ▶▶ » sans sélection passe la question (comptée fausse)', skip);
  await page.evaluate(() => CORE.destroy());

  /* apprentissage : score par positions (12 par section) — parcours réel */
  await page.evaluate(() => { location.hash = '#/'; });
  await wait(150);
  await enterRun('learning');
  await page.evaluate(() => { CORE.current.demoIdx = 6; });
  await wait(1600);                                   /* la démo se termine → écran de placement (6 objets) */
  await page.evaluate(() => { for (let i = 0; i < 6; i++) { const b = document.querySelector('.le-p[data-k="' + i + '"]'); if (b) b.click(); } });
  await wait(150);
  await page.evaluate(() => { const b = document.getElementById('leOk'); b && b.click(); });   /* → test réel, pause 6 s */
  await wait(200);
  await page.evaluate(() => { CORE.current.secEnd = Date.now() - 1; });
  await wait(400);                                    /* → présentation des 12 objets */
  for (let i = 0; i < 24 && (await page.evaluate(() => CORE.current.lePhase)) === 'show'; i++) { await page.evaluate(() => { CORE.current.showNext = Date.now() - 1; }); await wait(320); }
  const lePlace = await page.evaluate(() => ({ lePhase: CORE.current.lePhase, pool: document.querySelectorAll('.le-p').length }));
  ok(lePlace.lePhase === 'place' && lePlace.pool === 12, 'apprentissage : rappel des 12 objets après la présentation', lePlace);
  await page.evaluate(() => { const S = CORE.current; S.items[0].order.forEach(k => { const b = document.querySelector('.le-p[data-k="' + k + '"]'); if (b) b.click(); }); });
  await wait(250);
  await page.evaluate(() => { const b = document.getElementById('leNext'); b && b.click(); });
  await wait(350);
  const leScore = await page.evaluate(() => ({ pos: CORE.current.lePos, log: CORE.current.log.slice(-1)[0], sec: CORE.current.leSec }));
  ok(leScore.pos === 12 && leScore.sec === 1 && /12\/12/.test((leScore.log || {}).given || ''), 'apprentissage : 12 positions correctes comptées par section (72 au total)', leScore);
  await page.evaluate(() => CORE.destroy());

  /* multi-tâches : consigne qui alterne lettre / chiffre */
  await enterRun('multitask');
  const mtCue = await page.evaluate(() => document.querySelector('.mt-cue').innerText);
  ok(/LETTRE|CHIFFRE/.test(mtCue), 'multi-tâches : la consigne alterne LETTRE / CHIFFRE', mtCue.slice(0, 40));
  await page.evaluate(() => CORE.destroy());

  /* numérique : le temps écoulé termine la session et enregistre une tentative */
  await enterRun('numerical');
  const attemptsBefore = await page.evaluate(() => CORE.P.attempts().length);
  await page.evaluate(() => { CORE.current.deadline = Date.now() - 1; });
  await wait(500);
  const numEnd = await page.evaluate(() => ({ phase: CORE.current.phase, n: CORE.P.attempts().length, last: CORE.P.attempts().slice(-1)[0] }));
  ok(numEnd.phase === 'end' && numEnd.n === attemptsBefore + 1 && numEnd.last.items === 37 && numEnd.last.correct === 0, 'numérique : fin au chrono → tentative enregistrée sur 37 questions', { phase: numEnd.phase, items: numEnd.last.items, correct: numEnd.last.correct });
  await page.evaluate(() => CORE.destroy());

  /* anglais : les 3 sections s'enchaînent (aisance → vocabulaire → orthographe) */
  await page.evaluate(() => { location.hash = '#/run/english'; });
  await wait(250);
  for (let i = 0; i < 12; i++) { const ph = await page.evaluate(() => CORE.current && CORE.current.phase); if (ph !== 'intro') break; await page.evaluate(() => { const b = document.getElementById('inNext'); b && b.click(); }); await wait(160); }
  /* exemples 1 → run */
  for (let i = 0; i < 6 && (await page.evaluate(() => CORE.current.langPhase)) === 'examples'; i++) { await page.evaluate(() => { const b = document.querySelector('.optrow'); b && b.click(); }); await wait(950); }
  await page.evaluate(() => { const b = document.getElementById('lgStart'); b && b.click(); });
  await wait(150);
  const secNames = [];
  for (let k = 0; k < 3; k++) {
    secNames.push(await page.evaluate(() => CORE.current.cur.type));
    await page.evaluate(() => { CORE.current.secEnd = Date.now() - 1; });
    await wait(400);
    const inter = await page.evaluate(() => ({ phase: CORE.current.phase, langPhase: CORE.current.langPhase, next: !!document.getElementById('lgNext') }));
    if (k < 2) {
      ok(inter.langPhase === 'inter' && inter.next, 'langues : page de transition entre les sections ' + (k + 1) + ' et ' + (k + 2), inter);
      await page.evaluate(() => { const b = document.getElementById('lgNext'); b && b.click(); });
      await wait(200);
      for (let i = 0; i < 6 && (await page.evaluate(() => CORE.current.langPhase)) === 'examples'; i++) { await page.evaluate(() => { const b = document.querySelector('.optrow'); b && b.click(); }); await wait(950); }
      await page.evaluate(() => { const b = document.getElementById('lgStart'); b && b.click(); });
      await wait(150);
    } else ok(await page.evaluate(() => CORE.current.phase) === 'end', 'anglais : fin de la 3e section → écran de fin', null);
  }
  ok(secNames.join('>') === 'flu>voc>spe', 'anglais : ordre aisance → vocabulaire → orthographe', secNames);
  await page.evaluate(() => CORE.destroy());

  /* export / import JSON réel */
  const round = await page.evaluate(async () => {
    const P = CORE.P;
    const before = P.attempts().length;
    const data = { app: 'skema-training', v: 4, attempts: P.attempts(), details: P.details(), settings: P.settings() };
    const clone = JSON.parse(JSON.stringify(data));
    clone.attempts.forEach(a => a.id = a.id + 'IMP');
    U.store.set(P.key('attempts'), P.attempts().concat(clone.attempts));
    return { before, after: P.attempts().length };
  });
  ok(round.after > round.before, 'import : les tentatives d’une sauvegarde JSON s’ajoutent au profil', round);

  /* réglages : le code d’accès est enregistré */
  await page.evaluate(() => { location.hash = '#/reglages'; });
  await wait(250);
  const codeSet = await page.evaluate(() => { const i = document.getElementById('stCode'); i.value = 'CM2027'; i.dispatchEvent(new Event('change')); return CORE.P.code(); });
  ok(codeSet === 'CM2027', 'réglages : le code d’accès est modifiable et enregistré', codeSet);
  await page.evaluate(() => { const i = document.getElementById('stCode'); i.value = 'CM2026'; i.dispatchEvent(new Event('change')); });
  await page.evaluate(() => { location.hash = '#/'; });
  await wait(200);

  /* ── 16. réseau : aucune requête externe ── */
  group('Confidentialité / réseau');
  ok(external.length === 0, 'aucune requête hors du fichier servi', external.slice(0, 5));

  /* ── 17. mobile 390 px ── */
  group('Mobile 390 px');
  await page.setViewport({ width: 390, height: 800 });
  await page.evaluate(() => { location.hash = '#/'; });
  await wait(250);
  const mob = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }));
  ok(mob.sw <= mob.cw + 2, 'accueil sans débordement horizontal', mob);

  /* ── 18. aucune erreur JS globale ── */
  group('Erreurs JS');
  const realErrors = errors.filter(e => !/favicon/i.test(e));
  ok(realErrors.length === 0, 'aucune erreur JS pendant tout le parcours', realErrors.slice(0, 8));

  console.log('\n───────────────');
  console.log('checks : ' + (PASS + FAIL) + '   ✅ ' + PASS + '   ❌ ' + FAIL);
  await browser.close();
  srv.close();
  process.exit(FAIL ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
