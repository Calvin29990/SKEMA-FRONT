# AmplifyME Trainer — CFA Investing Simulator Challenge 2026

Simulateur d'entraînement **hors ligne** pour la session du **mardi 27 octobre 2026, 18:00–20:00 GMT**
(Investing Simulator Challenge, CFA Institute × AmplifyME). Zéro dépendance, zéro donnée live.

## Lancer

Ouvrir `index.html` dans le navigateur (double-clic suffit).
Tout tient dans 7 fichiers statiques : `index.html`, `styles.css`, `engine.js`, `engine-am.js`,
`drills.js`, `app.js`, `app-am.js`.

## Ce qu'il y a dedans

| Mode | Ce que tu fais | Ce que ça travaille |
|---|---|---|
| **Session complète** | Round 1 Asset Manager ($20 M, 5 lignes) → Round 2 Investment Bank (market maker + sales trader) | le format exact du 27/10 |
| **Desk Asset Manager** | Acheter / vendre au marché, réagir aux headlines | alpha vs benchmark, drawdown, concentration |
| **Desk Investment Bank** | Répondre aux RFQ, quoter bid/offer, hedger, tenir la limite | NUMT, COMM, FFC, SSRM |
| **Drills réflexes** | 6 exercices chronométrés de 60 s | bid/offer de tête, hedge, P&L, notionnel, fat finger, limite |
| **Fiche de bataille** | À relire la veille et 20 min avant | les critères du jeu, les 12 réflexes, le plan des 2 h |

## Les raccourcis (desk Investment Bank)

`1`–`5` ticker · `M` prix au mid ± 5 bps · `↵` envoyer la quote · `B` acheter · `S` vendre ·
`F` flatten · `X` annuler toutes les quotes · `Espace` pause.

## Barème du clone (entraînement)

Investment Bank : COMM 30 % · P&L 25 % · Risque 20 % · Relation 15 % · Fat finger 10 %.
Asset Manager : Alpha 55 % · Risque 25 % · Activité 10 % · Discipline 10 %.

AmplifyME classe en percentile sur l'ensemble des participants : le score ici est un **repère
absolu** pour savoir si tu es prêt, pas une prédiction du classement.

## Limites assumées

- Les prix sont simulés (marche aléatoire + news), pas les vrais cours de la session.
- Le carnet d'ordres, les volumes et les commissions sont simplifiés mais calibrés pour que la
  discipline paie et que les erreurs coûtent.
- Non affilié à AmplifyME ni au CFA Institute.
