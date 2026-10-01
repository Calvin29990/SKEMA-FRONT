# Morgan Stanley S&T — mémo de préparation bilingue FR / EN

> **Fiche indépendante, non officielle.** Elle explique en français des notions, formules et mots-clés anglais utiles pour réviser le Numerical Reasoning, l’Inductive Reasoning et le Situational Judgement. Ce n’est ni un corrigé, ni une copie de questions propriétaires, ni une garantie sur le contenu exact du test.

## Ce qui est confirmé — et ce qui ne l’est pas

L’invitation de candidature mentionne trois familles : **Numerical Reasoning** (raisonnement numérique), **Inductive Reasoning** (raisonnement inductif) et **Situational Judgement** (jugement situationnel). Les ressources publiques Aon décrivent des formats généraux, mais ne confirment pas les modules précis, le nombre de questions, le minutage, la langue proposée ou les choix de réponse configurés par Morgan Stanley pour cette candidature. Ne transpose pas automatiquement le format SKEMA ou Nomura. Pour la langue et les consignes, l’invitation et l’écran de démarrage font foi.

**À propos des affirmations extrêmes :** les mots absolus comme `always` (« toujours »), `never` (« jamais »), `all` (« tous ») ou `only` (« uniquement ») sont un **signal pour vérifier attentivement la portée** de l’affirmation — pas une preuve automatique qu’elle est fausse. La réponse dépend des données et des consignes.

Si les règles de l’évaluation interdisent l’aide extérieure, ferme cette fiche avant de commencer. Réponds seul pendant le test et n’utilise que les outils expressément autorisés.

---

## 1. Numerical Reasoning — raisonnement numérique

### Routine pour chaque question

1. **`Read the question carefully` — lis précisément la question.** Quelle mesure, quelle entreprise et quelle période sont demandées ?
2. **`Find the relevant data` — repère les données utiles.** Vérifie le titre du tableau, les lignes/colonnes, la devise, l’unité et les périodes.
3. **`Set up the calculation` — pose la relation avant le calcul.** Pour une variation en pourcentage, le dénominateur est normalement la valeur de départ.
4. **`Check like for like` — compare des éléments comparables.** N’oppose pas un trimestre à une année, un total à une valeur par unité, ou une devise à une autre sans conversion.
5. **`Estimate and sense-check` — estime puis vérifie l’ordre de grandeur.** Cela aide à repérer un zéro oublié ou un dénominateur inversé.
6. **`Use only the information given` — n’ajoute pas d’hypothèses externes.** Réponds à ce que les données démontrent, pas à ce qui te paraît probablement vrai.

### Pourcentages — percentages

Dans les formules, écris le taux sous forme décimale : `10% = 0.10`.

- **A représente quel pourcentage de B ?** `A / B × 100%`
- **p% de X :** `X × p / 100`
- **Taux de variation (`percentage change` / `growth rate`) :** `(nouvelle valeur − ancienne valeur) / ancienne valeur × 100%`
- **Après une hausse de p% (`increase by p%`) :** `valeur initiale × (1+p)`.
- **Après une baisse de p% (`decrease by p%`) :** `valeur initiale × (1−p)`.
- **Retrouver la valeur initiale après une hausse :** `valeur finale / (1+p)`.
- **Retrouver la valeur initiale après une baisse :** `valeur finale / (1−p)`.
- **Variations successives (`successive changes`) :** `final = initial × (1+p₁) × (1+p₂)`. Ne somme pas directement les taux si les bases changent.

**Exemple :** une valeur passe de 80 à 100. La hausse est 20; le taux de croissance est `20/80 = 25%`, pas 20%.

### `By` ou `to` ? Une différence essentielle

- **`increased by 10%`** = a augmenté **de** 10% (on calcule la variation par rapport au départ).
- **`increased to 10%`** = est passé **à** 10% (10% est la valeur finale).
- **`decreased from 12% to 9%`** = a baissé de **3 percentage points** (3 points de pourcentage), soit une baisse relative de `3/12 = 25%`.
- **`percentage point` / `pp`** = point de pourcentage. De 12% à 15%, c’est **+3 points**, mais une hausse relative de **25%** du taux.
- **`basis point` / `bp`** = point de base : `1 bp = 0.01 point de pourcentage = 0.0001` en taux décimal; `100 bps = 1 point de pourcentage`.

