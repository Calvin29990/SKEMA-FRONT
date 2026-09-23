# 🎓 MASTERCLASS DE REPRISE — 24 septembre 2026
## Corporate Valuation Methods (9h45-13h, Amphi C **301**) · Capital Structure & Dividend Policy (15h-18h15, Room D 117/118)

*Fichier unique — texte en français, concepts et formules en anglais (langue du cours). Ce que contient la S1 de chaque cours = **à maîtriser** ; la S2 de demain = **à anticiper** (section 3). Temps de lecture : 45-60 min. Refais les 3 calculs phares sans regarder avant de dormir.*

---

## 0. Pourquoi ces deux cours sont TON ticket pour le front office

Un desk d'achat/vente (equities, credit, FICC) n'évalue jamais « une entreprise » — il évalue **un écart entre prix de marché et valeur estimée** (*implied valuation gap*). Tout ce qui suit est le langage exact de ce métier :

| Concept du cours | Utilisation desk (front) |
|---|---|
| *Enterprise Value vs Equity Value* (pont EV→equity) | Comparer deux boîtes sans se tromper : un trader regarde d'abord l'EV, jamais le simple cours de bourse |
| *Normalisation / sustainable earnings* | Filtrer le bruit des résultats publiés → c'est exactement la routine d'un desk equities/research le jour des earnings |
| *ROIC vs WACC* | Le filtre binaire de tout value desk : ROIC > WACC = création de valeur = candidat long ; l'inverse = candidat short ou désendettement |
| *Growth = Reinvestment rate × ROIC* | Détecter une croissance qui détruit du cash — fondement des arguments de short-sellers (Lumen/Activist research) |
| *MM Proposition I* | Racine de toute pensée de relative value / arbitrage : le prix de l'ensemble = somme des parties |
| *Tax shield / financial distress → D\** | Le cœur du métier credit / high yield : plus la dette monte, plus le spread de crédit doit monter |
| *WACC* | Le hurdle rate : le desk compare systématiquement le carry d'une position à son coût d'opportunité |

Retiens cette phrase pour l'oral et les entretiens : **« Valuation is a defensible estimate — not the discovery of one hidden exact number. »** (slide S1) — ton boulot, c'est défendre une estimation, pas trouver un chiffre magique.

---
---

# PARTIE 1 — CORPORATE VALUATION METHODS (Sommer)
## S1 : *Valuation Foundations & Preparing for Valuation* ✅ À MAÎTRISER

### 1.1 Price ≠ Value — le point de départ de tout le cours

| Concept | Définition |
|---|---|
| **Market price** | Prix observable aujourd'hui — pas forcément la valeur |
| **Estimated intrinsic value** | Ton estimation (cash flows futurs + risque + hypothèses) |
| **Transaction value** | Ce qu'un acheteur précis paierait (contrôle, synergies, capacité de financement) |

**La chaîne complète de la S1 — apprends-la par cœur :**
```
Reported Financials → Normalize → Forecast → FCFF
FCFF → WACC → Enterprise Value
Enterprise Value → Equity Value → Value per Share
→ Compare to market price → Implied Gap (ex: prix 50€ vs valeur 62€ = gap +24%)
```
La conclusion est **toujours conditionnelle aux hypothèses** — la défense de l'hypothèse vaut plus que le chiffre.

### 1.2 Le paysage des méthodes (*valuation landscape*)

- **Intrinsic** : DDM, FCFE, FCFF (cash flows futurs → actualisation)
- **Relative** : multiples de bourse (trading multiples / comps)
- **Transaction & LBO** : transactions passées, rendement LBO
- **Asset-based** : NAV, liquidation

Aucune méthode n'est universelle : le choix dépend du business, du but, du point de vue.

### 1.3 ⭐ La règle d'or du matching (cause n°1 d'erreur en exam comme en interview)

| Cash flow | Taux d'actualisation | Valeur obtenue |
|---|---|---|
| **FCFF** (cash pour TOUS les apporteurs de capital) | **WACC** | **Enterprise Value** |
| **FCFE** (cash résiduel pour les actionnaires) | **Cost of equity** | **Equity Value** |

