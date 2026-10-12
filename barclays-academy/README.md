# 🎯 BARCLAYS ACADEMY — Briefing de mission (v1)

**Owner** : Calvin MINANG · **Créé le 12 octobre 2026** · **Cible : Londres uniquement**
**Deadline critique : assessment SHL Barclays — à passer le 13 octobre au plus tard**

---

## 0. Le préambule (à relire avant chaque session)

Deux ans de travail sans relâche pour intégrer SKEMA. Le process de recrutement a été **négligé par arrogance** — c'est reconnu, c'est écrit, c'est terminé. À partir d'aujourd'hui :

> **On ne se présente plus à un test sans y avoir été entraîné. Un test passé sans préparation est une candidature brûlée.**

Ce document organise la riposte : une plateforme d'entraînement **Barclays-only**, alimentée par **tes données réelles** (que tu vas me communiquer), avec un objectif unique — rendre tes tests parfaits.

| Actif | Statut |
|---|---|
| Barclays Banking GP 2027 London | 🟡 Assessment SHL à passer (dead. 16 oct) |
| CACEIS Luxembourg | 🟡 Call RH ven. 16 oct 10h — plan concret, à garder au chaud |
| HSBC S&T Off-Cycle London | 🟡 Immersive Assessment à passer (~15 oct) |
| BNP London GM Sales | 🟡 Test maptq/Talent Q à passer (~14 oct) |
| Deutsche Bank IBCM London | 🟢 En cours (assessment fait, rapport reçu) |

**Ordre de priorité des 7 prochains jours : Barclays SHL > tout le reste.**

---

## 1. 📥 Les données que Calvin va communiquer (NEXT STEP)

La plateforme sera construite sur **tes données réelles**, pas sur des suppositions. Dès que tu les envoies, je construis les modules correspondants. La spécification exacte des fichiers est dans **[`data/INPUT-DATA-SPEC.md`](data/INPUT-DATA-SPEC.md)**. En résumé :

| Dataset | Contenu | Priorité |
|---|---|---|
| `shl_sessions.csv` | Chaque mock/practice SHL : date, section, nb questions, bonnes réponses, temps moyen/question | 🔥 Immédiat |
| `error_log.csv` | Chaque erreur : type (numérique/déductif/inductif), cause (calcul, lecture, temps, panique), question source | 🔥 Immédiat |
| `sjt_responses.csv` | Scénarios RISES : ta réponse vs réponse attendue, justifications | 🟠 Semaine 1 |
| `english_daily.csv` | 60 min/jour : input (FT/Bloomberg), output (enregistrements), vocab SRS appris | 🟠 Semaine 1 |
| `report_db_feedback.md` | Le rapport DB (fait ✅) : Analysis + Curiosity = axes de drill | ✅ Fait |
| Captures d'écran des tests | Format réel des questions SHL Barclays (anonymisées) | 🔥 Immédiat |

**Règle de collecte** : pendant les 7 prochains jours, chaque session de practice = 1 ligne dans le CSV + screenshot des questions manquées. Pas de session sans trace.

---

## 2. 🏗️ La plateforme — spécification (Barclays ONLY)

