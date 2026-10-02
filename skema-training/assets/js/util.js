/* ═══════════════════════════════════════════════════════════════
   util.js — utilitaires partagés (RNG, DOM, stockage, figures SVG)
   Assessment Trainer — Calvin MINANG
   ═══════════════════════════════════════════════════════════════ */
'use strict';

const U = (() => {

  /* ─────────── RNG déterministe (mulberry32) ─────────── */
  function rng(seed) {
    let a = (seed >>> 0) || 1;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  const int = (r, a, b) => a + Math.floor(r() * (b - a + 1));
  const pick = (r, arr) => arr[Math.floor(r() * arr.length)];
  function shuffle(r, arr) {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(r() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }
  function sample(r, arr, n) { return shuffle(r, arr).slice(0, n); }
  const hash = (s) => { let h = 2166136261; for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; };

  /* ─────────── Formatage ─────────── */
  const pct = (n, d = 0) => (n === null || n === undefined || isNaN(n)) ? '—' : (n * 100).toFixed(d) + '%';
  const ms = (n) => n == null ? '—' : (n < 1000 ? Math.round(n) + ' ms' : (n / 1000).toFixed(1) + ' s');
  const num = (n, d = 1) => n == null || isNaN(n) ? '—' : Number(n).toFixed(d);
  const esc = (s) => String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  const fr = (iso) => { const d = new Date(iso); return d.toLocaleDateString('fr-FR', { day: '2-digit', month: 'short' }) + ' ' + d.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' }); };
  const dayKey = (d = new Date()) => d.toISOString().slice(0, 10);
  const daysBetween = (a, b) => Math.round((new Date(b) - new Date(a)) / 86400000);

  /* ─────────── Stockage ─────────── */
  const NS = 'skemaTrainer.v1.';
  const store = {
    get(k, def) {
      try { const v = localStorage.getItem(NS + k); return v === null ? def : JSON.parse(v); }
      catch (e) { return def; }
    },
    set(k, v) { try { localStorage.setItem(NS + k, JSON.stringify(v)); return true; } catch (e) { toast('Stockage local plein ou bloqué', 'err'); return false; } },
    del(k) { try { localStorage.removeItem(NS + k); } catch (e) {} },
    keys() { const out = []; try { for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (k.startsWith(NS)) out.push(k.slice(NS.length)); } } catch (e) {} return out; },
    wipe() { this.keys().forEach(k => this.del(k)); },
    size() { let b = 0; this.keys().forEach(k => { try { b += (localStorage.getItem(NS + k) || '').length; } catch (e) {} }); return b; }
  };

  /* ─────────── DOM ─────────── */
  const $ = (s, root = document) => root.querySelector(s);
  const $$ = (s, root = document) => Array.from(root.querySelectorAll(s));
  function el(tag, attrs, html) {
    const n = document.createElement(tag);
    if (attrs) for (const k in attrs) {
      if (k === 'class') n.className = attrs[k];
      else if (k === 'dataset') Object.assign(n.dataset, attrs[k]);
      else if (k.startsWith('on') && typeof attrs[k] === 'function') n.addEventListener(k.slice(2), attrs[k]);
      else n.setAttribute(k, attrs[k]);
    }
    if (html != null) n.innerHTML = html;
    return n;
  }
  const frag = (html) => { const t = document.createElement('template'); t.innerHTML = html.trim(); return t.content; };

  /* ─────────── Toasts ─────────── */
  function toast(msg, type, ttl = 3200) {
    const wrap = $('#toastWrap'); if (!wrap) return;
    const n = el('div', { class: 'toast ' + (type || '') }, msg);
    wrap.appendChild(n);
    setTimeout(() => { n.style.opacity = '0'; n.style.transform = 'translateX(30px)'; setTimeout(() => n.remove(), 220); }, ttl);
  }

  /* ─────────── Modale ─────────── */
  function modal(html) {
    const back = $('#modalBack'), box = $('#modalBox');
    box.innerHTML = html; back.hidden = false;
    back.onclick = (e) => { if (e.target === back) closeModal(); };
    document.addEventListener('keydown', escClose);
  }
  function escClose(e) { if (e.key === 'Escape') closeModal(); }
  function closeModal() { const b = $('#modalBack'); if (b) b.hidden = true; document.removeEventListener('keydown', escClose); }

  /* ─────────── Sons (bips WebAudio, sans fichier externe) ─────────── */
  let actx = null;
  function beep(kind = 'ok') {
    if (!store.get('settings', {}).sound) return;
    try {
      actx = actx || new (window.AudioContext || window.webkitAudioContext)();
      const o = actx.createOscillator(), g = actx.createGain();
      const f = { ok: 660, ko: 190, tick: 420, end: 520 }[kind] || 500;
      o.type = kind === 'ko' ? 'sawtooth' : 'sine';
      o.frequency.value = f;
      g.gain.setValueAtTime(0.0001, actx.currentTime);
      g.gain.exponentialRampToValueAtTime(0.05, actx.currentTime + 0.01);
      g.gain.exponentialRampToValueAtTime(0.0001, actx.currentTime + (kind === 'tick' ? 0.07 : 0.18));
      o.connect(g); g.connect(actx.destination);
      o.start(); o.stop(actx.currentTime + 0.2);
    } catch (e) {}
  }

  /* ═══════════════════════════════════════════════════════════
     FIGURES SVG — moteur unique.
     Les figures sont décrites par un "kind" + couleur + options,
     ce qui garantit des formes IDENTIQUES d'un tirage à l'autre
     (aucune déformation possible : géométrie paramétrique fixe).
     ═══════════════════════════════════════════════════════════ */
  const C = {
    ink: '#23282c', grn: '#0a8a3c', amb: '#b58100', red: '#c62828',
    blu: '#1565c0', pur: '#5b3d8f', gray: '#5a656e', teal: '#0d6f78', pink: '#b5317a'
  };
  const PALETTE = [C.grn, C.amb, C.red, C.blu, C.pur, C.teal, C.pink, C.ink];

  function svg(inner, vb = 100) {
    return '<svg viewBox="0 0 ' + vb + ' ' + vb + '" xmlns="http://www.w3.org/2000/svg">' + inner + '</svg>';
  }

  /** Forme élémentaire. kind ∈ liste ci-dessous. color = couleur. opts spécifiques. */
  function shape(kind, color, o = {}) {
    const c = color || C.ink, sw = o.sw || 7;
    const S = { 'stroke': c, 'stroke-width': sw, 'fill': 'none', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' };
    const A = (d) => '<path d="' + d + '" ' + attrs(S) + '/>';
    switch (kind) {
      /* lignes directionnelles (concentration / cut-e) */
      case 'line-up': return svg(A('M10 82 L30 50 L50 66 L72 26 L90 38'));
      case 'line-down': return svg(A('M10 20 L30 52 L50 36 L72 76 L90 64'));
      case 'line-updown': return svg(A('M10 72 L32 30 L52 62 L74 24 L90 48'));
      case 'line-downup': return svg(A('M10 28 L32 70 L52 38 L74 76 L90 52'));
      case 'line-wave': return svg(A('M8 52 Q26 18 44 52 T80 52 T108 52'));
      case 'line-flat': return svg(A('M10 52 L30 44 L50 58 L70 46 L90 55'));
      case 'line-step': return svg(A('M10 78 L32 78 L32 52 L54 52 L54 28 L80 28 L80 14'));
      /* flèches */
      case 'arr-up': return svg('<path d="M50 88 L50 20 M28 42 L50 18 L72 42" ' + attrs(S) + '/>');
      case 'arr-down': return svg('<path d="M50 12 L50 80 M28 58 L50 82 L72 58" ' + attrs(S) + '/>');
      case 'arr-right': return svg('<path d="M12 50 L80 50 M58 28 L82 50 L58 72" ' + attrs(S) + '/>');
      case 'arr-left': return svg('<path d="M88 50 L20 50 M42 28 L18 50 L42 72" ' + attrs(S) + '/>');
      case 'chev-up': return svg(A('M22 66 L50 32 L78 66'));
      case 'chev-down': return svg(A('M22 34 L50 68 L78 34'));
      /* points */
      case 'dot-1': return svg('<circle cx="50" cy="50" r="18" fill="' + c + '"/>');
      case 'dot-2': return svg('<circle cx="30" cy="50" r="15" fill="' + c + '"/><circle cx="70" cy="50" r="15" fill="' + c + '"/>');
      case 'dot-3': return svg('<circle cx="50" cy="26" r="13" fill="' + c + '"/><circle cx="28" cy="68" r="13" fill="' + c + '"/><circle cx="72" cy="68" r="13" fill="' + c + '"/>');
      case 'dot-ring': return svg('<circle cx="50" cy="50" r="30" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/><circle cx="50" cy="50" r="9" fill="' + c + '"/>');
      case 'dot-sq': return svg('<circle cx="50" cy="50" r="32" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/><rect x="36" y="36" width="28" height="28" fill="' + c + '"/>');
      /* cercles / disques */
      case 'circle': return svg('<circle cx="50" cy="50" r="34" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/>');
      case 'disc': return svg('<circle cx="50" cy="50" r="34" fill="' + c + '"/>');
      case 'half-top': return svg('<path d="M16 50 A34 34 0 0 1 84 50 Z" fill="' + c + '"/><circle cx="50" cy="50" r="34" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/>');
      case 'half-left': return svg('<path d="M50 84 A34 34 0 0 1 50 16 Z" fill="' + c + '"/><circle cx="50" cy="50" r="34" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/>');
      case 'quarter': return svg('<path d="M16 50 A34 34 0 0 1 50 16 L50 50 Z" fill="' + c + '"/>');
      /* carrés */
      case 'square': return svg('<rect x="18" y="18" width="64" height="64" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/>');
      case 'square-full': return svg('<rect x="18" y="18" width="64" height="64" fill="' + c + '"/>');
      case 'square-rot': return svg('<rect x="50" y="10" width="56" height="56" transform="rotate(45 50 50)" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/>');
      case 'square-half': return svg('<rect x="18" y="18" width="64" height="64" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/><rect x="18" y="50" width="64" height="32" fill="' + c + '"/>');
      case 'square-diag': return svg('<rect x="18" y="18" width="64" height="64" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/><path d="M18 82 L82 18" ' + attrs({ stroke: c, 'stroke-width': sw }) + '/>');
      /* triangles */
      case 'tri-up': return svg('<path d="M50 16 L86 84 L14 84 Z" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/>');
      case 'tri-down': return svg('<path d="M50 84 L86 16 L14 16 Z" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/>');
      case 'tri-left': return svg('<path d="M16 50 L84 86 L84 14 Z" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/>');
      case 'tri-right': return svg('<path d="M84 50 L16 86 L16 14 Z" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/>');
      case 'tri-full': return svg('<path d="M50 16 L86 84 L14 84 Z" fill="' + c + '"/>');
      /* croix / plus / étoile */
      case 'cross': return svg(A('M22 22 L78 78 M78 22 L22 78'));
      case 'plus': return svg(A('M50 18 L50 82 M18 50 L82 50'));
      case 'star': return svg('<path d="M50 12 L60 40 L90 40 L66 58 L75 88 L50 70 L25 88 L34 58 L10 40 L40 40 Z" ' + attrs({ stroke: c, 'stroke-width': 5, fill: 'none' }) + '/>');
      /* divers */
      case 'moon': return svg('<path d="M62 14 A38 38 0 1 0 62 86 A30 30 0 1 1 62 14 Z" fill="' + c + '"/>');
      case 'diamond': return svg('<path d="M50 14 L86 50 L50 86 L14 50 Z" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/>');
      case 'lshape': return svg(A('M22 20 L22 80 L80 80'));
      case 'zshape': return svg(A('M22 24 L80 24 L22 78 L80 78'));
      /* horloge (test mécanique) */
      case 'clock': {
        const h = ((o.hour || 3) % 12) * 30, m = (o.min || 0) * 6;
        return svg(
          '<circle cx="50" cy="50" r="38" ' + attrs({ stroke: c, 'stroke-width': 5, fill: 'none' }) + '/>' +
          '<line x1="50" y1="50" x2="' + (50 + 20 * Math.sin(h * Math.PI / 180)) + '" y2="' + (50 - 20 * Math.cos(h * Math.PI / 180)) + '" stroke="' + c + '" stroke-width="6" stroke-linecap="round"/>' +
          '<line x1="50" y1="50" x2="' + (50 + 30 * Math.sin(m * Math.PI / 180)) + '" y2="' + (50 - 30 * Math.cos(m * Math.PI / 180)) + '" stroke="' + c + '" stroke-width="4" stroke-linecap="round"/>' +
          '<circle cx="50" cy="50" r="3.5" fill="' + c + '"/>'
        );
      }
      case 'gear': {
        let t = '';
        for (let i = 0; i < 8; i++) {
          const a = i * 45 * Math.PI / 180;
          t += '<rect x="' + (50 + 28 * Math.cos(a) - 5) + '" y="' + (50 + 28 * Math.sin(a) - 5) + '" width="10" height="10" fill="' + c + '"/>';
        }
        return svg('<circle cx="50" cy="50" r="28" ' + attrs({ stroke: c, 'stroke-width': 8, fill: 'none' }) + '/>' + t);
      }
      /* flèche courbe (sens de rotation) */
      case 'rot-cw': return svg('<path d="M22 50 A28 28 0 1 1 50 78" ' + attrs(S) + '/><path d="M50 78 L36 70 M50 78 L38 90" ' + attrs(S) + '/>');
      case 'rot-ccw': return svg('<path d="M78 50 A28 28 0 1 1 50 22" ' + attrs(S) + '/><path d="M50 22 L64 30 M50 22 L62 10" ' + attrs(S) + '/>');
      default: return svg('<rect x="22" y="22" width="56" height="56" rx="8" ' + attrs({ stroke: c, 'stroke-width': sw, fill: 'none' }) + '/>');
    }
  }
  function attrs(o) { return Object.keys(o).map(k => k + '="' + o[k] + '"').join(' '); }

  /** Chiffre 1-9 en SVG, tracé au centre (Switch Challenge). */
  function digitSVG(d, color) {
    const c = color || C.ink;
    return svg('<text x="50" y="72" font-family="JetBrains Mono, monospace" font-size="72" font-weight="700" fill="' + c + '" text-anchor="middle">' + d + '</text>');
  }

  /** Tuile = case de grille pouvant contenir : rien, une forme, un chiffre, une lettre. */
  function tile(spec, size) {
    if (spec == null) return '<div class="mat"></div>';
    const cls = 'mat' + (spec.single ? ' single' : '');
    let inner = '';
    if (spec.type === 'digit') inner = digitSVG(spec.v, spec.color);
    else if (spec.type === 'letter') inner = svg('<text x="50" y="74" font-family="Inter" font-size="66" font-weight="800" fill="' + (spec.color || C.ink) + '" text-anchor="middle">' + esc(spec.v) + '</text>');
    else if (spec.type === 'shape') inner = shape(spec.kind, spec.color, spec.opts);
    else if (spec.type === 'empty') inner = '';
    else if (Array.isArray(spec.cells)) {
      /* matrice 2x2 explicite */
      inner = '<div class="mat">' + spec.cells.map(cs => '<i>' + (cs ? (cs.type === 'shape' ? shape(cs.kind, cs.color) : (cs.type === 'digit' ? digitSVG(cs.v, cs.color) : '')) : '') + '</i>').join('') + '</div>';
    }
    return '<div class="' + cls + '">' + inner + '</div>';
  }

  return { rng, int, pick, shuffle, sample, hash, pct, ms, num, esc, fr, dayKey, daysBetween,
           store, $, $$, el, frag, toast, modal, closeModal, beep,
           shape, svg, digitSVG, tile, C, PALETTE };
})();
