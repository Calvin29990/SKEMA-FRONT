/* Test de conformité v4.6 — charge les vrais scripts et démarre chaque section bancaire.
   Vérifie aussi les trois formats UBS, les thèmes par banque et le flux chat Morgan Stanley. */
'use strict';
const fs = require('fs'), path = require('path'), vm = require('vm');

const mkEl = () => new Proxy(function () {}, {
  get(t, p) {
    if (p === Symbol.toPrimitive || p === 'toString') return () => '';
    if (p === 'classList') return { add() {}, remove() {}, toggle() {}, contains: () => false };
    if (p === 'style' || p === 'dataset') return {};
    if (p === 'children' || p === 'childNodes') return [];
    if (p === 'querySelector') return () => null;
    if (p === 'querySelectorAll') return () => [];
    if (p === Symbol.iterator) return function* () {}[Symbol.iterator];
    if (typeof p === 'symbol') return undefined;
    return mkEl();
  },
  set: () => true,
  apply: () => mkEl()
});

/* body : objet plain qui trace setAttribute/removeAttribute (thèmes par banque) */
const bodyStub = {
  _attrs: {},
  setAttribute(k, v) { this._attrs[k] = String(v); },
  removeAttribute(k) { delete this._attrs[k]; },
  getAttribute(k) { return k in this._attrs ? this._attrs[k] : null; },
  classList: { add() {}, remove() {}, toggle() {}, contains: () => false }
};
/* view : objet plain (le Proxy ne stocke pas les surcharges innerHTML) */
const viewStub = { innerHTML: '', className: '', querySelector: () => null, querySelectorAll: () => [], appendChild() {} };

const sandbox = {
  console,
  localStorage: { getItem: () => null, setItem() {}, removeItem() {} },
  setInterval: () => 0, clearInterval() {}, setTimeout: () => 0, clearTimeout() {},
  URL: { createObjectURL: () => '' },
  AudioContext: undefined,
  navigator: { userAgent: 'node' },
  matchMedia: () => ({ matches: false, addListener() {}, addEventListener() {} })
};
sandbox.document = {
  body: bodyStub,
  getElementById: (id) => (id === 'view' ? viewStub : mkEl()),
  createElement: () => mkEl(),
  querySelector: () => null,
  querySelectorAll: () => [],
  addEventListener() {},
  documentElement: mkEl()
};
sandbox.window = sandbox;
sandbox.globalThis = sandbox;
const ctx = vm.createContext(sandbox);
const dir = path.join(__dirname, '..', 'assets', 'js');
for (const f of ['util.js', 'banks.js', 'ubs.js', 'drills.js', 'core.js']) {
  vm.runInContext(fs.readFileSync(path.join(dir, f), 'utf8'), ctx, { filename: f });
}
const CORE = sandbox.CORE, BANK = sandbox.BANK;

let fails = 0;
const ok = (cond, msg) => { console.log((cond ? 'PASS' : 'FAIL') + ' — ' + msg); if (!cond) fails++; };

/* 1. Catalogue : 14 anciennes + 13 nouvelles sections bancaires */
const bankIds = CORE.SECTIONS.filter(s => s.bank).map(s => s.id);
ok(bankIds.length === 13, '13 sections bancaires au catalogue (trouvé ' + bankIds.length + ')');
const byBank = {};
CORE.SECTIONS.filter(s => s.bank).forEach(s => { (byBank[s.bank] = byBank[s.bank] || []).push(s.id); });
ok((byBank.BNP || []).length === 5, 'BNP : 5 modules → ' + (byBank.BNP || []).join(', '));
ok((byBank.UBS || []).length === 3 && (byBank.UBS || []).join(',') === 'ubs-num,ubs-cult,ubs-ind', 'UBS : les 3 nouveaux modules → ' + (byBank.UBS || []).join(', '));
ok((byBank.MS || []).length === 5, 'MS : 5 modules → ' + (byBank.MS || []).join(', '));
ok(CORE.BANKS.BNP && CORE.BANKS.UBS && CORE.BANKS.MS, 'CORE.BANKS exporté pour les 3 banques');