### Module M1 — Simulateur SHL Verify Interactive (cœur du système)
- **3 batteries** : numérique (tables/graphes/%/croissance), déductif (planification d'agenda, logique), inductif (patterns)
- **Timer réaliste** : ~90 s/question, format interactif (drag & drop), pas de retour arrière
- **Analytics** : score par sous-type, courbe de progression, détection des patterns d'erreur récurrents (ex. : « erreurs de base de calcul après la question 15 »)
- **Cible de perfection** : ≥ 85 % de précision à ≤ 80 s/question sur 3 sessions consécutives

### Module M2 — Values & Mindset (OPQ32, triplets)
- Banque de triplets de statements (« most like me / next like me »)
- **Score de cohérence** : le piège n°1 est de se contredire entre items recoupés. La plateforme détecte tes incohérences internes
- Stratégie : honnêteté disciplinée — on définit TON profil (les 3 forces DB : Collaboration, Detail, Personal Responsibility + résorption Analysis/Curiosity) et on vérifie que chaque triplet est traité dans le même référentiel

### Module M3 — SJT RISES
- Scénarios de bureau Barclays avec 4 options, à classer
- Chaque scénario est mappé sur **R**espect, **I**ntegrity, **S**ervice, **E**xcellence, **S**tewardship
- La plateforme t'apprend la hiérarchie de décision Barclays : Integrity > remontée > action > efficacité brute

### Module M4 — English for Finance (complexification sérieuse)
Voir section 4.

### Phases de construction
| Phase | Contenu | Quand |
|---|---|---|
| **v0 (cette semaine)** | Feuille CSV + drills manuels chronométrés + revue d'erreurs quotidienne avec moi | Immédiat |
| **v1 (semaine prochaine)** | Web app : timers, banque de questions générée depuis tes erreurs, dashboard | Dès réception de 5+ sessions de data |
| **v2** | Mode examen complet 60 min, prédiction de percentile, simulation HireVue vidéo analysée | Après le test SHL |

> ⚠️ **Anti-procrastination** : la plateforme est la **servante** de l'entraînement, pas une excuse pour coder au lieu de driller. v0 d'abord (feuilles CSV), le code vient après le test réel.

---

## 3. 📅 Programme d'entraînement — jusqu'au test et au-delà

### Avant le SHL (13 oct)
- **Ce soir (12 oct)** : practice tests officiels fournis dans l'invitation SHL · 1 mock Verify Interactive chronométré · journal des erreurs (`error_log.csv`) · dormir 8h
- **Demain matin (13 oct)** : 15 min d'échauffement numérique légé + 1 série inductive · puis **PASSER LE TEST** — seul, silencieux, téléphone éteint, calculatrice papier, 90 min de block

### Règles du « test parfait » (à appliquer à CHAQUE test de la semaine)
1. Matin, cerveau frais (jamais après 21h, jamais après une journée de formulaires)
2. Un seul test par jour
3. Chrono visible, questions non-répondues = 0 (ne jamais laisser vide sur SHL)
4. Relecture des réponsesflaguées uniquement si temps restant
5. **Débrief dans les 2h** : chaque erreur qualifiée (calcul / lecture / méthode / temps) → `error_log.csv`
6. Le lendemain : refaire les 5 questions ratées les plus représentatives

### Rythme hebdo post-SHL (semaine du 13 → 19 oct)
| Jour | Matin | Soir (60-90 min) |
|---|---|---|
| Lun | Setup data + practice SHL | English module |
| **Mar** | **🎯 SHL BARCLAYS** | Débrief + CSV |
| Mer | 🎯 Test BNP (Talent Q : chrono par question 90s/75s, réponses proches, ne rien laisser vide) | Drills inductifs |
| Jeu | 🎯 HSBC Immersive (simulation journée, ~50 min, SJT + data pack) | Prépa CACEIS |
| Ven | ☎️ **CACEIS 10h** + débrief | English module + 4 histoires STAR DB |
| Week-end | Mock HireVue Barclays enregistré (anglais) + analyse | Rituel marché (FT 30 min) |

---

## 4. 🇬🇧 Anglais — plan v2 SPECIALISÉ (dossier [`english/`](english/))

**Diagnostic acté (12 oct)** : B2+ à l'oral (l'atout HireVue/AC), écrit faible → **on ne travaille PLUS l'écrit général**. On construit : **zéro mot inconnu dans le Hull/front office**, du natif anti-Frenglish, une prononciation propre, les maths/prog en anglais, la culture UK.

