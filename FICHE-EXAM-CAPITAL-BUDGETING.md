# FICHE EXAM — CAPITAL BUDGETING (Pr. Sébastien Dereeper) — Steps 1 & 2

> **Sources** : `Capital budgeting Introduction.pptx` (6 slides) + `Capital budgeting Step 1.pptx` (71 slides) + `Capital budgeting Step 2.pptx` (49 slides) — Berk & De Marzo, *Corporate Finance*, Pearson 2024 (ch. 7 et 8).
> **+ `Capital budgeting.docx`** = transcription audio du cours de 4 h du 28/09 → contient **les dates et modalités d'examen** (section 0) et les insistances du prof.
> Fiche établie le 29/09/2026 après le cours des 28 et 29/09 (bloc de 6 h).

---

## 0. ÉVALUATION — ce que le prof a annoncé en cours (audio du 28/09)

| | Midterm | Final |
|---|---|---|
| **Date** | **mardi 27 octobre 2026** | **mardi 10 novembre 2026, début d'après-midi** |
| **Durée** | 45 min | 90 min |
| **Format** | **30 questions QCM** (1 seule bonne réponse / proposition) | **questions de cours + exercices chiffrés** |
| **Barème** | +1 si juste, **0 si faux, 0 si pas de réponse → aucune pénalité** | — |
| **Note** | 30 pts = 20/20 ; 20 pts = 13,3/20 | — |
| **Plateforme** | **K2 + Safe Exam Browser (SEB)** — tout est bloqué (Excel, calculatrice PC, onglets) | idem K2 |
| **À apporter** | **calculatrice physique obligatoire** (SEB bloque celle du PC) | idem |
| **Pondération** | **40 %** | **60 %** |

*Points logistiques donnés par le prof :*
- Il fera un **essai SEB en amont** pour vérifier que ça tourne sur chaque machine (à faire dès que proposé — sinon version papier en secours).
- Correction **le jour même** pour la version K2 → note rapide.
- Les **supports sont déposés sur K2** : Step 1 dispo, **Step 2 et Step 3 seront mis en ligne** → à télécharger.
- ⚠️ **Il a prévenu que le programme du lundi matin peut tomber au test du mardi** → le cours du **lundi 26/10** fait partie du périmètre du midterm. Pas de révision « au feeling » ce week-end-là : tout ce qui a été traité avant le 27/10 est examinable.
- Le QCM est **aussi conceptuel** : il a explicitement fait un « wake up » sur *« que représente le 27,9 % ? »* → savoir **lire/interpréter un tableau**, pas seulement le recalculer.

### Plan du cours (18 h, 5 étapes)

| Step | Contenu | Référence Berk-De Marzo | Durée |
|---|---|---|---|
| **1** | **Calculer les cash flows** (cœur classique) | ch. 8 *Fundamentals of Capital Budgeting* | 4 h |
| **2** | **Rappel des règles de décision d'investissement** | ch. 7 *Investment Decision Rules* | 2 h |
| **3** | Coût de la dette, coût des fonds propres, coût du capital (**rappel**, pas de gestion de portefeuille) | ch. 12 *Estimating the Cost of Capital* | 2 h |
| **4** | **Cœur du cours (7 h)** : structure de capital et capital budgeting avec levier — MM 1958 (marchés parfaits) → fiscalité (bouclier fiscal) → valorisation avec levier | ch. 14, 15, 18 | 7 h |
| **5** | **Optionnel si le temps le permet (3 h)** : se méfier de la dette — détresse financière, coûts d'agence | ch. 16 | 3 h |

> **Annonce forte du prof** : le **Step 4 est le vrai saut de niveau** par rapport au M1. Message clé : *« la structure de capital influence le NPV d'un investissement »* — en marchés parfaits **la dette ne crée pas de valeur** (MM 1958), puis avec les **impôts la dette crée de la valeur** parce que les intérêts sont déductibles. Le Step 5 = le **revers** : la dette crée des obligations et de la **détresse financière**, donc « be careful with debt ».
> **Prérequis déclarés** : mathématiques financières, lecture des états financiers, cours de corporate finance M1.

---

## 1. STEP 1 — CALCULER LES CASH FLOWS

### 1.1 Vocabulaire de base (QCM)
- **Capital budget** = liste des investissements qu'une entreprise prévoit de réaliser.
- **Capital budgeting** = processus d'analyse des investissements alternatifs et de décision d'acceptation/rejet.
- **Incremental earnings** = variation **attendue** du résultat de l'entreprise **du fait** de la décision d'investissement. Règle d'or : **on ne retient que ce qui change**.
- **Free cash flow** = effet incrémental du projet sur le cash disponible de la firme.

