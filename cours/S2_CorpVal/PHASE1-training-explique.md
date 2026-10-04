# PHASE 1 — Le training corrigé, expliqué question par question (sans prérequis)

> **Méthode validée avec toi :** 3 phases, on n'en saute aucune.
> **PHASE 1 (ce doc) :** comprendre **chaque** réponse du training officiel (`Intrinsic_Valuation_Exercises` +
> `Solutions`), quasiment sans prérequis : le concept est re-expliqué de zéro, en bilingue, et chaque chiffre est justifié.
> Objectif : les réponses comprises par cœur. **PHASE 2 :** on adaptera (définitions du cours + cas/entreprises des TD).
> **PHASE 3 :** ≥ 3 blancs même timing, même style, même difficulté (sujet différent ok), objectif 18-20/20.
>
> Légende : chaque exo donne **Session exacte**, **Concept FR / EN**, puis **chaque question expliquée pas à pas**,
> et une **EN one-liner** pour fixer le vocabulaire du jour J (le midterm est en anglais).

---

## Exo 1 — FCFF valuation + pont EV→equity · **Session 3** (pont vu aussi **Session 1**)

> **Concept FR :** un DCF « firme » valorise d'abord **l'outil opérationnel** (Enterprise Value, EV) avec les flux FCFF
> discountés au WACC. Ensuite, un **pont** passe aux actionnaires : on retire ce qui appartient aux prêteurs (dette),
> on ajoute ce qui n'est pas dans les flux (cash excédentaire). **Concept EN :** *FCFF discounted at WACC gives
> enterprise value; the EV-to-equity bridge then subtracts debt and adds excess cash.*

**Q1 — FCFF₆ et TV₅.** La période stable commence **après** l'année 5 : le premier flux stable = FCFF₅ × (1+g) = 60 × 1,025 = **61,50**.
La terminal value est une perpétuité de Gordon appliquée à la firme : TV₅ = FCFF₆ ÷ (WACC − g) = 61,50 ÷ (0,085 − 0,025) = **1 025,00**.
*Pourquoi n+1 :* la formule valorise les flux **à partir de l'année 6**, mesurés **en fin d'année 5**.

**Q2 — PV et EV.** Chaque flux explicite se discounte à sa date : 42/1,085 + 47/1,085² + 52/1,085³ + 56/1,085⁴ + 60/1,085⁵ = **199,66**.
La TV₅ est un montant **en année 5** → on la discounte 5 fois : 1 025 ÷ 1,085⁵ = **681,67**. EV = 199,66 + 681,67 = **881,33**.

**Q3 — Bridge.** Equity = EV − dette + cash excédentaire = 881,33 − 180 + 25 = **726,33**.
*Pourquoi + cash :* ce cash ne génère **aucun** des FCFF valorisés → il s'ajoute séparément.

**Q4 — Par action.** 726,33 ÷ 50 M actions = **14,53 €**.

⚠️ Piège / *Trap :* mettre FCFF₅ au numérateur de la TV, ou oublier de discounter la TV₅.
🇧 *One-liner :* **Discount explicit flows and the terminal value separately; bridge EV to equity only once.**

---

## Exo 2 — Construire le FCFF depuis les prévisions · **Sessions 1-2** (NOPAT, marges, réinvestissement) + **Session 3** (discounting)

> **Concept FR :** on reconstruit la chaîne complète : **revenu → EBIT (marge) → NOPAT (impôt) → FCFF (− réinvestissement)**,
> où réinvestissement = CapEx net (CapEx − D&A) + variation de NWC. **Concept EN :** *Revenue × margin = EBIT; EBIT × (1−t) = NOPAT;
> NOPAT − reinvestment = FCFF.*

**Q1 — Revenu, EBIT, NOPAT.** Revenuₜ = revenuₜ₋₁ × (1+gₜ) : 1 080 / 1 155,6 / 1 224,9 / 1 286,2 / 1 337,6.
EBIT = marge × revenu : 151,2 / 167,6 / 183,7 / 199,4 / 214,0. NOPAT = EBIT × 0,75 : **113,4 / 125,7 / 137,8 / 149,5 / 160,5**.
*Pourquoi NOPAT :* c'est le profit opérationnel **après impôt mais avant financement** — la base du FCFF.