> ❌ Erreur fatale : actualiser du FCFF au cost of equity. FCFF appartient à la dette ET l'equity ; FCFE est le résidu actionnaires.

### 1.4 ⭐ Le pont EV → Equity (*EV-to-equity bridge*)

```
Equity Value = Enterprise Value − Debt + Cash(excédent) + Other non-operating assets
```
- **− Debt** : les prêteurs sont payés d'abord (claim prioritaire)
- **+ Cash excédentaire** : cash non nécessaire aux opérations
- **+ Actifs non-opérationnels** : participations sans lien avec le cœur de métier

**✏️ Exo rapide (Aster SA, slide 8) — résolution :**
- EV = 1 250 − 310 + 85 + 25 = **1 040 M€**
- Par action : 1 040 / 40 = **26 €**
- Pourquoi +cash ? Parce qu'il revient aux actionnaires sans passer par l'exploitation.
- Si on a actualisé du FCFF, la valeur AVANT le pont était l'**Enterprise Value**.

### 1.5 Normalisation : *Reported earnings ≠ Sustainable earnings*

Le filtre n'est PAS l'étiquette du management (« one-off »), c'est la **récurrence économique** :
- **REMOVE** : gains/pertes hors exploitation (vente d'un terrain inutilisé ✗)
- **ADJUST** : événements vraiment exceptionnels (premier cyber-incident ✓ si premier)
- **RETAIN** : coûts qui reviennent chaque année même étiquetés « exceptionnels » (restructuration 4 ans d'affilée = RETAIN)
- **RECLASSIFY** : postes mal rangés opérationnel/financier

**✏️ Exemple (slide 12) :** EBIT 420 + restruct 35 − gain cession 20 + cyber 12 = **447** (litige annuel de 8 conservé car récurrent).

### 1.6-1.8 NOPAT → Invested Capital → ROIC

```
NOPAT = Normalized EBIT × (1 − Operating tax rate)
Invested Capital = Operating Assets − Operating Liabilities
                 (≈ Debt + Equity − Non-operating assets)
ROIC = NOPAT ÷ Invested Capital
```
**Le test qui vaut des points d'entretien :** ROIC > WACC → création de valeur · ROIC ≈ WACC → croissance stérile · ROIC < WACC → destruction de valeur. Le numérateur (NOPAT) et le dénominateur (IC) doivent être **économiquement cohérents** (exclure excess cash des deux côtés).

**✏️ Slide 17 :** NOPAT = 300×75% = 225 · IC = 2 250−550 = 1 700 · ROIC = 13,2% > 8% → création.

### 1.9 ⭐ *Growth is not free* — la relation fondamentale

```
Growth ≈ Reinvestment rate × ROIC      ⟹      Reinvestment rate = Growth / ROIC
```
**Exercice des deux entreprises (slide 19) — même croissance de 6%, même NOPAT 200 :**
| | ROIC | Reinvestment rate | Reinvestment | FCFF |
|---|---|---|---|---|
| HighROIC | 15% | 40% | 80 | **120** |
| LowROIC | 8% | 75% | 150 | **50** |

→ Une croissance identique peut coûter presque 2× plus de cash. Moins le ROIC est haut, plus la croissance « mange » le FCFF. C'est l'argument technique central des short-sellers et des activistes (et du tri « quality » des value desks).

### 1.10-1.12 Reinvestment → FCFF → FCFE

```
Reinvestment = Net CapEx + Δ Operating NWC        (Net CapEx = CapEx − D&A)
FCFF = NOPAT − Reinvestment = NOPAT + D&A − CapEx − ΔNWC
FCFE = Net Income + D&A − CapEx − ΔNWC + Net borrowing
```
- **FCFF est indépendant du financement** (avant dette) → il se actualise au WACC → EV.
- **EBITDA ≠ FCFF** ! L'EBITDA ignore les impôts, le CapEx et le BFR. Point qui élimine 50% des candidats en entretien.
- **Net borrowing** dans le FCFE : émettre de la dette alimente le cash disponible pour les actionnaires ; la rembourser le consomme.

**✏️ De l'EBIT au FCFF (slide 22) :** NOPAT = 260×76% = 197,6 → Reinvestment = (70−45)+18 = 43 → **FCFF = 154,6**.

### 1.13 Les 8 erreurs classiques (checklist de survie — slide 28)

1. Mélanger enterprise value et equity value
2. Utiliser les résultats publiés sans fouiller les items inhabituels
3. Inclure des items de financement dans le profit opérationnel
4. NOPAT et invested capital incohérents entre eux
5. Prévoir la croissance sans considérer le reinvestment
6. Traiter l'EBITDA comme du free cash flow
7. Actualiser du FCFF au cost of equity
8. Ajouter automatiquement tout ce qui porte l'étiquette « one-off »

### 📐 Exercices CVM résolus (entraînement express — refais sans regarder)

**Ex 1 — Northstar (pont EV→equity) :** excess cash = 125−45 = **80** → Equity = 1 480 − 360 + 80 + 38 = **1 238 M€** → **24,76 €/action**. L'investissement coté (38) est ajouté car hors cœur de métier ; la dette se soustrait car claim prioritaire.

**Ex 2 — Helios (normalisation 510) :** restructuration (4 ans d'affilée) → **RETAIN** ; gain terrain → **REMOVE** (−18) ; premier cyber → **ADJUST** (+14) ; intégration d'acquisitions (stratégie récurrente) → **RETAIN** ; award CEO (sur 3 ans) → **RETAIN** ; rappel produit (aucun depuis 5 ans) → **ADJUST** (+16). **Base défendable ≈ 510 − 18 + 14 + 16 = 522 M€**.

**Ex 3 — Orion :** NOPAT = 240×75% = **180** · IC = (300+260+1 540) − (220+180) = **1 700** · ROIC = **10,6%**. Excess cash (250) et marketable securities (90) exclus : ils ne produisent pas le NOPAT — les inclure casserait la cohérence numérateur/dénominateur et diluerait artificiellement le ROIC.

**Ex 4 — Atlas/Beacon/Cedar (croissance 7%, NOPAT 250, WACC 8%) :**
| | ROIC | rr = 7%/ROIC | Reinvestment | FCFF | Verdict |
|---|---|---|---|---|---|
| Atlas | 20% | 35% | 87,5 | **162,5** | Crée de la valeur (ROIC>WACC) |
| Beacon | 10% | 70% | 175 | **75** | Peu de valeur marginale |
| Cedar | 6% | 116,7% | 291,7 | **−41,7** | Détruit : FCFF négatif ! |

Cedar augmente ses bénéfices comptables **en détruisant de la valeur économique** (ROIC 6% < WACC 8%).

**Ex 5 — Lumen :** NOPAT = 330×75% = 247,5 · Net CapEx = 82−55 = 27 · Reinvestment = 27+24 = 51 · **FCFF = 247,5 − 51 = 196,5** (les deux formes donnent pareil ✓) · rr = 51/247,5 = **20,6%**.

**Ex 6 — Nova Health (le full rehearsal parfait pour ce soir) :**
- Normalisation : restructuration 3 ans sur 4 → **RETAIN (−36 ne se rajoute PAS !)** ; vente du siège → REMOVE (−25) ; premier cyber → ADJUST (+18) → **EBIT normalisé = 620 − 25 + 18 = 613**
- NOPAT = 613×74% = **453,6** · Reinvestment = (92−80)+28 = **40** · **FCFF = 413,6**
- ROIC = 453,6/3 100 = **14,6%** · rr = 40/453,6 = **8,8%** · croissance fondamentale = 8,8% × 14,6% ≈ **1,3%**
- Excess cash = 310 − 110 = **200** (pour le futur pont EV→equity) · Taux = **WACC**
- Il reste à prévoir : croissance durable, horizon, reinvestissements, WACC → c'est la S2.

---
---

# PARTIE 2 — CAPITAL STRUCTURE & DIVIDEND POLICY (Pilkington)
## S1 : *Cost of Capital and Firm Value* ✅ À MAÎTRISER

### 2.1 Définitions & les 3 questions du cours

- **Capital structure** : proportion dette / equity / autres titres (ici : mix dette-equity).
- **Cost of capital** : **coût d'opportunité** d'investir dans le portefeuille des titres de l'entreprise — le rendement exigé parce que l'investisseur peut placer son argent ailleurs à risque comparable.
- Les 3 questions organisatrices : (1) changer le mix dette/equity peut-il **augmenter la valeur de la firme** ? (2) peut-il **baisser le WACC** ? (3) si oui, c'est quoi une structure **optimale** — et sous quelles conditions ?

### 2.2 Case I — Marchés parfaits (pas de frictions, pas d'impôts, pas de coûts de faillite)

**L'exemple U vs L (à savoir refaire) :** cash flows 6 000 ou 4 000 (50/50, espérance 5 000). L a 2 000 de dette à 10% → rembourse 2 200.
- U : equity reçoit 5 000
- L : dette 2 200 + equity (5 000−2 200) = 2 200 + 2 800 = **5 000 — total identique !**
- L'intuition MM (lait/crème/lait écrémé) : séparer les claims ne crée **aucun cash flow opérationnel** supplémentaire → si les payoffs sont identiques, **l'arbitrage impose la même valeur**.

**⭐ MM Proposition I :**
```
VU = VL   ·   Firm value indépendante de la structure   ·   WACC indépendant de la structure
```
Raison économique : le financement ne change pas les cash flows opérationnels.

### 2.3 Applications MM I — les deux expériences classiques (typedef exam)

**Rachat d'actions financé par dette** (*stock repurchase*, slide 11) : actifs 20 000, 1 000 M actions à 20$ → émission de 5 000 de dette pour racheter des actions.
- V = 20 000 (inchangé) · E = 20 000 − 5 000 = 15 000
- Rachat : 5 000/20 = 250 M actions → reste 750 M → prix = 15 000/750 = **20$/action — INCHANGÉ**.
- Conclusion qui vaut en desk : racheter ses actions avec de la dette ne fait **pas monter mécaniquement le cours**. L'effet « repurchases boost price » vient d'autres signaux (sous-évaluation, taxe, discipline) — jamais du simple swap dette↔equity.

**Émission d'actions** (*stock issuance*, slide 13) : 5 000 de cash neuf → total equity 25 000 · 250 M nouvelles actions → 25 000/1 250 = **20$/action**. Pas de « dilution de valeur » si le prix est juste : le nombre d'actions ET les actifs augmentent proportionnellement.

**L'exemple choc (slide 18) :** même L avec WACC 100%, dette 2 000 → VL = 2 500 = D 2 000 + E 500 → equity payoff 2 800 sur 500 de valeur = **rE = 460% !** Levier = rendement exigé qui explose.

### 2.4 ⭐ MM Proposition II — le levier renchérit l'equity

```
rE = rWACC + (D/E) × (rWACC − rD)
```
- Plus D/E monte, plus l'equity devient risquée (claim résiduelle après la dette) → plus les actionnaires exigent de rendement.
- Graphe à reproduire en exam/interview : **rE monte linéairement, rD constant, WACC constant** (pas de « dette pas chère = financement pas cher » : ce que tu gagnes sur la dette, tu le perds sur l'equity).

**✏️ Capital budgeting sans impôts (slide 19) :** D/E=0,6, rD=12%, rE=20% → D/V=37,5%, E/V=62,5% → WACC = 0,375×12 + 0,625×20 = **17%**. Cible D/E=1 → rE = 17+1×(17−12) = **22%** → WACC = 0,5×12 + 0,5×22 = **17% — inchangé ✓**.

### 2.5 Betas levier (la même chose exprimée en risque)

```
Sans impôt : βA = βE / (1 + D/E)        ⟹        βE = βA × (1 + D/E)
```
- **βA (asset beta)** = risque de l'actif opérationnel ; **βE (equity beta)** = risque des actionnaires après levier.
- **✏️ (slide 22) :** βE = (20−12)/5 = 1,6 → βA = 1,6/1,6 = **1,0** → cible D/E=1 → βE = 1,0×2 = **2,0** → rE = 12 + 2×5% = **22%** ✓ (même résultat que Prop II — les deux routes convergent, retiens ça).

### 2.6 Case II — avec impôts : la dette crée enfin de la valeur

Intérêts déductibles → moins d'impôts → cash flow réel supplémentaire :
```
Tax shield annuel = τ × Interest            Modified Prop I :  VL = VU + τ × D  (dette permanente)
Modified Prop II :                        rE = rU + (D/E) × (rU − rD) × (1 − τ)
After-tax WACC :                          WACC = (D/V)×rD×(1−τ) + (E/V)×rE
```
- La prime de levier est assouplie par (1−τ).
- **⚠️ Warning du slide 29** : quand le levier change, il faut mettre à jour **à la fois** les poids (D/V, E/V) **et** le rE — erreur classique de ne changer que les poids.

**✏️ Recapitalisation avec impôts (slides 31-33, T=40%) :** mêmes chiffrres → WACC actuel = 0,375×12×0,6 + 0,625×20 = **15,20%** → désendettement : rU ≈ **17,88%** → nouveau rE = 17,88 + (17,88−12)×0,6 ≈ **21,41%** → nouveau WACC = 0,5×12×0,6 + 0,5×21,41 ≈ **14,31%**. Avec impôts le WACC **baisse** avec la dette (tax shield). Vrai aussi via les betas avec impôts : βE = βA[1+(D/E)(1−τ)].

### 2.7 Case III — l'optimum existe grâce au *financial distress*

Le modèle Case II « seul » dirait : 100% de dette = optimal. Absurde → il manque les **coûts attendus de détresse financière** (bankruptcy costs, perte de clients/fournisseurs, restructurations…). La synthèse :

| | Case I (pas d'impôts) | Case II (impôts) | Case III (+ distress) |
|---|---|---|---|
| Bénéfice de la dette | aucun | tax shield ✓ | tax shield ✓ |
| Coût ajouté | aucun | aucun pas encore | coût attendu de distress ✓ |
| Firm value | constante | ↑ avec D | **maximum en D\*** |
| WACC | constant | ↓ avec D | **minimum en D\*** |
| Conclusion | structure irrelevante | toujours plus de dette | **structure optimale D\*** |

**Retenir la logique systématique :** *no effect → tax benefit → tax benefit vs distress cost → optimum.* C'est votre colonne vertébrale pour tout le semestre (et toute interview credit/rating/LBO).

### 📐 Activité de groupe NOVA — résolue (ton matériel de deliverable 3 minutes)

**Partie A (pas d'impôts) :** D/E=0,5 → D/V=1/3, E/V=2/3 · WACC = (1/3)6% + (2/3)12% = **10%** · rA = 10% · nouveau rE = 10 + 1×(10−6) = **14%** · nouveau WACC = 0,5×6 + 0,5×14 = **10% — inchangé.** Prédictions : rE ↑, WACC constant, firm value constante. Explanation pie : même cake, répartition différente — plus de créme non prioritaire dans chaque part de equity.

**Partie B (T=25%, rU=10%, rD=6%) :**
- rE à D/E=0,5 : 10 + 0,5×(4)×0,75 = **11,5%** ; à D/E=1 : 10 + 1×4×0,75 = **13%**
- WACC à 0,5 : (1/3)(6)(0,75) + (2/3)(11,5) = **9,17%** ; à 1 : 0,5×6×0,75 + 0,5×13 = **8,75%** → le WACC **baisse** avec les impôts (tax shield).
- VU = 120 M€, D = 30 M€ permanent → VL = 120 + 0,25×30 = **127,5 M€** (tax shield = **7,5 M€**).
- Point 9 (le piège du management) : avec la S1 seule on peut conclure que le **tax shield existe et baisse le WACC** ; on ne peut **pas encore** recommander la dette illimitée — il manque les distress costs (Case III) et la flexibilité financière. **C'est exactement la nuance attendue du porte-parole du Groupe 7.**

**Deliverable 3 points à répéter (pour ta prise de parole Groupe 7 quand Pilkington relancera) :**
1. Le levier augmente le risque de l'equity : rE monte avec D/E (Formule Prop II), même si la dette est « pas chère ».
2. Sans impôts le WACC est constant ; avec impôts il baisse — la différence vient du **tax shield**, un cash flow réel versé par l'État.
3. Le résultat fiscal seul ne suffit pas à pousser la dette au maximum : il faut Case III (distress) pour parler d'optimum D*.

### 🌐 Utilité front de Capital Structure (points d'entretien premium)
- Desk **credit/high-yield** : le spread de crédit est exactement le marché qui « price » les distress costs de Case III — plus la boîte s'endette, plus son CDS/spread monte.
- Desk **LBO/private credit** : eux vivent de la maximisation VL = VU + τD sous contrainte (covariances, ratings).
- **Ratings & covenants** : une boîte qui vise D* → la logique derrière les objectifs de rating (BB/B) → tu parleras couramment aux desks origination/DCM.
- **MM arbitrage** : relative value = comparer deux gâteaux identiques emballés différemment — la matrice intellectuelle du pair-trading capital-structure (long equity / short debt du même nom, etc.).
- Et pour ton quotidien FX/macro (stage visé) : même logique de claims — senior/subordinated, country ceilings, trunching.

---
---

# PARTIE 3 — DEMAIN : ce qui t'attend (à anticiper, 15 min suffisent)

## 3.1 CVM — S2 (9h45, Amphi C 301) — *« Session 2 de la S1 : du passé aux prévisions »*

La S1 a fini sur : *« can these operating economics persist? That is Session 2. »* → attend :
- Comment **construire et défendre une prévision** (build the forecast) : croissance durable, horizon de prévision
- Probablement : début de la **mécanique DCF** (actualisation, horizon explicite + terminal value)
- **Crossing check** multiples vs DCF
- ⚠️ **Ton moment : le choix d'entreprise** (listed, market cap > 1 Md$, FCF yield > 3%, hors émergents, 5 ans de data). Profite de la S2 pour demander au prof (et t'annoncer) ta shortlist — critères à réciter mot pour mot.

**Évite d'être perdu si le prof démarre par le DCF :** rappelle-toi que tout revient à `FCFF → WACC → EV → Equity`. Si tu sais produire du FCFF propre, toute la S2 est de l'habillage.

## 3.2 Capital Structure — S2 (15h, Room D 117/118) — **Bond Valuation**

Prépare ces 4 briques (5 min) avant d'entrer (el te suffiront pour suivre) :
1. **Price = somme actualisée des coupons + nominal** au yield (YTM)
2. **Prix ↓ quand taux ↑** (relation inverse — première loi de toute salle de marchés)
3. **Par / Discount / Premium** : coupon = YTM → 100 ; coupon < YTM → décote ; coupon > YTM → prime
4. La **duration** mesure la sensibilité du prix au taux — le thème central du cours de Saidane (Money/Banking, 5/10), donc bien écouter les premières définitions ici.
> *Prends la TA BA II Plus — même pas encore achetée, prépare la commande ce week-end (obligatoire pour les autres cours).*

## 3.3 Career Management (vendredi 14h45-18h00, Room A 220) — 20% présence

CV à jour + pitch 30 s (« stage de fin d'études janv. 2027 en transaction services/salle de marché »). Aucun support à rattraper.

---

## FAUTES À NE PAS COMMETTRE DEMAIN (auto-check 30 secondes)

- [ ] Je sais refaire **EV→Equity** : 1 480−360+80+38 = 1 238 / 50 = 24,76 €
- [ ] Je sais refaire **FCFF** : NOPAT − (Net CapEx + ΔNWC) — et pourquoi **EBITDA ≠ FCFF**
- [ ] Je sais refaire **MM II no-tax** : WACC 17% reste 17% (rE 20%→22%)
- [ ] Je sais refaire **MM II avec impôts** : WACC 15,20% → 14,31% (tax shield), et **VL = VU + τD = 127,5**
- [ ] Mes 2 questions prêtes : choix d'entreprise (Sommer) + Bond Valuation basics prêts (Pilkington)
- [ ] Shortlist entreprises démarrée (cap>1Md$, FCF yield>3%, non émergents, 5y data)
- [ ] Groupe 7 confirmé à Ahmad

*Généré le 23/09/2026 · collé au plan S1 réel des deux profs (slides + exos + activité de classe)*