### 1.2 Le cas HomeNet (Linksys) — le fil rouge à connaître par cœur

**Données** : étude de faisabilité 300 000 $ (**sunk → à exclure**) ; durée de vie 4 ans ; prix unitaire 260 $ ; coût unitaire 110 $ ; R&D upfront 15 000 000 $ ; équipement 7 500 000 $ (**5 ans**, amortissement linéaire) ; overhead annuel 2 800 000 $ ; volume 100 000 unités/an.

**3 niveaux de complexité, dans l'ordre du cours :**

| Ligne (\$000s) | An 0 | An 1 | An 2 | An 3 | An 4 | An 5 |
|---|---|---|---|---|---|---|
| **Tab. 1 — cas simple** : CA 26 000 ; COGS (11 000) ; marge brute 15 000 ; SG&A (2 800) ; R&D (15 000) ; amortissement (1 500)/an ; **EBIT** (15 000) / 10 700 / 10 700 / 10 700 / 10 700 / (1 500) ; impôt 20 % 3 000 / (2 140)×4 / 300 ; **UNI** (12 000) / 8 560 / 8 560 / 8 560 / 8 560 / (1 200) | | | | | | |
| **Tab. 2 — + cannibalisation (25 %)** : CA 23 500 ; COGS (9 500) ; marge 14 000 ; SG&A (3 000) ; **EBIT** (15 000) / 9 500 ×4 / 9 500 ; impôt 3 000 / (1 900)×4 / 300 ; **UNI** (12 000) / **7 600** ×4 / **(1 200)** | | | | | | |
| **Tab. 3 — + adoption/prix réels** (volumes 100k / 125k / 125k / 50k ; **prix et coût unitaire −10 %/an** ; SG&A **+4 %/an**) : CA 23 500 / 26 438 / 23 794 / 8 566 ; **EBIT** (15 000) / 9 500 / 11 130 / 9 430 / 228 / (1 500) ; **UNI** (12 000) / 7 600 / 8 904 / 7 544 / 183 / (1 200) | | | | | | |

> ⚠️ **Pourquoi l'an 5 existe alors que le projet dure 4 ans** : l'équipement s'amortit sur **5 ans** → il génère une **charge non-cash** (et un bouclier fiscal) en an 5 alors qu'il n'y a plus de ventes. C'est une question de QCM typique.

**Le tableau « anchor » — HomeNet Free Cash Flow (Tab. 5) :**

| (\$000s) | An 0 | An 1 | An 2 | An 3 | An 4 | An 5 |
|---|---|---|---|---|---|---|
| Unlevered Net Income (Tab. 2) | (12 000) | 7 600 | 7 600 | 7 600 | 7 600 | (1 200) |
| \+ Amortissement | — | 1 500 | 1 500 | 1 500 | 1 500 | 1 500 |
| − Capital expenditures | (7 500) | — | — | — | — | — |
| − Δ Net Working Capital | — | (2 100) | — | — | — | 2 100 |
| **= Free Cash Flow** | **(19 500)** | **7 000** | **9 100** | **9 100** | **9 100** | **2 400** |

**Le NWC (Tab. 4)** : créances = 15 % du CA (3 525) ; dettes fournisseurs = 15 % des COGS (1 425) ; **NWC = 2 100**, investi et **récupéré intégralement en fin de projet**.
→ *Trade credit* = différence entre créances et dettes fournisseurs. Toute **augmentation** du NWC est une **sortie de cash**.

### 1.3 Faut-il l'inclure dans les cash flows ? (la question la plus rentable du QCM)

