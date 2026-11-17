# NVDA — Reconstruire le dashboard dans Power BI Desktop (`.pbix`)

> **Important — à lire en premier**
> - Un vrai rapport Power BI (`.pbix`) est un binaire propriétaire : **il ne peut pas être généré depuis ce repo / cet agent**, uniquement par Power BI Desktop.
> - Donc **aucun lien GitHub ne fera « s'ouvrir le rapport tout seul » dans Power BI** : `NVIDIA_PowerBI_Dashboard.html` s'ouvre dans un **navigateur** (Chrome/Edge), pas dans Power BI.
> - En revanche, **les données transformées** (`NVDA_financial_analysis.xlsx` / `.csv`, avec Daily_Return, Cumulative_Return, MA20, Drawdown déjà calculées en Python) + ce guide te permettent de recréer **exactement** le même dashboard dans ton Power BI Desktop en ~15 minutes, puis de l'enregistrer en `.pbix`.

## 1. Obtenir les données (2 options)

**Option A — Excel (recommandé)**
1. Power BI Desktop → **Obtenir des données → Excel** → `NVDA_financial_analysis.xlsx` → feuille `Sheet1` → **Charger**.

**Option B — CSV**
1. **Obtenir des données → Texte/CSV** → `NVDA_financial_analysis.csv` → encodage **UTF-8** → délimiteur **virgule** → **Transformer les données**.

## 2. Power Query — mises en forme

1. Colonne `Date` → type **Date** (AAAA-MM-JJ).
2. `Close, High, Low, Open, MA20` → type **Nombre décimal**.
3. `Volume` → **Nombre entier**. `Daily_Return` → **Nombre décimal** (fraction : 0,017 = +1,7 %). `Cumulative_Return`, `Drawdown` → **Nombre décimal** (déjà en **%**).
4. (Option) Ajouter colonne **AbsRet** = `Number.Abs([Daily_Return])` pour la table des sessions extrêmes.
5. (Option) Histogramme : sélectionner `Daily_Return` → **Nouvelle requête → Grouper par** ou **Nouveau groupe → Taille de bac = 0,03**.
6. **Fermer et appliquer**.

## 3. Mesures DAX (Nouvelle mesure)

```dax
Total Return %      = LOOKUPVALUE('Sheet1'[Cumulative_Return], 'Sheet1'[Date], MAX('Sheet1'[Date]))
Volatility (Ann.) % = STDEV.S('Sheet1'[Daily_Return]) * SQRT(252) * 100
Sharpe Ratio        = (AVERAGE('Sheet1'[Daily_Return]) * 252 - 0.02) / (STDEV.S('Sheet1'[Daily_Return]) * SQRT(252))
Max Drawdown %      = MIN('Sheet1'[Drawdown])
Win Rate %          = DIVIDE(
                        CALCULATE(COUNTROWS('Sheet1'), 'Sheet1'[Daily_Return] > 0),
                        CALCULATE(COUNTROWS('Sheet1'), 'Sheet1'[Daily_Return] <> BLANK())
                      ) * 100
Avg Daily Return %  = AVERAGE('Sheet1'[Daily_Return]) * 100
Avg Volume (M)      = AVERAGE('Sheet1'[Volume]) / 1000000
```
✅ Valeurs attendues (période complète) : **+15,84 %** · **63,51 %** · **1,00** · **−32,68 %** · **53,1 %** · **+0,259 %** · **274 M**.

## 4. Visualisations (mapping avec le dashboard HTML)

| # | Visuel | Type Power BI | Champs |
|---|--------|---------------|--------|
| 1–6 | KPI | **Carte** | les 6 mesures DAX ci-dessus |
| 7 | Prix vs MA20 | **Courbe** | Axe = Date · Valeurs = Close, MA20 |
| 8 | Cumulative Return | **Courbe avec marqueurs / Aire** | Axe = Date · Valeurs = Cumulative_Return |
| 9 | Drawdown | **Courbe avec remplissage** (rouge) | Axe = Date · Valeurs = Drawdown |
| 10 | Rendements journaliers | **Histogramme groupé** (barres vert/rouge) | Axe = Date · Valeurs = Daily_Return |
| 11 | Distribution | **Histogramme** (bins de 0,03) | Daily_Return groupé |
| 12 | Volume | **Histogramme** (colonnes) | Axe = Date · Valeurs = Volume |
| 13 | KPI Snapshot | **Barres horizontales** | Mesures Return %, Volatility %, ABS(Max Drawdown %), Sharpe |
| 14 | Sessions extrêmes | **Table** | Date, Close, Daily_Return, Volume · filtre visuel **Top N = 6 par AbsRet**, tri Date |
| 15 | Filtre de période | **Segment** (slicer) | Champ Date (par Mois) → filtre tous les visuels |

