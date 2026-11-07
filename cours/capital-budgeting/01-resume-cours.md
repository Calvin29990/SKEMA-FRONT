# Capital Budgeting — résumé du cours, de l'introduction au Step 5

Ce document suit les supports de Sébastien Dereeper, fondés sur Berk & DeMarzo. Termes anglais conservés pour faciliter les QCM. Pour les calculs : [exercices et pièges](02-exercices-qcm.md) · [mémo express](03-memo-examen.md).

## Introduction : le fil conducteur

Le capital budgeting consiste à décider quels investissements créent de la valeur : **prévoir les flux incrémentaux → déterminer leur risque et leur taux → calculer la VAN → prendre en compte les effets du financement**. Un bon projet augmente la richesse des actionnaires ; un résultat comptable élevé ne garantit pas une création de valeur.

## Step 1 — Calculer les flux de trésorerie

### 1. Raisonner en différentiel

Pour chaque année, comparer « avec projet » à « sans projet ». Inclure ventes et coûts additionnels, coûts d'opportunité (loyer ou prix de vente abandonné), effets sur les autres produits (cannibalisation en **marge**, pas seulement en chiffre d'affaires), frais fixes réellement supplémentaires. Exclure les coûts irrécupérables (*sunk costs*) et frais qui existeraient dans tous les cas. Une perte de ventes qui aurait eu lieu même sans projet n'est pas causée par celui-ci.

### 2. Du résultat au free cash flow

- `EBIT = ventes incrémentales − coûts d'exploitation incrémentaux − amortissement`.
- `Résultat non endetté = EBIT × (1 − taux d'impôt T)` : sans intérêts, après impôt.
- **`FCF = EBIT × (1 − T) + amortissement − CAPEX − ΔBFR`**, avec `ΔBFR = BFR fin − BFR début`.
- `BFR = trésorerie d'exploitation + stocks + créances clients − dettes fournisseurs` (selon les postes donnés). Une hausse immobilise du cash ; la récupération finale est une entrée. Respecter le calendrier précisé dans l'énoncé.
- L'amortissement n'est pas un décaissement : on le réintègre, mais il réduit l'impôt. Son bouclier annuel vaut `T × amortissement` si la déduction est utilisable. L'investissement lui-même sort en CAPEX lorsqu'il est payé.
- Vendre un actif produit `prix de vente − T × (prix de vente − valeur comptable)` : si la vente est à perte, une économie d'impôt peut en résulter si elle est utilisable. Inclure la valeur résiduelle et les flux de fin de projet.

Les intérêts et remboursements de dette ne sont **pas** dans le FCF non endetté : les effets de financement sont traités séparément, notamment par le WACC après impôt ou l'APV. Une perte fiscale ne crée pas forcément un remboursement immédiat : vérifier capacité d'utilisation, plafonds et report. Actualiser les économies au moment où elles sont réellement obtenues.

### 3. Tester les hypothèses

`VAN = Σ FCF_t/(1+r)^t`, y compris le flux initial à t=0. Le taux reflète le risque des flux. Une **sensibilité** fait varier une hypothèse à la fois ; un **scénario** fait varier plusieurs paramètres ensemble ; le **seuil de rentabilité** cherche la valeur d'une hypothèse pour laquelle la VAN est nulle. Ce sont des outils d'analyse, pas des garanties de prévision.

## Step 2 — Règles de décision