| À **INCLURE** | Pourquoi |
|---|---|
| **Coûts d'opportunité** | valeur de la ressource dans sa **meilleure utilisation alternative**. Ex. le local : même « déjà possédé », on renonce au loyer → HomeNet Ex. 2 : loyer abandonné de 200 000 $/an en an 1-4, **net d'impôt** (baisse de l'UNI du **bénéfice après impôt du loyer**) |
| **Externalités du projet / cannibalisation** | effet indirect sur les autres activités. Ex. HomeNet : 25 % des ventes viennent de clients qui auraient acheté le routeur existant → **−25 000 u à 100 $** de CA, mais **économie de coût de 25 u à 60 $** → CA net 23 500 et COGS 9 500 |
| **Capital expenditures** | sortie de cash réelle à l'achat (an 0) |
| **Δ NWC** | cash immobilisé (puis libéré) |
| **Impôts marginaux** | au **taux marginal**, pas au taux moyen |

| À **EXCLURE** | Pourquoi |
|---|---|
| **Sunk costs** | déjà payés / payables quoi qu'il arrive. Ex. **les 300 000 $ d'étude de faisabilité**, la **R&D passée**. « La décision de continuer ou d'abandonner ne doit dépendre que des coûts et bénéfices **incrémentaux futurs** » |
| **Frais généraux fixes (overhead)** | non incrémentaux au projet → sauf la part réellement déclenchée par le projet |
| **Interest expense** | **le projet doit être jugé en lui-même, pas selon son financement**. Le mode de financement est capté par le **taux d'actualisation** (WACC), sinon on compte deux fois |
| **Effets concurrentiels inévitables** | si les ventes auraient baissé de toute façon (nouveaux produits des concurrents) → perte = **sunk cost** |

### 1.4 Impôts
- **Taux marginal d'IS** = taux sur le dollar marginal de résultat avant impôt. **Un impôt négatif = un crédit d'impôt** (cas an 0 du HomeNet : +3 000).
- **Unlevered Net Income = EBIT × (1 − τc)**.
- **Reports fiscaux** : *tax loss carryforwards* (report en avant) et *carrybacks* (en arrière) → une perte courante s'impute sur les bénéfices d'années proches.

### 1.5 La formule à écrire les yeux fermés

```
Free Cash Flow = Unlevered Net Income + Amortissement − CapEx − Δ NWC
```

- **Amortissement** : charge **non-cash** → on le **rajoute** ; il ne crée de la valeur que par le **bouclier fiscal** (**depreciation tax shield = τc × amortissement**).
- Version directe (slide 32) : `FCF = (CA − coûts) × (1 − τc) + τc × amortissement − CapEx − ΔNWC`. Le terme `τc × amortissement` est le **depreciation tax shield**.

### 1.6 NPV, WACC, IRR du projet HomeNet
- Taux d'actualisation = **coût du capital du projet (WACC) = 12 %** ; facteurs d'actualisation 1,000 / 0,893 / 0,797 / 0,712 / 0,636 / 0,567.
- PV des FCF = 6 250 / 7 254 / 6 477 / 5 783 / 1 362 → **NPV = 7 627 k$ (≈ 7,627 M$)** → **projet accepté**.
- **IRR = 27,9 %**.
- Interprétation (le prof y est revenu 3 fois) : l'IRR est **le taux pour lequel NPV = 0**, mais c'est aussi **le rendement moyen du projet** → 27,9 % de rendement contre 12 % exigés par les apporteurs de fonds = création de valeur. **Les deux lectures (NPV et IRR) racontent la même histoire ici.**

### 1.7 Choisir entre alternatives (mutuellement exclusives dans le Step 1)
HomeNet : **sous-traiter** (110 $/u) vs **produire en interne** (95 $/u + 5 M$ d'investissement upfront + stock = 1 mois de production).
- Sous-traitance : NWC **baisse** (les dettes fournisseurs sont financées par le fournisseur) → +1,65 M$ en an 5.
- Interne : NWC baisse de 0,633 M$ en an 1 puis remonte de 0,633 M$ en an 5.
- **Conclusion : la sous-traitance est l'alternative la moins chère** → en cas d'arbitrage, on compare les **NPV des FCF incrémentaux**, pas les coûts comptables.

### 1.8 Les 4 ajustements supplémentaires au FCF

**(a) Amortissements accélérés (MACRS)**
- *Modified Accelerated Cost Recovery System* : barème fiscal US par durée de vie, avec convention mi-année → **déductions plus fortes en début de vie** → **PV du bouclier fiscal plus élevée** → **NPV plus élevé**. Si l'actif est mis en service avant la fin de l'an 0, la 1ʳᵉ déduction se fait dès l'an 0.
- **Bonus depreciation** : déduire 100 % en an 0 → NPV encore plus haut.
- ⚠️ Ne pas oublier les autres **non-cash items** (amortissement des incorporels) et le fait que les cash flows sont **étalés dans l'année**.

**(b) Valeur de liquidation / cession (salvage) — HomeNet Ex. 5**
Équipement transféré d'une autre usine : **valeur de revente 2 M$**, **valeur comptable 1 M$**. À la fermeture (an 5) : revente 800 000 $.
- **An 0** : le renoncement à la vente est un **coût d'opportunité** → `−(2 000 − 20 % × (2 000 − 1 000))` = **−1 800** (on paie l'impôt sur la plus-value qu'on n'a pas réalisée).
- **An 1** : la VNC restante 1 000 devient amortissable → **bouclier fiscal +200**.
- **An 5** : l'actif est totalement amorti → **la totalité de la revente est imposable** → `800 × (1 − 20 %)` = **+640**.
- Nouveau FCF : (21 300) / 7 200 / 9 100 / 9 100 / 9 100 / 3 040 → **NPV = 6 368** (vs 7 627).
- 💡 Insistance du prof (audio) : *« quand vous achetez et vendez un actif, ayez toujours la valeur **nette d'impôt** »*. Il souligne que la vue « impôt sur une plus-value latente » est un point de vue de **calcul** ; la bonne pratique est de **faire porter la transaction par une entité** (la filiale vend, paie l'impôt) → le flux devient un **flux incrémental clair** (1,8 M$).

