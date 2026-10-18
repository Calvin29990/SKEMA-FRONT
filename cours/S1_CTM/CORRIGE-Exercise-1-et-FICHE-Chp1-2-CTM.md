# CORPORATE TREASURY MANAGEMENT (CTM) — Fiche Chapitres 1 & 2 + Corrigé intégral de `Exercise 1.docx`

> **Sources :** `cours/S1_CTM/CTM Course Chp 1  2.pptx` (45 slides) et `cours/S1_CTM/Exercise 1.docx`.
> **Cours :** Mardi 20/10/2026, 09:45–13:00 — *Lille Room A 407 EXEC*.
> **Structure du module (18h, 6 sessions) :**
> - **Session 1** : *Treasury mandate & risk* (Financial toolkit + worked exercises, dont `Exercise 1.docx`)
> - **Session 2** : *Cash & working capital* (Profit-to-cash bridge, WCR + **lancement du Case 1**)
> - **Session 3** : **🎯 Présentations en équipe de 5 (15 min + 6 min Q&A)**
> - **Session 4** : *Liquidity & funding* (Cash troughs, facilities, debt capacity)
> - **Session 5** : *Financial markets* (Rates, FX, commodities, surplus cash — **pile ton cœur de cible Front Office FX/Rates Sales !**)
> - **Session 6** : *Integrated stress test* (Combined downside & CFO action plan)
>
> **La discipline de décision du prof (répétée sur chaque cas) :**
> **1. Identify the exposure → 2. Quantify the cash consequence (amount & date) → 3. Recommend an executable decision (benefit, trade-off, owner, deadline).**

---

## PARTIE 1 — SYNTHÈSE DES CHAPITRES 1 & 2 (`CTM Course Chp 1  2.pptx`)

### Chapitre 1 — Pourquoi la Trésorerie existe et pourquoi elle est stratégique (Slides 3–27)

1. **Cash disponible $\neq$ Position nette $\neq$ EBITDA (Slides 4–6)**
   - *Règle d'or* : Une créance client à encaisser la semaine prochaine augmente la **position nette**, mais **ne paie pas une facture exigible ce soir**.
   - Une entreprise rentable ($\text{EBITDA} > 0$) peut faire défaut si les décaissements (salaires, fournisseurs à J+30) tombent avant l'encaissement client (J+60).
