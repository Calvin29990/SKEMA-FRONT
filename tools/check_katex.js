// Validateur KaTeX pour les .md du repo.
// Usage : node tools/check_katex.js fichier.md [autre.md ...]
// Verifie : rendu des blocs $$, rendu des inline $, parite des $,
// et absence des echappements interdits \, \% \& \$ qui cassent le rendu.
// Prerequis : npm i --prefix /tmp katex   (ou KATEX_PATH=... node tools/check_katex.js)
const fs = require('fs');
let katex;
for (const p of [process.env.KATEX_PATH, '/tmp/node_modules/katex', 'katex']) {
  if (!p) continue;
  try { katex = require(p); break; } catch (e) {}
}
if (!katex) {
  console.error("katex introuvable. Installe-le :  npm i --prefix /tmp katex");
  process.exit(2);
}
let total = 0;
for (const f of process.argv.slice(2)) {
  const s = fs.readFileSync(f, 'utf8');
  let err = 0;
  const bad = /\\[,%&$]/g;
  let m;
  while ((m = bad.exec(s))) { console.log(`${f}: ECHAPPEMENT INTERDIT ${m[0]} pos ${m.index}`); err++; }
  const blocks = [...s.matchAll(/\$\$([\s\S]+?)\$\$/g)];
  blocks.forEach((b, i) => {
    try { katex.renderToString(b[1], { throwOnError: true, displayMode: true }); }
    catch (e) { console.log(`${f}: BLOC ${i} KO: ${e.message}`); err++; }
  });
  const t = s.replace(/\$\$[\s\S]+?\$\$/g, '').replace(/`[^`]*`/g, '');
  const inl = [...t.matchAll(/\$([^$\n]+?)\$/g)];
  inl.forEach((b, i) => {
    try { katex.renderToString(b[1], { throwOnError: true }); }
    catch (e) { console.log(`${f}: INLINE ${i} ${JSON.stringify(b[1].slice(0, 40))} KO: ${e.message}`); err++; }
  });
  const n = (s.match(/\$/g) || []).length;
  if (n % 2) { console.log(`${f}: !! NOMBRE DE $ IMPAIR: ${n}`); err++; }
  console.log(`${f}: ${blocks.length} blocs, ${inl.length} inline, ${n} signes dollar, ${err} erreur(s)`);
  total += err;
}
process.exit(total ? 1 : 0);