**Q2 — D&A, CapEx, ΔNWC.** D&A = 4 % du revenu (43,2 / 46,2 / 49,0 / 51,4 / 53,5) ; CapEx = 5,5 % (59,4 / 63,6 / 67,4 / 70,7 / 73,6) ;
ΔNWC = 12 % × (revenuₜ − revenuₜ₋₁) = **9,6 / 9,1 / 8,3 / 7,4 / 6,2** (le NWC est un **stock** : c'est sa **variation** qui coûte du cash).

**Q3 — FCFF.** FCFF = NOPAT + D&A − CapEx − ΔNWC :
an 1 : 113,4 + 43,2 − 59,4 − 9,6 = **87,6** ; puis **99,3 / 111,1 / 122,9 / 134,3**.
*Pourquoi + D&A :* charge non cash, elle revient au cash flow. *Pourquoi − CapEx et − ΔNWC :* ce sont les investissements qui **consomment** du cash.

**Q4 — TV et EV.** FCFF₆ = 134,28 × 1,025 = 137,64 ; TV₅ = 137,64 ÷ (0,09 − 0,025) = **2 117,45**.
EV = PV des 5 FCFF (à 9 %) + PV(TV₅) = 424,05 + 1 376,18 ≈ **1 800,23**.

⚠️ Piège / *Trap :* ΔNWC = 12 % du revenu (faux) au lieu de 12 % de **l'augmentation** du revenu.
🇬🇧 *One-liner :* **FCFF is NOPAT minus reinvestment; working-capital cost is the CHANGE in NWC, not the level.**

---

## Exo 3 — FCFE avec net borrowing · **Session 1** (définition FCFE) + **Session 3**

> **Concept FR :** FCFE = cash **restant pour les actionnaires** après opérations, investissements **et financement de la dette** :
> on **ajoute** les nouveaux emprunts (cash qui entre) et on **retire** implicitement les remboursements (ici inclus dans « net borrowing »).
> **Concept EN :** *FCFE = NI + D&A − CapEx − ΔNWC + net borrowing; discounted at Ke it gives equity value directly.*

**Q1 — FCFE par an.** An 1 : 80 + 20 − 30 − 5 + 8 = **73** ; puis **76 / 80 / 84 / 90**.
*Pourquoi + net borrowing :* une dette nouvelle apporte du cash **disponible pour l'equity** ; un remboursement en prendrait.

**Q2 — Terminal equity.** TV₅ = 90 × 1,03 ÷ (0,10 − 0,03) = **1 324,29**. Note : taux = **Ke (10 %)**, pas WACC — on valorise l'equity.

**Q3 — Equity value.** PV des FCFE à 10 % : 66,36 + 62,81 + 60,11 + 57,37 + 55,88 = 302,53 ; + PV(TV) 822,28 = **1 124,81**.

**Q4 — Par action.** 1 124,81 ÷ 40 = **28,12**. Et **on ne soustrait PAS la dette** : le FCFE a déjà traité la dette.

⚠️ Piège / *Trap :* re-soustraire la dette après un FCFE (double compte).
🇬🇧 *One-liner :* **FCFE already nets out debt flows — the output is equity value, no bridge needed.**

---

## Exo 4 — FCFF vs FCFE : le matching · **Session 3** (et 1)

> **Concept FR :** la règle cardinale : **flux ↔ taux ↔ objet**. FCFF (tous financeurs) → WACC → EV. FCFE (actionnaires) → Ke → equity.
> **Concept EN :** *Match the cash flow to its discount rate and its value object; crossing them is a framework error.*

**Q1 — FCFF/WACC.** PV(70, 76, 82 à 8 %) = 64,81 + 65,16 + 65,08 = 195,05 ; TV₃ = 82 × 1,025 ÷ (0,08 − 0,025) = 1 528,18 ;
PV(TV) = 1 528,18 ÷ 1,08³ = 1 213,13 ; **EV = 1 408,19**.

**Q2 — FCFE/Ke.** PV(42, 46, 50 à 10 %) = 38,18 + 38,02 + 37,57 = 113,77 ; TV₃ = 50 × 1,025 ÷ (0,10 − 0,025) = 683,33 ;
PV = 513,40 ; **equity = 627,16**.

**Q3 — Pourquoi différents.** Le FCFF appartient aussi aux prêteurs → leur coût d'opportunité combiné = WACC → valeur de **toute** la firme.
Le FCFE est le résidu actionnaires → risque equity = Ke → valeur **equity**. EV − equity ici ≈ valeur de la dette + financement.

**Q4 — L'erreur.** Discounter FCFF à Ke mélange un flux « tous financeurs » avec un taux « actionnaires » : ni EV ni equity corrects.

🇬 *One-liner :* **FCFF→WACC→EV; FCFE→Ke→equity. Never cross.**

---

## Exo 5 — Construire la première année stable · **Session 3**

> **Concept FR :** en terminal, on ne « prolonge » pas le FCFF₅ : on **reconstruit** FCFF₆ à partir de l'économie stable
> (NOPAT₆, puis réinvestissement imposé par g et ROIC). **Concept EN :** *Build the first stable-year FCFF from sustainable
> NOPAT and the reinvestment rate g/ROIC.*

**Q1.** NOPAT₆ = 150 × 1,03 = **154,50**.
**Q2.** RR stable = g ÷ ROIC = 3 % ÷ 10 % = **30 %** (rappel : g = RR × ROIC, donc RR = g/ROIC).
**Q3.** Réinvestissement₆ = 154,50 × 30 % = **46,35** ; FCFF₆ = 154,50 − 46,35 = **108,15**.
**Q4.** TV₅ = 108,15 ÷ (0,08 − 0,03) = **2 163,00**.
**Q5 — Pourquoi pas FCFF₅ × 1,03 ?** Parce que le RR de la période explicite (croissance forte) n'est pas celui de l'état stable :
grower mécaniquement imposerait un réinvestissement **incohérent** avec g = 3 % et ROIC = 10 %.

🇬 *One-liner :* **Stable growth requires stable reinvestment: RR = g/ROIC, then FCFF = NOPAT − reinvestment.**

---

## Exo 6 — DCF complet avec économie terminale soutenable · **Session 3**

**Q1.** PV explicites à 8,5 % : 73,73 + 78,15 + 81,42 + 82,26 + 81,14 = **396,70**.
**Q2.** NOPAT₆ = 170 × 1,025 = **174,25** ; RR = 2,5 % ÷ 10 % = **25 %** ; réinv. = **43,56** ; FCFF₆ = **130,69**.
**Q3.** TV₅ = 130,69 ÷ (0,085 − 0,025) = **2 178,12** ; PV = 2 178,12 ÷ 1,085⁵ = **1 448,55**.
**Q4.** EV = 396,70 + 1 448,55 = **1 845,25**.
**Q5.** Part de la TV = 1 448,55 ÷ 1 845,25 = **78,5 %** → normal pour un going concern ; on **inspecte** g/ROIC/marge, on ne rejette pas.

🇬 *One-liner :* **A large terminal share is a checklist trigger, not an error.**

---

## Exo 7 — Multiple implicite en cross-check · **Session 3**

> **Concept FR :** on traduit la TV intrinsèque en langage de marché (EV/EBITDA) pour **vérifier** la cohérence — jamais l'inverse.
> **Concept EN :** *The implied exit multiple is a diagnostic cross-check of the stable assumptions.*

**Q1.** 2 178,12 ÷ 180 = **12,10×**.
**Q2.** Si 12× est plausible pour une firme mature de ce secteur → les hypothèses stables (g, ROIC, marge, WACC) sont crédibles ;
sinon, le multiple agit comme une **alarme**.
**Q3.** Benchmark nettement plus bas → inspecter **d'abord** : g trop haut, RR trop basse (ROIC trop optimiste), marge terminale au pic, WACC trop bas.

🇬 *One-liner :* **Compute the multiple FROM the DCF; never set the DCF from a market multiple.**

---

## Exo 8 — Sensibilité WACC × g avec RR cohérente · **Sessions 2-3**

> **Concept FR :** dans une sensibilité, quand g change **à ROIC constant**, le réinvestissement stable doit changer aussi
> (RR = g/ROIC) — et le WACC changeant, **toute** la actualisation change (flux explicites ET TV). **Concept EN :**
> *Holding ROIC fixed, a new g implies a new stable reinvestment rate; a new WACC re-discounts everything.*

**Q1 — Méthode par case :** RR = g/10 % ; NOPAT₆ = 170 × (1+g) ; FCFF₆ = NOPAT₆ × (1 − RR) ; TV₅ = FCFF₆/(WACC − g) ;
EV = PV des flux explicites **à ce WACC** + TV₅/(1+WACC)⁵.
Résultats officiels : **EV max = 2 070,71** (g 3 %, WACC 8 %) ; **EV min = 1 679,17** (g 2 %, WACC 9 %).
*Exemple complet (g 3 %, WACC 8 %) :* RR 30 % ; NOPAT₆ 175,1 ; FCFF₆ 122,57 ; TV₅ 2 451,4 ; PV explicites à 8 % = 402,33 ;
PV(TV) 1 668,4 ; EV ≈ **2 070,7**.
**Q2.** Max/min ci-dessus — et la valeur **monte** quand g ↑ et WACC ↓ (dénominateur de la perpétuité qui fond).
**Q3.** Si on gardait la même RR en changeant g, l'économie stable dirait « g = RR × ROIC » avec deux valeurs de g : contradiction interne.

🇬 *One-liner :* **In the sensitivity table, g and reinvestment move together when ROIC is fixed.**

---

## Exo 9 — Pont complet avec NCI et actifs non-op · **Sessions 1-3**

**Q1.** Equity = 2 400 − 500 (dette) + 120 (cash) − 40 (**NCI** : claim d'autres actionnaires) + 35 (invest. non-op) = **2 015,00**.
**Q2.** 2 015 ÷ 100 = **20,15 €**.
**Q3.** Après FCFF, la dette n'a **pas** été comptée dans les flux → on la retire une fois. Après FCFE, elle l'est déjà → la resoustraire casserait le modèle.

🇬 *One-liner :* **Subtract every non-common claim once; add every asset the FCFF never captured.**

---

## Exo 10 — Master case intégrée · **Sessions 1-2-3** (tout le programme)

**Q1 — Table complète** (revenu → FCFF) :

| M€ | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Revenu | 1 308,0 | 1 406,1 | 1 490,5 | 1 565,0 | 1 627,6 |
| EBIT | 196,2 | 217,9 | 238,5 | 258,2 | 276,7 |
| NOPAT | 147,2 | 163,5 | 178,9 | 193,7 | **207,5** |
| D&A | 45,8 | 49,2 | 52,2 | 54,8 | 57,0 |
| CapEx | 65,4 | 70,3 | 74,5 | 78,3 | 81,4 |
| ΔNWC | 10,8 | 9,8 | 8,4 | 7,5 | 6,3 |
| **FCFF** | **116,7** | **132,6** | **148,1** | **162,7** | **176,9** |

**Q2 — Année stable.** NOPAT₆ = 207,52 × 1,025 = **212,71** ; RR = 2,5 % ÷ 11 % = **22,73 %** ; réinv. = **48,34** ; FCFF₆ = **164,36**.
**Q3 — TV et EV.** TV₅ = 164,36 ÷ (0,085 − 0,025) = **2 739,39** ; PV = **1 821,82** ; PV explicites = **571,14** ; **EV = 2 392,96**.
**Q4 — Bridge et par action.** Equity = 2 392,96 − 350 + 90 = **2 132,96** ; ÷ 75 = **28,44 €**.
**Q5 — Multiple implicite.** EBITDA₅ = EBIT + D&A = 276,69 + 56,97 = **333,66** ; 2 739,39 ÷ 333,66 = **8,21×** → sobre, cohérent avec une firme mature.
**Q6 — Part TV = 76,13 %** → tester en priorité : **WACC, g stable, ROIC/RR stables, marge terminale** (ce qui bouge le plus la valeur).

🇬 *One-liner :* **One coherent story: margins, growth, reinvestment and terminal economics must agree.**

---

## Exo 11 — Perpétuité sans croissance · **Session 3** (DDM)

> **Concept FR :** dividende constant pour toujours = perpétuité simple : P₀ = D ÷ ke. **Concept EN :** *Zero-growth DDM = perpetuity.*

**Q1.** P₀ = 2,40 ÷ 0,08 = **30,00 €**.
**Q2.** (30 − 27,50) ÷ 27,50 = **+9,09 %** → l'intrinsèque est au-dessus du marché : le titre serait **undervalued** sous ces hypothèses.

🇬🇧 *One-liner :* **Constant dividend forever: P = D/ke.**

---

## Exo 12 — Gordon Growth · **Session 3**

**Q1.** D₁ = D₀ × (1+g) = 2,50 × 1,04 = **2,60** (Gordon valorise le dividende **à venir**).
**Q2.** P₀ = 2,60 ÷ (0,09 − 0,04) = **52,00**.
**Q3.** Dividend yield = D₁/P₀ = 5 % ; capital gain = g = 4 % ; total = 9 % = ke → **décomposition du retour** : yield + g = ke.

🇬🇧 *One-liner :* **Total return = dividend yield + growth; use D₁, not D₀.**

---

## Exo 13 — Croissance implicite du marché · **Session 3**

> **Concept FR :** « reverse engineering » : si le marché a raison, quel g le prix de 60 € implique-t-il ? On résout l'équation de Gordon pour g.
> **Concept EN :** *Solve the Gordon equation backwards to read the market's implied growth.*

**Q1.** 60 = 2,40(1+g)/(0,09−g) → 60×0,09 − 60g = 2,40 + 2,40g → 5,40 − 2,40 = 62,40g → g = 3,00/62,40 = **4,81 %**.
**Q2.** ke 9 % > g 4,81 % ✓ (dénominateur positif, modèle valide).
**Q3.** D₁ = 2,40 × 1,0481 = 2,5154 ; 2,5154 ÷ (0,09 − 0,0481) = **60,00** ✓ → le marché « paie » ≈ 4,8 % de croissance perpétuelle.

🇬🇧 *One-liner :* **The price embeds a growth assumption — you can solve for it.**

---

## Exo 14 — Croissance soutenable = rétention × ROE · **Session 3**

> **Concept FR :** la croissance durable vient des bénéfices **retenus** réinvestis au ROE : g = (1 − payout) × ROE.
> **Concept EN :** *Sustainable growth = retention ratio × ROE.*

**Q1.** Rétention = 1 − 0,40 = **60 %**. **Q2.** g = 0,60 × 0,15 = **9 %**.
**Q3.** D₀ = 5,00 × 0,40 = 2,00 ; D₁ = 2,00 × 1,09 = **2,18**.
**Q4.** P₀ = 2,18 ÷ (0,105 − 0,09) = **145,33**.
**Q5.** ke − g = 1,5 pt seulement → P₀ **explosif et ultra-sensible** : un petit changement d'hypothèse renverse la conclusion.

🇬 *One-liner :* **When ke − g is tiny, value is a knife-edge — flag the sensitivity.**

---

## Exo 15 — Payout requis pour une cible de g · **Session 3**

**Q1.** RR = g ÷ ROE = 6 % ÷ 15 % = **40 %**. **Q2.** Payout = 1 − 0,40 = **60 %**.
**Q3.** D₀ = 4,00 × 0,60 = 2,40 ; D₁ = 2,40 × 1,06 = **2,544**. **Q4.** P₀ = 2,544 ÷ (0,10 − 0,06) = **63,60**.
**Q5.** À ROE fixé, viser g = 8 % exigerait RR = 53,3 % → payout 46,7 % : **plus de croissance = moins de distribution** (le cash reste dans la firme).

🇬 *One-liner :* **Target growth pins down the retention ratio at a given ROE.**

---

## Exo 16 — Two-stage DDM · **Session 3**

> **Concept FR :** croissance forte explicite (ans 1-3), puis Gordon à partir de D₄ ; P₃ se discounte 3 fois.
> **Concept EN :** *Explicit dividends, then Gordon at the stable start; discount the terminal back over the explicit years.*

**Q1.** D₁ = 1,68 ; D₂ = 1,8816 ; D₃ = 2,1074. **Q2.** D₄ = 2,1074 × 1,04 = 2,1917.
**Q3.** P₃ = 2,1917 ÷ (0,10 − 0,04) = **36,5281**.
**Q4.** PV : 1,5273 + 1,5550 + 1,5833 + PV(P₃) 27,4442. **Q5.** P₀ = **32,11** ; part TV = 27,44 ÷ 32,11 = **85,47 %**.

🇬 *One-liner :* **P₃ is a Year-3 value: discount it three periods.**

---

## Exo 17 — Croissances variables puis stabilité · **Session 3**

**Q1.** D₁ = 2,07 (+15 %) ; D₂ = 2,3184 (+12 %) ; D₃ = 2,5271 (+9 %) ; D₄ = 2,6787 (+6 %) ; D₅ = 2,7724 (+3,5 %).
**Q2.** P₄ = 2,7724 ÷ (0,095 − 0,035) = **46,2072** (Gordon démarre **avec D₅**).
**Q3.** PV(D₁..D₄) = 1,8904 + 1,9336 + 1,9247 + 1,8632 ; PV(P₄) = 32,1406.
**Q4.** P₀ ≈ **39,75**. **Q5.** Part TV ≈ **80,85 %**.

🇬 *One-liner :* **Each explicit growth rate compounds the previous dividend.**

---

## Exo 18 — ROE et payout qui changent chaque année · **Session 3**

> **Concept FR :** chaque année a son propre gₜ = (1 − payoutₜ) × ROEₜ, donc son EPSₜ = EPSₜ₋₁ × (1+gₜ) et son Dₜ = EPSₜ × payoutₜ.
> **Concept EN :** *Year-by-year g from that year's payout and ROE; dividends follow that year's payout.*

**Q1.** g = 12,6 % / 10,4 % / 8,4 % / 6,0 % ; EPS = 5,067 / 5,594 / 6,064 / 6,428.
**Q2.** D = 1,5201 / 1,9579 / 2,4255 / 3,2138.
**Q3.** g stable = (1 − 0,60) × 10 % = **4 %**. **Q4.** EPS₅ = 6,6848 ; D₅ = 4,0109 ; P₄ = 4,0109 ÷ (0,09 − 0,04) = **80,2176**.
**Q5.** P₄ est une valeur **d'année 4** → tout se discounte à **10,5 %** (ke explicite) : P₀ = **60,74**. **Q6.** Part TV ≈ **88,59 %**.

🇬 *One-liner :* **Discount the terminal at the explicit-period ke raised to the terminal year.**

---

## Exo 19 — Ke qui change chaque année → facteurs cumulés · **Session 3**

> **Concept FR :** si le taux requis change chaque année, on ne peut pas utiliser (1+ke)ᵗ : on **multiplie** les facteurs (1+ke₁)(1+ke₂)…
> **Concept EN :** *A changing discount rate requires cumulative discount factors.*

**Q1.** D₁..D₅ = 1,44 / 1,728 / 1,9354 / 2,0708 / 2,1330. **Q2.** P₄ = 2,1330 ÷ (0,09 − 0,03) = **35,5493**.
**Q3.** Facteurs : an 1 = 1,12 ; an 2 = 1,2544 ; an 3 = 1,3924 ; an 4 = 1,5316.
**Q4.** PV = 1,44/1,12 + 1,728/1,2544 + 1,9354/1,3924 + 2,0708/1,5316 + 35,5493/1,5316.
**Q5.** P₀ ≈ **28,62**.

🇬 *One-liner :* **Multiply the yearly (1+ke) factors; never power a single rate.**

---

## Exo 20 — ROE–payout–DDM intégré · **Session 3**

**Q1.** g ans 1-3 = 0,65 × 17 % = 11,05 % ; EPS 6,663 / 7,399 / 8,217 ; D 2,332 / 2,590 / 2,876 ;
an 4 : g 7,7 % → EPS 8,850, D 3,982 ; an 5 : g 5,4 % → EPS 9,327, D 5,130.
**Q2.** g stable = 0,40 × 10 % = **4 %**. **Q3.** EPS₆ = 9,7006 ; D₆ = 5,8203.
**Q4.** P₅ = 5,8203 ÷ (0,09 − 0,04) = **116,4067**. **Q5.** P₀ ≈ **82,81** (discount à 10,5 % sur 1-5). **Q6.** Part TV ≈ **85,33 %**.

🇬 *One-liner :* **Chain g → EPS → dividend year by year; the stable block starts one year after the last explicit dividend.**

---

## Exo 21 — Reverse engineering + check de cohérence · **Session 3**

**Q1.** 48 = 2,20(1+g)/(0,095−g) → 4,56 − 48g = 2,20 + 2,20g → 2,36 = 50,20g → g = **4,70 %**.
**Q2.** D₁ = 2,20 × 1,047 = **2,3034**.
**Q3.** RR = g ÷ ROE = 4,70 % ÷ 12 % = **39,18 %**. **Q4.** Payout = **60,82 %**.
**Q5.** Dividende implicite = EPS 4,50 × 60,82 % = **2,74** ≠ D₀ réel 2,20 (écart ≈ 0,54) → le trio « prix 48 / ROE 12 % / EPS 4,50 »
n'est **pas pleinement cohérent** avec un Gordon constant : soit le marché attend autre chose, soit ROE/payout diffèrent.

🇬 *One-liner :* **Implied growth + implied payout must reproduce the actual dividend — otherwise the story conflicts.**

---

## Exo 22 — Cas analyste complet + sensibilité · **Session 3**

**Q1.** g₁₋₂ = 0,70 × 18 % = 12,6 % ; EPS 6,193 / 6,973 ; D 1,858 / 2,092 ; an 3 : g 9 % → EPS 7,601, D 3,040 ;
an 4 : g 6 % → EPS 8,057, D 4,028.
**Q2.** g stable = 0,40 × 10 % = **4 %**. **Q3.** EPS₅ = 8,3793 ; D₅ = 5,0276.
**Q4.** P₄ = 5,0276 ÷ (0,085 − 0,04) = **111,7233**.
**Q5.** PV explicites (ke 10 %) = 8,4537 ; PV(P₄) = 76,3085 ; **P₀ ≈ 84,76**.
**Q6-7.** Part TV = **90,03 %** ; vs marché 78 → (84,76 − 78)/78 = **+8,67 %** (intrinsèque au-dessus).
**Q8.** g 3,5 % → P₀ ≈ **76,80** ; g 4,5 % → P₀ ≈ **94,71** → ±0,5 pt de g = ±18 € : quand la TV pèse 90 %, **g stable EST la valo** → c'est l'hypothèse à défendre en priorité.

🇬 *One-liner :* **When terminal value dominates, the stable-growth assumption is the valuation.**

---

## Comment bosser ce doc (phase 1)

1. Lis un exo **cache-cache** : cache le chiffre, refais-le, compare.
2. Pour chaque exo, récite à voix haute : **session + concept FR + one-liner EN** avant de calculer.
3. Fin de phase 1 = refaire les 22 exos avec **0 erreur de méthode** (une erreur de calcul se corrige ; une erreur de méthode retourne au §concept).
4. Ensuite seulement → **phase 2** (définitions du cours + cas des TD) puis **phase 3** (blancs même timing).