### Fractions, ratios et proportions — fractions, ratios, proportions

- Passer d’une fraction à un pourcentage : `numérateur / dénominateur × 100%`.
- Comparer des fractions positives `a/b` et `c/d` en comparant `a×d` à `c×b` (dénominateurs positifs).
- Pour le ratio `a:b`, le total comprend `a+b` parts. La part correspondant à `a` dans un total `T` vaut `T × a/(a+b)`.
- Si `A:B = 2:3` et `A = 40`, une part vaut `40/2 = 20`; donc `B = 3×20 = 60`.
- **`A is twice B`** = A vaut deux fois B (`A=2B`). **`A is 200% of B`** = A vaut également `2B`. Mais **`A increased by 200%`** signifie que A a augmenté de deux fois sa valeur de départ : valeur finale `=3B` si B est le départ.
- Si les quantités sont proportionnelles, calcule d’abord la valeur par unité (`per unit`), puis multiplie.

### Moyennes, marges et parts de marché

- **Moyenne pondérée (`weighted average`) :** `Σ(poids × valeur) / Σ(poids)`. Quand les poids sont déjà en pourcentages totalisant 100%, convertis-les en décimales ou divise par 100.
- **Marge bénéficiaire (`profit margin`) :** `profit / revenue × 100%` = bénéfice / chiffre d’affaires.
- **Part de marché (`market share`) :** ventes de l’entreprise / ventes totales du marché `×100%`.
- **Prix moyen (`average price`) :** dépense totale / nombre total d’unités. Si les volumes diffèrent, ne fais pas la simple moyenne des prix.
- **Contribution à la croissance (`contribution to growth`) :** distingue le taux de croissance d’un segment de sa contribution à la hausse globale.

### Croissance composée — compounded growth

- **Taux de croissance annuel composé (`CAGR`, Compound Annual Growth Rate) :** `((valeur finale / valeur initiale)^(1/n) − 1) × 100%`, où `n` est le nombre de périodes.
- Croissance constante `r` pendant `n` périodes : `valeur finale = valeur initiale × (1+r)^n`.
- Une moyenne arithmétique des taux n’est pas toujours équivalente au taux composé; utilise la mesure demandée.

### Valeur actuelle — present value (PV) — et actualisation

Ces formules ne servent que si la question demande d’actualiser des flux. Fais correspondre le taux à la période : taux annuel avec périodes annuelles, taux trimestriel avec périodes trimestrielles.

- **Valeur actuelle d’un montant futur (`present value`, PV) :** `PV = FV / (1+r)^n`.
- **Valeur future (`future value`, FV) :** `FV = PV × (1+r)^n`.
- **Valeur actuelle de plusieurs flux (`cash flows`) :** `PV = Σ[CFₜ / (1+r)^t]`.
- **Valeur actuelle nette (`net present value`, NPV) :** `NPV = −investissement initial + Σ[CFₜ / (1+r)^t]`.
- **Annuité ordinaire (`ordinary annuity`), paiements en fin de période :** `PV = C × [1 − (1+r)^(−n)] / r`.
- **Perpétuité constante (`level perpetuity`) :** `PV = C/r`.
- **Perpétuité croissante (`growing perpetuity`) :** `PV = C₁/(r−g)`, seulement si `r>g` et si le premier paiement arrive dans une période.

`r` = taux **par période**, `n` = nombre de périodes, `C` = paiement constant et `CFₜ` = flux à la période `t`. Si le taux ou une hypothèse n’est pas fourni et que la question ne le demande pas, ne l’invente pas.

### Lire les tableaux et les affirmations

- Vérifie les unités : unités, milliers (`thousands`), millions (`millions`), pourcentage (`percent`), points de base (`basis points`) ou indice (`index`).
- Distingue le **niveau** (`the value was 120` = la valeur était 120), la **variation absolue** (`rose by 20` = a augmenté de 20) et le **taux** (`grew by 20%` = a crû de 20%).
- Un **index de 100** est une base de comparaison, pas nécessairement un montant en devise.
- Repère `annual`, `quarterly`, `year-to-date (YTD)` (depuis le début de l’année), `trailing twelve months (TTM)` (douze derniers mois) et `cumulative` (cumulé).
- `Average` = moyenne, mais vérifie si elle est simple ou pondérée.

### Les mots absolus : red flag de vérification, pas réponse automatique

