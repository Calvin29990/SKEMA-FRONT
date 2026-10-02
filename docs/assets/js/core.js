/* ═══════════════════════════════════════════════════════════════
   core.js — Registre des sections, moteurs de session, progression,
             feedback et stockage local.
   Assessment Trainer — Calvin MINANG
   ═══════════════════════════════════════════════════════════════ */
'use strict';

const CORE = (() => {

  const DL = { exam: '2026-10-07', examEnd: '2026-10-09' };

  /* Langue des consignes pendant les exercices (sélecteur de la plateforme) */
  const LANG = {
    fr: { validate:'Valider', skip:'Passer', quit:'Quitter', next:'Suivant', nextSub:'Affirmation suivante',
          hint:'Raccourcis 1-4 puis Entrée', right:'✔ Correct', wrong:'✘ Incorrect', answer:'Réponse',
          pickFig:'Cliquez la figure qui complète la suite (1-3)', pickLk:'Pas de bonne réponse — choisissez vite, restez cohérent.',
          same:'Identiques', diff:'Différentes', itemNext:'Item suivant', affirm:'Affirmation',
          memor:'Mémorisez les cases', reproduce:'Reproduisez les cases', selection:'Sélection' },
    en: { validate:'Submit', skip:'Skip', quit:'Quit', next:'Next', nextSub:'Next statement',
          hint:'Keys 1-4 then Enter', right:'✔ Correct', wrong:'✘ Incorrect', answer:'Answer',
          pickFig:'Click the figure that completes the series (1-3)', pickLk:'No right answer — answer quickly and stay consistent.',
          same:'Identical', diff:'Different', itemNext:'Next item', affirm:'Statement',
          memor:'Memorise the highlighted cells', reproduce:'Reproduce the cells', selection:'Selection' }
  };
  const T = () => LANG[(S && S.lang) === 'en' ? 'en' : 'fr'];

  /* ═══════════════════════════════════════════════════════════
     REGISTRE DES SECTIONS
     mode     : mc | likert | grid | pair | switch
     source   : 'fixed' (banque finie, contenu figé) | 'infinite' (généré)
     ═══════════════════════════════════════════════════════════ */
  const SECTIONS = [
    {
      id: 'verbal', name: 'Verbal Reasoning', fr: 'Raisonnement verbal', icon: '📖', family: 'cognitive',
      mode: 'mc', source: 'fixed', items: 36, dur: 15, perItem: 45, color: 'blu',
      desc: 'Passages en anglais + 3 affirmations : True / False / Cannot say. Banque de 12 passages (36 items) fidèle au format.',
      hint: 'On ne répond QUE sur la base du passage. « Cannot say » n’est pas « je ne sais pas » : c’est « le texte ne permet pas de trancher ».',
      need: 'Corpus fixe — à terminer puis à refaire pour la régularité.'
    },
    {
      id: 'verbalX', name: 'English Battery ∞', fr: 'Batterie anglaise illimitée', icon: '♾️', family: 'cognitive',
      mode: 'mc', source: 'infinite', items: 40, dur: 13, perItem: 40, color: 'blu',
      desc: 'Même format, passages inédits à chaque session (valeurs, secteurs, périodes tirés au sort). Objectif : 50 réponses exactes minimum par run.',
      hint: 'Cible = 50 réponses exactes. Vitesse : ~40 s par item, sans jamais relire le passage en entier.',
      need: 'Batterie illimitée : à répéter jusqu’à obtenir 50/… sans faute.'
    },
    {
      id: 'numerical', name: 'Numerical Reasoning', fr: 'Raisonnement numérique', icon: '📊', family: 'cognitive',
      mode: 'mc', source: 'fixed', items: 48, dur: 15, perItem: 75, color: 'grn',
      desc: 'Tableaux de données + questions chiffrées. Paper A = 48 items, Paper B = 37 items (extrait), calculateur autorisée.',
      hint: 'Toujours partir de l’unité demandée, vérifier le sens de la variation, et se méfier des pièges de part/variation.',
      need: 'Banque figée (37 ou 48 selon le paper choisi).'
    },
    {
      id: 'deductive', name: 'Déductif', fr: 'Raisonnement déductif', icon: '🧩', family: 'cognitive',
      mode: 'mc', source: 'fixed', items: 12, dur: 9, perItem: 45, color: 'pur',
      desc: 'Matrices logiques : trouver les règles (forme, couleur, position, remplissage) et en déduire la case manquante.',
      hint: 'Chercher d’abord la règle la plus simple ligne par ligne, puis colonne par colonne.',
      need: 'Banque figée : 12 matrices.'
    },
    {
      id: 'switch', name: 'Deductive Switch Challenge', fr: 'Switch Challenge', icon: '🔀', family: 'cognitive',
      mode: 'switch', source: 'fixed', items: 30, dur: 6, perItem: 30, color: 'pur',
      desc: 'On vous donne une suite d’entrée et une suite de sortie ; sélectionnez la combinaison d’échanges qui transforme l’une en l’autre.',
      hint: 'Repérer d’abord la position d’un seul symbole, éliminer, puis vérifier le second.',
      need: 'Banque figée : 30 séries, difficulté croissante.'
    },
    {
      id: 'inductive', name: 'Inductif', fr: 'Raisonnement inductif', icon: '🔷', family: 'cognitive',
      mode: 'mc', source: 'fixed', items: 30, dur: 8, perItem: 30, color: 'pur',
      desc: 'Séries de figures : conjecturez la suite selon la rotation, le nombre, le remplissage ou la couleur.',
      hint: 'Chaque série n’a qu’une seule règle dominante : la chercher avant de regarder les options.',
      need: 'Banque figée : 30 séries.'
    },
    {
      id: 'concentration', name: 'Concentration', fr: 'Capacité de concentration', icon: '👁️', family: 'cognitive',
      mode: 'pair', source: 'fixed', items: 60, dur: 3, perItem: 2.5, color: 'amb',
      desc: 'Deux figures très proches : identiques ou différentes ? Réponse en 2,5 secondes. Le rythme est volontairement inconfortable.',
      hint: 'Ne jamais hésiter plus de 1,5 s : l’erreur coûte moins cher que l’attente.',
      need: 'Banque figée : 60 paires.'
    },
    {
      id: 'learning', name: 'Learning Efficiency', fr: 'Efficacité d’apprentissage', icon: '⚡', family: 'cognitive',
      mode: 'grid', source: 'fixed', items: 20, dur: 6, perItem: 45, color: 'amb',
      desc: '5 cases clignotent brièvement dans une grille 5×5 : reproduisez-les. Le temps d’exposition diminue au fil des questions.',
      hint: 'Mémoriser des repères (ligne/colonne, motif), pas des positions indépendantes.',
      need: 'Banque figée : 20 planches, temps décroissant.'
    },
    {
      id: 'memory', name: 'Mémoire de travail', fr: 'Concentration avancée', icon: '🧠', family: 'cognitive',
      mode: 'grid', source: 'fixed', items: 15, dur: 4, perItem: 45, color: 'amb',
      desc: 'Grille 5×5 avec cases colorées : mémorisez puis reproduisez. Variante « capacité de concentration ».',
      hint: 'Associer une couleur à une zone de la grille plutôt qu’à une case isolée.',
      need: 'Banque figée : 15 planches.'
    },
    {
      id: 'info', name: 'Traitement de l’information', fr: 'Valeur de l’information', icon: '💡', family: 'cognitive',
      mode: 'mc', source: 'fixed', items: 18, dur: 9, perItem: 90, color: 'teal',
      desc: 'Décider si une information vaut son coût : valeur de l’information, espérance, bornes binaires. Format proche de Morgan Stanley.',
      hint: 'VI = espérance avec information − espérance sans information. Comparer ensuite au coût.',
      need: 'Banque figée : 18 items.'
    },
    {
      id: 'mech', name: 'Raisonnement mécanique', fr: 'Raisonnement mécanique', icon: '⚙️', family: 'cognitive',
      mode: 'mc', source: 'fixed', items: 24, dur: 10, perItem: 60, color: 'gray',
      desc: 'Engrenages, courroies, poulies, leviers, ressorts : sens de rotation et efforts.',
      hint: 'Engrenages : le sens s’inverse à chaque contact. Courroie droite : même sens. Courroie croisée : sens opposés.',
      need: 'Banque figée : 24 items.'
    },
    {
      id: 'workBehaviour', name: 'Comportement professionnel', fr: 'Work behaviour', icon: '🧭', family: 'behavioural',
      mode: 'likert', source: 'fixed', items: 36, dur: 8, perItem: 12, color: 'pur',
      desc: 'Affirmations à évaluer sur une échelle de fréquence. Aucune bonne réponse : le test mesure la cohérence et l’absence d’hésitation.',
      hint: 'Répondre vite et rester cohérent d’une question à l’autre. L’inconfort est attendu — ne pas chercher la réponse « parfaite ».',
      need: 'Banque figée : 36 affirmations.'
    },
    {
      id: 'motivation', name: 'Motivation & intérêts', fr: 'Centres d’intérêt professionnels', icon: '🎯', family: 'behavioural',
      mode: 'likert', source: 'fixed', items: 30, dur: 6, perItem: 12, color: 'pur',
      desc: '« À quel point souhaitez-vous… » sur une échelle de 4 points. Mesure l’adéquation au poste, pas une performance.',
      hint: 'Répondre en fonction du poste visé (marché/trading/sales), pas de manière générique.',
      need: 'Banque figée : 30 items.'
    }
  ];
  const byId = (id) => SECTIONS.find(s => s.id === id);

  /* ═══════════════════════════════════════════════════════════
     CONSTRUCTION DES ITEMS
     ═══════════════════════════════════════════════════════════ */
  function fixedVerbalItems() {
    const out = [];
    BANK.verbal.forEach(p => p.q.forEach((st, i) => {
      out.push({
        id: p.id + '.' + (i + 1), kind: 'mc', tag: p.theme,
        passage: p.passage, q: st.s, options: ['True', 'False', 'Cannot say'],
        ans: { 'true': 0, 'false': 1, 'cannot say': 2 }[st.a],
        why: st.w, time: 45, small: true
      });
    }));
    return out;
  }
  const VX_LABEL = { 'true': 'True', 'false': 'False', 'cannot say': 'Cannot say' };

  function buildItems(section, cfg) {
    const n = cfg.count;
    switch (section.id) {
      case 'verbal': return U.shuffle(U.rng(cfg.seed), fixedVerbalItems()).slice(0, n);
      case 'verbalX': {
        const out = [];
        for (let i = 0; i < n; i++) {
          const it = DRILL.verbalItem(cfg.seed * 7919 + i * 104729);
          out.push({
            id: it.id, kind: 'mc', tag: it.theme, passage: it.passage,
            q: it.q.map(x => x.t), options: it.q.map(x => VX_LABEL[x.a]),
            ans: -1, multi: true,
            sub: it.q, why: it.q.map(x => x.w), time: section.perItem
          });
        }
        return out;
      }
      case 'numerical': {
        const all = DRILL.numericalFixed().map(i => Object.assign({ kind: 'mc' }, i));
        return cfg.paper === 'B' ? all.slice(0, 37) : all;
      }
      case 'deductive': return U.shuffle(U.rng(cfg.seed), BANK.DED.map(d => Object.assign({ kind: 'mcfig', why: d.rule, time: section.perItem }, d))).slice(0, n);
      case 'inductive': return DRILL.inductiveSet(n).map(x => Object.assign(x, { kind: 'mcfig' }));
      case 'concentration': return DRILL.concentrationSet(n).map(x => Object.assign(x, { kind: 'pair' }));
      case 'learning': return DRILL.learningSet(n).map(x => Object.assign(x, { kind: 'grid' }));
      case 'memory': return DRILL.memorySet(n).map(x => Object.assign(x, { kind: 'grid' }));
      case 'switch': return DRILL.switchSet(n).map(x => Object.assign(x, { kind: 'switch' }));
      case 'info': return U.shuffle(U.rng(cfg.seed), BANK.info.map(x => ({ id: x.id, kind: 'mc', q: x.q, options: x.opts, ans: x.ans, why: x.why, time: section.perItem }))).slice(0, n);
      case 'mech': return U.shuffle(U.rng(cfg.seed), BANK.mech.map(x => ({ id: x.id, kind: 'mc', q: x.q, options: x.opts, ans: x.ans, why: x.why, scene: x.scene, tag: 'mécanique', time: section.perItem }))).slice(0, n);
      case 'workBehaviour': return U.shuffle(U.rng(cfg.seed), BANK.workBehaviour).slice(0, n)
        .map((s, i) => ({ id: 'WB' + i, kind: 'likert', q: s, scale: BANK.WB_SCALE, time: section.perItem }));
      case 'motivation': return U.shuffle(U.rng(cfg.seed), BANK.motivation).slice(0, n)
        .map((s, i) => ({ id: 'MO' + i, kind: 'likert', q: s, scale: BANK.MOT_SCALE, time: section.perItem }));
      default: return [];
    }
  }

  /** Simulation complète : échantillon de toutes les sections. */
  function buildMixed(cfg) {
    const mix = [
      ['numerical', 12], ['verbalX', 12], ['deductive', 6], ['inductive', 6],
      ['switch', 8], ['concentration', 15], ['learning', 4], ['info', 5], ['mech', 8]
    ];
    let items = [];
    mix.forEach(([sid, k], i) => {
      const sec = byId(sid);
      items = items.concat(buildItems(sec, { count: k, seed: cfg.seed + i * 977, paper: 'A' }));
    });
    return U.shuffle(U.rng(cfg.seed), items);
  }

  /* ═══════════════════════════════════════════════════════════
     STOCKAGE DES CAPTURES (IndexedDB)
     ═══════════════════════════════════════════════════════════ */
  const idb = {
    db: null,
    open() {
      return new Promise((res, rej) => {
        if (this.db) return res(this.db);
        try {
          const rq = indexedDB.open('skemaTrainer', 1);
          rq.onupgradeneeded = () => { const d = rq.result; if (!d.objectStoreNames.contains('shots')) d.createObjectStore('shots', { keyPath: 'id', autoIncrement: true }); };
          rq.onsuccess = () => { this.db = rq.result; res(this.db); };
          rq.onerror = () => rej(rq.error);
        } catch (e) { rej(e); }
      });
    },
    async put(rec) { const db = await this.open(); return new Promise((res, rej) => { const t = db.transaction('shots', 'readwrite'); t.objectStore('shots').add(rec).onsuccess = e => res(e.target.result); t.onerror = () => rej(t.error); }); },
    async all() { try { const db = await this.open(); return new Promise((res) => { const t = db.transaction('shots', 'readonly'); const r = t.objectStore('shots').getAll(); r.onsuccess = () => res(r.result || []); r.onerror = () => res([]); }); } catch (e) { return []; } },
    async del(id) { const db = await this.open(); return new Promise((res) => { const t = db.transaction('shots', 'readwrite'); t.objectStore('shots').delete(id).onsuccess = () => res(true); }); },
    async clear() { const db = await this.open(); return new Promise((res) => { const t = db.transaction('shots', 'readwrite'); t.objectStore('shots').clear().onsuccess = () => res(true); }); }
  };

  /* ═══════════════════════════════════════════════════════════
     PROGRESSION
     ═══════════════════════════════════════════════════════════ */
  /* ═══════════════════════════════════════════════════════════
     PROFILS — chaque utilisateur a son propre historique local
     ═══════════════════════════════════════════════════════════ */
  function normalizeName(n) {
    n = String(n || '').trim().replace(/\s+/g, ' ');
    if (!n) return '';
    return n.split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join(' ');
  }
  const PROFILES = {
    list() { return U.store.get('users', []); },
    current() { return U.store.get('user', null); },
    add(name) { const l = this.list(); if (name && l.indexOf(name) < 0) { l.push(name); U.store.set('users', l); } return name; },
    set(name) { const c = normalizeName(name); this.add(c); U.store.set('user', c); return c; },
    logout() { U.store.del('user'); },
    reset(name) { const l = this.list().filter(x => x !== name); U.store.set('users', l); }
  };

  const dFr = (iso) => iso ? new Date(iso).toLocaleDateString('fr-FR') : '—';
  const hFr = (iso) => iso ? new Date(iso).toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit', second: '2-digit' }) : '—';
  const csvc = (v) => '"' + String(v == null ? '' : v).replace(/"/g, '""').replace(/\s+/g, ' ').trim() + '"';

  const P = {
    profiles: PROFILES,
    key(k) { return k + '::' + (PROFILES.current() || 'Invité'); },

    /* migration de l'ancien format global vers un profil nommé */
    migrate() {
      try {
        const old = U.store.get('attempts', null);
        if (old && old.length) {
          const k = 'attempts::Calvin';
          if (!U.store.get(k, null)) U.store.set(k, old);
          U.store.del('attempts');
          const od = U.store.get('details', null);
          if (od) { if (!U.store.get('details::Calvin', null)) U.store.set('details::Calvin', od); U.store.del('details'); }
        }
      } catch (e) {}
    },

    attempts() { return U.store.get(this.key('attempts'), []); },
    details() { return U.store.get(this.key('details'), {}); },
    settings() {
      return U.store.get('settings', { sound: false, keyboard: true, feedback: 'immediate', showTimer: true,
        target: 50, strict: false, theme: 'light', langUI: 'fr', code: 'CM2026' });
    },
    saveSettings(s) { U.store.set('settings', s); },
    code() { const st = this.settings(); return String(st.code || 'CM2026').trim().toUpperCase(); },

    add(attempt, detail) {
      const a = this.attempts(); a.push(attempt);
      U.store.set(this.key('attempts'), a.slice(-800));
      if (detail && detail.length) {
        const d = this.details(); d[attempt.id] = detail;
        const ids = Object.keys(d);
        if (ids.length > 80) delete d[ids[0]];
        U.store.set(this.key('details'), d);
      }
    },
    clear() { U.store.del(this.key('attempts')); U.store.del(this.key('details')); },

    /* détail question par question d'une session */
    sessionLog(id) { const d = this.details(); return d[id] || []; },
    sessionOf(id) { return this.attempts().find(x => x.id === id) || null; },
    sessions() { return this.attempts().slice().reverse(); },

    /** Export CSV du détail d'une session (question par question). */
    csv(id) {
      const a = this.sessionOf(id) || {};
      const log = this.sessionLog(id);
      const head = ['Profil', 'Session', 'Date', 'Heure', 'Section', 'N°', 'Question', 'Réponse donnée',
        'Réponse correcte', 'Résultat', 'Temps (ms)', 'Explication'];
      const secName = (sid) => (byId(sid) ? byId(sid).name : (sid || ''));
      const rows = log.map((r, i) => [
        PROFILES.current() || '', id, dFr(a.at), hFr(a.at), secName(r.section), (r.n || i + 1),
        csvc(r.q), csvc(r.given), csvc(r.correct),
        r.ok === true ? 'correct' : (r.ok === false ? 'incorrect' : 'sans bonne reponse'),
        r.ms == null ? '' : r.ms, csvc(r.why)
      ]);
      const csv = [head.map(csvc).join(';')].concat(rows.map(r => r.join(';'))).join('\r\n');
      const blob = new Blob(['\ufeff' + csv], { type: 'text/csv;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const lk = document.createElement('a');
      lk.href = url;
      lk.download = 'detail-session-' + id + '-' + (PROFILES.current() || 'profil') + '.csv';
      lk.click();
      U.toast('Détail exporté (CSV)');
    },

    statsFor(id) {
      const all = this.attempts().filter(x => x.section === id);
      const a = all.filter(x => x.accuracy !== null && x.accuracy !== undefined);
      if (!all.length) return null;
      if (!a.length) return { n: all.length, behavioural: true, best: null, last: null, avg: null,
        avgMs: all.reduce((x, y) => x + (y.avgMs || 0), 0) / all.length, trend: 0, total: 0,
        lastAt: all[all.length - 1].at };
      const acc = a.map(x => x.accuracy);
      const best = Math.max(...acc);
      const last = a[a.length - 1];
      return {
        n: a.length, best, last: last.accuracy, lastAt: last.at, avg: acc.reduce((x, y) => x + y, 0) / a.length,
        avgMs: a.reduce((x, y) => x + (y.avgMs || 0), 0) / a.length,
        trend: acc.length >= 4 ? (acc.slice(-2).reduce((x, y) => x + y, 0) / 2 - acc.slice(-4, -2).reduce((x, y) => x + y, 0) / 2) : 0,
        total: a.reduce((x, y) => x + y.correct, 0)
      };
    },
    overall() {
      const a = this.attempts();
      if (!a.length) return { n: 0, correct: 0, items: 0, accuracy: 0, minutes: 0, answered: 0 };
      const items = a.reduce((x, y) => x + y.items, 0), correct = a.reduce((x, y) => x + y.correct, 0);
      return { n: a.length, correct, items, accuracy: items ? correct / items : 0,
        minutes: a.reduce((x, y) => x + (y.ms || 0), 0) / 60000,
        answered: a.reduce((x, y) => x + (y.answered || y.items), 0) };
    },
    days(n = 30) {
      const map = {};
      this.attempts().forEach(a => { const k = a.at.slice(0, 10); map[k] = (map[k] || 0) + a.items; });
      const out = [];
      for (let i = n - 1; i >= 0; i--) { const d = new Date(Date.now() - i * 86400000); const k = d.toISOString().slice(0, 10); out.push({ k, v: map[k] || 0 }); }
      return out;
    },
    streak() {
      const set = new Set(this.attempts().map(a => a.at.slice(0, 10)));
      let n = 0;
      for (let i = 0; i < 400; i++) { const k = new Date(Date.now() - i * 86400000).toISOString().slice(0, 10); if (set.has(k)) n++; else if (i > 0) break; }
      return n;
    },
    bestRun(section) { return Math.max(0, ...this.attempts().filter(a => a.section === section).map(a => a.correct)); },
    wrongs(limit = 30) {
      const d = this.details(), out = [];
      Object.keys(d).sort().reverse().forEach(k => { (d[k] || []).forEach(it => { if (it && it.ok === false) out.push(it); }); });
      return out.slice(0, limit);
    }
  };

  /* alias pratique : CORE.P.PROFILES et CORE.PROFILES pointent la même chose */
  P.PROFILES = PROFILES;

  /* ═══════════════════════════════════════════════════════════
     FEEDBACK ENGINE
     ═══════════════════════════════════════════════════════════ */
  function feedbackReport() {
    const a = P.attempts();
    if (!a.length) return null;
    const st = P.settings();
    const bySec = {};
    a.filter(x => x.accuracy !== null && x.accuracy !== undefined).forEach(x => { (bySec[x.section] = bySec[x.section] || []).push(x); });
    const weakest = Object.keys(bySec).map(k => ({
      id: k, name: (byId(k) || {}).name || k,
      acc: bySec[k].reduce((s, y) => s + y.accuracy, 0) / bySec[k].length,
      n: bySec[k].length
    })).sort((x, y) => x.acc - y.acc);

    const vel = a.filter(x => !x.behavioural).map(x => x.avgMs || 0).filter(x => x > 0);
    const meanVel = vel.length ? vel.reduce((x, y) => x + y, 0) / vel.length : 0;
    const sd = vel.length > 1 ? Math.sqrt(vel.reduce((s, v) => s + Math.pow(v - meanVel, 2), 0) / vel.length) : 0;

    const target = st.target || 50;
    const bestVX = P.bestRun('verbalX');
    const bestNum = P.bestRun('numerical');

    const lines = [];
    lines.push({ t: 'Objectif 50 réponses exactes (batterie anglaise illimitée)', v: bestVX, max: target, hint: bestVX >= target ? 'Objectif atteint : passez en mode 60 items pour verrouiller.' : 'Continuez : cible ' + target + ', meilleur run actuel ' + bestVX + '.' });
    lines.push({ t: 'Numerical : paper 48 items', v: bestNum, max: 48, hint: bestNum >= 40 ? 'Niveau solide — visez 44+' : 'Travaillez la table de données avant la question.' });

    const recos = [];
    if (weakest[0]) recos.push('Section la plus faible : **' + weakest[0].name + '** (' + U.pct(weakest[0].acc) + '). Faites 2 sessions de 10 min avant de passer à autre chose.');
    if (sd > meanVel * 0.6 && meanVel) recos.push('Temps de réponse très irréguliers (écart-type ' + Math.round(sd) + ' ms) : signe d’hésitation. Travaillez le mode **Concentration** et le **Switch Challenge** en série courte.');
    if (bestVX < target) recos.push('Pour atteindre 50 réponses exactes : enchaînez 3 runs de 40 items par jour, en visant ≥ 90 % et ≤ 35 s/item.');
    recos.push('Avant le ' + new Date(DL.exam).toLocaleDateString('fr-FR') + ' : une **simulation complète** par jour, puis révision ciblée des erreurs.');
    if ((P.overall().accuracy || 0) > 0.85) recos.push('Précision globale > 85 % : passez en mode **strict** (chrono par item, pas de feedback immédiat) pour simuler les conditions réelles.');

    return {
      overall: P.overall(), target, bestVX, bestNum, weakest, meanVel: Math.round(meanVel),
      sd: Math.round(sd), lines, recos, wrongs: P.wrongs(24), streak: P.streak()
    };
  }

  /* ═══════════════════════════════════════════════════════════
     MOTEUR DE SESSION
     ═══════════════════════════════════════════════════════════ */
  let S = null;               /* session courante */
  let tick = null;

  function destroy() {
    const hud0 = document.getElementById('hud');
    if (hud0) { hud0.innerHTML = ''; hud0.classList.remove('on'); }
    if (tick) { clearInterval(tick); tick = null; }
    if (S && S.phaseTimer) { clearTimeout(S.phaseTimer); }
    document.removeEventListener('keydown', onKey);
    S = null;
  }

  function onKey(e) {
    if (!S || S.done) return;
    const st = P.settings();
    if (!st.keyboard) return;
    if (S.locked) return;
    if (e.key >= '1' && e.key <= '4') {
      const it = S.items[S.i], idx = parseInt(e.key, 10) - 1;
      if (it.kind === 'likert') { if (idx < it.scale.length) pick(idx); return; }
      if (it.kind === 'pair') { if (idx < 2) pick(idx); return; }
      if (it.kind === 'grid' || it.kind === 'switch') { pick(idx); return; }
      if (it.kind === 'mc') { if (it.multi) toggleMulti(idx); else pick(idx); return; }
      if (it.kind === 'mcfig') { pick(idx); return; }
    }
    if (e.key === 'Enter') { S.pending ? submit() : next(); }
    if (e.key === ' ') { e.preventDefault(); next(); }
  }

  /* — état d'une réponse en cours — */
  let sel = null, multiSel = null, gridSel = null;

  /** Ajoute une ligne au journal de session : n° de question + horodatage exact. */
  function pushLog(entry) {
    entry.n = S.log.length + 1;
    entry.at = new Date().toISOString();
    S.log.push(entry);
  }

  function mount(view, sectionId, cfg) {
    destroy();
    const sec = byId(sectionId) || { id: sectionId, name: 'Simulation complète', icon: '🎯', mode: 'mc', perItem: 60 };
    cfg = Object.assign({ count: sec.items || 20, paper: 'A', timed: true, seed: Date.now() % 100000, mix: false }, cfg || {});
    const st = P.settings();
    const items = cfg.mix ? buildMixed(cfg) : buildItems(sec, cfg);

    const totalQ = items.reduce((a, it) => a + (it.multi ? it.sub.length : (it.sub ? it.sub.length : 1)), 0);
    const stLang = P.settings().lang || {};
    const lang = cfg.lang || stLang[sectionId] ||
      ((sectionId === 'verbal' || sectionId === 'verbalX') ? 'en' : (P.settings().langUI || 'fr'));
    S = {
      sec, cfg, items, i: 0, done: false, locked: false, pending: false, subIndex: 0, totalQ, lang,
      t0: Date.now(), qStart: 0, phase: 'question',
      results: [], times: [], sel: null, log: [], strict: !!cfg.strict,
      feedback: cfg.feedback || st.feedback,
      startedAt: new Date().toISOString()
    };

    writeHUD();
    document.addEventListener('keydown', onKey);
    render();
    return true;
  }

  function writeHUD() {
    const hud = U.$('#hud');
    if (!S) { hud.innerHTML = ''; hud.classList.remove('on'); return; }
    hud.classList.add('on');
    const total = S.totalQ || S.items.length;
    const answered = S.log.filter(r => r.ok !== null).length;
    const good = S.log.filter(r => r.ok === true).length;
    const bad = S.log.filter(r => r.ok === false).length;
    hud.innerHTML =
      '<span class="pill"><span class="k">Section</span>' + U.esc(S.sec.name) + '</span>' +
      '<span class="pill mono"><span class="k">Item</span>' + Math.min(answered + 1, total) + '/' + total + '</span>' +
      '<span class="pill hit mono">✔ ' + good + '</span>' +
      '<span class="pill miss mono">✘ ' + bad + '</span>' +
      '<span class="pill mono"><span class="k">Restant</span>' + (total - answered) + '</span>' +
      (S.feedback === 'immediate' ? '<span class="pill good">mode entraînement</span>' : '<span class="pill warn">mode examen</span>');
  }

  /* ─────────── Rendu principal ─────────── */
  function render() {
    const view = U.$('#view');
    if (!S) return;
    if (S.done) return renderSummary();
    if (S.phase === 'show') return renderShowPhase();
    const it = S.items[S.i];
    sel = null; multiSel = new Set(); gridSel = new Set();

    const pct = (S.i) / S.items.length;
    view.className = 'view';
    view.innerHTML =
      '<div class="runner">' +
      '<div class="row between" style="margin-bottom:10px">' +
        '<div><div class="qlabel">' + S.sec.icon + ' ' + U.esc(S.sec.name) + (S.cfg.paper === 'B' ? ' — Paper B (37)' : '') + '</div>' +
        '<div class="tiny dim" id="phaseMsg"></div></div>' +
        '<div class="row">' +
          '<span class="pill mono" id="qTimer">—</span>' +
          '<button class="btn sm ghost" id="btnSkip">' + T().skip + '</button>' +
          '<button class="btn sm ghost" id="btnQuit">' + T().quit + '</button>' +
        '</div>' +
      '</div>' +
      '<div class="progress" style="margin-bottom:14px"><i style="width:' + (pct * 100).toFixed(1) + '%"></i></div>' +
      '<div class="timerline"><i id="tbar" style="width:100%"></i></div>' +
      '<div id="qbody" class="qbody"></div>' +
      '<div class="row between" id="qfoot" style="margin-top:6px"></div>' +
      '</div>';

    U.$('#btnSkip').onclick = () => submit(true);
    U.$('#btnQuit').onclick = () => { if (confirm('Quitter la session ? Les réponses déjà données sont conservées.')) finish(); };
    renderItem(it);
    startTimer(it);
    writeHUD();
  }

  function renderItem(it) {
    const b = U.$('#qbody'), f = U.$('#qfoot');
    const st = P.settings();
    if (it.kind === 'mc') return renderMC(it, b, f);
    if (it.kind === 'mcfig') return renderMCFig(it, b, f);
    if (it.kind === 'likert') return renderLikert(it, b, f);
    if (it.kind === 'pair') return renderPair(it, b, f);
    if (it.kind === 'grid') return renderGridPhase(it, b, f);
    if (it.kind === 'switch') return renderSwitch(it, b, f);
    b.innerHTML = '<div class="fb ko">Item non pris en charge (kind = ' + U.esc(String(it.kind)) + ')</div>';
  }

  /* — MC classique — */
  function renderMC(it, b, f) {
    let html = '';
    if (it.passage) html += '<div class="qpassage">' + U.esc(it.passage) + '</div>';
    if (it.cols && it.rows) {
      html += '<table class="qtbl"><thead><tr>' + it.cols.map(c => '<th>' + U.esc(c) + '</th>').join('') + '</tr></thead><tbody>' +
        it.rows.map(r => '<tr>' + r.map((c, i) => '<td class="' + (typeof c === 'number' ? 'num' : '') + '">' + U.esc(c) + '</td>').join('') + '</tr>').join('') + '</tbody></table>';
    }
    if (it.scene) html += '<div class="figbox">' + DRILL.mechScene(it.scene) + '</div>';
    html += '<div class="qtext ' + (it.small ? 'sm' : '') + '">' + U.esc(it.q) + '</div>';
    html += '<div class="opts" id="opts">' + it.options.map((o, i) =>
      '<div class="opt" data-i="' + i + '"><span class="mk">✓</span><span>' + U.esc(o) + '</span><span class="keys">' + (i + 1) + '</span></div>').join('') + '</div>';
    b.innerHTML = html;
    f.innerHTML = '<span class="tiny dim">' + (it.tag ? 'Thème : ' + U.esc(it.tag) + ' · ' : '') + T().hint + '</span><button class="btn pri" id="okBtn" disabled>' + T().validate + '</button>';
    U.$$('#opts .opt').forEach(o => o.onclick = () => pick(+o.dataset.i));
    U.$('#okBtn').onclick = () => submit();
  }

  /* — MC figures (déductif / inductif) — */
  function renderMCFig(it, b, f) {
    let html = '';
    if (it.grid) {                       /* matrice déductive */
      const n = it.size || 3;
      html += '<div class="symgrid" style="grid-template-columns:repeat(' + n + ',64px)">' +
        it.grid.map((row, ri) => row.map((cell, ci) =>
          DRILL.dedTile(cell, (it.colors && it.colors[ri] && it.colors[ri][ci]) || 'ink')).join('')).join('') + '</div>';
    } else if (it.series) {              /* série inductive */
      html += '<div class="figrow" style="margin:18px 0 6px">' + it.series.map(k =>
        '<div class="sym">' + U.shape(k, DRILL.COLORMAP[it.color] || '#e6edf3') + '</div>').join('') + '</div>' +
        '<div class="center small dim" style="margin-bottom:8px">Quelle figure complète la série ?</div>';
    }
    html += '<div class="figrow" id="opts">' + it.opts.map((o, i) =>
      '<div class="sym opt" data-i="' + i + '">' + (o.shape ? DRILL.dedTile(o) : U.shape(o, DRILL.COLORMAP[it.color] || '#e6edf3')) + '</div>').join('') + '</div>';
    b.innerHTML = html;
    f.innerHTML = '<span class="tiny dim">' + T().pickFig + '</span><button class="btn pri" id="okBtn" disabled>' + T().validate + '</button>';
    U.$$('#opts .sym').forEach(o => o.onclick = () => pick(+o.dataset.i));
    U.$('#okBtn').onclick = () => submit();
  }

  /* — Likert — */
  function renderLikert(it, b, f) {
    b.innerHTML = '<div class="qtext">' + U.esc(it.q) + '</div>' +
      '<div class="opts" id="opts">' + it.scale.map((o, i) =>
        '<div class="opt" data-i="' + i + '"><span class="mk">✓</span><span>' + U.esc(o) + '</span><span class="keys">' + (i + 1) + '</span></div>').join('') + '</div>';
    f.innerHTML = '<span class="tiny dim">' + T().pickLk + '</span>';
    U.$$('#opts .opt').forEach(o => o.onclick = () => { pick(+o.dataset.i); setTimeout(() => submit(), 130); });
  }

  /* — Paires de concentration — */
  function renderPair(it, b, f) {
    b.innerHTML =
      '<div class="figrow" style="gap:26px">' +
        '<div class="sym" style="width:130px;height:130px">' + U.shape(it.left.kind, DRILL.COLORMAP[it.left.color]) + '</div>' +
        '<div class="sym" style="width:130px;height:130px">' + U.shape(it.right.kind, DRILL.COLORMAP[it.right.color]) + '</div>' +
      '</div>';
    f.innerHTML = '<button class="btn pri" data-v="1" style="flex:1">' + T().same + ' <span class="keys">1</span></button>' +
                  '<button class="btn pri" data-v="0" style="flex:1">' + T().diff + ' <span class="keys">2</span></button>';
    U.$$('#qfoot .btn').forEach(x => x.onclick = () => { pick(+x.dataset.v === 1 ? 0 : 1); submit(); });
  }

  /* — Grilles mémoire / learning — */
  function renderGridPhase(it, b, f) {
    f.innerHTML = '<button class="btn pri" id="okBtn" disabled>Valider</button>';
    U.$('#okBtn').onclick = () => submit();
    b.innerHTML = '<div class="center small dim">…</div>';
    S.phase = 'show';
    renderShowPhase(it);
  }
  function renderShowPhase(it) {
    const view = U.$('#view');
    const it2 = it || S.items[S.i];
    const size = it2.size || 5, color = it2.color || 'grn';
    let html = '<div class="card" style="text-align:center">' +
      '<div class="qtext" style="margin-bottom:4px">' + T().memor + '</div>' +
      '<div class="small dim" id="showCount"></div>' +
      '<div class="gridmem" style="grid-template-columns:repeat(' + size + ',52px)">';
    for (let c = 0; c < size * size; c++) {
      const on = it2.cells.includes(c);
      html += '<div class="gm ' + (on ? (color === 'grn' ? 'blue' : color) + ' spark' : 'blank edge') + '">' + (on ? '●' : '') + '</div>';
    }
    html += '</div><div class="tiny dim">' + (S.lang === 'en' ? 'The cells will disappear — reproduce them from memory.' : 'Les cases vont disparaître — reproduisez-les de mémoire.') + '</div></div>';
    U.$('#qbody').innerHTML = html;
    U.$('#qfoot').innerHTML = '<button class="btn pri" id="okBtn" disabled>Valider</button>';
    U.$('#okBtn').onclick = () => submit();
    const t0 = Date.now();
    S.phaseTimer = setTimeout(endShow, it2.show || 5000);
    if (tick) clearInterval(tick);
    tick = setInterval(() => {
      const left = Math.max(0, (it2.show - (Date.now() - t0)) / 1000);
      const el = U.$('#showCount'); if (el) el.textContent = left.toFixed(1) + ' s';
      if (left <= 0) clearInterval(tick);
    }, 100);
    function endShow() {
      clearInterval(tick);
      S.phase = 'answer'; S.gridStart = Date.now();
      renderAnswerGrid(it2);
    }
  }
  function renderAnswerGrid(it) {
    const size = it.size || 5, k = (it.cells || []).length;
    let html = '<div class="card" style="text-align:center">' +
      '<div class="qtext" style="margin-bottom:4px">' + T().reproduce + ' (' + k + ')</div>' +
      '<div class="small dim" id="gridMsg">' + T().selection + ' : 0 / ' + k + '</div>' +
      '<div class="gridmem" style="grid-template-columns:repeat(' + size + ',52px)">';
    for (let c = 0; c < size * size; c++) html += '<div class="gm blank edge" data-c="' + c + '"></div>';
    html += '</div></div>';
    U.$('#qbody').innerHTML = html;
    U.$('#qfoot').innerHTML = '<span class="tiny dim">' + (S.lang === 'en' ? 'Click the cells, then submit.' : 'Cliquez les cases puis validez.') + '</span><button class="btn pri" id="okBtn">' + T().validate + '</button>';
    gridSel = new Set();
    U.$$('#qbody .gm').forEach(g => g.onclick = () => {
      const c = +g.dataset.c;
      if (gridSel.has(c)) { gridSel.delete(c); g.className = 'gm blank edge'; }
      else {
        if (gridSel.size >= k) { U.toast('Vous ne pouvez sélectionner que ' + k + ' cases', 'warn', 1500); return; }
        gridSel.add(c); g.className = 'gm selected';
      }
      U.$('#gridMsg').textContent = T().selection + ' : ' + gridSel.size + ' / ' + k;
    });
    U.$('#okBtn').onclick = () => submit();
    startTimer(it);
  }

  /* — Switch challenge — */
  function renderSwitch(it, b, f) {
    const tile = (v) => '<div class="dnd-slot filled" style="border-color:' + ['#0a8a3c', '#b58100', '#c62828', '#1565c0'][(v - 1) % 4] + '">' + v + '</div>';
    b.innerHTML =
      '<div class="center small dim">Suite d’entrée</div>' +
      '<div class="dnd-rail">' + it.input.map(tile).join('') + '</div>' +
      '<div class="center small dim" style="margin-top:14px">Suite de sortie</div>' +
      '<div class="dnd-rail">' + it.output.map(tile).join('') + '</div>' +
      '<div class="center small dim" style="margin-top:22px">Quelle combinaison d’échanges produit ce résultat ?</div>' +
      '<div class="dnd-ops" id="opts">' + it.options.map((o, i) =>
        '<button class="dnd-op" data-i="' + i + '">' + U.esc(o.label) + '<small>' + (i + 1) + '</small></button>').join('') + '</div>';
    f.innerHTML = '<span class="tiny dim">' + (S.lang === 'en' ? 'A swap is applied from left to right.' : 'Un échange s’applique de gauche à droite.') + '</span><button class="btn pri" id="okBtn" disabled>' + T().validate + '</button>';
    U.$$('.dnd-op').forEach(o => o.onclick = () => pick(+o.dataset.i));
    U.$('#okBtn').onclick = () => submit();
  }

  /* ─────────── Interaction ─────────── */
  function pick(i) {
    const it = S.items[S.i];
    if (it.kind === 'mcfig') {
      multiSel = new Set([i]);
      U.$$('#opts .sym').forEach(o => o.classList.toggle('sel', +o.dataset.i === i));
    } else if (it.kind === 'switch') {
      multiSel = new Set([i]);
      U.$$('.dnd-op').forEach(o => o.classList.toggle('on', +o.dataset.i === i));
    } else {
      multiSel = new Set([i]);
      U.$$('#opts .opt').forEach(o => o.classList.toggle('sel', +o.dataset.i === i));
    }
    const btn = U.$('#okBtn'); if (btn) btn.disabled = false;
    if (it.kind === 'pair') return;
    if (!S.strict) return;
  }
  function toggleMulti() { /* réservé */ }

  /** Libellé affichable d'une option (gère les options objets du switch). */
  function label(it, idx) {
    if (idx == null) return 'non répondu';
    if (it.options) { const o = it.options[idx]; return (o && typeof o === 'object') ? (o.label || ('Option ' + (idx + 1))) : o; }
    if (it.opts) { const o = it.opts[idx]; return (o && typeof o === 'object') ? ('Figure ' + (idx + 1)) : ('Figure ' + (idx + 1)); }
    return String(idx + 1);
  }
  function ansLabel(it) {
    if (it.options) { const o = it.options[it.ans]; return (o && typeof o === 'object') ? (o.label || ('Option ' + (it.ans + 1))) : o; }
    return 'Figure ' + (it.ans + 1);
  }

  /** Corrige et enregistre la réponse courante. skip=true => passée. */
  function submit(skip) {
    if (S.locked || S.done) return;
    const it = S.items[S.i];
    const dt = Date.now() - (S.qStart || Date.now());
    S.times.push(dt);

    /* — Likert : pas de bonne réponse — */
    if (it.kind === 'likert') {
      const idx = multiSel && multiSel.size ? [...multiSel][0] : null;
      pushLog({ id: it.id, q: it.q, given: idx == null ? 'non répondu' : it.scale[idx], correct: null, ok: null, ms: dt, section: S.sec.id });
      S.results.push({ ok: null });
      next(); return;
    }

    /* — Grille mémorisation — */
    if (it.kind === 'grid') {
      const clicked = gridSel ? [...gridSel] : [];
      const target = it.cells;
      const hit = clicked.filter(c => target.includes(c)).length;
      const ok = hit === target.length && clicked.length === target.length;
      pushLog({ id: it.id, q: 'Grille ' + it.size + '×' + it.size + ' — mémoriser et reproduire ' + target.length + ' cases',
        given: clicked.length + ' cases (' + hit + ' correctes)', correct: target.length + ' cases', ok, ms: dt, section: S.sec.id });
      S.results.push({ ok });
      if (S.feedback === 'immediate') showFeedback(it, ok, dt, ok ? 'Placement exact.' : 'Comparez avec la position des cases vertes.', target.length + ' cases', false);
      else next();
      return;
    }

    /* — Paires de concentration — */
    if (it.kind === 'pair') {
      const idx = multiSel && multiSel.size ? [...multiSel][0] : null;
      const good = it.same ? 0 : 1;
      const ok = idx !== null && idx === good;
      pushLog({ id: it.id, q: 'Deux figures — identiques ou différentes ?',
        given: idx === 0 ? 'identiques' : (idx === 1 ? 'différentes' : 'non répondu'),
        correct: it.same ? 'identiques' : 'différentes', ok, ms: dt, section: S.sec.id });
      S.results.push({ ok });
      if (S.feedback === 'immediate' && !skip) showFeedback(it, ok, dt, it.same ? 'Les deux figures étaient identiques.' : 'Une forme ou une couleur différait.', it.same ? 'Identiques' : 'Différentes', false);
      else next();
      return;
    }

    /* — Batterie verbale illimitée : 3 affirmations par passage — */
    if (it.multi) {
      const idx = multiSel && multiSel.size ? [...multiSel][0] : null;
      const si = S.subIndex || 0;
      const sub = it.sub[si];
      const ansl = VX_LABEL[sub.a];
      const ok = idx !== null && it.options[idx] === ansl;
      pushLog({ id: it.id + '-' + (si + 1), q: sub.t, given: idx == null ? 'non répondu' : it.options[idx], correct: ansl, ok, ms: dt, section: S.sec.id, why: sub.w });
      S.results.push({ ok });
      S.lastSub = si;
      S.subIndex = si + 1;
      if (S.feedback === 'immediate') showFeedback(it, ok, dt, sub.w, ansl, true);
      else next();
      return;
    }

    /* — QCM standard (numérique, information, mécanique, figures) — */
    const idx = multiSel && multiSel.size ? [...multiSel][0] : null;
    const ok = idx !== null && idx === it.ans;
    pushLog({ id: it.id, q: it.q, given: label(it, idx), correct: ansLabel(it), ok, ms: dt, section: S.sec.id, why: it.why, okFlag: ok });
    S.results.push({ ok });
    if (S.feedback === 'immediate') showFeedback(it, ok, dt, it.why, ansLabel(it), false);
    else next();
  }

  function afterAnswer() {}

  function showFeedback(it, ok, dt, why, correctText, isSub) {
    const st = P.settings();
    if (it.kind === 'likert') { next(); return; }
    const b = U.$('#qbody');
    /* marque la réponse */
    if (it.kind === 'mc' || it.kind === 'mcfig') {
      const subAns = it.multi ? it.options.indexOf(VX_LABEL[it.sub[S.lastSub || 0].a]) : it.ans;
      U.$$('#opts .opt, #opts .sym').forEach(o => {
        const i = +o.dataset.i;
        const good = (i === subAns);
        const chosen = multiSel && multiSel.has(i);
        if (good) o.classList.add('ok');
        if (chosen && !good) o.classList.add('ko');
        if (!chosen && !good) o.classList.add('dim');
        o.classList.remove('sel');
      });
    }
    if (it.kind === 'switch') {
      U.$$('.dnd-op').forEach(o => {
        const i = +o.dataset.i;
        if (i === it.ans) o.classList.add('on');
        else if (multiSel && multiSel.has(i)) o.classList.add('ko');
      });
    }
    const whyTxt = Array.isArray(why) ? why.filter(Boolean)[0] : why;
    const txt = it.kind === 'likert' ? '' :
      '<div class="fb ' + (ok ? 'ok' : 'ko') + '" style="margin-top:16px">' +
      '<div class="fb-t">' + (ok ? T().right : T().wrong) + ' <span class="tag">' + U.ms(dt) + '</span>' +
      (correctText && !ok ? ' <span class="tag amb">' + T().answer + ' : ' + U.esc(correctText) + '</span>' : '') + '</div>' +
      (whyTxt ? '<div class="small muted">' + U.esc(whyTxt) + '</div>' : '') + '</div>';
    U.$('#qbody').insertAdjacentHTML('beforeend', txt);
    const moreSub = !!(it.multi && S.subIndex < it.sub.length);
    U.$('#qfoot').innerHTML = '<span class="tiny dim">' + (moreSub ? T().nextSub : T().itemNext) + ' — Entrée / Espace</span>' +
      '<button class="btn pri" id="nextBtn">' + (moreSub ? T().nextSub + ' (' + (S.subIndex + 1) + '/3)' : T().next) + '</button>';
    U.$('#nextBtn').onclick = () => next();
    S.locked = true;
    if (st.sound) U.beep(ok ? 'ok' : 'ko');
    /* le chrono de l'item est arrêté */
    if (tick) { clearInterval(tick); tick = null; }
    writeHUD();
  }

  function next() {
    if (!S) return;
    S.locked = false;
    if (S.items[S.i] && S.items[S.i].multi && (S.subIndex || 0) > 0 && S.subIndex < S.items[S.i].sub.length) {
      /* sous-question suivante du même passage */
      S.qStart = Date.now(); sel = null; multiSel = new Set();
      const it = S.items[S.i];
      const sub = it.sub[S.subIndex];
      U.$('#qbody').innerHTML = '<div class="qpassage">' + U.esc(it.passage) + '</div>' +
        '<div class="qtext sm">' + U.esc(sub.t) + '</div>' +
        '<div class="opts" id="opts">' + it.options.map((o, i) => '<div class="opt" data-i="' + i + '"><span class="mk">✓</span><span>' + U.esc(o) + '</span><span class="keys">' + (i + 1) + '</span></div>').join('') + '</div>';
      U.$$('#opts .opt').forEach(o => o.onclick = () => pick(+o.dataset.i));
      U.$('#qfoot').innerHTML = '<span class="tiny dim">' + T().affirm + ' ' + (S.subIndex + 1) + ' / 3</span><button class="btn pri" id="okBtn" disabled>' + T().validate + '</button>';
      U.$('#okBtn').onclick = () => submit();
      startTimer(it);
      return;
    }
    S.i++;
    S.subIndex = 0; S.lastSub = 0;
    if (S.i >= S.items.length) return finish();
    S.phase = 'question';
    render();
  }

  /* ─────────── Timer ─────────── */
  function startTimer(it) {
    if (tick) clearInterval(tick);
    const st = P.settings();
    S.qStart = Date.now();
    const limit = (it.time || S.sec.perItem) * 1000;
    if (!st.showTimer && S.strict) { U.$('#qTimer').textContent = '—'; }
    tick = setInterval(() => {
      const left = limit - (Date.now() - S.qStart);
      const bar = U.$('#tbar'), q = U.$('#qTimer');
      if (!bar || !q) return;
      const p = Math.max(0, Math.min(1, left / limit));
      bar.style.width = (p * 100) + '%';
      bar.className = p < 0.2 ? 'd' : (p < 0.5 ? 'w' : '');
      q.textContent = (left / 1000).toFixed(1) + ' s';
      q.className = 'pill mono' + (p < 0.2 ? ' danger' : (p < 0.5 ? ' warn' : ''));
      if (left <= 0 && !S.locked) {
        clearInterval(tick);
        if (S.sec.mode === 'pair' || S.sec.mode === 'likert') { if (!multiSel || !multiSel.size) submit(true); }
        else submit(true);
      }
    }, 100);
  }

  /* ─────────── Fin de session + résumé ─────────── */
  function finish() {
    if (!S || S.done) return;
    S.done = true;
    if (tick) { clearInterval(tick); tick = null; }
    const graded = S.log.filter(r => r.ok !== null);
    const correct = graded.filter(r => r.ok === true).length;
    const wrong = graded.filter(r => r.ok === false).length;
    const skipped = Math.max(0, (S.totalQ || S.items.length) - graded.length);
    const scored = graded.length || 1;
    const behavioural = graded.length === 0;
    const attempt = {
      id: 'A' + Date.now(),
      at: new Date().toISOString(),
      endedAt: new Date().toISOString(),
      date: dFr(new Date().toISOString()),
      time: hFr(new Date().toISOString()),
      user: PROFILES.current() || 'Invité',
      section: S.sec.id, sectionName: S.sec.name,
      behavioural,
      items: S.totalQ || S.items.length, answered: graded.length, correct, wrong, skipped,
      accuracy: behavioural ? null : correct / scored,
      avgMs: Math.round((graded.length ? graded : S.log).reduce((s, r) => s + r.ms, 0) / ((graded.length ? graded : S.log).length || 1)),
      ms: Date.now() - S.t0,
      paper: S.cfg.paper || null, mode: S.feedback
    };
    P.add(attempt, S.log.map(r => Object.assign({}, r)));
    renderSummary(attempt);
    writeHUD();
  }

  function renderBehaviourSummary(it) {
    const view = U.$('#view');
    const times = S.log.map(r => r.ms);
    const mean = times.reduce((a, b) => a + b, 0) / (times.length || 1);
    const sd = times.length > 1 ? Math.sqrt(times.reduce((a, t) => a + Math.pow(t - mean, 2), 0) / times.length) : 0;
    const quick = times.filter(t => t < 3000).length;
    const slow = times.filter(t => t > 8000).length;
    const rows = S.log.map(r => '<tr><td>' + U.esc(String(r.q).slice(0, 90)) + '</td><td>' + U.esc(r.given == null ? '—' : r.given) + '</td><td class="num">' + U.ms(r.ms) + '</td></tr>').join('');
    view.innerHTML =
      '<div class="runner">' +
      '<div class="card" style="text-align:center">' +
        '<div class="qlabel">' + (S.sec.icon || '') + ' ' + U.esc(S.sec.name) + ' — terminé</div>' +
        '<div class="scorebig mid" style="font-size:44px">' + times.length + ' réponses</div>' +
        '<div class="muted">Session comportementale : aucune bonne réponse attendue. Le critère est la <b>vitesse de décision</b> et la <b>cohérence</b>.</div>' +
        '<div class="row" style="justify-content:center;margin-top:16px">' +
          '<span class="pill mono">Temps moyen ' + U.ms(mean) + '</span>' +
          '<span class="pill mono">Régularité (σ) ' + Math.round(sd) + ' ms</span>' +
          '<span class="pill ' + (slow === 0 ? 'good' : 'warn') + '">' + quick + ' décisions &lt; 3 s · ' + slow + ' hésitations</span>' +
        '</div>' +
        '<div class="row" style="justify-content:center;margin-top:18px">' +
          '<button class="btn pri" id="againBtn">Refaire</button><button class="btn" id="homeBtn">Accueil</button><button class="btn ghost" id="progBtn">Progression</button>' +
        '</div>' +
      '</div>' +
      '<div class="card sp2"><div class="card-t">Lecture du résultat</div>' +
        '<ul class="ul small">' +
        (slow > times.length * 0.25 ? '<li><b>Hésitations nombreuses</b> : l’école signale que cet inconfort est attendu — choisissez la première réponse qui vous ressemble et avancez.</li>' : '<li>Décisions rapides et régulières : c’est le profil recherché pour ce type de questionnaire.</li>') +
        (sd > mean * 0.7 ? '<li>Temps très irréguliers : certains items vous mettent en difficulté. Repérez-les ci-dessous et fixez-vous une règle de réponse à l’avance.</li>' : '<li>Temps homogènes : votre grille de réponse personnelle est stable.</li>') +
        '<li>Aucune réponse n’est « fausse » : les recruteurs analysent la <b>cohérence interne</b>, pas les valeurs elles-mêmes.</li>' +
        '</ul></div>' +
      '<div class="card sp2"><div class="card-t">Détail des réponses</div><table class="tbl"><thead><tr><th>Affirmation</th><th>Votre choix</th><th class="num">Temps</th></tr></thead><tbody>' + rows + '</tbody></table></div>' +
      '</div>';
    if (U.$('#sumCsv')) U.$('#sumCsv').onclick = () => P.csv(it.id);
    if (U.$('#sumDetail')) U.$('#sumDetail').onclick = () => { location.hash = '#/session/' + it.id; };
    U.$('#againBtn').onclick = () => mount(view, S.sec.id, Object.assign({}, S.cfg, { seed: (S.cfg.seed + 13) % 99991 }));
    U.$('#homeBtn').onclick = () => { location.hash = '#/'; };
    U.$('#progBtn').onclick = () => { location.hash = '#/progression'; };
  }

  /** Tableau « question par question » : n°, question, réponses, résultat, temps, heure, explication. */
  function detailTable(log) {
    if (!log || !log.length) return '<div class="small dim">Aucun détail enregistré pour cette session.</div>';
    const good = log.filter(r => r.ok === true).length, bad = log.filter(r => r.ok === false).length;
    return '<div class="detailwrap"><table class="qtbl2"><thead><tr>' +
      '<th class="qn">N°</th><th class="qx">Question</th><th class="qa">Votre réponse</th><th class="qa">Correcte</th>' +
      '<th>Résultat</th><th>Temps</th><th>Heure</th><th>Explication</th></tr></thead><tbody>' +
      log.map((r, i) =>
        '<tr class="' + (r.ok === true ? 'r-ok' : (r.ok === false ? 'r-ko' : '')) + '">' +
        '<td class="qn">' + (r.n || i + 1) + '</td>' +
        '<td class="qx">' + U.esc(String(r.q || '').slice(0, 220)) + '</td>' +
        '<td class="qa">' + U.esc(r.given == null ? '—' : String(r.given).slice(0, 90)) + '</td>' +
        '<td class="qa">' + (r.correct == null ? '<span class="dim">sans bonne réponse</span>' : '<span class="good">' + U.esc(String(r.correct).slice(0, 90)) + '</span>') + '</td>' +
        '<td>' + (r.ok === true ? '<span class="good">✔ correct</span>' : (r.ok === false ? '<span class="bad">✘ incorrect</span>' : '<span class="dim">—</span>')) + '</td>' +
        '<td class="stamp">' + (r.ms == null ? '—' : U.ms(r.ms)) + '</td>' +
        '<td class="stamp">' + (r.at ? hFr(r.at) : '—') + '</td>' +
        '<td class="why">' + U.esc(String(r.why || '').slice(0, 200)) + '</td>' +
        '</tr>').join('') + '</tbody></table></div>' +
      '<div class="legend-detail"><span><i class="ok"></i> bonne réponse</span><span><i class="ko"></i> erreur</span>' +
      '<span>' + good + ' correctes · ' + bad + ' erreurs · ' + log.length + ' questions</span></div>';
  }

  function renderSummary(attempt) {
    const view = U.$('#view');
    const it = attempt || null;
    if (!it) return;
    if (it.behavioural) return renderBehaviourSummary(it);
    const st = P.settings();
    const acc = it.accuracy;
    const cls = acc >= 0.85 ? 'pass' : (acc >= 0.65 ? 'mid' : 'fail');
    const target = st.target || 50;
    const wrongs = S.log.filter(r => r.ok === false);

    /* ventilation par thème/tag */
    const byTag = {};
    S.log.forEach(r => { const k = (r.section || 'autre'); byTag[k] = byTag[k] || { n: 0, ok: 0 }; byTag[k].n++; if (r.ok) byTag[k].ok++; });

    view.innerHTML =
      '<div class="runner">' +
      '<div class="card" style="text-align:center">' +
        '<div class="qlabel">' + (S.sec.icon || '') + ' ' + U.esc(S.sec.name) + ' — terminé</div>' +
        '<div class="scorebig ' + cls + '">' + Math.round(acc * 100) + '%</div>' +
        '<div class="muted">' + it.correct + ' bonnes réponses sur ' + (it.answered || it.items) + ' · ' + it.wrong + ' erreurs · ' + it.skipped + ' non répondues</div>' +
        '<div class="row" style="justify-content:center;margin-top:16px">' +
          '<span class="pill mono">Temps moyen ' + U.ms(it.avgMs) + '</span>' +
          '<span class="pill mono">Durée ' + U.ms(it.ms) + '</span>' +
          '<span class="pill ' + (it.correct >= target ? 'good' : '') + '">Objectif ≥ ' + target + ' bonnes réponses</span>' +
        '</div>' +
        '<div class="row" style="justify-content:center;margin-top:18px">' +
          '<button class="btn pri" id="againBtn">Refaire</button>' +
          '<button class="btn" id="homeBtn">Accueil</button>' +
          '<button class="btn ghost" id="progBtn">Voir ma progression</button>' +
        '</div>' +
      '</div>' +
      (Object.keys(byTag).length > 1 ?
        '<div class="card sp2"><div class="card-t">Ventilation</div><div class="bars">' +
        Object.keys(byTag).map(k => {
          const v = byTag[k], p = v.ok / v.n;
          return '<div class="bar-row"><span class="bar-name">' + U.esc(k) + '</span>' +
            '<span class="bar-track"><i class="' + (p >= .85 ? '' : p >= .6 ? 'amb' : 'red') + '" style="width:' + (p * 100) + '%"></i></span>' +
            '<span class="bar-val">' + v.ok + '/' + v.n + '</span></div>';
        }).join('') + '</div></div>' : '') +
      '<div class="card sp2">' +
        '<div class="row between" style="margin-bottom:10px">' +
          '<div><div class="card-t" style="margin-bottom:2px">Détail question par question (' + S.log.length + ')</div>' +
          '<span class="small dim">Session du ' + dFr(it.at) + ' à ' + hFr(it.at) + ' · profil ' + U.esc(it.user || '—') + '</span></div>' +
          '<span class="row"><button class="btn sm" id="sumDetail">Vue complète</button>' +
          '<button class="btn sm ghost" id="sumCsv">CSV</button></span>' +
        '</div>' +
        detailTable(S.log) +
      '</div>' +
      '</div>';

    if (U.$('#sumCsv')) U.$('#sumCsv').onclick = () => P.csv(it.id);
    if (U.$('#sumDetail')) U.$('#sumDetail').onclick = () => { location.hash = '#/session/' + it.id; };
    U.$('#againBtn').onclick = () => mount(view, S.sec.id, Object.assign({}, S.cfg, { seed: (S.cfg.seed + 13) % 99991 }));
    U.$('#homeBtn').onclick = () => { location.hash = '#/'; };
    U.$('#progBtn').onclick = () => { location.hash = '#/progression'; };
  }

  /* ═══════════════════════════════════════════════════════════
     CAPTURES — import et stockage des images originales
     ═══════════════════════════════════════════════════════════ */
  async function addShot(file, note) {
    const dataUrl = await new Promise((res, rej) => { const fr = new FileReader(); fr.onload = () => res(fr.result); fr.onerror = rej; fr.readAsDataURL(file); });
    return idb.put({ name: file.name || 'capture', type: file.type || 'image/png', note: note || '', at: new Date().toISOString(), data: dataUrl });
  }

  return { SECTIONS, byId, mount, destroy, P, PROFILES, dFr, hFr, detailTable, feedbackReport, idb, addShot, buildItems, buildMixed, DL,
           get current() { return S; } };
})();
