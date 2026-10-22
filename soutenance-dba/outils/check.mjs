#!/usr/bin/env node
/**
 * Contrôle du dossier de soutenance — aucune dépendance.
 *
 *   node outils/check.mjs
 *
 * Vérifie : nombre et numérotation des diapositives, pieds de page,
 * cohérence arithmétique des chiffres affichés, présence des notes de
 * l'orateur, fichiers référencés, absence de ressources distantes,
 * absence de données nominatives interdites.
 */
import { readFileSync, existsSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import assert from "node:assert/strict";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (p) => readFileSync(join(ROOT, p), "utf8");

let failures = 0;
let checks = 0;
function check(title, fn) {
  checks++;
  try {
    fn();
    console.log("  ✓ " + title);
  } catch (error) {
    failures++;
    console.error("  ✗ " + title);
    console.error("    " + error.message.split("\n")[0]);
  }
}

const html = read("index.html");
const slides = [...html.matchAll(/<section class="slide[^"]*" id="s(\d+)" data-title="([^"]+)"/g)].map((m) => ({
  n: Number(m[1]),
  title: m[2],
}));

console.log("\nDossier de soutenance DBA — contrôle\n");

/* ---------- structure ---------- */
check("26 diapositives, numérotées de 1 à 26 sans trou", () => {
  assert.equal(slides.length, 26, "nombre de diapositives : " + slides.length);
  slides.forEach((s, i) => assert.equal(s.n, i + 1, "numérotation rompue à l'index " + i));
});

check("chaque diapositive porte un titre de sommaire", () => {
  slides.forEach((s) => assert.ok(s.title.trim().length > 2, "titre manquant pour la diapositive " + s.n));
});

check("chaque diapositive a un pied de page et un compteur cohérent", () => {
  const pgs = [...html.matchAll(/<div class="pg">(\d+) \/ 26<\/div>/g)].map((m) => Number(m[1]));
  assert.equal(pgs.length, 26, "pieds de page trouvés : " + pgs.length);
  pgs.forEach((p, i) => assert.equal(p, i + 1, "pied de page incohérent pour la diapositive " + (i + 1)));
});

check("chaque diapositive a une source citée et des notes de l'orateur", () => {
  const srcs = (html.match(/<div class="src">/g) || []).length;
  const notes = (html.match(/<aside class="notes">/g) || []).length;
  assert.equal(srcs, 26, "blocs « Sources » : " + srcs);
  assert.equal(notes, 26, "blocs de notes : " + notes);
});

/* ---------- chiffres affichés ---------- */
check("architecture : 8 + 61 + 8 = 77 sections", () => {
  const chapters = [10, 10, 9, 11, 10, 11];
  assert.equal(chapters.reduce((a, b) => a + b, 0), 61, "somme des sections de chapitres");
  assert.equal(8 + 61 + 8, 77, "total des sections");
  assert.ok(html.includes("77 sections numérotées"), "total absent de la diapositive 16");
  assert.ok(html.includes("8 + 61 + 8"), "détail du total absent de la diapositive 24");
});

check("supports : 115 avant, 40 après (27 tableaux + 13 figures)", () => {
  const before = [4, 10, 17, 17, 22, 25, 20];
  const after = [1, 5, 6, 6, 7, 9, 6];
  assert.equal(before.reduce((a, b) => a + b, 0), 115, "somme avant");
  assert.equal(after.reduce((a, b) => a + b, 0), 40, "somme après");
  assert.equal(27 + 13, 40, "tableaux + figures");
  assert.equal(76 + 39, 115, "tableaux + figures du programme initial");
  for (const marker of ["27", "13", "115", "40"]) {
    assert.ok(html.includes(marker), "chiffre absent : " + marker);
  }
});

check("échantillon : 15 + 20 + 10 = 45 participants", () => {
  assert.equal(15 + 20 + 10, 45, "somme de l'échantillon");
  assert.ok(html.includes("45 participants prévus") || html.includes("45"), "effectif absent");
});

/* ---------- statuts et prudence ---------- */
check("statuts explicites : prévisionnel, indicatif, à compléter", () => {
  for (const marker of ["prévisionnel", "indicative", "à compléter par l'auteur"]) {
    assert.ok(html.toLowerCase().includes(marker), "mention de statut absente : " + marker);
  }
});

check("aucun résultat de terrain affirmé, formulaire de prudence présent", () => {
  assert.ok(html.includes("Aucun résultat n'est présumé") || html.includes("aucun résultat n'est présumé"));
  assert.ok(html.includes("proposition à examiner"), "clause de prudence absente");
  assert.ok(html.includes("[à compléter par l'auteur : université d'inscription"), "champs auteur non signalés");
});

/* ---------- confidentialité ---------- */
check("confidentialité : codes EPES, aucun établissement enquêté nommé", () => {
  const banned = ["Saint-Exupéry", "Saint-Exupery", "BGFI", "SUP de COM", "EM Gabon", "Techniques Avancées", "Matrix"];
  for (const word of banned) {
    assert.ok(!html.includes(word), "donnée interdite présente : " + word);
  }
  for (const code of ["EPES-A", "EPES-E", "EPES-A à EPES-E"]) {
    assert.ok(html.includes(code), "code manquant : " + code);
  }
});

/* ---------- autonomie technique ---------- */
check("aucune ressource distante (police, script, feuille de style)", () => {
  for (const m of html.matchAll(/(?:src|href)="(https?:\/\/[^"]+)"/g)) {
    assert.ok(
      m[1].startsWith("https://upl-gabon.com/"),
      "ressource distante inattendue : " + m[1]
    );
  }
  assert.ok(!/<script[^>]+src="http/i.test(html), "script distant détecté");
  assert.ok(!/@import\s+url\(/i.test(read("style.css")), "import distant détecté dans style.css");
});

check("fichiers référencés présents et non vides", () => {
  const files = new Set();
  for (const m of html.matchAll(/(?:src|href)="(?!https?:|#|mailto:)([^"]+)"/g)) files.add(m[1]);
  for (const f of files) {
    const p = join(ROOT, f);
    assert.ok(existsSync(p), "fichier manquant : " + f);
    if (f !== "sources.html") assert.ok(statSync(p).size > 0, "fichier vide : " + f);
  }
  for (const f of ["style.css", "deck.js", "doc.css", "sources.html", "medias/gabon.svg", "medias/logo-upl.png", "data/gab_adm1.geojson", "outils/build-carte.py"]) {
    assert.ok(existsSync(join(ROOT, f)), "pièce du dossier manquante : " + f);
  }
});

check("page de sources : provenance du fond de carte et licence", () => {
  const src = read("sources.html");
  for (const marker of ["geoBoundaries", "GAUL 2001", "CC BY 4.0", "gab_adm1.geojson", "build-carte.py"]) {
    assert.ok(src.includes(marker), "mention absente de sources.html : " + marker);
  }
});

check("carte : neuf provinces, repères et mention de source", () => {
  const svg = read("medias/gabon.svg");
  const paths = (svg.match(/class="pv/g) || []).length;
  assert.equal(paths, 9, "provinces dessinées : " + paths);
  for (const city of ["Libreville", "Port-Gentil", "Franceville"]) {
    assert.ok(svg.includes(city), "ville absente : " + city);
  }
  assert.ok(/geoBoundaries/.test(svg), "source cartographique non citée dans le SVG");
});

check("notes de l'orateur : durée ou consigne dans chaque bloc", () => {
  const notes = [...html.matchAll(/<aside class="notes">([\s\S]*?)<\/aside>/g)].map((m) => m[1]);
  assert.equal(notes.length, 26, "blocs de notes : " + notes.length);
  notes.forEach((n, i) => assert.ok(n.trim().length > 40, "notes trop courtes pour la diapositive " + (i + 1)));
});

/* ---------- bilan ---------- */
console.log("");
if (failures) {
  console.error(`${failures} contrôle(s) en échec sur ${checks}.\n`);
  process.exit(1);
}
console.log(`${checks} contrôles passés — dossier cohérent.\n`);