Mots à entourer mentalement parce qu’ils rendent l’affirmation très forte :

- `always` = toujours; `never` = jamais.
- `all`, `every`, `each` = tous, chaque; `none` = aucun.
- `only`, `solely`, `entirely` = seulement, uniquement, entièrement.
- `must`, `cannot`, `impossible`, `guaranteed` = doit/forcément, ne peut pas, impossible, garanti.
- `exactly` = exactement; `at least` = au moins; `at most` / `no more than` = au plus / pas plus de.

**Méthode :** vérifie si les données couvrent toute la portée du mot. Une seule exception démontrée peut réfuter `always`, `all` ou `only`. Mais si aucune donnée ne permet de confirmer **ou** de contredire une affirmation universelle, la réponse peut être « information insuffisante », selon les choix du test. Un mot extrême n’est donc pas automatiquement faux.

À l’inverse, des termes comme `some` (certains), `may` (peut), `often` (souvent), `generally` (généralement) ou `usually` (habituellement) sont moins absolus, mais ils doivent eux aussi être vérifiés : ils ne rendent pas une phrase automatiquement vraie.

Fais aussi attention aux petits mots logiques : `not` (ne… pas), `except` (sauf), `unless` (à moins que / sauf si), `only if` (seulement si). Ils peuvent inverser la portée d’une phrase.

### `True / False / Cannot Say` — vrai / faux / impossible à déterminer

Certains exercices publics Aon de Numerical Reasoning utilisent des affirmations à classer à partir de données :

- **`True` — vrai :** les données permettent de conclure que l’affirmation est correcte.
- **`False` — faux :** les données la contredisent.
- **`Cannot Say` — impossible à déterminer :** les données ne suffisent ni à la confirmer ni à l’infirmer.

C’est un **format général d’exercices Aon**, pas une confirmation que le test Morgan Stanley utilise ces mêmes réponses. Utilise les choix réellement affichés et n’ajoute pas de connaissance extérieure.

### Exemple original — Numerical Reasoning (questions en anglais)

*Le tableau et les questions sont créés pour cette fiche; ils ne viennent pas d’un test Aon ou Morgan Stanley.*

| Region | Trades 2024 (000s) | Average fee 2024 (€) | Trades 2025 (000s) | Average fee 2025 (€) |
|---|---:|---:|---:|---:|
| UK | 48 | 125 | 54 | 120 |
| France | 36 | 150 | 40 | 165 |
| Germany | 42 | 140 | 39 | 150 |

`Revenue (€000s) = Trades (000s) × Average fee (€)`.

For each statement, choose **True**, **False** or **Cannot Say**, based only on the table:

1. `Total transaction volume increased by at least 5% from 2024 to 2025.`
2. `France’s transaction revenue increased by more than 20%.`
3. `The average fee increased in every region.`
4. `The number of distinct clients increased in Germany.`
5. `Germany’s transaction revenue declined by more than 1%.`
6. `Every region generated more revenue in 2025 than in 2024.`

<details>
<summary>Afficher les réponses et le raisonnement en français</summary>

1. **True.** Volume 2024 : `48+36+42=126`. Volume 2025 : `54+40+39=133`. Hausse : `7/126 ≈ 5,56%`, donc au moins 5%.
2. **True.** Revenu France 2024 : `36×150=5 400` (milliers d’euros). En 2025 : `40×165=6 600`. Hausse : `(6 600−5 400)/5 400 ≈ 22,22%`.
3. **False.** L’affirmation dit `every region` (chaque région). Le fee UK baisse de 125 € à 120 €, ce qui suffit à la contredire.
4. **Cannot Say.** Le tableau donne le nombre de transactions et les frais moyens, pas le nombre de clients distincts. Ne déduis pas un nombre de clients du nombre de transactions.
5. **False.** Revenu allemand : `42×140=5 880` en 2024 et `39×150=5 850` en 2025. La baisse est `30/5 880 ≈ 0,51%`, pas plus de 1%.
6. **False.** C’est une affirmation absolue (`every`). Le revenu allemand baisse de 5 880 à 5 850; une seule exception la réfute.

</details>

---

## 2. Inductive Reasoning — raisonnement inductif

Traite chaque symbole comme une donnée; évite de deviner d’après l’impression générale.

### Ordre de vérification utile

Vérifie une propriété à la fois :

