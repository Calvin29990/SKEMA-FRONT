# Questionnaire Excel Gestion 21 — guide débutant, puis méthode de résolution

**Calvin — préparation à l’entretien Assistant Sales / Relations Investisseurs**  
**Version préparatoire fondée sur les trois captures d’écran reçues.** Le classeur `.xlsx` lui-même n’est pas dans les pièces disponibles ici : je peux donc expliquer exactement ce que montrent les onglets et préparer les calculs, mais je ne vais pas inventer les chiffres finaux ni prétendre avoir vérifié les données masquées. Dès que le fichier Excel est joint, on peut compléter les résultats exacts, les formules aux bonnes cellules et un corrigé ligne par ligne.

---

## 0. D’abord : à quoi sert ce classeur ?

Ce n’est pas un exercice de trading ni un test de calcul mental. C’est plutôt un mini-cas de **gestion d’actifs** : on te donne des historiques de **valeurs liquidatives** (les prix des parts de fonds), puis on te demande de mesurer des performances, de comparer avec un indice, de mettre des données en forme et d’expliquer ce que les chiffres signifient.

Dans la vraie vie, un commercial ou un chargé de relations investisseurs ne se contente pas de produire un pourcentage. Il doit pouvoir dire :

1. **Quel produit / quelle part ?**
2. **Sur quelle période et avec quelles dates ?**
3. **Par rapport à quoi ?**
4. **Qu’est-ce que le chiffre signifie pour le client ?**
5. **Quelles limites ou quels risques faut-il préciser ?**

Un chiffre juste mais associé à la mauvaise part, à la mauvaise période ou au mauvais indice est un chiffre trompeur.

---

# Partie I — explication onglet par onglet

## Onglet 1 — `Instructions`

C’est l’énoncé. Il contient **sept questions**, pas les séries chiffrées nécessaires à tous les calculs.

### Traduction en français simple

1. **Performance 2024 de la part IC d’OCC 21** : combien la valeur de cette part a-t-elle progressé ou baissé entre la fin 2023 et la fin 2024 ?
2. **Performance 2024 de la part ID d’Immobilier 21** : même idée, mais avec une part distribuante d’un autre fonds. Il faut distinguer la simple variation de VL du rendement total qui tient compte d’une distribution.
3. **Comparer OCC 21 à un indice en base 100 de fin 2021 à fin 2025** : transformer les deux séries pour qu’elles commencent au même niveau, puis les tracer sur un graphique.
4. **Performance annualisée sur cinq ans de la part AC d’OCC 21 au 30/06/2026, et surperformance** : trouver le rendement annuel équivalent sur cinq ans et comparer à la référence demandée. La référence doit être vérifiée : les documents d’OCC 21 indiquent un **objectif de gestion** et précisent que le fonds n’a pas d’indice de référence destiné à reproduire sa performance. Il ne faut donc pas inventer un benchmark.
5. **Extraire des VL à des dates données** : remplir les colonnes IC, ID et AC à partir des historiques.
6. **Corrélation immobilier coté / taux** : calculer une relation statistique entre les variations observées et expliquer ce qu’elle veut dire — et ce qu’elle ne prouve pas.
7. **Proposer trois sociétés cotées pour Actions 21** : faire une mini-recherche d’investissement cohérente avec la stratégie, argumenter et reconnaître les risques.

> Les questions 6 et 7 se répondent avec une **analyse expliquée**, pas uniquement avec une formule Excel.

## Onglet 2 — `VL OCC 21`

Sur la capture, l’onglet contient un historique de **valeurs liquidatives OCC 21** et des colonnes de parts `IC`, `ID`, `AC` (la série complète semble aussi présenter `AD` dans une autre vue).

### Ce que signifie une valeur liquidative (VL)

Imagine un panier d’investissements détenu par le fonds. La VL est le prix calculé d’une part du panier à la date de valorisation, suivant les règles du fonds. Si une part vaut 1 000 € puis 1 100 €, sa hausse sur cette période est de 10 %.

### Les lettres des parts OCC 21

Les documents du fonds distinguent quatre parts :

- **IC** : capitalisation ;
- **ID** : distribution ;
- **AC** : capitalisation ;
- **AD** : distribution.

Les distributions sont prévues pour les parts `ID` et `AD`, alors que les revenus sont capitalisés pour `IC` et `AC`. Les parts I et A sont des catégories différentes avec des conditions et frais différents : ne remplace jamais une part par une autre dans un calcul. Le prospectus donne notamment des niveaux de frais distincts entre les parts I et A. La différence IC/AC n’est donc pas simplement une différence de lettre sans effet.

