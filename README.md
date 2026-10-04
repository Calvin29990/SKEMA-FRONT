# SKEMA-FRONT — Workspace Calvin MINANG

> **Pour Arena** : Ce README est ton point d'entrée. Chaque dossier a un objectif précis.
> Lis le dossier concerné avant de travailler.

---

## 📂 NAVIGATION RAPIDE

| Dossier | Contenu | Quand l'utiliser |
|---|---|---|
| `candidatures/` | Suivi candidatures banques, debriefs, notes Arena | Candidatures, entretiens, runbooks |
| `SKEMA-DOSSIER-ARCHIVE.md` | **Dispute financière SKEMA** (bourse ANBG, €7,500) | Problème SKEMA / titre de séjour |
| `cours/` | Cours S1 + S2 M2 CFM, syllabus, lectures | Devoirs, examens, révisions |
| `exercices/` | Exercices Excel, CFP, comptabilité | Pratique cours |
| `entretien/` | Questions entretien, fiches, guides (Jane Street, Optiver) | Préparation entretiens banques |
| `livres/` | 35+ livres de finance (options, quant, fixed income...) | Recherche, approfondissement |
| `documents/` | CV, Portfolio, conventions de stage, LinkedIn | Candidatures, admin |
| `planning/` | Emploi du temps, notes globales, plan S5 | Organisation semaine |
| `esg/` | Matrices ESG, données publiques | Cours/projets ESG |
| `bnp-training/` | **Plateforme entraînement BNP Maki** (clone pixel-perfect) | Prep test BNP 7-9 octobre |
| `skema-training/` | **Assessment Trainer v4.5** — 14 tâches format Aon/cut-e + 13 modules bancaires (BNP Maki, UBS, Morgan Stanley) | Prep MS / Aon / cut-e / Maki (restauré de l'historique, commit `f5d6f2a`) |
| `audits/` | Audit de fidélité du trainer (02/10) | Avant de s'appuyer sur skema-training |
| `scratch/` | Fichiers temporaires / archives | Nettoyage |

---

## 🏦 Assessment Trainer v4.5 — styles distincts par banque (04/10/2026)

Le trainer (`skema-training/`, publié via `docs/`) passe en v4.5 : chaque banque a désormais
son propre style, et le SJT Morgan Stanley est en mode messagerie comme le vrai chatAssess.

- **Morgan Stanley — chatAssess façon WhatsApp** (fini les blocs Aon) : fenêtre de messagerie
  bleu moderne (en-tête dégradé « Morgan Stanley — Recruitment », avatar, statut « en ligne /
  écrit… »), les 13 scénarios arrivent comme des **messages reçus** (bulles blanches), les
  réponses partent comme de vrais messages (bulles bleues, ✓✓, horodatage). **À la fin : message
  avec le lien vers le test suivant** (« 🔗 Évaluation suivante : Numerical Reasoning ») qui
  lance réellement `ms-num`, comme dans le process décrit par les candidats (Wall Street Oasis :
  « responding to messages of colleagues in fake scenarios using a chat feature »).
- **BNP — style Maki** (pas Aon) : thème blanc/rouge `#ce0f2e`, cartes et boutons arrondis.
- **UBS** : thème blanc/rouge vif `#ec0000` ; **Culture Match corrigé à 18 scénarios**
  (au lieu de 24) d'après les retours candidats (« 18 scenario-based questions », déc. 2024).
- Technique : thèmes via `body[data-bank]` (variables `--red/--red-d/--red-bg` déjà centralisées) ;
  nouveau kind `chatsjt` + `renderChat` dans `core.js` ; réponses du chat loggées sans champ `ok`
  → `finish()` les agrège comme un questionnaire comportemental ; bouton « Test suivant » sur
  l'écran de résultats ; crochets de test `__render/__beginRun/__chat`.
- **Vérifier** : `node skema-training/tools/test-banks.js` (124 contrôles, y compris le flux chat
  complet 13 réponses) · **Publier** : `python3 skema-training/build.py` (régénère `docs/` +
  `standalone/index.html`).

---

## 🔥 PRIORITÉS ACTUELLES (03/10/2026)

### 0. Semaine 03 → 13/10 — 3 tests restants + midterm Corp Val du ven. 09/10
- **Fichier** : `planning/DEADLINES-VERIF-2026-10-03.md` (limites, buffers −24 h, verdict pause samedi)
- **Prompt Gemini prêt à l'emploi** : `planning/PROMPT-GEMINI-2026-10-03.md`
- À passer cette quinzaine : **UBS** (limite jeu. 08/10 ≈ 16:09, retake interdit → visé dim. 04/10) ·
  **BNP Maki** (ultime 13/10, « pas avant le 7 » → visé sam. 10/10). **Morgan Stanley = RÉSERVÉ**
  (48 h expirées ≈ 16/08 ; le passer maintenant verrouille 6 mois → gardé pour le prochain off-cycle,
  prep via `skema-training/`). Séquence espacée pour recevoir la décision avant le test suivant quand
  c'est possible : détails dans `planning/DEADLINES-VERIF-2026-10-03.md` §0.
- **Midterm Corporate Valuation : ven. 09/10** (20 MCQ, 30 min, sessions 1-3 — annonce K2 du 29/09).
- Le calendrier K2 de la semaine 05-11/10 + l'annonce du midterm sont transcrits dans
  `planning/DEADLINES-VERIF-2026-10-03.md` §1bis (captures fournies en chat le 03/10 ; images non
  stockables dans le sandbox). Le `planning/EMPLOI DU TEMPS VALIDE.pdf` reste l'EDT **Université de
  Lille de Cléanne MINANG** — toujours pas l'EDT SKEMA S5.

## 🔥 PRIORITÉS PRÉCÉDENTES (30/09/2026)

### 1. SKEMA — Dispute financière (URGENT)
- **Fichier** : `SKEMA-DOSSIER-ARCHIVE.md`
- **Situation** : SKEMA réclame €7,500. La bourse ANBG couvre 2 ans (M1+M2). SKEMA n'a facturé qu'1 an.
- **Action en cours** : Mail à la Direction Générale (Alice Guilhon) — demain 8h30
- **Titre de séjour** : expire 30/01/2027 — certificat S5 indispensable
- **Ne pas** : menacer avocat en premier contact, dire "SKEMA cares about image", "je quitte SKEMA"

### 2. BNP Paribas — Test Maki (7-9 octobre)
- **Fichier** : `bnp-training/index.html`
- **Contrainte** : One shot only. Blacklist si échec. Pas avant le 7, pas après le 13/10.
- **Plateforme** : Maki People (PAS AON). Training en cours pour clone pixel-perfect.

### 3. Candidatures banques
- **Fichier** : `candidatures/TRACKING-CANDIDATURES-2026-2027.md`
- Barclays Off-Cycle Sales Paris 2027 — Under Consideration (referral Olivier Moser)
- Barclays Graduate Banking Paris 2027 — Under Consideration
- Crédit Agricole CIB — test AON reçu, code `b6x-kkd-ssr`

---

##  STRUCTURE DÉTAILLÉE

### `cours/` — Cours M2 Corporate Financial Management

| Sous-dossier | Matière | Contenu |
|---|---|---|
| `S1_FRA/` | Financial Reporting & Analysis | 6 readings (HBS, IMF, PwC, IFRS, Latham Watkins) |
| `S1_CF/` | Corporate Finance | Sessions, corrigés, syllabus FRA |
| `S1_MoneyBanking/` | Money, Banking & Financial Markets | Prerequisites, microeconomics |
| `S2_CorpVal/` | Corporate Valuation Methods | Sessions 1-2, exercices, student copies |
| `S2_CapitalStructure/` | Capital Structure & Dividend Policy | Session 2, exercices |
| `SustainableFinance/` | Sustainable Finance & Impact Investing | Module 1, fiche cours |
| Racine `cours/` | Syllabus | 4 syllabus (CorpFin, CorpVal, FRA, MoneyBanking) |

### `exercices/`

| Sous-dossier | Contenu |
|---|---|
| `Excel/` | Warm-up, Time Value of Money, Financial market notions |
| `CFP/` | Corporate Finance Prerequisites (exercices + solutions) |
| `Comptabilite/` | Accounting prerequisites, balance sheet exercises |
| Racine `exercices/` | Exercices divers (Ex 1-7) |

### `entretien/` — Préparation entretiens banques

- `Questions FX - question approfondie à envoyer.docx`
- `Questions Produits dérivés.docx`
- `Questions produits structurés.docx`
- `Fiche Produits Structurés.docx`
- `Questions greeks.docx`
- `Questions de base.docx`
- `Questions d'actualités.docx`
- `Questions générales stage.docx`
- `Questions-SG.docx`
- `FICHE-ENTRETIEN.docx`
- `Jane Street Guide.pdf`, `Optiver Guide (2023).pdf`
- `Glassdoor Quant Trader Interview Questions.txt`

### `livres/` — 35+ références finance

Quant : *Heard on The Street*, *A Practical Guide To Quant Finance Interviews*, *Quant Job Interview Questions*, *Fifty Challenging Problems in Probability*, *A Collection of Dice Problems*

Options/Dérivés : *Exotic Options Trading* (de Weert), *Foreign Exchange Option Pricing* (Clark), *Pricing Barrier Options*, *The Volatility Surface* (Gatheral), *Equity Derivatives Explained* (Bouzoubaa), *Advanced Equity Derivatives* (Bossu/Carr), *Convertible Arbitrage*

Fixed Income : *Fixed Income*, *Securities Finance* (Fabozzi), *The Repo Handbook* (Choudhry), *Managing Liquidity in Banks* (Duttweiler), *Liquidity Risk* (Banks), *Asset and Liability Management* (Corlosquet-Habart)

Commodities : *Cotton Trading Manual* (Townsend), *Wasde Soft Commo report*

Math : *Matrix Cookbook*, *Arbitrage-free smoothing implied volatility surface*

---

## 📁 FICHIERS CLÉS

| Fichier | Usage |
|---|---|
| `SKEMA-DOSSIER-ARCHIVE.md` | TOUT le dossier SKEMA (argument, preuves, stratégie, contacts) |
| `candidatures/TRACKING-CANDIDATURES-2026-2027.md` | Audit candidatures (blacklist, retake policies) |
| `bnp-training/index.html` | Clone plateforme BNP Maki (test 7-9 octobre) |
| `documents/CV_Calvin_MINANG.pdf` | CV à jour |
| `documents/Portfolio_Calvin_MINANG.pdf` | Portfolio |

---

## ️ RÈGLES

1. **Ne jamais** commiter de données sensibles (mots de passe, tokens, credentials)
2. **BNP training** : repo privé, entraînement Calvin uniquement, à supprimer après validation du test
3. **SKEMA dispute** : ton factuel et professionnel. Avocat = dernier recours seulement
4. **Candidatures** : toujours vérifier le tracking avant de postuler (blacklist, retake policies)
