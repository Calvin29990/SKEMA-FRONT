# Assessment Trainer — v4.6 · Aon/cut-e et modules bancaires

Plateforme personnelle d'entraînement aux tests d'aptitude utilisés dans les processus
de sélection. Elle conserve les **14 tâches de base Aon / cut-e** et ajoute 13 modules
BNP Paribas, UBS et Morgan Stanley. Les documents de référence servent à reprendre les
formats, durées et mécaniques ; toutes les questions, données et grilles d'entraînement
sont originales.

> ⚠️ **Contenu 100 % original.** Les textes, énoncés, tableaux et grilles sont générés ou
> rédigés pour cette plateforme. Aucun item de test réel n'est reproduit. Usage strictement
> personnel — Calvin MINANG.

## Les 14 tâches de base Aon / cut-e

| # | Tâche | Durée | Ce qui est reproduit |
|---|-------|-------|----------------------|
| 1 | Comportements professionnels | 18 min | 48 blocs × 3 affirmations, 6 points à répartir sur 6 cercles, sans chrono |
| 2 | Motivations et Intérêts Professionnels | 18 min | 36 blocs, même mécanique de points |
| 3 | Raisonnement numérique | 15 min | 37 affirmations TRUE/FALSE/CANNOT SAY, 6 feuilles de données **navigables librement**, 12:00, exemples ×3 |
| 4 | Raisonnement verbal | 15 min | 49 affirmations, 6 fiches de textes, 12:00, exemples ×3 |
| 5 | Pensée logique déductive | 9 min | grille 4×4, 1 case « ? », 4 options, 6:00, avance automatique + retour vert/rouge |
| 6 | Raisonnement Inductif | 9 min | « Ces deux grilles suivent une règle » + 4 candidats, exactement 2 à choisir (▶▶), 6:00 |
| 7 | Capacité de Concentration | 5 min | « E + exactement 3 points » : incorrect / correct (touches A et D), exemple 30 s puis 2:00 |
| 8 | Capacité multi-tâches | 8 min | jugement lettre/chiffre en alternance, **5:00** (scales mt) |
| 9 | Capacité d'apprentissage | 9 min | 6 sections : 12 objets mémorisés puis replacés dans l'ordre, pauses de 6 s, chrono global **5:00** |
| 10 | Traitement de l'information | 18 min | boîte de réception, directives de priorité (HIGH/MEDIUM/LOW) et actions, 15:00, mails en cours de test |
| 11 | Compétences Linguistiques - Anglais | 13 min | 3 sections : aisance (4:00), vocabulaire (4:00), orthographe (2:00), « ? » neutre |
| 12 | Compétences Linguistiques - Français | 13 min | mêmes 3 sections, en français |
| 13 | Raisonnement Mécanique | 18 min | 24 items, 3 options, 15:00, navigation ‹ ▦ › |
| 14 | Raisonnement Déductif - switchChallenge | 9 min | machine à codes, 3 codes proposés, niveaux, 6:00 |

## Chronomètres (durées officielles des tests)

Les durées de test sont celles des formats Aon / cut-e correspondants ; la durée affichée sur
l'accueil (colonne « Durée ») est celle du document de référence, qui inclut les consignes et
les exemples non notés (~3 min).

| Épreuve | Test | Chrono |
|---|---|---|
| Raisonnement numérique | scales numerical : 37 tâches | 12:00 |
| Raisonnement verbal | scales verbal : 49 tâches | 12:00 |
| Pensée logique déductive | scales lst / gapChallenge | 6:00 |
| Raisonnement Inductif | scales clx : 2 grilles + choisir 2 sur 4 | 6:00 |
| Capacité de Concentration | scales e3+ : E + exactement 3 points | exemple 0:30 puis 2:00 |
| Capacité multi-tâches | scales mt | 5:00 |
| Capacité d'apprentissage | learning efficiency : 6 sections (12 objets + 30 s + 6 s) | 5:00 |
| Traitement de l'information | boîte de réception (consignes du document) | 15:00 |
| Anglais / Français | scales lt : 3 épreuves (aisance, vocabulaire, orthographe) | 4:00 + 4:00 + 2:00 |
| Raisonnement Mécanique | scales mtu : 24 tâches | 15:00 |
| switchChallenge | scales switchChallenge | 6:00 |
| Comportements / Motivations | questionnaires de personnalité | aucune limite |