- Projet indépendant : accepter si **VAN > 0**, rejeter si < 0 ; à 0, indifférence financière. Les VAN de projets indépendants s'additionnent.
- Projets mutuellement exclusifs : retenir la **plus grande VAN positive**, et comparer aussi à l'option de ne rien faire.
- `TRI/IRR` : taux qui rend la VAN nulle. Pour un flux conventionnel (sortie initiale puis entrées) et un TRI unique, accepter si TRI > coût du capital. Cette règle peut s'inverser pour un projet de financement ; plusieurs changements de signe peuvent créer plusieurs TRI ou aucun. Ne pas classer deux projets exclusifs au seul TRI : taille, calendrier et risque comptent.
- TRI incrémental : calculer les flux du projet B moins A et étudier la VAN de cette différence. Les mêmes limites de TRI subsistent ; si risques différents, les taux pertinents ne sont pas forcément identiques.
- Payback : temps pour récupérer la mise initiale en flux non actualisés. Il ignore la valeur temps et les flux après le seuil ; ce n'est pas la règle de référence.
- En cas de ressource limitée, le cours définit `indice de profitabilité = VAN / quantité de ressource rare` (souvent investissement initial). Classer par indice décroissant aide, mais avec projets indivisibles ou contraintes multiples il faut comparer les **combinaisons** admissibles pour maximiser la VAN totale.
- Harmoniser fréquence et taux : pour un taux annuel effectif, `r_m = (1+r_annuel)^(1/12) − 1`. Pour une perpétuité croissante, `PV = FCF_1/(r−g)`, si r > g et hypothèses de croissance perpétuelle valides.

## Step 3 — Coût du capital et risque

- **CAPM / MEDAF** : `rE = rf + βE × (E[Rm] − rf)`. Le bêta mesure la sensibilité au risque de marché ; la volatilité mesure le risque total. Un titre plus volatil n'a pas nécessairement le bêta ni le coût des fonds propres le plus élevé.
- Bêta estimé par la pente de la régression des rendements excédentaires du titre sur ceux du marché ; alpha est l'ordonnée à l'origine. Les estimations historiques sont incertaines ; l'indice de marché est une approximation. Utiliser plusieurs comparables quand possible.
- Le rendement actuariel promis d'une dette (*YTM*) dépasse son rendement attendu en présence d'un risque de défaut. Pour un modèle simplifié : `rD ≈ YTM − probabilité de défaut × perte en cas de défaut` ; la définition exacte de la perte et les hypothèses de l'énoncé comptent. On peut aussi utiliser `rD = rf + βD × prime de marché`.
- Choisir un taux selon le **risque du projet**, pas automatiquement celui de l'entreprise entière. Pour les comparables sans trésorerie excédentaire, `βU = E/(D+E) × βE + D/(D+E) × βD` en valeurs de marché, dans le cadre sans impôt utilisé pour le portefeuille d'actifs. Avec cash, isoler les actifs opérationnels : `βop = (EβE + DβD − CβC)/(E+D−C)` ; ne pas confondre avec une approximation par dette nette.
- Un levier opérationnel plus élevé (plus de coûts fixes, à risque des ventes comparable) amplifie la sensibilité des profits et peut accroître le bêta.
- `WACC = E/(D+E) × rE + D/(D+E) × rD × (1−T)` si intérêts déductibles, avec poids de marché et politique de financement adaptée. Sans impôt, supprimer `(1−T)`. Ne pas actualiser un flux non endetté au seul coût des fonds propres endettés.

## Step 4A — Structure financière en marché parfait

Hypothèses de Modigliani–Miller : pas d'impôts ni coûts de transaction ou de détresse, information et accès aux marchés parfaits, titres correctement évalués. Pour des actifs et une politique d'investissement donnés :

- **Proposition I** : `VL = VU = D + E` : la dette partage différemment les flux et le risque, elle ne crée pas de valeur en elle-même. L'investisseur peut reproduire son levier personnellement (*homemade leverage*).
- **Proposition II, sans impôt** : `rE = rU + (D/E)(rU − rD)` et `rU = [E rE + D rD]/(D+E)`. Le risque et le rendement exigé des actions augmentent avec le levier ; le WACC sans impôt reste égal à rU dans ce cadre. Si la dette est risquée, conserver rD et βD : ne pas utiliser une formule supposant βD = 0 sans justification.
- Bilan en valeur de marché : `valeur d'entreprise opérationnelle = E + D − trésorerie excédentaire`. L'augmentation du bénéfice par action après un rachat financé par dette ne prouve pas une hausse du cours : le risque par action augmente aussi. Une émission d'actions au juste prix ne détruit pas de valeur mécaniquement.

