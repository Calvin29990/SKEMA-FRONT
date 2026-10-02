/* généré depuis /tmp/i18n — ne pas éditer à la main */

/* ═══════════════════════════════════════════════════════════════
   i18n.js — interface multilingue (Français / English / Español / Português)
   Traduit l'interface ET le feedback. Les questions et figures des tests
   ne sont jamais modifiées : seul l'habillage est traduit.
   ═══════════════════════════════════════════════════════════════ */
'use strict';

const I18N = (() => {

  const LANGS = [
    { id: 'fr', label: 'Français (UE)', short: 'Français' },
    { id: 'en', label: 'English (UK)', short: 'English' },
    { id: 'es', label: 'Español', short: 'Español' },
    { id: 'pt', label: 'Português', short: 'Português' }
  ];
  const DICT = __DICT__;
  /* les règles arrivent en JSON : on reconstruit les expressions régulières */
  const RAW = __RAW__;
  const RULES = {};
  Object.keys(RAW).forEach(k => { RULES[k] = RAW[k].map(r => ({ re: new RegExp(r.re), to: r.to })); });

  let cur = 'fr';
  const observers = [];
  const SKIP = { SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, TEXTAREA: 1, CODE: 1, PRE: 1 };
  const ATTRS = ['placeholder', 'title', 'aria-label', 'alt'];

  const norm = (s) => String(s).replace(/[\u2019\u2018\u02bc]/g, "'").replace(/\u00a0/g, ' ')
    .replace(/\s+/g, ' ').trim();

  /** Traduit une chaîne (utilisable hors DOM : CSV, impressions…). */
  function tr(s, lang) {
    const L = lang || cur;
    if (L === 'fr' || !s) return s;
    const m = /^(\s*)([\s\S]*?)(\s*)$/.exec(s);
    const lead = m[1], body = m[2], tail = m[3];
    if (!body) return s;
    const d = DICT[L] || {}, rules = RULES[L] || [];
    const dictOf = (x) => d[norm(x)];
    const ruleOf = (x) => {
      for (let i = 0; i < rules.length; i++) if (rules[i].re.test(x)) return x.replace(rules[i].re, rules[i].to);
      return undefined;
    };
    /* découpe sur les séparateurs et traduit chaque morceau (dict puis règle) */
    const parts = (x) => {
      const seps = [' · ', ' — ', ' – ', ' ; '];
      for (let i = 0; i < seps.length; i++) {
        const sep = seps[i];
        if (x.indexOf(sep) < 0) continue;
        const seg = x.split(sep).map(q => {
          const dd = dictOf(q);
          if (dd !== undefined) return dd;
          const rr = ruleOf(q);
          return rr !== undefined ? rr : q;
        });
        const joined = seg.join(sep);
        if (joined !== x) return joined;
      }
      return undefined;
    };
    let out = dictOf(body);
    if (out === undefined) {
      const rr = ruleOf(body);
      if (rr !== undefined) out = parts(rr) || rr;
    }
    if (out === undefined) out = parts(body);
    if (out === undefined) return s;
    return lead + out + tail;
  }

  function aplicable(el) {
    if (!el) return false;
    if (SKIP[el.tagName]) return false;
    if (el.closest && el.closest('[data-noi18n]')) return false;
    if (el.dataset && el.dataset.noi18n !== undefined) return false;
    return true;
  }

  /** Traduit un arbre DOM (idempotent : repart toujours du texte d'origine). */
  function apply(root, lang) {
    const L = lang || cur;
    applyTo(root || document.body, L);
  }

  function applyTo(root, L) {
    if (!root) return;
    if (root.nodeType === 3) { translateTextNode(root, L); return; }
    if (root.nodeType !== 1 && root.nodeType !== 9) return;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null);
    let n;
    while ((n = walker.nextNode())) translateTextNode(n, L);
    if (root.nodeType === 1 || root.nodeType === 9) {
      const els = root.querySelectorAll ? root.querySelectorAll('*') : [];
      for (let i = 0; i < els.length; i++) translateAttrs(els[i], L);
      if (root.nodeType === 1) translateAttrs(root, L);
    }
  }

  function translateTextNode(node, L) {
    if (!aplicable(node.parentElement)) return;
    if (node.__i18nSrc === undefined) node.__i18nSrc = node.nodeValue;
    const src = node.__i18nSrc;
    if (!src || !src.trim()) return;
    const out = (L === 'fr') ? src : tr(src, L);
    if (node.nodeValue !== out) { written.set(node, out); node.nodeValue = out; }
  }

  function translateAttrs(el, L) {
    if (!el.getAttribute || !aplicable(el)) return;
    if (!el.__i18nAttr) el.__i18nAttr = {};
    for (let i = 0; i < ATTRS.length; i++) {
      const a = ATTRS[i];
      const v = el.getAttribute(a);
      if (v == null || !v.trim()) continue;
      if (el.__i18nAttr[a] === undefined) el.__i18nAttr[a] = v;
      const out = (L === 'fr') ? el.__i18nAttr[a] : tr(el.__i18nAttr[a], L);
      if (v !== out) el.setAttribute(a, out);
    }
  }

  const written = new WeakMap();
  let mo = null;
  function observe() {
    if (mo || typeof MutationObserver === 'undefined') return;
    mo = new MutationObserver((muts) => {
      for (let i = 0; i < muts.length; i++) {
        const m = muts[i];
        if (m.type === 'characterData') {
          if (written.get(m.target) === m.target.nodeValue) continue;
          translateTextNode(m.target, cur);
        } else {
          for (let j = 0; j < m.addedNodes.length; j++) {
            const a = m.addedNodes[j];
            if (a.nodeType === 3) translateTextNode(a, cur);
            else if (a.nodeType === 1) applyTo(a, cur);
          }
        }
      }
    });
    mo.observe(document.documentElement, { childList: true, subtree: true, characterData: true });
  }

  function current() { return cur; }
  function label(id) { const l = LANGS.filter(x => x.id === (id || cur))[0]; return l ? l.label : ''; }

  function set(lang) {
    if (!LANGS.filter(x => x.id === lang).length) lang = 'fr';
    cur = lang;
    try { document.documentElement.lang = lang; } catch (e) {}
    if (typeof CORE !== 'undefined' && CORE.P && CORE.P.settings) {
      const st = CORE.P.settings();
      if (typeof st.lang !== 'string' || st.lang !== lang) { st.langUI = lang; st.lang = lang; CORE.P.saveSettings(st); }
    }
    observers.forEach(fn => { try { fn(lang); } catch (e) {} });
    apply(document.body, lang);
  }

  function init(initial) {
    let start = initial;
    try { if (!start && typeof CORE !== 'undefined' && CORE.P) start = CORE.P.settings().langUI; } catch (e) {}
    if (typeof start !== 'string' || !LANGS.filter(x => x.id === start).length) start = 'fr';
    cur = start;
    try { document.documentElement.lang = start; } catch (e) {}
    apply(document.body, start);
    observe();
    return start;
  }

  function onChange(fn) { observers.push(fn); }

  /** <select> des 4 langues, prêt à insérer. */
  function selectHTML(extraClass) {
    return '<select class="' + (extraClass || 'tlang') + '" data-lang-sel>' +
      LANGS.map(l => '<option value="' + l.id + '"' + (l.id === cur ? ' selected' : '') + '>' + l.label + '</option>').join('') +
      '</select>';
  }

  return { LANGS, tr, apply, set, init, current, label, onChange, selectHTML, norm };
})();