/* 2. Chaque section a une intro FR+EN */
CORE.SECTIONS.forEach(s => {
  const pages = BANK.INTRO[s.id];
  const good = pages && pages.length && pages.every(p => p && typeof p.fr === 'string' && p.fr.length > 50 && typeof p.en === 'string' && p.en.length > 50);
  ok(good, 'INTRO FR/EN présent pour ' + s.id);
});

/* 3. start() sur chaque nouvelle section : items conformes au format documenté */
const expect = {
  'bnp-num': 9, 'bnp-ps': 10, 'bnp-log': 0, 'bnp-sjt': 13, 'bnp-det': 0,
  'ubs-num': 18, 'ubs-cult': 18, 'ubs-ind': 0,   /* Numeric: 18 items; culture: 18 scenarios; inductive: generated */
  'ms-num': 18, 'ms-verb': 30, 'ms-ind': 0, 'ms-sw': 0, 'ms-sjt': 13
};
for (const id of bankIds) {
  CORE.start(id);
  const S = CORE.current;
  ok(S && S.sec.id === id, 'start(' + id + ') ouvre la session');
  if (expect[id] > 0) ok(S.items.length === expect[id], id + ' : ' + S.items.length + ' questions (attendu ' + expect[id] + ')');
  if (S.sec.timed) ok(S.sec.timed > 0, id + ' : chrono ' + S.sec.timed + ' s');
  CORE.destroy();
}

/* 4. Non régression : les 14 sections d'origine démarrent toujours */
for (const s of CORE.SECTIONS.filter(x => !x.bank)) {
  CORE.start(s.id);
  ok(CORE.current && CORE.current.sec.id === s.id, 'non-régression start(' + s.id + ')');
  CORE.destroy();
}

/* 5. Clés STR ajoutées */
ok(typeof BANK.STR.fr.blkSjt === 'string' && typeof BANK.STR.en.blkSjt === 'string', 'STR.blkSjt FR+EN');
['chatOnline', 'chatTyping', 'chatPlaceholder', 'chatSend', 'chatNextLbl', 'chatNextCta'].forEach(k => {
  ok(typeof BANK.STR.fr[k] === 'string' && typeof BANK.STR.en[k] === 'string', 'STR.' + k + ' FR+EN');
});

/* 6. v4.5 — thèmes par banque : data-bank posé sur body pendant la session, retiré après */
const themeOf = { 'bnp-num': 'BNP', 'ubs-num': 'UBS', 'ms-num': 'MS' };
for (const id of Object.keys(themeOf)) {
  CORE.start(id);
  ok(bodyStub._attrs['data-bank'] === themeOf[id], 'thème : data-bank="' + themeOf[id] + '" posé pendant ' + id);
  CORE.destroy();
  ok(!('data-bank' in bodyStub._attrs), 'thème : data-bank retiré après destroy(' + id + ')');
}

/* 7. v4.5 — Morgan Stanley chatAssess : kind chatsjt, 13 scénarios FR/EN, chaînage ms-num */
const sjt = CORE.byId('ms-sjt');
ok(sjt.kind === 'chatsjt', 'ms-sjt : kind "chatsjt" (trouvé ' + sjt.kind + ')');
ok(sjt.next === 'ms-num', 'ms-sjt : chaînage vers le test suivant (ms-num)');
ok(Array.isArray(BANK.msChat) && BANK.msChat.length === 13, 'BANK.msChat : 13 scénarios de chat (trouvé ' + (BANK.msChat || []).length + ')');
ok(BANK.msChat.every(c => typeof c.from === 'string' && c.from.length > 3 &&
   Array.isArray(c.in) && typeof c.in[0] === 'string' && c.in[0].length > 40 &&
   typeof c.in[1] === 'string' && c.in[1].length > 40),
   'BANK.msChat : chaque scénario a un expéditeur + message FR et EN');