### Comment lire chaque ligne

- La colonne `Date` donne la date associée à la VL.
- Les colonnes IC/ID/AC/AD donnent la VL de chacune des parts à cette date.
- Une date de question peut tomber un jour où le fonds n’a pas calculé de VL. Il faut alors retrouver la dernière VL disponible **à la date demandée ou juste avant**, selon la consigne et la convention retenue.

**Parallèle réel :** c’est comme comparer deux relevés de compte à des dates de clôture. On ne prend pas une valeur de la semaine suivante pour représenter le 31 décembre sans le signaler.

## Onglet 3 — `VL IMMOBILIER 21`

La capture montre une série chronologique de VL pour les parts IC, ID, AC et AD. Cette feuille sert au minimum à retrouver les valeurs nécessaires à la question 2 ; elle peut aussi contenir les données de la question 6 ou des séries supplémentaires. Il faut voir le classeur entier pour confirmer les colonnes.

`IMMOBILIER 21` investit en actions de foncières cotées de la zone euro : ce sont des **entreprises immobilières cotées**, et non un portefeuille d’appartements détenus directement par l’investisseur. La VL d’un fonds immobilier coté peut donc fluctuer comme une action, et être sensible aux anticipations de taux, au coût du financement, aux loyers, à la valorisation des actifs, aux perspectives économiques et au sentiment de marché.

### Autres onglets possibles

Les captures ne permettent pas de confirmer s’il existe d’autres onglets cachés ou non affichés (par exemple des données de taux ou d’indice). Le classeur original permettra de les inventorier proprement.

---

# Partie II — les formules indispensables

## 1. Calculer un rendement simple

**Formule financière :**

`Rendement = (valeur de fin / valeur de début) - 1`

**Exemple fictif :** VL de départ = 1 000 € ; VL d’arrivée = 1 080 €.

`1 080 / 1 000 - 1 = 0,08 = +8 %`

Dans Excel français, si la VL de début est en `B2` et celle de fin en `B3` :

`=B3/B2-1`

Formate la cellule en pourcentage. Vérification simple : une hausse doit donner un nombre positif ; une baisse, un nombre négatif.

### Pourquoi ne pas faire simplement « fin moins début » ?

`1 080 - 1 000 = 80 €` indique le changement en euros par part, mais ne donne pas le rendement comparable. Si le départ avait été 10 000 €, le même gain de 80 € n’aurait représenté que 0,8 %.

## 2. Calculer une performance annualisée

Le rendement annualisé est le taux annuel constant qui conduirait au même résultat cumulé sur la période. Il tient compte de la capitalisation.

`Rendement annualisé = (VL finale / VL initiale)^(1 / nombre d’années) - 1`

Exemple fictif : une valeur passe de 100 à 121 en deux ans.

- Rendement total : `121/100 - 1 = 21 %`.
- Rendement annualisé : `(121/100)^(1/2)-1 = 10 % par an`.
- Contrôle : `100 × 1,10 × 1,10 = 121`.

**Intérêt pratique :** comparer des performances sur des durées différentes. Dire « +21 % sur deux ans » n’est pas la même chose que dire « +21 % par an ».

## 3. Surperformance : toujours nommer la référence

- **Surperformance en points** = rendement du fonds − rendement de la référence.
- Si le fonds fait +8 % annualisé et la référence +6 % annualisé : surperformance = **+2 points de pourcentage par an**.
- Une autre mesure parfois utilisée est la performance relative composée : `(1 + rendement fonds)/(1 + rendement référence) - 1`. Il faut annoncer la convention choisie.

**Pour OCC 21 :** les informations du fonds indiquent un objectif de rendement annuel (dans les documents consultés : au-dessus de 7 % pour IC/ID, 6 % pour AC/AD), et pas un indice de référence à répliquer. La question 4 demande peut-être de comparer l’AC à l’objectif de 6 %, mais cela doit être confirmé par l’énoncé complet, le document de cours ou le classeur. Un objectif n’est pas une promesse de résultat.

## 4. Mettre deux séries en base 100

Pour chaque date `t` :

`Indice base 100 à t = valeur à t / valeur à la date de départ × 100`

Exemple fictif : niveau initial 200, niveau ultérieur 230 → `230/200×100 = 115`. Cela correspond à une hausse de 15 % depuis le départ.

Dans Excel, si les valeurs commencent en `B2` et la base est en `$B$2` :

`=B2/$B$2*100`

