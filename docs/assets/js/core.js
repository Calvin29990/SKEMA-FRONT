/* ═══════════════════════════════════════════════════════════════
   core.js — registre des épreuves conformes au document, moteur de
   session (intros, exemples, chronos globaux, navigation, score),
   profils, progression, export CSV/JSON.
   Assessment Trainer — Calvin MINANG — usage personnel.
   ═══════════════════════════════════════════════════════════════ */
'use strict';

const CORE = (() => {

  /* ═══════════════ REGISTRE — ordre et libellés de l'accueil réel ═══════════════ */
  const SECTIONS = [
    { id: 'behaviour',     home: 'Comportements professionnels',              head: 'Work-related Behaviour',                min: 18, kind: 'blocks',   blocks: 48 },
    { id: 'motivation',    home: 'Motivations et Intérêts Professionnels',    head: 'Work-related Interests and Motives',    min: 18, kind: 'blocks',   blocks: 36 },
    { id: 'numerical',     home: 'Raisonnement numérique',                    head: 'Numerical Reasoning',                   min: 15, kind: 'numverb',  timed: 720,  src: 'num' },
    { id: 'verbal',        home: 'Raisonnement verbal',                       head: 'Verbal Reasoning',                      min: 15, kind: 'numverb',  timed: 720,  src: 'verb' },
    { id: 'deductive',     home: 'Pensée logique déductive',                  head: 'Deductive-logical Thinking',            min: 9,  kind: 'latin',    timed: 360 },
    { id: 'inductive',     home: 'Raisonnement Inductif',                     head: 'Inductive Reasoning',                   min: 9,  kind: 'pick2',    timed: 360 },
    { id: 'concentration', home: 'Capacité de Concentration',                 head: 'Ability to Concentrate',                min: 5,  kind: 'edots',    timed: 120, exTime: 30 },
    { id: 'multitask',     home: 'Capacité multi-tâches',                     head: 'Multi-tasking',                         min: 8,  kind: 'mt',       timed: 300, noDetail: true },
    { id: 'learning',      home: 'Capacité d’apprentissage',             head: 'Learning Efficiency',                   min: 9,  kind: 'seqmem',  timed: 300 },
    { id: 'info',          home: 'Traitement de l’information',          head: 'Information Handling',                  min: 18, kind: 'inbox',    timed: 900 },
    { id: 'english',       home: 'Compétences Linguistiques - Anglais',  head: 'Competences Linguistiques - Anglais',  min: 13, kind: 'lang',     lang: 'en' },
    { id: 'french',        home: 'Compétences Linguistiques - Français', head: 'Compétences Linguistiques - Français', min: 13, kind: 'lang',     lang: 'fr' },
    { id: 'mechanical',    home: 'Raisonnement Mécanique',                    head: 'Mechanical Reasoning',                  min: 18, kind: 'mech',     timed: 900 },
    { id: 'switch',        home: 'Raisonnement Déductif - switchChallenge',   head: 'Deductive Reasoning - switchChallenge', min: 9,  kind: 'switchcode', timed: 360 },

    /* ══ BNP Paribas — Maki (plateforme depuis 2025). Formats documentés publiquement :
       psychotechniquetest.fr/bnp-paribas · psychotechnique.lu/bnp-paribas · test-banque.fr/bnp-paribas.
       Modules : numérique 9 q./10 min · logique élémentaire 13 q./8 min · résolution de problèmes
       10 q./10 min · jugement situationnel « communication efficace » 13 q./10 min · attention aux
       détails 10 q./12 min · anglais 16 q./5 min · français 21 q./6 min.
       Scoring : (bonnes ÷ total) − (erreurs × 0,5), plancher 0 ; seuils ~65-68 % BDDF, ~72 % CIB.
       Les questions restent la banque d'entraînement de cette plateforme. ══ */
    { id: 'bnp-num', bank: 'BNP', home: 'BNP Maki — raisonnement numérique (9 q. / 10 min)', head: 'BNP Maki — numerical reasoning (9 items / 10 min)', min: 10, kind: 'numverb', src: 'num', cap: 9, timed: 600 },
    { id: 'bnp-log', bank: 'BNP', home: 'BNP Maki — raisonnement logique (13 q. / 8 min)', head: 'BNP Maki — logical reasoning (13 items / 8 min)', min: 8, kind: 'pick2', timed: 480 },
    { id: 'bnp-ps', bank: 'BNP', home: 'BNP Maki — résolution de problèmes (10 q. / 10 min)', head: 'BNP Maki — problem solving (10 items / 10 min)', min: 10, kind: 'numverb', src: 'num', cap: 10, timed: 600 },
    { id: 'bnp-sjt', bank: 'BNP', home: 'BNP Maki — SJT « communication efficace » (jugement situationnel, 13 q. / 10 min)', head: 'BNP Maki — SJT “effective communication” (situational judgement, 13 items / 10 min)', min: 10, kind: 'blocks', blocks: 13, timed: 600, sjt: true },
    { id: 'bnp-det', bank: 'BNP', home: 'BNP Maki — attention aux détails (10 q. / 12 min)', head: 'BNP Maki — attention to detail (10 items / 12 min)', min: 12, kind: 'edots', timed: 720, exTime: 30 },

    /* ══ UBS — formats déjà présents (Aon / Korn Ferry). ══ */
    { id: 'ubs-num', bank: 'UBS', home: 'UBS — raisonnement numérique Aon (37 q. / 12 min)', head: 'UBS — Aon numerical reasoning (37 items / 12 min)', min: 12, kind: 'numverb', src: 'num', timed: 720 },
    { id: 'ubs-verb', bank: 'UBS', home: 'UBS — raisonnement logique/inductif (18 q. / 6 min)', head: 'UBS — logical/inductive reasoning (18 items / 6 min)', min: 6, kind: 'numverb', src: 'verb', cap: 18, timed: 360 },
    { id: 'ubs-cult', bank: 'UBS', home: 'UBS — Culture Match (préférences, 18 blocs)', head: 'UBS — Culture Match (preferences, 18 blocks)', min: 15, kind: 'blocks', blocks: 18 },

    /* ══ UBS — trois formats supplémentaires d’après les documents fournis.
       Ces nouveaux exercices et jeux de données sont originaux et fictifs. ══ */
    { id: 'ubs-num-18', bank: 'UBS', home: 'UBS — numérique (18 questions / 6 min · documents fournis)', head: 'UBS — numerical reasoning (18 items / 6 min · supplied format)', min: 6, kind: 'numverb', src: 'ubs', cap: 18, timed: 360 },
    { id: 'ubs-cult-action', bank: 'UBS', home: 'UBS — Culture Match (18 scénarios, plus/moins efficaces)', head: 'UBS — Culture Match (18 scenarios, most/least effective)', min: 20, kind: 'culture', blocks: 18 },
    { id: 'ubs-ind', bank: 'UBS', home: 'UBS — raisonnement inductif par grilles (6 min)', head: 'UBS — inductive reasoning with grids (6 min)', min: 6, kind: 'pick2', timed: 360 },

    /* ══ Morgan Stanley — Online Assessment selon poste/région : SHL (IBD/S&T notamment)
       ou Aon/cut-e (campus EMEA). Sources : forgeprep.io · careertestprep.com · preplounge.com ·
       gameassessmentprep.com. SHL : numérique 18 q./25 min · verbal 30 q./19 min · inductif 24 q./25 min.
       Aon EMEA : numérique + déductif + SJT chat + switchChallenge. ══ */
    { id: 'ms-num', bank: 'MS', home: 'Morgan Stanley — numérique (SHL, 18 q. / 25 min)', head: 'Morgan Stanley — numerical (SHL, 18 items / 25 min)', min: 25, kind: 'numverb', src: 'num', cap: 18, timed: 1500 },
    { id: 'ms-verb', bank: 'MS', home: 'Morgan Stanley — verbal (SHL, 30 q. / 19 min)', head: 'Morgan Stanley — verbal (SHL, 30 items / 19 min)', min: 19, kind: 'numverb', src: 'verb', cap: 30, timed: 1140 },
    { id: 'ms-ind', bank: 'MS', home: 'Morgan Stanley — inductif (SHL, 24 q. / 25 min)', head: 'Morgan Stanley — inductive (SHL, 24 items / 25 min)', min: 25, kind: 'pick2', timed: 1500 },
    { id: 'ms-sw', bank: 'MS', home: 'Morgan Stanley — switchChallenge (Aon)', head: 'Morgan Stanley — switchChallenge (Aon)', min: 9, kind: 'switchcode', timed: 360 },
    { id: 'ms-sjt', bank: 'MS', home: 'Morgan Stanley — chatAssess · SJT chat façon WhatsApp (13 scénarios / 10 min)', head: 'Morgan Stanley — chatAssess · chat-based SJT (13 scenarios / 10 min)', min: 10, kind: 'chatsjt', blocks: 13, timed: 600, next: 'ms-num' }
  ];

  /* Groupes affichés sur l'accueil (dans l'ordre d'apparition de SECTIONS). */
  const BANKS = {
    BNP: { title: 'BNP Paribas — Maki (plateforme depuis 2025)', src: 'Formats documentés : psychotechniquetest.fr · test-banque.fr · Glassdoor (process CIB stagiaires). Scoring Maki : (bonnes ÷ total) − (erreurs × 0,5), plancher 0. Modules anglais/français ≈ sections « Compétences Linguistiques » ci-dessus.' },
    UBS: { title: 'UBS — Online Assessment · 6 entraînements', src: 'Formats Aon/Korn Ferry existants, complétés par les trois formats des documents fournis : numérique (18 questions / 6 min), Culture Match (18 scénarios, plus/moins efficaces) et inductif par grilles (6 min). Les nouveaux exercices sont originaux et fictifs.' },
    MS: { title: 'Morgan Stanley — Online Assessment (SHL ou Aon)', src: 'Formats documentés : forgeprep.io · careertestprep.com · preplounge.com — SHL (IBD/S&T) ou Aon/cut-e (campus EMEA) selon le poste ; cut-scores numériques parmi les plus élevés. Aon chatAssess : répondre aux messages de collègues dans une interface de chat (retours candidats : Wall Street Oasis, mconsultingprep).' }
  };
  const byId = (id) => SECTIONS.find(s => s.id === id);

  /* ═══════════════ Stockage, profils, réglages ═══════════════ */
  const PROFILES = {
    list() { return U.store.get('users', []); },
    current() { return U.store.get('user', null); },
    set(n) { n = String(n || '').trim().replace(/\s+/g, ' '); n = n.split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join(' '); if (n && !this.list().includes(n)) { const l = this.list(); l.push(n); U.store.set('users', l); } U.store.set('user', n); return n; },
    logout() { U.store.del('user'); },
    purge(n) { const l = this.list().filter(x => x !== n); U.store.set('users', l); U.store.del('attempts::' + n); U.store.del('details::' + n); if (this.current() === n) U.store.del('user'); return l; }
  };
  const P = {
    key(k) { return k + '::' + (PROFILES.current() || 'Invité'); },
    attempts() { return U.store.get(this.key('attempts'), []); },
    details() { return U.store.get(this.key('details'), {}); },
    settings() { return U.store.get('settings', { sound: false, keyboard: true, instantFb: true, code: 'CM2026', langs: {} }); },
    saveSettings(s) { U.store.set('settings', s); },
    instantFb() { return this.settings().instantFb !== false; },
    setInstantFb(v) { const s = this.settings(); s.instantFb = !!v; this.saveSettings(s); },
    code() { return String(this.settings().code || 'CM2026').trim().toUpperCase(); },
    lang(sec) {
      const id = sec && sec.id ? sec.id : sec;
      const l = this.settings().langs || {};
      if (l[id]) return l[id];
      /* Par défaut les épreuves s'affichent en anglais (langue du test réel) ;
         seules les épreuves de langues gardent leur langue propre. L'habillage
         (accueil, progression, feedback, aide) reste en français. */
      return id === 'french' ? 'fr' : 'en';
    },
    setLang(sec, v) { const s = this.settings(); s.langs = s.langs || {}; s.langs[sec] = v; this.saveSettings(s); },
    add(attempt, detail) { const a = this.attempts(); a.push(attempt); U.store.set(this.key('attempts'), a.slice(-800)); if (detail && detail.length) { const d = this.details(); d[attempt.id] = detail; const ids = Object.keys(d); if (ids.length > 80) delete d[ids[0]]; U.store.set(this.key('details'), d); } },
    clear() { U.store.del(this.key('attempts')); U.store.del(this.key('details')); },
    sessionLog(id) { return this.details()[id] || []; },
    sessionOf(id) { return this.attempts().find(x => x.id === id) || null; },
    statsFor(id) {
      const all = this.attempts().filter(x => x.section === id);
      const gr = all.filter(x => x.accuracy !== null && x.accuracy !== undefined);
      if (!all.length) return null;
      if (!gr.length) return { n: all.length, behavioural: true, best: null, last: null, avgMs: all.reduce((a, b) => a + (b.avgMs || 0), 0) / all.length, lastAt: all[all.length - 1].at };
      const acc = gr.map(x => x.accuracy);
      return { n: gr.length, best: Math.max(...acc), last: acc[acc.length - 1], avg: acc.reduce((a, b) => a + b, 0) / acc.length, avgMs: gr.reduce((a, b) => a + (b.avgMs || 0), 0) / gr.length, lastAt: gr[gr.length - 1].at };
    },
    overall() {
      const a = this.attempts().filter(x => x.accuracy !== null && x.accuracy !== undefined);
      const items = a.reduce((s, x) => s + x.items, 0), correct = a.reduce((s, x) => s + x.correct, 0);
      return { n: this.attempts().length, correct, items, accuracy: items ? correct / items : 0, minutes: this.attempts().reduce((s, x) => s + (x.ms || 0), 0) / 60000 };
    },
    wrongs(limit = 40) {
      const d = this.details(), out = [];
      Object.keys(d).sort().reverse().forEach(k => (d[k] || []).forEach(it => {
        if (it && it.ok === false) out.push(Object.assign({ sess: k }, it, { sectionName: (byId(it.section) || {}).home || it.section }));
      }));
      return out.slice(0, limit);
    },
    PROFILES,                       /* alias : P.PROFILES.current() */
    csv(id) {
      const a = this.sessionOf(id) || {}, log = this.sessionLog(id);
      const c = v => '"' + String(v == null ? '' : v).replace(/"/g, '""').replace(/\s+/g, ' ').trim() + '"';
      const head = ['Profil', 'Session', 'Date', 'Heure', 'Section', 'N°', 'Question', 'Réponse donnée', 'Réponse correcte', 'Résultat', 'Temps (ms)', 'Explication'];
      const rows = log.map((r, i) => [PROFILES.current() || '', id, a.date || '', a.time || '', c(a.sectionName || ''), (r.n || i + 1), c(r.q), c(r.given), c(r.correct), c(r.ok === true ? 'Correcte' : r.ok === false ? 'Incorrecte' : 'Sans bonne réponse'), r.ms == null ? '' : r.ms, c(r.why)]);
      const blob = new Blob(['\ufeff' + [head.map(c).join(';')].concat(rows.map(r => r.join(';'))).join('\r\n')], { type: 'text/csv;charset=utf-8' });
      const url = URL.createObjectURL(blob), lk = document.createElement('a');
      lk.href = url; lk.download = 'detail-session-' + id + '.csv'; lk.click();
      U.toast('Détail exporté (CSV)');
    }
  };

  /* ═══════════════ Aides & moteur de retour immédiat ═══════════════ */
  const STR = (sec) => BANK.STR[P.lang(sec.id || sec)] || BANK.STR.fr;
  const mmss = (s) => { s = Math.max(0, Math.ceil(s)); return String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'); };
  const esc = U.esc;
  const symSVG = (spec, size) => U.shape(spec.kind, spec.color, { sw: 9 });

  const SYM_NAMES_DED = ['carré rouge', 'rond vert', 'triangle bleu', 'croix bleue'];
  const SYM_NAMES_SW  = ['triangle jaune', 'croix bleue', 'rond vert', 'carré rouge'];
  const IND_RULE_WHY = {
    corners: 'les 4 coins de la grille portent le même symbole',
    row:     'une ligne entière porte le même symbole',
    col:     'une colonne entière porte le même symbole',
    mirror:  'chaque ligne est symétrique gauche ↔ droite (1re et 3e colonnes identiques)',
    ring:    'les 8 cases du pourtour portent le même symbole'
  };

  function dedWhy(it) {
    const hr = it.hole[0], hc = it.hole[1];
    const ansSym = it.options[it.ans];
    const rowShown = [0, 1, 2, 3].filter(x => x !== hc && it.shown[hr + ',' + x] != null).length;
    const colShown = [0, 1, 2, 3].filter(y => y !== hr && it.shown[y + ',' + hc] != null).length;
    const others = [0, 1, 2, 3].filter(k => k !== ansSym).map(k => SYM_NAMES_DED[k]).join(', ');
    return 'Ligne ' + (hr + 1) + ', colonne ' + (hc + 1) + ' — la ligne du ? en montre déjà ' + Math.max(rowShown, 3) + ' et la colonne ' + colShown + ' (' + others + ') : une seule forme reste possible → ' + SYM_NAMES_DED[ansSym] + ' (option ' + (it.ans + 1) + ').';
  }
  function indWhy(it) {
    const ruleTxt = IND_RULE_WHY[it.rule] || 'les deux grilles d’exemple partagent la même règle de position';
    const pairTxt = it.good.map(x => x + 1).join(' et ');
    return 'Règle commune aux 2 grilles de gauche : ' + ruleTxt + ' — seules les grilles ' + pairTxt + ' (encadrées en vert) la respectent.';
  }
  function swWhy(it) {
    const code = it.codes[it.ans];
    const ord = n => n === 1 ? '1ᵉ' : n + 'ᵉ';
    const steps = code.map((d, p) => 'pos. ' + (p + 1) + '→' + d + ' (la ' + ord(d) + ' forme, ' + SYM_NAMES_SW[it.input[d - 1]] + ', passe en position ' + (p + 1) + ')').join(', ');
    return 'Permutation pas à pas : ' + steps + ' → code ' + code.join(' ') + '.';
  }
  function swFigHTML(it, givenIdx) {
    const good = it.codes[it.ans];
    const bad = (givenIdx != null && givenIdx !== it.ans && it.codes[givenIdx]) ? it.codes[givenIdx] : null;
    const inRow = '<div class="ifb-swrow"><span class="ifb-swlbl">Entrée</span>' +
      it.input.map((k, idx) => '<div class="ifb-swtile"><i>' + (idx + 1) + '</i>' + symSVG(BANK.SYM_SW[k]) + '</div>').join('') + '</div>';
    const midRow = '<div class="ifb-swmid">' +
      (bad ? '<span class="ifb-swcode ko" title="Code choisi">' + bad.join(' ') + '</span><span class="ifb-swarr">→</span>' : '') +
      '<span class="ifb-swcode ok" title="Bon code">' + good.join(' ') + '</span></div>';
    const outRow = '<div class="ifb-swrow"><span class="ifb-swlbl">Sortie</span>' +
      it.output.map((k, idx) => '<div class="ifb-swtile"><i>←' + good[idx] + '</i>' + symSVG(BANK.SYM_SW[k]) + '</div>').join('') + '</div>';
    return '<div class="ifb-swfig">' + inRow + midRow + outRow + '</div>';
  }
  function concWhy(it) {
    const n = it.dots.length;
    const pts = n + ' point' + (n > 1 ? 's' : '') + (n > 1 ? ' l’entourent' : ' l’entoure');
    if (it.shape === 'E' && n === 3) {
      return 'C’est bien un E complet (3 barres horizontales) et exactement 3 points l’entourent → réponse attendue : CORRECT.';
    }
    if (it.shape === 'E') {
      return 'C’est bien un E, mais ' + pts + ' — il en faudrait exactement 3 → réponse attendue : INCORRECT.';
    }
    const shapeWhy = it.shape === 'nomiddle'
      ? 'ce n’est pas un E (il manque la barre du milieu)'
      : it.shape === 'F'
        ? 'ce n’est pas un E (c’est un F : il manque la barre du bas)'
        : 'ce n’est pas un E (E inversé en miroir)';
    if (n === 3) {
      return 'Ici, ' + shapeWhy + ' malgré les 3 points — il faut un vrai E ET exactement 3 points → réponse attendue : INCORRECT.';
    }
    return 'Ici, ' + shapeWhy + ' et ' + pts + ' — il en faudrait exactement 3 → réponse attendue : INCORRECT.';
  }
  function mtWhy(it) {
    if (it.cue === 'letter') {
      return 'La consigne porte sur la LETTRE (on ignore le chiffre ' + it.digit + ') — lettre ' + it.letter + ' = ' + (it.ans === 'vowel' ? 'voyelle (A, E, I, O, U)' : 'consonne') + '.';
    }
    return 'La consigne porte sur le CHIFFRE (on ignore la lettre ' + it.letter + ') — chiffre ' + it.digit + ' = ' + (it.ans === 'even' ? 'pair (divisible par 2)' : 'impair') + '.';
  }
  function leFigHTML(placed, order) {
    const row = (lbl, arr, cmp) => '<div class="ifb-lerow"><span class="ifb-lelbl">' + esc(lbl) + '</span><div class="ifb-lecells">' +
      Array.from({ length: 12 }, (_, i) => {
        const k = arr[i];
        const cls = cmp ? (k === order[i] ? 'ok' : 'ko') : 'ok';
        return '<div class="ifb-lecell ' + cls + '"><i>' + (i + 1) + '</i>' + (k != null ? '<svg viewBox="0 0 100 100">' + BANK.leObjs[k] + '</svg>' : '<span>—</span>') + '</div>';
      }).join('') + '</div></div>';
    return '<div class="ifb-lefig">' + row('Ton ordre', placed, true) + row('Ordre correct', order, false) + '</div>';
  }
  function ifbHTML(opts) {
    const st = opts.ok === true ? 'ok' : opts.ok === false ? 'ko' : 'neutral';
    const cls = st + (opts.extraClass ? ' ' + opts.extraClass : '');
    const badge = opts.badge || (opts.ok === true ? '✔ Correct' : opts.ok === false ? '✘ Incorrect' : '● Neutre');
    return '<div class="ifb ' + cls + '" id="ifbPanel">' +
      '<div class="ifb-head">' +
        '<span class="ifb-badge ' + st + '">' + esc(badge) + '</span>' +
        '<span class="ifb-ans">' +
          (opts.given != null ? 'Votre réponse : <b>' + esc(opts.given) + '</b>' : '') +
          (opts.given != null && opts.expected != null ? ' · ' : '') +
          (opts.expected != null ? 'Réponse attendue : <b>' + esc(opts.expected) + '</b>' : '') +
        '</span>' +
        (opts.nextLabel !== false ? '<button type="button" class="ifb-next" id="ifbNext">' + esc(opts.nextLabel || 'Continuer ›') + '</button>' : '') +
      '</div>' +
      '<div class="ifb-why"><span class="ifb-k">POURQUOI</span> <span class="ifb-txt">' + esc(opts.why || '') + '</span>' + (opts.extra || '') + '</div>' +
      (opts.fig ? '<div class="ifb-fig">' + opts.fig + '</div>' : '') +
    '</div>';
  }
  function showInstantFb(host, opts, onNext, autoMs = 4200) {
    const old = document.getElementById('ifbPanel');
    if (old) old.remove();
    const wrap = document.createElement('div');
    wrap.innerHTML = ifbHTML(opts);
    const el = wrap.firstElementChild;
    host.appendChild(el);
    clearTimeout(S.fbTimer);
    const go = () => {
      if (!S || S.done) return;
      clearTimeout(S.fbTimer);
      S.fbLock = false;
      if (onNext) onNext();
    };
    const btn = el.querySelector('#ifbNext');
    if (btn) btn.onclick = go;
    if (autoMs && onNext) S.fbTimer = setTimeout(go, autoMs);
    return el;
  }

  /* ═══════════════ Moteur de session ═══════════════ */
  let S = null, tick = null;

  function destroy() {
    if (tick) { clearInterval(tick); tick = null; }
    if (S && S.clockId) clearInterval(S.clockId);
    if (S) { clearTimeout(S.nvTimer); clearTimeout(S.lgTimer); clearTimeout(S.fbTimer); clearTimeout(S.exTimer); clearTimeout(S.chatTimer); }
    S = null;
    document.body.classList.remove('running');
    if (document.body.removeAttribute) document.body.removeAttribute('data-bank');
    const ng = document.getElementById('navGrid'); if (ng) ng.classList.remove('on');
    ['skTimer', 'skCount', 'skLvl'].forEach(id => { const n = document.getElementById(id); if (n) { n.textContent = ''; if (id === 'skLvl') n.hidden = true; } });
    const bk = document.getElementById('skBook'); if (bk) bk.hidden = true;
  }

  function start(id) {
    destroy();
    const sec = byId(id);
    S = { sec, phase: 'intro', page: 0, i: 0, items: [], log: [], answers: {}, t0: 0, deadline: 0, secEnd: 0, sub: 0, exLeft: 0, sel: null, pick: new Set(), placed: [], pool: [], mail: 0, mails: [], late: 0, done: false, qStart: 0, tab: null, tabUser: false, fbLock: false,
          chatMsgs: [], chatTyping: false, chatAwaiting: false, chatDone: false, chatDraft: '', chatTimer: 0,
          cultureSel: { most: null, least: null } };
    buildItems();
    document.body.classList.add('running');
    if (sec.bank && document.body.setAttribute) document.body.setAttribute('data-bank', sec.bank);   /* thème par banque (styles.css) */
    tick = setInterval(onTick, 250);
    render();
  }

  function buildItems() {
    const sec = S.sec, seed = (Date.now() % 99991);
    switch (sec.kind) {
      case 'blocks': {
        const bank = sec.id === 'behaviour' ? BANK.behaviour : BANK.motivation;
        const li = P.lang(sec.id) === 'fr' ? 0 : 1;      /* énoncés stockés en paires [FR, EN] */
        S.items = Array.from({ length: sec.blocks }, (_, b) => ({
          id: sec.id + b,
          stmts: [bank[b * 3], bank[b * 3 + 1], bank[b * 3 + 2]].map(s => (s ? (s[li] || s[0]) : ''))
        }));
        break;
      }
      case 'numverb': {
        if (sec.src === 'num') {
          S.items = DRILL.NV.items.map(x => Object.assign({}, x));
          S.examples = DRILL.NV.items.slice(-3).map(x => Object.assign({}, x));
        } else if (sec.src === 'ubs') {
          S.items = BANK.ubsNumerical.map(x => Object.assign({}, x));
          S.examples = BANK.ubsNumericalExamples.map(x => Object.assign({}, x));
        } else {
          S.items = BANK.verbal.map(v => ({ id: v.id, kind: 'numverb', tab: v.sh, q: v.s, a: v.a, why: v.w }));
          S.examples = BANK.verbal.slice(-3).map(v => ({ id: v.id + 'x', kind: 'numverb', tab: v.sh, q: v.s, a: v.a, why: v.w }));
        }
        if (sec.cap) S.items = S.items.slice(0, sec.cap);   /* modules bancaires : nombre de questions documenté */
        break;
      }
      case 'culture': S.items = BANK.ubsCulture.map(x => Object.assign({}, x)); S.examples = [Object.assign({}, BANK.ubsCulturePractice)]; break;
      case 'latin': S.items = []; S.seed = seed; S.examples = [DRILL.dedItem(seed + 999, 900)]; break;
      case 'pick2': {
        S.items = []; S.seed = seed;
        const examples = sec.id === 'ubs-ind' ? 3 : 1;
        S.examples = Array.from({ length: examples }, (_, i) => DRILL.indItem(seed + 888 + i * 7919, 901 + i));
        break;
      }
      case 'edots': S.items = []; S.seed = seed; break;
      case 'mt': S.items = []; S.seed = seed; break;
      case 'seqmem': S.items = Array.from({ length: 6 }, (_, s2) => ({ sec: s2, order: DRILL.leOrder(seed, s2) })); S.demo = { order: DRILL.leOrder(seed, 90) }; break;
      case 'inbox': S.seed = seed; S.mails = BANK.infoMails.map((m, i) => Object.assign({ id: i, prio: null, act: null, arrived: 0 }, m)); S.lateAt = [180, 330, 480, 630]; break;
      case 'lang': S.items = []; S.seed = seed; break;   /* géré par sous-phases */
      case 'mech': S.items = BANK.mech.map(x => Object.assign({ why: x.w || '' }, x)); S.examples = [Object.assign({ why: BANK.mech[0].w || '' }, BANK.mech[0])]; break;
      case 'switchcode': S.items = []; S.seed = seed; break;
      case 'chatsjt': S.items = BANK.msChat.map((c, i2) => ({ id: sec.id + i2, from: c.from, in: c.in })); break;
    }
  }

  /* ── chrono global / par phase ── */
  function onTick() {
    if (!S || S.done) return;
    const now = Date.now();
    if (S.phase === 'run' || S.phase === 'example') {
      if (S.sec.kind === 'edots' && S.exMode && now >= S.deadline) {
        S.exMode = false; S.t0 = now; S.i = 0; S.qStart = now; S.deadline = now + S.sec.timed * 1000;
        U.toast('Test — 2:00', '', 1600); render(); return;
      }
      if (S.deadline && now >= S.deadline) return finish();
      if (S.sec.kind === 'seqmem' && S.phase === 'example') {
        if (S.demoPhase === 'show' && S.showNext && now >= S.showNext) { S.demoIdx++; leDemo(document.getElementById('view')); return; }
      } else if (S.sec.kind === 'seqmem') {
        if (S.lePhase === 'break' && now >= S.secEnd) { S.lePhase = 'show'; S.leIdx = 0; S.secEnd = 0; S.showNext = now + 1200; render(); return; }
        if (S.lePhase === 'show' && S.showNext && now >= S.showNext) { leShowStep(); return; }
        if (S.lePhase === 'place' && S.secEnd && now >= S.secEnd) return leNextSection(true);
      } else if (S.secEnd && now >= S.secEnd) {
        if (S.sec.kind === 'lang') return langNextSection(true);
      }
      if (S.sec.kind === 'inbox' && (now - S.t0) / 1000 >= S.lateAt[0]) {
        S.lateAt.shift();
        const i = S.late++;
        const m = BANK.infoMailsLate[i] || DRILL.infoMail(i - BANK.infoMailsLate.length);
        if (m) { S.mails.push(Object.assign({ id: S.mails.length, prio: null, act: null, arrived: now, isNew: true }, m)); if (S.phase === 'run') paintInboxList(); }
        const next = Math.max((S.lateAt.length ? S.lateAt[S.lateAt.length - 1] : 0) + 150, (now - S.t0) / 1000 + 150);
        if (S.deadline && (S.t0 + next * 1000) < (S.deadline - 20000)) S.lateAt.push(next);   /* toujours de nouveaux mails */
      }
    }
    chrome();
    if (S.phase === 'run' && S.sec.kind === 'seqmem' && S.lePhase === 'show' && now >= S.showNext) leShowStep();
  }

  function chrome() {
    const T = document.getElementById('skTimer'), C = document.getElementById('skCount'), L = document.getElementById('skLvl');
    const B = document.getElementById('skBook');
    if (B) B.hidden = !(S && S.sec.kind === 'inbox' && S.phase === 'run');
    if (!S || S.phase === 'intro' || S.phase === 'tutorial' || S.phase === 'example' || S.phase === 'end') { T.textContent = ''; C.textContent = ''; L.hidden = true; return; }
    const now = Date.now();
    let t = '';
    if (S.sec.kind === 'lang') t = (S.langPhase === 'run' && S.secEnd) ? mmss((S.secEnd - now) / 1000) : '';
    else if (S.sec.kind === 'seqmem') t = S.deadline ? mmss((S.deadline - now) / 1000) : '';
    else if (S.sec.timed) t = mmss((S.deadline - now) / 1000);
    T.textContent = t;
    T.classList.toggle('warn', !!t && (S.sec.timed ? (S.deadline - now) < 60000 : (S.secEnd - now) < 30000));
    let c = '';
    if (S.sec.kind === 'blocks' || S.sec.kind === 'culture') c = Math.min(S.i + 1, S.items.length) + '/' + S.items.length;
    else if (S.sec.kind === 'chatsjt') c = Math.min(S.log.length + 1, S.items.length) + '/' + S.items.length;
    else if (S.sec.kind === 'numverb') { const done = Object.keys(S.answers || {}).length; c = done ? done + ' / ' + S.items.length : ''; }
    else if (S.sec.kind === 'mech') c = Math.min(S.i + 1, S.items.length) + ' / ' + S.items.length;
    else if (S.sec.kind === 'lang') c = '';
    C.textContent = c;
    if (S.sec.kind === 'switchcode') { L.hidden = false; L.textContent = 'Level ' + (1 + Math.floor(S.i / 10)); } else L.hidden = true;
  }

  /* ═══════════════ Rendu ═══════════════ */
  function render() {
    const view = document.getElementById('view');
    document.getElementById('skTitle').textContent = S ? (S.phase === 'intro' || S.phase === 'tutorial' ? S.sec.head : S.sec.head) : 'Accueil';
    if (!S) return;
    if (S.phase === 'intro') return renderIntro(view);
    if (S.phase === 'tutorial') return renderTutorial(view);
    if (S.phase === 'example') return renderExample(view);
    if (S.phase === 'end') return renderEnd(view);
    /* run */
    switch (S.sec.kind) {
      case 'blocks': return renderBlocks(view);
      case 'culture': return renderCulture(view, S.phase === 'example' ? S.examples[S.i] : S.items[S.i], S.phase === 'example');
      case 'numverb': return renderNumVerb(view);
      case 'latin': return renderLatin(view);
      case 'pick2': return renderPick2(view);
      case 'edots': return renderEdots(view);
      case 'mt': return renderMT(view);
      case 'seqmem': return renderLE(view);
      case 'inbox': return renderInbox(view);
      case 'lang': return renderLang(view);
      case 'mech': return renderMech(view);
      case 'switchcode': return renderSwitch(view);
      case 'chatsjt': return renderChat(view);
    }
  }

  const introNav = (last) => { const T = STR(S.sec); return '<div class="intro-nav">' + (last ? '<button class="btn-intro" id="inBack">‹ ' + esc(T.intro) + '</button>' : '<span></span>') + '<button class="btn-next" id="inNext">' + esc(T.next) + ' ›</button></div>'; };

  function renderIntro(view) {
    const pages = BANK.INTRO[S.sec.id] || [];
    const lang = P.lang(S.sec.id);
    if (S.page >= pages.length) return beginRun();
    view.className = 'sk-main';
    view.innerHTML = '<div class="intro-page">' + pages[S.page][lang] + introNav(S.page > 0) + '</div>';
    const nx = document.getElementById('inNext'), bk = document.getElementById('inBack');
    nx.onclick = () => {
      const last = S.page === pages.length - 1;
      S.page++;
      if (last) { if (hasExamples()) { S.phase = S.sec.kind === 'switchcode' ? 'tutorial' : 'example'; S.i = 0; } else beginRun(); }
      render();
    };
    if (bk) bk.onclick = () => { S.page--; render(); };
    chrome();
  }
  function hasExamples() { return ['numverb', 'latin', 'pick2', 'culture', 'mech', 'edots', 'seqmem', 'lang', 'switchcode'].includes(S.sec.kind); }

  function renderTutorial(view) {
    const lang = P.lang(S.sec.id);
    const pages = BANK.INTRO.switch[1];
    view.className = 'sk-main';
    const demo = DRILL.swItem(4242, 0);
    view.innerHTML = '<div class="intro-page">' + pages[lang] +
      '<div class="sw-wrap"><div class="sw-row">' + demo.input.map(k => '<div class="sw-tile">' + symSVG(BANK.SYM_SW[k]) + '</div>').join('') + '</div>' +
      machineHTML('<span class="sw-code">1 3 2 4</span>') +
      '<div class="sw-row">' + [0, 2, 1, 3].map(k => '<div class="sw-tile">' + symSVG(BANK.SYM_SW[k]) + '</div>').join('') + '</div>' +
      '<div class="sw-dots"><i class="on"></i><i></i><i></i><i></i><i></i><i></i><button class="sw-next" id="tutNext">›</button></div></div></div>';
    document.getElementById('tutNext').onclick = () => beginRun();
    chrome();
  }
  const machineHTML = (mid) => '<div class="sw-machine"><div class="sw-funnel"></div>' + '<div class="sw-belt">' + mid + '</div>' + '<div class="sw-funnel up"></div></div>';

  /* ── exemples (non notés) ── */
  function renderExample(view) {
    const sec = S.sec;
    view.className = 'sk-main';
    if (sec.kind === 'lang') {
      if (!S.cur) { S.sub = 0; S.t0 = Date.now(); S.qStart = Date.now(); langBuildSection(); }
      return renderLang(view);
    }
    if (sec.kind === 'seqmem') return leDemo(view);
    if (sec.kind === 'edots') { S.phase = 'run'; S.exMode = true; S.deadline = Date.now() + sec.exTime * 1000; S.i = 0; return renderEdots(view); }
    const it = S.examples[S.i];
    if (!it) return beginRun();
    if (sec.kind === 'culture') return renderCulture(view, it, true);
    if (sec.kind === 'numverb') return nvItem(view, it, true);
    if (sec.kind === 'mech') return mechItem(view, it, true);
    if (sec.kind === 'latin') return latinItem(view, it, true);
    if (sec.kind === 'pick2') return pick2ItemView(view, it, true);
  }
  function exampleDone(ok) {
    if (!S) return;
    const curS = S;
    const fr = P.lang(S.sec.id) === 'fr', v = document.getElementById('view');
    const d = document.createElement('div');
    d.className = 'exfb ' + (ok ? 'ok' : 'ko');
    d.textContent = ok
      ? (fr ? 'Très bien ! Vous avez trouvé la bonne réponse.' : 'Very good! You found the right answer right away.')
      : (fr ? 'Ce n’est pas la bonne réponse : la solution correcte est mise en évidence.' : 'That was not correct: the right answer is highlighted.');
    if (v) v.appendChild(d);
    /* 1,2 s : le flux consignes → exemples → test reste lisible sans ralentir le passage au chrono. */
    S.exTimer = setTimeout(() => { if (S !== curS || S.phase !== 'example') return; S.i++; if (S.i >= (S.examples || []).length) beginRun(); else render(); }, 1200);
  }

  function beginRun() {
    S.phase = 'run'; S.t0 = Date.now(); S.qStart = Date.now(); S.i = 0;
    const sec = S.sec;
    if (sec.timed) S.deadline = S.t0 + sec.timed * 1000;
    if (sec.kind === 'blocks') S.sel = [0, 0, 0];
    if (sec.kind === 'culture') S.cultureSel = { most: null, least: null };
    if (sec.kind === 'numverb') { S.i = 0; if (!S.tabUser || !S.tab) S.tab = S.items[0] ? S.items[0].tab : null; }
    if (sec.kind === 'mech') S.i = 0;
    if (sec.kind === 'lang') { S.sub = 0; S.langPhase = 'examples'; S.langIdx = 0; langBuildSection(); S.secEnd = 0; }
    if (sec.kind === 'seqmem') { S.leSec = 0; startBreak(); }
    if (sec.kind === 'inbox') { S.mail = 0; }
    if (sec.kind === 'chatsjt') { const curS = S; clearTimeout(S.chatTimer); S.chatTimer = setTimeout(() => { if (S !== curS) return; chatArrive(0); }, 700); }
    render();
  }

  /* ═══════════════ BLOCS (comportement / motivation) ═══════════════ */
  function renderBlocks(view) {
    const it = S.items[S.i], T = STR(S.sec);
    const title = S.sec.id === 'behaviour' ? T.blkBeh : (S.sec.sjt ? T.blkSjt : T.blkMot);
    view.className = 'sk-main';
    const spent = S.sel.reduce((a, b) => a + b, 0);
    const fb = P.instantFb() ? ifbHTML({
      ok: null,
      badge: '● Profil enregistré',
      given: S.sel.join(' / ') + ' (' + spent + '/6 pts)',
      expected: 'Aucune bonne réponse (personnalité)',
      why: 'Ce questionnaire mesure vos préférences relatives entre les 3 affirmations (jusqu’à 6 points par bloc, sans obligation de tout distribuer) — gardez une répartition cohérente avec votre style réel.',
      nextLabel: 'Continuer ›'
    }) : '';
    view.innerHTML = '<div class="blk-head"><h2>' + esc(title) + '</h2><p>' + esc(T.blkSub) + '</p></div>' +
      '<div class="blk">' + it.stmts.map((s, r) => '<div class="blk-row"><div class="blk-t">' + esc(s) + '</div>' +
        '<div class="blk-d">' + [1, 2, 3, 4, 5, 6].map(v => '<span class="dot' + (S.sel[r] === v ? ' on' : '') + ((spent - S.sel[r] + v > 6) ? ' off' : '') + '" data-r="' + r + '" data-v="' + v + '"></span>').join('') + '</div></div>').join('') + '</div>' +
      fb +
      '<div class="blk-foot"><button class="blk-next" id="blkNext">›</button></div>' +
      '<div class="blk-rest" id="blkRest">' + (6 - spent) + '</div>';
    view.querySelectorAll('.dot:not(.off)').forEach(d => d.onclick = () => {
      const r = +d.dataset.r, v = +d.dataset.v;
      S.sel[r] = (S.sel[r] === v) ? 0 : v;
      renderBlocks(view);
    });
    const goNext = () => {
      S.log.push({ n: S.i + 1, q: 'Bloc ' + (S.i + 1), given: S.sel.join('/'), ok: null, ms: Date.now() - S.qStart, section: S.sec.id, why: 'Questionnaire de personnalité (sans bonne ni mauvaise réponse).' });
      S.sel = [0, 0, 0]; S.qStart = Date.now(); S.i++;
      if (S.i >= S.items.length) return finish();
      render();
    };
    document.getElementById('blkNext').onclick = goNext;
    const ifbN = document.getElementById('ifbNext');
    if (ifbN) ifbN.onclick = goNext;
    chrome();
  }

  /* ═══════════════ CULTURE MATCH — une réponse la plus efficace + la moins efficace ══ */
  function renderCulture(view, it, isEx) {
    if (!it) return isEx ? beginRun() : finish();
    const fr = P.lang(S.sec.id) === 'fr';
    const text = (v) => v && typeof v === 'object' ? (v[fr ? 'fr' : 'en'] || v.en || '') : String(v || '');
    const selection = S.cultureSel || { most: null, least: null };
    const mostLabel = fr ? 'La plus efficace' : 'Most effective';
    const leastLabel = fr ? 'La moins efficace' : 'Least effective';
    const title = fr ? 'Choisissez une réponse pour chaque catégorie' : 'Choose one response for each category';
    const submitLabel = isEx ? (fr ? 'Vérifier l’exemple' : 'Check example') :
      (S.i === S.items.length - 1 ? (fr ? 'Terminer' : 'Finish') : (fr ? 'Scénario suivant' : 'Next scenario'));
    const choices = it.actions.map((action, i) => {
      const mostOn = selection.most === i, leastOn = selection.least === i;
      return '<article class="cm-action" data-action="' + i + '"><div class="cm-action-letter">' + String.fromCharCode(65 + i) + '</div>' +
        '<div class="cm-action-copy">' + esc(text(action)) + '</div><div class="cm-action-picks">' +
        '<button type="button" class="cm-pick most' + (mostOn ? ' on' : '') + '" data-role="most" data-i="' + i + '" aria-pressed="' + mostOn + '">' + esc(mostLabel) + '</button>' +
        '<button type="button" class="cm-pick least' + (leastOn ? ' on' : '') + '" data-role="least" data-i="' + i + '" aria-pressed="' + leastOn + '">' + esc(leastLabel) + '</button></div></article>';
    }).join('');
    const hasPair = selection.most != null && selection.least != null && selection.most !== selection.least;
    view.className = 'sk-main narrow';
    view.innerHTML = '<div class="cm-wrap"><div class="cm-topline"><span>' + (isEx ? (fr ? 'Exemple guidé' : 'Practice example') :
      esc((fr ? 'Scénario ' : 'Scenario ') + (S.i + 1) + ' / ' + S.items.length)) + '</span><span class="cm-source">UBS · Culture Match</span></div>' +
      '<h2 class="cm-instruction">' + esc(title) + '</h2><section class="cm-scenario"><span>' + (fr ? 'SITUATION' : 'SCENARIO') + '</span><p>' + esc(text(it.scenario)) + '</p></section>' +
      '<div class="cm-columns"><span>' + (fr ? 'RÉACTION' : 'RESPONSE') + '</span><span>' + esc(mostLabel) + '</span><span>' + esc(leastLabel) + '</span></div>' +
      '<div class="cm-actions">' + choices + '</div>' +
      '<p class="cm-hint">' + (fr ? 'Sélectionnez deux actions différentes : une plus efficace et une moins efficace.' : 'Select two different actions: one most effective and one least effective.') + '</p>' +
      '<div class="cm-submit"><button class="btn-next" id="cmSubmit"' + (hasPair ? '' : ' disabled') + '>' + esc(submitLabel) + ' ›</button></div></div>';

    view.querySelectorAll('.cm-pick').forEach((button) => button.onclick = () => {
      if (S.fbLock) return;
      const role = button.dataset.role, idx = +button.dataset.i;
      const next = Object.assign({ most: null, least: null }, S.cultureSel || {});
      next[role] = next[role] === idx ? null : idx;
      const other = role === 'most' ? 'least' : 'most';
      if (next[other] === idx) next[other] = null;
      S.cultureSel = next;
      renderCulture(view, it, isEx);
    });

    document.getElementById('cmSubmit').onclick = () => {
      if (!hasPair) return U.toast(fr ? 'Choisissez deux actions différentes.' : 'Choose two different actions.', 'err', 1400);
      const mostOk = selection.most === it.best, leastOk = selection.least === it.least;
      if (isEx) {
        S.fbLock = true;
        view.querySelectorAll('.cm-action').forEach((row, idx) => {
          if (idx === it.best) row.classList.add('answer-most');
          if (idx === it.least) row.classList.add('answer-least');
        });
        exampleDone(mostOk && leastOk);
        return;
      }
      const given = (fr ? 'Plus efficace : ' : 'Most effective: ') + String.fromCharCode(65 + selection.most) +
        ' · ' + (fr ? 'Moins efficace : ' : 'Least effective: ') + String.fromCharCode(65 + selection.least);
      const expected = (fr ? 'Plus efficace : ' : 'Most effective: ') + String.fromCharCode(65 + it.best) +
        ' · ' + (fr ? 'Moins efficace : ' : 'Least effective: ') + String.fromCharCode(65 + it.least);
      S.answers[S.i] = { most: selection.most, least: selection.least };
      S.log.push({ n: S.i + 1, q: text(it.scenario), given, correct: expected, ok: mostOk && leastOk,
        mostOk, leastOk, ms: Date.now() - S.qStart, section: S.sec.id, why: text(it.why) });
      S.i++;
      S.cultureSel = { most: null, least: null };
      S.qStart = Date.now();
      if (S.i >= S.items.length) return finish();
      if (!P.instantFb()) return render();
      S.fbLock = true;
      showInstantFb(view, { ok: mostOk && leastOk, given, expected, why: text(it.why), nextLabel: fr ? 'Continuer ›' : 'Continue ›' }, () => {
        if (S && S.phase === 'run') { S.fbLock = false; render(); }
      }, 4000);
      chrome();
    };
    chrome();
  }

  /* ═══════════════ CHATSJT — Morgan Stanley chatAssess (mode messagerie) ═══════════════
     Les scénarios arrivent comme des messages reçus (bulles blanches) ; le candidat tape
     sa réponse, qui part comme un vrai message (bulle bleue, ✓✓, horodatage). Pas de
     bonne réponse : les entrées du log n'ont pas de champ `ok` → finish() les agrège
     comme un questionnaire comportemental. À la fin, un message contient le lien vers
     l'évaluation suivante (sec.next), comme dans le process réel. */
  const chatTime = () => { try { return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }); } catch (e) { return ''; } };

  function chatArrive(i) {
    if (!S || S.phase === 'end' || S.done) return;
    if (i >= S.items.length) {                     /* message final : lien vers le test suivant */
      const T = STR(S.sec);
      S.chatTyping = false; S.chatAwaiting = false; S.chatDone = true;
      S.chatMsgs.push({ who: 'them', link: true, from: 'Morgan Stanley — Recruitment', text: '🔗 ' + T.chatNextLbl + ' : ' + T.chatNextCta, t: chatTime() });
      return render();
    }
    const lang = P.lang(S.sec.id) === 'fr' ? 0 : 1;   /* scénarios stockés en paires [FR, EN] */
    const it = S.items[i];
    S.chatTyping = false; S.chatAwaiting = true; S.chatDraft = '';
    if (!S.qStart) S.qStart = Date.now();
    S.chatMsgs.push({ who: 'them', from: it.from, text: it.in[lang], t: chatTime() });
    render();
  }

  function chatSend(text) {
    if (!S || S.phase !== 'run' || S.done) return;
    text = String(text == null ? '' : text).trim();
    if (!S.chatAwaiting || !text) return;
    const lang = P.lang(S.sec.id) === 'fr' ? 0 : 1;
    const i = S.log.length;
    const it = S.items[i];
    if (!it) return;
    S.chatAwaiting = false;
    S.chatMsgs.push({ who: 'me', text, t: chatTime() });
    S.log.push({ n: i + 1, q: it.in[lang], given: text, ms: Date.now() - (S.qStart || Date.now()), section: S.sec.id });
    S.qStart = Date.now();
    S.chatTyping = true;
    render();
    clearTimeout(S.chatTimer);
    const curS = S;
    S.chatTimer = setTimeout(() => { if (S !== curS) return; chatArrive(i + 1); }, 900);
  }

  function renderChat(view) {
    const T = STR(S.sec);
    view.className = 'sk-main narrow';
    const msgs = S.chatMsgs.map(m => {
      if (m.who === 'me') return '<div class="chat-row me"><div class="bubble me">' + esc(m.text) + '<span class="b-time">' + esc(m.t) + ' <span class="b-ticks">✓✓</span></span></div></div>';
      const head = m.from ? '<div class="b-from">' + esc(m.from) + '</div>' : '';
      const cta = m.link ? '<button class="chat-cta" id="chatGoNext">▶ ' + esc(T.chatNextLbl) + ' — ' + esc(S.sec.next || '') + '</button>' : '';
      return '<div class="chat-row them"><div class="bubble them' + (m.link ? ' link-bubble' : '') + '">' + head + esc(m.text) + cta + '<span class="b-time">' + esc(m.t) + '</span></div></div>';
    }).join('');
    const typing = S.chatTyping ? '<div class="chat-row them"><div class="bubble them typing"><i></i><i></i><i></i></div></div>' : '';
    const inputBar = S.chatDone ? '' :
      '<div class="chat-input"><textarea id="chatIn" rows="2" placeholder="' + esc(T.chatPlaceholder) + '">' + esc(S.chatDraft || '') + '</textarea>' +
      '<button class="chat-send" id="chatSend"' + ((S.chatTyping || !S.chatAwaiting) ? ' disabled' : '') + '>' + esc(T.chatSend) + '</button></div>';
    view.innerHTML = '<div class="chat-app">' +
      '<div class="chat-head"><div class="chat-ava">MS</div><div class="chat-hdtxt"><b>Morgan Stanley — Recruitment</b><span id="chatStatus">' + (S.chatTyping ? esc(T.chatTyping) : esc(T.chatOnline)) + '</span></div><span class="chat-lock">🔒</span></div>' +
      '<div class="chat-body" id="chatBody">' + msgs + typing + '</div>' + inputBar + '</div>';
    const body = document.getElementById('chatBody');
    if (body && body.scrollTo) { try { body.scrollTop = body.scrollHeight; } catch (e) {} }
    const inp = document.getElementById('chatIn');
    if (inp) {
      inp.oninput = () => {
        S.chatDraft = inp.value;
        const b = document.getElementById('chatSend');
        if (b) b.disabled = S.chatTyping || !S.chatAwaiting || !String(inp.value || '').trim();
      };
      if (inp.addEventListener) inp.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); const b = document.getElementById('chatSend'); if (b) b.click(); }
      });
    }
    const send = document.getElementById('chatSend');
    if (send) send.onclick = () => {
      const v = inp ? String(inp.value || '') : '';
      if (!v.trim()) return U.toast(STR(S.sec).chatEmpty, 'err');
      chatSend(v);
    };
    const go = document.getElementById('chatGoNext');
    if (go) go.onclick = () => { const nx = S.sec.next; finish(); if (nx) location.hash = '#/run/' + nx; };
    chrome();
  }

  /* ═══════════════ NUMVERB (numérique + verbal) ═══════════════ */
  const nvText = (value) => value && typeof value === 'object'
    ? (value[P.lang(S.sec.id)] || value.en || value.fr || '')
    : String(value == null ? '' : value);
  const nvTabs = () => S.sec.src === 'num'
    ? DRILL.NV.tabs.map(t => ({ id: t.id, name: t.name }))
    : (S.sec.src === 'ubs'
      ? BANK.ubsNumericalSheets.map(t => ({ id: t.id, name: P.lang(S.sec.id) === 'fr' ? t.nameFr : t.nameEn }))
      : BANK.verbalSheets.map(t => ({ id: t.id, name: t.name })));
  /* Note affichée pendant les exemples : rend explicite le fait que le chrono
     du test ne démarre qu'après eux (les exemples sont non notés et non chronométrés). */
  function exNoteHTML() {
    const T = STR(S.sec), n = (S.examples || []).length;
    if (!S.sec || !S.sec.timed || !n) return '';
    const tpl = n > 1 ? T.exNoteMany : T.exNoteOne;
    return '<div class="ex-note">' + esc(tpl.replace('{t}', mmss(S.sec.timed))) + '</div>';
  }
  function nvItem(view, it, isEx) {
    const T = STR(S.sec);
    const tabs = nvTabs();
    /* Feuille affichée : le contenu suit l'onglet sélectionné (jamais l'onglet
       « subi » de la question). Par défaut, la feuille de la question ; dès que
       l'utilisateur choisit une feuille, ce choix est conservé d'une question à
       l'autre. */
    if (!S.tabUser || !tabs.some(t => t.id === S.tab)) S.tab = it.tab;
    const sheet = S.sec.src === 'ubs' ? BANK.ubsNumericalSheets.find(s => s.id === S.tab) : null;
    const fig = S.sec.src === 'num' ? DRILL.NV.figures[S.tab]() : (sheet ? sheet[P.lang(S.sec.id) === 'fr' ? 'fr' : 'en'] : BANK.verbalSheets.find(s => s.id === S.tab).html);
    view.className = 'sk-main';
    view.innerHTML = '<div class="nv-sheets"><span class="nv-sheets-l">' + esc(T.sheets) + '</span><div class="nv-tabs">' + tabs.map(t => '<button class="nv-tab' + (t.id === S.tab ? ' on' : '') + '" data-t="' + t.id + '" title="' + esc(T.sheetGo) + '">' + esc(t.name) + '</button>').join('') + '</div><span class="nv-sheets-h">' + esc(T.sheetsHint) + '</span></div>' +
      '<div class="nv-cols"><div class="nv-fig"><div class="nvtext">' + fig + '</div></div>' +
      '<div class="nv-side"><div class="nv-stmt">' + (isEx ? '<b>EXAMPLE</b> ' : '') + esc(nvText(it.q)) + '</div>' +
      (isEx ? exNoteHTML() : '') +
      '<div class="tfbtns">' + T.tf.map((l, i) => '<button class="tfbtn' + (S.sel === i ? ' sel' : '') + '" data-v="' + i + '">' + l + '</button>').join('') + '</div></div></div>' +
      navPadHTML();
    view.querySelectorAll('.nv-tab').forEach(b => b.onclick = () => { S.tab = b.dataset.t; S.tabUser = true; if (S.nvAns != null) S.sel = S.nvAns; nvItem(view, it, isEx); });
    view.querySelectorAll('.tfbtn').forEach(b => b.onclick = () => {
      const v = +b.dataset.v;
      if (isEx) { const curS = S; S.sel = v; view.querySelectorAll('.tfbtn').forEach(x => x.classList.remove('sel', 'ok', 'ko')); b.classList.add(it.a === v ? 'ok' : 'ko'); S.exTimer = setTimeout(() => { if (S === curS) exampleDone(it.a === v); }, 600); return; }
      S.nvAns = v;
      view.querySelectorAll('.tfbtn').forEach(x => { x.classList.remove('ok', 'ko'); x.classList.toggle('sel', x === b); });
      b.classList.add(v === it.a ? 'ok' : 'ko');
      if (P.instantFb() && v !== it.a) {
        const gBtn = view.querySelector('.tfbtn[data-v="' + it.a + '"]');
        if (gBtn) gBtn.classList.add('ok');
      }
      nvSchedule(view, it);
    });
    bindNav(view, isEx);
    chrome();
  }
  function renderNumVerb(view) { const it = S.items[S.i]; S.sel = S.answers[S.i] == null ? null : S.answers[S.i]; S.nvAns = null; nvItem(view, it, false); }
  const tfText = (it, idx) => (it.o ? it.o[idx] : STR(S.sec).tf[idx]);
  function nvCommitAndAdvance() {
    if (!S || S.done || S.phase !== 'run' || S.nvAns == null) return;
    clearTimeout(S.nvTimer);
    clearTimeout(S.fbTimer);
    S.nvInfo = S.nvInfo || {};
    S.nvInfo[S.i] = { ms: Date.now() - S.qStart };
    S.answers[S.i] = S.nvAns;
    S.nvAns = null; S.nvText = null; S.qStart = Date.now();
    S.i = Math.min(S.items.length - 1, S.i + 1);
    render();
  }
  function nvSchedule(view, it) {
    clearTimeout(S.nvTimer);
    clearTimeout(S.fbTimer);
    const oldSlide = view.querySelector('.nv-slide');
    if (oldSlide) oldSlide.remove();
    const ok = S.nvAns === it.a;
    if (P.instantFb()) {
      const tabs = nvTabs();
      const shObj = tabs.find(t => t.id === it.tab);
      const shName = shObj ? shObj.name : it.tab;
      const shKind = S.sec.src === 'verb' ? 'Fiche de texte' : 'Feuille de données';
      const whyTxt = (it.why ? nvText(it.why) + ' ' : '') + shKind + ' : ' + shName + '.';
      const side = view.querySelector('.nv-side') || view;
      const el = showInstantFb(side, {
        ok,
        given: tfText(it, S.nvAns),
        expected: tfText(it, it.a),
        why: whyTxt,
        extra: ' <button type="button" class="ifb-sheet" id="ifbSheet" data-t="' + esc(it.tab) + '">Ouvrir la feuille « ' + esc(shName) + ' »</button>',
        extraClass: 'nv-slide on'
      }, nvCommitAndAdvance, 4400);
      const shBtn = el.querySelector('#ifbSheet');
      if (shBtn) shBtn.onclick = () => {
        S.tab = it.tab; S.tabUser = true;
        view.querySelectorAll('.nv-tab').forEach(t => t.classList.toggle('on', t.dataset.t === S.tab));
        const activeSheet = S.sec.src === 'ubs' ? BANK.ubsNumericalSheets.find(s => s.id === S.tab) : null;
        const fig = S.sec.src === 'num' ? DRILL.NV.figures[S.tab]() : (activeSheet ? activeSheet[P.lang(S.sec.id) === 'fr' ? 'fr' : 'en'] : BANK.verbalSheets.find(s => s.id === S.tab).html);
        const box = view.querySelector('.nv-fig .nvtext');
        if (box) box.innerHTML = fig;
      };
      S.nvTimer = S.fbTimer;
      return;
    }
    S.nvTimer = setTimeout(() => {
      if (!S || S.done || S.phase !== 'run') return;
      const el = document.createElement('div');
      el.className = 'nv-slide';
      el.innerHTML = '<span class="ic ' + (ok ? 'ok' : 'ko') + '">' + (ok ? '✔' : '✘') + '</span><span>' + esc(S.nvText || (ok ? (P.lang(S.sec.id) === 'fr' ? 'Réponse correcte.' : 'Correct answer.') : (P.lang(S.sec.id) === 'fr' ? 'Réponse incorrecte.' : 'Wrong answer.'))) + '</span>';
      view.appendChild(el);
      requestAnimationFrame(() => el.classList.add('on'));
      S.nvTimer = setTimeout(nvCommitAndAdvance, 4000);
    }, 800);
  }

  /* ═══════════════ Navigation ‹ ▦ › ══════════════ */
  function navPadHTML() {
    const done = S && S.items && Object.keys(S.answers || {}).length >= S.items.length;
    return '<div class="navpad"><button id="nvPrev">‹</button><button id="nvGrid">▦</button><button id="nvNext">›</button>' +
      (done ? '<button class="navpad-end" id="nvEnd">' + esc(STR(S.sec).finish) + '</button>' : '') + '</div>';
  }
  function bindNav(view, isEx) {
    const p = document.getElementById('nvPrev'), n = document.getElementById('nvNext'), g = document.getElementById('nvGrid');
    if (isEx) { p.style.visibility = n.style.visibility = g.style.visibility = 'hidden'; return; }
    const e = document.getElementById('nvEnd'); if (e) e.onclick = () => finish();
    const stopNv = () => { if (S.sec.kind === 'numverb') { clearTimeout(S.nvTimer); clearTimeout(S.fbTimer); S.nvAns = null; } };
    p.onclick = () => { if (S.i > 0) { stopNv(); S.i--; render(); } };
    n.onclick = () => { stopNv(); S.i = Math.min(S.items.length - 1, S.i + 1); render(); };
    g.onclick = () => toggleNav();
  }
  function toggleNav() {
    const ng = document.getElementById('navGrid');
    if (ng.classList.contains('on')) { ng.classList.remove('on'); return; }
    ng.innerHTML = S.items.map((it, i) => '<button class="' + (S.answers[i] != null ? 'done' : '') + (i === S.i ? ' cur' : '') + '" data-i="' + i + '">' + (i + 1) + '</button>').join('');
    ng.classList.add('on');
    ng.querySelectorAll('button').forEach(b => b.onclick = () => { S.i = +b.dataset.i; ng.classList.remove('on'); render(); });
  }

  /* ═══════════════ DÉDUCTIF ═══════════════ */
  function latinItem(view, it, isEx) {
    const T = STR(S.sec);
    S.fbLock = false;
    view.className = 'sk-main narrow';
    view.innerHTML = '<div class="ded-wrap"><div class="qtitle">' + esc(T.chooseCorrect) + '</div><div class="ded-grid">' +
      it.grid.map((row, y) => row.map((v, x) => {
        if (it.hole && it.hole[0] === y && it.hole[1] === x) return '<div class="ded-tile hole">?</div>';
        if (it.shown && it.shown[y + ',' + x] != null) return '<div class="ded-tile">' + symSVG(BANK.SYM_DED[it.shown[y + ',' + x]]) + '</div>';
        return '<div class="ded-tile empty"></div>';
      }).join('')).join('') + '</div><div class="ded-sep"></div><div class="ded-opts" id="dopts">' +
      it.options.map((k, i) => '<button class="ded-opt" data-i="' + i + '">' + symSVG(BANK.SYM_DED[k]) + '</button>').join('') + '</div>' +
      '<div class="qsub" style="margin-top:14px">' + esc(T.dedNote) + '</div>' + (isEx ? exNoteHTML() : '') + '</div>';
    view.querySelectorAll('.ded-opt').forEach(b => b.onclick = () => {
      if (S.fbLock) return;
      const i = +b.dataset.i, ok = i === it.ans;
      if (isEx) { const curS = S; b.classList.add(ok ? 'ok' : 'ko'); S.exTimer = setTimeout(() => { if (S === curS) exampleDone(ok); }, 550); return; }
      S.fbLock = true;
      b.classList.add(ok ? 'ok' : 'ko');
      const goodBtn = view.querySelectorAll('.ded-opt')[it.ans];
      if (goodBtn) goodBtn.classList.add('ok');
      const hole = view.querySelector('.ded-tile.hole');
      if (hole) { hole.classList.add('ok'); hole.innerHTML = symSVG(BANK.SYM_DED[it.options[it.ans]]); }
      const why = dedWhy(it);
      S.log.push({ n: S.log.length + 1, q: 'Grille 4×4 — case « ? »', given: String(i + 1), correct: String(it.ans + 1), ok, ms: Date.now() - S.qStart, section: S.sec.id, why });
      S.qStart = Date.now(); S.i++;
      if (!P.instantFb()) {
        S.fbTimer = setTimeout(() => { if (S && S.phase === 'run') { S.fbLock = false; render(); } }, 420);
        return;
      }
      showInstantFb(view.querySelector('.ded-wrap') || view, {
        ok,
        given: 'Option ' + (i + 1) + ' (' + SYM_NAMES_DED[it.options[i]] + ')',
        expected: 'Option ' + (it.ans + 1) + ' (' + SYM_NAMES_DED[it.options[it.ans]] + ')',
        why,
        fig: '<div class="ifb-dedfig"><span class="ifb-mini">' + symSVG(BANK.SYM_DED[it.options[it.ans]]) + '</span><span>Forme attendue dans la case « ? » (ligne ' + (it.hole[0] + 1) + ', col. ' + (it.hole[1] + 1) + ')</span></div>'
      }, () => { if (S && S.phase === 'run') render(); }, 4200);
    });
    chrome();
  }
  const renderLatin = (view) => { while (S.items.length <= S.i) S.items.push(DRILL.dedItem(S.seed + S.items.length * 6151, S.items.length)); latinItem(view, S.items[S.i], false); };

  /* ═══════════════ INDUCTIF ═══════════════ */
  function pick2ItemView(view, it, isEx) {
    const T = STR(S.sec);
    S.fbLock = false;
    const g3 = g => '<div class="g3">' + g.map(k => '<div class="c">' + symSVG(BANK.SYM_IND[k]) + '</div>').join('') + '</div>';
    view.className = 'sk-main';
    view.innerHTML = '<div class="ind-wrap"><div class="ind-side"><div class="ind-t">' + esc(T.indLeft) + '</div><div class="ind-ex">' + it.examples.map(g3).join('') + '</div></div>' +
      '<div class="ind-side"><div class="ind-t">' + esc(T.indRight) + '</div><div class="ind-cands" id="cands">' + it.candidates.map((g, i) => '<div class="cand' + (S.pick.has(i) ? ' sel' : '') + '" data-i="' + i + '">' + g3(g) + '</div>').join('') + '</div></div></div>' +
      (isEx ? exNoteHTML() : '') +
      '<div class="ind-go"><button id="indGo" title="Valider">▶▶</button></div>';
    view.querySelectorAll('.cand').forEach(c => c.onclick = () => {
      if (S.fbLock) return;
      const i = +c.dataset.i;
      if (S.pick.has(i)) S.pick.delete(i); else { if (S.pick.size >= 2) return; S.pick.add(i); }
      view.querySelectorAll('.cand').forEach(x => x.classList.toggle('sel', S.pick.has(+x.dataset.i)));
    });
    document.getElementById('indGo').onclick = () => {
      if (S.fbLock) return;
      if (S.pick.size === 1) return U.toast(T.indSel, 'err', 1400);
      const pickedArr = [...S.pick].sort();
      const sel = pickedArr.length ? pickedArr.join(',') : '';
      const ok = pickedArr.length === 2 && sel === it.good.slice().sort().join(',');
      if (isEx) { S.pick = new Set(); exampleDone(ok); return; }
      S.fbLock = true;
      const why = indWhy(it);
      view.querySelectorAll('.cand').forEach((c, idx) => {
        if (it.good.includes(idx)) c.classList.add('ok');
        else if (S.pick.has(idx)) c.classList.add('ko');
      });
      S.log.push({ n: S.log.length + 1, q: 'Quelles deux grilles suivent la même règle ?', given: sel, correct: it.good.slice().sort().join(','), ok, ms: Date.now() - S.qStart, section: S.sec.id, why });
      S.pick = new Set(); S.qStart = Date.now(); S.i++;
      if (!P.instantFb()) { S.fbLock = false; return render(); }
      showInstantFb(view, {
        ok,
        given: pickedArr.length ? 'Grilles ' + pickedArr.map(x => x + 1).join(' et ') : 'Aucune (question passée)',
        expected: 'Grilles ' + it.good.map(x => x + 1).join(' et '),
        why
      }, () => { if (S && S.phase === 'run') render(); }, 4500);
    };
    chrome();
  }
  const renderPick2 = (view) => { while (S.items.length <= S.i) S.items.push(DRILL.indItem(S.seed + S.items.length * 4093, S.items.length)); pick2ItemView(view, S.items[S.i], false); };

  /* ═══════════════ CONCENTRATION ═══════════════ */
  function renderEdots(view) {
    const T = STR(S.sec);
    S.fbLock = false;
    while (S.items.length <= S.i) S.items.push(DRILL.concItem(S.seed + S.items.length * 3571, S.items.length));
    const it = S.items[S.i];
    view.className = 'sk-main narrow';
    view.innerHTML = '<div class="conc-q">' + esc(T.concQ) + '</div><div class="conc-box">' + DRILL.concSVG(it.shape, it.dots) + '</div>' +
      '<div class="conc-btns"><button class="conc-btn" data-v="0">incorrect</button><button class="conc-btn" data-v="1">correct</button></div>';
    const answer = (v) => {
      if (S.fbLock) return;
      const ok = (v === 1) === it.correct;
      if (S.exMode) { S.i++; return render(); }
      S.fbLock = true;
      const why = concWhy(it);
      const btn = view.querySelector('.conc-btn[data-v="' + v + '"]'); if (btn) btn.classList.add(ok ? 'ok' : 'ko');
      const goodBtn = view.querySelector('.conc-btn[data-v="' + (it.correct ? 1 : 0) + '"]'); if (goodBtn) goodBtn.classList.add('ok');
      S.log.push({ n: S.log.length + 1, q: 'E + 3 points ?', given: v === 1 ? 'correct' : 'incorrect', correct: it.correct ? 'correct' : 'incorrect', ok, ms: Date.now() - S.qStart, section: S.sec.id, why });
      S.qStart = Date.now(); S.i++;
      if (!P.instantFb()) { S.fbLock = false; return render(); }
      showInstantFb(view, {
        ok,
        given: v === 1 ? 'correct' : 'incorrect',
        expected: it.correct ? 'correct' : 'incorrect',
        why,
        fig: '<div class="ifb-concfig"><div class="ifb-conccard">' + DRILL.concSVG(it.shape, it.dots) + '<span>Objet affiché (' + it.dots.length + ' pt' + (it.dots.length > 1 ? 's' : '') + ')</span></div><div class="ifb-conccard ref">' + DRILL.concSVG('E', [[26, 22], [74, 22], [26, 88]]) + '<span>Cible : vrai E + 3 pts</span></div></div>'
      }, () => { if (S && S.phase === 'run') render(); }, 3800);
    };
    view.querySelectorAll('.conc-btn').forEach(b => b.onclick = () => answer(+b.dataset.v));
    S.keyHandler = (e) => {
      if (S.fbLock) { if (e.key === 'Enter' || e.key === ' ') { const n = document.getElementById('ifbNext'); if (n) n.click(); } return; }
      if (e.key === 'd' || e.key === 'D') answer(1);
      if (e.key === 'a' || e.key === 'A') answer(0);
    };
    chrome();
  }

  /* ═══════════════ MULTI-TÂCHES ═══════════════ */
  function renderMT(view) {
    S.fbLock = false;
    while (S.items.length <= S.i) S.items.push(DRILL.mtItem(S.seed + S.items.length * 7717, S.items.length));
    const it = S.items[S.i];
    const lang = P.lang(S.sec.id);
    const cue = it.cue === 'letter' ? (lang === 'fr' ? 'Jugez la LETTRE : voyelle ou consonne ?' : 'Judge the LETTER: vowel or consonant?') : (lang === 'fr' ? 'Jugez le CHIFFRE : pair ou impair ?' : 'Judge the DIGIT: odd or even?');
    const opts = it.cue === 'letter' ? (lang === 'fr' ? ['voyelle', 'consonne'] : ['vowel', 'consonant']) : (lang === 'fr' ? ['pair', 'impair'] : ['even', 'odd']);
    const good = it.cue === 'letter' ? (it.ans === 'vowel' ? 0 : 1) : (it.ans === 'even' ? 0 : 1);
    view.className = 'sk-main narrow';
    view.innerHTML = '<div class="mt-cue">' + esc(cue) + '</div><div class="mt-stim"><div class="ch">' + it.letter + '</div><div class="ch">' + it.digit + '</div></div>' +
      '<div class="mt-btns">' + opts.map((o, i) => '<button class="mt-btn" data-i="' + i + '">' + esc(o) + '</button>').join('') + '</div>';
    view.querySelectorAll('.mt-btn').forEach(b => b.onclick = () => {
      if (S.fbLock) return;
      S.fbLock = true;
      const idx = +b.dataset.i, ok = idx === good;
      b.classList.add(ok ? 'ok' : 'ko');
      const goodBtn = view.querySelectorAll('.mt-btn')[good]; if (goodBtn) goodBtn.classList.add('ok');
      const why = mtWhy(it);
      S.log.push({ n: S.log.length + 1, q: cue + ' (' + it.letter + it.digit + ')', given: opts[idx], correct: opts[good], ok, ms: Date.now() - S.qStart, section: S.sec.id, why });
      S.qStart = Date.now(); S.i++;
      if (!P.instantFb()) { S.fbLock = false; return render(); }
      showInstantFb(view, {
        ok,
        given: opts[idx],
        expected: opts[good],
        why
      }, () => { if (S && S.phase === 'run') render(); }, 3400);
    });
    chrome();
  }

  /* ═══════════════ LEARNING EFFICIENCY ═══════════════ */
  function startBreak() { S.lePhase = 'break'; S.secEnd = Date.now() + 6000; render(); }
  function leDemo(view) {
    const T = STR(S.sec);
    if (!S.demoPhase) { S.demoPhase = 'show'; S.demoIdx = 0; S.showNext = 0; S.demoSel = Array(6).fill(null); }
    if (S.demoPhase === 'show') {
      view.className = 'sk-main narrow';
      if (S.demoIdx >= 6) { S.demoPhase = 'place'; S.demoSel = Array(6).fill(null); return leDemo(view); }
      view.innerHTML = '<div class="qtitle">' + esc(T.leShow) + '</div><div class="le-seq"><div class="le-obj"><svg viewBox="0 0 100 100">' + BANK.leObjs[S.demo.order[S.demoIdx]] + '</svg></div></div>';
      S.showNext = Date.now() + 1300;
      return chrome();
    }
    view.className = 'sk-main narrow';
    const filledD = S.demoSel.filter(x => x != null).length;
    view.innerHTML = '<div class="qtitle">' + esc(T.lePlace) + '</div>' +
      '<div class="le-pool">' + [0, 1, 2, 3, 4, 5].filter(k => !S.demoSel.includes(k)).sort((a, b) => S.demo.order[b] - S.demo.order[a]).map(k => '<button class="le-p" data-k="' + k + '"><svg viewBox="0 0 100 100">' + BANK.leObjs[S.demo.order[k]] + '</svg></button>').join('') + '</div>' +
      '<div class="le-fields">' + Array.from({ length: 6 }, (_, i) => '<div class="le-f' + (S.demoSel[i] != null ? ' filled' : '') + '" data-f="' + i + '">' + (S.demoSel[i] != null ? '<svg viewBox="0 0 100 100">' + BANK.leObjs[S.demo.order[S.demoSel[i]]] + '</svg>' : '<i>' + (i + 1) + '</i>') + '</div>').join('') + '</div>' +
      '<div class="intro-nav center"><button class="btn-next" id="leOk" ' + (filledD < 6 ? 'disabled' : '') + '>' + esc(T.next) + ' ›</button></div>';
    view.querySelectorAll('.le-p').forEach(b => b.onclick = () => { const k = +b.dataset.k; const f = S.demoSel.indexOf(null); if (f >= 0) { S.demoSel[f] = k; leDemo(view); } });
    view.querySelectorAll('.le-f').forEach(f => f.onclick = () => { const i = +f.dataset.f; if (S.demoSel[i] != null) { S.demoSel[i] = null; leDemo(view); } });
    document.getElementById('leOk').onclick = () => { S.demoPhase = null; beginRun(); };
    chrome();
  }
  function leShowStep() {
    const view = document.getElementById('view');
    if (S.leIdx >= 12) { S.lePhase = 'place'; S.secEnd = Date.now() + 30000; S.placed = Array(12).fill(null); S.pool = shuffle12(S.items[S.leSec].order); return renderLE(view); }
    S.leIdx++; S.showNext = Date.now() + 1000;
    renderLE(view);
  }
  const shuffle12 = (order) => { const a = order.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  function renderLE(view) {
    const T = STR(S.sec);
    view.className = 'sk-main narrow';
    if (S.lePhase === 'break') {
      const fb = (S.leLast && P.instantFb()) ? ifbHTML({
        ok: S.leLast.ok === 12,
        given: S.leLast.ok + ' / 12 positions correctes',
        expected: '12 / 12 dans l’ordre exact',
        why: 'Section ' + S.leLast.sec + ' : ton ordre vs l’ordre correct, objet par objet en figures (vert = bonne position, rouge = position erronée).',
        fig: leFigHTML(S.leLast.placed, S.leLast.order),
        nextLabel: 'Continuer ›'
      }) : '';
      view.innerHTML = '<div class="le-break">' + esc(T.leBreak) + ' <b>' + mmss(Math.max(0, (S.secEnd - Date.now()) / 1000)) + '</b></div>' + fb;
      const ifbN = document.getElementById('ifbNext');
      if (ifbN) ifbN.onclick = () => { S.lePhase = 'show'; S.leIdx = 0; S.secEnd = 0; S.showNext = Date.now() + 1200; render(); };
      return chrome();
    }
    if (S.lePhase === 'show') {
      const o = S.leIdx < 12 ? S.items[S.leSec].order[S.leIdx] : null;
      view.innerHTML = '<div class="qtitle">' + esc(T.leShow) + ' (' + (S.leSec + 1) + '/6)</div><div class="le-seq">' + (o != null ? '<div class="le-obj"><svg viewBox="0 0 100 100">' + BANK.leObjs[o] + '</svg></div>' : '') + '</div>';
      return chrome();
    }
    /* place */
    const filled = S.placed.filter(x => x != null).length;
    const left = S.secEnd ? mmss(Math.max(0, (S.secEnd - Date.now()) / 1000)) : '';
    view.innerHTML = '<div class="qtitle">' + esc(T.lePlace) + ' (' + (S.leSec + 1) + '/6)' + (left ? ' — ' + left : '') + '</div>' +
      '<div class="le-pool">' + S.pool.filter(k => !S.placed.includes(k)).map(k => '<button class="le-p" data-k="' + k + '"><svg viewBox="0 0 100 100">' + BANK.leObjs[k] + '</svg></button>').join('') + '</div>' +
      '<div class="le-fields">' + Array.from({ length: 12 }, (_, i) => '<div class="le-f' + (S.placed[i] != null ? ' filled' : '') + '" data-f="' + i + '">' + (S.placed[i] != null ? '<svg viewBox="0 0 100 100">' + BANK.leObjs[S.placed[i]] + '</svg>' : '<i>' + (i + 1) + '</i>') + '</div>').join('') + '</div>' +
      '<div class="le-bar"><i style="width:' + Math.round(filled / 12 * 100) + '%"></i></div>' +
      '<div class="intro-nav center"><button class="btn-next" id="leNext" ' + (filled < 12 ? 'disabled' : '') + '>' + esc(T.next) + ' ›</button></div>';
    view.querySelectorAll('.le-p').forEach(b => b.onclick = () => { const k = +b.dataset.k; const f = S.placed.indexOf(null); if (f >= 0) { S.placed[f] = k; renderLE(view); } });
    view.querySelectorAll('.le-f').forEach(f => f.onclick = () => { const i = +f.dataset.f; if (S.placed[i] != null) { S.placed[i] = null; renderLE(view); } });
    document.getElementById('leNext').onclick = () => leNextSection(false);
    chrome();
  }
  function leNextSection(auto) {
    const ord = S.items[S.leSec].order;
    const ok = S.placed.filter((k, i) => k === ord[i]).length;
    const why = 'Section ' + (S.leSec + 1) + ' : ' + ok + ' / 12 objets placés à la bonne position.';
    S.leLast = { sec: S.leSec + 1, placed: S.placed.slice(), order: ord.slice(), ok, why };
    S.lePos = (S.lePos || 0) + ok;
    S.log.push({ n: S.leSec + 1, q: 'Section ' + (S.leSec + 1) + ' — ordre des 12 objets', given: ok + '/12 positions correctes', correct: '12/12', ok: ok === 12, ms: 30000, section: S.sec.id, why });
    S.leSec++;
    if (S.leSec >= 6) return finish();
    startBreak();
  }

  /* ═══════════════ INFORMATION HANDLING ═══════════════ */
  const mailDate = (d, arrived) => { const dt = arrived ? new Date(arrived) : new Date(Date.now() - d * 86400000); return dt.toLocaleDateString('fr-FR') + ' ' + dt.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' }); };
  function expectedMail(m) {
    const R = BANK.infoRules;
    let prio;
    if ((m.tag === 'atlas' && m.d > 2) || (m.tag === 'boreal' && m.to === R.me && m.d > 5) || m.tag === 'cascade') prio = 0;
    else if ((m.tag === 'atlas' && m.d <= 2) || (m.tag === 'boreal' && m.to === R.me && m.d <= 5) || m.to === R.support) prio = 1;
    else prio = 2;
    let act;
    if (m.tag === 'atlas') act = 0; else if (m.tag === 'boreal') act = 1; else if (m.to === R.support) act = 2; else if (m.tag === 'cascade') act = 3; else if (m.crit) act = 4; else act = -1;
    return { prio, act };
  }
  function explainMail(m) {
    const R = BANK.infoRules, e = expectedMail(m);
    const prioName = ['HIGH', 'MEDIUM', 'LOW'][e.prio];
    let prioRule;
    if (m.tag === 'atlas' && m.d > 2) prioRule = 'related to project ATLAS and sent more than 2 days ago (' + m.d + ' j)';
    else if (m.tag === 'boreal' && m.to === R.me && m.d > 5) prioRule = 'sent directly to Mr. Martin about project BOREAL more than 5 days ago (' + m.d + ' j)';
    else if (m.tag === 'cascade') prioRule = 'related to project CASCADE';
    else if (m.tag === 'atlas' && m.d <= 2) prioRule = 'referring to project ATLAS and sent in the last 2 days (' + m.d + ' j)';
    else if (m.tag === 'boreal' && m.to === R.me && m.d <= 5) prioRule = 'sent directly to Mr. Martin about BOREAL in the last 5 days (' + m.d + ' j)';
    else if (m.to === R.support) prioRule = 'addressed to ' + R.support;
    else prioRule = 'all other e-mails (hors critères HIGH/MEDIUM)';
    const actLabels = BANK.STR.fr.actV;
    const actName = e.act >= 0 ? actLabels[e.act] : 'Aucune action';
    const actRule = e.act >= 0 ? R.actions[e.act] : 'no action required';
    const why = 'Priorité ' + prioName + ' — ' + prioRule + ' · Action : ' + actName + ' (' + actRule + ').';
    return { prio: e.prio, act: e.act, prioName, actName, prioRule, actRule, why };
  }
  function renderInbox(view) {
    const T = STR(S.sec), R = BANK.infoRules;
    view.className = 'sk-main';
    view.innerHTML = '<div class="inbox-wrap"><div class="inbox-list"><div class="inbox-head"><span>Date ⇅</span><span id="ibClock"></span></div><div id="ibList"></div></div>' +
      '<div class="mailview" id="ibView"></div></div><button class="guide-fab" id="ibGuide" title="' + esc(T.guide) + '" aria-label="' + esc(T.guide) + '"><svg viewBox="0 0 24 24" width="22" height="22" fill="#fff" aria-hidden="true"><path d="M11 6.5A4.5 4.5 0 0 0 6.5 2H2v16h5.5A3.5 3.5 0 0 1 11 21zM13 6.5A4.5 4.5 0 0 1 17.5 2H22v16h-5.5A3.5 3.5 0 0 0 13 21z"/></svg></button>' +
      '<div class="guide-panel" id="guidePanel"><div class="guide-box"><h3>' + esc(T.guide) + '</h3>' + guideHTML() + '<div class="row end"><button class="btn" id="guideClose">OK</button></div></div></div>';
    paintInboxList();
    paintMail();
    S.clockId = setInterval(() => { const c = document.getElementById('ibClock'); if (!c) return; const d = new Date(); c.textContent = d.toLocaleDateString('fr-FR') + ' ' + d.toLocaleTimeString('fr-FR'); }, 1000);
    const c0 = document.getElementById('ibClock'); if (c0) { const d0 = new Date(); c0.textContent = d0.toLocaleDateString('fr-FR') + ' ' + d0.toLocaleTimeString('fr-FR'); }
    document.getElementById('ibGuide').onclick = () => document.getElementById('guidePanel').classList.add('on');
    const bk = document.getElementById('skBook'); if (bk) bk.onclick = () => document.getElementById('guidePanel').classList.add('on');
    document.getElementById('guideClose').onclick = () => document.getElementById('guidePanel').classList.remove('on');
    chrome();
  }
  function guideHTML() {
    const R = BANK.infoRules;
    return '<p><b>Priority is HIGH for the e-mails:</b></p><ul>' + R.high.map(x => '<li>' + esc(x) + '</li>').join('') + '</ul>' +
      '<p><b>Priority is MEDIUM for the e-mails:</b></p><ul>' + R.medium.map(x => '<li>' + esc(x) + '</li>').join('') + '</ul>' +
      '<p>' + esc(R.low) + '</p><p>The periods of time refer exclusively to the date and do not depend on the hours or minutes, weekends or public holidays.</p>' +
      '<p><b>React to the e-mails:</b></p><ul>' + R.actions.map(x => '<li>' + esc(x) + '</li>').join('') + '</ul>';
  }
  function paintInboxList() {
    const el = document.getElementById('ibList'); if (!el) return;
    const sorted = S.mails.map((m, i) => ({ m, i })).sort((a, b) => (b.m.arrived || 0) - (a.m.arrived || 0) || a.m.d - b.m.d);
    el.innerHTML = sorted.map(({ m, i }) => '<div class="mail' + (i === S.mail ? ' on' : '') + (m.isNew ? ' new' : '') + '" data-i="' + i + '">' +
      (!m.read ? '<i class="dotu"></i>' : '') +
      '<div class="m1"><span>' + esc(m.from) + '</span><span class="prio ' + (m.prio === 0 ? 'H' : m.prio === 1 ? 'M' : m.prio === 2 ? 'L' : '') + '">' + (m.prio != null ? ['H', 'M', 'L'][m.prio] : '') + '</span></div>' +
      '<div class="mto">To: ' + esc(m.to) + '</div>' +
      '<div class="m2">' + esc(m.subj) + '</div><div class="m3">' + mailDate(m.d, m.arrived) + '</div><i class="flag">⚑</i></div>').join('');
    el.querySelectorAll('.mail').forEach(x => x.onclick = () => { S.mail = +x.dataset.i; S.mails[S.mail].isNew = false; S.mails[S.mail].read = true; paintInboxList(); paintMail(); });
  }
  function paintInboxFb(m) {
    const box = document.getElementById('ibFb');
    if (!box) return;
    if (!P.instantFb() || (m.prio == null && m.act == null)) { box.innerHTML = ''; return; }
    const T = STR(S.sec), ex = explainMail(m);
    const pOk = m.prio === ex.prio, aOk = (m.act == null ? -1 : m.act) === ex.act;
    const given = (m.prio != null ? T.prioV[m.prio] : '—') + ' / ' + (m.act != null && m.act >= 0 ? T.actV[m.act] : T.noAction);
    const expected = T.prioV[ex.prio] + ' / ' + (ex.act >= 0 ? T.actV[ex.act] : T.noAction);
    box.innerHTML = ifbHTML({
      ok: pOk && aOk,
      given,
      expected,
      why: ex.why,
      nextLabel: S.mail < S.mails.length - 1 ? 'E-mail suivant ›' : false
    });
    const nx = box.querySelector('#ifbNext');
    if (nx) nx.onclick = () => {
      S.mail = (S.mail + 1) % S.mails.length;
      S.mails[S.mail].isNew = false; S.mails[S.mail].read = true;
      paintInboxList(); paintMail();
    };
  }
  function paintMail() {
    const T = STR(S.sec), m = S.mails[S.mail], el = document.getElementById('ibView'); if (!el || !m) return;
    el.innerHTML = '<div class="row"><span class="k">From</span><span>' + esc(m.from) + '</span></div>' +
      '<div class="row"><span class="k">To</span><span>' + esc(m.to) + '</span></div>' +
      '<div class="row"><span class="k">Date</span><span>' + mailDate(m.d, m.arrived) + '</span></div>' +
      '<div class="row"><span class="k">Subject</span><span><b>' + esc(m.subj) + '</b></span></div>' +
      '<div class="body">' + esc(m.body) + '</div>' +
      '<div class="mail-ctl"><label>' + esc(T.prio) + '</label><select id="mPrio"><option value="">—</option>' + T.prioV.map((p, i) => '<option value="' + i + '"' + (m.prio === i ? ' selected' : '') + '>' + p + '</option>').join('') + '</select>' +
      '<label>' + esc(T.action) + '</label><select id="mAct"><option value="-1">' + esc(T.noAction) + '</option>' + T.actV.map((p, i) => '<option value="' + i + '"' + (m.act === i ? ' selected' : '') + '>' + esc(p) + '</option>').join('') + '</select></div>' +
      '<div id="ibFb"></div>';
    document.getElementById('mPrio').onchange = (e) => { m.prio = e.target.value === '' ? null : +e.target.value; paintInboxList(); paintInboxFb(m); };
    document.getElementById('mAct').onchange = (e) => { m.act = +e.target.value; paintInboxFb(m); };
    paintInboxFb(m);
  }

  /* ═══════════════ LANGUES (anglais / français) ═══════════════ */
  function langBank() {
    const lang = S.sec.lang === 'en' ? 'en' : 'fr';
    return [{ type: 'flu', sec: 240 }, { type: 'voc', sec: 240 }, { type: 'spe', sec: 120 }]
      .map((x, k) => Object.assign({ sec: x.sec }, DRILL.langSection(lang, x.type, (S.seed || 1) + k * 977)));
  }
  function langBuildSection() { S.cur = langBank()[S.sub]; S.langIdx = 0; S.langPhase = 'examples'; S.langDone = 0; S.langCount = S.cur.items.length; }
  function langExample(view) {
    const T = STR(S.sec), q = S.cur.at(S.langIdx);
    view.className = 'sk-main';
    view.innerHTML = '<div class="qinstr">EXEMPLE — ' + esc(instrFor(S.cur.type)) + '</div>' + langItemHTML(q) ;
    bindLangOpts(view, (i) => { const curS = S; view.querySelectorAll('.optrow').forEach((x, k) => { if (k === q.a) x.classList.add('ok'); else if (k === i) x.classList.add('ko'); }); S.exTimer = setTimeout(() => { if (S !== curS) return; S.langIdx++; if (S.langIdx >= 2) S.langPhase = 'ready'; render(); }, 800); });
    chrome();
  }
  const instrFor = (t) => STR(S.sec).langInstr[t];
  function langItemHTML(q) {
    const list = (q.o || []).slice();
    return '<div class="stmtcard">' + esc(q.s) + '</div><div class="optrows">' + list.map((o, i) => '<button class="optrow" data-i="' + i + '">' + esc(o) + '</button>').join('') +
      '<button class="optrow" data-i="99">?</button></div>';
  }
  function bindLangOpts(view, cb) { view.querySelectorAll('.optrow').forEach(b => b.onclick = () => cb(+b.dataset.i)); }
  function langReady(view) {
    const T = STR(S.sec), names = { en: ['Fluency', 'Vocabulary', 'Spelling'], fr: ['Aisance', 'Vocabulaire', 'Orthographe'] };
    const lang = S.sec.lang === 'en' ? 'en' : 'fr';
    view.className = 'sk-main narrow';
    view.innerHTML = '<div class="intro-page"><p class="k">' + esc(names[lang][S.sub]) + '</p>' +
      '<p>' + (S.sec.lang === 'en'
        ? 'You are about to start this section. It lasts ' + Math.round(S.cur.sec / 60) + ' minute(s) and ends automatically. Answer, then click “next” to move on.'
        : 'Vous allez commencer cette section. Elle dure ' + Math.round(S.cur.sec / 60) + ' minute(s) et se termine automatiquement. Répondez puis cliquez sur « suivant ».') + '</p>' +
      '<div class="intro-nav center"><button class="btn-next" id="lgStart">' + esc(T.start) + ' ›</button></div></div>';
    document.getElementById('lgStart').onclick = () => { S.phase = 'run'; S.langPhase = 'run'; S.langIdx = 0; S.langDone = 0; S.qStart = Date.now(); S.secEnd = Date.now() + S.cur.sec * 1000; render(); };
    return chrome();
  }
  function renderLang(view) {
    const T = STR(S.sec);
    if (S.langPhase === 'examples') return langExample(view);
    if (S.langPhase === 'ready') return langReady(view);
    if (S.langPhase === 'inter') {
      view.className = 'sk-main';
      const nxt = S.sub + 1;
      view.innerHTML = '<div class="intro-page"><p>' + (S.sec.lang === 'en' ? 'The previous section is now complete.' : 'La section précédente est maintenant terminée.') + '</p><p>' +
        (S.sec.lang === 'en' ? 'You will now see the 2 examples of the next section.' : 'Vous allez maintenant découvrir les 2 exemples de la section suivante.') + '</p>' +
        '<div class="intro-nav center"><button class="btn-next" id="lgNext">' + esc(T.next) + ' ›</button></div></div>';
      document.getElementById('lgNext').onclick = () => { S.sub = nxt; langBuildSection(); S.langPhase = 'examples'; S.phase = 'example'; S.secEnd = 0; render(); };
      return chrome();
    }
    const q = S.cur.at(S.langIdx);
    view.className = 'sk-main';
    view.innerHTML = '<div class="qinstr">' + esc(instrFor(S.cur.type)) + '</div>' + langItemHTML(q) +
      '<div class="langnext"><button class="langchev" id="lgNext" disabled title="' + esc(T.next) + '">›</button></div>';
    const advance = () => {
      clearTimeout(S.lgTimer); clearTimeout(S.fbTimer);
      const i = S.langSel == null ? 99 : S.langSel, qq = S.cur.at(S.langIdx);
      const unk = i === 99, ok = unk ? null : (i === qq.a);
      S.log.push({ n: S.log.length + 1, q: qq.s, given: unk ? '?' : qq.o[i], correct: qq.o[qq.a], ok, ms: Date.now() - S.qStart, section: S.sec.id, why: qq.w || '' });
      S.qStart = Date.now(); S.langSel = null; S.langDone++; S.langIdx++;
      render();                                  /* la section ne s'épuise jamais : le générateur prend le relais */
    };
    bindLangOpts(view, (i) => {
      S.langSel = i;
      view.querySelectorAll('.optrow').forEach(x => {
        const ki = +x.dataset.i;
        x.classList.remove('sel', 'ok', 'ko');
        if (ki === i) x.classList.add('sel');
        if (P.instantFb()) {
          if (ki === q.a) x.classList.add('ok');
          else if (ki === i && i !== 99) x.classList.add('ko');
        }
      });
      const nx = document.getElementById('lgNext'); nx.disabled = false;
      if (P.instantFb()) {
        const unk = i === 99, ok = unk ? null : (i === q.a);
        showInstantFb(view, {
          ok,
          badge: unk ? '● Neutre (?)' : undefined,
          given: unk ? '? (neutre)' : q.o[i],
          expected: q.o[q.a],
          why: q.w || ('Réponse attendue : ' + q.o[q.a])
        }, advance, S.cur.type !== 'flu' ? 3200 : 0);
      } else if (S.cur.type !== 'flu') {
        clearTimeout(S.lgTimer);
        S.lgTimer = setTimeout(() => { if (S && S.phase === 'run' && S.langPhase === 'run' && S.langSel === i) advance(); }, 420);
      }
    });
    document.getElementById('lgNext').onclick = advance;
    chrome();
  }
  function langNextSection(auto) {
    S.secEnd = 0;                       /* évite la re-déclenche de la fin de section */
    clearTimeout(S.lgTimer); clearTimeout(S.fbTimer);
    if (auto) { U.toast(S.sec.lang === 'en' ? 'Time is up for this section' : 'Le temps de cette section est écoulé', '', 2200); }
    if (S.sub < 2) { S.langPhase = 'inter'; S.phase = 'example'; render(); } else finish();
  }

  /* ═══════════════ MÉCANIQUE ═══════════════ */
  function mechItem(view, it, isEx) {
    view.className = 'sk-main';
    const hasAns = !isEx && S.sel != null;
    const showFb = hasAns && P.instantFb();
    view.innerHTML = '<div class="qwrap"><div class="qtitle" style="font-size:15px;font-weight:600;text-align:left">' + (isEx ? 'EXAMPLE — ' : '') + esc(it.q) + '</div>' + (isEx ? exNoteHTML() : '') +
      '<div class="optrows">' + it.o.map((o, i) => {
        let cls = S.sel === i ? ' sel' : '';
        if (showFb) { if (i === it.a) cls += ' ok'; else if (i === S.sel) cls += ' ko'; }
        return '<button class="optrow' + cls + '" data-i="' + i + '">' + esc(o) + '</button>';
      }).join('') + '</div>' +
      (showFb ? ifbHTML({
        ok: S.sel === it.a,
        given: it.o[S.sel],
        expected: it.o[it.a],
        why: it.why || it.w || '',
        nextLabel: S.i < S.items.length - 1 ? 'Continuer ›' : 'Terminer ›'
      }) : '') +
      '<div class="panel-gray" style="margin-top:18px">' + sceneSVG(it.sc) + '</div></div>' + navPadHTML();
    view.querySelectorAll('.optrow').forEach(b => b.onclick = () => {
      S.sel = +b.dataset.i;
      if (isEx) { const curS = S; view.querySelectorAll('.optrow').forEach((x, k) => { if (k === it.a) x.classList.add('ok'); else if (k === S.sel) x.classList.add('ko'); }); S.exTimer = setTimeout(() => { if (S === curS) exampleDone(it.a === S.sel); }, 700); return; }
      S.nvInfo = S.nvInfo || {};
      S.nvInfo[S.i] = { ms: Date.now() - S.qStart };
      S.answers[S.i] = S.sel;
      mechItem(view, it, false);
    });
    const ifbN = document.getElementById('ifbNext');
    if (ifbN) ifbN.onclick = () => {
      if (S.i < S.items.length - 1) { S.i++; S.qStart = Date.now(); render(); }
      else finish();
    };
    bindNav(view, isEx);
    chrome();
  }
  function sceneSVG(kind) {
    const c = '#6b6b6b', hl = '#3d3d3d';
    const gear = (cx, cy, r, label) => '<g><circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="none" stroke="' + c + '" stroke-width="3"/>' +
      Array.from({ length: 12 }, (_, i) => { const a = i * 30 * Math.PI / 180; return '<rect x="' + (cx + (r + 3) * Math.cos(a) - 3).toFixed(1) + '" y="' + (cy + (r + 3) * Math.sin(a) - 3).toFixed(1) + '" width="6" height="6" fill="' + c + '"/>'; }).join('') +
      '<text x="' + cx + '" y="' + (cy + 5) + '" font-size="15" font-weight="700" fill="' + hl + '" text-anchor="middle">' + label + '</text></g>';
    const pul = (cx, cy, r, label) => '<g><circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="none" stroke="' + c + '" stroke-width="3"/><circle cx="' + cx + '" cy="' + cy + '" r="3.5" fill="' + c + '"/><text x="' + cx + '" y="' + (cy + 5) + '" font-size="14" font-weight="700" fill="' + hl + '" text-anchor="middle">' + label + '</text></g>';
    const ln = (x1, y1, x2, y2) => '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="' + c + '" stroke-width="2.5"/>';
    switch (kind) {
      case 'gears2': return sv2(360, 180, gear(110, 90, 48, 'A') + gear(222, 90, 48, 'B'));
      case 'gears3': return sv2(420, 180, gear(80, 90, 40, 'A') + gear(178, 90, 40, 'B') + gear(276, 90, 40, 'C'));
      case 'gears4': return sv2(500, 180, gear(70, 90, 34, 'A') + gear(158, 90, 34, 'B') + gear(246, 90, 34, 'C') + gear(334, 90, 34, 'D'));
      case 'gears2size': return sv2(420, 180, gear(100, 90, 32, 'A') + gear(260, 90, 66, 'B'));
      case 'belt': return sv2(420, 200, pul(110, 100, 56, 'A') + pul(300, 100, 56, 'B') + ln(110, 44, 300, 44) + ln(110, 156, 300, 156));
      case 'beltcross': return sv2(420, 220, pul(110, 110, 56, 'A') + pul(300, 110, 56, 'B') + ln(110, 54, 300, 166) + ln(110, 166, 300, 54));
      case 'lever': return sv2(460, 180, ln(30, 130, 430, 130) + '<path d="M230 130 L230 168" stroke="' + hl + '" stroke-width="6"/>' + '<rect x="26" y="92" width="48" height="36" fill="' + c + '"/>' + ln(410, 130, 410, 100) + '<path d="M402 104 L410 88 L418 104 Z" fill="' + c + '"/>');
      case 'pulley1': return sv2(300, 220, pul(150, 50, 42, 'P') + ln(150, 92, 150, 160) + '<rect x="120" y="160" width="60" height="40" fill="' + c + '"/>');
      case 'pulley2': return sv2(320, 240, pul(100, 44, 30, 'F') + pul(200, 44, 30, 'F') + ln(100, 74, 100, 170) + ln(200, 74, 200, 170) + '<rect x="110" y="170" width="80" height="42" fill="' + c + '"/>');
      case 'pulley3': return sv2(380, 240, pul(80, 40, 26, 'F') + pul(170, 40, 26, 'F') + pul(260, 40, 26, 'F') + ln(80, 66, 80, 168) + ln(170, 66, 170, 168) + ln(260, 66, 260, 168) + '<rect x="100" y="168" width="140" height="40" fill="' + c + '"/>');
      case 'spring': return sv2(280, 220, ln(50, 36, 230, 36) + '<path d="M140 36 ' + Array.from({ length: 9 }, (_, i) => 'L' + (i % 2 ? 112 : 168) + ' ' + (48 + i * 11)).join(' ') + '" stroke="' + c + '" stroke-width="3.5" fill="none"/>' + '<rect x="100" y="150" width="80" height="40" fill="' + c + '"/>');
      case 'axle': return sv2(400, 200, pul(130, 100, 62, 'G') + pul(280, 100, 24, 'P') + ln(130, 100, 280, 100));
      default: return sv2(300, 160, gear(150, 80, 44, '·'));
    }
  }
  const sv2 = (w, h, inner) => '<svg viewBox="0 0 ' + w + ' ' + h + '" width="100%" style="max-height:240px" xmlns="http://www.w3.org/2000/svg">' + inner + '</svg>';
  const renderMech = (view) => { S.sel = S.answers[S.i] == null ? null : S.answers[S.i]; mechItem(view, S.items[S.i], false); };

  /* ═══════════════ SWITCH CHALLENGE ═══════════════ */
  function renderSwitch(view) {
    S.fbLock = false;
    while (S.items.length <= S.i) S.items.push(DRILL.swItem(S.seed + S.items.length * 977, S.items.length));
    const it = S.items[S.i];
    view.className = 'sk-main narrow';
    view.innerHTML = '<div class="sw-wrap"><div class="sw-row">' + it.input.map(k => '<div class="sw-tile">' + symSVG(BANK.SYM_SW[k]) + '</div>').join('') + '</div>' +
      machineHTML('<div style="display:flex;gap:14px">' + it.codes.map((c, i) => '<button class="sw-codeopt" data-i="' + i + '">' + c.join(' ') + '</button>').join('') + '</div>') +
      '<div class="sw-row">' + it.output.map(k => '<div class="sw-tile">' + symSVG(BANK.SYM_SW[k]) + '</div>').join('') + '</div></div>';
    view.querySelectorAll('.sw-codeopt').forEach(b => b.onclick = () => {
      if (S.fbLock) return;
      S.fbLock = true;
      const i = +b.dataset.i, ok = i === it.ans;
      b.classList.add(ok ? 'ok' : 'ko');
      const goodBtn = view.querySelectorAll('.sw-codeopt')[it.ans];
      if (goodBtn) goodBtn.classList.add('ok');
      const why = swWhy(it);
      S.log.push({ n: S.log.length + 1, q: 'Code appliqué : entrée → sortie', given: it.codes[i].join(''), correct: it.codes[it.ans].join(''), ok, ms: Date.now() - S.qStart, section: S.sec.id, why });
      S.qStart = Date.now(); S.i++;
      if (!P.instantFb()) {
        S.fbTimer = setTimeout(() => { if (S && S.phase === 'run') { S.fbLock = false; render(); } }, 380);
        return;
      }
      showInstantFb(view.querySelector('.sw-wrap') || view, {
        ok,
        given: it.codes[i].join(' '),
        expected: it.codes[it.ans].join(' '),
        why,
        fig: swFigHTML(it, i)
      }, () => { if (S && S.phase === 'run') render(); }, 4800);
    });
    chrome();
  }

  /* ═══════════════ Intertitres & fin ═══════════════ */
  function finish() {
    if (!S || S.done) return;
    S.done = true;
    if (tick) { clearInterval(tick); tick = null; }
    clearTimeout(S.nvTimer); clearTimeout(S.lgTimer); clearTimeout(S.fbTimer); clearTimeout(S.chatTimer);
    const sec = S.sec;
    let correct = 0, graded = 0, answered = 0;
    if (sec.kind === 'numverb' || sec.kind === 'mech') {
      if (sec.kind === 'numverb' && S.nvAns != null && S.answers[S.i] == null) S.answers[S.i] = S.nvAns;
      S.items.forEach((it, i) => {
        const a = S.answers[i], info = (S.nvInfo && S.nvInfo[i]) || {};
        S.log.push({ n: i + 1, q: nvText(it.q), given: a == null ? '—' : tfText(it, a), correct: tfText(it, it.a), ok: a != null && a === it.a, ms: info.ms || 0, section: sec.id, why: nvText(it.why || it.w || '') });
      });
      graded = S.items.length; answered = Object.keys(S.answers).length;
      correct = S.log.filter(r => r.ok === true).length;
    } else if (sec.kind === 'lang') {
      const good = S.log.filter(r => r.ok === true).length, bad = S.log.filter(r => r.ok === false).length;
      correct = good; graded = good + bad; answered = S.log.length;
      S.langNet = good - bad;
    } else if (sec.kind === 'culture') {
      correct = S.log.reduce((n, r) => n + (r.mostOk ? 1 : 0) + (r.leastOk ? 1 : 0), 0);
      graded = S.items.length * 2;
      answered = S.log.length * 2;
    } else if (sec.kind === 'blocks') { graded = 0; answered = S.log.length; }
    else if (sec.kind === 'chatsjt') { graded = 0; answered = S.log.length; }   /* réponses libres du chat : comportemental */
    else if (sec.kind === 'seqmem') { correct = S.lePos || 0; graded = 72; answered = 72; }
    else if (sec.kind === 'inbox') {
      S.mails.forEach((m, i) => { const ex = explainMail(m); const pOk = m.prio === ex.prio, aOk = (m.act == null ? -1 : m.act) === ex.act; if (pOk) correct++; if (aOk) correct++; graded += 2; answered += 2; S.log.push({ n: i + 1, q: m.subj, given: (m.prio != null ? ['HIGH', 'MEDIUM', 'LOW'][m.prio] : '—') + ' / ' + (m.act != null ? m.act + 1 : '—'), correct: ['HIGH', 'MEDIUM', 'LOW'][ex.prio] + ' / ' + (ex.act + 1), ok: pOk && aOk, ms: 0, section: sec.id, why: ex.why }); });
    } else { correct = S.log.filter(r => r.ok === true).length; graded = S.log.filter(r => r.ok !== null && r.ok !== undefined).length; answered = S.log.length; }
    const behavioural = graded === 0;
    const attempt = {
      id: 'A' + Date.now(), at: new Date().toISOString(), date: new Date().toLocaleDateString('fr-FR'), time: new Date().toLocaleTimeString('fr-FR'),
      user: PROFILES.current() || 'Invité', section: sec.id, sectionName: sec.home, behavioural,
      items: graded || answered || 1, answered, correct, wrong: graded - correct, net: sec.kind === 'lang' ? (S.langNet || 0) : null, skipped: Math.max(0, (graded || answered) - answered),
      accuracy: behavioural ? null : (graded ? correct / graded : 0),
      avgMs: (() => { const t = S.log.filter(r => r.ms > 0); return t.length ? Math.round(t.reduce((a, b) => a + b.ms, 0) / t.length) : 0; })(),
      ms: Date.now() - S.t0, mode: 'real'
    };
    P.add(attempt, S.log.map(r => Object.assign({}, r)));
    S.attempt = attempt;
    S.phase = 'end';
    document.getElementById('navGrid').classList.remove('on');
    render();
  }
  const COREmmss = mmss;
  function renderEnd(view) {
    const a = S.attempt, lang = P.lang(S.sec.id);
    const cultureBreakdown = S.sec.kind === 'culture'
      ? '<p class="tiny">' + (lang === 'fr' ? 'Plus efficace : ' : 'Most effective: ') + S.log.filter(r => r.mostOk).length + '/18 · ' +
        (lang === 'fr' ? 'Moins efficace : ' : 'Least effective: ') + S.log.filter(r => r.leastOk).length + '/18</p>' : '';
    view.className = 'sk-main narrow';
    view.innerHTML = '<div class="intro-page"><p class="k">' + (lang === 'fr' ? 'Test terminé.' : 'Test finished.') + '</p>' +
      (a.behavioural ? '<p>' + (lang === 'fr' ? 'Vos réponses ont été enregistrées : ce questionnaire ne comporte pas de bonne réponse.' : 'Your answers have been recorded: this questionnaire has no right or wrong answers.') + '</p>'
        : '<p>' + (lang === 'fr' ? 'Score : ' : 'Score: ') + '<b>' + a.correct + ' / ' + a.items + '</b> (' + U.pct(a.accuracy) + ')</p>') + cultureBreakdown +
      '<p class="tiny">' + (lang === 'fr' ? 'Durée : ' : 'Time: ') + COREmmss(a.ms / 1000) + '</p>' +
      '<p class="tiny" style="color:var(--tx3)">' + (lang === 'fr' ? 'Le détail question par question est disponible dans le menu ≡ → Feedback détaillé.' : 'The question-by-question detail is available in the ≡ menu → Feedback.') + '</p>' +
      '<div class="intro-nav"><button class="btn-intro" id="endHome">‹ ' + (lang === 'fr' ? 'Tâches' : 'Tasks') + '</button>' +
      '<div class="end-actions"><button class="btn-next" id="endFb">' + (lang === 'fr' ? 'Feedback' : 'Feedback') + '</button>' +
      (S.sec.next ? '<button class="btn-next" id="endNext">' + (lang === 'fr' ? 'Test suivant' : 'Next test') + ' ›</button>' : '') +
      '</div></div></div>';
    document.getElementById('endHome').onclick = () => { destroy(); location.hash = '#/'; };
    document.getElementById('endFb').onclick = () => { destroy(); location.hash = '#/feedback'; };
    const endNext = document.getElementById('endNext');
    if (endNext) endNext.onclick = () => { const nx = S.sec.next; destroy(); location.hash = '#/run/' + nx; };
    chrome();
  }

  /* ═══════════════ Clavier ═══════════════ */
  document.addEventListener('keydown', (e) => {
    if (!S || S.done || !P.settings().keyboard) return;
    if (S.keyHandler && (S.sec.kind === 'edots')) return S.keyHandler(e);
    if (S.phase !== 'run') return;
    const k = e.key;
    if (S.fbLock && (k === 'Enter' || k === ' ')) { const n = document.getElementById('ifbNext'); if (n) { e.preventDefault(); n.click(); } return; }
    if (S.fbLock) return;
    if (S.sec.kind === 'latin' && k >= '1' && k <= '4') { const b = document.querySelectorAll('.ded-opt')[+k - 1]; if (b) b.click(); }
    if (S.sec.kind === 'switchcode' && k >= '1' && k <= '3') { const b = document.querySelectorAll('.sw-codeopt')[+k - 1]; if (b) b.click(); }
    if (S.sec.kind === 'mech' && k >= '1' && k <= '3') { const b = document.querySelectorAll('.optrow')[+k - 1]; if (b) b.click(); }
    if (S.sec.kind === 'numverb' && (k === '1' || k === '2' || k === '3')) { const b = document.querySelectorAll('.tfbtn')[+k - 1]; if (b) b.click(); }
    if (S.sec.kind === 'lang' && k >= '1' && k <= '5') { const b = document.querySelectorAll('.optrow')[+k - 1]; if (b) b.click(); }
  });

  return { SECTIONS, BANKS, byId, start, destroy, finish, P, PROFILES, STR, mmss, toggleNav, expectedMail, explainMail, get current() { return S; },
           /* crochets de test (tools/test-banks.js) : ne font pas partie de l'UI */
           __render: render, __beginRun: beginRun, __chat: { send: chatSend, arrive: chatArrive } };
})();

if (typeof window !== 'undefined') window.CORE = CORE; else globalThis.CORE = CORE;