/* 8. v4.5 — flux chat complet : 13 réponses → log comportemental → finish() */
CORE.start('ms-sjt');
ok(bodyStub._attrs['data-bank'] === 'MS', 'chat : thème MS actif pendant la session');
CORE.__beginRun();
let S = CORE.current;
ok(S.phase === 'run', 'chat : beginRun passe en phase run');
ok(S.sec.timed === 600 && S.deadline > 0, 'chat : chrono 10:00 armé');
CORE.__chat.arrive(0);   /* dans l'UI : setTimeout 700 ms (indicateur de frappe) */
for (let i = 0; i < 13; i++) {
  ok(S.chatAwaiting === true, 'chat : scénario ' + (i + 1) + '/13 en attente de réponse');
  CORE.__chat.send('Réponse pro au scénario ' + (i + 1) + ' : je vérifie, je respecte la procédure et j’escalade au bon niveau.');
  CORE.__chat.arrive(i + 1);   /* dans l'UI : setTimeout 900 ms après l'envoi */
}
ok(S.log.length === 13, 'chat : 13 réponses loggées (trouvé ' + S.log.length + ')');
ok(S.log.every(r => !('ok' in r)), 'chat : aucune entrée "ok" → agrégé comme comportemental');
ok(S.log.every(r => typeof r.given === 'string' && r.given.length > 10), 'chat : chaque réponse texte est enregistrée');
ok(S.chatDone === true, 'chat : message final avec lien vers le test suivant reçu');
ok(/Numerical Reasoning/.test(S.chatMsgs[S.chatMsgs.length - 1].text), 'chat : le message final pointe vers Numerical Reasoning');
CORE.finish();
ok(S.attempt && S.attempt.behavioural === true, 'finish() : session chatAssess enregistrée (behavioural)');
ok(S.attempt && S.attempt.answered === 13, 'finish() : 13 réponses agrégées (trouvé ' + (S.attempt && S.attempt.answered) + ')');
ok(S.attempt && S.attempt.section === 'ms-sjt', 'finish() : rattaché à la section ms-sjt');
CORE.destroy();
ok(!('data-bank' in bodyStub._attrs), 'chat : thème retiré après la session');

/* 9. UBS — contenu original, formats documentés et trois modules correctement câblés */
ok(BANK.ubsNumericalSheets.length === 6, 'ubs-num : six feuilles de données');
ok(BANK.ubsNumerical.length === 18 && BANK.ubsNumerical.every(q => [0, 1, 2].includes(q.a) && BANK.ubsNumericalSheets.some(s => s.id === q.tab)), 'ubs-num : 18 questions, chacune rattachée à une feuille et une réponse T/F/Cannot Say');
ok(BANK.ubsNumerical.some(q => q.a === 2), 'ubs-num : inclut des questions CANNOT SAY');
ok(CORE.byId('ubs-cult').kind === 'culture' && CORE.byId('ubs-cult').blocks === 18, 'ubs-cult : type dédié, 18 scénarios');
CORE.start('ubs-cult');
ok(CORE.current.items.length === 18 && CORE.current.items.every(q => q.actions.length === 3 && q.best !== q.least), 'ubs-cult : 18 scénarios × 3 options, clés Most / Least distinctes');
ok(CORE.current.examples.length === 1 && !CORE.current.sec.timed, 'ubs-cult : exemple guidé et aucune limite de temps');
CORE.__beginRun();
const cultureSession = CORE.current;
cultureSession.log = Array.from({ length: 18 }, (_, i) => ({
  n: i + 1, q: 'Situation ' + (i + 1), given: 'Most A · Least C', correct: 'Most A · Least C',
  ok: i < 10, mostOk: i < 12, leastOk: i < 10, ms: 1000, section: 'ubs-cult', why: 'Practice scoring check.'
}));
CORE.finish();
ok(cultureSession.attempt && cultureSession.attempt.items === 36 && cultureSession.attempt.correct === 22 && cultureSession.attempt.answered === 36 && Math.abs(cultureSession.attempt.accuracy - 22 / 36) < 1e-9, 'ubs-cult : score Most + Least sur 36 décisions');
CORE.destroy();
CORE.start('ubs-num');
ok(CORE.current.items.length === 18 && CORE.current.examples.length === 3 && CORE.current.sec.timed === 360, 'ubs-num : 18 questions, 3 exemples, chrono 6:00');
CORE.destroy();
CORE.start('ubs-ind');
ok(CORE.current.sec.kind === 'pick2' && CORE.current.examples.length === 3 && CORE.current.sec.timed === 360, 'ubs-ind : grilles pick-two, 3 exemples, chrono 6:00');
CORE.destroy();

console.log(fails ? '\n' + fails + ' ÉCHEC(S)' : '\nTOUS LES TESTS PASSENT');
process.exit(fails ? 1 : 0);