Les `$` gardent la cellule de départ fixe quand on recopie la formule. Faire la même opération pour le fonds et l’indice, en choisissant des dates comparables. Ensuite, sélectionner les dates et les deux colonnes base 100 → **Insertion > Graphique en courbes**.

**Pourquoi base 100 ?** Deux séries peuvent avoir des niveaux de prix différents — par exemple une VL à 1 200 et un indice à 4 500. Les niveaux bruts ne sont pas comparables. Base 100 compare leurs évolutions depuis une même origine.

## 5. Extraire la VL correspondant à une date

Excel récent en français peut utiliser `RECHERCHEX`. Exemple à adapter une fois qu’on connaît les colonnes exactes :

`=RECHERCHEX(date_cible;colonne_dates;colonne_VL;"Non trouvé";-1)`

Le mode `-1` cherche une correspondance exacte ou, à défaut, la date immédiatement inférieure dans une liste triée par date croissante. C’est souvent adapté à une date sans VL, mais il faut confirmer que l’énoncé veut bien la dernière VL disponible avant la date.

Alternative avec `INDEX`/`EQUIV` sur une série chronologique triée :

`=INDEX(plage_VL;EQUIV(date_cible;plage_dates;1))`

L’option approximative exige un historique trié par dates croissantes. La formule renvoie une VL antérieure ou égale à la date cible, pas nécessairement une VL du jour exact.

**Si `#N/A` apparaît :** vérifier que les dates sont de vraies dates Excel (pas du texte), que la colonne est triée, et décider si l’on cherche une date exacte ou la dernière date précédente.

---

# Partie III — résolution guidée des sept questions

## Question 1 — Performance 2024 de la part IC du fonds OCC 21

### Méthode

1. Dans `VL OCC 21`, repérer la colonne `IC`.
2. Repérer la dernière VL disponible à la fin de 2023 et la dernière VL disponible à la fin de 2024. Pour un fonds à VL hebdomadaire, ce ne sera pas forcément le 31 décembre exact.
3. Calculer :

`=(VL_IC_fin_2024/VL_IC_fin_2023)-1`

4. Formater en pourcentage.
5. Écrire l’intervalle réel dans la réponse, par exemple « dernière VL disponible de 2023 à dernière VL disponible de 2024 », si les dates diffèrent des 31 décembre.

### Ce que tu dirais en situation professionnelle

« La part IC a réalisé X % sur la période mesurée. J’ai utilisé la dernière VL disponible de chaque année, car la date civile de clôture ne correspond pas nécessairement à une date de calcul de VL. »

### Erreurs fréquentes

- prendre la première VL de 2024 comme départ alors que la question porte sur toute l’année 2024 ;
- soustraire des VL au lieu de calculer un rendement en pourcentage ;
- confondre IC et ID ou IC et AC ;
- oublier que les VL sont déjà nettes de certains frais du fonds, selon les règles de calcul ;
- arrondir les deux VL trop tôt.

**Valeur numérique :** impossible à établir de manière fiable avec les captures, car les VL de fin 2023 et 2024 ne sont pas visibles.

## Question 2 — Performance 2024 de la part ID du fonds IMMOBILIER 21

La question porte bien sur 2024 et sur la colonne `ID`.

1. Repérer la VL ID au début de 2024 (dernière VL de 2023 ou première VL de 2024, selon la convention explicitée par le classeur) et la VL ID à la fin de 2024 (dernière VL publiée en 2024).
2. Calculer d’abord la variation de VL : `(VL_fin_2024/VL_début_2024)-1`.
3. Vérifier dans le classeur et les documents du fonds si « performance » signifie cette variation seule ou un rendement total intégrant les distributions. Pour une part `ID`, cette distinction est importante : les distributions de revenus ou de plus-values sont versées au porteur, et le montant correspondant peut faire baisser la VL à la date de détachement.
4. Si une distribution intervient pendant 2024, ne l’ajoute pas mécaniquement à la VL finale sans tenir compte de sa date. Pour un rendement total exact, utiliser une série de VL ajustée des distributions ou composer les rendements avec distributions selon la méthode définie dans la source. Si le sujet demande expressément la seule évolution de la VL, présenter ce chiffre comme tel et signaler qu’il exclut le cash distribué.

**Parallèle concret :** deux épargnants peuvent avoir un investissement de même valeur totale ; l’un reçoit du cash sur son compte (part distributive), l’autre le laisse dans le fonds (part capitalisante). Comparer uniquement les soldes visibles à la fin peut faire croire à tort que le premier a moins gagné.

**Valeur numérique :** à calculer à partir de la série exacte et, si nécessaire, des dates/montants de distribution du classeur.