**(c) Valeur terminale / de continuation — Base Hardware**
FCF année 4 = 1 300 M$ ; au-delà, croissance **g = 5 %/an**, coût du capital **r = 10 %** →
`TV₄ = FCF₅ / (r − g) = 1 300 × 1,05 / (0,10 − 0,05) = 27 300` (**perpetuité croissante** ; 21 × le FCF de l'an 4).
FCF actualisés : (10 500) / (5 500) / 800 / 1 200 / **28 600** (1 300 + 27 300) → **NPV ≈ 5 597**.
- 💡 Le prof a longuement insisté : **« la valeur terminale est le point où on peut faire n'importe quoi »**. Exemple de l'appartement (40 m², 200 000 €, loyer 1 000 €/mois, IS 25 %, 20 ans, revente à la fin) : tout le rendement dépend des **hypothèses de revente** et de **croissance du loyer**. En QCM : *la valeur terminale est la valeur **de marché** des FCF **de tous les dates futures***.

**(d) Reports fiscaux (tax carryforwards) — Verian Industries**
Perte d'exploitation **140 M$**, résultat avant impôt futur **50 M$/an**. **Règle US : on ne peut absorber que 80 % du résultat imposable de l'année.** → utilisation de **40 / 40 / 40 / 20** → **résultat imposable 10 / 10 / 10 / 30 / 50**.
Avec +10 M$ de résultat en an 1 (donc 60) : report 48 / 40 / 40 / 12 → imposable **12 / 10 / 10 / 38 / 50**.
- **L'impôt d'une partie du résultat courant est donc **repoussé** → la valeur temps le réduit. En pratique on approxime parfois avec un **taux d'IS marginal plus faible**.
- 💡 Analogie du prof : la **rénovation d'un appartement** → le déficit de la 1ʳᵉ année se reporte sur les loyers positifs des 10 années suivantes.

### 1.9 Analyser le projet
**Break-even** = niveau d'un paramètre qui annule la NPV du projet.
| Paramètre HomeNet | Seuil |
|---|---|
| Unités vendues | **77 121 unités/an** |
| Prix de gros | **228 $/u** |
| Coût des biens vendus | **142 $/u** |
| Coût du capital | **27,9 %** (i.e. = IRR) |

**EBIT break-even of sales** = niveau de ventes où **EBIT = 0**.

**Sensitivity analysis** = effet sur la NPV de la variation **d'un seul** paramètre, les autres constants. (Table HomeNet pire/meilleur cas : unités 70k/130k ; prix 240/280 ; COGS 120/100 ; NWC 3 000/1 600 ; cannibalisation 40 %/10 % ; coût du capital 15 %/10 %.)
*Exemple HomeNet 6* : SG&A possiblement 3,8 M$ au lieu de 2,8 M$ → +1 M$ réduit le FCF de **800** après impôt/an ; PV = 800 × AF(12 %, 4 ans) = **2 430** → **NPV tombe à 5 197**.

**Scenario analysis** = variation **simultanée** de plusieurs hypothèses (ex. stratégies de prix : prix 260/100k → NPV 7 627 ; 245/110k → 7 032 ; 275/90k → 7 509).
→ Si on connaît les **probabilités** de chaque scénario : **expected NPV** = moyenne pondérée des NPV.

---

## 2. STEP 2 — LES RÈGLES DE DÉCISION D'INVESTISSEMENT

### 2.1 La règle NPV (stand-alone)
Projet Fredrick's Feed and Farm : coût **250 M$**, flux de **35 M$/an à perpétuité**.
`NPV = −250 + 35 / r`. À **r = 10 %** → **NPV = +100 M$** → accepter. (C'est une **perpétuité constante** : 35/0,10 = 350.)
- **Règle** : accepter si **NPV > 0** ; rejeter si NPV < 0. Le NPV dépend du taux d'actualisation.
- **Si une autre règle est en conflit avec le NPV → on suit le NPV.** (phrase à retenir pour le QCM)

### 2.2 La règle de l'IRR et ses **3 pièges**
**Règle** : accepter si **IRR > coût du capital** ; rejeter si IRR < coût du capital.
Ici **IRR = 35/250 = 14 %** → NPV > 0 tant que r < 14 %.
✅ **La règle fonctionne pour un projet stand-alone SI tous les cash flows négatifs précèdent les positifs** (une seule inversion de signe).

| Piège | Exemple Star (écrivain) | Leçon |
|---|---|---|
| **1. Delayed investments** (flux négatifs **après** les positifs) | +1 M$ aujourd'hui, **−500 k$/an pendant 3 ans**, opportunité 10 % → **IRR = 23,38 % > 10 %** mais **NPV = −243 k$ < 0** | Quand les bénéfices **précèdent** les coûts, la NPV est une fonction **croissante** du taux → **IRR et NPV divergent : suivre le NPV** |
| **2. Multiple IRRs** (plusieurs inversions de signe) | +550 k$ aujourd'hui, −500 k$ ×3, +1 M$ en an 4 → **deux IRR : 7,164 % et 33,673 %** ; NPV < 0 **entre** les deux | L'IRR n'est pas unique → **règle inapplicable** ; à r = 10 % → **rejeter** |
| **3. Nonexistent IRR** | +750 k$ aujourd'hui, −500 k$ ×3, +1 M$ en an 4 → **NPV > 0 pour tout r** | Aucun taux n'annule la NPV → **règle inapplicable** ; accepter |

⚠️ **Erreur fréquente à ne pas commettre** : *l'IRR (le chiffre) reste utile* — il mesure le **rendement moyen** du projet et la **sensibilité de la NPV à une erreur d'estimation du coût du capital**. C'est **la règle IRR** (le critère de décision) qui est défaillante.

### 2.3 La règle du Payback
**Payback period** = temps nécessaire pour récupérer l'investissement initial ; on accepte si < seuil fixé.
- Fredrick's avec seuil 5 ans : 35 × 5 = 175 < 250 → **rejet**, il faut **8 ans** pour rembourser.
- **Pitfalls** : ① ignore le **coût du capital / la valeur temps**, ② ignore **tous les cash flows après** le payback, ③ critère de seuil **arbitraire (ad hoc)**.
- Elle reste très utilisée… **par simplicité**.

### 2.4 Choisir entre projets mutuellement exclusifs
- **NPV** : retenir le **NPV le plus élevé**.
- **IRR** : retenir le **plus haut IRR** → **risque d'erreur** dès que le choix est exclusif. L'exemple du local commercial (perpétuités croissantes, `NPV = C₁/(r − g) − I`) :

| Projet | Invest. | C₁ | Croissance | Coût du capital | **IRR** | **NPV** |
|---|---|---|---|---|---|---|
| Librairie | 300 000 | 63 000 | 3 % | 8 % | **24 %** | 960 000 |
| **Coffee shop** | 400 000 | 80 000 | 3 % | 8 % | 23 % | **1 200 000** ✅ |
| Magasin de musique | 400 000 | 104 000 | 0 % | 8 % | 26 % | 900 000 |
| Électronique | 400 000 | 100 000 | 3 % | **11 %** | 28 % | 850 000 |

**Les 4 raisons pour lesquelles l'IRR se trompe en mutuellement exclusif :**
1. **Différence d'échelle** — doubler la taille double la NPV, **pas l'IRR** (librairie IRR 24 % > coffee 23 %, mais NPV 960k < 1 200k).
2. **Timing des cash flows** — un rendement vaut d'autant plus qu'il est **gagné longtemps** (même échelle, même horizon : musique IRR 26 % > coffee 23 % mais NPV inférieure car g = 0).
3. **Différence de risque** — un IRR attractif pour un projet sûr ne l'est pas pour un projet risqué (électronique : IRR 28 % le plus élevé, NPV 850k la plus faible, car coût du capital 11 %).
4. (Conséquence) **on ne peut pas comparer des IRR de projets de tailles différentes**.

### 2.5 L'**incremental IRR** — la bonne façon d'utiliser l'IRR
**Règle** : appliquer la règle de l'IRR **à la différence des cash flows** entre les deux alternatives.

*Exemple des révisions d'usine* (M$, projets exclusifs) :

| | An 0 | An 1 | An 2 | An 3 | IRR |
|---|---|---|---|---|---|
| Révision **mineure** | (10) | 6 | 6 | 6 | **36,3 %** |
| Révision **majeure** | (50) | 25 | 25 | 25 | **23,4 %** |
| **Incrément (majeure − mineure)** | **(40)** | **19** | **19** | **19** | **20,0 %** |

Coût du capital **12 %** → l'IRR incrémentale **20 % > 12 %** → **passer à la révision majeure est attractif** : l'échelle plus grande compense l'IRR plus faible. À r = 12 %, NPV majeure ≈ **10,05** > NPV mineure ≈ **4,41**.
→ **L'IRR incrémentale = le taux de croisement (*crossover*) des profils de NPV**, le taux auquel le meilleur choix s'inverse.
*(Note : dans le deck, les libellés du tableau slide 36 sont inversés — la logique correcte est bien majeure = −50/25/25/25, mineure = −10/6/6/6, comme le confirme le tableau d'incrément de la slide 38.)*

**Défauts de la règle incrémentale** : l'IRR incrémentale **peut ne pas exister** ; **plusieurs** IRR incrémentales possibles ; le fait que l'IRR dépasse le coût du capital **pour les deux projets** n'implique pas que **l'un** ait une NPV positive ; si les projets ont des **coûts du capital différents**, on ne sait pas à quoi comparer l'IRR incrémentale.

### 2.6 Profitability index et contraintes de ressources
**Profitability index = NPV / Investissement** (ou NPV / unité de ressource rare).
Budget de 100 M$, 3 projets :

| Projet | NPV | Investissement | **PI** |
|---|---|---|---|
| 1 | 110 | 100 | 1,10 |
| 2 | **70** | 50 | **1,40** |
| 3 | **60** | 50 | **1,20** |

→ Il vaut mieux prendre **2 et 3 ensemble** (NPV 130, investissement 100) et **renoncer à 1** (NPV 110) : le PI identifie la meilleure combinaison, pas le meilleur projet.

*NetIt (contrainte de ressources humaines, 190 ingénieurs, NPV en M$)* — on classe par **PI = NPV / ETP** :

| Rang | Projet | NPV | ETP | PI | ETP cumulés |
|---|---|---|---|---|---|
| 1 | A | 22,7 | 47 | 0,483 | 47 |
| 2 | F | 12,9 | 32 | 0,403 | 79 |
| 3 | E | 20,6 | 58 | 0,355 | 137 |
| 4 | **Router** | 17,7 | 50 | **0,354** | **187** |
| 5 | C | 14,0 | 40 | 0,350 | (dépassement) |
| 6 | D | 11,5 | 61 | 0,189 | |
| 7 | B | 8,1 | 44 | 0,184 | |

→ **Retenir A, F, E, Router** (187 ETP) → renoncer à **C, D, B** = **33,6 M$ de NPV abandonnée**.
*(Le slide affiche « $3.36 million » : coquille, la somme 14,0 + 11,5 + 8,1 = 33,6.)*

**Limites du PI :**
- **Ressource résiduelle** : un petit projet de NPV 120 k$ nécessitant 3 ingénieurs a un PI = 0,04 → classé dernier, **mais** 3 ingénieurs restent inutilisés après les 4 premiers projets → **il faut le prendre quand même**. Le classement par PI échoue quand la ressource ne peut pas être utilisée exactement.
- **Contraintes multiples** (plusieurs ressources rares) : **le PI s'effondre complètement** → il faut de l'optimisation combinatoire.

---

## 3. QCM — 20 pièges classiques (réponses en fin de fiche)

1. Une étude de faisabilité déjà payée doit être incluse dans les cash flows du projet. → **Faux** (sunk cost)
2. L'interest expense doit être déduit des FCF du projet. → **Faux** (le financement est dans le taux d'actualisation)
3. Le loyer auquel on renonce pour utiliser un local déjà possédé est un cash flow. → **Vrai** (coût d'opportunité, net d'impôt)
4. Un amortissement plus rapide réduit la NPV car il accélère les décaissements. → **Faux** (il augmente la PV du bouclier fiscal)
5. Toute augmentation du NWC est une sortie de cash. → **Vrai**
6. Le NWC est récupéré à la fin du projet. → **Vrai**
7. La NPV du projet dépend du mode de financement retenu dans le calcul du FCF. → **Faux** (on utilise les FCF **unlevered** + WACC)
8. Une charge non-cash n'a aucun effet sur la NPV. → **Faux** (effet via l'impôt)
9. Quand IRR et NPV s'opposent pour un projet stand-alone, on suit l'IRR. → **Faux**
10. La règle IRR est fiable si tous les flux négatifs précèdent les positifs. → **Vrai**
11. Un projet peut avoir deux IRR. → **Vrai** (plus d'une inversion de signe)
12. IRR = 20 % > coût du capital 12 % garantit NPV > 0. → **Faux** (delayed investments, IRR multiples)
13. Un projet sans IRR doit être rejeté. → **Faux** (NPV > 0 partout → accepter)
14. Le payback prend en compte les cash flows après la période de récupération. → **Faux**
15. En mutuellement exclusif, le projet avec le plus haut IRR a toujours la plus haute NPV. → **Faux** (échelle, timing, risque)
16. L'IRR incrémentale se compare au coût du capital. → **Vrai** (mais limites : existence, unicité, coûts du capital hétérogènes)
17. Le PI (=NPV/investissement) suffit pour choisir sous contrainte de ressources. → **Faux** (ressource résiduelle, contraintes multiples)
18. Un actif cédé totalement amorti génère un flux égal au prix de vente. → **Faux** (prix de vente **net d'impôt sur la plus-value**)
19. La valeur terminale = valeur de marché des FCF **de toutes les dates futures**. → **Vrai**
20. Sensitivity analysis = varier **simultanément** plusieurs paramètres. → **Faux** (c'est l'analyse de **scénarios**)

---

## 4. FORMULAIRE

```
Unlevered Net Income = EBIT × (1 − τc)
FCF                  = UNI + Amortissement − CapEx − ΔNWC
Depreciation tax shield = τc × Amortissement
NPV                  = Σ FCFt / (1 + r)^t          (accepter si > 0)
IRR                  = r tel que NPV(r) = 0        (accepter si > r)
Payback              = temps de récupération de I₀
PI                   = NPV / Investissement
Perpétuité constante :   PV = C / r
Perpétuité croissante :  PV = C₁ / (r − g)         [g < r]
Valeur terminale :       TV_T = FCF_{T+1} / (r − g)
VAN d'une annuité :      A × [1 − (1+r)^−n] / r
Après-impôt sur cession  = Prix − τc × (Prix − VNC)
```

---

## 5. EXERCICES D'ENTRAÎNEMENT (corrigés en §6)

**Exercice 1 — UNI → FCF → NPV.**
CapEx 1 000 000 € amorti **linéairement sur 5 ans** (VNC nulle) ; CA 900 000 €/an ; COGS 400 000 €/an ; SG&A 150 000 €/an ; **NWC 100 000 € investi en an 0 et récupéré en an 5** ; IS 25 % ; coût du capital 10 %.
→ UNI annuel ? FCF de chaque année ? NPV ? IRR ? Payback ?

**Exercice 2 — coûts pertinents.**
Une étude de faisabilité de 300 000 € a déjà été payée. Le projet utilisera un local qui pourrait être loué 200 000 €/an (an 1 à 4). IS 25 %.
→ Quel montant annuel retient-on pour le local ? Pourquoi l'étude de faisabilité est-elle exclue ?

**Exercice 3 — IRR et NPV en conflit.**
Vous encaissez **2 000 000 € immédiatement** mais devez abandonner 750 000 €/an de revenus pendant 3 ans. Coût d'opportunité 8 %.
→ IRR ? NPV ? Que dit chaque règle ? Que faites-vous ?

**Exercice 4 — IRR multiples.**
Flux : **−1 000 ; +2 500 ; −1 540**.
→ Combien d'IRR ? Lesquelles ? NPV à 0 %, 30 % et 60 % ? Faut-il accepter à r = 30 % ?

**Exercice 5 — mutuellement exclusifs.**
Projet A : −1 000 ; +500 ; +500 ; +500. Projet B : −5 000 ; +2 200 ; +2 200 ; +2 200. Coût du capital 10 %.
→ IRR de chacun ? NPV de chacun ? IRR incrémentale ? Lequel choisir ?

**Exercice 6 — profitability index.**
Budget **100 M€**. Projets : A (NPV 60, inv. 70), B (NPV 40, inv. 55), C (NPV 30, inv. 45), D (NPV 5, inv. 5).
→ Que donne le classement par PI ? Quelle est la combinaison optimale ? Le PI a-t-il fonctionné ?

**Exercice 7 — valeur terminale.**
FCF de l'an 4 = 500 k€ ; croissance attendue 2 %/an au-delà ; coût du capital 9 %.
→ Valeur terminale en an 4 ? En multiple du FCF de l'an 4 ?

**Exercice 8 — amortissement accéléré.**
CapEx 1 000 €, IS 25 %, r = 10 %. Comparer le PV du bouclier fiscal en **linéaire sur 5 ans** vs **MACRS 5 ans** (20 % / 32 % / 19,2 % / 11,52 % / 11,52 % / 5,76 %).
→ Quel est le gain de NPV et pourquoi ?

---

## 6. CORRIGÉS

**1.** EBIT = 900 000 − 400 000 − 150 000 − **200 000** = 150 000 → UNI = 112 500. NWC en fin de vie = **+100 000**.
FCF = **−1 100 000** (an 0, avec CapEx + NWC) ; **+312 500** (ans 1 à 4) ; **+412 500** (an 5).
NPV(10 %) = −1 100 000 + 312 500 × 3,16987 + 412 500 × 0,62092 = **+146 713** → **accepter**.
IRR ≈ **14,9 %** > 10 %. Payback **3,52 ans**.

**2.** Coût d'opportunité = **200 000 × (1 − 25 %) = 150 000 €/an** en an 1-4 (on retient le **manque à gagner après impôt**, car on raisonne sur l'UNI). L'étude de faisabilité est un **sunk cost** : payée quoi qu'il arrive, elle ne change pas la décision → **exclue**.

**3.** IRR ≈ **6,13 %** ; NPV(8 %) = 2 000 000 − 750 000 × 2,5771 = **+67 177**.
→ **L'IRR dit rejeter** (6,13 % < 8 %), le **NPV dit accepter**. Les bénéfices précèdent les coûts → NPV **croissante** avec r → **la règle IRR est en défaut, on suit le NPV** → **accepter** (à r = 12 % la NPV monte même à ~198 600).

**4.** Deux inversions de signe → polynôme du 2ᵈ degré en x = 1/(1+r) : **IRR = 10 % et 40 %**.
NPV(0 %) = **−40** ; NPV(30 %) = **+12** ; NPV(60 %) = **−39**. À r = 30 % (entre les deux IRR) **NPV > 0 → accepter** — illustration qu'un IRR ne suffit pas : il faut regarder **où** on se situe.

**5.** A : IRR **23,4 %**, NPV(10 %) **+243**. B : IRR **15,3 %**, NPV(10 %) **+471**.
→ B a le **plus haut NPV** malgré l'IRR le plus faible (**échelle**). IRR incrémentale (B − A) = (−4 000 ; 1 700 ×3) → **13,2 % > 10 %** → **prendre B**.

**6.** PI : D **1,000** ; A **0,857** ; B **0,727** ; C **0,667**. Le classement glouton prend **D (5)** puis **A (70)** → NPV **65**, budget 75, **25 inutilisés**.
→ **Optimum = B + C** (investissement 100, **NPV 70**) → **le PI a échoué** : la ressource résiduelle est mal exploitée et il faut comparer des **combinaisons**, pas une liste.

**7.** FCF₅ = 500 × 1,02 = **510** → `TV₄ = 510 / (0,09 − 0,02) =` **7 285,7 k€** → soit **14,57 ×** le FCF de l'an 4 (le multiple `(1+g)/(r−g)`).

**8.** Linéaire (200/an sur 5 ans) : PV du bouclier = 0,25 × 200 × 3,79079 = **189,54**.
MACRS : PV = 0,25 × (200 × 0,90909 + 320 × 0,82645 + 192 × 0,75131 + 115,2 × 0,68301 + 115,2 × 0,62092 + 57,6 × 0,56447) = **193,32**.
→ **Gain de NPV ≈ +3,8** pour 1 000 de CapEx : l'accélération **avance** les déductions dans le temps → le bouclier fiscal vaut plus parce qu'il est **actualisé moins longtemps**. Le prof a fait exactement ce raisonnement (bonus depreciation → NPV encore plus haut).

---

## 7. À ANTICIPER POUR LES STEPS 3-5 (annoncé par le prof)

- **Step 3** : coût de la dette, **coût des fonds propres (CAPM)**, **coût moyen pondéré du capital** — « c'est un rappel, on ne fait pas de gestion de portefeuille ». Chapitre 12.
- **Step 4 (7 h, le cœur)** : **Modigliani-Miller 1958** en marchés parfaits (la dette **ne** crée **pas** de valeur) → **frictions fiscales** : les **intérêts sont déductibles** donc **la dette crée de la valeur**, mais **pas trop de dette** → **capital budgeting avec levier** : le NPV d'un projet **dépend de la structure de capital**. Un des premiers réflexes de la corporate finance : **choisir le bon niveau de dette pour maximiser la valeur**. Chapitres 14, 15, 18.
- **Step 5 (optionnel)** : détresse financière, coûts d'agence, asymétrie d'information → « l'autre face de la dette » : elle crée des **obligations**, de la **tension** (**stress**) sur la trésorerie.

*Question à poser avant le midterm* : quelles pondérations exactes pour Step 1-2 au QCM du 27/10, et **où s'arrête le périmètre** (les Steps 3-5 sont-ils exclus) ?

---

*Fiche établie le 29/09/2026. Données de cours : decks Step 1/Step 2 + transcription audio `Capital budgeting.docx`. Dates d'examen issues de l'annonce orale du professeur en séance — **à reconfirmer sur YEP/K2** (l'annonce mentionnait un possible ajustement de créneau).*
