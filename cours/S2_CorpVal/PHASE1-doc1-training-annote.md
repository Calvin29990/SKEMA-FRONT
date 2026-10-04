# DOC 1 — Training du prof, template original : réponses en vert + explications très détaillées en bas

> **Template repris à l'identique du booklet du prof** (`Intrinsic_Valuation_Exercises (midterm training).pdf`) :
> mêmes tableaux, mêmes questions numérotées. **Réponses en [[vert]] juste sous l'énoncé** ; **l'explication
> très détaillée est en bas de chaque exercice** (cache-la avec le pouce pendant que tu refais).
> Tous les chiffres sont vérifiés par recalcul indépendant (collent au corrigé officiel).

---

## Exercise 1. FCFF Valuation and EV-to-Equity Bridge

A company forecasts the FCFF below. WACC = 8.5%; perpetual growth after Year 5 = 2.5%; debt = €180m; excess cash = €25m; diluted shares = 50m.

| Year | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| FCFF (€m) | 42 | 47 | 52 | 56 | 60 |

1. Calculate FCFF6 and terminal value at the end of Year 5.
2. Calculate the present value of explicit FCFF and terminal value.
3. Calculate enterprise value.
4. Bridge to equity value and calculate value per share.

**Réponses :** [[1. FCFF6 = 61.50 ; TV5 = 1 025.00]] · [[2. PV explicites = 199.66 ; PV(TV) = 681.67]] · [[3. EV = 881.33]] · [[4. Equity = 726.33 → 14.53 €/action]]

**Explication très détaillée :**
- **Q1.** La période « stable » commence **après** l'année 5 : le premier flux de la perpétuité est donc FCFF6 = FCFF5 × (1+g) = 60 × 1.025 = **61.50**. La terminal value est la formule de Gordon appliquée à la firme : TV5 = FCFF6 ÷ (WACC − g) = 61.50 ÷ (0.085 − 0.025) = 61.50 ÷ 0.06 = **1 025.00**. *Pourquoi n+1 :* la perpétuité valorise **tous les flux à partir de l'année 6**, et ce paquet vaut, par construction, à la **fin de l'année 5** (d'où l'indice 5). *Pourquoi WACC et pas Ke :* le FCFF appartient à tous les financeurs → son taux d'opportunité est le WACC.
- **Q2.** Chaque flux explicite revient à aujourd'hui avec son propre facteur : 42/1.085 = 38.71 ; 47/1.085² = 39.99 ; 52/1.085³ = 40.85 ; 56/1.085⁴ = 40.57 ; 60/1.085⁵ = 40.54 → total **199.66**. La TV5 (1 025.00) est un montant **de fin d'année 5** : il faut la discounté 5 fois, 1 025 ÷ 1.085⁵ = 1 025 ÷ 1.503657 ≈ **681.67**. L'erreur classique est d'oublier ce second discounting.
- **Q3.** EV = 199.66 + 681.67 = **881.33**. C'est la valeur de l'outil **opérationnel** : la somme des deux blocs de flux actualisés.
- **Q4.** Le pont : equity = EV − debt + excess cash = 881.33 − 180 + 25 = **726.33**. *Pourquoi − debt :* la dette a un claim prioritaire que les FCFF n'ont pas rémunéré séparément (ils sont avant dette). *Pourquoi + cash :* le cash excédentaire ne produit **aucun** des FCFF projetés → il n'est pas dans l'EV → on l'ajoute. Par action : 726.33 ÷ 50 = **14.53**.

## Exercise 2. Build FCFF from Operating Forecasts

Year-0 revenue is €1,000m. Tax rate = 25%; D&A = 4.0% of revenue; CapEx = 5.5% of revenue; operating NWC = 12% of revenue. WACC = 9.0%; terminal growth = 2.5%.

| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Revenue growth | 8% | 7% | 6% | 5% | 4% |
| EBIT margin | 14.0% | 14.5% | 15.0% | 15.5% | 16.0% |

1. Forecast revenue, EBIT and NOPAT for Years 1–5.
2. Calculate D&A, CapEx and ΔNWC (ΔNWC = 12% × (Revenueₜ − Revenueₜ₋₁)).
3. Calculate FCFF = NOPAT + D&A − CapEx − ΔNWC.
4. Calculate terminal value and enterprise value.

**Réponses :** [[1. Rev 1 080 / 1 155.6 / 1 224.9 / 1 286.2 / 1 337.6 · EBIT 151.2 / 167.6 / 183.7 / 199.4 / 214.0 · NOPAT 113.4 / 125.7 / 137.8 / 149.5 / 160.5]] · [[2. D&A 43.2→53.5 · CapEx 59.4→73.6 · ΔNWC 9.6 / 9.1 / 8.3 / 7.4 / 6.2]] · [[3. FCFF 87.6 / 99.3 / 111.1 / 122.9 / 134.3]] · [[4. TV5 = 2 117.45 ; EV = 1 800.23]]