## Question 3 — OCC 21 et indice Euronext en base 100, 31/12/2021–31/12/2025

1. Confirmer le nom exact de l’indice dans l’énoncé / classeur. La capture semble dire « Euronext Caped/Capped », mais le nom exact doit être lu dans le fichier.
2. Identifier la VL IC OCC 21 la plus proche à la date de départ et à chaque date de comparaison, ainsi que la série d’indice correspondante.
3. Choisir des dates alignées. Si une VL est hebdomadaire et l’indice quotidien, sélectionner des observations comparables ou ramener les deux séries à une fréquence commune.
4. Calculer pour les deux séries : `valeur_t / valeur_départ × 100`.
5. Faire un graphique en courbes, titre clair, axe vertical « Base 100 », légende identifiant le fonds et l’indice, période indiquée.
6. Écrire l’interprétation sans confondre les deux séries : à la date finale, si le fonds est à 140 et l’indice à 120, chacun a progressé de 40 % et 20 % depuis la base (écart de 20 points de base 100 ; ce n’est pas directement un rendement relatif composé).

### Dividendes : vérifier la convention

Un indice de prix qui ignore les dividendes n’est pas la même chose qu’un indice dividendes réinvestis. Un fonds reçoit éventuellement des dividendes de ses titres. Il faut utiliser l’indice indiqué dans l’énoncé (souvent la version « net return » si l’on compare des rendements investissables) et le nommer dans le graphique.

**Valeurs et graphique :** nécessitent les colonnes de données et l’identification précise de l’indice, absentes des captures.

## Question 4 — Rendement annualisé cinq ans de la part AC d’OCC 21 au 30/06/2026

1. La date finale est le 30/06/2026.
2. Trouver la VL AC au 30/06/2021 ou la dernière VL disponible avant cette date, selon la convention de l’exercice.
3. Trouver la VL AC au 30/06/2026 ou la dernière VL disponible à cette date.
4. Calculer :

`=(VL_AC_30juin2026/VL_AC_30juin2021)^(1/5)-1`

5. Pour la « surperformance », identifier la référence expressément demandée. Les documents publics d’OCC 21 mentionnent un objectif de gestion de 6 % net annuel pour la catégorie AC/AD (à confirmer avec la version applicable à l’exercice) et indiquent que le fonds ne cherche pas à répliquer un indice. Si la consigne compare à l’objectif, la différence en points est `rendement annualisé AC – 6 %`.

### Jargon : annualisé n’est pas cumulé

Si le résultat cumulé sur cinq ans est +40 %, le rendement annualisé n’est pas `40/5=8 %` exactement. Il faut calculer `1,40^(1/5)-1`, soit environ 6,96 % par an.

**Valeur numérique :** nécessite les deux VL exactes et la référence visée par « surperformance ».

## Question 5 — Remplir IC, ID et AC aux dates indiquées

Les dates visibles dans la capture sont : 17/01/2019, 30/04/2020, 09/06/2021, 04/05/2023 et 21/11/2024.

Pour chaque date :

1. rechercher la date dans la table `VL OCC 21` ;
2. retourner la VL IC, ID et AC correspondante ;
3. si la date exacte n’existe pas, prendre la dernière VL disponible antérieure ou égale si c’est la convention attendue, et noter la date effective utilisée ;
4. contrôler une ligne manuellement en retrouvant cette date dans la source.

Une formule de recherche est utile pour automatiser cinq dates × trois parts, mais le contrôle visuel est essentiel : la bonne formule peut retourner la mauvaise colonne si la plage sélectionnée est décalée.

## Question 6 — Corrélation entre variations d’IMMOBILIER 21 et variations des taux

### Ce que veut dire corrélation

La corrélation mesure si deux séries ont tendance à évoluer ensemble. Elle est comprise entre `-1` et `+1` :

- près de `+1` : elles évoluent souvent dans le même sens ;
- près de `-1` : elles évoluent souvent dans des sens opposés ;
- près de `0` : pas de relation linéaire forte observée dans l’échantillon.

Elle ne prouve **pas** qu’une variable cause l’autre.

### Bonne méthode de calcul

1. Identifier exactement la série de taux (taux souverain, maturité, pays, fréquence) et la période.
2. Calculer des rendements du fonds entre dates successives : `VL_t/VL_(t-1)-1`.
3. Calculer les variations du taux sur les mêmes dates : en points de pourcentage ou points de base. Comparer une série de rendements à des variations de taux est généralement plus informatif qu’à un taux de niveau, mais il faut suivre la consigne du fichier.
4. Aligner les dates, supprimer les paires incomplètes, vérifier les unités et les fréquences.
5. Calculer une corrélation Excel, en français généralement `=COEFFICIENT.CORRELATION(plage_rendements;plage_variations_taux)` (le nom peut varier selon la version/langue).
6. Interpréter le signe, la force et les limites de l’échantillon.