## Utilisation

- Ouvrir `standalone/index.html` (fichier autonome, aucune dépendance externe) ou le dossier
  publié `docs/` — le lien htmlpreview du README racine pointe sur le standalone.
- L'accueil liste les 14 tâches avec leur durée et un bouton **Début** ; chaque test enchaîne
  consignes → exemples non notés → test chronométré → écran de fin.
- **Barre d'onglets** sous la barre rouge : *Tâches à accomplir · Progression · Feedback · Aide & réglages*
  (l'onglet suit la page ouverte ; le menu ≡ reste disponible).
- **Feedback en français** : filtre par épreuve, relecture question par question (votre réponse,
  bonne réponse, explication, temps), « Refaire cette épreuve », export CSV par session.
- **Chronomètres standards** sur toutes les épreuves sauf les deux questionnaires de personnalité
  (comportements, motivations) qui restent sans limite de temps, conformément au document.
- **Feuilles de données / fiches de textes** (numérique, verbal) : les onglets restent sous votre
  contrôle — **le contenu suit l'onglet choisi** (cliquer *Outlook* affiche bien le graphique
  FY 8 / FY 9, la question restant affichée). Par défaut chaque question ouvre sa propre feuille ;
  dès que vous choisissez une feuille, ce choix est conservé d'une question à l'autre.
- **Exemples → chrono explicite** : pendant les exemples, une note rappelle que le chrono du test
  (12:00 pour le numérique) ne démarre qu'après le 3ᵉ exemple ; les exemples ont été accélérés
  (~1,8 s chacun) pour un passage immédiat au test réel.
- **Langue** : par défaut **toute l'épreuve s'affiche en anglais** (consignes, énoncés,
  true / false / cannot say, « Data sheets », e-mails, items de mécanique, blocs de personnalité) ;
  l'habillage — accueil, progression, feedback, aide — reste en français. Les deux tests de
  langues conservent leur langue de contenu. Réglage **épreuve par épreuve** dans *Aide & réglages*.
- **Banques de personnalité complètes et bilingues** : comportement 48 blocs × 3 = **144 énoncés**,
  motivation 36 blocs × 3 = **108 énoncés**, en français et en anglais — plus aucun bloc vide.
- **Jamais à court de questions** : anglais et français (aisance, vocabulaire, orthographe)
  enchaînent la banque des captures puis des **questions similaires générées à l'infini** ;
  la boîte de réception reçoit des e-mails sans fin ; déductif, inductif, concentration,
  multi-tâches et switch génèrent leurs items à la volée (toujours des questions nouvelles).