1. **`Count` — nombre :** objets, points, côtés ou éléments.
2. **`Type` — type :** forme, symbole ou catégorie.
3. **`Position` — position :** emplacement, ordre, intérieur/extérieur, gauche/droite, haut/bas.
4. **`Orientation` — orientation :** rotation, direction, miroir ou ordre de rotation.
5. **`Appearance` — apparence :** remplissage, hachures, couleur, taille, contour.
6. **`Relationship` — relation :** chevauchement, inclusion, alternance, addition/soustraction ou déplacement.

Compare ensuite les lignes, colonnes ou cases adjacentes. Dis la règle en une phrase et vérifie-la pour chaque élément. Si la consigne demande l’intrus (`odd one out`), cherche la propriété que la majorité partage et que l’intrus ne respecte pas. Préfère une règle simple qui explique l’ensemble à une règle compliquée qui ne marche que pour quelques figures.

Le document public Aon **Scales ix** présente génériquement neuf objets, dont un qui ne suit pas la règle. Cela ne prouve pas que Morgan Stanley utilise Scales ix, la même grille, le même minutage ou le même nombre de questions.

**Pièges à éviter :** ne te fixe pas trop vite sur la couleur ou la rotation; vérifie le nombre et la position. Certaines suites alternent deux règles (positions impaires et paires). Confirme le sens de rotation et si le pas est fixe. Si une piste ne fonctionne pas pour toutes les figures, teste une autre propriété.

### Exemple original — Inductive Reasoning (question en anglais)

*Version textuelle simplifiée d’une recherche de règle parmi neuf objets; les symboles sont décrits plutôt que dessinés. Ce n’est pas une question officielle.*

**Which object is the odd one out? Select one object.**

| Object | Shape | Number of dots |
|---:|---|---:|
| 1 | Triangle | 1 |
| 2 | Square | 2 |
| 3 | Pentagon | 3 |
| 4 | Square | 2 |
| 5 | Pentagon | 3 |
| 6 | Triangle | 1 |
| 7 | Pentagon | 3 |
| 8 | Square | 1 |
| 9 | Triangle | 1 |

<details>
<summary>Afficher la réponse et le raisonnement en français</summary>

**Objet 8.** Cherche une relation qui marche pour huit objets : triangle = 3 côtés et 1 point; carré = 4 côtés et 2 points; pentagone = 5 côtés et 3 points. La règle est `number of dots = number of sides − 2`. L’objet 8 est un carré avec 1 point : il devrait en avoir 2. Vérifie que la même règle explique les huit autres objets avant de choisir.

</details>

**Second example — Which object is the odd one out?**

Each object has an arrow and a number of dots:

| Object | Arrow | Dots |
|---:|---|---:|
| 1 | Up | 1 |
| 2 | Right | 2 |
| 3 | Down | 3 |
| 4 | Left | 1 |
| 5 | Up | 2 |
| 6 | Right | 3 |
| 7 | Down | 1 |
| 8 | Left | 2 |
| 9 | Up | 4 |

<details>
<summary>Afficher la réponse et le raisonnement en français</summary>

**Objet 9.** Deux cycles se superposent : les flèches tournent `Up → Right → Down → Left`, tandis que les points suivent `1 → 2 → 3`, puis recommencent. Après `Left / 2`, l’objet 9 devrait être `Up / 3`; il a 4 points. Cette vérification de deux propriétés est plus solide qu’une impression visuelle isolée.

</details>

---

## 3. Situational Judgement — jugement situationnel

Il n’existe pas de corrigé public des scénarios Morgan Stanley. Ces principes sont des repères de jugement professionnel, **pas une grille officielle de notation**.

### Ordre de priorité général

1. **`Compliance` — conformité :** loi, règlement, procédures internes et intégrité des marchés. Ce sont des limites à respecter, pas des contraintes à échanger contre la rapidité ou le chiffre d’affaires.
2. **`Client interests` — intérêts du client :** servir son besoin légitime, tenir compte de l’adéquation (`suitability`) et rester exact. « Client first » ne veut pas dire contourner la conformité, promettre l’impossible ou traiter injustement un autre client.
3. **`Confidentiality` — confidentialité :** protéger les données client et les informations sensibles.
4. **`Urgency and impact` — urgence et impact :** prévenir ou limiter rapidement un préjudice; repérer qui a l’autorité pour agir.
5. **`Respectful communication` — communication respectueuse :** clarifier les faits, rester diplomate, éviter accusation et spéculation.
6. **`Ownership and escalation` — prise en charge et remontée :** agir dans son rôle; solliciter le responsable ou la fonction de contrôle appropriée si le risque est important.
7. **`Follow-through` — suivi :** documenter comme prévu par la procédure et vérifier que le problème est traité.

