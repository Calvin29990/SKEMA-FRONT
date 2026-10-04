/* Test de conformité — charge les vrais scripts et démarre chaque nouvelle section bancaire. */
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
const sandbox = {
  console,
  localStorage: { getItem: () => null, setItem() {}, removeItem() {} },
  setInterval: () => 0, clearInterval() {}, setTimeout: () => 0, clearTimeout() {},
  URL: { createObjectURL: () => '' },
  AudioContext: undefined,
  navigator: { userAgent: 'node' },
  matchMedia: () => ({ matches: false, addListener() {}, addEventListener() {} })
};
sandbox.document = { body: mkEl(), getElementById: () => mkEl(), createElement: () => mkEl(), querySelector: () => null, querySelectorAll: () => [], addEventListener() {}, documentElement: mkEl() };
sandbox.window = sandbox;
sandbox.globalThis = sandbox;
const ctx = vm.createContext(sandbox);
const dir = path.join(__dirname, '..', 'assets', 'js');
for (const f of ['util.js', 'banks.js', 'drills.js', 'core.js']) {
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
ok((byBank.UBS || []).length === 3, 'UBS : 3 modules → ' + (byBank.UBS || []).join(', '));
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
  'ubs-num': 37, 'ubs-verb': 18, 'ubs-cult': 24,
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

console.log(fails ? '\n' + fails + ' ÉCHEC(S)' : '\nTOUS LES TESTS PASSENT');
process.exit(fails ? 1 : 0);
