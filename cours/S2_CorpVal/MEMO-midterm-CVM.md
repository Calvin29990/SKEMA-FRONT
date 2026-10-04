# MÉMO MIDTERM — CORPORATE VALUATION METHODS (ven. 09/10, 20 MCQ, 30 min, sessions 1-3)

> **Sources vérifiées dans ce repo :** `Session 1 - CVM (Farooq).pdf`, `Session_2_Forecasting_Valuation_Inputs_Student.pdf`,
> `Session 3.pdf`, `Intrinsic_Valuation_Exercises (midterm training).pdf` + `Intrinsic_Valuation_Solutions (midterm training).docx`
> (cours/S2_CorpVal/). Mail de Farooq : les MCQ K2 sont **conceptuels** — « focus on understanding the ideas rather than
> memorizing formulas ». Donc : 30 min pour 20 MCQ = **90 s/question** → ce sont les réflexes de cohérence qui rapportent,
> pas les gros calculs.
>
> 🏋️ **Avant le midterm :** refais dans l'ordre les exos « drill 30 min » (§7) chrono en main, puis les MCQ K2 de Farooq.

---

## 1. Les 10 réflexes de cohérence (80 % des MCQ tombent là-dessus)

| # | Réflexe | La règle | Le piège de MCQ |
|---|---|---|---|
| 1 | **Cash flow ↔ taux ↔ objet** | FCFF → WACC → **Enterprise Value** · FCFE → Ke → **Equity Value** · Dividendes → Ke → Equity Value (DDM) | « discount FCFF at the cost of equity » = erreur de framework, pas de calcul |
| 2 | **Pont EV → equity** | Equity = EV − debt (+ claims senior/NCI) + cash excédentaire + actifs non opérationnels | oublier le cash ; ou re-soustraire la dette après une valo FCFE |
| 3 | **Normalisation = récurrence économique, pas l'étiquette** | on ajoute les vrais one-off, on retire les gains non opérationnels, on **garde** les charges « one-off » qui reviennent chaque année | add-back automatique de tout ce qui est labelisé « one-off » (4e année consécutive de restructuration = récurrent) |
| 4 | **NOPAT & invested capital cohérents** | NOPAT = EBIT normalisé × (1−t) · IC = actifs opérationnels − passifs opérationnels (cash excédentaire **exclu**) | mettre le cash excédentaire dans l'IC ; utiliser le net income dans le ROIC |
| 5 | **La croissance n'est pas gratuite** | g = taux de réinvestissement × ROIC · donc taux de réinvestissement stable = g ÷ ROIC | prévoir 6 % de croissance avec CapEx ≈ D&A et ΔNWC = 0 = histoire incohérente |
| 6 | **FCFF ≠ EBITDA** | FCFF = NOPAT + D&A − CapEx − ΔNWC = NOPAT − réinvestissement | traiter EBITDA comme un cash flow (ignore taxes, CapEx, NWC) |
| 7 | **Terminal value = année n+1, discountée n fois** | TVₙ = FCFFₙ₊₁ ÷ (WACC − g), avec WACC > g ; TVₙ se discount sur n périodes | mettre FCFFₙ au numérateur ; oublier de discounter la TV ; g ≥ WACC |
| 8 | **Stable = un package, pas un seul g** | g + marge mature + ROIC soutenable + réinvestissement cohérent + risque stable | juger la valo sur le % de TV seul (77 % n'est pas une erreur en soi → on inspecte les hypothèses) |
| 9 | **Multiple implicite = cross-check** | EV/EBITDA implicite = TV ÷ EBITDA de l'année terminale ; on compare à l'économie d'une firme mature | choisir un multiple de marché d'abord et appeler ça « intrinsic terminal value » |
| 10 | **DDM : D₁, pas D₀** | P₀ = D₁ ÷ (Ke − g) ; D₁ = D₀(1+g) ; g soutenable = rétention × ROE | utiliser D₀ au numérateur ; payout élevé + croissance perpétuelle élevée sans ROE suffisant |

---

## 2. Formules à connaître par cœur (référence verbatim du corrigé officiel)

| Famille | Formule |
|---|---|
| FCFF | FCFF = NOPAT + D&A − CapEx − ΔNWC opérationnel = NOPAT − Réinvestissement |
| FCFE | FCFE = Net Income + D&A − CapEx − ΔNWC + Net Borrowing |
| NOPAT / ROIC | NOPAT = EBIT normalisé × (1 − t) · ROIC = NOPAT ÷ Invested Capital |
| Croissance fondamentale | g ≈ Reinvestment Rate × ROIC · RR stable = g ÷ ROIC stable |
| DCF firme | EV = Σ FCFFₜ/(1+WACC)ᵗ + TV/(1+WACC)ⁿ · TVₙ = FCFFₙ₊₁/(WACCₛₜ − g) |
| DCF equity | Equity = Σ FCFEₜ/(1+Ke)ᵗ + TV equityₙ/(1+Ke)ⁿ |
| Pont | Equity = EV − debt − claims + cash + actifs non opérationnels |
| Par action | Value/share = Equity ÷ actions diluées |
| Multiple implicite | EV/EBITDA implicite = TV ÷ EBITDA terminal |
| Ke | Ke = Rf + β × ERP (+ risque pays) · β bottom-up : unlever les pairs, médiane, relever au D/E cible |
| WACC | WACC = E/(D+E)·Ke + D/(D+E)·Kd·(1−T), poids de **marché** |
| DDM | P₀ = Σ Dₜ/(1+Ke)ᵗ · zéro croissance : P₀ = D/Ke · Gordon : P₀ = D₁/(Ke−g) · g = rétention × ROE |
| R&D capitalisée | EBIT ajusté = EBIT + R&D courante − amortissement R&D (pas de magie de cash : le FCFF net ne change quasi pas) |

---

## 3. Session 1 en 8 points (fondations)

1. **Price ≠ value** : le prix s'observe, la valeur se défend ; une valo = une estimation conditionnelle aux hypothèses.
2. **4 familles de méthodes** : intrinsic (DDM/FCFE/FCFF), relative (multiples), transaction/LBO, asset-based (NAV) — aucune n'est supérieure partout.
3. **Exemple Aster (bridge)** : EV 1 250 − debt 310 + cash 85 + non-op 25 = **equity 1 050** → /40 M actions = **26,25 €/action**. Le cash s'ajoute car il ne génère pas les FCFF valorisés.
4. **Normalisation (exemple du cours)** : EBIT 420 + restructuration 35 − gain de cession 20 + cyber one-off 12 = **447** ; la charge de contentieux **récurrente** (8) reste dedans.
5. **ROIC vs WACC** : ROIC > WACC = création de valeur ; ROIC < WACC = la croissance **détruit** de la valeur.
6. **Exemple chiffré** : NOPAT 225 ; IC = 2 250 − 550 = 1 700 ; ROIC = **13,2 %** (vs WACC 8 % → création).
7. **Même croissance, cash très différent** : NOPAT 200, g 6 % : ROIC 15 % → RR 40 %, FCFF 120 ; ROIC 8 % → RR 75 %, FCFF 50.
8. **Epsilon Technologies (debrief officiel)** : EBIT normalisé **540** (510+30) ; NOPAT **405** ; réinvestissement (105−65)+20 = **60** ; FCFF **345** ; ROIC = 405/2 700 = **15 %** ; g fondamentale = 40 % × 15 % ≈ **2,22 %** ; taux correct pour FCFF = **WACC**.

## 4. Session 2 en 8 points (prévisions & WACC)

1. **Revenus par drivers** : marché × part ; volume × prix ; clients × ARPU ; stores × sales/store. Somme des segments **avant** le total groupe.
2. **Exemple du cours** : marché 4,0 % + part +0,8 % → **4,8 %** en 2027 (puis 4,4 %, 3,8 %).
3. **Margin bridge** : 12,0 % +0,4 (pricing/mix) +0,3 (input cost) +0,5 (levier opé.) −0,4 (investissement) = **12,8 %**. « +50 bps/an » sans mécanisme = pas une prévision.
4. **Horizon explicite** : 5 ans si mature ; 7-10+ si croissance/marge/ROIC loin de l'état stable. Test : « l'année terminale ressemble-t-elle à une firme mature ? »
5. **R&D capitalisée** : EBIT ajusté = 300 + 100 − 60 = **340** ; NOPAT +30 après impôt ; FCFF : +30 +60 −100 ≈ **−10** → le bénéfice est **analytique** (ROIC/réinvestissement propres), pas un cash magique.
6. **Beta bottom-up (exo 3 corrigé)** : unlever βL/(1+(1−T)·D/E) → A 1,20/1,225 = 0,980 ; B 1,05/1,15 = 0,913 ; C 1,35/1,375 = 0,982 → médiane **0,980** ; relever à D/E 35 % : 0,980 × (1+0,75×0,35) = **1,237** ; Ke = 2,5 + 1,237×5 = **8,68 %** ; poids : E 74,07 % / D 25,93 % → WACC ≈ 0,7407×8,68 + 0,2593×4,5×0,75 ≈ **7,30 %**. Jamais de poids **book**.
7. **Inputs WACC** : Rf dans la **devise** des cash flows (pas le pays du siège) ; ERP sourcé/daté ; Kd **forward** (spread courant ou synthétique), pas « intérêts historiques / dette book ».
8. **Exemple WACC du cours** : Ke 8,0 % ; Kd après impôt 3,375 % ; 75/25 → **6,84 %**.

## 5. Session 3 en 8 points (DCF & DDM)

1. **Timeline** : TV₅ contient les flux **à partir de l'année 6** ; l'année 5 est un flux explicite.
2. **Exemple fil rouge du cours** : PV FCFF explicites **440,9** ; FCFF₆ = 154,5 − 46,35 = **108,15** (RR = 3 %/10 % = 30 %) ; TV₅ = 108,15/5 % = **2 163** ; PV(TV) = **1 472** ; EV = **1 912,9** ; part TV ≈ **77 %** (→ on inspecte, on ne rejette pas).
3. **Bridge du cours** : 1 912,9 − 500 + 120 = **1 532,9** → /100 actions = **15,33 €**.
4. **4 checks de TV** : g < WACC · RR = g/ROIC plausible · économie mature (pas peak-cycle) · multiple implicite cohérent.
5. **Sensibilité vs scénario** : sensibilité = on bouge 1-2 inputs mécaniquement (table g × WACC du cours : 10,6 → 26,6 €) ; scénario = on change **l'histoire économique** liée.
6. **DDM = un DCF** dont le flux est le dividende ; P₀ = D/Ke (zéro croissance) ; Gordon P₀ = D₁/(Ke−g) ; multi-stages si transition.
7. **Gordon (exemple du cours)** : D₁ = 2,00×1,03 = 2,06 ; P₀ = 2,06/(0,09−0,03) = **34,33**. Yield = D₁/P₀ = 5 % + g 4 % = Ke 9 % (décomposition du retour).
8. **g = rétention × ROE** : payout 60 % + ROE 12 % → g = 4,8 %. Payout élevé + g perpétuel élevé **exige** un ROE élevé, sinon hypothèses incompatibles.

---

## 6. Training midterm — les 22 exos du prof : réponses clés + piège

*Réfais-les d'abord sans regarder, puis contrôle ici. Les valeurs viennent du corrigé officiel (docx).*

| # | Résultat clé (corrigé officiel) | Piège à éviter |
|---|---|---|
| 1 | FCFF₆ = 61,50 ; TV₅ = 61,50/(0,085−0,025) = **1 025** ; PV explicites 199,66 + PV TV 681,67 = EV **881,33** ; equity = 881,33−180+25 = **726,33** → **14,53 €/action** | numérateur = FCFF**6** ; ne pas oublier le cash |
| 2 | TV₅ = 134,28×1,025/(0,09−0,025) = 2 117,45 ; EV = **1 800,23** | ΔNWC = 12 % × (Revₜ − Revₜ₋₁), pas 12 % du CA |
| 3 | FCFE an 5 = 90 ; TV equity = 90×1,03/0,07 = 1 324,29 ; equity = **1 124,81** → **28,12 €/action** | FCFE → **pas** de soustraction de dette ensuite |
| 4 | FCFF/WACC : EV **1 408,19** ; FCFE/Ke : equity **627,16** ; discount FCFF à Ke = mismatch | objets différents → taux différents |
| 5 | NOPAT₆ = 154,50 ; RR = 30 % ; réinv. 46,35 ; FCFF₆ = **108,15** ; TV₅ = **2 163** | on construit l'année stable, on ne « grow » pas mécaniquement FCFF₅ |
| 6 | PV explicites 396,70 ; FCFF₆ = 130,69 ; TV₅ = 2 178,12 ; PV(TV) 1 448,55 ; EV = **1 845,25** ; part TV = **78,5 %** | part TV élevée = inspecter, pas rejeter |
| 7 | Multiple implicite = 2 178,12/180 = **12,1×** ; écart vs mature → revoir g, ROIC/réinv., marge, WACC | le multiple est un **check**, pas la valo |
| 8 | Table 3×3 : EV max **2 070,71** / min **1 679,17** ; si ROIC fixé, changer g **oblige** à changer la RR | sinon hypothèses stables incohérentes |
| 9 | Equity = 2 400 − 500 + 120 − 40 (NCI) + 35 = **2 015** → **20,15 €/action** | NCI = claim à soustraire ; invest. non-op à ajouter |
| 10 | NOPAT₆ 212,71 ; RR 22,73 % ; FCFF₆ 164,36 ; TV 2 739,39 ; PV 571,14 + 1 821,82 = EV **2 392,96** ; equity **2 132,96** → **28,44** ; implicite **8,21×** ; part TV **76,1 %** | master case : tout s'enchaîne, une erreur amont se propage |
| 11 | P₀ = 2,40/0,08 = **30,00** ; vs marché 27,50 → **+9,09 %** | zéro croissance = perpétuité simple |
| 12 | D₁ = 2,60 ; P₀ = 2,60/0,05 = **52,00** ; yield 5 % + g 4 % = Ke 9 % | D₁ ≠ D₀ |
| 13 | 60(0,09−g) = 2,40(1+g) → g = **4,81 %** ; vérif Ke > g ✓ | reverse-engineering : résoudre pour g |
| 14 | rétention 60 % ; g = 9 % ; D₁ = 2,18 ; P₀ = 2,18/0,015 = **145,33** ; spread 1,5 pt → **très sensible** | petit (Ke−g) = valo explosive = signal d'alerte |
| 15 | RR = 6/15 = 40 % ; payout 60 % ; D₁ = 2,544 ; P₀ = **63,60** ; g plus haut → payout plus bas | cible de g impose la rétention |
| 16 | D₁-₃ = 1,68/1,8816/2,1074 ; P₃ = 36,5281 ; P₀ = **32,11** ; part TV = **85,47 %** | P₃ se discount sur 3 ans |
| 17 | D₅ = 2,7724 ; P₄ = 46,2072 ; P₀ ≈ **39,75** ; part TV ≈ **80,85 %** | croissances variables puis stable : D₅ = D₄×1,035 |
| 18 | g₁₋₄ = 12,6/10,4/8,4/6 % ; P₄ = 80,2176 ; P₀ = **60,74** ; part TV **88,59 %** | P₄ discounté à 10,5 %⁴ (ke explicite), pas 9 % |
| 19 | D₅ = 2,1330 ; P₄ = 35,5493 ; facteurs cumulés 1,12/1,2544/1,3924/1,5316 ; P₀ ≈ **28,62** | ke **changeant** → facteurs de discount cumulés, pas (1+ke)ᵗ simple |
| 20 | g = 11,05 % (ans 1-3), 7,7 %, 5,4 % ; P₅ = 116,4067 ; P₀ ≈ **82,81** ; part TV **85,33 %** | EPSₜ = EPSₜ₋₁×(1+gₜ), Dₜ = EPSₜ×payoutₜ |
| 21 | g implicite = **4,70 %** ; rétention 39,18 % ; payout 60,82 % ; dividende implicite 2,74 ≠ D₀ 2,20 → **incohérent** | le check final compare D implicite et D réel |
| 22 | P₀ ≈ **84,76** vs marché 78 → **+8,67 %** ; part TV **90 %** ; sensibilité g 3,5 % → 76,80 / g 4,5 % → 94,71 | ±0,5 pt de g = ±18 € : le terminal fait la valo |

---

## 7. Drill 30 min (comme le jour J)

Refais **chrono** (90 s chacun) : exos **1, 3, 5, 9, 11, 12, 13, 14, 15, 16** puis 4 questions conceptuelles à voix haute :
1. Quel taux pour FCFF ? pour FCFE ? pour un dividende ? → WACC / Ke / Ke.
2. Pourquoi soustrait-on la dette après un FCFF et pas après un FCFE ?
3. Une charge « one-off » qui revient chaque année : adjust ou retain ? → **retain**.
4. g = 3 %, ROIC stable = 10 % : quelle RR stable ? → 30 %.

**Seuil :** 10/10 calculs + 4/4 conceptuels en ≤ 30 min, sinon relis le réflexe fautif au §1 et rejoue à J+1.

---

## 8. Les 8 erreurs classiques du cours (à cocher mentalement en lisant chaque MCQ)

1. Mélanger enterprise et equity value. · 2. Utiliser le résultat publié sans normaliser. · 3. Mettre des items de financement dans le profit opérationnel. · 4. NOPAT et invested capital incohérents. · 5. Prévoir la croissance sans réinvestissement. · 6. EBITDA pris pour un free cash flow. · 7. FCFF discounté au cost of equity. · 8. Add-back automatique de tous les « one-off ».

> **Règle d'or de Farooq :** chaque numéro doit avoir une **explication économique**, pas seulement un calcul. Si une MCQ te propose un chiffre « sans mécanisme », c'est le leurre.
