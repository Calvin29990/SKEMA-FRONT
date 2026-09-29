# COURS EXPRESS — CAPITAL BUDGETING EN 1 HEURE

### Step 1 (Cash flows) + Step 2 (Règles de décision) · Pr. Sébastien Dereeper
### 🎯 Objectif : midterm du **27/10** (30 QCM) + final du **10/11** — pas la maîtrise académique, la **réussite à l'examen**

---

## COMMENT UTILISER CE DOCUMENT

Vous avez des bases légères. Ce document repart de zéro et va droit au but : **comprendre assez pour reconnaître une question et appliquer la bonne formule.**

| Bloc | Contenu | Durée |
|---|---|---|
| **0** | Les 5 briques financières de base (si vous ne les avez pas, tout le reste s'écroule) | 10 min |
| **1** | Ce qu'on compte / ce qu'on ne compte PAS dans un projet | 10 min |
| **2** | EBIT → UNI → FCF → NPV : **le cas HomeNet en entier** | 12 min |
| **3** | Les 4 ajustements qui traînent dans les exercices | 8 min |
| **4** | Les règles de décision + **tous leurs pièges** | 12 min |
| **5** | Risque, méthode d'exercice, réflexes de QCM | 8 min |
| **Annexes** | Formulaire · Vocabulaire FR/EN · Les 12 choses à savoir par cœur | référence |

> **Si vous n'avez que 10 minutes** : lisez le Bloc 0, puis l'Annexe C, puis faites les 8 « Testez-vous ». C'est 80 % du QCM.
> **Le QCM est en anglais.** Le vocabulaire de l'Annexe B n'est pas décoratif : la moitié des erreurs en QCM sont des erreurs de traduction, pas de finance.

---
---

# BLOC 0 — LES 5 BRIQUES DE BASE (10 min)

## Brique 1 — Actualiser : 1 € demain ≠ 1 € aujourd'hui

C'est **tout** le cours. Une entreprise investit aujourd'hui pour encaisser plus tard. Comme l'argent encaissé plus tard vaut moins, on le **ramène à aujourd'hui** avant de comparer.

**Formule** — la valeur actuelle (VA / *present value*) d'un flux C reçu dans t années :

```
VA = C / (1 + r)^t
```

- `r` = le **taux d'actualisation** = le **coût du capital** = **ce que les apporteurs de fonds exigent** pour ce niveau de risque.
- `1 / (1+r)^t` = le **facteur d'actualisation**.

**Exemple** : vous recevrez 110 € dans un an, votre coût du capital est 10 %.
→ VA = 110 / 1,10 = **100 €**. Donc 110 € dans un an **=** 100 € aujourd'hui pour vous.

**Les facteurs d'actualisation à 12 %** (le taux du cours) — reconnaissez-les, ils reviennent partout :

| Année | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Facteur | 1,000 | **0,893** | **0,797** | **0,712** | **0,636** | **0,567** |

> ⚠️ **Piège de QCM** : plus le flux est **lointain**, plus le facteur est **petit** — donc un euro dans 10 ans vaut **beaucoup moins** qu'un euro dans 2 ans. Toute question qui « avance » des flux dans le temps **augmente** la valeur ; toute question qui les « repousse » la **diminue**.

## Brique 2 — La NPV : LA règle de décision

**Net Present Value** = la somme de tous les flux du projet, ramenés à aujourd'hui.

```
NPV = Σ [ FCF_t / (1+r)^t ]   puis on enlève l'investissement de départ
```

Autrement dit : **NPV = ce que le projet rapporte − ce qu'il coûte**, tout exprimé en euros d'aujourd'hui.

**Règle** : **NPV > 0 → on accepte. NPV < 0 → on refuse.**

**Pourquoi c'est LA bonne règle ?** Une NPV de +100 M€ veut dire : *ce projet rapporte 100 M€ de plus que ce que les actionnaires exigent pour le même risque.* C'est littéralement de la valeur créée. Aucune autre règle ne mesure ça aussi directement — retenez cette phrase, elle tombe en QCM (« pourquoi la NPV est-elle toujours la bonne décision ? »).

## Brique 3 — Les perpétuités (un projet qui ne s'arrête jamais)

Très fréquent dans les exercices de Berk-De Marzo.

```
Perpétuité constante   : VA = C / r
Perpétuité croissante  : VA = C₁ / (r − g)      avec g = taux de croissance, g < r
```

**Exemple 1** : un projet rapporte **35 M€ par an, pour toujours**, coûte 250 M€, r = 10 %.
→ VA = 35 / 0,10 = **350 M€** → **NPV = 350 − 250 = +100 M€** → **accepter**.

**Exemple 2** (le coffee shop du Step 2) : investissement **400**, premier flux **80**, croissance **3 %**, r = **8 %**.
→ VA = 80 / (0,08 − 0,03) = 80 / 0,05 = **1 600** → **NPV = 1 600 − 400 = +1 200**.

> ⚠️ Si `g > r`, la formule donne un résultat **négatif ou absurde** : c'est impossible à long terme. Piège classique.

## Brique 4 — Les annuités (un flux constant pendant n années)

```
VA = A × [ 1 − (1+r)^−n ] / r
```

Le crochet s'appelle le **facteur d'annuité**. À **12 % sur 4 ans** il vaut **3,03735** (donc 4 flux de 1 000 valent **3 037** aujourd'hui, pas 4 000).

C'est la formule qui sert à actualiser un FCF constant sur plusieurs années d'un coup — très utile pour aller vite.

## Brique 5 — Le TRI / IRR

**Internal Rate of Return** = le taux d'actualisation qui rend la **NPV égale à zéro**.

```
IRR = le r tel que  NPV(r) = 0
```

**Interprétation à retenir** (le prof y est revenu 3 fois en cours) : c'est **le rendement que le projet génère**.

Sur HomeNet : **NPV = 7 627** et **IRR = 27,9 %**. Traduction : *« le projet rapporte 27,9 % alors que les financeurs exigent 12 % »* → création de valeur.

**Règle** : accepter si **IRR > r** (coût du capital).
**MAIS** — et c'est le cœur du Step 2 — **cette règle a trois maladies graves** (Bloc 4). Quand IRR et NPV se contredisent : **on suit toujours la NPV**.

### ✅ TESTEZ-VOUS (Bloc 0)
1. Vous recevrez 200 dans 2 ans. r = 10 %. Combien vaut-il aujourd'hui ?
2. Un projet coûte 1 000 et rapporte 150 par an pour toujours. r = 8 %. NPV ?
3. On vous annonce « IRR = 25 %, coût du capital = 15 % ». Que concluez-vous ?

**→ Réponses :** (1) 200 / 1,10² = **165,3**. (2) 150 / 0,08 = 1 875 → NPV = **+875**. (3) Le projet rapporte 25 % pour 15 % exigés → **création de valeur, NPV positive** (mais voir les 3 pièges du Bloc 4 avant de conclure en mutuellement exclusif).

---
---

# BLOC 1 — CE QU'ON COMPTE, CE QU'ON NE COMPTE PAS (10 min)

## La règle unique : le principe incrémental

> **On ne retient QUE ce qui change du fait de la décision.**

Une entreprise, c'est un ensemble d'activités. Un nouveau projet modifie certaines lignes et pas d'autres. On ne garde que les lignes qui bougent. C'est la **incremental earnings** : la variation **attendue** du résultat **à cause** du projet.

À partir de cette seule règle, on déduit tout le tableau ci-dessous. **Ne l'apprenez pas par cœur — relisez-le comme une conséquence.**

## ✅ À INCLURE

| Élément | Pourquoi |
|---|---|
| **Coûts d'opportunité** (*opportunity cost*) | Le local est déjà à vous ? Peu importe : si vous l'utilisez, vous **renoncez** au loyer que vous auriez pu en tirer. C'est un vrai manque à gagner, donc un vrai coût. |
| **Externalités du projet / cannibalisation** | Si le nouveau produit vole des ventes à l'ancien, cette perte est **une conséquence de la décision** → on la compte. |
| **Capital expenditures (CapEx)** | Acheter une machine, c'est une vraie sortie de cash. |
| **Δ Net Working Capital** | Du cash immobilisé dans les stocks/créances. Une **augmentation** du NWC est une **sortie** de cash. |
| **Impôts** | Toujours au **taux marginal** (le taux sur le dernier euro de résultat), pas au taux moyen. |

## ❌ À EXCLURE

| Élément | Pourquoi |
|---|---|
| **Sunk costs** | Déjà payés, ou payables **quoi qu'il arrive**. Ex. **l'étude de faisabilité à 300 000 $**, la **R&D déjà dépensée**. Ils ne changent rien à la décision d'aujourd'hui. |
| **Frais généraux fixes** (*overhead*) | Le loyer du siège, la compta centrale… ils ne bougent pas parce qu'on lance le projet → non incrémentaux. Sauf la part réellement déclenchée par le projet. |
| **Interest expense** ⚠️ | **LE piège du cours.** On ne déduit **jamais** les intérêts des cash flows du projet. Raison : *« le projet doit être jugé en lui-même, pas selon son financement »*. Le financement est déjà pris en compte **dans le taux d'actualisation r**. Si on déduisait les intérêts **et** qu'on actualisait au WACC, on compterait le financement **deux fois**. |
| **Effets concurrentiels inévitables** | Si les ventes auraient baissé de toute façon (parce qu'un concurrent sort un produit de toute manière), la perte n'est **pas** causée par votre décision. |

## Les 4 situations à reconnaître instantanément en QCM

1. **« L'entreprise a déjà dépensé 300 000 $ en étude de faisabilité »** → **sunk cost, on ignore.**
2. **« Le projet utilisera un local qu'on aurait pu louer 200 000 $/an »** → **coût d'opportunité, on compte**… mais **net d'impôt** ! Si le taux d'IS est 25 % : on retient **200 000 × (1 − 0,25) = 150 000 $/an**. Pourquoi ? Parce qu'on travaille sur le résultat **après impôt** : le loyer encaissé aurait été imposé, donc le manque à gagner réel est de 150 000.
3. **« 25 % des ventes du nouveau produit viennent de clients qui auraient acheté l'ancien »** → **cannibalisation, on compte.**
4. **« Il faudra rembourser l'emprunt à 6 % »** → **interest expense, on ignore.**

### ✅ TESTEZ-VOUS (Bloc 1)
Une société a payé 500 k€ d'études, va utiliser un terrain qui rapporte 80 k€/an de loyer (IS 30 %), et devra rembourser un emprunt de 2 M€ à 5 %. Quels montants entre dans l'analyse ?

**→ Réponse :** **seulement 80 × (1 − 0,30) = 56 k€/an** de coût d'opportunité. Les 500 k€ (sunk) et les 5 % d'intérêts (dans le taux d'actualisation) sont **exclus**.

---
---

# BLOC 2 — DE L'EBIT AU CASH FLOW : LE CAS HOMENET EN ENTIER (12 min)

C'est **l'exercice type** du midterm. Une fois celui-là compris, vous savez tout faire.

## Le contexte (Linksys / produit HomeNet)

- Durée de vie du produit : **4 ans**.
- Prix de vente : **260 $/unité**. Coût de production : **110 $/unité**. Ventes : **100 000 unités/an**.
- **R&D upfront** : 15 000 000 $. **Équipement** : 7 500 000 $, amorti **linéairement sur 5 ans**.
- **Overhead annuel** : 2 800 000 $. **Taux d'impôt : 20 %**.
- Coût du capital (= taux d'actualisation) : **12 %**.
- Étude de faisabilité : 300 000 $ → **déjà payée, exclue**.
- Tous les chiffres sont en **milliers de $** (« $000s »).

## ÉTAPE A — Le compte de résultat incrémental (la version simple)

| Ligne ($000s) | An 0 | An 1 | An 2 | An 3 | An 4 | An 5 |
|---|---|---|---|---|---|---|
| 1. **Sales** (100 000 × 260) | | 26 000 | 26 000 | 26 000 | 26 000 | |
| 2. **Cost of Goods Sold** (100 000 × 110) | | (11 000) | (11 000) | (11 000) | (11 000) | |
| 3. **Gross Profit** | | 15 000 | 15 000 | 15 000 | 15 000 | |
| 4. **SG&A** (overhead) | | (2 800) | (2 800) | (2 800) | (2 800) | |
| 5. **R&D** | (15 000) | | | | | |
| 6. **Depreciation** (7 500 / 5) | | (1 500) | (1 500) | (1 500) | (1 500) | (1 500) |
| 7. **= EBIT** | **(15 000)** | 10 700 | 10 700 | 10 700 | 10 700 | **(1 500)** |
| 8. **Income Tax @20 %** | 3 000 | (2 140) | (2 140) | (2 140) | (2 140) | 300 |
| 9. **= Unlevered Net Income** | **(12 000)** | 8 560 | 8 560 | 8 560 | 8 560 | **(1 200)** |

### Les 4 choses à comprendre dans ce tableau

**① Aucune ligne d'intérêts.** C'est exactement la règle du Bloc 1 : *unlevered* veut dire **« sans dette »**. On juge le projet comme s'il était financé uniquement par fonds propres.

**② L'an 0 est négatif, et ça donne un IMPÔT POSITIF.** EBIT = −15 000 → l'impôt à 20 % vaut **+3 000**. Traduction : **un impôt négatif = un crédit d'impôt**. Quand une entreprise perd de l'argent sur un projet, elle paie **moins** d'impôt sur le reste de ses activités. **Ne mettez jamais 0 : mettez le signe opposé.**

**③ Pourquoi le projet a 5 ans alors qu'il vend pendant 4 ans ?** Parce que l'équipement s'amortit sur **5 ans**. L'an 5 n'a aucune vente, mais porte encore une **charge d'amortissement** (non-cash) qui génère elle aussi un crédit d'impôt : EBIT = −1 500 → impôt +300 → UNI = **−1 200**. C'est une question de QCM quasi certaine.

**④ La formule de l'UNI :**
```
Unlevered Net Income = EBIT × (1 − τ)          τ = taux d'impôt
```
Vérification an 1 : 10 700 × (1 − 0,20) = 10 700 × 0,80 = **8 560** ✔

## ÉTAPE B — L'ajustement cannibalisation

Dans le cours, on raffine : **25 % des ventes de HomeNet viennent de clients qui auraient acheté le routeur existant de Linksys** à 100 $, dont le coût est 60 $.

| Effet | Calcul | Impact |
|---|---|---|
| CA perdu (25 000 unités × 100 $) | | **−2 500** |
| Coût de production économisé (25 000 × 60 $) | | **+1 500** |
| **= perte de marge brute** | | **−1 000** |
| + hausse du SG&A (support) | | **−200** |
| **= perte d'EBIT** | | **−1 200** |
| **= perte d'UNI après impôt** | −1 200 × 0,80 | **−960** |

Le nouvel UNI annuel devient **9 500 × 0,80 = 7 600** (au lieu de 8 560).

> ⚠️ **Le tableau de FCF qui suit est construit sur cette version AVEC cannibalisation (UNI = 7 600).** Si vous oubliez la cannibalisation, vous trouverez une NPV trop élevée. C'est le genre d'erreur qui fait perdre 2-3 points.

## ÉTAPE C — Du résultat au cash-flow : LE TABLEAU PIVOT ⭐

**Le tableau le plus important du cours.** Il faut pouvoir le reconstruire de mémoire.

| ($000s) | An 0 | An 1 | An 2 | An 3 | An 4 | An 5 |
|---|---|---|---|---|---|---|
| **Unlevered Net Income** | (12 000) | 7 600 | 7 600 | 7 600 | 7 600 | (1 200) |
| **+ Depreciation** | — | 1 500 | 1 500 | 1 500 | 1 500 | 1 500 |
| **− Capital Expenditures** | (7 500) | — | — | — | — | — |
| **− Δ Net Working Capital** | — | (2 100) | — | — | — | **+2 100** |
| **= FREE CASH FLOW** | **(19 500)** | **7 000** | **9 100** | **9 100** | **9 100** | **2 400** |

### La formule pivot

```
FCF = Unlevered Net Income + Amortissement − CapEx − ΔNWC
```

### Pourquoi chaque ligne ?

**+ Amortissement** —— L'amortissement est une **charge non-cash**. On ne paie personne quand on « amortit ». Pourtant on l'a déduit pour calculer l'impôt (et c'est utile, ça réduit l'impôt) : il faut donc le **rajouter** pour retrouver le cash réel.
→ Son seul effet sur la valeur passe par l'impôt : c'est le **bouclier fiscal** (voir Étape E).

**− CapEx** —— L'achat de la machine (7 500) est une **vraie sortie de cash en an 0**. On ne l'a jamais mise dans l'EBIT (on a mis l'amortissement à la place) : il faut donc la mettre ici. Sinon elle n'apparaîtrait nulle part.

**− ΔNWC (Net Working Capital)** —— Le NWC, c'est l'argent **immobilisé** dans l'activité :

| ($000s) | An 1 |
|---|---|
| Receivables = 15 % du CA | 3 525 |
| Payables = 15 % des COGS | (1 425) |
| **= Net Working Capital** | **2 100** |

Concrètement : vous vendez à crédit → vos clients vous doivent de l'argent (créances) → **du cash qui n'est pas encore rentré**. En contrepartie vos fournisseurs vous font crédit (dettes fournisseurs) → **du cash que vous n'avez pas encore sorti**. Le solde **2 100** est immobilisé.
- En **an 1** : on l'investit → **sortie** de 2 100.
- De l'an 2 à 4 : le NWC ne change pas → aucun flux.
- En **an 5** : le projet s'arrête, on récupère tout → **entrée** de 2 100.

> La différence créances/dettes fournisseurs s'appelle le **trade credit**. Une **augmentation** du NWC est toujours une **sortie** de trésorerie.

**Vérification de chaque ligne** (à savoir refaire) :
- An 0 : −12 000 + 0 − 7 500 − 0 = **−19 500** ✔
- An 1 : 7 600 + 1 500 − 2 100 = **7 000** ✔
- An 2-4 : 7 600 + 1 500 = **9 100** ✔
- An 5 : −1 200 + 1 500 + 2 100 = **2 400** ✔

## ÉTAPE D — Actualiser : la NPV et l'IRR

| ($000s) | An 0 | An 1 | An 2 | An 3 | An 4 | An 5 |
|---|---|---|---|---|---|---|
| Free Cash Flow | (19 500) | 7 000 | 9 100 | 9 100 | 9 100 | 2 400 |
| Facteur @12 % | 1,000 | 0,893 | 0,797 | 0,712 | 0,636 | 0,567 |
| **PV** | (19 500) | 6 250 | 7 254 | 6 477 | 5 783 | 1 362 |
| **NPV** | **+7 627** | | | | | |
| **IRR** | **27,9 %** | | | | | |

**Lecture** : le projet crée **7 627 k$ ≈ 7,6 M$** de valeur, et il rapporte **27,9 %** alors que les financeurs exigent **12 %**. → **NPV > 0, on accepte.**

## ÉTAPE E — Le bouclier fiscal (depreciation tax shield)

**L'amortissement n'a aucune valeur en lui-même — sa valeur vient de l'impôt qu'il économise.**

```
Bouclier fiscal annuel = τ × Amortissement
```
HomeNet : 20 % × 1 500 = **300 $ (000s) d'impôt économisé chaque année pendant 5 ans.**

> C'est **le** fil rouge vers le Step 4 : le prof a annoncé que la dette crée de la valeur **parce que les intérêts sont déductibles** — exactement le même mécanisme. Si vous avez compris le bouclier fiscal de l'amortissement, vous avez compris 80 % du Step 4.

### ✅ TESTEZ-VOUS (Bloc 2) — l'exercice le plus rentable
Un projet : CA **500 000**/an, COGS **200 000**/an, SG&A **50 000**/an, machine de **900 000** amortie **linéairement sur 3 ans**, **NWC de 60 000** investi en an 0 et récupéré en an 3, impôt **25 %**, r = **10 %**. Donnez l'UNI, le FCF de chaque année, la NPV.

**→ Corrigé :** Amortissement = 900 000 / 3 = **300 000**. EBIT = 500 000 − 200 000 − 50 000 − 300 000 = **−50 000** → UNI = −50 000 × 0,75 = **−37 500** (crédit d'impôt, l'entreprise paie 12 500 d'impôt **en moins** ailleurs).
FCF : **an 0 = −960 000** (−900 000 − 60 000) ; **ans 1-2 = 262 500** (−37 500 + 300 000) ; **an 3 = 322 500** (+ 60 000 récupérés).
NPV = −960 000 + 262 500/1,10 + 262 500/1,21 + 322 500/1,331 = −960 000 + 238 636 + 216 942 + 242 299 = **−262 122 → projet à rejeter**.
(Leçon : ici l'amortissement **améliore** la situation — il économise 0,25 × 300 000 = **75 000 d'impôt par an**. Sans lui, la perte serait bien plus lourde. C'est la preuve que **l'amortissement crée de la valeur par l'impôt**.)

---
---

# BLOC 3 — LES 4 AJUSTEMENTS QUI TRAÎNENT DANS LES EXERCICES (8 min)

## ① Amortissement accéléré (MACRS)

Aux États-Unis, le fisc autorise le **MACRS** (*Modified Accelerated Cost Recovery System*) : on déduit **plus au début**, moins à la fin.

| Barème MACRS 5 ans | An 1 | An 2 | An 3 | An 4 | An 5 | An 6 |
|---|---|---|---|---|---|---|
| % du coût amorti | 20 % | 32 % | 19,2 % | 11,52 % | 11,52 % | 5,76 % |

**Pourquoi ça augmente la NPV ?** Le bouclier fiscal est **le même au total** (τ × coût de l'actif), mais il arrive **plus tôt** → il est actualisé **moins longtemps** → il vaut **plus cher**.

**Chiffre à retenir** : sur 1 000 de CapEx, τ = 25 %, r = 10 %
- Linéaire 5 ans : PV du bouclier = **189,5**
- MACRS 5 ans : PV du bouclier = **193,3** → **gain ≈ +3,8 de NPV**

**Corollaire — la *bonus depreciation*** : déduire 100 % dès l'an 0 augmente encore la NPV. **Règle générale : plus l'amortissement est accéléré, plus la NPV est élevée.** (Question de QCM déjà vue : *« pourquoi une entreprise préfère-t-elle le barème le plus accéléré ? »*)

## ② Valeur de cession (*salvage / liquidation value*)

**La règle d'or : raisonner en NET D'IMPÔT.**

```
Flux après impôt sur une cession = Prix de vente − τ × (Prix de vente − Valeur comptable)
```

**Cas type (HomeNet Ex. 5)** : un équipement transféré d'une autre usine, **valeur de revente 2 000**, **valeur comptable 1 000**, τ = 20 %.

| Moment | Raisonnement | Flux |
|---|---|---|
| **An 0** | On renonce à vendre 2 000. Mais si on avait vendu, on aurait payé 20 % × (2 000 − 1 000) = 200 d'impôt. Le vrai manque à gagner est donc **net d'impôt**. | **−1 800** |
| **An 1** | La VNC restante (1 000) devient amortissable → bouclier fiscal | **+200** |
| **An 5** | Revente à 800, actif **totalement amorti** (VNC = 0) → **tout** est imposable | 800 × 0,80 = **+640** |

Nouveau FCF : **(21 300) / 7 200 / 9 100 / 9 100 / 9 100 / 3 040** → **NPV = 6 368** (au lieu de 7 627).
→ **Ne jamais oublier l'impôt : c'est la source d'erreur n°1 de cet ajustement.**

## ③ Valeur terminale / de continuation

À la fin du projet, l'affaire ne « disparaît » pas : on la **vend**. Sa valeur = les cash flows **de toutes les dates futures**, ramenés à la date de fin.

```
Valeur terminale en T = FCF_(T+1) / (r − g)          (= perpétuité croissante)
```

**Cas type (Base Hardware)** : FCF de l'an 4 = **1 300**, croissance ensuite **g = 5 %**, r = **10 %**.

```
TV₄ = 1 300 × 1,05 / (0,10 − 0,05) = 1 365 / 0,05 = 27 300
```
→ soit **21 ×** le FCF de l'an 4 (le multiple `(1+g)/(r−g) = 1,05/0,05 = 21`).
On remplace le flux de l'an 4 par **1 300 + 27 300 = 28 600**, puis on actualise : **NPV ≈ 5 597**.

> ⚠️ Le prof a beaucoup insisté : **« la valeur terminale est le point où on peut faire n'importe quoi »** — elle dépend entièrement de `g` et de `r`. Son exemple de l'appartement : 40 m² à 200 000 €, loué 1 000 €/mois, revendu dans 20 ans → **tout** le rendement dépend de l'hypothèse de revente. Retenez la définition : **valeur de marché des FCF de toutes les dates futures**.

## ④ Reports fiscaux (*tax loss carryforwards*)

Une entreprise qui perd de l'argent aujourd'hui ne récupère pas tout de suite le crédit d'impôt : elle le **reporte** sur ses bénéfices futurs.

**Cas Verian Industries** : perte de **140 M$**, bénéfices futurs **50 M$/an**.
**Règle US à connaître** : on ne peut absorber que **80 %** du résultat imposable de l'année → 80 % × 50 = **40 par an**.

| | An 0 | An 1 | An 2 | An 3 | An 4 | An 5 |
|---|---|---|---|---|---|---|
| Résultat avant impôt | (140) | 50 | 50 | 50 | 50 | 50 |
| Report utilisé | | (40) | (40) | (40) | (20) | — |
| **Résultat imposable** | | **10** | **10** | **10** | **30** | **50** |

**Conséquence économique** : l'impôt sur une partie du résultat courant est **repoussé dans le temps** → sa valeur actuelle **baisse**. En pratique, certaines entreprises approximent en utilisant un **taux d'impôt marginal plus faible**.

*(Analogie du prof : la rénovation d'un appartement — le déficit de la 1ʳᵉ année se reporte sur les loyers positifs des années suivantes.)*

### ✅ TESTEZ-VOUS (Bloc 3)
Machine de 600 000 amortie sur 4 ans en linéaire vs MACRS 5 ans (20/32/19,2/11,52/11,52/5,76 %). τ = 30 %, r = 8 %. Quelle méthode donne la NPV la plus haute et pourquoi ?

**→ Réponse :** **MACRS**. À taux et coût identiques, le **total** du bouclier fiscal est le même, mais il est encaissé **plus tôt** → actualisé moins longtemps → **valeur actuelle plus élevée**.

---
---

# BLOC 4 — LES RÈGLES DE DÉCISION ET TOUS LEURS PIÈGES (12 min)

*vous devriez maintenant lire cette partie beaucoup plus vite et plus sereinement*

## 4.1 La règle NPV (projet isolé / *stand-alone*)

**La règle** : NPV > 0 → accepter. NPV < 0 → refuser.
**Le principe fondamental** : *si une autre règle contredit la NPV, on suit la NPV*. À écrire tel quel en QCM.

## 4.2 La règle de l'IRR et ses **TROIS PIÈGES**

**La règle** : accepter si **IRR > coût du capital**.
Elle fonctionne… **à une condition** : que **tous les flux négatifs précèdent les flux positifs** (une seule inversion de signe dans la série).

Dès que cette condition est violée, ça casse. Les trois cas d'école du prof — **le cas « Star l'écrivain »** :

| | Les flux | Ce qui se passe | Verdict |
|---|---|---|---|
| **Piège 1 — Delayed investment** (les bénéfices viennent **avant** les coûts) | **+1 000 000** aujourd'hui, puis **−500 000/an pendant 3 ans** | **IRR = 23,38 %** > 10 % → la règle IRR dit **accepter**. Mais **NPV = −243 426** → il faut **refuser** | Quand les bénéfices précèdent les coûts, la NPV est une fonction **croissante** du taux : IRR et NPV **divergent** → **suivre la NPV** |
| **Piège 2 — Multiple IRRs** | +550 000 aujourd'hui, −500 000 × 3, **+1 000 000 en an 4** | **Deux IRR : 7,164 % et 33,673 %**. Entre les deux, la NPV est **négative** | L'IRR n'est pas unique → **règle inapplicable**. À r = 10 % → **refuser** |
| **Piège 3 — Nonexistent IRR** | +750 000 aujourd'hui, −500 000 × 3, +1 000 000 en an 4 | **Aucun taux n'annule la NPV** (elle est positive partout) | **Règle inapplicable** → accepter (car NPV > 0) |

**Le signal d'alerte à repérer dans l'énoncé** : comptez les **changements de signe**.
- Un seul changement de signe (−, +, +, +) → IRR fiable.
- Plusieurs changements (−, +, −) → **méfiance, IRR multiples possibles**.
- Les + d'abord puis les − → **méfiance, delayed investment**.

> ⚠️ **Erreur fréquente** : ne confondez pas **l'IRR** (le chiffre) et **la règle IRR** (le critère de décision). L'IRR **reste utile** : il mesure le **rendement moyen** du projet et la **sensibilité de la NPV à une erreur d'estimation du coût du capital**. C'est **le critère** qui est défaillant, pas l'indicateur.

## 4.3 La règle du Payback

**Payback period** = le temps qu'il faut pour **récupérer l'investissement de départ**.
**La règle** : accepter si le payback < un seuil fixé.

**Exemple Fredrick's** : investissement **250**, flux **35/an**, seuil **5 ans**.
35 × 5 = 175 < 250 → **refus**. En réalité il faut **8 ans** pour rembourser (7 × 35 = 245 < 250).

**Les 3 défauts (à savoir citer)** :
1. **Ignore le coût du capital et la valeur temps de l'argent.**
2. **Ignore tous les cash flows après la période de récupération** (un projet qui rapporte énormément en années 6-10 mais lentement au début sera injustement rejeté).
3. **Repose sur un seuil arbitraire** (*ad hoc*).

Pourquoi est-elle si utilisée ? **La simplicité.** (C'est la réponse attendue.)

## 4.4 Choisir entre projets **mutuellement exclusifs**

**Mutuellement exclusifs** = on ne peut en prendre qu'**un seul** (ex. un seul local disponible).

- **NPV** : prendre le **NPV le plus élevé**. ✅ Toujours correct.
- **IRR** : prendre le **plus haut IRR**. ❌ **Peut mener à une erreur.**

**Le contre-exemple du cours** (le local commercial, perpétuités croissantes) :

| Projet | Investissement | Flux an 1 | Croissance | Coût du capital | **IRR** | **NPV** |
|---|---|---|---|---|---|---|
| Librairie | 300 000 | 63 000 | 3 % | 8 % | **24 %** | 960 000 |
| **☕ Coffee shop** | 400 000 | 80 000 | 3 % | 8 % | 23 % | **1 200 000** ✅ |
| Magasin de musique | 400 000 | 104 000 | 0 % | 8 % | 26 % | 900 000 |
| Magasin d'électronique | 400 000 | 100 000 | 3 % | **11 %** | 28 % | 850 000 |

**Le coffee shop a le MEILLEUR NPV mais PAS le meilleur IRR.** La règle IRR choisirait la librairie (24 %), l'électronique (28 %) ou la musique (26 %) — **toutes de mauvais choix**.

**Les 4 raisons pour lesquelles l'IRR échoue en mutuellement exclusif** :
1. **Différence d'échelle** — doubler la taille d'un projet **double la NPV** mais **pas l'IRR**. Un petit projet à fort IRR peut générer peu de valeur.
2. **Timing des cash flows** — un rendement vaut d'autant plus qu'il est **gagné longtemps**. Le magasin de musique a un IRR de 26 % mais `g = 0` → sa valeur plafonne.
3. **Différence de risque** — un IRR attractif pour un projet **sûr** ne l'est pas pour un projet **risqué**. L'électronique a le meilleur IRR (28 %) mais le pire NPV, parce que son coût du capital est 11 %.
4. **Conséquence** : on **ne peut pas comparer** des IRR de projets de tailles différentes.

## 4.5 L'**incremental IRR** — la bonne façon d'utiliser l'IRR

**L'idée** : au lieu de comparer deux IRR, on applique la règle de l'IRR **à la différence des cash flows** entre les deux projets.

**Le cas des révisions d'usine** (en M$) :

| | An 0 | An 1 | An 2 | An 3 | **IRR** |
|---|---|---|---|---|---|
| Révision **mineure** | (10) | 6 | 6 | 6 | **36,3 %** |
| Révision **majeure** | (50) | 25 | 25 | 25 | **23,4 %** |
| **Incrément (majeure − mineure)** | **(40)** | **19** | **19** | **19** | **20,0 %** |

Coût du capital = **12 %**.
→ L'IRR incrémentale (**20 %**) **dépasse** le coût du capital (**12 %**) → **passer à la majeure est attractif** : la taille plus grande compense le rendement en % plus faible.
Vérification par les NPV à 12 % : majeure ≈ **10,05** > mineure ≈ **4,41** ✔

> **À retenir absolument** : l'IRR incrémentale est **le taux de croisement (*crossover rate*) des profils de NPV** — le taux auquel le meilleur choix s'inverse.

**Les 4 limites de l'IRR incrémentale** :
1. Elle **peut ne pas exister**.
2. Il peut y en avoir **plusieurs**.
3. Le fait que l'IRR dépasse le coût du capital **pour les deux projets** n'implique pas que **l'un des deux** ait une NPV positive.
4. Si les deux projets ont des **coûts du capital différents**, on ne sait pas **à quoi** comparer l'IRR incrémentale.

## 4.6 Profitability Index et contraintes de ressources

Quand on a **un budget limité**, on ne peut pas tout prendre : il faut classer.

```
Profitability Index (PI) = NPV / Investissement
```
(ou NPV par unité de ressource rare — ingénieurs, mètres carrés, etc.)

**Exemple 1** — budget 100 M$, 3 projets :

| Projet | NPV | Investissement | **PI** |
|---|---|---|---|
| 1 | 110 | 100 | 1,10 |
| 2 | **70** | 50 | **1,40** |
| 3 | **60** | 50 | **1,20** |

→ On prend **2 + 3 ensemble** (NPV total 130, investissement 100) et on **renonce à 1** (NPV seule : 110).
**Le PI identifie la meilleure COMBINAISON, pas le meilleur projet.**

**Exemple 2 — NetIt** (contrainte = 190 ingénieurs, on classe par PI = NPV / effectif) :

| Rang | Projet | NPV (M$) | ETP | PI | ETP cumulés |
|---|---|---|---|---|---|
| 1 | A | 22,7 | 47 | 0,483 | 47 |
| 2 | F | 12,9 | 32 | 0,403 | 79 |
| 3 | E | 20,6 | 58 | 0,355 | 137 |
| 4 | **Router** | 17,7 | 50 | **0,354** | **187** |
| 5 | C | 14,0 | 40 | 0,350 | *(dépassement)* |
| 6 | D | 11,5 | 61 | 0,189 | |
| 7 | B | 8,1 | 44 | 0,184 | |

→ **Retenir A, F, E, Router** (187 ETP sur 190). On renonce à **C, D et B**, soit **33,6 M$ de NPV abandonnée**.

**Les 2 limites du PI** :
1. **Ressource résiduelle mal gérée** : un petit projet de NPV 120 k$ nécessitant 3 ingénieurs a un PI = 0,04 → classé **dernier**. Mais **3 ingénieurs restent inutilisés** après les 4 premiers projets → il **faut le prendre quand même**. Le classement par PI échoue quand on ne peut pas utiliser la ressource exactement.
2. **Contraintes multiples** (budget **et** effectif **et** machines) : **le PI s'effondre complètement** → il faut de l'optimisation combinatoire.

### ✅ TESTEZ-VOUS (Bloc 4)
Budget **100**. Projets : A (NPV 80, coût 80), B (NPV 45, coût 50), C (NPV 40, coût 45).
Que donne le classement par PI ? Quelle est la combinaison réellement optimale ?

**→ Réponse :** PI : **A = 1,000**, B = 0,900, C = 0,889.
Classement glouton → on prend **A** (coût 80)… et il **reste 20 inutilisés** : ni B ni C ne rentrent. NPV = **80**.
Or **B + C** coûte 95 (≤ 100) et rapporte **45 + 40 = 85** → **NPV supérieure**.
➡️ **Le PI a échoué** : exactement le cas d'école de la **ressource résiduelle** mal exploitée (§4.6, limite n°1). C'est le piège que le prof a mis en avant avec le petit projet à 120 000 $ et 3 ingénieurs.

---
---

# BLOC 5 — RISQUE, MÉTHODE D'EXERCICE, RÉFLEXES QCM (8 min)

## 5.1 Analyser un projet

**Break-even** = **le niveau d'un paramètre qui annule la NPV** du projet.

| Paramètre HomeNet | Seuil |
|---|---|
| Unités vendues | **77 121 unités/an** |
| Prix de gros | **228 $/unité** |
| Coût des biens vendus | **142 $/unité** |
| Coût du capital | **27,9 %** (= l'IRR, forcément) |

**EBIT break-even of sales** = le niveau de ventes où **EBIT = 0**.

**Sensitivity analysis** vs **Scenario analysis** — LA question de QCM piège :

| | Sensitivity analysis | Scenario analysis |
|---|---|---|
| Ce qu'on fait | On change **UN SEUL** paramètre, les autres restent constants | On change **PLUSIEURS paramètres SIMULTANÉMENT** |
| Exemple | « et si le SG&A montait de 1 M$ ? » | « et si on baissait le prix **et** qu'on vendait plus ? » (3 stratégies de prix : 260/100k → NPV 7 627 ; 245/110k → 7 032 ; 275/90k → 7 509) |
| Sur les statistiques | — | Si on connaît les **probabilités** de chaque scénario → **Expected NPV** = moyenne pondérée |

**Exemple chiffré de sensibilité** (HomeNet 6) : SG&A monterait à 3,8 M$ au lieu de 2,8 M$ (+1 M$).
→ Le FCF baisse de **800**/an après impôt (1 000 × 0,80). Sur 4 ans à 12 % : 800 × 3,03735 = **2 430**.
→ **NPV tombe de 7 627 à 5 197.**

## 5.2 La méthode en 6 étapes pour TOUT exercice chiffré

Apprenez cette séquence et appliquez-la mécaniquement, sans réfléchir :

```
1. LISTER les données et repérer ce qui est EXCLU
   → y a-t-il une étude déjà payée (sunk) ? un local possédé (opportunité) ?
     des intérêts (à ignorer) ? une cannibalisation ?

2. CALCULER l'EBIT de chaque année
   → CA − COGS − SG&A − R&D − Amortissement

3. CONVERTIR en UNI
   → EBIT × (1 − τ)      ⚠️ si EBIT négatif, l'impôt est POSITIF (crédit d'impôt)

4. PASSER au FCF
   → UNI + Amortissement − CapEx − ΔNWC
   ⚠️ le NWC est récupéré en DERNIÈRE année
   ⚠️ ne pas oublier l'an 5 (amortissement seul, s'il existe)

5. ACTUALISER
   → Σ FCF_t / (1+r)^t     puis NPV = total
   → NPV > 0 ? alors accepté

6. CALCULER l'IRR si demandé
   → et COMPARER au coût du capital
```

**Les 3 oublis qui coûtent le plus de points** : ① oublier de récupérer le NWC en fin de projet, ② oublier que l'impôt sur un EBIT négatif est positif, ③ oublier l'ajustement d'impôt sur la valeur de cession.

## 5.3 Les réflexes de QCM (30 secondes par question)

Le QCM ne demande pas de calculer : il demande de **reconnaître**. Voici les 20 réflexes :

| # | Affirmation | ✅/❌ | # | Affirmation | ✅/❌ |
|---|---|---|---|---|---|
| 1 | Une étude de faisabilité déjà payée s'inclut | ❌ sunk | 11 | Un projet peut avoir deux IRR | ✅ |
| 2 | Les intérêts se déduisent des FCF du projet | ❌ | 12 | IRR > r garantit NPV > 0 | ❌ (pièges 1-3) |
| 3 | Le loyer auquel on renonce est un cash flow | ✅ | 13 | Un projet sans IRR doit être rejeté | ❌ |
| 4 | Amortir plus vite réduit la NPV | ❌ l'inverse | 14 | Le payback tient compte de l'après-payback | ❌ |
| 5 | Une hausse du NWC est une sortie de cash | ✅ | 15 | En exclusif, plus haut IRR = meilleur choix | ❌ |
| 6 | Le NWC est récupéré en fin de projet | ✅ | 16 | L'IRR incrémentale se compare au coût du capital | ✅ |
| 7 | La NPV du projet dépend de son financement | ❌ | 17 | Le PI suffit sous contrainte de ressources | ❌ |
| 8 | Une charge non-cash n'a aucun effet sur la NPV | ❌ (impôt) | 18 | Un actif totalement amorti est vendu hors impôt | ❌ |
| 9 | Si IRR et NPV s'opposent, on suit l'IRR | ❌ | 19 | TV = valeur de marché des FCF futurs | ✅ |
| 10 | La règle IRR marche si − avant + | ✅ | 20 | Sensitivity = changer plusieurs paramètres | ❌ (= scénarios) |

## 5.4 Le piège méta du midterm

Le prof a fait en cours un **« wake up »** sur : *« que représente le 27,9 % ? »*. Traduction : **il ne suffira pas de recalculer, il faudra INTERPRÉTER.**

Entraînez-vous à dire à voix haute, pour chaque chiffre :
- **NPV = 7 627** → « le projet crée 7,6 M$ de valeur au-delà de ce qu'exigent les apporteurs de fonds à 12 % »
- **IRR = 27,9 %** → « le projet rapporte 27,9 % alors que le coût du capital est 12 % »
- **Bouclier fiscal = 300/an** → « l'amortissement réduit l'impôt de 300 par an »
- **NWC = 2 100** → « l'activité immobilise 2 100 de trésorerie, récupérés à l'arrêt du projet »
- **Valeur terminale = 27 300** → « la valeur de marché de tous les flux après l'an 4, sous hypothèse de croissance de 5 % à perpétuité »

---
---

# ANNEXE A — FORMULAIRE À SAVOIR ÉCRIRE DE MÉMOIRE

```
Unlevered Net Income   = EBIT × (1 − τ)
FREE CASH FLOW         = UNI + Amortissement − CapEx − ΔNWC
Bouclier fiscal        = τ × Amortissement
NPV                    = Σ FCF_t / (1+r)^t        → accepter si > 0
IRR                    = le r tel que NPV(r) = 0  → accepter si > r
Payback                = temps de récupération de I₀
Profitability Index    = NPV / Investissement
Perpétuité constante   = C / r
Perpétuité croissante  = C₁ / (r − g)             avec g < r
Valeur terminale       = FCF_(T+1) / (r − g)
Annuité (VA)           = A × [1 − (1+r)^−n] / r
Cession après impôt    = Prix − τ × (Prix − Valeur comptable)
```

# ANNEXE B — VOCABULAIRE FR / EN (le QCM est en anglais)

| English | Français | English | Français |
|---|---|---|---|
| Capital budgeting | Choix d'investissement | Payback period | Délai de récupération |
| Incremental earnings | Résultat incrémental | Profitability index | Indice de profitabilité |
| Unlevered net income | Résultat net sans dette | Mutually exclusive projects | Projets mutuellement exclusifs |
| Free cash flow (FCF) | Flux de trésorerie disponible | Incremental IRR | TRI incrémental / différentiel |
| Net working capital (NWC) | Besoin en fonds de roulement | Crossover rate | Taux de croisement |
| Trade credit | Crédit interentreprises | Stand-alone project | Projet isolé |
| Opportunity cost | Coût d'opportunité | Cost of capital / WACC | Coût du capital / CMPC |
| Sunk cost | Coût irrécupérable | Discount rate / factor | Taux / facteur d'actualisation |
| Cannibalization | Cannibalisation | Capital expenditures (CapEx) | Investissements |
| Depreciation tax shield | Économie d'impôt sur amortissement | Salvage / liquidation value | Valeur de cession |
| Straight-line depreciation | Amortissement linéaire | Book value | Valeur comptable |
| MACRS | Amortissement accéléré fiscal | Terminal / continuation value | Valeur terminale |
| Tax loss carryforward | Report en avant des déficits | Break-even analysis | Analyse du point mort |
| Sensitivity analysis | Analyse de sensibilité | Scenario analysis | Analyse de scénarios |
| Overhead | Frais généraux | Tax rate | Taux d'imposition |
| Resource constraint | Contrainte de ressources | Expected NPV | NPV espérée |

# ANNEXE C — LES 12 CHOSES À SAVOIR PAR CŒUR (si vous ne retenez que ça)

1. **NPV > 0 → accepter.** Si une autre règle la contredit, **c'est la NPV qui gagne**.
2. **FCF = UNI + Amortissement − CapEx − ΔNWC.**
3. **UNI = EBIT × (1 − τ).** EBIT négatif → **impôt POSITIF (crédit d'impôt)**.
4. **Sunk costs → exclure. Coûts d'opportunité → inclure. Intérêts → exclure.**
5. Le **NWC est récupéré** la dernière année du projet.
6. **L'amortissement crée de la valeur uniquement par l'impôt** : bouclier = τ × amortissement. **Plus il est accéléré, plus la NPV est haute.**
7. **Cession d'actif : toujours nette d'impôt** = Prix − τ × (Prix − VNC).
8. **Valeur terminale = FCF_(T+1) / (r − g)** = valeur de marché de tous les flux futurs.
9. **La règle IRR casse** si : les + précèdent les −, ou plusieurs inversions de signe (IRR multiples/inexistantes).
10. **Mutuellement exclusif → NPV, jamais l'IRR** (échelle, timing, risque).
11. **Le payback** ignore la valeur temps et l'après-payback, seuil arbitraire.
12. **Sensitivity = 1 paramètre. Scenario = plusieurs.**

---
---

# ET MAINTENANT ?

Les **annotations de cours ne suffisent pas** : il faut de la **répétition active**. On va s'entraîner en 3 paliers :

**Palier 1 — QCM blanc (30 questions, 45 min, conditions réelles)**
Je vous génère 30 QCM au format exact du midterm (English, 1 bonne réponse, pas de pénalité), chronométré. → *dites-moi « go QCM »*

**Palier 2 — Exercices chiffrés (format final)**
Des cas type HomeNet de difficulté croissante : FCF + NPV + IRR, puis avec amortissement accéléré, valeur de cession, valeur terminale, report fiscal, puis mutuellement exclusifs + IRR incrémentale + PI. → *« go exos »*

**Palier 3 — Les questions de cours du final**
Les questions ouvertes type *« pourquoi la NPV est-elle toujours la bonne règle ? »*, *« pourquoi la règle IRR peut-elle échouer ? »* — avec des réponses modèles courtes à mémoriser. → *« go cours »*

> **Règle de travail** : une session = **un palier**, pas plus. On corrige, on note les erreurs, on refait les mêmes dans 48 h. C'est ça qui fait monter la note — pas de relire ce document 10 fois.

---

*Fiche d'accompagnement complète (détails, tableaux intégraux du cours, 8 exercices corrigés) : `FICHE-EXAM-CAPITAL-BUDGETING.md`. Établi le 29/09/2026 — Step 1 + Step 2, sources : decks du prof + transcription audio du cours du 28/09.*
