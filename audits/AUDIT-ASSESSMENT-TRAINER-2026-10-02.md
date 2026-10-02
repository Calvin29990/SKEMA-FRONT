# Audit — Assessment Trainer / SKEMA-Training

**Date : 2 octobre 2026 · Référence : document Word fourni par Calvin.**

## Verdict

**La plateforme est une base d’entraînement exploitable, mais pas encore une reproduction fidèle du document.** L’écart ne se limite pas aux couleurs : plusieurs modules utilisent une autre tâche cognitive, certains chronomètres ne correspondent pas aux consignes, et plusieurs parcours usuels échouent.

La précédente session s’est arrêtée **juste après une adaptation des modules déductif et inductif**. Elle avait aussi ajouté le numérique à onglets, un chargeur local de données, l’anglais, la motivation et un examen blanc. Certaines adaptations ne sont toutefois présentes que dans le moteur ou dans les tests, pas dans le parcours proposé par défaut.

**Recommandation : conserver le socle, corriger les blocages, puis reprendre les épreuves une par une à partir de leurs consignes et captures. Une simple retouche CSS ne suffira pas.**

---

## 1. Version et périmètre vérifiés

### Plateforme

- Branche du lien : `arena/01a0fb43-skema-front`.
- Commit audité : [`600bd907492ac522e7bfc22976b4d1dccbc4784b`](https://github.com/Calvin29990/SKEMA-FRONT/commit/600bd907492ac522e7bfc22976b4d1dccbc4784b).
- Dernier commit : **2 octobre 2026 à 17 h 37, heure de Paris**.
- [Pull request n° 4](https://github.com/Calvin29990/SKEMA-FRONT/pull/4) : ouverte, non fusionnée, description vide au moment de l’audit.
- Fichier réellement testé : `skema-training/standalone/index.html`, celui visé par le lien HTMLPreview, servi localement par HTTP.
- Sources modulaires, copie publique `docs/`, README, outil de build et harnais de test également consultés.

### Document de référence

- [`DOC IMPORTANT base Entretien front.docx`](https://github.com/Calvin29990/SKEMA-FRONT/blob/a264854e6fc6bdfcde0b29cd3edf94beae6a2be6/DOC%20IMPORTANT%20base%20Entretien%20front.docx), à la racine de `main`.
- Blob Git : `25661ab617403d810ff3390945b77506ffb3aa0d`.
- **338 images uniques, 339 occurrences** dans le document : une image apparaît deux fois.
- Extraction de l’ensemble des images ; lecture visuelle représentative et OCR ciblé de **112 images**, notamment les introductions, règles, écrans de réponse et chronomètres.
- Les références `imageN.png` ci-dessous désignent les fichiers contenus dans `word/media/` du DOCX, et non des numéros de page.

### Méthode et limites

- Navigation dans Chromium headless 153, tests sur le standalone et les sources modulaires.
- Test des **16 boutons de départ de l’accueil**, inspection de 13 épreuves, contrôles de sauvegarde, de clavier, de chronométrage et d’affichage mobile à 390 px.
- Échantillonnage déterministe de **960 items inductifs**.
- Les profils de test sont isolés : aucun historique du navigateur personnel de Calvin n’a été modifié.
- Le cache éventuel du service HTMLPreview et les autres navigateurs ne sont pas évalués.
- Il s’agit d’un audit de fidélité **au document fourni**, pas d’une certification officielle des tests de toutes les banques. Les réponses de toutes les banques de questions n’ont pas fait l’objet d’une validation pédagogique exhaustive.

**Aucune correction de la plateforme, fusion ou publication n’a été effectuée.** Le document et ses captures ont été conservés uniquement dans un dossier temporaire exclu de Git. Seul ce rapport est ajouté à la branche de cette session, `arena/01a0fd43-skema-front`.

---

## 2. Où la précédente session s’est arrêtée

Les indices disponibles sont l’historique Git, les sources et les tests ; il n’y a pas de compte rendu de passation dédié dans `skema-training/`, ni dans la description de la PR.

| Étape du 2 octobre | Commit | État retrouvé |
|---|---|---|
| Numérique au format à onglets | `a7b4f6d7aa87` | 37 affirmations, 6 onglets, chrono global de 12 minutes. |
| Chargement de contenu personnel | `cd491c87a5d6` | Import JSON local ; données personnelles exclues des livrables publics. |
| Adaptation du verbal | `2e5adc5826d6` | Panneaux de texte et mise en page ajoutés au moteur numérique/importable. Le bouton « Verbal Reasoning » conserve néanmoins l’ancien parcours. |
| Anglais et motivation | `6c6af71520eb` | Anglais avec intertitres/exemples/« ? » ; motivation en blocs de 3 avec répartition de points. |
| Examen blanc de 3 épreuves | `b0667d1f58ab` | Tirage de 3 familles et enchaînement. Certaines banques tirées restent les anciennes variantes. |
| Contrôle de l’accueil | `e4744ffc0d2d` | Vérification du nombre de cartes, pas de tous les démarrages sans paramètres. |
| **Dernière intervention** | **`600bd907492a`** | **Déductif 4×4 et inductif « 2 parmi 4 ». Anciens formats conservés en sections cachées.** |

Le README est en retard sur le code : il annonce encore 13 sections, des matrices déductives, des séries inductives et une motivation sur échelle. L’accueil actuel contient **14 épreuves visibles + examen blanc + simulation**, soit 16 lignes. Trois variantes supplémentaires sont cachées dans le registre.

---

## 3. Ce qui mérite d’être conservé

- Application statique sans dépendance serveur pour l’usage courant.
- Fichier standalone autonome ; aucune requête externe observée dans les scénarios de navigateur exécutés.
- Profils locaux, historique horodaté, détail des réponses, export CSV, progression, thèmes et interface FR/EN/ES/PT.
- Numérique à onglets : bon point de départ structurel.
- Motivation : moteur de répartition de points réutilisable pour le comportement professionnel.
- Import JSON local de figures et de textes : utile pour travailler avec des références personnelles sans les intégrer au site public.
- Organisation des sources en banques, générateurs, moteur et vues ; harnais de navigateur existants.

Ces éléments réduisent le travail de reprise. En revanche, les traductions de l’interface et une galerie de captures ne remplacent pas des moteurs d’épreuve conformes au document.

---

## 4. Comparaison des épreuves avec le document

| Épreuve | Format montré dans le document | Version actuelle | Diagnostic |
|---|---|---|---|
| **Anglais** | 3 types distincts : aisance/phrases, vocabulaire par définition, orthographe. 2 exemples par section. Vocabulaire : 4 min ; orthographe : 2 min ; ensemble : 10 min. Orthographe à 2 choix + « ? ». | 3 groupes tirés de la même banque de **59 phrases à compléter**, toujours 4 choix + « ? », avec 20 s par item. | **Partiel.** Vocabulaire et orthographe ne sont pas réellement implémentés comme épreuves distinctes. Voir images 2, 16–17, 29–32. |
| **Verbal** | **49 affirmations, 12 min**, 6 onglets de textes stables, navigation entre questions et réponses modifiables. | Bouton par défaut : 36 affirmations sur 12 passages, présentation QCM classique, 45 s par item. Le format à textes/onglets n’est accessible qu’en chargeant un JSON dans la tâche numérique. | **Écart majeur du parcours par défaut.** Voir images 81–83 et 84–125. |
| **Numérique** | **37 affirmations, 12 min**, 6 feuilles de données, True / False / Cannot say, navigation. | Même architecture générale et chrono global ; figures et données d’entraînement intégrées. | **Le plus proche structurellement**, mais ce n’est pas une reproduction visuelle exacte. Démarrage depuis la fiche de configuration cassé. Voir images 41–48. |
| **Déductif** | Grilles 4×4 **partiellement remplies**, une case cible « ? », contraintes ligne/colonne. 6 minutes pour répondre à autant de questions que possible. | Grille entièrement remplie sauf la case cible : **15 indices visibles**, donc réponse directement déductible d’une seule ligne. 12 items, 30 s par item. | **Adaptation récente, difficulté et rythme non fidèles.** Les captures de questions contiennent plusieurs cases vides. Voir images 126–156, notamment 132–144. |
| **Inductif** | 2 exemples, 4 candidates, choisir les 2 conformes. Règles de nombre/position, une paire correcte, chrono global de 6 min. | Structure visuelle générale présente. Palette empruntée au déductif ; catalogue de règles limité ; 8 items, 45 s par item. Génération ambiguë dans certains cas. | **Adaptation récente à fiabiliser.** Voir images 157–174. |
| **Comportement professionnel** | **48 blocs** selon le compteur final ; chaque bloc comporte 3 affirmations et jusqu’à 6 points à répartir. Pas de limite de temps, environ 15 min, pas de retour arrière. | 36 affirmations isolées sur une échelle « Presque jamais / Parfois / Souvent / Presque toujours », 12 s par item. | **Mauvais mécanisme.** Réutiliser le moteur de blocs, sans mélanger comportement et motivation. Voir images 175–178 et 227 (`48/48`). |
| **Motivation / intérêts** | 36 blocs de 3 affirmations, jusqu’à 6 points à répartir ; sans limite de temps et sans retour arrière. | 36 blocs, allocation plafonnée à 6, pas de chrono imposé. | **Bonne base fonctionnelle.** Mise en page et contenu d’entraînement restent à aligner. Voir images 228–264. |
| **Concentration** | Identifier **un E entouré d’exactement 3 points**, boutons correct/incorrect, raccourcis D/A ; objet visible jusqu’à la réponse, test global de 2 min. | Comparer deux formes et répondre identiques/différentes ; chrono par paire, avec un défaut d’unité majeur. | **Autre tâche cognitive.** Corriger le chrono ne suffira pas. Voir images 265–273. |
| **Learning Efficiency** | Mémoriser l’**ordre d’objets présentés successivement** ; 6 sections avec les mêmes 12 objets, restitution par glisser-déposer, 30 s par section, pause de 6 s ; environ 5 min. | Mémoriser 5 positions dans une grille 5×5 puis recliquer les cases ; 20 planches et exposition décroissante. | **Autre tâche cognitive.** L’ordre et l’apprentissage répété sont absents. Voir images 274–287, notamment 280. |
| **Traitement de l’information** | Boîte de réception simulée : lire, prioriser et agir sur les e-mails suivant des règles ; nouveaux messages pendant l’épreuve ; consignes consultables ; chrono global de 15 min. | 18 QCM de finance/probabilités sur la valeur de l’information et l’espérance, 90 s par item. | **Contresens de format.** Il faut un moteur de messagerie, pas une autre banque de QCM. Voir images 288–299. |
| **Mécanique** | 24 questions illustrées, 3 réponses, **15 min au total**, retour aux questions précédentes et modification des réponses. | 24 QCM thématiquement proches, scènes SVG simplifiées, 60 s par item, pas de navigation arrière équivalente. | **Thèmes proches, interface et conditions différentes.** Voir images 304–331. |
| **Switch Challenge** | Symboles colorés, opérateurs sous forme de **codes de permutation** à 4 chiffres, choix entre codes, niveaux ; chrono global de 6 min. | Suites numériques entrée/sortie ; choix de séquences d’échanges notées `⇄`, 25–45 s par item. | **Logique apparentée, interaction non conforme.** Voir images 332–338. |
| **Français** | Présent sur la liste des tâches ; exercices linguistiques visibles. | Aucun module de compétences linguistiques françaises. | **Absent.** Une interface traduite en français n’est pas cette épreuve. Voir image 1 et images 300–303. |
| **Multitâche** | Présent sur la liste des tâches. | Aucun module correspondant ; « Mémoire de travail » est un ajout distinct. | **Absent.** Les captures disponibles ne permettent pas de spécifier précisément ce test : ne pas inventer son format. Voir image 1. |

### Deux confusions à corriger

1. **« English Battery ∞ » est en réalité du raisonnement verbal en anglais**, avec True / False / Cannot say. Ce n’est pas une batterie illimitée de compétences linguistiques. L’objectif d’accueil « 50 réponses » est attaché à `verbalX`, pas à l’épreuve linguistique `english`.
2. L’examen blanc tire `numericalMCQ` et `verbalX`, **pas** les formats à onglets attendus pour le numérique et le verbal. La simulation complète utilise également le numérique QCM. L’appellation « comme le jour J » est donc prématurée.

### Fidélité visuelle

Le document montre principalement une barre rouge SKEMA, des pages blanches, des contrôles et dimensions propres à chaque test. Le site utilise une marque CM verte, un fond gris, une navigation permanente et un tableau de scores générique. L’inductif reprend maintenant la disposition 2 exemples / 4 candidates, mais les symboles, espacements et contrôles diffèrent encore.

Le chantier visuel doit venir **avec les bons mécanismes**, et non masquer leur absence.

---

## 5. Bugs techniques reproduits

**P0 : parcours inutilisable ou chrono gravement erroné. P1 : résultat/conditions d’entraînement non fiables. P2 : qualité, accessibilité, finition.**

### P0 — à corriger avant toute refonte

#### T01 — Trois départs depuis l’accueil échouent

- Accueil → Début de **English Battery ∞**, **Déductif** ou **Inductif**.
- Session construite avec **0 item**, zone de question vide, exception : `Cannot read properties of undefined (reading 'kind')`.
- Cause : `runView()` fournit `count: undefined`, qui écrase le nombre par défaut dans `mount()` ; les générateurs bouclent alors sur un nombre non défini.
- Références : `app.js:414–426`, `core.js:192–230` et `691–701`.
- Le démarrage avec `?count=12` ou `?count=8` fonctionne : c’est ce chemin que vérifient les tests existants, pas le bouton usuel.

#### T02 — Début depuis la fiche Numérique échoue

- Ouvrir `#/section/numerical`, puis cliquer sur Début.
- Exception : `Cannot read properties of null (reading 'value')` ; la fiche reste affichée.
- Cause : le gestionnaire lit `#cfgPaper`, qui n’existe pas dans le formulaire du numérique à onglets.
- Référence : `app.js:306–379`, en particulier ligne 379.

#### T03 — Chrono de concentration multiplié par 1 000

- Le générateur donne `time: 2500` en millisecondes.
- Le moteur interprète cette valeur en secondes et la multiplie par 1 000.
- Le navigateur affiche **`2499.8 s`**, soit environ **41 min 40 par paire**, au lieu des 2,5 s annoncées par le site.
- Références : `drills.js:522–544`, `core.js:1256–1290`.
- Ensuite, il faudra aligner le véritable format sur les **2 minutes globales** du document, et pas seulement corriger l’unité de ce prototype.

### P1 — fiabilité et conditions d’épreuve

| ID | Constat vérifié | Conséquence / reprise |
|---|---|---|
| **T04 — Chronos** | Déductif : 30 s réinitialisées à chaque item ; inductif : 45 s ; anglais : 20 s. Contrairement à l’annonce, aucun délai global de 6 ou 10 min n’est appliqué à ces sessions. | Introduire des chronos au niveau du test ou de sa phase. Préserver les exemples non chronométrés et les questionnaires sans limite. `core.js:1256–1290`. |
| **T05 — Inductif ambigu** | Sur **960 items** déterministes (120 graines × 8), **457** contiennent des candidates répétées ; **25** admettent une autre règle du catalogue compatible avec les deux exemples mais donnant une autre paire correcte. | Tester la distinction des candidates et l’unicité de la paire parmi les règles admises. Exemple reproductible : graine 0, item `I2-2`, règle prévue « miroir », autre règle plausible « ligne ». Ces nombres décrivent cet échantillon, pas toute la banque. `core.js:277–351`. |
| **T06 — Barème anglais** | Une réponse « ? » à un item noté est journalisée `ok: false` et incrémente le compteur d’erreurs. Le document prévoit que « ? » laisse le score inchangé, tandis qu’une mauvaise réponse fait perdre des points. | Distinguer réponse incorrecte, inconnue et non répondue ; ne pas inventer les coefficients précis du barème s’ils ne sont pas documentés. Images 16 et 32 ; `core.js:1057–1167`. |
| **T07 — Mode examen** | Les compteurs ✔ / ✘ restent visibles après une réponse, même avec correction annoncée seulement à la fin. Exemple : `Item2/12 ✔ 1 ✘ 0 … mode examen`. | Clarifier la simulation sans correction intermédiaire ; masquer ce retour dans ce mode. Ne pas supprimer le feedback natif d’un test qui le prévoit, notamment le déductif. `core.js:721–741`. |
| **T08 — Sauvegarde JSON** | L’export contient les tentatives et réglages, mais pas le détail des réponses ni les captures. L’import écrit la clé globale `attempts`, alors que les profils lisent `attempts::<profil>`. Après rechargement, la migration attribue les données importées à Calvin, même depuis un autre profil. | Ce n’est pas une sauvegarde/restauration complète. Importer vers le bon profil, inclure les détails, définir explicitement le périmètre des captures et vérifier un aller-retour. `app.js:777–803`, `core.js:487–498`. |
| **T09 — Indicateurs** | Dans un jeu neutre de contrôle, 3 réponses cognitives correctes donnent 100 %. L’ajout de 3 items de motivation sans bonne/mauvaise réponse fait tomber la précision globale à **50 %**. Les sections comportementales restent à 0 de progression car `best === null`. | Exclure ces questionnaires du dénominateur de précision et utiliser un critère de complétion distinct. `core.js:568–575`, `app.js:237–245`. |

### P2 — interface et accessibilité

- **T10 — Clavier déductif/inductif incomplet :** le gestionnaire 1–4 ne traite pas `latin4` et `pick2`. Sur le déductif, `1` ne sélectionne rien ; `Entrée` avance ensuite sans journaliser de réponse. Les nouveaux contrôles utilisent des `div` cliquables, sans comportement de bouton accessible équivalent. Références : `core.js:655–683`, `851–890`.
- **T11 — Inductif mobile :** à 390 px de fenêtre, le document atteint **467 px** de largeur, entraînant un défilement horizontal. L’accueil, le numérique et la motivation n’ont pas présenté ce débordement dans les quatre vues contrôlées.
- **T12 — Documentation :** README principal et README de tests incomplets par rapport aux dernières adaptations ; absence de spécification de conformité par module.

---

## 6. Ce que les tests existants prouvent — et ne prouvent pas

Les sept harnais ont été exécutés avec les assertions conservées. Seul le chemin local absolu de `docs/index.html` dans `e2e.js` a été adapté au dossier temporaire de l’audit.

| Harnais | Vérifications réussies | Échecs |
|---|---:|---:|
| `nv.js` | 20 | 0 |
| `perso.js` | 16 | 0 |
| `verbal.js` | 10 | 0 |
| `exam.js` | 18 | 0 |
| `exam3.js` | 9 | 0 |
| `dedind.js` | 18 | 0 |
| `e2e.js` | 36 | 0 |
| **Total** | **127** | **0** |

**Ces succès ne valent pas validation de fidélité.**

- Le déductif/inductif est lancé avec un nombre d’items explicite : le défaut du bouton d’accueil passe inaperçu.
- Le test du verbal réel charge une fixture dans **Numerical**, puis vérifie cette importation. Il ne prouve pas que le bouton Verbal utilise ce format.
- Le test anglais vérifie groupes/exemples/bouton « ? », pas les trois types linguistiques ni les minuteries officielles du document.
- Aucun de ces harnais ne compare les captures du DOCX à l’interface, ni ne valide les tâches E/points, séquence d’objets ou boîte de réception.
- Le contrôle inductif vérifie la règle choisie par le générateur, pas l’absence d’une deuxième règle plausible.

Les scénarios supplémentaires de cet audit reproduisent donc des problèmes **malgré** les 127 vérifications vertes.

---

## 7. Confidentialité à clarifier

- Le stockage local et l’import sans envoi réseau sont de bonnes propriétés observées.
- L’écran de code d’accès reste un **garde-fou côté navigateur**, pas une authentification serveur : il ne protège pas les fichiers d’un dépôt public.
- Le document original est toujours accessible dans la branche `main` du dépôt public, malgré les mentions « usage personnel » et les exclusions de contenu personnel ajoutées à la plateforme.
- Aucune suppression, modification de visibilité ou opération sur l’historique Git n’a été entreprise. Si une confidentialité réelle est souhaitée, il faudra traiter ce point séparément avec l’accord de Calvin.

---

## 8. Plan de reprise conseillé

### Lot 1 — Rendre les parcours fiables

1. Corriger le nombre d’items par défaut et le formulaire Numérique.
2. Normaliser les unités de temps ; ajouter les bons chronos globaux/par phase.
3. Ajouter un test qui **clique chacun des 16 boutons** de l’accueil sans paramètres artificiels.
4. Corriger sauvegarde/restauration et indicateurs des questionnaires sans score.

### Lot 2 — Aligner les épreuves prioritaires

1. **Anglais :** vrais sous-tests aisance, vocabulaire et orthographe, exemples, « ? » neutre, phases 4 / 4 / 2 minutes ; banque originale d’entraînement extensible. Séparer clairement cette batterie du raisonnement verbal en anglais.
2. **Verbal :** brancher une épreuve dédiée avec 6 onglets textuels, 49 affirmations et 12 minutes, sans dépendre d’un import dans le module numérique.
3. **Comportement :** 48 blocs de 3, allocation jusqu’à 6 points, sans limite de temps ; conserver la motivation séparément.
4. **Déductif :** générer des grilles clairsemées dont **la case demandée** a une solution unique, avec difficulté graduée et session globale de 6 min.
5. **Inductif :** palette conforme, règles variées, suppression des règles équivalentes (« centre » et « diagonales » ici), candidates distinctes, paire correcte non ambiguë, 6 min.

### Lot 3 — Remplacer les prototypes hors format

- Concentration : E/variantes et points, réponses correct/incorrect, touches D/A, 2 min globales.
- Learning Efficiency : présentation séquentielle, ordre de 12 objets, 6 répétitions et restitution par glisser-déposer ; préciser les durées de présentation à partir d’une référence supplémentaire si nécessaire.
- Information Handling : boîte de réception, priorités, actions, nouveaux messages, consignes consultables et chrono de 15 min.
- Switch : opérateurs codés et symboles, niveaux, 6 min globales.
- Mécanique : navigation et changement de réponse, 24 items et 15 min ; compléter les familles de figures.
- Français : épreuve dédiée. Multitâche : obtenir ses consignes/captures avant de définir un moteur.

### Lot 4 — Finaliser l’expérience

- Aligner barre supérieure, couleurs, formes, dimensions, transitions et contrôles sur les captures, tout en conservant une indication claire qu’il s’agit d’entraînement.
- Corriger clavier, focus, rôles accessibles et débordements mobiles.
- Faire tirer à l’examen blanc **les nouveaux moteurs réels**, avec leur durée et leur propre navigation.
- Refaire les exports standalone/docs et vérifier chaque module sur le **livrable généré**, pas uniquement les sources.
- Mettre à jour README, critères de fidélité et tests de non-régression.

### Critère d’acceptation par épreuve

Une épreuve n’est « alignée au document » que si sont vérifiés : **tâche demandée, contenu d’entraînement approprié, interaction, consignes/exemples, chrono, navigation, traitement des réponses, fidélité visuelle et démarrage depuis l’accueil**. La mention « format réel » ne doit pas reposer seulement sur la présence d’une grille ou de boutons.

---

## 9. Références de code et empreintes

Tous les chemins suivants sont relatifs au commit audité, et non à la branche courante de cette session.

- [Registre, générateurs et moteur : `core.js`](https://github.com/Calvin29990/SKEMA-FRONT/blob/600bd907492ac522e7bfc22976b4d1dccbc4784b/skema-training/assets/js/core.js).
- [Routes, formulaires et sauvegarde : `app.js`](https://github.com/Calvin29990/SKEMA-FRONT/blob/600bd907492ac522e7bfc22976b4d1dccbc4784b/skema-training/assets/js/app.js).
- [Attention, apprentissage et switch : `drills.js`](https://github.com/Calvin29990/SKEMA-FRONT/blob/600bd907492ac522e7bfc22976b4d1dccbc4784b/skema-training/assets/js/drills.js).
- [Banque linguistique : `bank-plus.js`](https://github.com/Calvin29990/SKEMA-FRONT/blob/600bd907492ac522e7bfc22976b4d1dccbc4784b/skema-training/assets/js/bank-plus.js).
- [Numérique et import de textes : `numverb.js`](https://github.com/Calvin29990/SKEMA-FRONT/blob/600bd907492ac522e7bfc22976b4d1dccbc4784b/skema-training/assets/js/numverb.js).
- [Harnais de navigateur](https://github.com/Calvin29990/SKEMA-FRONT/tree/600bd907492ac522e7bfc22976b4d1dccbc4784b/skema-training/tools/tests).

Empreintes SHA-256 des fichiers téléchargés :

```text
standalone/index.html
1f5cc6075bfb810bbd53ecc06d435ad9402370484eac10d6c6ce3b1f57260d5b

DOC IMPORTANT base Entretien front.docx
59e7fa18d8b6ad4bdfbffa327c5b3049cf9e521cef4c7059f6f946274d602eee
```

**Conclusion : point d’arrêt retrouvé et audit réalisé. Le socle peut être repris, mais il faut encore corriger des bugs de lancement et remplacer plusieurs prototypes par les tâches réellement montrées dans le document.**