## 5. Thème NVIDIA / Power BI

- Fond : `#0D1117` (panneaux `#141B26`) · accent NVIDIA : `#76B900` · rouge risque `#F2555A` · ambre `#F2A93B` · teal `#2DD4BF` · texte `#E9EDF5` — police **Segoe UI**.
- Bandeau titre noir + liseré vert 3 px ; coins arrondis 12–14 px (format → Coins arrondis) ; grille 12 colonnes.
- Power BI Desktop : **Affichage → Thème → Personnaliser le thème actuel** pour appliquer ces couleurs, ou importer un JSON de thème avec ces valeurs.

## 6. Zones de texte — interprétations standard courtes (étape manquante du brief)

Ajoute **une zone de texte par visuel** (le fichier `Power BI Work (4).html` n'en contient AUCUNE — 0 occurrence vérifiée) :

- **Prix vs MA20** → « Close $134,79 vs MA20 $127,77 (+5,5 %) : structure haussière à court terme ; au-dessus de la MA20 depuis la reprise de mai. »
- **Cumulative Return** → « +15,8 % sur 82 séances — record +20,1 % (20-02) puis creux −19,2 % (04-04) : performance path-dépendante, portée par quelques séances AI. »
- **Drawdown** → « Max drawdown −32,7 % (04-04) : zone de bear market (>20 %) ; recapture presque complète à −3,5 % fin mai — la taille de position est la contrainte critique. »
- **Daily Returns** → « Rendement moyen +0,26 %/j pour σ=4,0 %/j ; queues épaisses : +18,7 % (09-04) vs −8,7 % (03-03) — tape événementielle. »
- **Distribution** → « Masse ±1,5–3 % avec queue droite positive ; kurtose en excès → les modèles normaux sous-estiment le risque de queue (VaR historique). »
- **Volume** → « Capitulation : 612,9 M titres le 09-04 (+18,7 %), 611,0 M le 07-04 ; normalisation ~200–370 M en mai — reprise propre. »
- **Sharpe** → « ≈1,0 (RF 2 %) : le risque est payé, pas démesuré — mais sans marge de sécurité. »
- **Volatilité** → « 63,5 % annualisé ≈ 3× le marché actions — exposition high-beta AI ; dimensionner en conséquence. »
- **Win Rate** → « 53,1 % de séances gagnantes (43/81) — le profit vient de la magnitude, pas de la fréquence. »
- **Max Drawdown** → « −32,7 % > seuil institutionnel de confort −20 % : gouvernance risque à expliciter. »
- **MA20** → « Clôture > MA20 : tendance CT intacte ; reperdre la MA20 invaliderait la reprise. »
- **KPI Snapshot** → « Vol 63,5 % ≫ Return +15,8 % : gains gagnés à travers les swings, pas en ligne droite ; Sharpe ≈1 dit que le risque était payé. »
- **Sessions extrêmes** → « 27-02 (−8,5 %), 03-03 (−8,7 %), 04-04 (−7,4 %) concentrent la baisse ; 09-04 (+18,7 %) la capitulation — quelques séances expliquent l'essentiel. »
- **Verdict** → « Le fichier Power BI source ne contenait aucune interprétation ; celles-ci la comblent — à recopier telles quelles en zones de texte dans le .pbix. »

## 7. Pousser le résultat

1. Fichier → **Enregistrer sous** → `NVDA_PowerBI_Dashboard.pbix`.
2. Pour le partager : le committer dans le repo (les .pbix sont des binaires — acceptés par Git, mais préférer **Power BI Service → Publier** pour le streaming/partage propre) ou joindre via **SharePoint / Drive**.

## Étapes 1–6 de l'énoncé (rappel)

1. ✅ Société = NVIDIA (NVDA) · 2. ✅ Objectif = performance/risque historique · 3. ✅ Audience = PM & investisseurs institutionnels · 4. ⚠️ Drivers = prix vs MA20, régime de volatilité, drawdown, volume (peers AAPL/MSFT/… & heatmap de corrélation non reproductibles hors ligne) · 5. ✅ KPIs = rendement, vol, Sharpe, drawdown, win rate, MA20 · 6. 🟡 Rapport livré en HTML (navigateur) + ce guide → `.pbix` à générer dans Power BI Desktop.