**Explication très détaillée :**
- **Q1.** La chaîne se construit maillon par maillon : revenuₜ = revenuₜ₋₁ × (1+gₜ) (croissance **composée**, pas additive) ; EBITₜ = margeₜ × revenuₜ (la marge **monte** chaque année : c'est l'hypothèse d'amélioration) ; NOPATₜ = EBITₜ × (1 − 25 %) : c'est le profit opérationnel après impôt **mais avant toute considération de financement** — la brique de base du FCFF.
- **Q2.** D&A et CapEx sont donnés en % du revenu → simples multiplications. **ΔNWC est le point de bascule :** le NWC est un **stock** (12 % du revenu) ; ce qui coûte du cash c'est **l'augmentation** du stock : ΔNWCₜ = 12 % × (Revₜ − Revₜ₋₁). Ex. an 1 : 0.12 × (1 080 − 1 000) = 9.6. Quand la croissance ralentit (8 % → 4 %), ΔNWC **diminue** (9.6 → 6.2) : moins de cash immobilisé.
- **Q3.** FCFF = NOPAT + D&A (charge non cash qui revient) − CapEx (cash investi en actifs longs) − ΔNWC (cash immobilisé en working capital). An 1 : 113.4 + 43.2 − 59.4 − 9.6 = **87.6**. On voit la mécanique : la firme croît, donc CapEx > D&A et ΔNWC > 0 → le FCFF est **inférieur** au NOPAT.
- **Q4.** FCFF6 = 134.28 × 1.025 ≈ 137.64 ; TV5 = 137.64 ÷ (0.09 − 0.025) = 137.64 ÷ 0.065 = **2 117.45**. EV = Σ PV(FCFF à 9 %) + PV(TV5) = 424.05 + 1 376.18 = **1 800.23**. Note : ici le corrigé officiel utilise FCFF6 = FCFF5×1.025 **sans reconstruire le réinvestissement stable** (méthode « grow the FCFF ») — les deux méthodes (celle-ci et celle de l'exo 5) coexistent ; au midterm, suis **la consigne de l'énoncé**.

## Exercise 3. FCFE Valuation with Net Borrowing

Cost of equity = 10.0%; perpetual growth after Year 5 = 3.0%; diluted shares = 40m.

| €m | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Net income | 80 | 88 | 96 | 103 | 109 |
| D&A | 20 | 21 | 22 | 23 | 24 |
| CapEx | 30 | 32 | 34 | 35 | 36 |
| ΔNWC | 5 | 6 | 6 | 7 | 7 |
| Net borrowing | 8 | 5 | 2 | 0 | 0 |

1. Calculate FCFE for each year.
2. Calculate terminal equity value at the end of Year 5.
3. Calculate equity value directly.
4. Calculate intrinsic value per share. Do not subtract debt again.

**Réponses :** [[1. FCFE 73 / 76 / 80 / 84 / 90]] · [[2. TV equity5 = 1 324.29]] · [[3. Equity = 1 124.81]] · [[4. 28.12 €/action]]

**Explication très détaillée :**
- **Q1.** FCFE = Net Income + D&A − CapEx − ΔNWC + Net Borrowing. An 1 : 80 + 20 − 30 − 5 + 8 = **73**. *Pourquoi + net borrowing :* le FCFE est le cash **pour les actionnaires** ; un emprunt nouveau fait entrer du cash qui leur est disponible, un remboursement en sortirait. Les années 4-5 (borrowing = 0) : la firme ne s'endette plus → FCFE = NI + D&A − CapEx − ΔNWC.
- **Q2.** TV equity5 = FCFE₆ ÷ (Ke − g) = 90 × 1.03 ÷ (0.10 − 0.03) = 92.7 ÷ 0.07 = **1 324.29**. *Pourquoi Ke :* le flux est un flux equity → taux equity.
- **Q3.** PV des FCFE à 10 % : 73/1.1 = 66.36 ; 76/1.21 = 62.81 ; 80/1.331 = 60.11 ; 84/1.4641 = 57.37 ; 90/1.61051 = 55.88 → 302.53. PV(TV) = 1 324.29 ÷ 1.61051 = 822.28. Equity = **1 124.81**.
- **Q4.** 1 124.81 ÷ 40 = **28.12**. *Ne pas soustraire la dette :* elle est **déjà** traitée dans le flux (via le net borrowing) et dans le taux (Ke) — la resoustraire compterait deux fois le claim des prêteurs.

## Exercise 4. FCFF versus FCFE — Match Cash Flow and Discount Rate

After Year 3, both FCFF and FCFE grow at 2.5% perpetually. WACC = 8.0%; cost of equity = 10.0%.

| €m | Y1 | Y2 | Y3 |
|---|---|---|---|
| FCFF | 70 | 76 | 82 |
| FCFE | 42 | 46 | 50 |

1. Value the firm using FCFF and WACC.
2. Value common equity directly using FCFE and the cost of equity.
3. State why the two calculations use different discount rates and produce different valuation objects.
4. Identify the error if FCFF were discounted at the cost of equity.

**Réponses :** [[1. EV = 1 408.19]] · [[2. Equity = 627.16]] · [[3. flux ↔ taux ↔ objet : FCFF→WACC→EV ; FCFE→Ke→equity]] · [[4. mismatch : ni EV ni equity corrects]]

**Explication très détaillée :**
- **Q1.** PV(FCFF) = 70/1.08 + 76/1.08² + 82/1.08³ = 64.81 + 65.16 + 65.08 = 195.05. TV3 = 82 × 1.025 ÷ (0.08 − 0.025) = 84.05 ÷ 0.055 = 1 528.18 ; PV = 1 528.18 ÷ 1.259712 = 1 213.13. **EV = 1 408.19**.
- **Q2.** PV(FCFE) = 42/1.1 + 46/1.21 + 50/1.331 = 38.18 + 38.02 + 37.57 = 113.77. TV3 = 50 × 1.025 ÷ (0.10 − 0.025) = 51.25 ÷ 0.075 = 683.33 ; PV = 513.40. **Equity = 627.16**.
- **Q3.** Le FCFF est le cash de **tous** les financeurs (dette + equity) → son risque combiné = WACC → il produit la valeur de **toute** la firme (EV). Le FCFE est le **résidu** après la dette → risque equity seul = Ke → il produit **directement** l'equity. La différence EV − equity (≈ 781) correspond à la valeur du claim de la dette nette du financement.
- **Q4.** Discounter FCFF à Ke applique un taux « actionnaires » à un flux « tous financeurs » : le numérateur et le dénominateur ne racontent plus la même histoire → le résultat n'est ni l'EV ni l'equity. C'est l'erreur de framework la plus sanctionnée.

## Exercise 5. Build the First Stable-Year FCFF

At the end of Year 5, NOPAT is €150m. Stable growth from Year 6 onward is 3.0%, stable ROIC is 10.0%, stable WACC is 8.0%.

1. Calculate Year-6 NOPAT. 2. Calculate the stable reinvestment rate using g/ROIC. 3. Calculate Year-6 reinvestment and FCFF. 4. Calculate terminal value at the end of Year 5. 5. Explain why mechanically growing Year-5 FCFF is not necessary when stable economics are built explicitly.

**Réponses :** [[1. 154.50]] · [[2. 30 %]] · [[3. Réinv. 46.35 ; FCFF6 = 108.15]] · [[4. TV5 = 2 163.00]] · [[5. RR stable = g/ROIC impose le réinvestissement ; grower FCFF5 imposerait un RR incohérent]]

**Explication très détaillée :**
- **Q1.** NOPAT6 = 150 × 1.03 = **154.50** : la croissance stable s'applique au NOPAT de l'année 5.
- **Q2.** Rappel de la relation fondamentale **g = RR × ROIC** → RR = g ÷ ROIC = 3 % ÷ 10 % = **30 %**. Sens : pour croître de 3 % avec des investissements qui rapportent 10 %, il faut réinvestir 30 % du NOPAT.
- **Q3.** Réinvestissement6 = 154.50 × 30 % = **46.35** ; FCFF6 = NOPAT6 − Réinv. = 154.50 − 46.35 = **108.15**.
- **Q4.** TV5 = 108.15 ÷ (0.08 − 0.03) = 108.15 ÷ 0.05 = **2 163.00**.
- **Q5.** Pendant la période explicite, le RR reflète une croissance **forte** (souvent > 30-40 %). Si on faisait FCFF5 × 1.03, on garderait implicitement l'ancien RR : incohérent avec « g = 3 %, ROIC = 10 % ». La méthode de la session 3 consiste donc à **reconstruire** l'année 6 à partir de l'économie stable (NOPAT, g, ROIC), pas à prolonger mécaniquement.

## Exercise 6. Full DCF with Sustainable Terminal Economics

WACC = 8.5%. Year-5 NOPAT is €170m. From Year 6: stable growth = 2.5%, stable ROIC = 10.0%.

| Year | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| FCFF (€m) | 80 | 92 | 104 | 114 | 122 |

1. PV of explicit FCFF. 2. Build Year-6 NOPAT, reinvestment rate, reinvestment, FCFF. 3. TV and its PV. 4. Enterprise value. 5. Percentage of EV from PV(TV).

**Réponses :** [[1. 396.70]] · [[2. NOPAT6 = 174.25 ; RR = 25 % ; réinv. = 43.56 ; FCFF6 = 130.69]] · [[3. TV5 = 2 178.12 ; PV = 1 448.55]] · [[4. EV = 1 845.25]] · [[5. 78.5 %]]

**Explication très détaillée :**
- **Q1.** 80/1.085 = 73.73 ; 92/1.177225 = 78.15 ; 104/1.277289 = 81.42 ; 114/1.385859 = 82.26 ; 122/1.503657 = 81.14 → **396.70**. (Le flux de l'an 5 discounté « moins » en valeur que l'an 4 ? Non : 81.14 < 82.26 car le facteur 1.085⁵ pèse plus — vérifie toujours l'ordre de grandeur.)
- **Q2.** NOPAT6 = 170 × 1.025 = **174.25** ; RR = 2.5 % ÷ 10 % = **25 %** ; réinv. = 174.25 × 25 % = **43.56** ; FCFF6 = 174.25 − 43.56 = **130.69**.
- **Q3.** TV5 = 130.69 ÷ (0.085 − 0.025) = 130.69 ÷ 0.06 = **2 178.12** ; PV = 2 178.12 ÷ 1.085⁵ = **1 448.55** (discountée **5** fois : c'est une valeur de fin d'an 5).
- **Q4.** EV = 396.70 + 1 448.55 = **1 845.25**.
- **Q5.** 1 448.55 ÷ 1 845.25 = **78.5 %**. *Interprétation :* normal pour un going concern (5 ans de flux explicites vs des décennées après). Ce n'est **pas** un motif de rejet : c'est un motif d'**inspection** de g, ROIC, marge et WACC (les 4 checks de la session 3).

## Exercise 7. Implied Terminal Multiple as a DCF Cross-Check

Use Exercise 6. Year-5 EBITDA is €180m.

1. Implied terminal EV/EBITDA. 2. What it tells you. 3. If a mature benchmark were materially below, what would you investigate first?

**Réponses :** [[1. 12.10×]] · [[2. diagnostic de cohérence des hypothèses stables]] · [[3. g, RR/ROIC, marge terminale, WACC]]

**Explication très détaillée :**
- **Q1.** 2 178.12 ÷ 180 = **12.10×**. On divise la TV **intrinsèque** par l'EBITDA terminal : ça traduit le DCF en langage de marché.
- **Q2.** Si 12× est dans la zone des multiples de firmes matures comparables → les hypothèses stables (g, ROIC, réinvestissement, marge, WACC) sont **crédibles**. Si c'est très au-dessus → le DCF « paie » une histoire trop généreuse. Le multiple est un **thermomètre**, pas la valo.
- **Q3.** Ordre d'inspection : **g trop haut** (le dénominateur WACC−g fond), **RR trop basse / ROIC trop optimiste** (FCFF6 gonflé), **marge terminale au pic de cycle**, **WACC trop bas**. Jamais l'inverse : on ne remplace pas la TV par « 10× EBITDA » pour faire joli.

## Exercise 8. WACC × Growth Sensitivity with Reinvestment Consistency

Explicit FCFF from Exercise 6; Year-5 NOPAT = €170m; stable ROIC = 10%. For every g, first recalculate RR = g/ROIC and Year-6 FCFF. Complete the 3×3 EV table; identify highest/lowest; explain why changing g must change stable reinvestment when ROIC is fixed.

| | g=2.0% | g=2.5% | g=3.0% |
|---|---|---|---|
| WACC=8.0% | 1 975.84 | 2 019.49 | [[2 070.71 (max)]] |
| WACC=8.5% | 1 816.01 | 1 845.25 | 1 878.78 |
| WACC=9.0% | [[1 679.17 (min)]] | 1 697.93 | 1 718.89 |

**Explication très détaillée :**
- **Méthode par case (5 étapes) :** RR = g ÷ 10 % ; NOPAT6 = 170 × (1+g) ; FCFF6 = NOPAT6 × (1 − RR) ; TV5 = FCFF6 ÷ (WACC − g) ; EV = PV des flux explicites **à CE WACC** + TV5 ÷ (1+WACC)⁵.
- **Détail case max (g 3 %, WACC 8 %) :** RR 30 % ; NOPAT6 = 175.1 ; FCFF6 = 122.57 ; TV5 = 122.57 ÷ 0.05 = 2 451.4 ; PV explicites à 8 % = 402.33 (attention : le WACC changeant, **les flux explicites se re-discountent aussi**) ; PV(TV) = 2 451.4 ÷ 1.08⁵ = 1 668.4 ; EV ≈ **2 070.71**.
- **Détail case min (g 2 %, WACC 9 %) :** RR 20 % ; NOPAT6 = 173.4 ; FCFF6 = 138.72 ; TV5 = 138.72 ÷ 0.07 = 1 981.7 ; PV explicites à 9 % = 389.0 ; PV(TV) = 1 290.1 ; EV ≈ **1 679.17**.
- **Pourquoi RR doit bouger avec g :** l'économie stable dit g = RR × ROIC. À ROIC fixé (10 %), choisir g = 3 % **implique** RR = 30 % ; garder l'ancien RR produirait deux valeurs de g contradictoires dans le même bloc terminal.

## Exercise 9. Enterprise Value to Common Equity Value

EV = €2,400m. Debt = €500m; excess cash = €120m; non-controlling interests = €40m; non-operating investments = €35m; diluted shares = 100m.

1. Common equity value. 2. Value per diluted share. 3. Why debt is subtracted after FCFF but not again after FCFE.

**Réponses :** [[1. 2 015.00]] · [[2. 20.15]] · [[3. la dette n'est pas dans les FCFF ; elle est déjà dans les FCFE]]

**Explication très détaillée :**
- **Q1.** Equity = 2 400 − 500 (dette) + 120 (cash excéd.) − 40 (**NCI** : des actionnaires minoritaires ont un claim prioritaire sur une partie des actifs) + 35 (investissements non opérationnels, hors des FCFF) = **2 015.00**.
- **Q2.** 2 015 ÷ 100 = **20.15** (actions **diluées** : cohérent avec les claims qui peuvent diluer).
- **Q3.** Après un FCFF, l'EV rémunère dette + equity mais les flux ignorent la dette → on soustrait le claim dette **une fois**. Après un FCFE, le flux a déjà ajouté/retiré le net borrowing et le taux est Ke → l'output **est** l'equity : resoustraire la dette = double compte.

## Exercise 10. Integrated DCF Master Case

Year-0 revenue €1,200m. Tax 25%; D&A = 3.5% of revenue; CapEx = 5.0% of revenue; operating NWC = 10% of revenue. WACC = 8.5%. Debt = €350m; excess cash = €90m; diluted shares = 75m. Stable: g = 2.5%, ROIC = 11.0%.

| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Revenue growth | 9.0% | 7.5% | 6.0% | 5.0% | 4.0% |
| EBIT margin | 15.0% | 15.5% | 16.0% | 16.5% | 17.0% |

1. Forecast revenue, EBIT, NOPAT, D&A, CapEx, ΔNWC and FCFF for Years 1–5. 2. Build Year-6 FCFF from stable economics. 3. TV, PV(TV), EV. 4. Bridge to equity and value per share. 5. Implied terminal EV/EBITDA (Year-5 EBITDA). 6. % of EV from TV and strongest sensitivity candidates.

**Réponses :** [[1. table complète ci-dessous]] · [[2. NOPAT6 = 212.71 ; RR = 22.73 % ; FCFF6 = 164.36]] · [[3. TV5 = 2 739.39 ; PV = 1 821.82 ; EV = 2 392.96]] · [[4. Equity = 2 132.96 → 28.44 €]] · [[5. 8.21×]] · [[6. 76.13 % ; tester WACC, g, ROIC/RR, marge terminale]]

| M€ | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Revenue | 1 308.0 | 1 406.1 | 1 490.5 | 1 565.0 | 1 627.6 |
| EBIT | 196.2 | 217.9 | 238.5 | 258.2 | 276.7 |
| NOPAT | 147.2 | 163.5 | 178.9 | 193.7 | 207.5 |
| D&A | 45.8 | 49.2 | 52.2 | 54.8 | 57.0 |
| CapEx | 65.4 | 70.3 | 74.5 | 78.3 | 81.4 |
| ΔNWC | 10.8 | 9.8 | 8.4 | 7.5 | 6.3 |
| **FCFF** | **116.7** | **132.6** | **148.1** | **162.7** | **176.9** |

**Explication très détaillée :**
- **Q1.** Même chaîne que l'exo 2 : revenu composé → EBIT par marge → NOPAT × 0.75 → FCFF = NOPAT + D&A − CapEx − ΔNWC. Ex. an 1 : 147.15 + 45.78 − 65.40 − 10.80 = 116.73. ΔNWC an 1 = 10 % × (1 308 − 1 200) = 10.8.
- **Q2.** NOPAT6 = 207.52 × 1.025 = 212.71 ; RR = 2.5 ÷ 11 = 22.73 % ; réinv. = 48.34 ; FCFF6 = 212.71 − 48.34 = **164.36**.
- **Q3.** TV5 = 164.36 ÷ (0.085 − 0.025) = 164.36 ÷ 0.06 = 2 739.39 ; PV = 2 739.39 ÷ 1.085⁵ = 1 821.82 ; PV explicites = 571.14 ; **EV = 2 392.96**.
- **Q4.** Equity = 2 392.96 − 350 + 90 = 2 132.96 ; ÷ 75 = **28.44 €**.
- **Q5.** EBITDA5 = EBIT5 + D&A5 = 276.69 + 56.97 = 333.66 ; 2 739.39 ÷ 333.66 = **8.21×** → sobre pour une firme mature → hypothèses stables crédibles.
- **Q6.** 1 821.82 ÷ 2 392.96 = **76.13 %** → sensibilité prioritaire : **WACC, g stable, ROIC/RR stable, marge terminale** (ce sont eux qui font bouger le bloc terminal).

---

## Part II — Dividend Discount Models

**Rappels de formules (Session 3) :** P₀ = Σ Dₜ/(1+Ke)ᵗ · zéro croissance P₀ = D/Ke · Gordon P₀ = D₁/(Ke−g) · g = rétention × ROE · rétention = 1 − payout.

## Exercise 11. Zero-Growth Dividend Perpetuity

Constant dividend €2.40; ke = 8.0%; market price €27.50. 1. Intrinsic value. 2. % difference vs market.

**Réponses :** [[1. 30.00]] · [[2. +9.09 %]]

**Explication très détaillée :**
- **Q1.** Dividende constant pour toujours = perpétuité simple : P₀ = D ÷ ke = 2.40 ÷ 0.08 = **30.00**. Pas de g : le dénominateur est ke seul.
- **Q2.** (30.00 − 27.50) ÷ 27.50 = 0.0909 = **+9.09 %** → sous ces hypothèses, le marché serait **en dessous** de l'intrinsèque (undervalued). Le sens du calcul : (intrinsèque − marché) ÷ marché.

## Exercise 12. Gordon Growth Model

D0 = €2.50; g = 4.0%; ke = 9.0%. 1. D1. 2. P0. 3. Dividend yield and capital-gain yield.

**Réponses :** [[1. 2.60]] · [[2. 52.00]] · [[3. yield 5 % + g 4 % = ke 9 %]]

**Explication très détaillée :**
- **Q1.** Gordon valorise le dividende **à venir** : D₁ = D₀(1+g) = 2.50 × 1.04 = **2.60**. Utiliser D₀ au numérateur est LE piège.
- **Q2.** P₀ = 2.60 ÷ (0.09 − 0.04) = 2.60 ÷ 0.05 = **52.00**.
- **Q3.** Dividend yield = D₁/P₀ = 2.60/52 = 5 % ; sous croissance constante, le prix croît à g = 4 % → capital gain 4 % ; 5 % + 4 % = 9 % = ke : **décomposition du retour attendu** (le modèle est cohérent par construction).

## Exercise 13. Market-Implied Constant Growth

P0 = €60.00; D0 = €2.40; ke = 9.0%. 1. Solve for g. 2. Check ke > g. 3. Verify D1/(ke−g) = 60.

**Réponses :** [[1. g = 4.81 %]] · [[2. 9 % > 4.81 % ✓]] · [[3. 2.5154/0.0419 = 60.00 ✓]]

**Explication très détaillée :**
- **Q1.** Reverse engineering : 60 = 2.40(1+g)/(0.09−g) → 60×0.09 − 60g = 2.40 + 2.40g → 5.40 − 2.40 = 62.40g → g = 3.00/62.40 = **4.81 %**. Le prix du marché « contient » cette attente de croissance.
- **Q2.** ke 9 % > g 4.81 % → dénominateur positif, modèle valide.
- **Q3.** D₁ = 2.40 × 1.0481 = 2.5154 ; 2.5154 ÷ (0.09 − 0.0481) = 2.5154 ÷ 0.0419 ≈ **60.00** : la boucle est bouclée.

## Exercise 14. Sustainable Growth and Intrinsic Value

EPS0 = €5.00; payout 40%; ROE 15%; ke 10.5%. 1. Retention. 2. g. 3. D0, D1. 4. P0. 5. Check ke > g.

**Réponses :** [[1. 60 %]] · [[2. 9 %]] · [[3. D0 = 2.00 ; D1 = 2.18]] · [[4. 145.33]] · [[5. oui, mais spread 1.5 pt → ultra-sensible]]

**Explication très détaillée :**
- **Q1-2.** Rétention = 1 − 0.40 = 60 % ; g = 0.60 × 0.15 = **9 %** : la croissance durable vient des bénéfices **retenus** réinvestis au ROE.
- **Q3.** D₀ = 5.00 × 0.40 = 2.00 ; D₁ = 2.00 × 1.09 = **2.18**.
- **Q4.** P₀ = 2.18 ÷ (0.105 − 0.09) = 2.18 ÷ 0.015 = **145.33**.
- **Q5.** ke > g oui (10.5 > 9) → mathématiquement OK ; mais un spread de 1.5 pt rend P₀ **explosif** : ±0.5 pt de g change tout → c'est un signal d'alerte, pas une valo confortable.

## Exercise 15. Required Payout Policy for a Target Growth Rate

ROE 15%; target g 6%; EPS0 €4.00; ke 10%. 1. Retention required. 2. Payout. 3. D0, D1. 4. P0. 5. Why higher g requires lower payout at fixed ROE.

**Réponses :** [[1. 40 %]] · [[2. 60 %]] · [[3. D0 = 2.40 ; D1 = 2.544]] · [[4. 63.60]] · [[5. g = RR×ROE : à ROE fixé, g ↑ ⇒ RR ↑ ⇒ payout ↓]]

**Explication très détaillée :**
- **Q1.** g = RR × ROE → RR = g ÷ ROE = 6 ÷ 15 = **40 %**.
- **Q2.** Payout = 1 − 0.40 = **60 %**.
- **Q3.** D₀ = 4.00 × 0.60 = 2.40 ; D₁ = 2.40 × 1.06 = **2.544**.
- **Q4.** P₀ = 2.544 ÷ (0.10 − 0.06) = **63.60**.
- **Q5.** À ROE constant, la seule source de croissance est la rétention : viser 8 % exigerait RR = 8/15 = 53.3 % → payout 46.7 %. **Plus de croissance = moins de distribution.**

## Exercise 16. Two-Stage DDM

D0 = €1.50; 12% for Years 1–3; stable 4%; ke 10%. 1. D1-D3. 2. D4. 3. P3. 4. Discount. 5. P0 and TV share.

**Réponses :** [[1. 1.68 / 1.8816 / 2.1074]] · [[2. 2.1917]] · [[3. 36.5281]] · [[4. PV = 1.5273 + 1.5550 + 1.5833 + 27.4442]] · [[5. P0 = 32.11 ; part TV 85.47 %]]

**Explication très détaillée :**
- **Q1-2.** Chaque dividende explicite compose le précédent : D₁ = 1.5×1.12 ; D₂ = D₁×1.12 ; D₃ = D₂×1.12. D₄ = D₃×1.04 : premier dividende **stable** — c'est lui qui entre dans Gordon.
- **Q3.** P₃ = D₄ ÷ (0.10 − 0.04) = 2.1917 ÷ 0.06 = **36.5281** : valeur **en fin d'année 3** de tous les dividendes à partir de l'année 4.
- **Q4.** P₃ se discounte **3 fois** (comme D₃) : 36.5281 ÷ 1.1³ = 27.4442.
- **Q5.** P₀ = **32.11** ; la TV pèse 85.47 % → cohérent avec un DDM (la valeur d'une action vient surtout du long terme) ; on checke surtout g et ke.

## Exercise 17. Varying Growth Rates Before Stability

D0 = €1.80; growth 15/12/9/6% Years 1–4; stable 3.5%; ke 9.5%. 1. D1-D5. 2. P4. 3. PVs. 4. P0. 5. TV share.

**Réponses :** [[1. 2.07 / 2.3184 / 2.5271 / 2.6787 / 2.7724]] · [[2. 46.2072]] · [[3. 1.8904 / 1.9336 / 1.9247 / 1.8632 / 32.1406]] · [[4. 39.75]] · [[5. 80.85 %]]

**Explication très détaillée :**
- **Q1.** Chaque taux s'applique au dividende **précédent** : D₁ = 1.8×1.15 ; D₂ = D₁×1.12 ; etc. D₅ = D×1.035 = premier dividende stable → c'est lui qui nourrit Gordon.
- **Q2.** P₄ = 2.7724 ÷ (0.095 − 0.035) = 2.7724 ÷ 0.06 = **46.2072**.
- **Q3-4.** Chaque PV à sa puissance : D₁/1.095, D₂/1.095²… P₄/1.095⁴ = 32.1406 ; P₀ ≈ **39.75**.
- **Q5.** 32.14 ÷ 39.75 = **80.85 %**.

## Exercise 18. Changing ROE, Payout and Growth

EPS0 = €4.50. Y1: ROE 18%/payout 30% ; Y2: 16%/35% ; Y3: 14%/40% ; Y4: 12%/50%. Stable: ROE 10%/payout 60%. ke explicit 10.5%; stable ke 9%.

**Réponses :** [[g = 12.6/10.4/8.4/6 % · EPS 5.067/5.594/6.064/6.428 · D 1.520/1.958/2.426/3.214]] · [[P4 = 80.2176]] · [[P0 = 60.74]] · [[part TV 88.59 %]]

**Explication très détaillée :**
- **Chaque année a SON gₜ = (1 − payoutₜ) × ROEₜ**, donc SON EPSₜ = EPSₜ₋₁ × (1+gₜ), et SON dividende Dₜ = EPSₜ × payoutₜ. An 1 : g = 0.70×0.18 = 12.6 % ; EPS₁ = 4.5×1.126 = 5.067 ; D₁ = 5.067×0.30 = 1.5201. Et ainsi de suite — la mécanique g→EPS→D se répète avec les paramètres de l'année.
- **Stable :** g = 0.40×0.10 = 4 % ; EPS₅ = 6.4277×1.04 = 6.6848 ; D₅ = 6.6848×0.60 = 4.0109 ; P₄ = 4.0109 ÷ (0.09−0.04) = **80.2176**.
- **Discount :** P₄ est une valeur d'année 4 → tout se discounte au ke **explicite** 10.5 % (P₄ ÷ 1.105⁴). Le ke stable 9 % ne sert **qu'à calculer P₄**. P₀ = **60.74** ; part TV **88.59 %**.

## Exercise 19. Multi-Stage DDM with a Changing Cost of Equity

D0 = €1.20; growth 20/20/12/7%; stable 3%. ke: 12/12/11/10%; stable ke 9%.

**Réponses :** [[D1-D5 = 1.44 / 1.728 / 1.9354 / 2.0708 / 2.1330]] · [[P4 = 35.5493]] · [[facteurs cumulés 1.12 / 1.2544 / 1.3924 / 1.5316]] · [[P0 ≈ 28.62]]

**Explication très détaillée :**
- **Q1-2.** Dividendes : composition successive ; P₄ = D₅ ÷ (0.09 − 0.03) = 2.1330 ÷ 0.06 = **35.5493** (ke **stable** pour P₄).
- **Q3.** Quand ke change chaque année, (1+ke)ᵗ est **faux** : on multiplie les facteurs : an 2 = 1.12×1.12 = 1.2544 ; an 3 = 1.2544×1.11 = 1.3924 ; an 4 = 1.3924×1.10 = 1.5316. P₄ (valeur d'an 4) utilise le facteur an 4.
- **Q4-5.** P₀ = 1.44/1.12 + 1.728/1.2544 + 1.9354/1.3924 + 2.0708/1.5316 + 35.5493/1.5316 ≈ **28.62**.

## Exercise 20. Integrated ROE–Payout–DDM Valuation

EPS0 = €6.00. Y1-3: ROE 17%/payout 35%; Y4: 14%/45%; Y5: 12%/55%. Stable ROE 10%/payout 60%. ke 10.5% (Y1-5), 9% stable.

**Réponses :** [[g 1-3 = 11.05 % ; g4 = 7.7 % ; g5 = 5.4 % · EPS 6.663/7.399/8.217/8.850/9.327 · D 2.332/2.590/2.876/3.982/5.130]] · [[g stable 4 % ; D6 = 5.8203 ; P5 = 116.4067]] · [[P0 ≈ 82.81]] · [[part TV 85.33 %]]

**Explication très détaillée :** même moteur que l'exo 18 sur 5 années explicites : gₜ = (1−payoutₜ)×ROEₜ ; EPS compose ; Dₜ = EPSₜ×payoutₜ. Années 1-3 partagent le même couple (17/35) → même g 11.05 %. P₅ = D₆ ÷ (0.09−0.04), avec D₆ = EPS₅×1.04×0.60 = 5.8203 → **116.4067** ; tout se discounte à 10.5 % (P₅ ÷ 1.105⁵) ; P₀ ≈ **82.81** ; part TV **85.33 %**.

## Exercise 21. Reverse Engineering Market Expectations

P0 = €48; D0 = €2.20; ke 9.5%; long-run ROE 12%; current EPS €4.50. 1. Implied g. 2. D1. 3. Retention required. 4. Payout. 5. Consistency check vs D0.

**Réponses :** [[1. g = 4.70 %]] · [[2. 2.3034]] · [[3. 39.18 %]] · [[4. 60.82 %]] · [[5. dividende implicite 2.74 ≠ 2.20 → incohérent]]

**Explication très détaillée :**
- **Q1.** 48 = 2.20(1+g)/(0.095−g) → 4.56 − 48g = 2.20 + 2.20g → 2.36 = 50.20g → g = **4.70 %**.
- **Q2.** D₁ = 2.20 × 1.047 = **2.3034**.
- **Q3.** Pour que 4.70 % soit **soutenable** au ROE 12 % : RR = g ÷ ROE = 4.70 ÷ 12 = **39.18 %**.
- **Q4.** Payout = 1 − 0.3918 = **60.82 %**.
- **Q5.** Avec EPS 4.50 et payout 60.82 %, le dividende « cohérent » serait 4.50 × 0.6082 ≈ **2.74** — mais le dividende réellement payé est 2.20. Écart ≈ 0.54 → le trio prix/ROE/EPS **ne raconte pas une histoire cohérente** avec un Gordon constant : soit le marché anticipe autre chose, soit payout/ROE diffèrent. C'est ça, le « reverse engineering » : lire les attentes **puis** les confronter aux fondamentaux.

## Exercise 22. Full Analyst Case: Transition to Stable Growth

EPS0 = €5.50. Y1-2: ROE 18%/payout 30%; Y3: 15%/40%; Y4: 12%/50%. Stable ROE 10%/payout 60%. ke 10% (Y1-4), 8.5% stable. Market price €78.

1-9 : croissance/EPS/D par année, g stable, EPS5/D5, P4, P0, part TV, comparaison marché, sensibilité g 3.5/4.5 %.

**Réponses :** [[g 12.6/12.6/9/6 % · EPS 6.193/6.973/7.601/8.057 · D 1.858/2.092/3.040/4.028]] · [[g stable 4 % ; D5 = 5.0276 ; P4 = 111.7233]] · [[P0 = 84.76]] · [[part TV 90.03 %]] · [[vs marché +8.67 %]] · [[sensibilité : 76.80 / 94.71]]

**Explication très détaillée :**
- **Q1.** Moteur g→EPS→D année par année (cf. exo 18). Années 1-2 : même couple → g 12.6 % deux fois.
- **Q2-3.** g stable = 0.40×0.10 = 4 % ; EPS₅ = 8.0569×1.04 = 8.3793 ; D₅ = 8.3793×0.60 = 5.0276.
- **Q4.** P₄ = 5.0276 ÷ (0.085 − 0.04) = 5.0276 ÷ 0.045 = **111.7233** (ke stable 8.5 %).
- **Q5.** PV des D₁-₄ à 10 % = 8.4537 ; PV(P₄) = 111.7233 ÷ 1.1⁴ = 76.3085 ; **P₀ = 84.76**.
- **Q6-7.** Part TV = 76.31 ÷ 84.76 = **90.03 %** ; vs marché : (84.76 − 78) ÷ 78 = **+8.67 %**.
- **Q8.** g 3.5 % → D₅ ≈ 5.0034, P₄ = 5.0034 ÷ 0.05 = 100.07 → P₀ ≈ **76.80** ; g 4.5 % → D₅ ≈ 5.0517, P₄ = 5.0517 ÷ 0.04 = 126.29 → P₀ ≈ **94.71**. Conclusion : ±0.5 pt de g = ±18 € alors que le marché est à 78 → **quand la TV pèse 90 %, g stable EST la valuation** : c'est L'hypothèse à défendre.

---

> **Fin de phase 1 atteinte quand :** les 22 exos refaits cache-cache avec 0 erreur de **méthode** (le chiffre se rattrape, la méthode non). Ensuite → phase 2 (définitions du cours + cas des TD).