## Step 4B — Dette et fiscalité

- `Résultat net = (EBIT − intérêts) × (1−T)` sous les hypothèses fiscales simples. `Bouclier fiscal des intérêts = T × intérêts` si l'entreprise utilise pleinement la déduction. Le remboursement du principal n'est pas déductible.
- **APV** : `VL = VU + valeur actuelle des boucliers fiscaux` si aucun autre effet du financement. Actualiser chaque bouclier au taux correspondant à son risque. Pour une dette D permanente, taux d'impôt constant, intérêts et bouclier utilisables à perpétuité et risque/taux de bouclier cohérents avec ceux de la dette : `PV(bouclier) = T × D`. Ce raccourci n'est pas général.
- Si la dette est ajustée à un ratio cible, valoriser les FCF par le WACC après impôt sous les hypothèses appropriées ; comparer à VU pour isoler l'avantage fiscal. **Ne pas ajouter à nouveau** le bouclier à une valeur déjà obtenue au WACC après impôt.
- Fiscalité personnelle : l'avantage relatif de la dette est `T* = 1 − [(1−Tc)(1−Te)/(1−Ti)]`, où Te est le taux personnel effectif sur actions et Ti celui sur intérêts. Il peut être inférieur à Tc, nul ou négatif.
- Plus de dette n'apporte pas nécessairement plus d'économie utilisable : revenus imposables, plafonds légaux et pertes peuvent limiter la déduction. La détresse et les conflits d'agence complètent l'analyse.

## Step 5 — Prudence avec la dette : détresse et incitations

- **Défaut** : incapacité à honorer les obligations ; ce n'est pas automatiquement une destruction de valeur totale. Un transfert de richesse entre créanciers et actionnaires n'est pas à lui seul un coût collectif. Les coûts directs (avocats, procédures) et indirects (perte de clients, fournisseurs, salariés, investissements) détruisent de la valeur, parfois avant toute faillite.
- **Trade-off** : `VL ≈ VU + PV(avantages fiscaux) − PV(coûts de détresse) ± effets d'agence`. Dette optimale lorsque son bénéfice marginal compense son coût marginal ; elle dépend notamment de la stabilité des flux, des actifs et des opportunités de croissance.
- **Risk shifting / asset substitution** : responsabilité limitée incite des actionnaires très endettés à choisir des projets trop risqués, dont une partie des pertes est supportée par les créanciers.
- **Debt overhang / sous-investissement** : un projet à VAN positive peut être refusé si l'essentiel du gain revient aux créanciers existants alors que les actionnaires financent le coût. Paiements excessifs aux actionnaires et endettement supplémentaire peuvent aussi transférer de la valeur aux dépens des créanciers.
- Covenants, surveillance et maturité de la dette peuvent limiter les conflits, mais réduisent la flexibilité et ont un coût. À l'inverse, une dette raisonnable peut discipliner les dirigeants, limiter le gaspillage de free cash flow et maintenir la concentration du capital. Une entreprise mature à flux stables peut généralement supporter davantage de dette qu'une entreprise de R&D risquée.

## Sources et périmètre

Supports du dépôt : [Introduction](../../Capital%20budgeting%20Introduction%20%284%29.pptx), [Step 1](../../Capital%20budgeting%20Step%201%20%283%29.pptx), [Step 2](../../Capital%20budgeting%20Step%202%20%282%29.pptx), [Step 3](../../Capital%20budgeting%20Step%203.pptx), [Step 4A](../../Capital%20budgeting%20Step%204A.pptx), [Step 4B](../../Capital%20budgeting%20Step%204B.pptx), [Step 5](../../Capital%20budgeting%20Step%205.pptx). Deux fichiers Step 4A sont identiques. Les supports et la capture décrivent des modalités d'examen différentes : vérifier les modalités actuelles sur K2.
