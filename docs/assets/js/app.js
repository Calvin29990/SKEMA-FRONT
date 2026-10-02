/* ═══════════════════════════════════════════════════════════════
   app.js — routeur, accueil « Tâches à accomplir » (14 lignes),
   profils, progression, feedback détaillé, réglages, export/import.
   Assessment Trainer — Calvin MINANG — usage personnel.
   ═══════════════════════════════════════════════════════════════ */
'use strict';

(() => {
  const P = CORE.P, esc = U.esc, $ = U.$;
  const view = () => document.getElementById('view');

  /* ═══════════════ Menu burger ═══════════════ */
  const burger = $('#skBurger'), menu = $('#skMenu');
  burger.onclick = (e) => { e.stopPropagation(); menu.classList.toggle('open'); };
  document.addEventListener('click', (e) => { if (menu.classList.contains('open') && !menu.contains(e.target)) menu.classList.remove('open'); });
  menu.addEventListener('click', (e) => { if (e.target.tagName === 'A') menu.classList.remove('open'); });

  /* ═══════════════ Profil / première visite ═══════════════ */
  function ensureUser() {
    const cur = P.PROFILES.current();
    if (cur) return paintUser();
    const list = P.PROFILES.list();
    U.modal('<h2>Bienvenue</h2><p class="tiny">Plateforme d’entraînement personnelle — conforme au document de référence. Choisissez ou créez un profil (les résultats sont enregistrés par profil, dans ce navigateur uniquement).</p>' +
      (list.length ? '<div class="userlist">' + list.map(u => '<button class="btn" data-u="' + esc(u) + '">' + esc(u) + '</button>').join('') + '</div><p class="tiny">…ou nouveau profil :</p>' : '') +
      '<div class="row"><input id="uName" class="inp" placeholder="Prénom NOM" autocomplete="off"><button class="btn primary" id="uGo">Entrer</button></div>');
    $('#uGo').onclick = () => { const n = P.PROFILES.set($('#uName').value); if (!n) return U.toast('Indiquez un nom de profil', 'err'); U.closeModal(); paintUser(); route(); };
    $('#uName').addEventListener('keydown', (e) => { if (e.key === 'Enter') $('#uGo').click(); });
    document.querySelectorAll('.userlist [data-u]').forEach(b => b.onclick = () => { P.PROFILES.set(b.dataset.u); U.closeModal(); paintUser(); route(); });
  }
  function paintUser() { $('#skUserName').textContent = P.PROFILES.current() || '—'; }

  /* ═══════════════ Routeur ═══════════════ */
  function route() {
    const h = location.hash || '#/';
    if (!h.startsWith('#/run/') && CORE.current) CORE.destroy();
    if (h.startsWith('#/run/')) { const id = h.slice(6); if (CORE.byId(id)) { if (!CORE.current || CORE.current.sec.id !== id) CORE.start(id); return; } location.hash = '#/'; return; }
    document.getElementById('navGrid').classList.remove('on');
    const tab = h === '#/progression' ? 'progression' : h === '#/feedback' ? 'feedback' : h === '#/reglages' ? 'reglages' : 'home';
    const tabs = document.getElementById('skTabs');
    if (tabs) tabs.querySelectorAll('a').forEach(a => a.classList.toggle('on', a.dataset.tab === tab));
    if (h === '#/progression') return pageProgress();
    if (h === '#/feedback') return pageFeedback();
    if (h === '#/reglages') return pageSettings();
    pageHome();
  }
  window.addEventListener('hashchange', route);

  /* ═══════════════ ACCUEIL — liste des 14 tâches ═══════════════ */
  function pageHome() {
    document.getElementById('skTitle').textContent = 'Tâches à accomplir';
    const v = view(); v.className = 'sk-main home';
    v.innerHTML = '<div class="home-head"><h1>Tâches à accomplir</h1><p class="tiny">Chaque ligne ouvre le test réel : consignes, exemples, chronomètre et navigation identiques au document de référence.</p></div>' +
      '<div class="tasks">' + CORE.SECTIONS.map(s => {
        const st = P.statsFor(s.id);
        const badge = st ? (st.behavioural ? '<span class="tk-badge">' + st.n + '× fait</span>' : '<span class="tk-badge">' + U.pct(st.last) + '</span>') : '';
        return '<div class="task" data-id="' + s.id + '"><div class="tk-name">' + esc(s.home) + '</div><div class="tk-time">' + s.min + ' minutes</div>' + badge +
          (s.noDetail ? '' : '<button class="tk-info" data-info="' + s.id + '" title="Détails">›</button>') +
          '<button class="tk-start" data-start="' + s.id + '">Début</button></div>';
      }).join('') + '</div>';
    v.querySelectorAll('[data-start]').forEach(b => b.onclick = () => { location.hash = '#/run/' + b.dataset.start; });
    v.querySelectorAll('[data-info]').forEach(b => b.onclick = (e) => { e.stopPropagation(); infoModal(b.dataset.info); });
  }
  function infoModal(id) {
    const s = CORE.byId(id), st = P.statsFor(id);
    const intro = (BANK.INTRO[id] && BANK.INTRO[id][0]) ? BANK.INTRO[id][0].fr : '';
    const plain = intro.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 420);
    U.modal('<h2>' + esc(s.home) + '</h2><p class="tiny">' + esc(s.head) + ' — durée indicative ' + s.min + ' min.</p>' +
      (plain ? '<p class="tiny">' + esc(plain) + '…</p>' : '') +
      (st ? '<p class="tiny">Vos résultats : ' + (st.behavioural ? st.n + ' passage(s), questionnaire sans bonne réponse.' : st.n + ' passage(s) — meilleur ' + U.pct(st.best) + ', dernier ' + U.pct(st.last) + ', moyenne ' + U.pct(st.avg) + '.') + '</p>' : '<p class="tiny">Jamais passé sur ce profil.</p>') +
      '<div class="row end"><button class="btn" id="miClose">Fermer</button><button class="btn primary" id="miGo">Début</button></div>');
    $('#miClose').onclick = U.closeModal;
    $('#miGo').onclick = () => { U.closeModal(); location.hash = '#/run/' + id; };
  }

  /* ═══════════════ PROGRESSION ═══════════════ */
  function pageProgress() {
    document.getElementById('skTitle').textContent = 'Progression';
    const v = view(); v.className = 'sk-main page';
    const o = P.overall(), att = P.attempts().slice().reverse();
    v.innerHTML = '<h1>Progression</h1>' +
      '<div class="cards">' +
      card('Sessions', o.n) + card('Réponses correctes', o.correct + ' / ' + o.items) + card('Précision globale', U.pct(o.accuracy)) + card('Temps cumulé', Math.round(o.minutes) + ' min') +
      '</div>' +
      '<h2>Par épreuve</h2><div class="tbl-wrap"><table class="tbl"><thead><tr><th>Épreuve</th><th>Passages</th><th>Meilleur</th><th>Dernier</th><th>Moyenne</th><th>Temps moy./question</th></tr></thead><tbody>' +
      CORE.SECTIONS.map(s => { const st = P.statsFor(s.id); return '<tr><td>' + esc(s.home) + '</td>' + (st ? (st.behavioural ? '<td>' + st.n + '</td><td colspan="4" class="tiny">questionnaire sans bonne réponse</td>' : '<td>' + st.n + '</td><td>' + U.pct(st.best) + '</td><td>' + U.pct(st.last) + '</td><td>' + U.pct(st.avg) + '</td>') + '<td>' + (st.avgMs ? (st.avgMs / 1000).toFixed(1) + ' s' : '—') + '</td>' : '<td colspan="5" class="tiny">jamais passé</td>') + '</tr>'; }).join('') +
      '</tbody></table></div>' +
      '<h2>Historique</h2>' + (att.length ? '<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Date</th><th>Épreuve</th><th>Score</th><th>Précision</th><th>Durée</th><th></th></tr></thead><tbody>' +
        att.slice(0, 60).map(a => '<tr><td>' + esc(a.date || '') + ' ' + esc(a.time || '') + '</td><td>' + esc(a.sectionName || a.section) + '</td><td>' + (a.behavioural ? '—' : a.correct + '/' + a.items) + '</td><td>' + (a.accuracy == null ? '—' : U.pct(a.accuracy)) + '</td><td>' + Math.round((a.ms || 0) / 60000) + ' min</td><td><button class="btn xs" data-sess="' + a.id + '">Détail</button></td></tr>').join('') +
        '</tbody></table></div>' : '<p class="tiny">Aucune session pour l’instant.</p>') +
      '<div class="row end" style="margin-top:18px"><button class="btn danger" id="pgReset">Effacer l’historique du profil</button></div>';
    v.querySelectorAll('[data-sess]').forEach(b => b.onclick = () => sessModal(b.dataset.sess));
    $('#pgReset').onclick = () => {
      U.modal('<h2>Effacer ?</h2><p class="tiny">Tout l’historique et les détails du profil courant seront supprimés de ce navigateur.</p><div class="row end"><button class="btn" id="rcNo">Annuler</button><button class="btn danger" id="rcYes">Effacer</button></div>');
      $('#rcNo').onclick = U.closeModal;
      $('#rcYes').onclick = () => { P.clear(); U.closeModal(); U.toast('Historique effacé'); route(); };
    };
  }
  const card = (t, val) => '<div class="card"><div class="cv">' + val + '</div><div class="ct">' + esc(t) + '</div></div>';

  function sessModal(id) {
    const a = P.sessionOf(id), log = P.sessionLog(id);
    const sec = a && CORE.byId(a.section);
    U.modal('<h2>' + esc((a && a.sectionName) || 'Session') + '</h2>' +
      '<p class="tiny">' + esc((a && a.date) || '') + ' ' + esc((a && a.time) || '') +
      (a && a.accuracy != null ? ' — score ' + a.correct + '/' + a.items + ' (' + U.pct(a.accuracy) + ')' : '') +
      (a && a.ms ? ' — durée ' + Math.round(a.ms / 60000) + ' min' : '') + '</p>' +
      '<div class="fbbox">' + (log.length ? log.map((r, i) => '<div class="logrow ' + (r.ok === true ? 'ok' : r.ok === false ? 'ko' : '') + '"><b>Question ' + (r.n || i + 1) + '</b> — ' + esc(r.q) +
        '<br><span class="tiny">Votre réponse : <b>' + esc(r.given) + '</b> · Bonne réponse : <b>' + esc(r.correct) + '</b>' + (r.ms ? ' · ' + U.ms(r.ms) : '') +
        (r.why ? '<br>Explication : ' + esc(r.why) : '') + '</span></div>').join('') : '<p class="tiny">Aucun détail enregistré pour cette session.</p>') + '</div>' +
      '<div class="row end"><button class="btn" id="smClose">Fermer</button>' +
      (sec ? '<button class="btn primary" id="smRedo">Refaire cette épreuve</button>' : '') +
      '<button class="btn" id="smCsv">Exporter en CSV</button></div>');
    $('#smClose').onclick = U.closeModal;
    $('#smCsv').onclick = () => P.csv(id);
    if (sec) $('#smRedo').onclick = () => { U.closeModal(); location.hash = '#/run/' + sec.id; };
  }

  /* ═══════════════ FEEDBACK ═══════════════ */
  function pageFeedback() {
    document.getElementById('skTitle').textContent = 'Feedback';
    const v = view(); v.className = 'sk-main page';
    const o = P.overall(), att = P.attempts().slice().reverse(), wrongs = P.wrongs(80);
    v.innerHTML = '<h1>Feedback</h1>' +
      '<p class="tiny">Relecture en français de vos sessions : épreuve, question, réponse donnée, bonne réponse et explication. Tout reste dans ce navigateur.</p>' +
      '<div class="cards">' + card('Sessions enregistrées', o.n) + card('Réponses correctes', o.correct + ' / ' + o.items) + card('Précision globale', U.pct(o.accuracy)) + card('Temps cumulé', Math.round(o.minutes) + ' min') + '</div>' +
      '<div class="setbox"><h2>Revoir une session</h2>' +
      '<div class="setrow"><span>Filtrer par épreuve</span><select id="fbSel"><option value="">Toutes les épreuves</option>' +
      CORE.SECTIONS.map(s2 => '<option value="' + s2.id + '">' + esc(s2.home) + '</option>').join('') + '</select></div>' +
      '<div class="sesslist" id="fbList"></div></div>' +
      '<h2>Dernières erreurs</h2>' +
      (wrongs.length
        ? '<p class="tiny">Chaque ligne indique la question, votre réponse, la bonne réponse et l’explication.</p>' +
          '<div class="logbox">' + wrongs.map(r => '<div class="logrow ko"><b>' + esc(r.q) + '</b><br><span class="tiny">' +
            (r.sectionName ? esc(r.sectionName) + ' · ' : '') + 'Votre réponse : <b>' + esc(r.given) + '</b> · Bonne réponse : <b>' + esc(r.correct) + '</b>' +
            (r.why ? ' · ' + esc(r.why) : '') + '</span></div>').join('') + '</div>'
        : '<p class="tiny">Aucune erreur enregistrée pour l’instant — bravo.</p>');
    const paint = () => {
      const id = $('#fbSel').value, list = att.filter(a => !id || a.section === id);
      $('#fbList').innerHTML = list.length ? list.slice(0, 60).map(a =>
        '<button class="btn xs" data-sess="' + a.id + '">' + esc(a.sectionName || a.section) + ' · ' + esc(a.date || '') + ' ' + esc(a.time || '') +
        (a.accuracy == null ? '' : ' · ' + U.pct(a.accuracy)) + '</button>').join('')
        : '<p class="tiny">Aucune session pour ce filtre.</p>';
      $('#fbList').querySelectorAll('[data-sess]').forEach(b => b.onclick = () => sessModal(b.dataset.sess));
    };
    $('#fbSel').onchange = paint;
    paint();
  }

  /* ═══════════════ RÉGLAGES ═══════════════ */
  function pageSettings() {
    document.getElementById('skTitle').textContent = 'Aide & réglages';
    const v = view(); v.className = 'sk-main page';
    const st = P.settings();
    v.innerHTML = '<h1>Aide &amp; réglages</h1>' +
      '<div class="setbox"><h2>Langue des consignes (tests de langues)</h2>' +
      '<div class="setrow"><span>Compétences Linguistiques - Anglais</span><select id="lgEn"><option value="fr">Français</option><option value="en">English</option></select></div>' +
      '<div class="setrow"><span>Compétences Linguistiques - Français</span><select id="lgFr"><option value="fr">Français</option><option value="en">English</option></select></div>' +
      '<h2>Interface</h2>' +
      '<div class="setrow"><span>Sons (retours sonores)</span><input type="checkbox" id="stSound"></div>' +
      '<div class="setrow"><span>Raccourcis clavier (1-4, D/A…)</span><input type="checkbox" id="stKeys"></div>' +
      '<div class="setrow"><span>Code d’accès du profil</span><input class="inp sm" id="stCode" maxlength="12"></div>' +
      '<h2>Données</h2><p class="tiny">Tout est stocké localement dans ce navigateur (localStorage), par profil. L’export JSON contient l’historique et le détail question par question.</p>' +
      '<div class="row"><button class="btn" id="stExport">Exporter (JSON)</button><button class="btn" id="stImport">Importer</button><button class="btn danger" id="stPurge">Supprimer ce profil</button></div></div>' +
      '<h2>Aide</h2><div class="setbox tiny"><p>• Accueil → « Début » lance le test réel (consignes + exemples + chrono).</p><p>• Pendant un test : le menu ≡ reste accessible ; « ›/‹ » et « ▦ » naviguent entre questions quand le test réel le permet.</p><p>• Tests chronométrés : le temps restant s’affiche en haut à droite ; à 0, la session se termine et les questions non répondues comptent comme incorrectes.</p><p>• Comportements / Motivations : répartissez jusqu’à 6 points par bloc (1-6), sans obligation de tout distribuer.</p><p>• Concentration : touches D = correct, A = incorrect.</p></div>';
    $('#lgEn').value = P.lang({ id: 'english' }); $('#lgFr').value = P.lang({ id: 'french' });
    $('#lgEn').onchange = (e) => P.setLang('english', e.target.value);
    $('#lgFr').onchange = (e) => P.setLang('french', e.target.value);
    $('#stSound').checked = !!st.sound; $('#stKeys').checked = st.keyboard !== false; $('#stCode').value = st.code || 'CM2026';
    $('#stSound').onchange = (e) => { st.sound = e.target.checked; P.saveSettings(st); };
    $('#stKeys').onchange = (e) => { st.keyboard = e.target.checked; P.saveSettings(st); };
    $('#stCode').onchange = (e) => { st.code = (e.target.value || 'CM2026').trim().toUpperCase(); P.saveSettings(st); U.toast('Code mis à jour'); };
    $('#stExport').onclick = exportJSON;
    $('#stImport').onclick = importJSON;
    $('#stPurge').onclick = () => {
      U.modal('<h2>Supprimer le profil ?</h2><p class="tiny">Historique et détails du profil « ' + esc(P.PROFILES.current() || '') + ' » seront définitivement supprimés de ce navigateur.</p><div class="row end"><button class="btn" id="pcNo">Annuler</button><button class="btn danger" id="pcYes">Supprimer</button></div>');
      $('#pcNo').onclick = U.closeModal;
      $('#pcYes').onclick = () => { P.PROFILES.purge(P.PROFILES.current()); U.closeModal(); paintUser(); location.hash = '#/'; ensureUser(); };
    };
  }

  /* ═══════════════ Export / Import JSON ═══════════════ */
  function exportJSON() {
    const who = P.PROFILES.current() || 'Invité';
    const data = { app: 'skema-training', v: 4, exportedAt: new Date().toISOString(), profile: who, settings: P.settings(), attempts: P.attempts(), details: P.details() };
    const blob = new Blob([JSON.stringify(data, null, 1)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const lk = document.createElement('a'); lk.href = url; lk.download = 'skema-training-' + who.toLowerCase().replace(/\s+/g, '-') + '-' + new Date().toISOString().slice(0, 10) + '.json'; lk.click();
    U.toast('Sauvegarde exportée');
  }
  function importJSON() {
    U.modal('<h2>Importer une sauvegarde</h2><p class="tiny">Choisissez un fichier JSON exporté depuis cette plateforme. Les données seront fusionnées dans le profil courant « ' + esc(P.PROFILES.current() || 'Invité') + ' ».</p><div class="row"><input type="file" id="impFile" accept=".json,application/json"><button class="btn primary" id="impGo">Importer</button></div>');
    $('#impGo').onclick = () => {
      const f = $('#impFile').files && $('#impFile').files[0];
      if (!f) return U.toast('Choisissez un fichier', 'err');
      const rd = new FileReader();
      rd.onload = () => {
        try {
          const d = JSON.parse(rd.result);
          if (d.app !== 'skema-training' || !Array.isArray(d.attempts)) throw new Error('format');
          const att = P.attempts(), det = P.details();
          const seen = new Set(att.map(a => a.id));
          let n = 0;
          d.attempts.forEach(a => { if (a && a.id && !seen.has(a.id)) { att.push(a); seen.add(a.id); n++; } });
          U.store.set(P.key('attempts'), att.slice(-800));
          if (d.details && typeof d.details === 'object') { Object.keys(d.details).forEach(k => { if (!det[k]) { det[k] = d.details[k]; n++; } }); U.store.set(P.key('details'), det); }
          if (d.settings && d.settings.langs) { const s = P.settings(); s.langs = Object.assign({}, s.langs, d.settings.langs); P.saveSettings(s); }
          U.closeModal(); U.toast('Import terminé : ' + n + ' élément(s) ajouté(s) au profil courant'); route();
        } catch (e) { U.toast('Fichier invalide', 'err'); }
      };
      rd.readAsText(f);
    };
  }

  /* ═══════════════ Barre rouge : boutons ═══════════════ */
  $('#skExport').onclick = () => { menu.classList.remove('open'); exportJSON(); };
  $('#skImport').onclick = () => { menu.classList.remove('open'); importJSON(); };
  $('#skUser').onclick = () => { menu.classList.remove('open'); ensureUser2(); };
  $('#skOut').onclick = () => { menu.classList.remove('open'); P.PROFILES.logout(); paintUser(); CORE.destroy(); location.hash = '#/'; ensureUser(); };
  function ensureUser2() {
    const list = P.PROFILES.list();
    U.modal('<h2>Profil</h2><p class="tiny">Profil actuel : <b>' + esc(P.PROFILES.current() || '—') + '</b></p>' +
      '<div class="userlist">' + list.map(u => '<button class="btn" data-u="' + esc(u) + '">' + esc(u) + '</button>').join('') + '</div>' +
      '<div class="row"><input id="uName2" class="inp" placeholder="Nouveau profil" autocomplete="off"><button class="btn primary" id="uGo2">Changer</button></div>');
    $('#uGo2').onclick = () => { const n = P.PROFILES.set($('#uName2').value); if (!n) return U.toast('Indiquez un nom', 'err'); U.closeModal(); paintUser(); route(); };
    document.querySelectorAll('.userlist [data-u]').forEach(b => b.onclick = () => { P.PROFILES.set(b.dataset.u); U.closeModal(); paintUser(); route(); });
  }

  /* ═══════════════ Démarrage ═══════════════ */
  $('#footMeta').textContent = 'Assessment Trainer v4.1 — conforme au document de référence — ' + new Date().toLocaleDateString('fr-FR');
  ensureUser();
  route();
})();
