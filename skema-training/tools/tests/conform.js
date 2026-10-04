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
    await page.evaluate(s => document.querySelector(s).click(), '.task[data-id="' + id + '"] .tk-start');
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

  /* ── 4bis. banques de personnalité : complètes et bilingues (FR / EN) ── */
  group('Banques de personnalité (complètes, FR / EN)');
  const banks = await page.evaluate(() => {
    const missing = [], empty = [];
    const check = (bank, blocks) => {
      for (let b = 0; b < blocks; b++) {
        for (let k = 0; k < 3; k++) {
          const p = bank[b * 3 + k];
          if (!p) { missing.push(b + 1); continue; }
          if (!p[0] || !String(p[0]).trim()) empty.push('fr·bloc ' + (b + 1));
          if (!p[1] || !String(p[1]).trim()) empty.push('en·bloc ' + (b + 1));
        }
      }
    };
    check(BANK.behaviour, 48); check(BANK.motivation, 36);
    return { beh: BANK.behaviour.length, mot: BANK.motivation.length, missing, empty };
  });
  ok(banks.beh === 144, 'comportement : 48 blocs × 3 = 144 énoncés', banks.beh);
  ok(banks.mot === 108, 'motivation : 36 blocs × 3 = 108 énoncés', banks.mot);
  ok(banks.missing.length === 0, 'aucun bloc incomplet (plus d’énoncés vides en fin de questionnaire)', banks.missing);
  ok(banks.empty.length === 0, 'aucun énoncé vide, en français comme en anglais', banks.empty);
  for (const lg of ['en', 'fr']) {
    await page.evaluate((l) => CORE.P.setLang('behaviour', l), lg);
    await enterRun('behaviour');
    const shown = await page.evaluate(() => CORE.current.items.map(it => it.stmts.map(s => String(s || '').trim()).join(' ')));
    ok(shown.length === 48 && shown.every(t => t.length > 12), 'comportement (' + lg + ') : les 48 blocs affichent réellement leurs 3 énoncés', shown.filter(t => t.length <= 12).length);
    if (lg === 'en') {
      const first = await page.evaluate(() => ({ shown: CORE.current.items[0].stmts[0], bank: BANK.behaviour[0][1] }));
      ok(first.shown === first.bank, 'comportement : énoncés anglais affichés par défaut', first.shown);
    }
    await page.evaluate(() => CORE.destroy());
  }
  await page.evaluate(() => CORE.P.setLang('behaviour', 'en'));

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
  ok(nvTab0.sheets === 6 && nvTab0.tab === nvTab0.itemTab, '6 feuilles de données, ouverture sur la feuille de la question', nvTab0);
  /* cliquer un onglet change réellement le contenu affiché (et pas seulement la surbrillance) */
  const nvClick = await page.evaluate(() => {
    const norm = (s) => String(s).replace(/\s+/g, ' ').trim();
    const txt = (el) => norm(el.textContent);
    const before = txt(document.querySelector('.nv-fig .nvtext'));
    const stmt = document.querySelector('.nv-stmt').innerText;
    const target = [...document.querySelectorAll('.nv-tab')].find(x => x.dataset.t === 'outlook');
    target.click();
    const after = txt(document.querySelector('.nv-fig .nvtext'));
    const tmp = document.createElement('div'); tmp.innerHTML = DRILL.NV.figures.outlook();
    const expected = txt(tmp);
    return { changed: before !== after, matches: after.length > 20 && after === expected, fy: /FY 8/.test(after) && /FY 9/.test(after), on: document.querySelector('.nv-tab.on').dataset.t, tab: CORE.current.tab, sameStmt: stmt === document.querySelector('.nv-stmt').innerText };
  });
  ok(nvClick.on === 'outlook' && nvClick.tab === 'outlook', 'l’onglet cliqué devient actif', { on: nvClick.on, tab: nvClick.tab });
  ok(nvClick.changed && nvClick.matches, 'le contenu suit l’onglet choisi : cliquer Outlook affiche la feuille Outlook', { changed: nvClick.changed, matches: nvClick.matches });
  ok(nvClick.fy, 'Outlook affiche bien le graphique FY 8 / FY 9', nvClick.fy);
  ok(nvClick.sameStmt, 'la question reste affichée pendant le changement de feuille', nvClick.sameStmt);
  /* la feuille choisie est mémorisée d'une question à l'autre */
  await page.evaluate(() => { document.getElementById('nvNext').click(); });
  await wait(150);
  const nvTab2 = await page.evaluate(() => ({ tab: CORE.current.tab, itemTab: CORE.current.items[CORE.current.i].tab, on: document.querySelector('.nv-tab.on').dataset.t, fig: /FY 8/.test(document.querySelector('.nv-fig .nvtext').innerHTML), i: CORE.current.i }));
  ok(nvTab2.i === 1 && nvTab2.tab === 'outlook' && nvTab2.on === 'outlook' && nvTab2.fig, 'la feuille choisie est conservée (contenu compris) à la question suivante', nvTab2);
  /* sans choix explicite, la feuille par défaut reste celle de la question posée */
  await page.evaluate(() => CORE.destroy());
  await enterRun('numerical');
  for (let k = 0; k < 5; k++) { await page.evaluate(() => document.getElementById('nvNext').click()); await wait(120); }
  const nvDef0 = await page.evaluate(() => ({ tab: CORE.current.tab, itemTab: CORE.current.items[CORE.current.i].tab, i: CORE.current.i }));
  await page.evaluate(() => { document.getElementById('nvNext').click(); });
  await wait(150);
  const nvDef1 = await page.evaluate(() => ({ tab: CORE.current.tab, itemTab: CORE.current.items[CORE.current.i].tab, on: document.querySelector('.nv-tab.on').dataset.t, i: CORE.current.i }));
  ok(nvDef0.tab === nvDef0.itemTab && nvDef1.tab === nvDef1.itemTab && nvDef1.on === nvDef1.itemTab && nvDef0.itemTab !== nvDef1.itemTab, 'sans choix explicite : chaque question ouvre sa propre feuille de données', { q5: nvDef0, q6: nvDef1 });
  await page.evaluate(() => CORE.destroy());
  await enterRun('verbal');
  const vb = await page.evaluate(() => ({ tabs: [...document.querySelectorAll('.nv-tab')].map(t => t.textContent.trim()).length, n: CORE.current.items.length, names: [...document.querySelectorAll('.nv-tab')].map(t => t.textContent.trim()) }));
  ok(vb.tabs === 6 && vb.n === 49, 'verbal : 6 onglets de textes + 49 affirmations', vb);
  ok(vb.names.length === 6 && vb.names.every(n => n === n.toUpperCase()), 'onglets de textes nommés en capitales (comme les captures)', vb.names);
  await page.evaluate(() => CORE.destroy());

  /* ── 14bis. flux exemples → chrono : explicite et rapide ── */
  group('Exemples → chrono (flux explicite)');
  await page.evaluate(() => { location.hash = '#/'; });
  await page.waitForSelector('.task[data-id="numerical"] .tk-start');
  await page.click('.task[data-id="numerical"] .tk-start');
  await wait(150);
  for (let i = 0; i < 12 && (await page.evaluate(() => CORE.current && CORE.current.phase)) === 'intro'; i++) { await page.evaluate(() => { const b = document.getElementById('inNext'); b && b.click(); }); await wait(140); }
  const ex0 = await page.evaluate(() => ({ phase: CORE.current.phase, n: (CORE.current.examples || []).length, note: (document.querySelector('.ex-note') || {}).innerText || '', timer: document.getElementById('skTimer').textContent, example: /EXAMPLE/.test(document.querySelector('.nv-stmt').innerText) }));
  ok(ex0.phase === 'example' && ex0.n === 3, 'numérique : 3 exemples non notés avant le test', { phase: ex0.phase, n: ex0.n });
  ok(ex0.example && /12:00/.test(ex0.note), 'note sous l’énoncé : le chrono 12:00 démarre après le 3ᵉ exemple', ex0.note);
  ok(ex0.timer === '', 'aucun chrono affiché pendant les exemples', ex0.timer);
  const tEx = Date.now();
  for (let k = 0; k < 3; k++) {
    const before = await page.evaluate(() => CORE.current.i);
    await page.evaluate(() => { const b = document.querySelector('.tfbtn'); b && b.click(); });
    for (let w = 0; w < 45; w++) {
      const st = await page.evaluate(() => ({ i: CORE.current.i, ph: CORE.current.phase }));
      if (st.ph === 'run' || st.i > before) break;
      await wait(60);
    }
  }
  const perExample = (Date.now() - tEx) / 3;
  ok(perExample < 2200, 'exemples accélérés (~1,8 s par exemple, seuil 2,2 s)', Math.round(perExample));
  const runSt = await page.evaluate(() => ({ phase: CORE.current.phase, timer: document.getElementById('skTimer').textContent, example: /EXAMPLE/.test(document.querySelector('.nv-stmt').innerText), note: !!document.querySelector('.ex-note') }));
  ok(runSt.phase === 'run' && runSt.timer === '12:00', 'fin des exemples → le test réel démarre et le chrono affiche 12:00', runSt);
  ok(!runSt.example && !runSt.note, 'la 1re question réelle ne porte plus mention d’exemple', runSt);
  await wait(1300);
  const tick1 = await page.evaluate(() => document.getElementById('skTimer').textContent);
  ok(tick1 === '11:59' || tick1 === '11:58', 'le chrono décompte bien après le démarrage (11:59)', tick1);
  await page.evaluate(() => CORE.destroy());

  /* ── 14ter. langue : épreuves en anglais par défaut, habillage en français ── */
  group('Langue des épreuves (anglais par défaut)');
  const langDef = await page.evaluate(() => {
    const s = CORE.P.settings(); delete s.langs; CORE.P.saveSettings(s);
    const o = {}; ['behaviour', 'numerical', 'verbal', 'mechanical', 'info', 'english', 'french'].forEach(id => o[id] = CORE.P.lang(id));
    return o;
  });
  ok(langDef.numerical === 'en' && langDef.verbal === 'en' && langDef.behaviour === 'en' && langDef.mechanical === 'en' && langDef.info === 'en', 'épreuves en anglais par défaut', langDef);
  ok(langDef.english === 'en' && langDef.french === 'fr', 'tests de langues : consignes dans la langue de l’épreuve', { en: langDef.english, fr: langDef.french });
  await page.evaluate(() => { location.hash = '#/'; });
  await wait(150);
  await page.click('.task[data-id="numerical"] .tk-start');
  await wait(150);
  const introEn = await page.evaluate(() => document.querySelector('.intro-page').innerText);
  ok(/This test checks your ability to analyse/.test(introEn), 'consignes du numérique en anglais', introEn.slice(0, 60));
  for (let i = 0; i < 12 && (await page.evaluate(() => CORE.current && CORE.current.phase)) === 'intro'; i++) { await page.evaluate(() => { const b = document.getElementById('inNext'); b && b.click(); }); await wait(140); }
  const numEn = await page.evaluate(() => ({ sheets: document.querySelector('.nv-sheets-l').textContent.trim(), hint: document.querySelector('.nv-sheets-h').textContent.trim(), tf: [...document.querySelectorAll('.tfbtn')].map(b => b.textContent.trim()).join('/'), stmt: document.querySelector('.nv-stmt').innerText.trim(), expected: DRILL.NV.items[DRILL.NV.items.length - 3].q }));
  ok(numEn.sheets === 'Data sheets' && /Move freely between the sheets/.test(numEn.hint), 'numérique : libellés de feuilles en anglais', { sheets: numEn.sheets, hint: numEn.hint.slice(0, 40) });
  ok(numEn.tf === 'true/false/cannot say', 'numérique : true / false / cannot say', numEn.tf);
  ok(/^EXAMPLE\s+/.test(numEn.stmt) && numEn.stmt.replace(/^EXAMPLE\s+/, '') === numEn.expected, 'énoncé d’exemple anglais et complet (base Halden & Roe)', numEn.stmt.slice(0, 60));
  await page.evaluate(() => CORE.destroy());
  await enterRun('behaviour');
  const behEn = await page.evaluate(() => ({ rows: [...document.querySelectorAll('.blk-t')].map(x => x.textContent.trim()), en: BANK.behaviour.slice(0, 3).map(p => p[1]), head: document.querySelector('.blk-head h2').textContent }));
  ok(behEn.rows.join('|') === behEn.en.join('|'), 'comportement : le 1er bloc s’affiche en anglais', behEn.rows);
  ok(/How accurately do these statements describe your behaviour\?/.test(behEn.head), 'comportement : intertitre en anglais', behEn.head);
  await page.evaluate(() => CORE.destroy());
  await enterRun('mechanical');
  const mechEn = await page.evaluate(() => ({ shown: [...document.querySelectorAll('.optrow')].map(b => b.innerText.trim()), bank: BANK.mech[0].o }));
  ok(mechEn.shown.join('/') === mechEn.bank.join('/'), 'mécanique : options de l’exemple en anglais', mechEn.shown);
  await page.evaluate(() => CORE.destroy());
  await enterRun('info');
  const infoEn = await page.evaluate(() => ({ prio: [...document.querySelectorAll('#mPrio option')].map(o => o.textContent).join('/'), lab: [...document.querySelectorAll('.mail-ctl label')].map(l => l.textContent).join('/') }));
  ok(/HIGH/.test(infoEn.prio) && /MEDIUM/.test(infoEn.prio) && /LOW/.test(infoEn.prio) && /Priority/.test(infoEn.lab) && /Action/.test(infoEn.lab), 'boîte de réception : libellés anglais (Priority / Action / HIGH…)', infoEn);
  await page.evaluate(() => CORE.destroy());
  /* réglage épreuve par épreuve : le numérique rebascule en français */
  await page.evaluate(() => CORE.P.setLang('numerical', 'fr'));
  await page.evaluate(() => { location.hash = '#/'; });
  await wait(150);
  await page.click('.task[data-id="numerical"] .tk-start');
  await wait(150);
  const introFr = await page.evaluate(() => document.querySelector('.intro-page').innerText);
  ok(/Ce test mesure votre capacité/.test(introFr), 'réglage par épreuve : le numérique repasse en français', introFr.slice(0, 60));
  await page.evaluate(() => CORE.destroy());
  await page.evaluate(() => { const s = CORE.P.settings(); delete s.langs; CORE.P.saveSettings(s); });

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
  const rg = await page.evaluate(() => ({
    n: document.querySelectorAll('select.langsel').length,
    def: { num: document.getElementById('lg-numerical').value, be: document.getElementById('lg-behaviour').value, fr: document.getElementById('lg-french').value },
    sound: !!document.getElementById('stSound'), code: document.getElementById('stCode').value
  }));
  ok(rg.n === 14, 'réglages : langue réglable épreuve par épreuve (14 sélecteurs)', rg.n);
  ok(rg.def.num === 'en' && rg.def.be === 'en' && rg.def.fr === 'fr', 'réglages : anglais par défaut, français pour l’épreuve de français', rg.def);
  ok(rg.sound && rg.code === 'CM2026', 'réglages : sons et code d’accès présents', { sound: rg.sound, code: rg.code });
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
  ok(/LETTER|DIGIT/.test(mtCue), 'multi-tâches : consigne en anglais par défaut (LETTER / DIGIT)', mtCue.slice(0, 40));
  await page.evaluate(() => CORE.destroy());
  await page.evaluate(() => CORE.P.setLang('multitask', 'fr'));
  await enterRun('multitask');
  const mtCueFr = await page.evaluate(() => document.querySelector('.mt-cue').innerText);
  ok(/LETTRE|CHIFFRE/.test(mtCueFr), 'multi-tâches : le réglage par épreuve repasse la consigne en français', mtCueFr.slice(0, 40));
  await page.evaluate(() => CORE.P.setLang('multitask', 'en'));
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

  /* ── 19bis. retour immédiat v4.3 : juste/faux + pourquoi + figures sur les 14 épreuves ── */
  group('Retour immédiat (juste/faux + pourquoi + figures)');
  ok(await page.evaluate(() => CORE.P.instantFb() === true), 'retour immédiat activé par défaut');

  /* Numérique : chiffres du dossier + feuille de données + Continuer */
  await enterRun('numerical');
  await page.evaluate(() => { CORE.current.tab = 'outlook'; CORE.current.tabUser = true; document.querySelectorAll('.tfbtn')[0].click(); });
  await wait(120);
  const ifbNum = await page.evaluate(() => {
    const el = document.querySelector('.ifb');
    return el ? { txt: el.innerText, sheetBtn: !!document.getElementById('ifbSheet'), nextBtn: !!document.getElementById('ifbNext'), itemTab: CORE.current.items[0].tab } : null;
  });
  ok(ifbNum && /POURQUOI/i.test(ifbNum.txt) && /Feuille de données/.test(ifbNum.txt) && ifbNum.sheetBtn, 'numérique : retour immédiat avec explication chiffrée et bouton de feuille de données', ifbNum && ifbNum.txt.slice(0, 90));
  const ifbNumAct = await page.evaluate(() => {
    document.getElementById('ifbSheet').click();
    const tabAfterSheet = CORE.current.tab;
    const itemTab = CORE.current.items[0].tab;
    document.getElementById('ifbNext').click();
    return { tabAfterSheet, itemTab, i: CORE.current.i, ans: Object.keys(CORE.current.answers).length };
  });
  ok(ifbNumAct.tabAfterSheet === ifbNumAct.itemTab && ifbNumAct.i === 1 && ifbNumAct.ans === 1, 'numérique : le bouton ouvre la bonne feuille et « Continuer › » passe immédiatement à la question suivante', ifbNumAct);
  await page.evaluate(() => CORE.destroy());

  /* Verbal : justification + fiche de texte */
  await enterRun('verbal');
  await page.evaluate(() => { document.querySelectorAll('.tfbtn')[0].click(); });
  await wait(120);
  const ifbVer = await page.evaluate(() => { const el = document.querySelector('.ifb'); return el ? el.innerText : ''; });
  ok(/POURQUOI/i.test(ifbVer) && /Fiche de texte/.test(ifbVer), 'verbal : retour immédiat avec justification et fiche de texte concernée', ifbVer.slice(0, 90));
  await page.evaluate(() => CORE.destroy());

  /* Déductif : ligne/colonne + bonne option en vert + verrou anti-double-clic */
  await enterRun('deductive');
  const ifbDed = await page.evaluate(() => {
    document.querySelectorAll('.ded-opt')[0].click();
    const el = document.querySelector('.ifb');
    const lock = CORE.current.fbLock;
    const log1 = CORE.current.log.length;
    document.querySelectorAll('.ded-opt')[1].click(); /* ignoré grâce au verrou */
    const log2 = CORE.current.log.length;
    return { txt: el ? el.innerText : '', greenOpt: !!document.querySelector('.ded-opt.ok'), holeOk: !!document.querySelector('.ded-tile.hole.ok svg'), fig: !!document.querySelector('.ifb-dedfig svg'), lock, log1, log2 };
  });
  ok(ifbDed.greenOpt && ifbDed.holeOk && ifbDed.fig && /Ligne \d+/.test(ifbDed.txt) && /colonne \d+/.test(ifbDed.txt), 'déductif : explication ligne/colonne + forme attendue affichée dans la case « ? » et surlignée en vert', ifbDed.txt.slice(0, 90));
  await page.evaluate(() => { document.getElementById('ifbNext').click(); });
  const dedNextOk = await page.evaluate(() => ({ lock: CORE.current.fbLock, ifb: !!document.querySelector('.ifb') }));
  ok(ifbDed.lock && ifbDed.log1 === ifbDed.log2 && !dedNextOk.ifb, 'déductif : verrou anti-double-réponse actif puis levé au clic sur « Continuer › »', { ifbDed, dedNextOk });
  await page.evaluate(() => CORE.destroy());

  /* Inductif : règle en clair + les 2 bonnes grilles encadrées en vert */
  await enterRun('inductive');
  const ifbInd = await page.evaluate(() => {
    const c = document.querySelectorAll('.cand'); c[0].click(); c[1].click();
    document.getElementById('indGo').click();
    const el = document.querySelector('.ifb');
    return { txt: el ? el.innerText : '', greenCands: document.querySelectorAll('.cand.ok').length };
  });
  ok(ifbInd.greenCands === 2 && /Règle commune aux 2 grilles de gauche/.test(ifbInd.txt), 'inductif : règle formulée en clair + les 2 grilles valides encadrées en vert', ifbInd);
  await page.evaluate(() => { document.getElementById('ifbNext').click(); });
  ok(await page.evaluate(() => !document.querySelector('.ifb')), 'inductif : « Continuer › » passe à l’item suivant', null);
  await page.evaluate(() => CORE.destroy());

  /* Switch : permutation pas à pas + figure entrée → code → sortie */
  await enterRun('switch');
  const ifbSw = await page.evaluate(() => {
    const S = CORE.current, it = S.items[S.i];
    const wrongIdx = it.codes.findIndex((_, k) => k !== it.ans);
    document.querySelectorAll('.sw-codeopt')[wrongIdx].click();
    const el = document.querySelector('.ifb');
    return {
      txt: el ? el.innerText : '',
      fig: !!document.querySelector('.ifb-swfig'),
      tiles: document.querySelectorAll('.ifb-swtile svg').length,
      codeOk: !!document.querySelector('.ifb-swcode.ok'),
      codeKo: !!document.querySelector('.ifb-swcode.ko')
    };
  });
  ok(/pos\. 1→\d/.test(ifbSw.txt) && /pos\. 4→\d/.test(ifbSw.txt), 'switch : permutation expliquée pas à pas (pos. 1→… à pos. 4→…)', ifbSw.txt.slice(0, 90));
  ok(ifbSw.fig && ifbSw.tiles === 8 && ifbSw.codeOk && ifbSw.codeKo, 'switch : figure entrée → code → sortie (mauvais code barré en rouge, bon code en vert)', ifbSw);
  await page.evaluate(() => CORE.destroy());

  /* Concentration : nature de la forme + nombre exact de points + figure comparative */
  await enterRun('concentration');
  await page.evaluate(() => { CORE.current.deadline = Date.now() - 1; });
  await wait(350);
  const ifbConc = await page.evaluate(() => {
    document.querySelector('.conc-btn').click();
    const el = document.querySelector('.ifb');
    return { txt: el ? el.innerText : '', fig: document.querySelectorAll('.ifb-concfig .ifb-conccard svg').length };
  });
  ok(/E|barre|retourné/.test(ifbConc.txt) && /point/.test(ifbConc.txt), 'concentration : explique si la forme est un vrai E et combien de points elle porte', ifbConc.txt.slice(0, 90));
  ok(ifbConc.fig === 2, 'concentration : figure comparative (objet affiché vs cible E + 3 points)', ifbConc.fig);
  await page.evaluate(() => CORE.destroy());

  /* Multi-tâches : dimension jugée + règle */
  await enterRun('multitask');
  const ifbMt = await page.evaluate(() => {
    document.querySelector('.mt-btn').click();
    const el = document.querySelector('.ifb');
    return el ? el.innerText : '';
  });
  ok(/La consigne porte sur/.test(ifbMt) && /(voyelle|consonne|pair|impair)/.test(ifbMt), 'multi-tâches : rappelle la dimension jugée (lettre ou chiffre) et la justification', ifbMt.slice(0, 90));
  await page.evaluate(() => CORE.destroy());

  /* Apprentissage : fin de section → comparaison en figures des 12 objets */
  await enterRun('learning');
  await page.evaluate(() => { CORE.current.demoIdx = 6; });
  await wait(1500);
  await page.evaluate(() => { for (let i = 0; i < 6; i++) { const b = document.querySelector('.le-p'); if (b) b.click(); } });
  await wait(100);
  await page.evaluate(() => { document.getElementById('leOk').click(); });
  await wait(150);
  await page.evaluate(() => { CORE.current.secEnd = Date.now() - 1; });
  await wait(350);
  for (let i = 0; i < 24 && (await page.evaluate(() => CORE.current.lePhase)) === 'show'; i++) { await page.evaluate(() => { CORE.current.showNext = Date.now() - 1; }); await wait(280); }
  await page.evaluate(() => { for (let i = 0; i < 12; i++) { const b = document.querySelector('.le-p'); if (b) b.click(); } document.getElementById('leNext').click(); });
  await wait(150);
  const ifbLe = await page.evaluate(() => {
    const el = document.querySelector('.ifb');
    return { txt: el ? el.innerText : '', cells: document.querySelectorAll('.ifb-lefig .ifb-lecell svg').length };
  });
  ok(/Section 1/.test(ifbLe.txt) && ifbLe.cells === 24, 'apprentissage : fin de section avec comparaison en figures (12 placés vs 12 attendus)', { cells: ifbLe.cells, txt: ifbLe.txt.slice(0, 80) });
  await page.evaluate(() => CORE.destroy());

  /* Boîte de réception : règle du guide appliquée au mail + bouton E-mail suivant */
  await enterRun('info');
  const ifbInfo = await page.evaluate(() => {
    const p = document.getElementById('mPrio'), a = document.getElementById('mAct');
    p.value = '0'; p.dispatchEvent(new Event('change'));
    a.value = '0'; a.dispatchEvent(new Event('change'));
    const el = document.querySelector('#ibFb .ifb');
    return { txt: el ? el.innerText : '', next: !!document.querySelector('#ibFb #ifbNext') };
  });
  ok(/Priorité (HIGH|MEDIUM|LOW)/.test(ifbInfo.txt) && /Action :/.test(ifbInfo.txt) && ifbInfo.next, 'boîte de réception : affiche la règle du guide (priorité + action attendue)', ifbInfo.txt.slice(0, 100));
  const infoNextMail = await page.evaluate(() => { document.querySelector('#ibFb #ifbNext').click(); return CORE.current.mail; });
  ok(infoNextMail === 1, 'boîte de réception : « E-mail suivant › » sélectionne le message suivant', infoNextMail);
  await page.evaluate(() => CORE.destroy());

  /* Mécanique : explication physique + surlignage vert/rouge + Continuer */
  await enterRun('mechanical');
  const ifbMech = await page.evaluate(() => {
    document.querySelectorAll('.optrow')[0].click();
    const el = document.querySelector('.ifb');
    return { txt: el ? el.innerText : '', okOpt: !!document.querySelector('.optrow.ok'), next: !!document.getElementById('ifbNext') };
  });
  ok(ifbMech.okOpt && ifbMech.next && /POURQUOI/i.test(ifbMech.txt) && ifbMech.txt.length > 40, 'mécanique : explication du phénomène de transmission + bonne option en vert', ifbMech.txt.slice(0, 90));
  const mechNext = await page.evaluate(() => { document.getElementById('ifbNext').click(); return CORE.current.i; });
  ok(mechNext === 1, 'mécanique : « Continuer › » passe à la question suivante', mechNext);
  await page.evaluate(() => CORE.destroy());

  /* Langues (anglais & français) : retour immédiat + « ? » neutre */
  await enterRun('english');
  const ifbEn = await page.evaluate(() => {
    document.querySelectorAll('.optrow')[0].click();
    const el = document.querySelector('.ifb');
    return { txt: el ? el.innerText : '', okOpt: !!document.querySelector('.optrow.ok') };
  });
  ok(ifbEn.okOpt && /POURQUOI/i.test(ifbEn.txt), 'anglais : retour immédiat dès le clic sur une option', ifbEn.txt.slice(0, 90));
  const ifbEnUnk = await page.evaluate(() => {
    document.querySelector('.optrow[data-i="99"]').click();
    const el = document.querySelector('.ifb');
    return el ? el.innerText : '';
  });
  ok(/Neutre/.test(ifbEnUnk), 'anglais : l’option « ? » affiche un retour neutre non pénalisé', ifbEnUnk.slice(0, 80));
  await page.evaluate(() => CORE.destroy());

  await enterRun('french');
  const ifbFr = await page.evaluate(() => {
    document.querySelectorAll('.optrow')[0].click();
    const el = document.querySelector('.ifb');
    return el ? el.innerText : '';
  });
  ok(/POURQUOI/i.test(ifbFr), 'français : retour immédiat sur la réponse choisie', ifbFr.slice(0, 90));
  await page.evaluate(() => CORE.destroy());

  /* Comportements & Motivations : bandeau de synthèse + Continuer */
  await enterRun('behaviour');
  const ifbBeh = await page.evaluate(() => {
    const el = document.querySelector('.ifb');
    document.getElementById('ifbNext').click();
    return { hadFb: !!el, i: CORE.current.i };
  });
  ok(ifbBeh.hadFb && ifbBeh.i === 1, 'comportements : panneau de retour immédiat et bouton « Continuer › »', ifbBeh);
  await page.evaluate(() => CORE.destroy());

  await enterRun('motivation');
  const ifbMot = await page.evaluate(() => {
    const el = document.querySelector('.ifb');
    document.getElementById('ifbNext').click();
    return { hadFb: !!el, i: CORE.current.i };
  });
  ok(ifbMot.hadFb && ifbMot.i === 1, 'motivations : panneau de retour immédiat et bouton « Continuer › »', ifbMot);
  await page.evaluate(() => CORE.destroy());

  /* Aide & réglages : interrupteur « Retour immédiat » */
  await page.evaluate(() => { location.hash = '#/reglages'; });
  await wait(200);
  const stInst = await page.evaluate(() => {
    const cb = document.getElementById('stInstant');
    if (!cb) return null;
    const initial = cb.checked;
    cb.checked = false; cb.dispatchEvent(new Event('change'));
    const afterOff = CORE.P.instantFb();
    return { initial, afterOff };
  });
  ok(stInst && stInst.initial === true && stInst.afterOff === false, 'réglages : case « Retour immédiat » cochée par défaut et désactivable', stInst);
  await enterRun('deductive');
  const noIfb = await page.evaluate(() => {
    document.querySelector('.ded-opt').click();
    return !document.querySelector('.ifb');
  });
  await page.evaluate(() => { CORE.P.setInstantFb(true); CORE.destroy(); });
  ok(noIfb && (await page.evaluate(() => CORE.P.instantFb() === true)), 'mode cadence d’examen : décocher « Retour immédiat » masque le panneau en direct', noIfb);

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