2. **Les 4 piliers du mandat Trésorerie (Slides 7–11)**
   - **Liquidity protection** (payer à l'échéance), **Financing decisions** (financer actifs et croissance), **Risk management** (contrôler les expositions cash), **Business support** (éclairer les décisions commerciales en amont).
   - **Gouvernance & contrôle interne** : politique centralisée (appétit au risque, limites, instruments autorisés, banques) + exécution locale encadrée. Séparation stricte des tâches sur la chaîne de paiement : **Initiate $\rightarrow$ Approve $\rightarrow$ Confirm $\rightarrow$ Settle** (anti-fraude au président / faux RIB fournisseur, où 100 k€ détournés = **200 k€** de sortie de cash totale car le vrai fournisseur reste à payer).
3. **Typologie des risques de trésorerie (Slides 12–16)**
   - **Liquidity risk vs Funding risk** :
     - *Liquidity risk* = Peut-on payer à la bonne date et au bon endroit ? (ex. retard de règlement client).
     - *Funding risk* = Peut-on obtenir ou renouveler un financement ? (ex. ligne de crédit non refinancée).
   - **Market risks (FX, Taux, Commodities)** :
     - **FX** : un EUR plus fort réduit la contre-valeur en EUR des encaissements nets en USD ($\text{EUR reçus} = \frac{\text{USD}}{\text{taux EUR/USD}}$). Exemple : sur $10\text{ M\$}$, passer de $1{,}10$ à $1{,}20$ fait chuter l'encaissement de $9{,}091\text{ M€}$ à $8{,}333\text{ M€}$ (**$-758\text{ k€}$**).
     - **Piège du FX Forward (engagement ferme de livraison, Slides 20–21)** : si on couvre $100\%$ d'une prévision de $10\text{ M\$}$ par un forward livrable mais que les clients ne paient que $6\text{ M\$}$, l'entreprise est **sur-couverte (over-hedged)** et doit **acheter $4\text{ M\$}$ au spot** sur le marché pour honorer la livraison à la banque ! *(Angle Sales FX parfait pour briller en cours).*
4. **Formules financières du Chapitre 1 (Slides 23–27)**
   - **BFR opérationnel (Operating WCR)** :
     $$\text{Operating WCR (BFR)} = \text{Inventory} + \text{Receivables} - \text{Payables}$$
     *(Exclut la trésorerie et la dette financière).*
   - **Levier net (Net Debt-to-EBITDA)** et **Couverture des intérêts (Interest Coverage)** :
     $$\text{Net Debt / EBITDA} = \frac{\text{Debt} - \text{Eligible Cash}}{\text{EBITDA}} \qquad ; \qquad \text{Interest Coverage} = \frac{\text{EBITDA}}{\text{Annual Interest}}$$
     *Attention* : $\text{Net Debt / EBITDA}$ n'est **pas** un « nombre d'années pour rembourser » car l'EBITDA ignore impôts, CapEx, $\Delta\text{BFR}$ et intérêts.
   - **Réponse à un incident de liquidité (Outage, Slides 26–27)** : ne pas regarder seulement le solde de fin de semaine (ex. solde à $0\text{ M€}$), mais l'**écart par rapport au buffer minimum requis** (ex. si buffer requis $= 3\text{ M€}$ et cash final $= 0\text{ M€}$, il faut tirer **$3\text{ M€}$** sur une ligne confirmée avant la date critique).

---

### Chapitre 2 — Cash & Working Capital (Slides 28–45)

1. **Pont EBITDA $\rightarrow$ Cash et coût de la croissance (Slides 29–34)**
   - $\Delta\text{WCR} = \text{WCR}_{\text{closing}} - \text{WCR}_{\text{opening}} \implies \text{Impact Cash-Flow} = -\Delta\text{WCR}$.
   - La croissance consomme du cash : si le ratio $\text{WCR / Revenue} = 20\%$ et que le CA passe de $200\text{ M€}$ à $250\text{ M€}$, il faut financer **$+10\text{ M€}$** de BFR additionnel avant même d'encaisser la marge.
2. **Les 4 ratios de rotation du cycle d'exploitation (base 365 jours, Slides 35–38)**
   $$\text{DSO} = \frac{\text{Average Receivables}}{\text{Annual Credit Sales}} \times 365 \qquad \text{(délai d'encaissement clients)}$$
   $$\text{DIO} = \frac{\text{Average Inventory}}{\text{Annual COGS}} \times 365 \qquad \text{(durée de détention des stocks)}$$
   $$\text{DPO} = \frac{\text{Average Trade Payables}}{\text{Annual Credit Purchases (ou COGS proxy)}} \times 365 \qquad \text{(délai de paiement fournisseurs)}$$
   $$\text{CCC (Cash Conversion Cycle)} = \text{DIO} + \text{DSO} - \text{DPO}$$
3. **BFR négatif et CCC négatif : avantage structurel vs signal de détresse (Slides 39–41)**
   - **Avantage structurel** : rotation rapide des stocks + encaissement comptant + crédit fournisseur négocié et respecté (ex. grande distribution).
   - **Signal d'alarme (Warning signal)** : un BFR négatif provoqué par des **retards de paiement fournisseurs (overdue payables)** cache un stress de liquidité (risque de coupure des livraisons ou retrait des délais).
   - **Même avec un CCC négatif**, une entreprise reste exposée au risque de liquidité : baisse du CA (qui inverse le BFR négatif et aspire le cash), raccourcissement des délais fournisseurs, salaires/loyers/impôts, CapEx et échéances de dette.
4. **Formules de libération de cash (Cash Release, Slides 42–43)**
   - **Via DSO** (base = Credit Sales / Revenue) :
     $$\text{Cash libéré (DSO)} = \text{Annual Credit Sales} \times \frac{\text{Jours gagnés}}{365}$$
   - **Via DIO** (base = COGS) :
     $$\text{Cash libéré (DIO)} = \text{Annual COGS} \times \frac{\text{Jours gagnés}}{365}$$
   - **Via DPO** (base = Credit Purchases / COGS proxy) :
     $$\text{Cash libéré (DPO)} = \text{Annual COGS} \times \frac{\text{Jours ajoutés}}{365}$$
   *(Ne jamais mélanger la base Sales pour DSO et la base COGS pour DIO/DPO !)*

---

## PARTIE 2 — CORRIGÉ INTÉGRAL DE `Exercise 1.docx` (*Business Model and Treasury Profile*)

### Rappel des données de l'énoncé (en EUR millions, base 365 jours)

| Metric (EUR m) | Profile A | Profile B | Profile C | Profile D | Profile E |
|---|---:|---:|---:|---:|---:|
| **Revenue** *(assimilé à Credit Sales)* | 1 000 | 500 | 365 | 300 | 400 |
| **COGS** *(proxy des achats à crédit)* | 750 | 400 | 219 | 90 | 120 |
| **EBITDA** | 55 | 50 | 50 | 90 | 100 |
| **Cash** *(non restreint, 100% éligible)* | 60 | 40 | 20 | 80 | 90 |
| **Debt** *(portant intérêt)* | 140 | 180 | 100 | 120 | 60 |
| **Receivables** | 5 | 100 | 60 | 45 | 10 |
| **Inventory** | 65 | 180 | 36 | 30 | 80 |
| **Payables** | 110 | 90 | 42 | 15 | 25 |
| **Fixed assets** *(valeur nette comptable)* | 220 | 250 | 180 | 220 | 170 |

---

### Question 1 — Calcul de l'Operating BFR, DSO, DIO, DPO, CCC et Net Debt / EBITDA

#### A. Formules, unités et hypothèses (conformes à l'énoncé et aux slides)
- **Hypothèses de l'énoncé** : année de **365 jours** ; soldes opérationnels = moyennes annuelles représentatives ; $100\%$ du chiffre d'affaires (Revenue) traité comme ventes à crédit pour le calcul du DSO ; COGS utilisé comme proxy des achats annuels à crédit pour le calcul du DPO ; Cash $100\%$ non restreint et éligible en déduction de la dette.
- **Formules et unités** :
  - $\text{Operating BFR (WCR)} = \text{Inventory} + \text{Receivables} - \text{Payables}$ *(en **EUR millions**, €m)*
  - $\text{DSO} = \dfrac{\text{Receivables}}{\text{Revenue}} \times 365$ *(en **jours**, days)*
  - $\text{DIO} = \dfrac{\text{Inventory}}{\text{COGS}} \times 365$ *(en **jours**, days)*
  - $\text{DPO} = \dfrac{\text{Payables}}{\text{COGS}} \times 365$ *(en **jours**, days)*
  - $\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO}$ *(en **jours**, days)*
  - $\text{Net Debt} = \text{Debt} - \text{Cash}$ *(en **EUR millions**, €m)*
  - $\text{Net Debt to EBITDA} = \dfrac{\text{Debt} - \text{Cash}}{\text{EBITDA}}$ *(multiple en **$\times$ EBITDA**)*

#### B. Tableau des résultats complets (et ratios complémentaires d'analyse)

| Indicateur (Unité) | Formule | Profile A | Profile B | Profile C | Profile D | Profile E |
|---|---|---:|---:|---:|---:|---:|
| **Operating BFR (WCR)** (€m) | $\text{Inv} + \text{Rec} - \text{Pay}$ | **$-\mathbf{40{,}0\text{ M€}}$** | **$+\mathbf{190{,}0\text{ M€}}$** | **$+\mathbf{54{,}0\text{ M€}}$** | **$+\mathbf{60{,}0\text{ M€}}$** | **$+\mathbf{65{,}0\text{ M€}}$** |
| *Operating BFR / Revenue* (%) | $\text{BFR} / \text{Rev}$ | *-4,0 %* | *+38,0 %* | *+14,8 %* | *+20,0 %* | *+16,25 %* |
| **DSO** (jours) | $(\text{Rec} / \text{Rev}) \times 365$ | **1,83 j** | **73,00 j** | **60,00 j** | **54,75 j** | **9,13 j** |
| **DIO** (jours) | $(\text{Inv} / \text{COGS}) \times 365$ | **31,63 j** | **164,25 j** | **60,00 j** | **121,67 j** | **243,33 j** |
| **DPO** (jours) | $(\text{Pay} / \text{COGS}) \times 365$ | **53,53 j** | **82,13 j** | **70,00 j** | **60,83 j** | **76,04 j** |
| **CCC** (jours) | $\text{DIO} + \text{DSO} - \text{DPO}$ | **$-\mathbf{20{,}07\text{ j}}$** | **$+\mathbf{155{,}13\text{ j}}$** | **$+\mathbf{50{,}00\text{ j}}$** | **$+\mathbf{115{,}58\text{ j}}$** | **$+\mathbf{176{,}42\text{ j}}$** |
| **Net Debt** (€m) | $\text{Debt} - \text{Cash}$ | **$80{,}0\text{ M€}$** | **$140{,}0\text{ M€}$** | **$80{,}0\text{ M€}$** | **$40{,}0\text{ M€}$** | **$-\mathbf{30{,}0\text{ M€}}$** *(Net Cash)* |
| **Net Debt / EBITDA** ($\times$) | $(\text{Debt} - \text{Cash}) / \text{EBITDA}$ | **$1{,}45\times$** | **$2{,}80\times$** | **$1{,}60\times$** | **$0{,}44\times$** | **$-\mathbf{0{,}30\times}$** |
| *Gross Margin* (%) *(repère)* | $(\text{Rev} - \text{COGS}) / \text{Rev}$ | *25,0 %* | *20,0 %* | *40,0 %* | *70,0 %* | *70,0 %* |
| *EBITDA Margin* (%) *(repère)* | $\text{EBITDA} / \text{Rev}$ | *5,5 %* | *10,0 %* | *13,7 %* | *30,0 %* | *25,0 %* |

*Détail des calculs par profil :*
- **Profile A** : $\text{BFR} = 65 + 5 - 110 = -40\text{ M€}$ ; $\text{DSO} = (5/1000)\times 365 = 1{,}825\text{ j}$ ; $\text{DIO} = (65/750)\times 365 = 31{,}633\text{ j}$ ; $\text{DPO} = (110/750)\times 365 = 53{,}533\text{ j}$ ; $\text{CCC} = 31{,}633 + 1{,}825 - 53{,}533 = -20{,}075\text{ j}$ ; $\text{Net Debt / EBITDA} = (140-60)/55 = 80/55 = 1{,}455\times$.
- **Profile B** : $\text{BFR} = 180 + 100 - 90 = +190\text{ M€}$ ; $\text{DSO} = (100/500)\times 365 = 73{,}00\text{ j}$ ; $\text{DIO} = (180/400)\times 365 = 164{,}25\text{ j}$ ; $\text{DPO} = (90/400)\times 365 = 82{,}125\text{ j}$ ; $\text{CCC} = 164{,}25 + 73{,}00 - 82{,}125 = +155{,}125\text{ j}$ ; $\text{Net Debt / EBITDA} = (180-40)/50 = 140/50 = 2{,}80\times$.
- **Profile C** : $\text{BFR} = 36 + 60 - 42 = +54\text{ M€}$ ; $\text{DSO} = (60/365)\times 365 = 60{,}00\text{ j}$ ; $\text{DIO} = (36/219)\times 365 = 60{,}00\text{ j}$ ; $\text{DPO} = (42/219)\times 365 = 70{,}00\text{ j}$ ; $\text{CCC} = 60 + 60 - 70 = +50{,}00\text{ j}$ ; $\text{Net Debt / EBITDA} = (100-20)/50 = 80/50 = 1{,}60\times$.
- **Profile D** : $\text{BFR} = 30 + 45 - 15 = +60\text{ M€}$ ; $\text{DSO} = (45/300)\times 365 = 54{,}75\text{ j}$ ; $\text{DIO} = (30/90)\times 365 = 121{,}67\text{ j}$ ; $\text{DPO} = (15/90)\times 365 = 60{,}83\text{ j}$ ; $\text{CCC} = 121{,}67 + 54{,}75 - 60{,}83 = +115{,}58\text{ j}$ ; $\text{Net Debt / EBITDA} = (120-80)/90 = 40/90 = 0{,}44\times$.
- **Profile E** : $\text{BFR} = 80 + 10 - 25 = +65\text{ M€}$ ; $\text{DSO} = (10/400)\times 365 = 9{,}125\text{ j}$ ; $\text{DIO} = (80/120)\times 365 = 243{,}33\text{ j}$ ; $\text{DPO} = (25/120)\times 365 = 76{,}04\text{ j}$ ; $\text{CCC} = 243{,}33 + 9{,}125 - 76{,}04 = +176{,}42\text{ j}$ ; $\text{Net Debt / EBITDA} = (60-90)/100 = -30/100 = -0{,}30\times$.

---

### Question 2 — Association de chaque profil à son secteur (3+ indices financiers + interprétations alternatives)

| Profil | Secteur identifié | 3+ Indices financiers décisifs (Clues) | Interprétation alternative plausible (et comment trancher) |
|---|---|---|---|
| **A** | **Supermarket** *(Grande distribution alimentaire)* | 1. **DSO quasi nul ($1{,}83\text{ j}$)** : règlement immédiat des consommateurs en magasin (espèces / règlement carte bancaire en 24–48h).<br>2. **BFR négatif ($-40\text{ M€}$) et CCC négatif ($-20{,}07\text{ j}$)** : rotation rapide des stocks ($\text{DIO} = 31{,}6\text{ j}$) payés aux fournisseurs à $53{,}5\text{ j}$ ($\text{DPO} > \text{DIO} + \text{DSO}$).<br>3. **Volume massif ($1\,000\text{ M€}$) et marge EBITDA très faible ($5{,}5\%$)** avec marge brute de $25\%$ : modèle typique *high-volume, low-margin* du retail alimentaire. | *Alternative* : une chaîne de restauration rapide ou d'e-commerce B2C généraliste présenterait aussi un DSO $\approx 2\text{ j}$ et un BFR négatif, mais la taille de l'actif immobilisé ($220\text{ M€}$ de magasins/entrepôts) et la marge EBITDA de $5{,}5\%$ collent exactement au supermarché. |
| **B** | **Aircraft manufacturer** *(Constructeur aéronautique / équipementier lourd)* | 1. **Cycle de production extrêmement long ($\text{DIO} = 164{,}25\text{ j}$ soit $\approx 5{,}5\text{ mois}$, $\text{Inventory} = 180\text{ M€}$)** : poids massif des encours de production (Work-in-Progress / assemblages longs).<br>2. **BFR opérationnel colossal ($+190\text{ M€}$, soit $38\%$ du CA)** combiné à un **DSO long ($73\text{ j}$)** (clients B2B compagnies aériennes/États) et des immobilisations lourdes (**Fixed Assets $= 250\text{ M€}$**, le plus élevé de l'échantillon).<br>3. **Endettement net élevé ($\text{Net Debt} = 140\text{ M€}$, levier $2{,}80\times\text{EBITDA}$)** et marge brute industrielle ($20\%$) : industrie lourde très consommatrice de capitaux. | *Alternative* : un grand exportateur de biens d'équipement / machines-outils sur mesure (*heavy industrial exporter*). On tranche entre B et C par la durée de cycle ($\text{DIO} = 164\text{ j}$ et $\text{BFR/CA} = 38\%$ pour B contre $\text{DIO} = 60\text{ j}$ et $\text{BFR/CA} = 14{,}8\%$ pour C). Note : l'énoncé précise *« no customer advances included »*, ce qui explique pourquoi le BFR de l'avionneur B apparaît intégralement à financer par dette. |
| **C** | **Industrial exporter** *(Exportateur industriel B2B)* | 1. **DSO B2B classique à $60{,}0\text{ j}$** et **DIO industriel standard à $60{,}0\text{ j}$** : cycle de fabrication et d'expédition export régulier.<br>2. **DPO négocié à $70{,}0\text{ j}$**, laissant un **CCC positif maîtrisé de $50{,}0\text{ j}$** ($\text{BFR} = 54\text{ M€}$, soit $14{,}8\%$ du CA) — exactement les chiffres de l'exemple fil rouge du cours (Slides 24 & 35–38).<br>3. **Marge brute industrielle de $40\%$ et marge d'EBITDA de $13{,}7\%$**, avec une base d'usines significative ($\text{Fixed Assets} = 180\text{ M€}$ pour $365\text{ M€}$ de CA) et une trésorerie serrée ($20\text{ M€}$). | *Alternative* : un sous-traitant aéronautique de rang 2 ou un chimiste de spécialité B2B. La structure équilibrée ($60\text{ j} / 60\text{ j} / 70\text{ j}$) et la marge brute de $40\%$ signent l'industriel exportateur. |
| **D** | **Pharmaceutical company** *(Laboratoire pharmaceutique)* | 1. **Marge brute très élevée ($70\%$, $\text{COGS} = 30\%$ du CA) et plus forte marge d'EBITDA ($30{,}0\%$)** : typique d'une industrie de propriété intellectuelle / brevets à faible coût marginal de fabrication.<br>2. **Ventes B2B ($\text{DSO} = 54{,}75\text{ j}$)** : contrairement au luxe, la pharma vend à des grossistes-répartiteurs, hôpitaux et organismes de santé qui paient à $\approx 55\text{ j}$.<br>3. **DIO élevé ($121{,}67\text{ j}$ sur un petit COGS de $90\text{ M€}$)** lié aux principes actifs (API), contrôles qualité réglementaires et stocks de sécurité sanitaires, couplé à un bilan très liquide ($\text{Cash} = 80\text{ M€}$, $\text{Net Debt / EBITDA} = 0{,}44\times$) pour financer la R&D. | *Alternative* : si on ne regardait que la marge brute de $70\%$, on pourrait hésiter avec le **Luxury (E)** ; mais le **DSO de $54{,}8\text{ j}$ (D, B2B santé) contre $9{,}1\text{ j}$ (E, boutiques retail B2C)** et le **DIO de $122\text{ j}$ vs $243\text{ j}$** permettent de distinguer sans ambiguïté la Pharma (D) du Luxe (E). |
| **E** | **Luxury company** *(Maison de luxe)* | 1. **Marge brute exceptionnelle ($70\%$) et marge EBITDA de $25\%$** : pricing power élevé de la marque.<br>2. **Combinaison unique : DSO très court ($9{,}13\text{ j}$) + DIO très long ($243{,}33\text{ j} \approx 8\text{ mois}$)** : ventes majoritairement en boutiques propres (retail B2C payé comptant + petite part wholesale/duty-free expliquant les $9\text{ j}$), mais stocks très lourds ($80\text{ M€}$ pour $120\text{ M€}$ de COGS) dus au vieillissement/artisanat (maroquinerie, horlogerie, spiritueux), aux matières rares et au refus des soldes.<br>3. **Trésorerie nette positive ($\text{Net Debt} = -30\text{ M€}$, $\text{Cash} = 90\text{ M€} > \text{Debt} = 60\text{ M€}$)** : structure financière ultra-saine typique des groupes de luxe. | *Alternative* : joaillier / producteur de champagne ou cognac (sous-secteur du luxe où le vieillissement porte le DIO à $>200\text{ j}$). |

---

### Question 3 — Comparaison des profils A et B : qui immobilise le plus de cash, et pourquoi le CCC seul ne permet de déclarer aucun des deux « sain/safe » ?

1. **Qui immobilise le plus de cash dans ses opérations ?**
   - C'est **le Profil B (Aircraft manufacturer)**, et de très loin :
     - **En valeur absolue** : B immobilise **$\text{Operating BFR} = +190\text{ M€}$** de cash dans son cycle d'exploitation ($180\text{ M€}$ de stocks + $100\text{ M€}$ de créances $-$ $90\text{ M€}$ de dettes fournisseurs), soit **$38\%$ de son chiffre d'affaires** ($3{,}8\times$ son EBITDA annuel !).
     - **En durée** : son cycle de conversion de cash est de **$\text{CCC} = +155{,}1\text{ jours}$** ($\approx 5\text{ mois}$ de décalage à financer entre le paiement des fournisseurs et l'encaissement des clients).
     - À l'inverse, **le Profil A (Supermarket)** affiche un **$\text{Operating BFR négatif de }-40\text{ M€}$** ($-4\%$ du CA) et un **$\text{CCC négatif de }-20{,}1\text{ jours}$** : ce sont ses fournisseurs ($110\text{ M€}$ de dettes fournisseurs) qui financent ses stocks ($65\text{ M€}$) et ses créances ($5\text{ M€}$), dégageant une ressource nette de trésorerie de $40\text{ M€}$.

2. **Pourquoi NI A NI B ne peuvent être déclarés « safe » (à l'abri du risque de liquidité) sur la seule base du CCC ?**
   - **Pourquoi un CCC négatif ($-20{,}1\text{ j}$) ne rend PAS le Profil A « safe » (Slides 39–41)** :
     1. *Illusion du BFR négatif / risque d'arriérés fournisseurs* : un DPO élevé ($53{,}5\text{ j}$, $110\text{ M€}$) peut cacher des **factures fournisseurs en retard (overdue payables)** plutôt que des délais contractuels sains. Si les fournisseurs réduisent leurs délais de seulement $15\text{ jours}$, A perd immédiatement $\frac{15}{365}\times 750 = 30{,}8\text{ M€}$ de cash (la moitié de sa trésorerie !).
     2. *Sensibilité à une baisse d'activité* : avec un BFR négatif, **une baisse du chiffre d'affaires détruit du cash** (les dettes fournisseurs de $110\text{ M€}$ arrivent à échéance alors que les ventes au comptant ralentissent).
     3. *Marge très fine et obligations hors-BFR* : la marge d'EBITDA de A n'est que de **$5{,}5\%$ ($55\text{ M€}$)**, alors qu'il porte **$140\text{ M€}$ de dette brute** ($\text{Net Debt / EBITDA} = 1{,}45\times$) et $220\text{ M€}$ d'actifs fixes à entretenir. Le CCC ignore les salaires, loyers, impôts, CapEx de maintenance et les échéances de remboursement de la dette.
   - **Pourquoi un CCC très élevé ($+155{,}1\text{ j}$) ne signifie PAS automatiquement que B va faire défaut — mais pourquoi son diagnostic exige d'aller au-delà du CCC** :
     1. *Le CCC est une moyenne annuelle statique, pas un échéancier de trésorerie daté* : il ne dit pas **quand** tombent les prochaines échéances de salaires, de fournisseurs ou de dette, ni quelles lignes de crédit tirables (committed RCF) sont disponibles.
     2. *Mais B cumule ici tous les signaux d'alerte hors-CCC* : un levier élevé (**$\text{Net Debt / EBITDA} = 2{,}80\times$**, dette brute de $180\text{ M€}$), seulement **$40\text{ M€}$ de cash** (à peine $36\text{ jours}$ de COGS), et $280\text{ M€}$ bloqués en stocks + créances. Le moindre retard de livraison d'un avion (qui bloque l'encaissement d'une grosse créance) ou de paiement d'un client crée un trou de liquidité immédiat.

---

### Question 4 — Recommandations au CFO : une priorité spécifique et actionnable par entreprise

> *Méthode du cours : Cibler le levier prioritaire $\rightarrow$ Chiffrer le gain de cash potentiel $\rightarrow$ Préciser le garde-fou opérationnel (trade-off).*

1. **Profile A (Supermarket) — Priorité : Sécuriser la soutenabilité du crédit fournisseurs ($110\text{ M€}$) et stress-tester la liquidité en cas de baisse de CA**
   - **Pourquoi** : Le modèle repose sur un BFR négatif ($-40\text{ M€}$) et une marge d'EBITDA très fine ($5{,}5\%$), avec $140\text{ M€}$ de dette brute contre $60\text{ M€}$ de cash.
   - **Action concrète CFO** : Auditer immédiatement l'échéancier des $110\text{ M€}$ de *Payables* pour vérifier qu'il n'y a aucun arriéré critique (*0 overdue*), mettre en place une ligne de crédit confirmée (RCF) couvrant un choc de $-10\text{ j}$ de DPO ($\approx \frac{10}{365}\times 750 = 20{,}5\text{ M€}$ de sortie de cash), et utiliser l'excédent de cash opérationnel pour réduire la dette brute de $140\text{ M€}$.

2. **Profile B (Aircraft manufacturer) — Priorité : Libérer du cash opérationnel sur le DIO ($164{,}3\text{ j}$) et le DSO ($73\text{ j}$) + sécuriser le refinancement ($\text{Net Debt / EBITDA} = 2{,}80\times$)**
   - **Pourquoi** : Avec $190\text{ M€}$ bloqués dans le BFR ($38\%$ du CA), un levier à $2{,}80\times\text{EBITDA}$ et seulement $40\text{ M€}$ de cash, B est en zone de vulnérabilité maximale (risque de liquidité + risque de funding).
   - **Action concrète CFO (chiffrée)** :
     - **Opérations & Commerce** : introduire des acomptes contractuels à la commande / jalons (*milestone progress payments*), réduire le **DSO de $13\text{ jours}$** (de $73\text{ j}$ à $60\text{ j}$ $\implies \text{gain cash} = 500 \times \frac{13}{365} =$ **$+17{,}8\text{ M€}$**) et réduire le **DIO de $20\text{ jours}$** sur les encours non critiques ($\implies \text{gain cash} = 400 \times \frac{20}{365} =$ **$+21{,}9\text{ M€}$**), soit **$\approx +40\text{ M€}$ de cash libéré** (doublant le buffer de cash ou ramenant le levier Net Debt/EBITDA de $2{,}80\times$ à $2{,}00\times$).

3. **Profile C (Industrial exporter) — Priorité : Reconstituer le buffer de liquidité ($20\text{ M€}$ trop faible) et couvrir le risque de change FX de manière sélective**
   - **Pourquoi** : Le cycle de BFR est sain et équilibré ($\text{DSO } 60\text{ j} / \text{DIO } 60\text{ j} / \text{DPO } 70\text{ j} \implies \text{CCC } 50\text{ j}$), **mais** la trésorerie disponible n'est que de **$20\text{ M€}$** ($5{,}5\%$ du CA, le plus faible de tous les profils) face à $100\text{ M€}$ de dette et $60\text{ M€}$ de créances à l'export.
   - **Action concrète CFO (chiffrée)** :
     - Réduire le **DSO de $10\text{ jours}$** (relance / résolution des litiges clients, passant de $60\text{ j}$ à $50\text{ j}$) et le **DIO de $10\text{ jours}$** : cela libère $(365 \times \frac{10}{365}) + (219 \times \frac{10}{365}) = 10 + 6 =$ **$+16\text{ M€}$ de cash**, portant le cash de $20\text{ M€}$ à $36\text{ M€}$ (Exactement l'exemple de la Slide 42 du cours !).
     - En parallèle, mettre en place une politique de couverture FX **par paliers (layered forwards, ex. 50–70% du carnet ferme)** pour protéger la marge export sans risquer la sur-couverture (*over-hedging*, Slide 21) en cas de retard de paiement client.

4. **Profile D (Pharmaceutical company) — Priorité : Optimiser le recouvrement des créances B2B ($\text{DSO} = 54{,}8\text{ j}$) et le rendement/allocation de l'importante trésorerie ($80\text{ M€}$)**
   - **Pourquoi** : La rentabilité est excellente ($\text{EBITDA} = 90\text{ M€}$, marge $30\%$) et le levier très bas ($0{,}44\times$), mais la société conserve à la fois $80\text{ M€}$ de cash et $120\text{ M€}$ de dette brute (*cost of carry* négatif si la dette coûte plus cher que le placement du cash), et ses créances clients représentent $15\%$ du CA.
   - **Action concrète CFO (chiffrée)** :
     - Ramener le **DSO de $54{,}75\text{ j}$ à $45\text{ j}$** auprès des distributeurs/hôpitaux ($\implies \text{gain cash} = 300 \times \frac{9{,}75}{365} =$ **$+8{,}0\text{ M€}$**), **sans** toucher aux stocks de sécurité critiques ($\text{DIO} = 121{,}7\text{ j}$ indispensables pour éviter les ruptures de médicaments).
     - Utiliser une partie du cash excédentaire ($80\text{ M€}$) pour rembourser par anticipation une tranche de la dette brute ($120\text{ M€}$) afin d'économiser les frais financiers tout en gardant un buffer R&D/M&A.

5. **Profile E (Luxury company) — Priorité : Arbitrer l'allocation de la trésorerie nette positive ($+30\text{ M€}$ Net Cash) et piloter la composition des stocks ($\text{DIO} = 243{,}3\text{ j}$)**
   - **Pourquoi** : E est en situation de **Net Cash ($90\text{ M€}$ de cash pour $60\text{ M€}$ de dette, $\text{Net Debt / EBITDA} = -0{,}30\times$)** avec un DSO très court ($9{,}1\text{ j}$), mais immobilise **$80\text{ M€}$ de stocks ($\text{DIO} = 243{,}3\text{ j}$)**.
   - **Action concrète CFO (chiffrée)** :
     - Segmenter les $80\text{ M€}$ de stocks entre **stocks stratégiques/permanents** (matières rares, vieillissement, icônes intemporelles — à préserver absolument pour protéger l'image de marque) et **stocks saisonniers à rotation lente** : réduire le DIO de seulement **$20\text{ jours}$** via un meilleur *demand planning* libère $120 \times \frac{20}{365} =$ **$+6{,}6\text{ M€}$** sans brader les prix.
     - Définir avec le Board une politique d'investissement du surplus de cash ($90\text{ M€}$) : placements monétaires sécurisés/liquides (MMF), remboursement de dette à l'échéance ou retour aux actionnaires (dividendes / rachat d'actions).
