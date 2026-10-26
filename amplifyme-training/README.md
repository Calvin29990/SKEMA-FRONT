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
| **Session complète** | Round 1 Asset Manager ($20 M, 5 lignes) → Round 2 Investment Bank (quote board + RFQ blocs) | le format du 27/10 : AM puis IB |
| **Desk Asset Manager** | Acheter / vendre au marché, réagir aux headlines en < 5 s | ROI score, Execution, BSRM |
| **Desk Investment Bank** | Poster ses axes sur le board, répondre aux RFQ blocs, dénouer au marché | NUMT, COMM, ETM, SSRM, FFC |
| **Drills réflexes** | 6 exercices chronométrés de 60 s | bid/offer de tête, hedge, P&L, notionnel, fat finger, limite |
| **Fiche de bataille** | À relire la veille et 20 min avant | les critères du jeu, les 12 réflexes, le plan des 2 h |

## Les raccourcis (desk Investment Bank)

`1`–`5` ticker · `M` prix au mid ± 4 bps · `↵` poster l'axe · `B` acheter · `S` vendre ·
`F` flat la ligne · `X` annuler toutes les quotes · `Espace` pause · `?` aide.

## Barème du clone — aligné sur les métriques publiques d'AmplifyME

### Sell-side (Investment Bank)

| Métrique | Poids | Ce que ça mesure | Comment gagner |
|---|---|---|---|
| **NUMT** | 25 % | nombre de trades client | garder 3–4 axes les plus compétitifs du board |
| **COMM** | 25 % | commission (8 bps du notionnel) | des clips de 40–50k affichés, sur les lignes chères |
| **ETM** | 20 % | Exchange Trade Metric : risque client dénoué, vitesse, taille des clips | dénouer en < 10 s, clips de 25–50k, zéro position à la cloche |
| **SSRM** | 20 % | Sell-Side Risk Management : temps passé près de la limite | rester sous 85 % de 100 000 actions par ligne |
| **FFC** | 10 % | fat fingers | prix croisé, prix à 8 % du mid, volume > 500k |

`ETM = 100 × part dénouée × (0,55 + 0,25×vitesse + 0,20×qualité des clips)`, ×0,85 si une position reste ouverte.
`SSRM = 100 − 100×utilisation moyenne − 1,4×secondes au-dessus de la limite − 12 si max > 90 %`.

### Buy-side (Asset Manager)

| Métrique | Poids | Ce que ça mesure | Comment gagner |
|---|---|---|---|
| **ROI score** | 40 % | ton ROI converti en **percentile de cohorte** | 3 % de ROI ≈ P78, 5 % ≈ P91, 7 % ≈ P96 |
| **Execution score** | 30 % | prix obtenu vs le mid de référence | clips de 8–12 % du portefeuille, on achète l'offer |
| **BSRM** | 30 % | risque : stops tenus **et** risque réellement engagé | 70–95 % investi, stop à −1,2 % par ligne |

`Execution = 100 − 5,2 × slippage moyen (bps) + 20 × min(1, clip / 8 %)`.
`BSRM = 40 + 25 × min(1, exposition moyenne / 85 %) + 35 × (1 − drawdown / 2 %) − 1,2 × s sous le stop`.

### Percentile et rang

Le score composite est traduit en percentile estimé (courbe calibrée sur les retours de
participants : ~90 % est déjà très bon) puis en rang sur une cohorte de **2 100 joueurs**
(édition 2025). Repère : **top 100 ≈ P95**, finale mondiale = **top 10 % de chaque compétition régionale**.

## Ce qui est fidèle au vrai jeu (sources)

- **Format** : AM puis IB, simulation live de 2 h ; cohorte de ~2 100 participants en 2025 ;
  top 10 % par région → finale mondiale ; les 5 premiers gagnent une inscription au CFA L1.
- **Sell-side** : prix affichés sur un **quote board électronique** face à des banques concurrentes,
  hedge via un instrument liquide, **RFQ blocs dans la fenêtre de chat**.
- **Métriques** : NUMT / COMM / FFC / SSRM / ETM côté banque ; ROI score (percentile) /
  Execution / BSRM côté asset manager.
- **Comportements attendus** : réaction à une news en moins de 20 s, spreads serrés = relation client,
  dénouement lentement pour ne pas payer l'impact.

## Repères mesurés (bots de calibration, jsdom / node)

| Profil | Sell-side | Buy-side |
|---|---|---|
| **Desk discipliné** (3–4 axes en permanence, hedge immédiat en clips ≤ 45k, `X` sur chaque news) | 83–90 / A · **P91–P97** | 70–86 / B–A |
| **Desk passif** (peu d'axes, positions non dénouées) | 34–47 / E–D · P13–P33 | 56 avec de gros clips |
| **Desk inactif** (aucun trade) | 30 / E · P8 | — |

Autrement dit : le top 100 se joue sur la **régularité** (tous les axes vivants, tout dénoué, zéro FFC),
pas sur un coup d'éclat.

## Limites assumées

- Aucune formule officielle d'ETM, de SSRM ou d'Execution n'est publique : ce sont des **proxys
  mesurables** construits à partir des définitions citées par AmplifyME et ses participants.
- Les prix sont simulés (marche aléatoire + news), pas les vrais cours de la session.
- Le round AM du clone dure 4 min contre 30 min dans le vrai jeu : la courbe ROI → percentile est
  recalibrée sur cette durée compressée.
- Le poids exact des composantes n'est pas public (40/30/30 côté AM, 25/25/20/20/10 côté IB sont
  des hypothèses affichées, pas des chiffres officiels).
- Non affilié à AmplifyME ni au CFA Institute.
