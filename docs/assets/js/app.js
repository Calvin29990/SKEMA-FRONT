/* ═══════════════════════════════════════════════════════════════
   app.js — Routeur + vues
   Design épuré clair (réplique plateforme d'évaluation CIB).
   Assessment Trainer — Calvin MINANG
   ═══════════════════════════════════════════════════════════════ */
'use strict';

(() => {

  const view = U.$('#view');

  /* ─────────── Icônes (SVG filaires, style plateforme) ─────────── */
  const I = {
    lock: '<svg viewBox="0 0 24 24"><rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>',
    hourglass: '<svg viewBox="0 0 24 24"><path d="M7 3h10M7 21h10M8.5 3v3.2L12 9.8l3.5-3.6V3M8.5 21v-3.2L12 14.2l3.5 3.6V21"/></svg>',
    gear: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.2"/><path d="M12 2.8v3M12 18.2v3M2.8 12h3M18.2 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/></svg>',
    check: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M8 12.4l2.7 2.7L16 9.6"/></svg>',
    clock: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7.2v5l3.3 2"/></svg>',
    expire: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7.2v5l3.3 2"/><path d="M3.4 3.4l17.2 17.2"/></svg>',
    error: '<svg viewBox="0 0 24 24"><path d="M12 3.6l9 15.9H3z"/><path d="M12 9.6v4.1M12 16.6h.01"/></svg>',
    refused: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M6.2 6.2l11.6 11.6M17.8 6.2L6.2 17.8"/></svg>'
  };
  const LEGEND = [
    ['lock', 'Vérrouillée'], ['hourglass', 'Pas encore commencée'], ['gear', 'En progrès'],
    ['check', 'Terminée'], ['expire', 'Expirée'], ['error', 'Erreur'], ['refused', 'Entretien refusé']
  ];

  /* ═══════════════════ ROUTEUR ═══════════════════ */
  function parseHash() {
    const raw = location.hash.replace(/^#\/?/, '');
    const [path, query] = raw.split('?');
    const parts = path.split('/').filter(Boolean);
    const params = {};
    (query || '').split('&').filter(Boolean).forEach(kv => { const [k, v] = kv.split('='); params[decodeURIComponent(k)] = decodeURIComponent(v || ''); });
    return { parts, params };
  }

  function route() {
    CORE.destroy();
    U.$('#hud').innerHTML = '';
    U.$('#hud').classList.remove('on');
    U.$('#mainnav').classList.remove('open');
    const { parts, params } = parseHash();
    const p = parts[0] || '';
    U.$$('.navlink').forEach(a => a.classList.toggle('on', a.getAttribute('href') === '#/' + p || (p === '' && a.getAttribute('href') === '#/')));
    window.scrollTo(0, 0);
    if (p === '') return landing();
    if (p === 'section') return sectionView(parts[1]);
    if (p === 'run') return runView(parts[1], params);
    if (p === 'session') return sessionView(parts[1]);
    if (p === 'progression') return progressionView();
    if (p === 'feedback') return feedbackView();
    if (p === 'captures') return capturesView();
    if (p === 'reglages') return settingsView();
    return landing();
  }
  function routeAndBind() { route(); bindSwitches(); bindLang(); if (typeof I18N !== 'undefined') I18N.apply(view); }

  /* ═══════════════════ LANGUE (FR / EN / ES / PT) ═══════════════════ */
  function setLang(v) {
    I18N.set(v);
    U.$$('[data-lang-sel],#langSel').forEach(el => { el.value = v; });
    U.toast('Langue : ' + I18N.label(v));
  }
  function bindLang() {
    U.$$('[data-lang-sel],#langSel').forEach(el => { el.onchange = () => setLang(el.value); el.value = I18N.current(); });
  }

  /* ═══════════════════ ÉCRAN D'ACCÈS (code + prénom) ═══════════════════ */
  function showLogin() {
    document.documentElement.classList.add('userpending');
    if (U.$('#loginOverlay')) return;
    const known = CORE.PROFILES.list();
    const ov = document.createElement('div');
    ov.id = 'loginOverlay';
    ov.innerHTML =
      '<div class="lg-box">' +
        '<div class="lg-mk">CM</div>' +
        '<h2>Assessment Trainer</h2>' +
        '<p class="sub">Espace d’entraînement personnel.<br>Saisissez le code d’accès puis votre prénom : ' +
          'chaque profil conserve son propre historique, horodaté à la seconde.</p>' +
        '<label for="lgCode">Code d’accès</label>' +
        '<input id="lgCode" type="password" placeholder="••••••" autocomplete="off" spellcheck="false">' +
        '<label for="lgName">Prénom</label>' +
        '<input id="lgName" type="text" placeholder="Calvin" autocomplete="off" spellcheck="false">' +
        '<button class="go" id="lgGo">Accéder</button>' +
        '<div class="lg-err" id="lgErr"></div>' +
        (known.length ? '<div class="lg-sep">Profils enregistrés sur cet appareil</div>' +
          '<div class="lg-users">' + known.map(n => '<button data-name="' + U.esc(n) + '">' + U.esc(n) + '</button>').join('') + '</div>' : '') +
        '<div class="lg-foot">Accès réservé — reproduction et diffusion interdites.<br>' +
          'Données stockées uniquement dans ce navigateur.</div>' +
        '<div class="lg-lang">' + I18N.selectHTML('langsel') + '</div>' +
      '</div>';
    document.body.appendChild(ov);

    const code = U.$('#lgCode'), name = U.$('#lgName'), err = U.$('#lgErr');
    function go(prefill) {
      const c = (code.value || '').trim().toUpperCase();
      const n = (prefill || name.value || '').trim();
      if (c !== CORE.P.code()) { err.textContent = 'Code d’accès incorrect.'; code.focus(); return; }
      if (!n) { err.textContent = 'Indiquez votre prénom.'; name.focus(); return; }
      CORE.PROFILES.set(n);
      CORE.P.migrate();
      ov.remove();
      document.documentElement.classList.remove('userpending');
      paintUser();
      routeAndBind();
      U.toast('Profil « ' + CORE.PROFILES.current() + ' » — historique séparé');
    }
    U.$('#lgGo').onclick = () => go();
    const lgSel = ov.querySelector('[data-lang-sel]');
    if (lgSel) lgSel.onchange = () => { I18N.set(lgSel.value); U.$$('[data-lang-sel],#langSel').forEach(x => { x.value = lgSel.value; }); };
    U.$$('#loginOverlay .lg-users button').forEach(b => b.onclick = () => { name.value = b.dataset.name; go(); });
    ov.addEventListener('keydown', (e) => { if (e.key === 'Enter') go(); });
    setTimeout(() => code.focus(), 80);
  }

  function paintUser() {
    const n = CORE.PROFILES.current();
    const el = U.$('#userName');
    if (el) el.textContent = n || '—';
  }

  function userMenu() {
    const cur = CORE.PROFILES.current() || '';
    const others = CORE.PROFILES.list().filter(x => x !== cur);
    U.modal(
      '<h3 style="margin-bottom:6px">Profil : ' + U.esc(cur) + '</h3>' +
      '<div class="small dim" style="margin-bottom:16px">Chaque profil possède son propre historique (tentatives horodatées, progression, feedback). ' +
        'Pratique si vous prêtez la plateforme : les résultats restent séparés.</div>' +
      '<div class="card-t">Changer de profil</div>' +
      (others.length ? '<div class="row" style="margin-bottom:14px">' + others.map(n => '<button class="btn sm" data-sw="' + U.esc(n) + '">' + U.esc(n) + '</button>').join('') + '</div>'
        : '<div class="small dim" style="margin-bottom:14px">Aucun autre profil enregistré.</div>') +
      '<div class="setrow"><div><div class="t">Nouveau profil</div><div class="d">Entrez un prénom puis validez</div></div>' +
        '<input id="umName" placeholder="Prénom" style="width:150px"></div>' +
      '<div class="setrow"><div><div class="t">Code d’accès du site</div><div class="d">Modifiable — à communiquer aux personnes autorisées</div></div>' +
        '<input id="umCode" value="' + U.esc(CORE.P.code()) + '" style="width:150px;text-transform:uppercase"></div>' +
      '<div class="row end sp2"><button class="btn ghost" id="umOut">Quitter le profil</button>' +
        '<button class="btn pri" id="umSave">Enregistrer</button></div>'
    );
    U.$$('[data-sw]').forEach(b => b.onclick = () => {
      CORE.PROFILES.set(b.dataset.sw); CORE.P.migrate();
      U.closeModal(); paintUser(); routeAndBind();
      U.toast('Profil « ' + CORE.PROFILES.current() + ' »');
    });
    U.$('#umSave').onclick = () => {
      const nm = U.$('#umName').value.trim();
      const cd = U.$('#umCode').value.trim().toUpperCase();
      if (cd) { const st = CORE.P.settings(); st.code = cd; CORE.P.saveSettings(st); }
      if (nm) { CORE.PROFILES.set(nm); CORE.P.migrate(); }
      U.closeModal(); paintUser(); routeAndBind();
      U.toast('Profil « ' + CORE.PROFILES.current() + ' » enregistré');
    };
    U.$('#umOut').onclick = () => { CORE.PROFILES.logout(); U.closeModal(); showLogin(); };
  }

  /* ═══════════════════ ACCUEIL — tableau des tâches ═══════════════════ */
  function landing() {
    const o = CORE.P.overall();
    const st = CORE.P.settings();
    const days = U.daysBetween(new Date().toISOString().slice(0, 10), CORE.DL.exam);
    const target = st.target || 50;
    const bestVX = CORE.P.bestRun('verbalX');
    const plan = CORE.SECTIONS;
    const totalMin = plan.reduce((a, s) => a + (s.dur || 0), 0);
    const doneMin = plan.reduce((a, s) => a + (s.dur || 0) * sectionProgress(s.id), 0);
    const SEG = 20, filled = Math.round(SEG * (totalMin ? doneMin / totalMin : 0));

    view.className = 'view';
    view.innerHTML =
      '<div class="pagecard">' +
        '<h1>Bienvenue dans votre entraînement</h1>' +
        '<p class="intro">Vous trouverez ci-dessous la liste des tâches d’entraînement. Vous devez accomplir toutes ces tâches avant le test. ' +
          'Veillez à vous assurer que vous êtes dans un environnement confortable, où vous pouvez vous concentrer sans être interrompu(e). ' +
          'Avant de commencer chaque exercice, vous pouvez sélectionner la langue des consignes qui vous convient le mieux. ' +
          'Les banques de questions marquées <b>∞</b> sont illimitées (style et règles identiques) ; les autres reprennent un contenu figé, identique à chaque session.</p>' +

        '<div class="taskhead">' +
          '<h2>Tâches à accomplir</h2>' +
          '<div class="progwrap">' +
            '<div class="plabel">Progression de l’entraînement</div>' +
            '<div class="pcount">' + Math.round(doneMin) + ' / ' + totalMin + ' minute(s)</div>' +
            '<div class="progbar" title="Progression du plan : chaque section compte pour 3 sessions réussies (≥ 85 %)">' +
              Array.from({ length: SEG }, (_, i) => '<i class="' + (i < filled ? 'f' : '') + '"></i>').join('') +
            '</div>' +
          '</div>' +
        '</div>' +

        '<div class="tasktable">' + plan.map(taskRow).join('') + simRow() + '</div>' +

        '<div class="legend">' + LEGEND.map(([k, l]) =>
          '<div class="li">' + I[k] + '<span>' + l + '</span></div>').join('') + '</div>' +
      '</div>' +

      '<div class="summarystrip">' +
        stat('Sessions', o.n, formatMinutes(o.minutes) + ' de travail cumulé') +
        stat('Précision globale', U.pct(o.accuracy), o.correct + ' / ' + o.items + ' bonnes réponses') +
        stat('Série en cours', CORE.P.streak() + ' j', 'Objectif : une session par jour') +
        stat('Cible « 50 réponses »', bestVX + ' / ' + target, bestVX >= target ? 'Objectif atteint ✔' : 'Batterie anglaise illimitée') +
      '</div>' +

      '<p class="tiny dim sp">Prochaine échéance : ' +
        (days > 0 ? 'J−' + days : (days === 0 ? 'aujourd’hui' : 'fenêtre en cours')) +
        ' · une seule tentative autorisée. <a href="#/progression" style="color:var(--grn)">Voir ma progression détaillée →</a></p>';

    /* — interactions — */
    U.$$('.trow').forEach(r => {
      const id = r.dataset.id;
      const start = r.querySelector('.tstart');
      if (start) start.onclick = (e) => { e.stopPropagation(); startRun(id === '_mix' ? 'mixed' : id, id === '_mix' ? { mix: '1', strict: '1', mode: 'end' } : {}); };
      r.querySelector('.tchev').onclick = (e) => { e.stopPropagation(); r.classList.toggle('open'); };
      const sel = r.querySelector('.tlang');
      if (sel) sel.onchange = () => setLang(sel.value);
    });
  }

  function sectionProgress(id) {
    const st = CORE.P.statsFor(id);
    if (!st || st.best == null) return 0;
    if (st.best < 0.85) return Math.min(0.4, st.n * 0.1);
    return Math.min(1, st.n / 3);
  }

  function taskRow(s) {
    const st = CORE.P.statsFor(s.id);
    const state = !st ? 'none' : (st.best != null && st.best >= 0.85 ? 'done' : 'prog');
    const icon = state === 'done' ? I.check : (state === 'prog' ? I.gear : I.hourglass);
    const cls = state === 'done' ? 'st-done' : (state === 'prog' ? 'st-prog' : '');
    const lg = I18N.current();
    return '' +
      '<div class="trow ' + cls + '" data-id="' + s.id + '">' +
        '<span class="tico">' + icon + '</span>' +
        '<span class="tname"><span>' + U.esc(s.name) + (s.source === 'infinite' ? ' ∞' : '') + '</span>' +
          '<span class="tchev" title="Détails">▼</span></span>' +
        '<span class="tdur">' + I.clock + '~ ' + s.dur + ' minute(s)</span>' +
        I18N.selectHTML('tlang') +
        '<button class="tstart">Début</button>' +
      '</div>' +
      '<div class="tdetails">' +
        '<div class="d">' + U.esc(s.desc) + '</div>' +
        '<div class="hint"><b>Méthode :</b> ' + U.esc(s.hint) + '</div>' +
        '<div class="stats"><span class="tag">' + s.items + ' items disponibles</span><span class="tag">' + s.perItem + ' s / item</span>' +
          (s.source === 'infinite' ? '<span class="tag amb">banque illimitée</span>' : '<span class="tag">banque figée</span>') +
          (st ? '<span class="tag blu">' + st.n + ' session(s)</span><span class="tag ' + (st.best >= .85 ? 'grn' : 'amb') + '">meilleur ' + U.pct(st.best) + '</span>' : '<span class="tag">jamais faite</span>') +
        '</div>' +
      '</div>';
  }

  function simRow() {
    const st = CORE.P.statsFor('mixed');
    const done = st && st.best != null && st.best >= 0.8;
    return '' +
      '<div class="trow ' + (done ? 'st-done' : '') + '" data-id="_mix">' +
        '<span class="tico">' + (done ? I.check : I.gear) + '</span>' +
        '<span class="tname"><span>Simulation complète — conditions d’examen</span><span class="tchev" title="Détails">▼</span></span>' +
        '<span class="tdur">' + I.clock + '~ 49 minute(s)</span>' +
        I18N.selectHTML('tlang') +
        '<button class="tstart">Début</button>' +
      '</div>' +
      '<div class="tdetails">' +
        '<div class="d">Enchaînement des principales épreuves (numérique, verbal, déductif, inductif, switch, concentration, mécanique) avec chrono par item et correction en fin de session.</div>' +
        '<div class="hint"><b>Méthode :</b> à lancer lorsque chaque section est déjà réussie à ≥ 85 %. Aucun retour en arrière, aucune pause.</div>' +
        '<div class="stats"><span class="tag">~136 questions</span><span class="tag amb">mode examen</span>' +
          (st ? '<span class="tag blu">' + st.n + ' session(s)</span>' : '<span class="tag">jamais faite</span>') + '</div>' +
      '</div>';
  }

  const stat = (k, v, s) => '<div class="stat"><div class="k">' + k + '</div><div class="v">' + v + '</div><div class="s">' + s + '</div></div>';
  const formatMinutes = (m) => m >= 60 ? Math.floor(m / 60) + ' h ' + String(Math.round(m % 60)).padStart(2, '0') : Math.round(m) + ' min';

  /* ═══════════════════ FICHE SECTION ═══════════════════ */
  function sectionView(id) {
    const s = CORE.byId(id);
    if (!s) return landing();
    const st = CORE.P.statsFor(id);
    const isNum = id === 'numerical';
    view.className = 'view';
    view.innerHTML =
      '<a class="btn sm ghost" href="#/">&larr; Retour aux tâches</a>' +
      '<div class="pagecard sp">' +
        '<h1>' + U.esc(s.name) + ' <span class="tiny dim">' + U.esc(s.fr) + '</span></h1>' +
        '<p class="intro">' + U.esc(s.desc) + '<br><b>Méthode :</b> ' + U.esc(s.hint) + '</p>' +
        '<div class="row" style="margin-bottom:18px">' +
          '<span class="tag">' + s.items + ' items disponibles</span>' +
          '<span class="tag">' + s.perItem + ' s par item</span>' +
          '<span class="tag">~ ' + s.dur + ' min</span>' +
          (st ? '<span class="tag blu">' + st.n + ' session(s)</span><span class="tag ' + (st.best >= .85 ? 'grn' : 'amb') + '">meilleur ' + U.pct(st.best) + '</span>' +
                '<span class="tag">temps moyen ' + U.ms(st.avgMs) + '</span>' : '<span class="tag">jamais faite</span>') +
        '</div>' +
        '<div class="hr"></div>' +
        '<div class="grid g2">' +
          '<div><div class="card-t">Configuration</div>' +
            (isNum
              ? '<div class="setrow"><div><div class="t">Nombre de questions</div><div class="d">Imposé par le paper (37 ou 48) — contenu figé, identique à chaque session</div></div><span class="tag amb">Figé</span></div>'
              : '<div class="setrow"><div><div class="t">Nombre d’items</div><div class="d">Banque disponible : ' + s.items + ' items</div></div>' +
                '<input id="cfgCount" type="number" min="4" max="' + Math.max(s.items, 120) + '" value="' + s.items + '" style="width:88px"></div>') +
            (isNum ? '<div class="setrow"><div><div class="t">Paper</div><div class="d">A = 48 items (complet) · B = 37 items (extrait)</div></div>' +
              '<select id="cfgPaper"><option value="A">Paper A — 48</option><option value="B">Paper B — 37</option></select></div>' : '') +
            '<div class="setrow"><div><div class="t">Feedback</div><div class="d">Immédiat = entraînement · Fin de session = conditions d’examen</div></div>' +
              '<select id="cfgFb"><option value="immediate">Immédiat</option><option value="end">Fin de session</option></select></div>' +
            '<div class="setrow"><div><div class="t">Mode strict</div><div class="d">Chrono par item obligatoire, pas de retour en arrière</div></div>' +
              '<div class="switch" id="cfgStrict"><i></i></div></div>' +
            '<div class="row end sp"><button class="btn pri lg" id="startBtn">Début</button></div>' +
          '</div>' +
          '<div><div class="card-t">Consignes officielles (rappel)</div>' +
            '<ul class="ul small">' +
              '<li>Un item = un seul passage ou un seul tableau : ne restez pas bloqué.</li>' +
              '<li>Répondez à toutes les questions : une absence de réponse compte comme une erreur.</li>' +
              '<li>Le chronomètre est global sur certains tests : gardez ~1 min de marge.</li>' +
              '<li>Aucun brouillon papier pendant les tests en ligne surveillés.</li>' +
            '</ul>' +
          '</div>' +
        '</div>' +
      '</div>';

    let strict = s.mode === 'pair' || s.mode === 'likert';
    const swS = U.$('#cfgStrict');
    swS.classList.toggle('on', strict);
    swS.onclick = () => { strict = !strict; swS.classList.toggle('on', strict); };
    U.$('#startBtn').onclick = () => {
      const cfg = { count: isNum ? s.items : Math.max(1, Math.min(200, +U.$('#cfgCount').value || s.items)), strict: strict ? '1' : '0', mode: U.$('#cfgFb').value };
      if (isNum) cfg.paper = U.$('#cfgPaper').value;
      startRun(id, cfg);
    };
  }

  function startRun(sectionId, cfg) {
    const q = Object.keys(cfg).map(k => k + '=' + encodeURIComponent(cfg[k])).join('&');
    location.hash = '#/run/' + sectionId + (q ? '?' + q : '');
  }

  /* ═══════════════════ SESSION ═══════════════════ */
  function runView(id, params) {
    view.className = 'view';
    const cfg = {
      count: params.count ? +params.count : undefined,
      paper: params.paper || 'A',
      strict: params.strict === '1',
      feedback: params.mode || CORE.P.settings().feedback,
      seed: Date.now() % 99991,
      mix: params.mix === '1'
    };
    CORE.mount(view, id, cfg);
  }

  /* ═══════════════════ DÉTAIL D'UNE SESSION (question par question) ═══════════════════ */
  const detailTable = (log) => CORE.detailTable(log);

  function sessionView(id) {
    const a = CORE.P.sessionOf(id);
    const log = CORE.P.sessionLog(id);
    view.className = 'view';
    if (!a) {
      view.innerHTML = '<div class="pagecard"><h1>Session introuvable</h1>' +
        '<p class="intro">Le détail de cette session n’est plus conservé (les 80 dernières sessions sont gardées).</p>' +
        '<button class="btn pri" onclick="location.hash=\'#/feedback\'">Retour au feedback</button></div>';
      return;
    }
    const pct = a.behavioural ? null : Math.round((a.accuracy || 0) * 100);
    view.innerHTML =
      '<a class="btn sm ghost" href="#/feedback">&larr; Feedback</a>' +
      '<div class="pagecard sp">' +
        '<h1>' + U.esc(a.sectionName || a.section) + ' <span class="tiny dim">détail question par question</span></h1>' +
        '<div class="row" style="margin:14px 0 6px">' +
          '<span class="tag blu">👤 ' + U.esc(a.user || '—') + '</span>' +
          '<span class="tag">📅 ' + CORE.dFr(a.at) + '</span>' +
          '<span class="tag">🕒 ' + CORE.hFr(a.at) + '</span>' +
          '<span class="tag">' + a.correct + ' / ' + a.answered + ' correctes</span>' +
          (pct == null ? '<span class="tag">questionnaire — pas de bonne réponse</span>' : '<span class="tag ' + (pct >= 85 ? 'grn' : pct >= 65 ? 'amb' : 'red') + '">' + pct + ' %</span>') +
          '<span class="tag mono">temps moyen ' + U.ms(a.avgMs) + '</span>' +
          '<span class="tag mono">durée ' + U.ms(a.ms) + '</span>' +
          (a.paper ? '<span class="tag">Paper ' + a.paper + '</span>' : '') +
        '</div>' +
        '<div class="row" style="margin:14px 0 4px">' +
          '<button class="btn pri sm" id="csvBtn">Télécharger le détail (CSV)</button>' +
          '<button class="btn sm" id="againBtn">Refaire cette section</button>' +
          '<button class="btn sm ghost" id="printBtn">Imprimer / PDF</button>' +
        '</div>' +
        '<div class="hr"></div>' +
        detailTable(log) +
      '</div>';
    U.$('#csvBtn').onclick = () => CORE.P.csv(id);
    U.$('#againBtn').onclick = () => startRun(a.section, a.paper ? { paper: a.paper } : {});
    U.$('#printBtn').onclick = () => window.print();
  }

  /* ═══════════════════ PROGRESSION ═══════════════════ */
  function progressionView() {
    const o = CORE.P.overall();
    const attempts = CORE.P.attempts().slice().reverse();
    const days = CORE.P.days(30);
    const max = Math.max(1, ...days.map(d => d.v));
    const st = CORE.P.settings();
    const target = st.target || 50;
    const bestVX = CORE.P.bestRun('verbalX');
    const bestNum = CORE.P.bestRun('numerical');
    const runsVX = CORE.P.attempts().filter(a => a.section === 'verbalX').length;

    view.className = 'view';
    view.innerHTML =
      '<div class="pagecard">' +
      '<h1>Progression</h1><p class="intro" style="margin-bottom:18px">Profil <b>' + U.esc(CORE.PROFILES.current() || '—') + '</b> — suivi local, horodaté au jour et à l’heure, aucune donnée envoyée. ' +
        'Chaque tentative est conservée avec le détail de ses questions.</p>' +
      '<div class="summarystrip" style="margin:0 0 22px">' +
        stat('Sessions', o.n, 'depuis le début') +
        stat('Précision globale', U.pct(o.accuracy), o.correct + ' / ' + o.items) +
        stat('Temps cumulé', formatMinutes(o.minutes), 'de travail') +
        stat('Contenus à revoir', CORE.P.wrongs(999).length, 'erreurs enregistrées') +
      '</div>' +

      '<div class="card sp"><div class="card-t">Objectifs imposés</div>' +
        '<div class="bars">' +
          objRow('Batterie anglaise ∞ — meilleur run', bestVX, target) +
          objRow('Numerical — meilleur run (paper A)', bestNum, 48) +
          objRow('Runs anglais réalisés', runsVX, 12) +
        '</div>' +
        '<div class="small dim sp">' + (bestVX >= target ? '✅ Objectif « 50 réponses exactes » atteint — verrouillez-le en mode strict.' : '🎯 Il reste ' + (target - bestVX) + ' bonnes réponses à gagner sur la batterie anglaise.') + '</div>' +
      '</div>' +

      '<div class="card sp"><div class="card-t">Par section</div>' +
      (attempts.length ? '<table class="tbl"><thead><tr><th>Section</th><th class="num">Sessions</th><th class="num">Dernier</th><th class="num">Meilleur</th><th class="num">Moyenne</th><th class="num">Temps/item</th><th class="num">Tendance</th></tr></thead><tbody>' +
        CORE.SECTIONS.map(s => {
          const x = CORE.P.statsFor(s.id);
          if (!x) return '<tr><td>' + U.esc(s.name) + '</td><td class="num">—</td><td class="num">—</td><td class="num">—</td><td class="num">—</td><td class="num">—</td><td class="num">—</td></tr>';
          if (x.behavioural) return '<tr><td>' + U.esc(s.name) + '</td><td class="num">' + x.n + '</td><td class="num">—</td><td class="num">—</td><td class="num">—</td><td class="num">' + U.ms(x.avgMs) + '</td><td class="num">questionnaire</td></tr>';
          const tr = x.trend > 0.02 ? '<span class="tag grn">▲</span>' : x.trend < -0.02 ? '<span class="tag red">▼</span>' : '<span class="tag">＝</span>';
          return '<tr><td>' + U.esc(s.name) + '</td><td class="num">' + x.n + '</td><td class="num">' + U.pct(x.last) + '</td><td class="num">' + U.pct(x.best) + '</td><td class="num">' + U.pct(x.avg) + '</td><td class="num">' + U.ms(x.avgMs) + '</td><td class="num">' + tr + '</td></tr>';
        }).join('') + '</tbody></table>' : '<div class="small dim">Aucune session enregistrée.</div>') +
      '</div>' +

      '<div class="card sp"><div class="card-t">Activité (30 derniers jours)</div>' +
        '<div class="heat">' + days.map(d => {
          const l = d.v === 0 ? '' : d.v < max * 0.25 ? 'l1' : d.v < max * 0.5 ? 'l2' : d.v < max * 0.8 ? 'l3' : 'l4';
          return '<i class="' + l + '" title="' + d.k + ' : ' + d.v + ' items"></i>';
        }).join('') + '</div>' +
        '<div class="small dim sp">' + days.reduce((s, d) => s + d.v, 0) + ' items sur 30 jours · série actuelle : ' + CORE.P.streak() + ' jour(s)</div>' +
      '</div>' +

      '<div class="card sp"><div class="card-t">Dernières sessions</div>' +
      (attempts.length ? attempts.slice(0, 25).map(a =>
        '<div class="row between" style="padding:9px 0;border-bottom:1px solid var(--line)">' +
          '<div><b>' + U.esc(a.sectionName || a.section) + '</b> <span class="tag">' + CORE.dFr(a.at) + ' · ' + CORE.hFr(a.at) + '</span>' +
          (a.paper ? ' <span class="tag blu">Paper ' + a.paper + '</span>' : '') +
          ' <button class="btn sm ghost" data-det="' + a.id + '">détail</button></div>' +
          '<div class="row">' + (a.behavioural ? '<span class="tag">questionnaire — ' + a.items + ' réponses</span>' :
            '<span class="tag mono">' + a.correct + '/' + a.answered + '</span>' +
            '<span class="tag ' + (a.accuracy >= .85 ? 'grn' : a.accuracy >= .65 ? 'amb' : 'red') + '">' + U.pct(a.accuracy) + '</span>') +
          '<span class="tag mono">' + U.ms(a.avgMs) + '/item</span></div>' +
        '</div>').join('') : '<div class="small dim">Aucune session.</div>') +
      '</div>' +

      '<div class="row sp2"><button class="btn" id="expBtn">Exporter mes données (JSON)</button>' +
      '<button class="btn ghost" id="printBtn">Imprimer / PDF</button>' +
      '<button class="btn danger" id="clrBtn">Effacer tout l’historique</button></div>' +
      '</div>';

    U.$$('[data-det]').forEach(b => b.onclick = () => { location.hash = '#/session/' + b.dataset.det; });
    U.$('#expBtn').onclick = () => exportData();
    U.$('#printBtn').onclick = () => window.print();
    U.$('#clrBtn').onclick = () => { if (confirm('Effacer définitivement tout l’historique ?')) { CORE.P.clear(); U.toast('Historique effacé'); routeAndBind(); } };
  }

  function kpi(t, v) { return '<div class="stat"><div class="k">' + t + '</div><div class="v">' + v + '</div></div>'; }
  function objRow(t, v, max) {
    const p = Math.max(0, Math.min(1, v / max));
    return '<div class="bar-row"><span class="bar-name">' + t + '</span>' +
      '<span class="bar-track" style="flex:3"><i class="' + (p >= 1 ? '' : p >= .6 ? 'amb' : 'red') + '" style="width:' + (p * 100) + '%"></i></span>' +
      '<span class="bar-val">' + v + '/' + max + '</span></div>';
  }

  /* ═══════════════════ FEEDBACK ═══════════════════ */
  function feedbackView() {
    const r = CORE.feedbackReport();
    view.className = 'view';
    if (!r) {
      view.innerHTML = '<div class="pagecard"><h1>Feedback</h1>' +
        '<p class="intro">Aucune session pour le moment. Le rapport se construit automatiquement dès la première session terminée.</p>' +
        '<div class="row"><button class="btn pri" onclick="location.hash=\'#/\'">Choisir une tâche</button></div></div>';
      return;
    }
    const st = CORE.P.settings();
    view.innerHTML =
      '<div class="pagecard">' +
      '<h1>Feedback automatique</h1>' +
      '<p class="intro" style="margin-bottom:18px">Analyse de vos ' + r.overall.n + ' sessions (' + r.overall.items + ' items, ' + U.pct(r.overall.accuracy) + ' de précision).</p>' +
      '<div class="summarystrip" style="margin:0 0 22px">' +
        stat('Précision', U.pct(r.overall.accuracy), r.overall.correct + ' / ' + r.overall.items) +
        stat('Temps moyen / item', U.ms(r.meanVel), 'régularité σ = ' + r.sd + ' ms') +
        stat('Série', r.streak + ' j', 'jours consécutifs') +
        stat('Erreurs enregistrées', r.wrongs.length, 'à revoir ci-dessous') +
      '</div>' +

      '<div class="card"><div class="card-t">Objectifs</div><div class="bars">' +
        r.lines.map(l => objRow(l.t, l.v, l.max)).join('') + '</div>' +
        '<ul class="ul small sp">' + r.lines.map(l => '<li>' + l.hint + '</li>').join('') + '</ul>' +
      '</div>' +

      '<div class="card sp"><div class="card-t">Sections les plus fragiles</div>' +
        (r.weakest.length ? '<div class="bars">' + r.weakest.slice(0, 6).map(w =>
          '<div class="bar-row"><span class="bar-name">' + U.esc(w.name) + '</span>' +
          '<span class="bar-track"><i class="' + (w.acc >= .85 ? '' : w.acc >= .6 ? 'amb' : 'red') + '" style="width:' + (w.acc * 100) + '%"></i></span>' +
          '<span class="bar-val">' + U.pct(w.acc) + '</span></div>').join('') + '</div>' +
        '<div class="small dim sp">Priorité de travail : <b>' + U.esc(r.weakest[0].name) + '</b>.</div>'
        : '<div class="small dim">Aucune session notée pour l’instant.</div>') +
      '</div>' +

      '<div class="card sp"><div class="card-t">Plan d’action</div><ul class="ul num">' +
        r.recos.map(x => '<li>' + mdBold(x) + '</li>').join('') + '</ul></div>' +

      '<div class="card sp"><div class="card-t">Historique détaillé par session (' + CORE.P.sessions().length + ')</div>' +
        '<div class="small dim" style="margin-bottom:10px">Chaque tentative est enregistrée au jour et à l’heure exacte, avec le détail de chaque question. Cliquez sur « Détail » pour tout revoir.</div>' +
        (CORE.P.sessions().length ? CORE.P.sessions().slice(0, 40).map(a =>
          '<div class="sessrow">' +
            '<span class="st">' + CORE.dFr(a.at) + ' · ' + CORE.hFr(a.at) + '</span>' +
            '<span><span class="sn">' + U.esc(a.sectionName || a.section) + '</span>' +
            '<span class="ss"> · ' + U.esc(a.user || '') + ' · ' + a.correct + ' / ' + a.answered + ' · ' + U.ms(a.avgMs) + '/item</span></span>' +
            (a.behavioural ? '<span class="tag">questionnaire</span>'
              : '<span class="tag ' + (a.accuracy >= .85 ? 'grn' : a.accuracy >= .65 ? 'amb' : 'red') + '">' + U.pct(a.accuracy) + '</span>') +
            '<span class="row"><button class="btn sm" data-det="' + a.id + '">Détail</button>' +
            '<button class="btn sm ghost" data-csv="' + a.id + '">CSV</button></span>' +
          '</div>').join('') : '<div class="small dim">Aucune session.</div>') +
      '</div>' +

      '<div class="card sp"><div class="card-t">Journal des erreurs (' + r.wrongs.length + ')</div>' +
        (r.wrongs.length ? r.wrongs.map(w =>
          '<div class="fb ko"><div class="fb-t">' + U.esc(String(w.q || '').slice(0, 160)) + '</div>' +
          '<div class="small">Votre réponse : <b>' + U.esc(w.given == null ? '—' : String(w.given)) + '</b>' +
          (w.correct != null ? ' · Attendue : <b>' + U.esc(String(w.correct)) + '</b>' : '') +
          ' <span class="tag">' + U.esc(CORE.byId(w.section) ? CORE.byId(w.section).name : (w.section || '')) + '</span> <span class="tag mono">' + U.ms(w.ms) + '</span></div>' +
          (w.why ? '<div class="small dim" style="margin-top:4px">' + U.esc(w.why) + '</div>' : '') + '</div>').join('')
          : '<div class="small dim">Aucune erreur enregistrée. Passez en mode strict ou augmentez le nombre d’items.</div>') +
      '</div>' +

      '<div class="card sp"><div class="card-t">Réglages rapides</div>' +
        '<div class="setrow"><div><div class="t">Mode de feedback par défaut</div><div class="d">Immédiat (entraînement) ou fin de session (examen)</div></div>' +
        '<select id="fbMode"><option value="immediate"' + (st.feedback === 'immediate' ? ' selected' : '') + '>Immédiat</option><option value="end"' + (st.feedback === 'end' ? ' selected' : '') + '>Fin de session</option></select></div>' +
        '<div class="setrow"><div><div class="t">Objectif de bonnes réponses (batterie ∞)</div><div class="d">Valeur annoncée par l’école : 50 minimum</div></div>' +
        '<input id="fbTarget" type="number" min="10" max="200" value="' + (st.target || 50) + '" style="width:88px"></div>' +
      '</div>' +
      '<div class="row sp2"><button class="btn" id="printBtn2">Imprimer / PDF</button><button class="btn ghost" id="homeBtn2">Retour aux tâches</button></div>' +
      '</div>';

    U.$('#fbMode').onchange = (e) => { const s = CORE.P.settings(); s.feedback = e.target.value; CORE.P.saveSettings(s); U.toast('Réglage enregistré'); };
    U.$('#fbTarget').onchange = (e) => { const s = CORE.P.settings(); s.target = Math.max(1, +e.target.value || 50); CORE.P.saveSettings(s); U.toast('Objectif : ' + s.target); };
    U.$$('[data-det]').forEach(b => b.onclick = () => { location.hash = '#/session/' + b.dataset.det; });
    U.$$('[data-csv]').forEach(b => b.onclick = () => CORE.P.csv(b.dataset.csv));
    U.$('#printBtn2').onclick = () => window.print();
    U.$('#homeBtn2').onclick = () => location.hash = '#/';
  }
  const mdBold = (s) => U.esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');

  /* ═══════════════════ CAPTURES ═══════════════════ */
  async function capturesView() {
    view.className = 'view';
    const shots = await CORE.idb.all();
    view.innerHTML =
      '<div class="pagecard">' +
      '<h1>Captures originales</h1>' +
      '<p class="intro" style="margin-bottom:18px">Importez ici vos captures d’écran de référence. ' +
        'Les images sont conservées <b>telles quelles</b> (aucun recadrage, aucune modification) et stockées uniquement dans ce navigateur.</p>' +
      '<div class="dropzone" id="dz">' +
        '<div style="font-size:30px">🖼️</div>' +
        '<div style="font-weight:600;margin-top:8px">Glissez vos captures ici</div>' +
        '<div class="small dim">ou cliquez pour choisir des fichiers · Ctrl+V fonctionne aussi</div>' +
      '</div>' +
      '<input type="file" id="fileIn" accept="image/*" multiple hidden>' +
      '<div class="row between sp2" style="align-items:flex-end">' +
        '<div><h2 style="margin:0">Bibliothèque (' + shots.length + ')</h2>' +
        '<div class="small dim">Associez chaque capture à une section pour la retrouver pendant l’entraînement.</div></div>' +
        '<button class="btn sm danger" id="clrShots">Tout supprimer</button>' +
      '</div>' +
      '<div class="gallery sp2">' + (shots.length ? shots.map(s =>
        '<div class="shot"><img src="' + s.data + '" alt="' + U.esc(s.name) + '" loading="lazy">' +
        '<div class="cap"><span>' + U.esc(String(s.name).slice(0, 20)) + '</span>' +
        '<span class="row"><select data-id="' + s.id + '" data-note="' + U.esc(s.note || 'autre') + '" class="shotSel" style="font-size:11px;padding:3px 4px"></select>' +
        '<button data-del="' + s.id + '">✕</button></span></div></div>').join('')
        : '<div class="small dim">Aucune capture importée.</div>') + '</div>' +
      '</div>';

    const dz = U.$('#dz'), fi = U.$('#fileIn');
    const handle = async (files) => {
      if (!files || !files.length) return;
      let n = 0;
      for (const f of files) { if (f.type.startsWith('image/')) { await CORE.addShot(f, 'autre'); n++; } }
      U.toast(n + ' capture(s) importée(s) — non modifiée(s)');
      capturesView();
    };
    dz.onclick = () => fi.click();
    fi.onchange = () => handle(fi.files);
    dz.ondragover = (e) => { e.preventDefault(); dz.classList.add('over'); };
    dz.ondragleave = () => dz.classList.remove('over');
    dz.ondrop = (e) => { e.preventDefault(); dz.classList.remove('over'); handle(e.dataTransfer.files); };
    document.onpaste = (e) => { const items = (e.clipboardData || {}).items || []; const fs = []; for (const it of items) { if (it.type.startsWith('image/')) { const f = it.getAsFile(); if (f) fs.push(f); } } if (fs.length) handle(fs); };
    U.$$('[data-del]').forEach(b => b.onclick = async () => { await CORE.idb.del(+b.dataset.del); capturesView(); });
    U.$('#clrShots').onclick = async () => { if (confirm('Supprimer toutes les captures ?')) { await CORE.idb.clear(); capturesView(); } };
    const META = { verbal: 'Verbal', verbalX: 'Anglais ∞', numerical: 'Numerical', deductive: 'Déductif', switch: 'Switch', inductive: 'Inductif', concentration: 'Concentration', learning: 'Learning', memory: 'Mémoire', info: 'Information', mech: 'Mécanique', workBehaviour: 'Comportement', motivation: 'Motivation', autre: 'Autre' };
    U.$$('.shotSel').forEach(s => {
      const cur = s.dataset.note || 'autre';
      s.innerHTML = Object.keys(META).map(k => '<option value="' + k + '"' + (k === cur ? ' selected' : '') + '>' + META[k] + '</option>').join('');
      s.onchange = async () => {
        const all = await CORE.idb.all(); const rec = all.find(x => x.id === +s.dataset.id);
        if (rec) { rec.note = s.value; await CORE.idb.del(rec.id); await CORE.idb.put(rec); U.toast('Capture classée'); }
      };
    });
  }

  /* ═══════════════════ AIDE & RÉGLAGES ═══════════════════ */
  function settingsView() {
    const st = CORE.P.settings();
    const size = (U.store.size() / 1024).toFixed(1);
    view.className = 'view';
    view.innerHTML =
      '<div class="pagecard">' +
      '<h1>Aide &amp; réglages</h1>' +
      '<p class="intro" style="margin-bottom:18px">Tout est stocké localement dans ce navigateur. Aucune donnée n’est envoyée sur Internet.</p>' +

      '<div class="card"><div class="card-t">Pendant les exercices</div>' +
        swRow('sound', 'Signal sonore', 'Bip à chaque bonne / mauvaise réponse', st.sound) +
        swRow('keyboard', 'Raccourcis clavier', '1-4 pour répondre · Entrée pour valider · Espace pour passer', st.keyboard) +
        swRow('theme', 'Thème sombre', 'Basculer l’affichage en mode sombre', st.theme === 'dark') +
      '</div>' +

      '<div class="card sp"><div class="card-t">Par défaut</div>' +
        '<div class="setrow"><div><div class="t">Feedback</div><div class="d">Immédiat = entraînement · Fin de session = examen</div></div>' +
        '<select id="sFb"><option value="immediate">Immédiat</option><option value="end">Fin de session</option></select></div>' +
        '<div class="setrow"><div><div class="t">Objectif de bonnes réponses (batterie ∞)</div><div class="d">Cible annoncée : 50</div></div>' +
        '<input id="sTarget" type="number" min="5" max="300" value="' + (st.target || 50) + '" style="width:88px"></div>' +
      '</div>' +

      '<div class="card sp"><div class="card-t">Profils &amp; accès</div>' +
        '<div class="setrow"><div><div class="t">Profil actif</div><div class="d">Chaque profil a son propre historique, horodaté</div></div>' +
        '<div class="row"><span class="tag blu">' + U.esc(CORE.P.PROFILES.current() || '—') + '</span>' +
        '<button class="btn sm" id="stProfile">Gérer les profils</button></div></div>' +
        '<div class="setrow"><div><div class="t">Code d’accès</div><div class="d">Requis à l’ouverture du site (à communiquer aux personnes autorisées)</div></div>' +
        '<input id="stCode" value="' + U.esc(CORE.P.code()) + '" style="width:150px;text-transform:uppercase"></div>' +
        '<div class="setrow"><div><div class="t">Profils enregistrés</div><div class="d">' + (CORE.P.PROFILES.list().join(' · ') || 'aucun') + '</div></div>' +
        '<span class="tag">' + CORE.P.PROFILES.list().length + '</span></div>' +
      '</div>' +

      '<div class="card sp"><div class="card-t">Données</div>' +
        '<div class="setrow"><div><div class="t">Historique</div><div class="d">' + CORE.P.attempts().length + ' sessions · ' + size + ' Ko utilisés</div></div>' +
        '<div class="row"><button class="btn sm" id="expBtn">Exporter</button><button class="btn sm" id="impBtn">Importer</button><button class="btn sm danger" id="rstBtn">Réinitialiser</button></div></div>' +
        '<div class="setrow"><div><div class="t">Captures importées</div><div class="d">Stockées en base locale (IndexedDB), jamais modifiées</div></div>' +
        '<button class="btn sm danger" id="clrShots">Supprimer</button></div>' +
      '</div>' +

      '<div class="card sp"><div class="card-t">Méthode</div>' +
        '<ul class="ul small">' +
        '<li>Les figures et questions d’origine ne doivent être ni déformées ni modifiées : les banques figées reprennent les mêmes formes géométriques paramétriques à chaque tirage.</li>' +
        '<li>Le verbal et le numerical ne se confondent pas : l’un est un jugement sur un texte, l’autre un calcul sur un tableau.</li>' +
        '<li>Concentration et learning efficiency : temps très court, l’entraînement passe avant la réflexion.</li>' +
        '<li>Comportement professionnel et motivation : l’inconfort du choix rapide est attendu ; la cohérence est le critère.</li>' +
        '<li>Batterie anglaise illimitée : viser <b>50 réponses exactes minimum</b>, puis verrouiller en mode strict.</li>' +
        '</ul></div>' +

      '<div class="card sp" style="text-align:center">' +
        '<div class="small muted">Plateforme personnelle d’entraînement — <b>réservée à Calvin MINANG</b>.<br>Ne pas diffuser · Ne pas publier · Aucune donnée personnelle transmise.</div>' +
      '</div>' +
      '</div>';

    U.$('#sFb').value = st.feedback;
    U.$('#sFb').onchange = (e) => { st.feedback = e.target.value; CORE.P.saveSettings(st); U.toast('Enregistré'); };
    U.$('#sTarget').onchange = (e) => { st.target = Math.max(1, +e.target.value || 50); CORE.P.saveSettings(st); U.toast('Objectif : ' + st.target); };
    U.$('#stProfile').onclick = () => userMenu();
    U.$('#stCode').onchange = (e) => { const s2 = CORE.P.settings(); s2.code = (e.target.value || 'CM2026').trim().toUpperCase(); CORE.P.saveSettings(s2); U.toast('Code d’accès enregistré'); };
    U.$('#expBtn').onclick = () => exportData();
    U.$('#impBtn').onclick = () => importData();
    U.$('#rstBtn').onclick = () => { if (confirm('Réinitialiser tout l’historique et les réglages ?')) { CORE.P.clear(); U.store.wipe(); U.toast('Réinitialisé'); routeAndBind(); applyTheme('light'); } };
    U.$('#clrShots').onclick = async () => { await CORE.idb.clear(); U.toast('Captures supprimées'); };
  }
  function swRow(key, title, desc, on) {
    return '<div class="setrow"><div><div class="t">' + title + '</div><div class="d">' + desc + '</div></div>' +
      '<div class="switch ' + (on ? 'on' : '') + '" data-k="' + key + '"><i></i></div></div>';
  }

  function bindSwitches() {
    U.$$('.switch[data-k]').forEach(s => s.onclick = () => {
      const st = CORE.P.settings();
      if (s.dataset.k === 'theme') { const dark = st.theme !== 'dark'; applyTheme(dark ? 'dark' : 'light'); return; }
      st[s.dataset.k] = !st[s.dataset.k];
      CORE.P.saveSettings(st); s.classList.toggle('on', !!st[s.dataset.k]);
    });
  }

  /* ═══════════════════ THÈME & LANGUE ═══════════════════ */
  function applyTheme(theme) {
    document.documentElement.dataset.theme = theme;
    const st = CORE.P.settings(); st.theme = theme; CORE.P.saveSettings(st);
    const sw = U.$('#themeSw');
    if (sw) sw.classList.toggle('on', theme === 'dark');
    U.$$('.switch[data-k="theme"]').forEach(x => x.classList.toggle('on', theme === 'dark'));
  }

  /* ═══════════════════ IMPORT / EXPORT ═══════════════════ */
  function exportData() {
    const payload = { app: 'skema-trainer', version: 2, user: 'Calvin MINANG', at: new Date().toISOString(), attempts: CORE.P.attempts(), settings: CORE.P.settings() };
    const blob = new Blob([JSON.stringify(payload, null, 1)], { type: 'application/json' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'skema-trainer-calvin-' + U.dayKey() + '.json';
    a.click();
    U.toast('Export généré');
  }
  function importData() {
    const i = document.createElement('input'); i.type = 'file'; i.accept = 'application/json';
    i.onchange = () => {
      const f = i.files[0]; if (!f) return;
      const fr = new FileReader();
      fr.onload = () => {
        try {
          const d = JSON.parse(fr.result);
          if (d.attempts) U.store.set('attempts', d.attempts);
          if (d.settings) U.store.set('settings', d.settings);
          U.toast('Données importées'); routeAndBind();
        } catch (e) { U.toast('Fichier illisible', 'err'); }
      };
      fr.readAsText(f);
    };
    i.click();
  }

  /* ═══════════════════ BOOT ═══════════════════ */
  window.addEventListener('hashchange', routeAndBind);
  U.$('#burger').onclick = () => U.$('#mainnav').classList.toggle('open');
  U.$('#mainnav').addEventListener('click', (e) => { if (e.target.tagName === 'A') U.$('#mainnav').classList.remove('open'); });
  U.$$('[data-nav]').forEach(n => n.addEventListener('click', () => { if (n.dataset.nav) location.hash = n.dataset.nav; }));

  /* sélecteur de langue global (défaut des consignes) */
  const ls = U.$('#langSel');
  const st0 = CORE.P.settings();
  ls.value = I18N.current();
  ls.onchange = () => setLang(ls.value);

  /* interrupteur de thème de l'en-tête */
  const themeSw = U.$('#themeSw');
  if (themeSw) themeSw.onclick = () => applyTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark');

  U.$('#footerMeta').textContent = 'Usage personnel · v3.0 — ' + new Date().toLocaleDateString('fr-FR');
  applyTheme(document.documentElement.dataset.theme === 'dark' ? 'dark' : 'light');

  /* pastille utilisateur */
  if (U.$('#userBtn')) U.$('#userBtn').onclick = () => userMenu();
  paintUser();

  /* langue de l'interface (FR par défaut, mémorisée par profil/navigateur) */
  if (typeof I18N !== 'undefined') {
    I18N.init();
    I18N.onChange(() => {
      /* pendant une session en cours on ne relance pas l'exercice : on retraduit l'écran */
      if (location.hash.indexOf('#/run/') === 0 || location.hash.indexOf('#/session/') === 0) {
        I18N.apply(document.body);
        const v = U.$('#view'); if (v) I18N.apply(v);
      } else routeAndBind();
    });
  }

  /* accès : profil mémorisé -> application ; sinon écran d'accès (code + prénom) */
  CORE.P.migrate();
  if (!CORE.P.PROFILES.current()) {
    showLogin();
  } else {
    document.documentElement.classList.remove('userpending');
    routeAndBind();
  }
})();