### Protéger les informations — mots-clés à reconnaître

- `confidential information` = information confidentielle.
- `restricted information` = information soumise à des restrictions internes.
- `inside information` / `material non-public information` = information privilégiée / information importante non publique, selon le contexte et les règles applicables.
- `authorised recipient` = destinataire autorisé; `need-to-know basis` = uniquement si la personne en a besoin pour son travail.
- `approved channel` = canal autorisé; `disclose` = divulguer; `leak` = fuite; `report a breach` = signaler un incident/une violation.

Ne diffuse pas d’informations sensibles à des personnes non autorisées, ne vérifie pas un destinataire à la légère et n’utilise pas de compte personnel ou d’outil public pour des données confidentielles. En cas de fuite possible, suis immédiatement la procédure de signalement; ne cache pas l’incident et ne mène pas d’enquête hors de ton rôle.

### Respect, diplomatie et escalade

- Pour un malentendu mineur, clarifie directement et en privé si c’est approprié.
- Pour une faute grave ou répétée, un risque client important, une violation de contrôle ou un risque de marché, alerte rapidement le canal approprié — même si la personne impliquée est plus senior.
- `Escalate` signifie transmettre à un responsable ou une fonction compétente; ce n’est ni accuser sans preuve, ni répandre l’information à tout le monde.
- `Acknowledge` = reconnaître/accuser réception; `clarify` = clarifier; `raise a concern` = signaler une préoccupation; `seek guidance` = demander conseil; `take ownership` = prendre la responsabilité du suivi.
- Décris des faits observables et leur impact; ne fais pas de commérage, de représailles ou de promesses hors de ton autorité.
- Si tu ne sais pas, vérifie et donne un délai réaliste pour revenir vers la personne (`I will check and get back to you`). L’honnêteté est préférable à une réponse improvisée.

### Mini-checklist C.L.E.A.R.

- **C — Compliance :** est-ce autorisé et conforme ?
- **L — Listen :** quel est le besoin réel ? Qu’est-ce qui manque comme fait ?
- **E — Evaluate :** quelle urgence, quel impact, quel risque de confidentialité ?
- **A — Act :** quelle action utile puis-je prendre dans mon rôle ?
- **R — Report and review :** faut-il signaler, documenter ou vérifier le suivi ?

Dans un choix forcé, méfie-toi en général des réponses qui retardent sans raison, dissimulent un problème, divulguent trop largement, contournent les contrôles, spéculent ou promettent un résultat impossible. Cherche une réaction proportionnée, rapide et conforme. Ce sont des principes généraux, pas une garantie de réponse attendue par Morgan Stanley.

### Exemples originaux — Situational Judgement (scénarios en anglais)

*Choisis la meilleure action professionnelle. Les explications sont des principes généraux, pas un corrigé officiel.*

**1. A client presentation is due shortly. You notice a material discrepancy in a chart prepared by a colleague. What is the best response?**

A. Send the presentation as it is; correct the chart later if anyone notices.
B. Raise the discrepancy constructively with your colleague, verify the source, correct the information and alert the responsible person if the deadline or client communication is affected.
C. Delete the slide without telling anyone.
D. Criticise the colleague in a group message so the whole team knows who made the mistake.

**2. A client asks for another client’s transaction details as a benchmark. What is the best response?**

A. Share the details after removing the other client’s name, without checking the rules.
B. Explain that you cannot disclose another client’s confidential information; offer an authorised public or aggregated alternative if available.
C. Send the details to the client’s personal email so fewer people see them.
D. Ask a colleague to send the information instead.

**3. A colleague tells you they accidentally emailed confidential client data to an unauthorised recipient. What should you do?**

A. Ask them to wait and see whether the recipient complains.
B. Forward the email and attachment to the whole team to warn everyone.
C. Follow the firm’s incident-reporting process promptly, alert the appropriate manager/control function, preserve the relevant facts and avoid further unnecessary disclosure.
D. Contact the recipient personally and threaten them if they do not delete it.