→ Tout est dans [`english/00-PLAN-ANGLO.md`](english/00-PLAN-ANGLO.md) + 5 fichiers :
1. [`01-hull-front-office-vocab.md`](english/01-hull-front-office-vocab.md) — ~180 termes (Hull-Zero), 15/jour → Anki
2. [`02-faux-amis-frenglish.md`](english/02-faux-amis-frenglish.md) — pièges FR→EN + remplacements natifs
3. [`03-prononciation.md`](english/03-prononciation.md) — 55 mots trappes + paires de stress + les chiffres
4. [`04-maths-prog-english.md`](english/04-maths-prog-english.md) — opérations, stats, Python, Excel (pivot table ≠ TCD)
5. [`05-uk-culture-actu-auteurs.md`](english/05-uk-culture-actu-auteurs.md) — institutions, Chancellor Healey, tracker quotidien, auteurs à citer

**Stack quotidien (~90-110 min dès le 13 oct)** : 30 min vocab Hull · 10 min prononciation · 5 min dé-Frenglish · 30 min Bloomberg/débats actifs · **1 HireVue filmé/jour** (rotation de 14 questions dans le plan).

**Métriques du 26 oct** : 14 HireVue filmées · 0 mot inconnu (1 résumé Hull + 1 article FT Markets) · 210 cartes Anki · liste des 55 mots prononcée sans erreur 3 jours de suite.

---

## 5. 🛂 Aspects administratifs — si Londres t'embauche (France → UK)

### 5.1 Ton titre de séjour français : que se passe-t-il vraiment ?

| Situation | Effet d'un départ à Londres |
|---|---|
| **Carte de séjour « étudiant » (VLS-TS validé ou carte pluriannuelle)** | Elle **expire à sa date de fin** — partir ne la « retire » pas. Aucune pénalité, aucun casier. Une future demande en France repart de zéro, normalement |
| **APS « recherche d'emploi » (post-diplôme, si tu restais en France)** | Simplement non demandée ou non renouvelable sans résidence en France |
| **Carte de résident 10 ans** (si tu en avais une) | ⚠️ Peut être **retirée en cas d'absence de France > 2 ans consécutifs** (exceptions : conjoint de Français, etc.) — pas ton cas probable, mais à savoir |
| **Statut long terme-UE** (si acquis un jour) | Se perd après 12 mois consécutifs hors UE — point de vigilance futur |
| **Déménagement** | Déclaration de départ au centre des impôts, Sécu française → NHS côté UK, CAF/Pôle emploi : non, résidence principale = UK |

**Bottom line** : partir à Londres ne détruit **rien** de permanent. Ton titre étudiant s'éteint naturellement avec la fin des études. Le seul point d'attention réel, ce sont les statuts long terme (10 ans / LTE-UE) si tu les acquiers plus tard.

### 5.2 Le visa UK Skilled Worker — le mécanisme

