# SKEMA-Training — plateforme personnelle d'entraînement

> **Usage strictement personnel — Calvin MINANG.** Ne pas diffuser, ne pas publier, ne pas partager le dossier.
> Aucune donnée ne quitte le navigateur : tout est stocké en local (`localStorage` + `IndexedDB`).

---

## 1. Lancer la plateforme

Aucune installation, aucune dépendance :

```bash
cd skema-training
python3 -m http.server 8080 --bind 0.0.0.0
# puis ouvrir http://localhost:8080
```

Les données de progression sont attachées à l'origine (`http://localhost:8080`) : gardez toujours le même port pour retrouver votre historique.

---

## 2. Ce que contient la plateforme

Accueil à **6 onglets de familles** (Tous · Anglais · Raisonnement · Attention & mémoire · Comportement · Examen) et **13 sections + 1 simulation complète**.

| Section | Type de banque | Volume | Fidélité au dossier SKEMA |
|---|---|---|---|
| Verbal Reasoning | **figée** | 12 passages × 3 affirmations = 36 items | True / False / Cannot say, passages en anglais, aucune réponse hors texte |
| English Battery ∞ | **illimitée** | généré à la demande (40 items/run par défaut) | Même format, passages inédits : cible **50 réponses exactes** |
| Numerical Reasoning | **figée** | **Paper A = 48 items** / **Paper B = 37 items** | Tableaux de données, 4 options, calculatrice, ~75 s/item |
| Déductif | figée | 12 matrices | Règles forme / couleur / position / remplissage |
| Deductive Switch Challenge | figée | 30 séries | Combinaisons d'échanges à retrouver |
| Inductif | figée | 30 séries | Rotation, nombre, remplissage, couleur |
| Concentration | figée | 60 paires | Identiques / différentes, **2,5 s** par paire |
| Learning Efficiency | figée | 20 planches | Grille 5×5, cases qui clignotent, temps décroissant (9 s → 5 s) |
| Mémoire de travail | figée | 15 planches | Grille 5×5, restitution sans indice |
| Traitement de l'information | figée | 18 items | Valeur de l'information, espérance, bornes binaires |
| Raisonnement mécanique | figée | 24 items | Engrenages, courroies, poulies, leviers, ressorts (scènes SVG paramétriques) |
| Comportement professionnel | figée | 36 affirmations | Échelle de fréquence 4 points, **aucune bonne réponse** |
| Motivation & intérêts | figée | 30 items | Échelle d'intérêt 4 points |
| **Simulation complète** | mixte | ~136 questions | Enchaînement type examen, chrono, mode strict |

Deux modes de fonctionnement :
- **Entraînement** — feedback immédiat, correction détaillée, chrono visible ;
- **Examen** — feedback en fin de session, mode strict, chrono par item (réglable par section).

Raccourcis clavier : `1-4` répondre · `Entrée` valider · `Espace` item suivant.

---

## 3. Fidélité des questions et des figures

- **Banques figées** : le contenu est *identique à chaque session* (pas de tirage aléatoire du contenu). Ce que vous mesurez est donc votre **régularité**, pas la chance — exactement comme à l'examen.
- **Figures** : elles sont générées par un moteur géométrique paramétrique unique (`U.shape`). Une forme donnée a toujours exactement la même géométrie, la même épaisseur de trait et les mêmes proportions : **aucune déformation, aucun recadrage, aucune ré-échelle entre deux sessions**. Les couleurs viennent d'une palette fixe (`U.PALETTE`).
- **Batterie anglaise illimitée** : le *style*, la *longueur*, le *vocabulaire sectoriel* et la *logique des réponses* (1 vraie, 1 fausse, 1 impossible à dire) sont invariants ; seules les valeurs (pourcentages, montants, périodes, villes) sont tirées au sort. Aucune ambiguïté n'est possible : un item est rejeté s'il ne contient pas exactement une réponse de chaque type.
- **Captures originales** : l'onglet `Captures` importe **telles quelles** vos captures d'écran du document Drive (`DOC IMPORTANT base Entretien front.docx`) — stockage binaire sans retouche, sans redimensionnement, sans recadrage. Elles servent de référence visuelle à côté des exercices.

---

## 4. Modifier ou étendre les banques (sans casser la fidélité)

| Fichier | Rôle |
|---|---|
| `assets/js/banks.js` | Contenu **figé** : passages verbaux, matrices déductives, affirmations comportementales, motivation, mécanique, valeur de l'information |
| `assets/js/drills.js` | Générateurs déterministes : numerical (48 items), inductif, concentration, learning, switch, mémoire + moteur de la batterie anglaise illimitée |
| `assets/js/core.js` | Registre des sections, moteurs de session, progression, feedback |
| `assets/js/app.js` | Routeur et vues (Accueil, Section, Progression, Feedback, Captures, Réglages) |

### Ajouter un item figé (exemple : verbal)

```js
// dans banks.js → const verbal = [ … ]
{
  id: 'V13', theme: 'Mon thème',
  passage: 'Texte du passage…',
  q: [
    { s: 'Affirmation vraie.',  a: 'true',       w: 'Justification visible après réponse.' },
    { s: 'Affirmation fausse.', a: 'false',      w: 'Justification.' },
    { s: 'Hors du texte.',      a: 'cannot say', w: 'Justification.' }
  ]
}
```
Chaque item doit conserver **1 vraie / 1 fausse / 1 impossible à dire** par passage (règle de fidélité).

### Remplacer le contenu par les questions exactes du document source

Le moteur est *data-driven* : il suffit de remplacer les tableaux de `banks.js` (et les items de `numericalFixed()` dans `drills.js`) par les questions d'origine, en conservant le schéma `{ id, q, options|opts, ans, why, time }`. Aucune modification du moteur n'est nécessaire.

---

## 5. Progression

Onglet `Progression` : sessions, précision, heatmap 30 jours, tendance par section, barres d'objectif (dont **50 réponses exactes** sur la batterie anglaise).
Onglet `Feedback` : analyse automatique (sections fragiles, régularité des temps, plan d'action daté jusqu'au 7-9 octobre) et **journal des erreurs** avec la bonne réponse et l'explication.
Onglet `Réglages` : son, clavier, chrono, mode de feedback par défaut, objectif, **export/import JSON**, réinitialisation.

---

## 6. Notes

- Interface en français, contenu des tests en anglais (comme à l'examen) pour le verbal.
- Les tests Maki/cut‑e sont chronométrés au niveau du test entier : entraînez-vous à ne jamais dépasser le temps par item indiqué dans chaque section.
- Ce dossier est un espace d'entraînement : **ne jamais publier ce contenu**, il est réservé à un usage individuel.