- Numérique / verbal / mécanique : bouton **Terminer** dès que tout est répondu (pas besoin
  d'attendre la fin du chrono) ; navigation ‹ ▦ › et grille de questions.
- **Retour immédiat (v4.3)** : après chaque réponse, un panneau d'explication (`.ifb`) indique
  **✔ Correct / ✘ Incorrect**, la réponse attendue, **POURQUOI** (explication détaillée +
  figures visuelles : grilles, machine à codes, E + points, comparaison des 12 objets,
  accès direct à la feuille de données) et un bouton **Continuer ›** (désactivable dans
  *Aide & réglages* pour retrouver la cadence d'examen).

## Données & confidentialité

Tout est stocké localement (`localStorage`), par profil : historique horodaté, détail
question par question (export CSV par session), export/import JSON complet. Aucune requête
réseau n'est émise par la page — vérifié par le harnais de conformité.

## Développement

```
skema-training/
  index.html              page hôte (barre rouge SKEMA, menu, vues)
  assets/css/styles.css   habillage et composants des épreuves
  assets/js/util.js       utilitaires (rng, store, toast, modale, formes SVG)
  assets/js/banks.js      banques de contenu original (textes, énoncés, grilles, mails…)
  assets/js/ubs.js        contenus fictifs et données des 3 modules UBS
  assets/js/drills.js     générateurs déterministes + banque numérique + graphiques
  assets/js/core.js       registre des épreuves, moteur de session, scoring
  assets/js/app.js        routeur, accueil, progression, feedback, réglages, import/export
  build.py                génère standalone/index.html, docs/ et le ZIP hors-ligne
  tools/tests/conform.js  harnais de conformité (Chromium headless, 241 contrôles)
```

```bash
cd skema-training
python3 build.py                       # régénère standalone/ + docs/ + ZIP
NODE_PATH=… node tools/tests/conform.js   # 241 contrôles de conformité
```

Le harnais vérifie : les 14 lignes de l'accueil (libellés + minutes), l'ouverture de chaque
épreuve sans erreur JS, les durées et compteurs, les mécaniques d'interaction (points,
skips, retours vert/rouge, « ? » neutre), les flux de sections, l'enregistrement des
sessions, l'absence de requête externe et le rendu mobile 390 px. Il contrôle aussi les
ajouts v4.1 (chrono global de l'apprentissage, navigation libre entre les feuilles de
données, réserves inépuisables, barre d'onglets, feedback en français), les correctifs
v4.2 (contenu réellement lié à l'onglet choisi, feuille par défaut = question posée,
choix mémorisé, note « le chrono démarre après les exemples » + décompte vérifié 12:00 → 11:59,
anglais par défaut avec réglage épreuve par épreuve, et banques de personnalité complètes
144 + 108 énoncés, FR et EN, aucun bloc vide) et le retour immédiat v4.3 sur les 14 épreuves.

## Modules bancaires (v4.6) — BNP Maki, UBS, Morgan Stanley

13 sections supplémentaires, regroupées sur l'accueil sous trois en-têtes. Les captures
fournies servent à caler les formats et les durées ; les énoncés, tableaux, scénarios et
grilles de ce trainer restent **originaux et fictifs** (aucun item du test réel n'est copié).

| Groupe | Modules d'entraînement | Sources de format |
|---|---|---|
| **BNP Paribas — Maki** | numérique 9 q./10 min · logique 13 q./8 min · résolution de problèmes 10 q./10 min · SJT 13 q./10 min · attention aux détails 10 q./12 min | psychotechniquetest.fr/bnp-paribas · test-banque.fr/bnp-paribas · Glassdoor (process CIB stagiaires) |
| **UBS — Online Assessment** | **Numérique** : 18 q./6 min, 6 feuilles ; **Culture Match** : 18 scénarios, ~20 min sans chrono, choix « plus/moins efficace » ; **Inductif** : 2 grilles modèles + choisir 2 candidates, 6 min | captures des documents UBS fournis pour cette session ; contenu du trainer entièrement original |
| **Morgan Stanley — OA** | SHL : numérique 18 q./25 min · verbal 30 q./19 min · inductif 24 q./25 min ; Aon EMEA : switchChallenge + SJT chat 13 q./10 min | forgeprep.io · careertestprep.com · preplounge.com · gameassessmentprep.com |

Les trois modules UBS ont des consignes FR/EN, une mécanique dédiée pour le choix « Most /
Least effective », six tableaux/visualisations numériques fictifs et des grilles inductives
générées. Les résultats Culture Match sont indicatifs pour l'entraînement, pas une notation
officielle UBS.

Test de conformité : `node skema-training/tools/test-banks.js` (charge les vrais scripts,
vérifie le catalogue, les durées et banques UBS, démarre chaque section et contrôle la
non-régression des 14 épreuves d'origine).