1. **Offer** → l'employeur (sponsor licencié : Barclays, DB, HSBC, BNP London ✅) délivre un **Certificate of Sponsorship (CoS)** — numéro électronique, avec date de début, rôle, salaire
2. **Seuils** : général £41 700 ; **new entrant** (toi, < 26 ans ou jeune diplômé) : **£33 400 + 70 % du going rate** — les salaires analystes (£55-70k) passent largement
3. **Demande en ligne** → biométrie à **TLScontact/VFS Paris** → décision standard ~3 semaines (priority 5 jours ouvrés, +£500) → **eVisa** numérique (les BRP papier n'existent plus) + share code pour louer/travailler
4. On peut postuler jusqu'à 3 mois avant la date de début du CoS

### 5.3 Les coûts exacts (taux 2026, en vigueur depuis le 8 avril 2026)

| Poste | Qui paie | Montant |
|---|---|---|
| Frais de visa Skilled Worker (≤ 3 ans, depuis l'étranger) | **Toi** (souvent remboursé par la banque) | **£819** |
| Frais de visa (> 3 ans) | Toi | £1 618 |
| **IHS** — Immigration Health Surcharge (NHS) | **Toi** (souvent remboursé) | **£1 035/an** → 3 ans = **£3 105** |
| Service priority (optionnel) | Toi | £500 |
| CoS (par travailleur) | Employeur (obligatoire) | £525 |
| Immigration Skills Charge | Employeur (interdit de te le refacturer) | £1 320/an (grand sponsor) |
| Sponsor licence | Employeur | £1 682 (une fois) |

**Ton budget réaliste en sortie de poche** : **~£3 900-4 400** pour un visa 3 ans (£819 + £3 105 + éventuels frais TLS) — et **négocie le remboursement** : chez les bulge brackets, la prise en charge visa + IHS est fréquente pour les programmes graduate. Question à poser à l'offre : *“Does the firm cover visa fees and the Immigration Health Surcharge for graduate joiners?”*

- **Dépendants** : conjoint/enfants bienvenus (visa dependant, mêmes frais + IHS par personne) — le conjoint peut travailler
- **Anglais** : preuve requise au niveau B1 (diploma enseigné en anglais, SELT type IELTS UKVI 4.0+… ton dossier SKEMA peut souvent suffire — à vérifier selon ta nationalité/formation)

### 5.4 Après le visa : le chemin vers l'installation

- **ILR (settlement)** : actuellement **5 ans** de Skilled Worker → résidence permanente. ⚠️ **Réforme « Earned Settlement » en cours** : consultation fermée le 12 fév. 2026, le projet passe la barre de 5 → **10 ans** pour la plupart des routes. Pas encore promulgué (à suivre au moment venu) — pour toi (départ 2027), la réforme s'appliquera probablement : **compte sur 10 ans dans ton plan mental, considère 5 ans comme un bonus**
- Anglais au settlement : exigence qui passe de B1 → **B2** (effective ~mars 2027)
- Skilled Worker = tu peux changer d'employeur (nouvelle CoS, mise à jour de visa) — tu n'es pas la propriété de Barclays

### 5.5 Erasmus & statut étudiant : la clarification

- **Erasmus ne crée aucun droit au UK** : le Royaume-Uni est sorti d'Erasmus+ (remplacé côté UK par le Turing Scheme). Aucune route de visa UK ne passe par Erasmus
- Ton statut étudiant français (SKEMA) s'éteint **avec ton diplôme**, quelle que soit ta destination — Londres n'annule rien, et ton Erasmus/expériences ne sont « perdus » nulle part : ils alimentent ton CV
- Inversement : pas de double statut possible (étudiant en France + salarié à Londres) — le passage se fait proprement : diplôme → CoS → visa → départ

### 5.6 Checklist chronologique si offer

- [ ] J+0 : offre signée — demander remboursement visa/IHS + date de début du CoS
- [ ] J+3 : CoS reçu → vérifier rôle, salaire, dates (une erreur = visa refusé)
- [ ] J+7 : compte UKVI + formulaire Skilled Worker + paiement visa + IHS
- [ ] J+10 : RDV biométrie TLScontact Paris (prendre passeport, CoS, diplômes, preuve d'anglais, relevés bancaires si exigés : **£1 270 de fonds propres** si la banque ne certifie pas ta maintenance — souvent dispensé pour les sponsors A-rated)
- [ ] J+15-25 : décision eVisa → share code
- [ ] Avant départ : déclaration fiscale de départ (impots.gouv), clôture/mutation des contrats FR (mutuelle, électricité…), compte bancaire UK à l'arrivée (Revolut/Wise en pont)
- [ ] Arrivée : NHS via IHS payé, NI number (national insurance) si pas auto-attribué, logement (share code + 3 payslips pour l'agence)

---

## 6. ✅ Prochaines actions immédiates (dans l'ordre)

1. **Ce soir** : practice SHL officiels + 1 mock chronométré → premiers `shl_sessions.csv` + `error_log.csv`
2. **Demain matin** : 🎯 **PASSER LE SHL BARCLAYS**
3. **Envoyer la data** (CSV + screenshots) → je construis la v1 de la plateforme sur tes vrais points faibles
4. **Chaque soir** : bloc anglais 60-90 min (section 4)
5. **Vendredi** : CACEIS à 10h — pitch prêt, question contrat/visa posée tôt

> **Cité pour la route** : *“Discipline equals freedom.”* — L'arrogance a coûté une saison. La discipline en rachète une en 7 jours.