### Parallèle avec la vraie vie

Quand les taux montent, le financement immobilier peut coûter plus cher et les rendements obligataires deviennent relativement plus compétitifs ; cela peut peser sur les foncières. Mais les loyers, l’occupation, l’inflation, les perspectives de croissance, les bénéfices, le levier financier, les primes de risque et les attentes des investisseurs changent aussi. Donc « les taux montent, le fonds baisse » peut être une intuition économique ; ce n’est pas une loi mécanique et une corrélation historique ne permet pas de prédire à elle seule la prochaine performance.

**Résultat numérique et interprétation de l’échantillon :** nécessitent les séries de taux et les données VL complètes.

## Question 7 — Choisir et justifier trois sociétés pour Actions 21

Il s’agit d’une mini-idée d’investissement, pas d’une devinette où il existe forcément trois réponses officielles. La proposition doit être cohérente avec la stratégie réelle du fonds et appuyée sur des informations à jour.

### Grille simple pour analyser une société

Pour chacune des trois sociétés :

1. **Nom, pays, secteur et ticker/ISIN** : montrer que le titre est bien coté et admissible dans l’univers considéré.
2. **Activité** : expliquer en une phrase comment l’entreprise gagne de l’argent.
3. **Qualité des fondamentaux** : évolution des ventes, marges, cash-flow, dette, bilan, position concurrentielle.
4. **Valorisation** : expliquer pourquoi le prix paraît raisonnable par rapport aux bénéfices, flux de trésorerie, actifs ou pairs. Une action à faible multiple n’est pas automatiquement une bonne valeur.
5. **Catalyseur / horizon** : quel événement ou amélioration pourrait libérer de la valeur, et à quel horizon ?
6. **Risque principal** : dette, cyclicité, réglementation, concurrence, exécution, gouvernance, etc.
7. **Conclusion équilibrée** : « titre à étudier » plutôt que « titre qui va forcément monter ».

Une bonne réponse ne doit pas laisser croire que tu connais le portefeuille actuel si tu ne l’as pas consulté. Présente les trois noms comme des **idées personnelles à analyser**, pas comme des positions de Gestion 21.

**Pour faire ce travail correctement**, il faut les caractéristiques exactes d’Actions 21 données par l’exercice, un univers de titres admissibles et des sources récentes sur les sociétés. Dès que le fichier est disponible, on peut construire trois cas cohérents et sourcés, avec points positifs et risques.

---

# Partie IV — parler de la réponse comme un professionnel débutant

Pour chaque calcul, utilise une phrase en quatre morceaux :

> « J’ai mesuré **[la série / la part]** entre **[date de départ]** et **[date de fin effective]**. J’ai utilisé **[la formule / méthode]**. Le résultat est **[x %]**, ce qui signifie **[interprétation simple]**. La limite est **[benchmark / distributions / dates / échantillon]**. »

Exemple fictif :

> « La part IC a progressé de 8 % entre la dernière VL disponible de 2023 et celle de 2024, calculé par VL finale divisée par VL initiale moins un. Cela représente une hausse de 8 % sur cette période, avant de conclure sur la qualité du fonds : il faudrait aussi regarder le risque, les frais et une comparaison pertinente. »

Cette structure démontre à la fois Excel, compréhension financière et prudence commerciale.

---

## Sources financières de référence

Sources Gestion 21 consultées pour préparer ce guide :

- [OCC 21 — stratégie, parts, caractéristiques et documents](https://gestion-21.fr/funds-occ-21/)
- [Prospectus OCC 21](https://gestion-21.fr/wp-content/uploads/2024/06/OCC21_Prospectuscomplet-31.05.2024.pdf) — catégories de parts, capitalisation/distribution, objectif et frais (vérifier la version en vigueur à la date de l’exercice).
- [IMMOBILIER 21](https://gestion-21.fr/funds/immobilier-21/) — stratégie et informations sur le fonds.
- [ACTIONS 21](https://gestion-21.fr/funds/actions-21/) — stratégie et documents récents.

*Ce document explique une méthode de travail. Il ne constitue ni une recommandation d’investissement, ni le corrigé chiffré du fichier tant que le classeur source n’a pas été fourni.*