<details>
<summary>Afficher les meilleures réponses et le raisonnement en français</summary>

1. **B — agir sur l’exactitude tout en restant diplomate.** Il faut vérifier le chiffre rapidement, corriger l’information et prévenir la personne responsable si le client ou l’échéance est concerné. C’est respectueux envers le collègue sans dissimuler une erreur matérielle. Envoyer une information connue comme erronée, la cacher ou humilier le collègue sont de mauvais choix professionnels.
2. **B — confidentialité d’abord, puis solution autorisée.** Retirer le nom ne garantit pas l’anonymat : le détail d’une transaction peut permettre d’identifier le client. Refuse la divulgation et propose seulement une source publique ou des données agrégées dont l’usage est autorisé.
3. **C — remonter immédiatement par la procédure prévue.** Une fuite potentielle peut créer un risque client, réglementaire ou de sécurité. Il faut alerter le canal compétent sans délai, rester factuel et ne pas propager davantage le fichier. Attendre, dissimuler, diffuser à toute l’équipe ou improviser une menace à l’extérieur ne remplace pas la procédure.

</details>

---

## 4. Mini-glossaire anglais pour tableaux et consignes

| Mot / expression | Sens en français |
|---|---|
| `revenue` / `sales` | chiffre d’affaires / ventes |
| `profit` / `loss` | bénéfice / perte |
| `cost` / `expense` | coût / charge |
| `margin` | marge |
| `yield` | rendement |
| `share` | part; peut aussi signifier action selon le contexte |
| `total` / `overall` | total / global |
| `respectively` | respectivement; associe les valeurs dans le même ordre |
| `whereas` / `while` | tandis que / alors que; marque souvent un contraste |
| `unless` | à moins que / sauf si |
| `at least` / `no less than` | au moins; inclut la borne |
| `more than` / `greater than` | plus de / supérieur à; exclut l’égalité |
| `at most` / `no more than` | au plus / pas plus de; inclut généralement la borne maximale |
| `approximately` / `roughly` | environ / à peu près |
| `previous` / `following` | précédent / suivant |
| `year-on-year (YoY)` | par rapport à la même période l’année précédente |
| `quarter-on-quarter (QoQ)` | par rapport au trimestre précédent |
| `cumulative` / `year-to-date (YTD)` | cumulé / depuis le début de l’année |
| `does not necessarily mean` | ne signifie pas nécessairement; une conclusion ne découle pas automatiquement du fait |

---

## 5. Avant de lancer l’évaluation

- Relis l’invitation et les consignes affichées. Vérifie la langue, le temps, les outils permis (calculatrice, brouillon) et la possibilité de revenir aux questions.
- Prévois une plage sans interruption correspondant à la durée officielle, avec une marge. Ne déduis pas le minutage Morgan Stanley d’un test Aon ou SKEMA différent.
- Vérifie connexion, batterie et calme; coupe les notifications.
- Si le test doit être fait en une séance, ne le lance que lorsque tu as le temps nécessaire. Suis les instructions de l’employeur si elles disent autre chose.
- Pendant l’épreuve, réponds seul et n’utilise que les outils expressément autorisés. Ne partage pas de questions ou captures du test en direct.

## Sources publiques

Ces sources décrivent des formats **Aon généraux**, pas la configuration exacte de Morgan Stanley :

- [Aon — Préparer son évaluation en ligne](https://www.aon.com/en/capabilities/talent-and-rewards/prepare-for-your-online-assessment)
- [Aon — Exemples de raisonnement numérique (PDF)](https://www.aon.com/getmedia/3cc4d7fa-531f-4c0d-b4b3-e88afb130b74/practice-tasks-numerical-reasoning.pdf)
- [Aon — Exemples de raisonnement inductif Scales ix (PDF)](https://www.aon.com/getmedia/54a05144-c659-4bcb-bb18-8613d9081845/practice-tasks-inductive-reasoning-ix.pdf)
- [Aon — Espace candidat (présentation générale de chatAssess)](https://assessment.aon.com/fr-fr/espace-candidat?shortcut=)

**À retenir :** `check the data` (vérifie les données), `test the rule` (vérifie la règle), `protect the client and confidential information` (protège le client et les informations confidentielles), `follow policy` (respecte la procédure). L’invitation et l’écran officiel, pas cette fiche, définissent le test réel.
