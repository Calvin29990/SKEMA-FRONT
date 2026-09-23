# Arsenal des 12 entretiens
## Cours complet, dictionnaire, stratégies et réponses types

> **Ce document se suffit à lui-même.** Aucun terme n'y est employé sans avoir
> été défini au moins une fois. Il est conçu pour être lu en entier une fois,
> puis relu par morceaux : **un mini-cours d'une page avant chaque appel**.
>
> **Structure :**
> **Partie 1** — le dictionnaire : tout ce qu'on suppose que tu sais.
> **Partie 2** — les stratégies : quoi faire quand tu ne sais pas.
> **Partie 3** — les 12 entretiens : un mini-cours + 12 questions-réponses.
> **Partie 4** — la fiche de survie.

---

# PARTIE 1 — LE DICTIONNAIRE

## 1.1 Les mots de l'organigramme

Ce sont les mots qui te feront passer pour un connaisseur ou pour un
touriste, et ils n'ont rien de technique. **Ce sont juste des noms de boîtes.**

### La banque, de haut en bas

**BFI** (Banque de Financement et d'Investissement). En anglais **CIB**,
*Corporate & Investment Bank*. C'est la partie de la banque qui travaille avec
les **entreprises** et les **institutions**, jamais avec les particuliers.

Dans la BFI, deux grands blocs :

**① Global Banking** — le conseil et le crédit. Fusions-acquisitions, émission
d'actions, émission d'obligations, prêts. **Pas de salle de marché.**

**② Global Markets** — la salle de marché. C'est là que tu veux aller.

### Dans Global Markets : les deux moitiés

🔑 **C'est LE découpage à ne jamais rater.**

**FIC** ou **FICC** — *Fixed Income, Currencies (and Commodities)*.
En français : **taux, change (et matières premières)**.
On y trouve : les obligations, les swaps de taux, le change, l'or, le pétrole.

**Equity** — les **actions** et tout ce qui en dérive.
On y trouve : les actions elles-mêmes, les options sur actions, les produits
structurés sur indices, le prêt-emprunt de titres.

| Si on te dit... | C'est... |
|---|---|
| FIC / FICC | Taux + change (+ matières premières) |
| Equity | Actions |
| **Global Markets** | **Les deux réunis** |
| Rates | Taux uniquement |
| Credit | Obligations d'entreprise uniquement |
| FX / Forex | Change uniquement |
| EQD | Equity Derivatives = dérivés actions |

> 🚨 **L'erreur éliminatoire :** dire « Global Markets » quand on parle de FIC,
> ou l'inverse. Deutsche Bank a fait **2 614 M€ en FIC** au T2 2026 — pas en
> Global Markets, qui est plus large. Confondre les deux devant un
> professionnel te sort du processus en une phrase.

### Les trois métiers du desk

**Sales.** Il parle aux clients. Il reçoit une demande, va chercher un prix
auprès du trader, ajoute sa marge, renvoie le prix, exécute. **Il ne porte pas
de risque de marché.** Il est payé sur le volume de flux et la marge.

**Trader.** Il donne les prix et **porte le risque**. Quand le sales vend une
option à un client, c'est le trader qui se retrouve avec la position en face et
qui doit la gérer.

**Structureur.** Il conçoit les produits sur mesure. Il travaille en amont du
sales : quand un client a un besoin que les produits standards ne couvrent pas,
le structureur assemble.

> 🗣️ **La phrase à connaître par cœur :**
> *« Le trader porte le risque, le sales porte la relation, le structureur crée
> le produit. »*

### Les autres mots d'organigramme

**Front office** — ceux qui parlent au marché ou au client : sales, traders,
structureurs. **Middle office** — contrôle, validation, suivi des positions.
**Back office** — règlement-livraison, comptabilité. **Trade support** — le
pont entre front et back : il s'assure que ce qui a été traité est
correctement enregistré.

**Buy-side / sell-side.** Le **sell-side**, c'est la banque : elle fabrique et
vend des produits. Le **buy-side**, c'est le client institutionnel : fonds,
assureurs, gérants. Ils achètent. **Tu postules côté sell-side.**

---

## 1.2 Les mots du produit

### L'option, depuis zéro

Une **option** est un **droit**, pas une obligation. C'est toute la différence
avec un contrat à terme.

**Call** = droit d'**acheter**. **Put** = droit de **vendre**.
**Strike** (prix d'exercice) = le prix fixé d'avance auquel on pourra acheter
ou vendre. **Prime** = ce qu'on paie pour avoir ce droit. **Maturité** ou
**échéance** = la date limite.

**Européenne** : exerçable **uniquement** à l'échéance.
**Américaine** : exerçable **à tout moment** jusqu'à l'échéance.

**Dans la monnaie** (*in the money*) : exercer serait rentable aujourd'hui.
**À la monnaie** (*at the money*, ATM) : le strike est égal au cours actuel.
**En dehors de la monnaie** (*out of the money*, OTM) : exercer n'aurait pas
de sens aujourd'hui.

### Le sous-jacent

Le **sous-jacent** est ce sur quoi porte l'option : une action, un indice, une
paire de devises, un taux. Une option n'existe jamais seule, elle est toujours
« sur » quelque chose.

### La volatilité — le mot le plus important du métier

La **volatilité** mesure l'ampleur des variations de prix. Elle s'exprime en
pourcentage annuel. Une volatilité de 20 % signifie, en gros, que le sous-jacent
bouge de 20 % par an en ordre de grandeur.

**Deux volatilités différentes, et il faut savoir les distinguer :**

**Volatilité réalisée** (ou historique) : ce que le marché **a fait**. On la
calcule sur les cours passés. C'est un constat.

**Volatilité implicite** : ce que le marché **anticipe**. On ne la calcule pas
sur les cours, on l'**extrait du prix des options**. Si une option se paie
cher, c'est que le marché anticipe beaucoup de mouvement.

> 🔑 **L'idée à retenir : le prix d'une option EST une volatilité.** Sur un desk
> d'options, on ne dit pas « cette option vaut 5 euros », on dit « elle se
> traite à 22 de vol ». C'est la même information.

**La conversion à connaître :** volatilité journalière = volatilité annuelle
divisée par la racine de 252 (le nombre de jours de bourse dans l'année).
Une volatilité de **13 % par an** donne **0,82 % par jour**.

### Smile et skew — enfin expliqués

Voici le point que tu m'as dit ne pas maîtriser. Prenons-le lentement.

**Le problème de départ.** Le modèle de Black-Scholes suppose qu'il existe
**une seule volatilité** pour un sous-jacent donné. Une action aurait « sa »
volatilité, point.

**Ce qu'on observe en réalité.** Si on prend toutes les options sur la même
action, à la même échéance, mais à des strikes différents, et qu'on calcule
pour chacune la volatilité implicite que le marché lui attribue — **on ne
trouve pas le même chiffre.**

**Le smile.** Quand on trace ces volatilités implicites en fonction du strike,
la courbe n'est pas plate : elle est plus haute sur les côtés (strikes bas et
strikes élevés) que au milieu (à la monnaie). **Ça dessine un sourire.** D'où
le nom.

**Le skew.** C'est **l'asymétrie** de ce sourire. Dans la vraie vie, le sourire
n'est presque jamais symétrique : un côté est plus haut que l'autre.

**Sur les actions, le skew est très marqué du côté des puts.** Les options de
protection à la baisse coûtent nettement plus cher que les options de hausse
équivalentes.

> 🗣️ **Pourquoi ? La réponse à donner :**
> *« Parce que les krachs sont à la baisse, pas à la hausse. Une action peut
> perdre 30 % en une séance, elle ne les gagne jamais en une séance. Le marché
> paie donc cher la protection à la baisse. On date souvent ce phénomène
> d'après le krach de 1987. »*

**Sur le change, c'est différent.** Il n'y a pas de « côté krach » évident :
quand l'euro baisse, le dollar monte, c'est symétrique par construction. Le
skew y dit plutôt **quelle direction fait peur sur cette paire précise**. Sur
les devises émergentes, il est asymétrique du côté de la dépréciation locale.

**L'indice SKEW.** C'est un indice publié par le CBOE qui mesure justement
cette asymétrie sur le S&P 500. Quand il est élevé, le marché paie cher la
protection. Mi-septembre 2026, il est autour de **146-152** : très élevé.

**La surface de volatilité.** Si on ajoute une troisième dimension — la
maturité — on obtient une surface : une volatilité implicite par couple
(strike, échéance). C'est ce que gère un desk d'options.

### Les grecs — les cinq sensibilités

Un **grec** mesure la sensibilité du prix d'une option à un paramètre. On les
appelle comme ça parce qu'on les note par des lettres grecques.

| Grec | Sensibilité à | En une phrase |
|---|---|---|
| **Delta** | le sous-jacent | La quantité à couvrir. Un call à la monnaie est vers 0,50 |
| **Gamma** | la variation du delta | Fort près du strike et près de l'échéance |
| **Vega** | la volatilité | Maximum à la monnaie, augmente avec la maturité |
| **Thêta** | le temps qui passe | Négatif pour l'acheteur, positif pour le vendeur |
| **Rhô** | le taux d'intérêt | **En change il y en a deux**, un par devise |

**Le delta expliqué.** Si le delta vaut 0,45, une hausse de 1 euro du
sous-jacent fait monter l'option de 0,45 euro. C'est donc **la quantité de
sous-jacent qu'il faut détenir pour être couvert** : pour 100 options, je
détiens 45 actions.

**Le gamma expliqué.** Le delta ne reste pas constant : il change quand le
sous-jacent bouge. Le gamma mesure cette variation. **Conséquence pratique :
une couverture en delta doit être refaite en permanence.**

> 🔑 **La relation à connaître absolument :**
> *« Gamma et thêta sont les deux faces d'une même pièce. Être long gamma,
> c'est être payé pour rebalancer sa couverture quand le marché bouge — et ce
> privilège se paie en thêta chaque jour. »*

**Les grecs de deuxième ordre** (pour les desks exotiques) :
**Vanna** = sensibilité du delta à la volatilité.
**Volga** = sensibilité du vega à la volatilité.
**Charm** = variation du delta avec le temps qui passe.

### Black-Scholes et Garman-Kohlhagen

**Black-Scholes-Merton** est le modèle standard de valorisation d'une option.
Il donne un prix à partir de cinq paramètres : cours du sous-jacent, strike,
taux sans risque, volatilité, temps restant.

**Ses hypothèses, et pourquoi elles sont fausses :**
- Volatilité **constante** → faux, c'est tout le smile.
- Rendements **log-normaux** → faux, les queues de distribution sont plus
  épaisses dans la réalité (les événements extrêmes sont plus fréquents que le
  modèle ne le prévoit).
- **Pas de coûts de transaction** → faux.
- Couverture **en continu** possible → faux, on rebalance à intervalles.

**Garman-Kohlhagen** est l'adaptation de Black-Scholes au **change**. La seule
différence conceptuelle : il y a **deux taux sans risque**, un par devise. La
devise étrangère se comporte comme une action versant un dividende continu égal
à son taux d'intérêt.

**Les valeurs de référence à connaître.** Avec S = 100, K = 105, r = 3 %,
volatilité 25 %, échéance 0,5 an :

| | Valeur |
|---|---|
| Call | **5,5760** |
| Put | **9,0127** |
| Delta du call | **0,4591** |
| Gamma | **0,0224** |
| Vega (pour 1 point de vol) | **0,2806** |
| Thêta par jour | **−0,0225** |

**N(d1) et N(d2).** Ce sont deux quantités qui apparaissent dans la formule.

> ⚠️ **Ne les inverse jamais :**
> **N(d2) est la probabilité d'exercice** en univers risque-neutre.
> **N(d1) est le delta**, donc le ratio de couverture.
> Beaucoup de supports d'étudiants confondent les deux, et un trader corrige
> systématiquement.

**La parité call-put.** C'est une **relation d'arbitrage**, pas un modèle :

```
C − P = S − K × e^(−rT)
```

Elle ne dépend d'**aucune** hypothèse sur la volatilité. Si elle est violée, il
y a de l'argent gratuit à prendre. Vérification sur les chiffres ci-dessus :
5,5760 − 9,0127 = **−3,4368**, et 100 − 105 × e^(−0,015) = **−3,4368**.

---

## 1.3 Les mots du marché

**Spot** (ou comptant) : le prix pour une livraison immédiate.
**Forward** (ou terme) : le prix fixé aujourd'hui pour une livraison future.

**De gré à gré** (*OTC*, over-the-counter) : contrat bilatéral, sur mesure,
négocié directement entre deux parties. **Risque de contrepartie** : si l'autre
fait faillite, on perd.

**Coté** (ou *listed*) : contrat standardisé, échangé sur un marché organisé,
avec une **chambre de compensation** qui s'interpose entre acheteur et vendeur.
Chacun fait face à la chambre, pas à l'autre. **Le risque de contrepartie
bilatéral disparaît.**

**Appel de marge.** Sur un marché coté, on dépose une **marge initiale** au
départ, puis on règle chaque jour la variation de valeur : c'est la **marge de
variation**. On ne peut donc pas accumuler une perte cachée.

**Roll.** Un contrat à terme a une échéance. Pour garder la position, il faut
la reporter sur l'échéance suivante : c'est le roll. **Base** : l'écart entre
le prix du contrat et celui du sous-jacent.

**RFQ** (*request for quote*) : le client demande un prix. **Streaming** : la
banque diffuse des prix en continu, sans qu'on les demande.
**Hit ratio** : la part des prix cotés qui se transforment en transactions.
**Internaliser** : croiser deux flux clients en interne sans passer par le
marché — c'est très rentable.
**Last look** : le droit, pour le teneur de marché, de vérifier une dernière
fois avant d'exécuter.
**Market impact** : l'effet de mon propre ordre sur le prix.
**Spread** : l'écart entre le prix d'achat et le prix de vente. C'est la
rémunération du teneur de marché.

**Pip.** L'unité de cotation d'une paire de devises : la 4ᵉ décimale en
général, la 2ᵉ sur les paires en yen. **Ordre de grandeur : 0,5 pip sur
10 millions d'EUR/USD vaut 500 dollars.**

**Point de base** (*basis point*, bp) : un centième de pour cent, soit 0,01 %.
Le langage standard des taux.

---

## 1.4 Les mots du risque

**VaR** (*Value at Risk*) : la perte maximale attendue sur un horizon donné, à
un niveau de confiance donné. « VaR 1 jour à 99 % de 2 millions » signifie :
dans 99 % des cas, la perte d'une journée ne dépassera pas 2 millions.

**Ses limites** : elle ne dit rien de ce qui se passe **au-delà** du seuil ;
elle suppose une stabilité des corrélations qui disparaît précisément en crise ;
elle est calibrée sur le passé.

**Expected shortfall** : la moyenne des pertes **dans la queue**, au-delà du
seuil de VaR. Introduite justement pour combler le premier défaut.

**Stress test** : au lieu de faire une statistique, on applique un scénario
choisi — « et si le marché baisse de 20 % et que les corrélations passent à
1 ? »

**Drawdown** : la perte depuis le plus haut atteint. **Ratio de Sharpe** : le
rendement en excès du taux sans risque, divisé par la volatilité. Il mesure le
rendement par unité de risque. *Se prononce « charp ».*

---

## 1.5 Les mots des taux

**Obligation** : un titre de dette. L'émetteur emprunte, verse des **coupons**
périodiques, rembourse le **nominal** à l'échéance.

**Rendement à maturité** (*yield*) : le taux qui égalise la valeur actuelle des
flux futurs et le prix du titre. **Sa limite** : il suppose que les coupons
sont réinvestis à ce même taux, ce qui n'arrive quasiment jamais.

**Relation fondamentale : quand les taux montent, le prix des obligations
baisse.** Un titre ancien à 3 % devient moins attractif si le marché offre 4 %,
donc son prix chute jusqu'à ce que son rendement rejoigne 4 %.

**Duration de Macaulay** : la durée moyenne pondérée des flux, en années.
**Duration modifiée** : la variation de prix en pourcentage pour une variation
de 1 % du taux.
**DV01** : la variation de valeur en **monnaie**, pour **1 point de base**.

```
DV01 = Nominal × Duration modifiée × 0,0001
```

> 🔑 **Pourquoi le DV01 est la mesure reine :** c'est **la seule des trois qui
> s'additionne**. On ne peut pas additionner la duration d'une obligation et
> celle d'un swap, les nominaux diffèrent. Les DV01 sont tous en euros par
> point de base : **c'est la monnaie commune du risque de taux.**

**Convexité.** La duration suppose une relation **linéaire** entre prix et taux.
En réalité la relation est **courbe**. La convexité mesure cette courbure.

**Conséquence pratique :** pour un petit mouvement, la duration suffit. Pour un
choc de 100 points de base, elle **sous-estime le gain et surestime la perte**.
**La convexité est un ami de l'acheteur d'obligations.**

**Convexité négative** : certains titres l'ont à l'envers. Une obligation
*callable* (que l'émetteur peut rembourser par anticipation) voit ses gains
plafonnés quand les taux baissent, parce que l'émetteur rembourse et refinance.

**Courbe des taux** : les taux en fonction de la maturité.
**Pentue** : le long rapporte plus que le court — situation normale.
**Plate** : peu d'écart. **Inversée** : le court rapporte plus que le long.

**Swap de taux** (*IRS*) : échange d'un taux fixe contre un taux variable sur
un nominal donné. Le nominal n'est jamais échangé, seuls les intérêts le sont.
**Jambe fixe** et **jambe variable**.

**Cap** : une option qui plafonne un taux variable. **Floor** : qui le plancher.
**Collar de taux** : achat d'un cap financé par la vente d'un floor.
**Swaption** : une option sur un swap.

**Spread de crédit** : le supplément de rendement qu'une obligation d'entreprise
offre au-dessus d'un titre d'État de même maturité. Il rémunère le risque de
défaut.

**CDS** (*credit default swap*) : un contrat d'assurance contre le défaut d'un
émetteur. L'acheteur de protection paie une prime périodique ; si le défaut
survient, il est indemnisé.

**MOVE** : l'indice de volatilité du marché des taux américains. L'équivalent
du VIX pour les obligations.

---

## 1.6 Les mots du change

**Cotation.** Une paire s'écrit **base / cotée**. Sur EUR/USD = 1,1700, l'euro
est la base, le dollar la cotée : un euro vaut 1,17 dollar. **Quand la paire
monte, la base s'apprécie.**

**Cours à terme.** Ce n'est **pas une prévision** : c'est mécaniquement le
comptant corrigé de l'écart de taux entre les deux devises.

```
F = S × (1 + taux cotée × t) / (1 + taux base × t)
```

> 🔑 **La devise au taux le plus élevé part en déport** (elle vaut moins cher à
> terme). Si ce n'était pas le cas, il y aurait un arbitrage sans risque.

**Swap de change** : achat au comptant et vente à terme simultanés (ou
l'inverse). **Ce n'est pas une position directionnelle** : c'est un outil de
trésorerie, on déplace une date de valeur.

**NDF** (*non-deliverable forward*) : un terme réglé **en différence**, en
dollars, sans jamais livrer la devise locale. Il existe parce que certaines
devises ne sont pas librement livrables hors de leur pays.

```
Paiement = Nominal × (Forward − Fixing) / Fixing
```

⚠️ **On divise par le fixing**, pas par le forward.

**Fixing** : un cours de référence officiel, publié à heure fixe, utilisé pour
dénouer les contrats.

---

## 1.7 Les mots des produits structurés

Un **produit structuré** est un titre qui combine une composante obligataire et
une ou plusieurs options, pour offrir un profil de gain sur mesure.

**Autocall.** Un produit qui se **rappelle automatiquement** (*auto-call*) si
le sous-jacent est au-dessus d'un seuil à une date de constatation. Le client
récupère alors son capital plus un coupon, et le produit s'arrête.

**Phoenix.** Une variante qui verse un coupon à chaque constatation où le
sous-jacent est au-dessus d'une **barrière de coupon**, même si le produit ne
se rappelle pas.

**Coupon à effet mémoire.** Si une constatation passe sous la barrière, le
coupon n'est pas versé — mais il n'est pas perdu : il est **mis en mémoire** et
sera versé en totalité à la première constatation qui repasse au-dessus.

**Barrière de protection du capital.** Le niveau en dessous duquel le client
commence à perdre du capital à l'échéance. Une barrière à 60 % signifie : tant
que le sous-jacent ne descend pas sous 60 % de son niveau initial, le capital
est remboursé intégralement.

**Worst-of.** Un produit indexé non pas sur un sous-jacent mais sur **le moins
performant d'un panier**. Plus risqué, donc mieux rémunéré.

**Reverse convertible.** Un produit à coupon élevé où, si le sous-jacent baisse
sous un seuil, le client est remboursé en actions au lieu d'espèces.

**Variance swap** : un contrat qui permet de prendre position directement sur
la volatilité réalisée, sans passer par des options.

**Dispersion** : une stratégie qui joue l'écart entre la volatilité d'un indice
et celle de ses composantes. Elle revient à prendre position sur la corrélation.

**Term sheet** : la fiche descriptive du produit — sous-jacent, dates,
barrières, coupons, conditions de rappel. C'est le document commercial de
référence.

---

## 1.8 Les mots de la finance islamique

**Riba** : l'intérêt. Interdit.
**Gharar** : l'incertitude excessive dans un contrat. Interdit.
**Maysir** : la spéculation pure, le jeu de hasard. Interdit.

**Sukuk** : souvent traduit par « obligation islamique », mais ce n'est pas une
obligation. Le porteur détient **une part de propriété dans un actif réel** et
perçoit une quote-part des revenus de cet actif — pas un intérêt.

**Murabaha** : une vente à coût majoré. La banque achète le bien et le revend
au client avec une marge connue d'avance, payable à terme.

**Ijara** : un crédit-bail. La banque achète et loue.

**Sharia board** : le comité de conformité religieuse qui valide les produits.

---

# PARTIE 2 — LES STRATÉGIES

## 2.1 Le principe du couloir

Un entretien n'est pas un examen : **personne ne coche une liste**. Celui qui
pose les questions oriente la conversation. Si tu subis, on te promène sur tout
le programme. Si tu proposes un terrain, on y va — **parce que ton
interlocuteur aussi préfère parler de ce qu'il connaît bien.**

> ⚠️ **La règle de sécurité.** Un chiffre posé dans le couloir doit survivre à
> la question suivante : *« ah bon, et ça vient d'où ? »*. Si tu ne peux pas
> répondre, **ne pose pas le chiffre** — tu viens d'inviter ton interlocuteur à
> creuser exactement là où tu es faible. Le couloir se construit avec **peu de
> chiffres, tous solides.**

## 2.2 Les trois temps du couloir

**① La trace.** Une chose que tu as réellement faite, en une phrase.
**② Le chiffre.** Un seul, vérifiable, qui plante le décor.
**③ La question ouverte.** Qui rend la parole et installe le sujet.

**Exemple complet :**

> « J'ai construit un pricer Black-Scholes pour comprendre ce qu'il y a
> derrière un prix. Quand j'ai vu que l'equity a fait plus 43 % chez vous au
> deuxième trimestre pendant que le FICC était à moins 0,4 %, je me suis
> demandé si ça venait de la demande client ou des conditions de marché. Vous
> le voyez comment, de là où vous êtes ? »

Trois phrases, et **le sujet est maintenant l'equity structuré** — un terrain
que tu as préparé.

## 2.3 Les six manœuvres de récupération

Voici quoi faire, concrètement, selon la situation.

### Manœuvre 1 — L'aveu et le pont

**Quand :** on te pose une question technique dont tu ignores la réponse.

> « Je ne l'ai pas pratiqué. Ce que j'en comprends, c'est [deux phrases
> maximum]. Ce que je voudrais qu'on m'apprenne, c'est [une chose précise].
> En revanche, là où j'ai vraiment mis les mains, c'est [ta trace]. »

🔑 **Trois éléments obligatoires :** l'aveu franc, une amorce de compréhension,
**une question précise**. La question précise est ce qui prouve que tu as
réfléchi au sujet même sans le maîtriser.

### Manœuvre 2 — La montée d'un cran

**Quand :** la question est trop technique, mais tu comprends l'enjeu
économique derrière.

> « Je ne saurais pas vous le calculer. Mais je comprends pourquoi c'est un
> sujet : [l'enjeu en une phrase]. »

**Exemple.** On te demande de calculer un vanna. Tu réponds :
> « Je ne saurais pas le calculer. Mais je comprends l'enjeu : ça veut dire que
> ma couverture en delta se dégrade quand la volatilité bouge, donc je ne peux
> pas gérer delta et vega séparément. »

**Tu as perdu le calcul, tu as gagné le raisonnement.** C'est souvent suffisant
pour un stagiaire.

### Manœuvre 3 — Le pivot par analogie

**Quand :** la question porte sur une classe d'actifs que tu ne connais pas,
mais dont la mécanique ressemble à une que tu connais.

> « Je ne l'ai pas vu sous cet angle, mais la logique me paraît proche de
> [ce que tu connais]. Est-ce que la comparaison tient ? »

**Exemples de ponts utilisables :**

| Inconnu | Ton pont |
|---|---|
| Barrière sur actions | « C'est la même logique qu'un knock-out en change » |
| Convexité obligataire | « C'est du gamma appliqué aux taux » |
| Skew commodities | « Comme le skew actions, mais inversé : c'est la pénurie qui fait peur » |
| Corrélation worst-of | « C'est de la dispersion, donc de la vol relative » |
| Spread de crédit | « C'est le prix du risque de défaut, comme une prime d'assurance » |

⚠️ **Termine toujours par une question.** L'analogie proposée sans question
ressemble à une affirmation — et si elle est fausse, tu l'as affirmée.

### Manœuvre 4 — Le retour au client

**Quand :** on te pousse sur la technique et tu sens que tu vas caler.

> « Sur la mécanique je serais moins précis que vous. Ce qui m'intéresse, c'est
> le besoin en face : pourquoi un client demande ça plutôt qu'autre chose ? »

**Pourquoi ça marche :** c'est **exactement** la bonne question pour un poste
de sales. Tu ne fuis pas, tu recentres sur ta valeur ajoutée réelle.

### Manœuvre 5 — L'ancrage sur ta trace

**Quand :** un blanc, une question trop vague, ou tu as besoin de reprendre
pied.

> « Est-ce que je peux vous donner un exemple concret de ce que j'ai fait ? »

**Personne ne refuse.** Et tu reprends la main sur un terrain que tu maîtrises
à 100 % : ShockDesk, le pricer, BQL chez BPCE.

### Manœuvre 6 — Le chiffre qui plante le décor

**Quand :** tu veux installer un sujet dès le début.

Tu poses **un** chiffre vérifié, puis une question ouverte. Le sujet est
installé pour les dix minutes suivantes.

> ⚠️ **Un seul chiffre par prise de parole, et jamais deux fois le même chiffre
> dans un entretien.** Répéter, c'est avouer qu'on n'en a qu'un.

## 2.4 Les cinq réflexes

**① Conclusion d'abord.** On répond, puis on explique. Jamais l'inverse.
**② Un chiffre par réponse.** Un seul. Deux, c'est un étalage ; zéro, c'est du
vent.
**③ « Je » et pas « on ».** « J'ai construit », pas « on a fait ».
**④ Trancher, puis nuancer.** « Oui, mais » — jamais « ça dépend » tout seul.
**⑤ Finir net et se taire.** Celui qui rajoute une phrase de trop annule celle
d'avant.

## 2.5 Ce qui élimine vraiment

| Faute | Pourquoi c'est grave |
|---|---|
| **Bluffer** | Un professionnel le détecte en trois secondes. C'est son métier |
| **Confondre FIC et Global Markets** | Montre qu'on n'a pas lu les résultats |
| **Présenter un backtest comme réel** | Question d'honnêteté, pas de technique |
| **Parler de trading perso** | Vocabulaire retail, pas sell-side |
| **Répondre plus de 30 secondes** | On décroche |
| **Ne poser aucune question** | Signal de désintérêt |

> 🔑 **« Je ne sais pas » n'élimine personne. Bluffer trente secondes de trop,
> si.**

## 2.6 L'alerte vocabulaire

| ❌ Ne dis jamais | ✅ Dis plutôt |
|---|---|
| « trader le Forex » | « exécuter un flux client », « couvrir une exposition » |
| « effet de levier » | « nominal », « notionnel » |
| « money management » | « limites de risque », « sizing » |
| « gagner sur le marché » | « capturer du spread », « hit ratio » |
| « analyse technique » | « positionnement », « flux », « niveaux suivis » |
| « développeur » | « j'automatise », « Python est un outil » |

**La phrase qui tue une candidature :** *« J'ai commencé à m'intéresser aux
marchés en tradant sur une plateforme. »*

---

# PARTIE 3 — LES 12 ENTRETIENS

## 3.0 Le contexte marché à connaître avant tout appel

**Vérifié au 18 septembre 2026 :**

| Fait | Détail |
|---|---|
| **Fed, 16 septembre** | **Première hausse depuis plus de trois ans**, jugée hawkish, dollar en hausse |
| **BCE, 10 septembre** | **+25 pb**, dépôt à **2,50 %**, effectif le 16 |
| **10 ans américain** | A **dépassé 5 %** le 15 septembre, puis reflux |
| **VIX** | **17,71** le 17, **15,44** le 18 — détente rapide |
| **SKEW** | **146-152**, très élevé |
| **MOVE** (vol de taux) | **76-81**, en baisse |
| **Pétrole** | Flambée début septembre, puis repli |

🔑 **La lecture que presque aucun étudiant ne fait :**

> « Ce que je trouve intéressant, c'est que la volatilité actions s'est
> détendue très vite après la Fed — le VIX est repassé sous 16 — alors que le
> SKEW reste autour de 146. Le marché est calme mais continue de payer cher la
> protection à la baisse. »

## 3.0 bis Le fait transversal du T2 2026

| Maison | Actions | FICC |
|---|---|---|
| **BNP Paribas** | Equity & Prime **1 406 M€, +43,2 %** (record) | **1 404 M€, −0,4 %** |
| **Natixis** | Equity **317 M€, +59 %**, dérivés **×2,5** | Global Markets total +16 % |
| **CACIB** | Banque d'investissement **+63,8 %** hors change | **Stable**, trésorerie en souffrance |
| **Deutsche Bank** | — | FIC **2 614 M€, +16 %** (record) |

> 🔴 **Les dérivés actions explosent partout en France pendant que le FICC
> stagne.** Ce n'est pas un hasard si 5 de tes 12 pistes sont en equity : **les
> desks qui recrutent sont ceux qui ont gagné de l'argent six mois plus tôt.**

---

## 🟦 ENTRETIEN 1 — Adam Cohen, Natixis, EQD & Structured Products Sales

### Mini-cours

**Qui il est.** Sales sur le desk dérivés actions et produits structurés de
Natixis, la BFI du groupe BPCE. Paris 13ᵉ. **Il cherche un stagiaire pour
décembre** et a proposé un appel.

**Ce que fait son desk.** Il conçoit et vend des produits structurés sur
actions à des banques privées, des distributeurs, des family offices et aux
réseaux BPCE — Caisses d'Épargne et Banques Populaires. Les produits : autocall,
Phoenix, reverse convertible. Les sous-jacents : Euro Stoxx 50, S&P 500,
CAC 40, et des paniers en worst-of.

**Le chiffre.** Au T2 2026, l'activité Equity de Natixis a fait **317 M€,
+59 %** sur un an, **les revenus des dérivés étant multipliés par 2,5**.

**La logique économique du desk, en une idée.** Un client veut du rendement
dans un monde où le rendement sans risque est faible. La banque lui en fabrique
en lui faisant **vendre de la volatilité** : le client encaisse une prime
d'option déguisée en coupon, et accepte en échange de porter le risque de
baisse au-delà d'une barrière. **Le desk gagne sur la structuration, pas sur la
direction du marché.**

**Le travail d'un stagiaire.** Pricing quotidien sur les pricers internes,
rédaction de term sheets et de fiches produits, suivi de vie des produits
(dates de constatation, barrières de rappel, coupons en mémoire),
automatisation Excel/VBA et Bloomberg.

**Ton avantage ici.** Tu as lu **Priour & Magne en entier** — un ouvrage écrit
du point de vue du conseiller qui distribue ces produits. C'est **exactement**
le client de ce desk. Et ton stage BPCE Assurances, c'est **le même groupe**.

**Ce que tu tais.** Le change, le LatAm, l'ENSAE.

### Ton accroche

> « J'ai vu que les revenus des dérivés actions ont été multipliés par 2,5 au
> deuxième trimestre. De l'extérieur on ne sait pas si ça vient du nombre de
> tickets ou de la taille des opérations — vous le voyez comment sur le desk ? »

### Les 12 questions

**1. Qu'est-ce qu'un autocall ? Explique-le comme à un client.**
> Un produit qui verse un coupon et se rembourse automatiquement par anticipation
> si le sous-jacent est au-dessus d'un seuil à une date de constatation. Le
> client échange un potentiel de hausse contre un coupon fixe, et porte le
> risque de baisse au-delà d'une barrière.

**2. Le client est acheteur ou vendeur de volatilité ?**
> Vendeur. Et vendeur de skew. Le coupon n'est pas un rendement, c'est une
> prime d'option : il vend un put à barrière.

**3. Pourquoi le coupon est-il élevé ?**
> Parce que la prime encaissée est grosse. Un coupon élevé n'est jamais un
> cadeau, c'est le prix d'un risque que le client accepte de porter.

**4. Différence entre un autocall et un Phoenix ?**
> L'autocall paie quand il se rappelle. Le Phoenix paie un coupon à chaque
> constatation au-dessus de la barrière de coupon, même sans rappel.

**5. Qu'est-ce qu'un coupon à effet mémoire ?**
> Un coupon manqué n'est pas perdu : il est mis en mémoire et versé en totalité
> à la première constatation qui repasse au-dessus de la barrière.

**6. Barrière à 60 %, le sous-jacent baisse de 30 % puis remonte. Que se
passe-t-il ?**
> Une baisse de 30 % met le sous-jacent à 70 %, donc au-dessus de la barrière
> de 60 %. Le coupon est payé normalement. La mémoire ne sert pas ici — elle ne
> se déclenche que sous 60 %.

⚠️ **C'est un piège arithmétique, pas un piège produit.** Prends deux secondes
avant de répondre.

**7. Qu'est-ce qu'un worst-of ?**
> Un produit indexé sur le moins performant d'un panier. Plus risqué, donc
> mieux rémunéré.

**8. Impact d'une baisse de corrélation implicite sur un worst-of ?**
> L'investisseur est vendeur de corrélation. Corrélation basse égale dispersion
> forte, donc plus de chances qu'un sous-jacent décroche : le put vendu vaut
> plus cher, ce qui permet d'afficher un coupon plus élevé.

**9. Qu'est-ce que le skew, et pourquoi il compte ici ?**
> L'asymétrie de la volatilité implicite entre les strikes. Sur les actions,
> les puts en dehors de la monnaie se paient plus cher, parce que les krachs
> sont à la baisse. Comme le client vend un put, il vend la partie la plus
> chère de la surface.

**10. Que se passe-t-il si le produit n'est jamais rappelé ?**
> Il va à l'échéance. Si le sous-jacent est au-dessus de la barrière de
> protection, le capital est remboursé. Sinon, le client subit la baisse.

**11. Qu'est-ce qu'un term sheet ?**
> La fiche descriptive du produit : sous-jacent, dates de constatation,
> barrières, coupons, conditions de rappel. C'est le document de référence
> commercial.

**12. Tes réflexes Excel et Bloomberg ?**
> Chez BPCE : requêtes BQL pour récupérer les séries, VBA pour la mise en forme
> et les contrôles. Le réflexe que je garde : une matrice de prix doit se
> régénérer sans intervention manuelle, sinon elle est fausse dès qu'un input
> bouge.

---

## 🟦 ENTRETIEN 2 — Maxime Fauchère-Collin, BNP Paribas, EQD Exotic Trading

### Mini-cours

**Qui il est.** Trader sur le desk exotiques dérivés actions de BNP Paribas
CIB. Centrale Lille et EDHEC. Il t'a proposé un appel le week-end prochain et
t'a dit de le tutoyer.

**Ce que fait son desk.** Il **porte le risque** des produits que les sales et
les structureurs vendent. Quand un client achète un autocall, quelqu'un se
retrouve avec la position inverse : c'est lui. Son métier est de couvrir cette
position en permanence, sur tous les grecs à la fois.

**Le chiffre.** Au T2 2026, Equity & Prime Services a fait **1 406 M€, +43,2 %**
— un record — pendant que le FICC faisait **1 404 M€, −0,4 %**.

**La difficulté de son métier, en une idée.** Sur une option vanille, on couvre
le delta et ça suffit à peu près. Sur un exotique, **les grecs interagissent** :
le delta change quand la volatilité bouge (c'est vanna), le vega change quand
la volatilité bouge (c'est volga). Près d'une barrière, le delta peut basculer
brutalement. **On ne peut pas gérer les risques séparément.**

**Ta stratégie ici, et elle est différente des autres.** Tu ne peux pas gagner
sur la technique — il en fait dix heures par jour. **Tu gagnes sur l'honnêteté
et la qualité de tes questions.** Un trader exotique respecte énormément un
junior qui dit « je ne sais pas » et pose la bonne question derrière. Ce qu'il
ne supporte pas, c'est le vernis.

**Ton avantage.** Tu as codé un pricer et calculé des grecs toi-même. C'est peu,
mais c'est réel, et beaucoup de candidats n'ont jamais écrit une ligne.

### Ton accroche

> « Sur un desk exotique, qu'est-ce qui prend le plus de temps : trouver le
> prix, ou gérer le risque une fois que le trade est fait ? »

### Les 12 questions

**1. Qu'est-ce qu'une option à barrière ?**
> Une option qui s'active ou se désactive si le sous-jacent touche un niveau.
> Knock-in : elle n'existe que si la barrière est touchée. Knock-out : elle
> disparaît si elle l'est.

**2. Pourquoi une knock-out est-elle moins chère qu'une vanille ?**
> Parce qu'elle peut disparaître. On paie moins pour un droit qui peut
> s'éteindre.

**3. Pourquoi le gamma est-il dangereux près d'une barrière ?**
> Parce que le delta peut basculer brutalement quand le spot approche du
> niveau. La couverture doit être ajustée très vite, et l'ajustement lui-même
> coûte cher.

**4. Qu'est-ce que vanna ? Volga ?**
> Vanna, c'est la sensibilité du delta à la volatilité. Volga, la sensibilité
> du vega à la volatilité. Je ne les ai pas manipulés en pratique. Ce que je
> comprends, c'est que ça veut dire qu'on ne peut pas gérer delta et vega
> séparément.

**5. Qu'est-ce qu'une option asiatique ?**
> Une option dont le payoff dépend de la moyenne du sous-jacent sur la période,
> pas du cours final.

**6. Pourquoi est-elle moins chère ?**
> Parce que la volatilité d'une moyenne est plus faible que celle du spot —
> d'un facteur racine de trois environ, soit à peu près 42 % de moins en
> moyenne géométrique. Ce n'est pas une remise, c'est mécanique.

**7. Qu'est-ce que le pin risk ?**
> Le risque, à l'échéance, que le sous-jacent finisse très près du strike : on
> ne sait pas si l'option sera exercée, donc on ne sait pas quelle position on
> aura le lendemain.

**8. Qu'est-ce qu'un variance swap ?**
> Un contrat qui permet de prendre position directement sur la volatilité
> réalisée, sans passer par un portefeuille d'options à rebalancer.

**9. Comment couvre-t-on le vega d'un panier ?**
> Je ne l'ai pas fait. Ce que je comprends, c'est que le vega de l'indice n'est
> pas la somme des vegas des composantes, à cause de la corrélation — donc la
> couverture laisse forcément un résidu de corrélation.

**10. Qu'est-ce que le smile ?**
> La volatilité implicite varie selon le strike au lieu d'être unique comme le
> suppose Black-Scholes. Tracée en fonction du strike, la courbe remonte des
> deux côtés.

**11. Quelles hypothèses de Black-Scholes sont fausses ?**
> Volatilité constante — c'est le smile. Rendements log-normaux — les queues
> sont plus épaisses. Couverture en continu — on rebalance à intervalles. Pas
> de coûts de transaction.

**12. Tu as codé quoi, exactement ?**
> Un pricer Black-Scholes avec les grecs, et un module de stress qui applique
> des chocs de courbe. Le résultat qui m'a le plus appris, c'est de voir le
> gamma exploser près de l'échéance.

---

## 🟦 ENTRETIEN 3 — Manon Giorgi, BNP Paribas, Cross-Asset Listed Derivatives Sales

### Mini-cours

**Qui elle est.** Sales sur les dérivés **listés** cross-asset chez BNP
Paribas. Elle t'a dit en juillet : *« on recrutera très certainement quelqu'un
en janvier 27, recontacte-moi en octobre »*.

**Ce que veut dire « listé ».** C'est le point central de cet entretien.
**Listé = coté sur un marché organisé**, avec une chambre de compensation qui
s'interpose entre acheteur et vendeur. Par opposition au **gré à gré**, où deux
parties contractent directement.

**Les trois différences à connaître :**

| | Listé | Gré à gré |
|---|---|---|
| Contrat | **Standardisé** | Sur mesure |
| Contrepartie | La **chambre de compensation** | L'autre partie |
| Règlement | **Appel de marge quotidien** | À l'échéance |

**Pourquoi ça change le métier.** Sur du listé, il n'y a **pas de risque de
contrepartie bilatéral** et pas de négociation des termes. Le sales ne vend pas
une structure sur mesure : il apporte de la **liquidité**, de l'**exécution** et
du **service** — meilleur prix, bonne échéance, gestion du roll.

**Cross-asset** signifie qu'elle couvre plusieurs classes d'actifs : futures et
options sur indices actions, sur taux, parfois sur matières premières.

**Le chiffre.** Equity & Prime Services **+43,2 %** au T2 2026, contre FICC
**−0,4 %**. Et le détail mémorable : **1 406 contre 1 404 millions** — les deux
moitiés de Global Markets à égalité parfaite.

### Ton accroche

> « Au deuxième trimestre, Equity & Prime Services a fait plus 43 % pendant que
> le FICC était à moins 0,4 % — 1 406 millions contre 1 404, les deux moitiés
> de Global Markets à égalité. Est-ce que ça se ressent dans la façon dont le
> desk est sollicité ? »

### Les 12 questions

**1. Différence entre listé et gré à gré ?**
> Le listé est standardisé, compensé par une chambre, avec appel de marge
> quotidien. Le gré à gré est sur mesure et bilatéral, avec un risque de
> contrepartie direct.

**2. À quoi sert une chambre de compensation ?**
> Elle s'interpose entre acheteur et vendeur. Chacun fait face à la chambre, pas
> à l'autre : le risque de contrepartie bilatéral disparaît.

**3. Qu'est-ce qu'un appel de marge ?**
> On dépose une marge initiale, puis on règle chaque jour la variation de
> valeur. C'est ce qui empêche d'accumuler une perte cachée.

**4. Qu'est-ce que le roll ?**
> Un contrat à terme a une échéance. Pour garder la position, on la reporte sur
> l'échéance suivante. C'est un moment de flux important et un sujet
> d'exécution à part entière.

**5. Qu'est-ce que la base ?**
> L'écart entre le prix du contrat à terme et celui du sous-jacent. Elle tend
> vers zéro à l'approche de l'échéance.

**6. Pourquoi un client choisit-il du listé plutôt que du gré à gré ?**
> Pour la liquidité, la transparence du prix et l'absence de risque de
> contrepartie. Il accepte en échange de ne pas avoir de sur-mesure.

**7. Sur quoi gagne un sales de listé ?**
> Sur le volume et la qualité d'exécution, pas sur une marge de structuration.
> C'est un métier de flux.

**8. Qu'est-ce qu'un future sur indice ?**
> Un engagement standardisé d'acheter ou vendre l'indice à une date future, à
> un prix fixé aujourd'hui, réglé en espèces.

**9. Cross-asset, qu'est-ce que ça change pour toi ?**
> Il faut comprendre plusieurs mécaniques, mais la grammaire est la même :
> sensibilité, couverture, liquidité. C'est ce qui m'intéresse.

**10. Qu'est-ce que le VIX ? Où est-il ?**
> L'indice de volatilité implicite du S&P 500. Il est repassé sous 16 le
> 18 septembre après la Fed, alors que le SKEW reste autour de 146.

**11. Qu'est-ce que le delta ?**
> La sensibilité du prix de l'option au sous-jacent, donc la quantité à
> couvrir. Un call à la monnaie est autour de 0,50.

**12. Tu apportes quoi à un desk de flux ?**
> De l'automatisation. Chez BPCE j'ai construit des chaînes BQL et VBA qui se
> régénèrent seules. Sur un métier de volume, le temps gagné sur le reporting
> est du temps rendu au client.

---

## 🟦 ENTRETIEN 4 — Rafael Real, Natixis, Assistant Trader Equity / Trade Support

### Mini-cours

**Qui il est.** Assistant trader et trade support sur le desk actions de
Natixis. Il t'a dit qu'il essaierait de t'appeler dans la semaine.

**Ce qu'est le trade support.** C'est le **pont entre le front office et le
back office**. Quand un trade est fait, il faut qu'il soit correctement
enregistré, que les deux parties soient d'accord sur les termes, que les
positions et le résultat du jour soient justes.

**Les tâches réelles :** saisie et vérification des opérations, résolution des
écarts (*breaks*), rapprochement des positions, contrôle du P&L quotidien,
préparation des données pour le desk.

> ⚠️ **Ne méprise jamais ce poste, même en pensée.** C'est une porte d'entrée
> classique vers le front, et surtout : **c'est là qu'on apprend comment la
> banque fonctionne réellement.** Un trader qui ne comprend pas le cycle de vie
> d'un trade est un trader incomplet.

**Ce qu'on attend d'un stagiaire ici.** De la **rigueur** avant tout. Un écart
non résolu à 18 h, c'est un problème pour tout le monde. Et de
l'**automatisation** : beaucoup de contrôles sont encore manuels.

**Ton avantage, et il est énorme sur ce poste.** Ton stage BPCE était
**exactement** ça : reporting multi-actifs, contrôle, automatisation.
**C'est la piste où ton expérience colle le mieux à 100 %.**

**Ce qu'il t'a demandé** — profil automatisation ou suivi quotidien ? **Réponds
les deux, en commençant par la rigueur.**

### Ton accroche

> « Ce que j'ai fait chez BPCE, c'était du contrôle et de l'automatisation sur
> du multi-actifs. Ce qui m'intéresse ici, c'est de voir le cycle de vie
> complet d'un trade — est-ce que c'est vraiment la meilleure école pour
> comprendre un desk ? »

### Les 12 questions

**1. Qu'est-ce que le trade support ?**
> Le pont entre le front et le back. On s'assure que ce qui a été traité est
> correctement enregistré, rapproché et valorisé.

**2. Qu'est-ce qu'un break ?**
> Un écart entre deux systèmes ou entre nous et la contrepartie. Il faut
> l'identifier, comprendre d'où il vient et le résoudre avant la clôture.

**3. Qu'est-ce que le P&L quotidien ?**
> Le résultat du jour du desk. On le calcule, on l'explique et on le rapproche
> de ce que le trader attendait.

**4. Que fais-tu si ton chiffre ne colle pas à celui du trader ?**
> Je cherche d'abord dans mes données : périmètre, date, cours utilisé. Je ne
> vais le voir qu'avec une hypothèse précise, pas avec un problème.

**5. Automatisation ou suivi quotidien ?**
> Les deux, dans cet ordre : d'abord fiable, ensuite rapide. Un contrôle
> automatisé mais faux est pire qu'un contrôle manuel.

**6. Qu'est-ce que tu as automatisé chez BPCE ?**
> Des requêtes BQL pour récupérer les séries multi-actifs, et du VBA pour la
> mise en forme et les contrôles de cohérence. L'objectif était que le rapport
> se régénère sans intervention.

**7. Qu'est-ce que BQL ?**
> Le langage de requête de Bloomberg. On interroge directement les données au
> lieu de les extraire cellule par cellule.

**8. Un exemple d'erreur que tu as trouvée ?**
> Un écart de valorisation qui venait d'une date de cours décalée d'un jour sur
> une ligne. Rien de spectaculaire, mais c'est exactement le genre de chose qui
> fausse un rapport entier.

**9. Qu'est-ce qu'une date de valeur ?**
> La date à laquelle l'échange effectif a lieu, différente de la date de
> négociation.

**10. Pourquoi ce poste et pas directement du front ?**
> Parce que c'est là qu'on comprend comment un desk fonctionne réellement. Je
> préfère commencer par savoir ce qui se passe après le trade.

**11. Comment tu gères la pression de la clôture ?**
> En traitant les écarts au fil de l'eau plutôt qu'en fin de journée, et en
> disant tôt quand quelque chose bloque.

**12. Tu te vois où après ?**
> Sur un desk. Mais je ne considère pas ce poste comme une étape à franchir —
> c'est le seul endroit où on voit la chaîne complète.

---

## 🟦 ENTRETIEN 5 — Mouminatou Dione, CACIB, Equity Derivatives Market Risk

### Mini-cours

**Qui elle est.** Analyste risque de marché sur les dérivés actions chez Crédit
Agricole CIB. Elle s'est proposée de se renseigner pour toi — **elle attend une
relance depuis huit jours.**

**Ce qu'est le risque de marché.** Une équipe **indépendante du front** qui
mesure et encadre le risque pris par les desks. Elle ne prend pas de position :
elle calcule, alerte, et fait respecter les limites.

**Ce qu'elle fait concrètement :** calcul quotidien de la VaR, stress tests
sur scénarios, suivi des grecs agrégés du desk, contrôle des limites,
explication des variations de risque.

> 🔑 **C'est ta porte « quant-adjacente ».** Tu m'as dit être ouvert au quant :
> le risque de marché est le métier le plus proche du quant accessible avec un
> profil école de commerce. On y fait du Python, des statistiques, de la
> modélisation — mais avec un objectif de contrôle, pas de pricing.

**La difficulté propre au risque sur les dérivés actions.** Un portefeuille
d'options n'a pas un risque linéaire. Il faut raisonner en **sensibilités**
agrégées, et surtout en **scénarios** : que se passe-t-il si le marché baisse
de 20 % **et** que la volatilité double **et** que les corrélations passent
à 1 ? C'est précisément ce que la VaR ne capture pas.

**Ton avantage.** ShockDesk **est** un outil de stress test. Tu as appliqué des
chocs de courbe et mesuré l'impact. C'est littéralement leur métier.

### Ton accroche

> « J'ai construit un outil qui applique des chocs de courbe et mesure l'impact
> sur un portefeuille. Ce que je n'ai pas, c'est la partie gouvernance : qui
> fixe les limites, et que se passe-t-il concrètement quand une limite est
> dépassée ? »

### Les 12 questions

**1. Qu'est-ce que la VaR ?**
> La perte maximale attendue sur un horizon donné, à un niveau de confiance
> donné. Par exemple une VaR un jour à 99 %.

**2. Ses limites ?**
> Elle ne dit rien au-delà du seuil, elle suppose des corrélations stables qui
> sautent précisément en crise, et elle est calibrée sur le passé.

**3. VaR historique ou paramétrique ?**
> L'historique rejoue les variations passées telles quelles. La paramétrique
> suppose une loi, souvent normale, ce qui sous-estime les extrêmes.

**4. Qu'est-ce que l'expected shortfall ?**
> La moyenne des pertes au-delà du seuil de VaR. Elle a été introduite pour
> combler le premier défaut de la VaR.

**5. Qu'est-ce qu'un stress test ?**
> Au lieu d'une statistique, on applique un scénario choisi : baisse de 20 %,
> doublement de la volatilité, corrélations à 1.

**6. Comment mesure-t-on le risque d'un portefeuille d'options ?**
> Pas en linéaire. On agrège les grecs — delta, gamma, vega — et on complète
> par des scénarios, parce que le gamma rend la perte non proportionnelle.

**7. Pourquoi un choc de corrélation est-il important en dérivés actions ?**
> Parce que les produits multi-sous-jacents comme les worst-of sont directement
> exposés à la corrélation. Si elle bouge, le prix bouge sans que les
> sous-jacents aient bougé.

**8. Différence entre risque de marché et risque de contrepartie ?**
> Le risque de marché, c'est que le prix bouge contre nous. Le risque de
> contrepartie, c'est que l'autre partie ne paie pas.

**9. À quoi sert Python dans une équipe de risque ?**
> À industrialiser : récupérer les positions, appliquer les scénarios, produire
> les chiffres tous les jours de la même façon. L'intérêt n'est pas la
> sophistication, c'est la reproductibilité.

**10. Parle-moi de ShockDesk.**
> Un backtest sur juillet-août 2026, 25,5 millions de dollars de nominal :
> 337 883 dollars, soit 1,32 %, Sharpe 1,67, drawdown maximum 8 points de base,
> 21 trades.

**11. Ses limites ?**
> Deux mois c'est trop court pour que le Sharpe soit significatif, je n'ai pas
> modélisé l'impact de marché, et j'ai choisi les paramètres en connaissant la
> période — donc risque de surajustement.

**12. Pourquoi le risque plutôt que le front ?**
> Parce que c'est le seul endroit où on voit le portefeuille entier et pas une
> position. Et parce que c'est là qu'on apprend ce qui casse.

---

## 🟩 ENTRETIEN 6 — Louis Riou, CACIB, salle des marchés de Nantes

### Mini-cours

**Qui il est.** Assistant trader / vendeur en salle des marchés régionale de
CACIB à Nantes. **Il a confirmé chercher un stagiaire pour janvier** et proposé
un appel rapidement.

**Ce qu'est une salle régionale.** À Paris, les desks sont hyperspécialisés :
un sales fait du change, un autre du taux. **En salle régionale, le même
interlocuteur couvre le change, les taux et le placement de trésorerie** pour
des entreprises du territoire. Ici : ETI du Grand Ouest — agroalimentaire,
logistique maritime, naval, distribution.

**Qui sont les clients.** Pas des investisseurs. Des **trésoriers
d'entreprise**. Leur métier n'est pas de gagner de l'argent sur les marchés,
c'est de **sécuriser un budget**.

> 🔑 **L'idée centrale, et elle vaut l'entretien entier :**
> *« Un trésorier ne cherche pas le meilleur cours, il cherche à tenir son
> budget. Il a un cours budget voté en interne ; son objectif est de ne pas
> s'en écarter, pas de battre le marché. »*
>
> Presque aucun candidat ne comprend ça, et c'est pourtant toute la différence
> entre vendre à un investisseur et vendre à une entreprise.

**Les produits :** terme sec, swap de change, NDF, tunnel, options vanilles
côté change ; swap de taux, cap, floor, collar côté taux ; dépôt à terme et
billets de trésorerie côté placement.

**Les tâches d'un stagiaire :** rédaction du point marché quotidien envoyé aux
directeurs financiers clients, saisie et suivi des opérations, maintenance des
outils de simulation de couverture, support aux commerciaux itinérants.

**Ton avantage.** C'est **la seule piste où toute ta préparation change
s'applique directement.** Forward, NDF, tunnel, accumulateur, restructuration :
tu as tout.

⚠️ **La question de mobilité tombera.** Prépare une réponse nette. Une
hésitation sur Nantes tue la candidature plus sûrement qu'une erreur technique.

### Ton accroche

> « Ce qui m'intéresse en salle régionale, c'est qu'on est au contact direct du
> trésorier. Et un trésorier ne cherche pas le meilleur cours, il cherche à
> tenir son budget. Est-ce que la remontée des taux a changé leur façon
> d'arbitrer entre terme sec et structure optionnelle ? »

### Les 12 questions

**1. Qu'est-ce qu'un cours à terme ? C'est une prévision ?**
> Non. C'est mécaniquement le comptant corrigé de l'écart de taux entre les deux
> devises. Sinon il y aurait un arbitrage sans risque. La devise au taux le plus
> élevé part en déport.

**2. EUR/USD à 1,1700, taux euro 2 %, taux dollar 3,5 %, un an. Le terme ?**
> Le dollar a le taux le plus élevé, donc il part en déport : le terme est
> au-dessus. 1,17 × 1,035 / 1,02 égale 1,1872, soit environ 172 pips.

🔑 **Donne le sens avant le chiffre.** Bon sens et ordre de grandeur : tu t'en
sors. Quatre décimales dans le mauvais sens : tu es mort.

**3. Un exportateur encaisse 2 millions de dollars dans six mois. Que
proposes-tu ?**
> D'abord je lui demande son cours budget et son horizon, parce que c'est ça
> qui détermine la structure, pas ma vue sur le marché.

**4. Il veut un plancher mais garder la hausse.**
> Un tunnel. Il achète un put pour garantir un cours plancher et finance la
> prime en vendant un call, ce qui plafonne sa hausse. Souvent construit à
> prime nulle.

**5. Comment tu lui présentes le tunnel ?**
> On échange du potentiel contre de la gratuité.

**6. Qu'est-ce qu'un terme boosté ? Où est le risque ?**
> Il obtient un cours meilleur que le terme sec, mais avec un doublement du
> nominal si un seuil est franchi. Le client améliore son cours en vendant de
> la convexité.

**7. Qu'est-ce qu'un accumulateur ?**
> Un produit qui accumule dans une zone et double ou se désactive en dehors. Il
> a fait des dégâts considérables chez des corporates asiatiques en 2008 — c'est
> le produit qu'on ne place pas sans être sûr que le client a compris.

**8. Le spot a bougé de 8 % contre le client. Que fais-tu ?**
> Je l'appelle avant qu'il m'appelle, et je propose une restructuration. La
> valeur ajoutée d'un sales, c'est ça — pas de constater la perte avec lui.

**9. Qu'est-ce qu'un swap de change ?**
> Un achat au comptant et une vente à terme simultanés. Ce n'est pas une
> position directionnelle : c'est un outil de trésorerie, on déplace une date
> de valeur.

**10. Qu'est-ce qu'un NDF ?**
> Un terme réglé en différence, en dollars, sans livrer la devise locale. Il
> existe pour les devises non librement livrables.

**11. Qu'est-ce qu'un cap ? Un collar de taux ?**
> Un cap plafonne un taux variable — c'est une option. Un collar, c'est un cap
> financé par la vente d'un floor, donc on plafonne à la hausse mais on renonce
> à profiter de la baisse.

**12. Nantes, ça te convient vraiment ?**
> Oui, et ce n'est pas une concession. En salle régionale on voit le change, le
> taux et la trésorerie sur le même client — à Paris j'aurais une seule de ces
> trois vues. Pour une première expérience, c'est mieux.

---

## 🟩 ENTRETIEN 7 — Matthieu Mugler, CACIB, Cross-Asset Sales

### Mini-cours

**Qui il est.** Sales cross-asset en salle des marchés, Crédit Agricole
Île-de-France. Contacté sur recommandation d'**Ali Megarni**. Il t'a dit :
*« Nous recrutons pour janvier 2027, stages de 6 mois, campagnes ouvertes en
octobre. »* **Tu lui as demandé un appel — il n'a pas encore répondu.**

**Ce que veut dire cross-asset.** Il ne couvre pas un produit mais un
**client**, avec tous les produits dont ce client a besoin : change, taux,
parfois inflation ou crédit. Son métier est de comprendre l'exposition globale
d'une entreprise et d'y répondre.

**Le chiffre.** Au T2 2026, la Banque de Marché et d'Investissement de CACIB a
fait **933 M€, +8,5 %**, avec une **banque d'investissement en hausse de 63,8 %
hors effet change** portée par l'equity structuré et l'ECM, pendant que le
**FICC restait stable**, pénalisé par la trésorerie dans un contexte de
réduction des bilans des banques centrales.

**Pourquoi ce détail est utile.** Il montre **un écart interne** : une partie
de la maison cartonne, une autre souffre, et la cause est identifiée. C'est un
sujet de conversation naturel pour quelqu'un qui couvre plusieurs classes.

**Ali.** Une seule mention, ici. **Ne le réutilise nulle part ailleurs chez
CACIB.**

### Ton accroche

> « Les revenus de BMI ont progressé de 8,5 % au deuxième trimestre, mais avec
> un écart marqué : l'equity structuré a très bien marché pendant que la
> trésorerie a souffert de la réduction des bilans des banques centrales. Sur
> un desk cross-asset, est-ce que ça change la façon dont les clients
> arbitrent ? »

### Les 12 questions

**1. Qu'est-ce qu'un sales cross-asset couvre ?**
> Un client, pas un produit. Change, taux, parfois inflation et crédit. L'enjeu
> est de comprendre l'exposition globale, pas de vendre une ligne.

**2. Pourquoi une entreprise couvre-t-elle, au fond ?**
> Pour sécuriser un budget voté, pas pour battre le marché. C'est de la
> réduction de variance, pas de la performance.

**3. Qu'est-ce que le risque de change économique ?**
> Le risque de compétitivité à moyen terme, par opposition au risque
> transactionnel qui porte sur une facture identifiée. Il est beaucoup plus
> difficile à couvrir parce qu'il n'a pas de montant ni de date.

**4. Un client a du change et du taux. Par quoi commences-tu ?**
> Par celui qui pèse le plus sur son résultat. S'il ne le sait pas, c'est déjà
> le premier sujet de la conversation.

**5. Qu'est-ce qu'un swap de taux ?**
> Un échange de taux fixe contre variable sur un nominal. Le nominal n'est pas
> échangé, seuls les intérêts le sont.

**6. Qu'est-ce qu'un produit hybride ?**
> Un produit dont le payoff dépend de plusieurs classes d'actifs à la fois — par
> exemple taux et change. La difficulté est la corrélation entre les deux.

**7. Qu'est-ce que le tunnel, et pourquoi ça marche commercialement ?**
> Une protection financée par la vente du potentiel inverse. Ça marche parce
> que le client voit une prime nulle — mais il a payé, simplement pas en
> espèces.

**8. La BCE a monté ses taux. Qu'est-ce que ça change pour tes clients ?**
> Le coût de portage change, donc les points de terme changent. Et la question
> du placement de trésorerie redevient un sujet, ce qui n'était pas le cas il y
> a quelques années.

**9. Qu'est-ce qu'un cap ?**
> Une option qui plafonne un taux variable. L'emprunteur paie une prime et
> connaît son taux maximal.

**10. Comment tu expliques une perte de couverture à un directeur financier ?**
> En rappelant l'objectif initial. Une couverture qui « perd » quand le marché
> va dans le bon sens a fait exactement son travail : elle a supprimé
> l'incertitude. Le problème, c'est quand ça n'a pas été dit au départ.

**11. Qu'est-ce que la restructuration ?**
> Ajuster une couverture existante quand le marché a bougé. C'est ce qui
> distingue un sales qui suit son client d'un sales qui a vendu une fois.

**12. Pourquoi CACIB ?**
> Parce que c'est une maison où les corporates sont au centre, pas en
> complément. Et parce que le cross-asset correspond à ce que je cherche : voir
> plusieurs mécaniques sur le même client.

---

## 🟨 ENTRETIEN 8 — François Blanc / Yvon Pilchen, IRS Cross-market Trading

### Mini-cours

**Qui ils sont.** François Blanc est Executive Director, trading IRS
cross-market. **Il t'a dit ne pas avoir de poste mais t'a orienté vers son
manager, Yvon Pilchen.** C'est une recommandation : utilise-la explicitement.

**Ce qu'est un IRS.** *Interest Rate Swap*, swap de taux d'intérêt. Deux
parties échangent des flux d'intérêts sur un nominal : l'une paie un taux fixe,
l'autre un taux variable. **Le nominal n'est jamais échangé.**

**Pourquoi c'est le produit le plus traité au monde en volume.** Parce que
c'est l'outil standard pour transformer une dette à taux variable en dette à
taux fixe, ou l'inverse. Toute entreprise endettée, toute banque, tout assureur
en utilise.

**Ce que veut dire cross-market.** Il ne traite pas un seul marché mais les
écarts **entre** marchés : entre devises, entre courbes, entre instruments. Son
métier est le **spread**, pas la direction.

**Les notions indispensables :**

**Jambe fixe / jambe variable.** Le payeur de fixe paie un taux connu et reçoit
un taux qui se recalcule périodiquement.

**Courbe des taux.** L'ensemble des taux selon la maturité. Elle peut monter
(pentue), être plate, ou descendre (inversée).

**OIS** (*Overnight Indexed Swap*) : un swap indexé sur le taux au jour le jour.
En euro, la référence est l'**€STR**. C'est la courbe considérée comme sans
risque.

**Le contexte du moment.** Le 10 ans américain a **dépassé 5 %** le 15 septembre
2026, la Fed a monté ses taux le 16 — **première hausse depuis plus de trois
ans** — et le MOVE, indice de volatilité des taux, est **redescendu vers 76**.

### Ton accroche

> « Monsieur Blanc m'a orienté vers vous. Ce qui m'a frappé cette semaine, c'est
> que le dix ans américain a dépassé 5 % avant la Fed et que le MOVE est
> redescendu après. La volatilité de taux s'est détendue alors que la Fed vient
> de monter — est-ce que le marché considère que c'est la dernière hausse ? »

### Les 12 questions

**1. Qu'est-ce qu'un swap de taux ?**
> Un échange de taux fixe contre variable sur un nominal. Le nominal n'est pas
> échangé, seuls les flux d'intérêts le sont.

**2. Qui paie quoi ?**
> Le payeur de fixe paie un taux connu et reçoit le variable. Il gagne si les
> taux montent.

**3. Qu'est-ce que le DV01 ?**
> La variation de valeur pour un point de base. C'est la seule mesure de
> sensibilité qui s'additionne entre instruments différents — la monnaie commune
> du risque de taux.

**4. Duration modifiée, DV01 : la différence ?**
> La duration modifiée est en pourcentage, le DV01 en monnaie. C'est pour ça
> qu'on peut additionner des DV01 et pas des durations.

**5. Obligation 5 ans, coupon 3 %, rendement 4 %. Prix et DV01 sur 10 millions ?**
> Coupon inférieur au rendement, donc sous le pair : prix 95,55. Duration
> modifiée 4,528. DV01 égale 10 millions fois 4,528 fois 0,0001, soit environ
> 4 530 euros par point de base.

**6. Qu'est-ce que la convexité ?**
> La duration suppose une relation linéaire entre prix et taux. En réalité elle
> est courbe. Pour un choc important, la duration sous-estime le gain et
> surestime la perte.

**7. Qu'est-ce qu'une convexité négative ?**
> Une obligation callable : quand les taux baissent, l'émetteur rembourse et
> refinance, donc le gain du porteur est plafonné.

**8. Que signifie une courbe inversée ?**
> Que le marché anticipe des baisses de taux, donc un ralentissement.
> Historiquement c'est le meilleur signal avancé de récession, mais avec un
> délai de douze à vingt-quatre mois. C'est un signal, pas un calendrier.

**9. Peut-on couvrir une obligation d'entreprise avec un future d'État ?**
> Seulement la composante taux. Le spread de crédit reste entièrement ouvert.
> Égaliser deux DV01 sur deux courbes différentes ne neutralise pas le risque,
> ça crée un spread trade.

**10. Qu'est-ce que l'€STR ?**
> Le taux au jour le jour de référence en euro, qui sert de base à la courbe
> OIS considérée comme sans risque.

**11. Qu'est-ce qu'une swaption ?**
> Une option sur un swap : le droit d'entrer dans un swap à des conditions
> fixées d'avance.

**12. Qu'est-ce que ShockDesk apporte ici ?**
> C'est un outil de stress de courbe. J'applique des chocs et je mesure
> l'impact. Le résultat : sur deux mois, 1,32 % avec un Sharpe de 1,67 et
> 8 points de base de drawdown maximum — sur un backtest, avec toutes les
> limites que ça implique.

---

## 🟨 ENTRETIEN 9 — Santander CIB Paris / Élodie Castoriano, Fixed Income & Rates

### Mini-cours

**La situation.** Mickael Dos Santos, ex-Santander, t'a donné le nom d'Élodie
Castoriano et l'adresse `hr-paris@gruposantander.com`. **Tu entres par les RH,
pas par le desk** — le registre est donc différent : plus de motivation, moins
de technique pointue, mais la technique doit être propre.

**Ce qu'est Santander CIB.** La banque de financement et d'investissement du
groupe espagnol Santander. Sa force : **l'Europe du Sud et l'Amérique latine**,
où le groupe est très implanté. À Paris, c'est une succursale de taille
moyenne — donc des équipes resserrées et un stagiaire plus exposé.

> 🔑 **Ton espagnol est un vrai atout ici, et c'est le seul endroit de tes douze
> pistes où c'est le cas.** Mentionne-le, une fois, sans insister.

**Fixed income** signifie littéralement « revenu fixe » : les obligations et
tout ce qui s'y rattache. **Rates** désigne les taux au sens large — swaps,
futures, courbe.

**Les notions de base à tenir :**

**Marché primaire** : l'émission, quand l'émetteur lève des fonds.
**Marché secondaire** : l'échange des titres entre investisseurs ensuite.
**Spread de crédit** : le supplément de rendement au-dessus du souverain, qui
rémunère le risque de défaut.
**Notation** : l'évaluation par une agence de la qualité de crédit.
**Investment grade** : bonne qualité. **High yield** : spéculatif, rendement
plus élevé.

### Ton accroche

> « Ce qui m'intéresse chez Santander, c'est que c'est une des rares maisons à
> Paris où l'Amérique latine n'est pas un sujet lointain. Je parle espagnol.
> Est-ce que ça se traduit concrètement dans les flux du desk parisien ? »

### Les 12 questions

**1. Qu'est-ce que le fixed income ?**
> Tout ce qui relève de la dette : obligations souveraines et d'entreprise,
> swaps, instruments de taux.

**2. Primaire ou secondaire, la différence ?**
> Le primaire, c'est l'émission : l'émetteur lève des fonds. Le secondaire,
> c'est l'échange des titres entre investisseurs ensuite.

**3. Qu'est-ce qu'un spread de crédit ?**
> L'écart de rendement entre une obligation d'entreprise et un titre d'État de
> même maturité. Il rémunère le risque de défaut.

**4. Qu'est-ce qui fait bouger un spread alors que le taux ne bouge pas ?**
> La perception du risque de l'émetteur : résultats, notation, secteur,
> liquidité du titre. C'est le prix du risque de crédit, pas le prix du temps.

**5. Investment grade et high yield ?**
> L'investment grade est de bonne qualité de crédit, le high yield est
> spéculatif et offre un rendement plus élevé pour compenser.

**6. Qu'est-ce qu'un CDS ?**
> Un contrat d'assurance contre le défaut d'un émetteur. L'acheteur de
> protection paie une prime périodique et est indemnisé en cas de défaut.

**7. Pourquoi le rendement à maturité est-il imparfait ?**
> Parce qu'il suppose que les coupons sont réinvestis à ce même taux, ce qui
> n'arrive quasiment jamais.

**8. Relation prix-taux d'une obligation ?**
> Inverse. Quand les taux montent, les titres anciens deviennent moins
> attractifs, donc leur prix baisse jusqu'à ce que leur rendement rejoigne le
> marché.

**9. Qu'est-ce que la duration ?**
> La sensibilité du prix à une variation de taux. La duration modifiée donne la
> variation en pourcentage pour 1 % de taux.

**10. Qu'est-ce que le DV01 ?**
> La même chose en monnaie, pour un point de base. C'est la seule mesure qui
> s'additionne.

**11. Le 10 ans américain a dépassé 5 %. Qu'est-ce que ça change ?**
> Ça repositionne tout le reste : le coût de financement des entreprises, la
> valorisation des actifs longs, et l'arbitrage entre actions et obligations.

**12. Pourquoi Santander ?**
> Pour l'ancrage européen et latino-américain, et parce qu'une structure
> parisienne de taille moyenne expose plus vite un stagiaire qu'un très grand
> desk.

---

## 🟪 ENTRETIEN 10 — Olivier Moser, Barclays Private Bank, Monaco

### Mini-cours

**La situation.** Sales Manager chez Barclays Private Bank à Monaco. Il a
accepté de transmettre ton CV à ses RH. **C'est de la cooptation : tu ne passes
pas par le tunnel étudiant classique.**

**Ce qu'est la banque privée, et pourquoi tout change.** Le client n'est ni une
entreprise ni un fonds : c'est **une personne fortunée ou une famille**.
L'objectif n'est pas de couvrir une exposition ni de battre un indice, c'est de
**préserver et transmettre un patrimoine**.

> 🔴 **Bascule de vocabulaire obligatoire.** Tout ton lexique sell-side est
> déplacé ici. On ne dit pas « capturer du spread », on ne dit pas « flux
> client », on ne dit pas « corporate ».

| ❌ Ne dis pas | ✅ Dis |
|---|---|
| produit structuré | **solution d'investissement** |
| couverture | **protection du capital** |
| corporate | **client privé**, **famille** |
| rendement | **performance** |
| capturer du spread | **répondre à un besoin** |

**UHNW** (*ultra high net worth*) : les très grandes fortunes.

**Gestion conseillée** : la banque recommande, le client décide.
**Gestion sous mandat** : le client délègue les décisions.

**Le profil de risque** est une obligation réglementaire : la banque doit
vérifier que le produit correspond au client. C'est **MIF II** qui l'impose en
Europe.

**Le risque émetteur.** C'est le point le plus important à comprendre sur les
produits structurés vendus en banque privée : **même un produit « à capital
garanti » dépend de la solidité de la banque émettrice.** Si elle fait faillite,
la garantie ne vaut rien. Lehman Brothers en 2008 en est l'exemple.

**Ton avantage.** Le **Priour** que tu as lu en entier est écrit **exactement
pour ce public** : conseiller financier et investisseur particulier. Ici, tu
peux le citer sans réserve.

### Ton accroche

> « J'ai lu un ouvrage sur les produits structurés écrit du point de vue du
> conseiller, pas du desk. Ce qui m'a frappé, c'est que la difficulté n'est pas
> de construire le produit, c'est de le faire comprendre. Est-ce que c'est là
> que se joue l'essentiel du travail ? »

### Les 12 questions

**1. Qu'est-ce qui distingue la banque privée de la banque d'investissement ?**
> Le client. En banque privée c'est une personne ou une famille, et l'horizon
> est patrimonial — préserver et transmettre, pas couvrir une exposition.

**2. Qu'est-ce qu'un client UHNW ?**
> Une très grande fortune, avec des besoins de structuration patrimoniale qui
> dépassent le simple placement.

**3. Gestion conseillée ou sous mandat ?**
> En conseillée la banque recommande et le client décide. En mandat, le client
> délègue les décisions.

**4. Qu'est-ce que le profil de risque ? Pourquoi est-ce réglementaire ?**
> C'est l'évaluation de la tolérance au risque et de l'expérience du client.
> MIF II impose de vérifier l'adéquation entre le produit et le client.

**5. Pourquoi proposer un produit structuré à un client privé ?**
> Parce qu'il permet de définir un profil de gain précis — un niveau de
> protection, un niveau de performance — plutôt que de subir le marché.

**6. Qu'est-ce qu'un produit à capital protégé ?**
> Une obligation zéro coupon qui reconstitue le capital à l'échéance, plus une
> option achetée avec le reste pour la performance.

**7. Qu'est-ce que le risque émetteur ?**
> Même un produit à capital garanti dépend de la solidité de la banque
> émettrice. Si elle fait défaut, la garantie ne vaut rien. C'est le point que
> les clients comprennent le moins bien.

**8. Comment expliques-tu une perte à un client privé ?**
> En revenant au scénario présenté au départ. Si la perte était prévue dans un
> scénario connu, la conversation est possible. Sinon, c'est la vente initiale
> qui était mauvaise.

**9. Qu'est-ce qui fait qu'un client reste ?**
> Le fait qu'on l'appelle quand ça va mal, pas seulement quand on a quelque
> chose à lui proposer.

**10. Qu'est-ce qu'une allocation d'actifs ?**
> La répartition du patrimoine entre grandes classes — actions, obligations,
> liquidités, non coté. C'est ce qui explique l'essentiel de la performance à
> long terme.

**11. Tu connais quoi aux produits structurés ?**
> J'ai lu un ouvrage entier écrit du point de vue du conseiller : construction,
> catégories, vie du produit, documentation commerciale. Ce qui m'a le plus
> appris, c'est la partie sur la valorisation en cours de vie.

**12. Pourquoi Monaco ?**
> Parce que c'est une place de banque privée concentrée, avec une clientèle
> internationale, et une taille d'équipe où un stagiaire voit réellement le
> métier.

---

## ⬜ ENTRETIEN 11 — Pauline Barbier, HSBC, Recrutement Global Markets

### Mini-cours

**Qui elle est.** Recruitment Specialist chez HSBC, basée à **Cracovie** —
c'est le centre de services RH d'HSBC pour l'Europe. Elle t'a répondu :
*« Courant octobre, nous devrions commencer à publier les offres de stages. »*

**Le registre est complètement différent.** Elle n'évaluera pas ta maîtrise du
gamma. Elle vérifie : **éligibilité, dates, convention, langue, motivation,
cohérence du parcours.** Son travail est de filtrer, pas de tester.

> ⚠️ **Ne sors aucun chiffre de marché à un RH.** Ça ne marche pas, et ça peut
> même donner l'impression que tu récites. Le couloir ici est **administratif**.

**Les quatre points qui décident :**

**① Tes dates exactes.** Janvier à juin 2027, six mois.
**② La convention de stage.** Point critique : si tu es diplômé en décembre
2026, es-tu encore couvert par une convention en janvier ? **Vérifie auprès de
SKEMA et aie la réponse au mot près.** C'est un motif de rejet purement
administratif et il tombe très tôt.
**③ Ton anglais.** HSBC est une banque britannique : l'entretien peut basculer
en anglais sans prévenir.
**④ La cohérence.** **Un seul intitulé de diplôme**, partout, toujours le même.

**Ce qu'il faut lui demander concrètement :** faut-il postuler en ligne, ou
peut-elle flécher ton profil vers le hub Markets ? Une RH aime une question
opérationnelle à laquelle elle peut répondre.

### Ton accroche

> « Vous m'aviez indiqué que les offres sortiraient courant octobre. Je me
> permets de revenir vers vous : dois-je postuler en ligne dès la publication,
> ou pouvez-vous flécher mon profil vers le hub Markets ? »

### Les 12 questions

**1. Parlez-moi de vous. (30 secondes, pas 40)**
> M2 Finance à SKEMA, candidat FRM. Stage chez BPCE Assurances en reporting
> multi-actifs sous Bloomberg et VBA. Je cherche un stage de fin d'études de
> six mois en Global Markets à partir de janvier 2027.

**2. Vos dates exactes ?**
> Janvier à juin 2027, six mois, avec convention SKEMA.

**3. Vous avez une convention de stage ?**
> Oui, le stage de fin d'études fait partie du cursus.

⚠️ **Ne réponds ça que si c'est vérifié.** Sinon : « Je vous confirme le cadre
exact par écrit dès demain. »

**4. Pourquoi HSBC ?**
> Pour la dimension internationale réelle de la franchise Markets et parce que
> le passage entre Paris et Londres y est un vrai sujet, pas une ligne sur une
> plaquette.

**5. Pourquoi Global Markets ?**
> Parce que c'est le seul endroit où on voit le prix se former en direct et où
> la décision est immédiate.

**6. Quel desk vous intéresse ?**
> Je suis ouvert. Mon socle, c'est le pricing d'options et l'analyse de
> sensibilité — ça sert en actions, en taux comme en change.

**7. Vous parlez anglais ?**
> Oui, niveau professionnel. Je peux poursuivre l'entretien en anglais si vous
> préférez.

🔑 **Propose-le. Ça impressionne, et ça désamorce le test surprise.**

**8. Vous postulez ailleurs ?**
> Oui, plusieurs maisons à Paris sur des postes de marché. Je suis transparent
> là-dessus.

**9. Votre plus gros défaut ?**
> Je vais trop vite au résultat. J'ai appris à le corriger en vérifiant le sens
> d'un calcul avant sa valeur.

**10. Vous n'avez jamais travaillé en salle.**
> C'est exact, et c'est ce que je viens chercher. Ce que j'apporte, c'est le
> socle technique et l'habitude de me préparer.

**11. Qu'est-ce que vous savez de notre process ?**
> Je sais qu'il comporte des tests en ligne et souvent un entretien vidéo
> enregistré. Je suis disponible pour les passer dès que les offres sortent.

**12. Quelles sont vos questions ?**
> Le calendrier exact de publication, et si les candidatures sont examinées au
> fil de l'eau ou après la date limite.

---

## ⬜ ENTRETIEN 12 — Nicolas Ruiz, BNP Paribas, Graduate Global Markets

### Mini-cours

**Qui il est.** Graduate en Global Markets chez BNP Paribas CIB — donc **un
junior, pas un décideur.** Il t'a dit : *« Mon équipe ouvrira l'offre d'ici
octobre ou novembre pour janvier, reste à l'affût. »*

**Pourquoi cet entretien est différent des onze autres.** Il n'a **aucun
pouvoir de décision**. Mais il a trois choses de grande valeur : il sait quand
l'offre sort, il sait ce que le desk cherche vraiment, et **il peut transmettre
ton CV en interne** — ce qui vaut bien plus qu'une candidature en ligne.

**La posture à adopter.** Ce n'est pas un entretien, c'est **une conversation
entre pairs à deux ans d'écart**. Trop formel, tu passes pour un candidat qui
récite. Trop décontracté, tu perds le bénéfice.

> ⚠️ **Un point à corriger.** Ton dernier message lui parlait de *« crédits »*
> et de *« 2 cas longs ou 4 tests rapides »* sur ta plateforme. C'est de la
> formulation produit, et ça te classe du côté « étudiant qui fait sa promo »
> plutôt que « candidat sérieux ». Si tu remontres la plateforme, dis :
> *« J'ai monté un outil d'entraînement aux entretiens. Le niveau te paraît
> réaliste ? Deux lignes me suffisent. »*

**Ce qu'un graduate peut te dire et que personne d'autre ne te dira :** qui
décide réellement, ce que le desk reproche aux stagiaires précédents, et si
l'offre est déjà pré-attribuée.

### Ton accroche

> « Tu m'avais dit octobre-novembre. Avant que l'offre sorte : qu'est-ce que le
> desk reproche le plus souvent aux stagiaires qui arrivent ? Je préfère le
> savoir avant qu'après. »

### Les 12 questions

**1. Tu en es où dans ta recherche ?**
> J'ai une dizaine de pistes actives à Paris, toutes pour janvier. Je prépare la
> technique en parallèle pour être prêt quand les offres sortent.

**2. Tu vises quoi comme desk ?**
> Je suis ouvert. Mon socle, c'est le pricing et la sensibilité. Ce qui compte
> pour moi, c'est d'apprendre sur un desk qui traite du risque.

**3. Pourquoi BNP ?**
> Parce que Global Markets a fait un trimestre exceptionnel avec un mix
> équilibré — Equity & Prime à plus 43 % et FICC stable. Ça veut dire que les
> deux moitiés tournent.

**4. Tu connais notre organisation ?**
> Global Markets se partage entre Equity & Prime Services et FICC. Au deuxième
> trimestre, 1 406 millions d'un côté, 1 404 de l'autre — presque à égalité.

**5. Qu'est-ce que tu as fait techniquement ?**
> Un pricer Black-Scholes avec les grecs et un module de stress, plus du
> reporting multi-actifs automatisé chez BPCE sous BQL et VBA.

**6. C'est quoi ton niveau réel en options ?**
> Je suis solide sur les vanilles, les grecs et la logique de couverture. Sur
> les exotiques je comprends les enjeux mais je ne les ai pas manipulés.

**7. Le graduate programme, ça se passe comment ?**
> *(C'est toi qui poses)* — Tu as fait quelles rotations, et est-ce que tu as pu
> choisir ?

**8. Qu'est-ce qui t'a surpris en arrivant ?**
> *(À lui)* — Qu'est-ce qui t'a le plus surpris entre ce que tu imaginais et la
> réalité du desk ?

**9. Les stagiaires, ils font quoi vraiment ?**
> *(À lui)* — Sur ton desk, un stagiaire passe son temps sur quoi
> concrètement ?

**10. Comment sort l'offre ?**
> *(À lui)* — Elle passe par le site, ou le desk a déjà quelqu'un en tête quand
> elle est publiée ?

**11. Je peux t'envoyer mon CV ?**
> Si tu veux bien le garder sous la main pour le moment où l'offre sort, ça
> m'aiderait beaucoup.

**12. Qu'est-ce que je devrais bosser d'ici là ?**
> *(À lui)* — Si tu étais à ma place avec trois mois devant toi, tu
> travaillerais quoi en priorité ?

🔑 **Dans cet entretien, les bonnes questions valent plus que les bonnes
réponses.** Six des douze sont à poser, pas à préparer.

---

# PARTIE 4 — LA FICHE DE SURVIE

## 4.1 Les prompts Gemini

### Mode calibrage — à utiliser en premier

```
Tu es un professionnel qui reçoit un stagiaire pour un desk
[DESK] chez [MAISON] à Paris. Entretien de 15 minutes en français,
exigeant mais bienveillant.

Une question à la fois. Après CHAQUE réponse, donne-moi une seule
ligne de verdict parmi : "trop long", "pas chiffré", "vague",
"bluff", "bien" — puis enchaîne immédiatement.

Ne creuse pas plus de deux fois sur la même question.
Ne me félicite pas par politesse.
```

### Mode combat — seulement après trois « bien » d'affilée

```
Même rôle, mais cette fois tu es pressé et sceptique.
Tu interromps si je dépasse 30 secondes.
Si j'avance un chiffre, tu demandes systématiquement d'où il vient.
Si je bluffe, tu creuses jusqu'à ce que ça casse.

À la fin, exactement 4 points :
1. Où j'ai bluffé
2. Où j'aurais dû dire "je ne sais pas" et ne l'ai pas fait
3. Quelle réponse était trop longue
4. Est-ce que tu me prendrais, et pourquoi
```

### Mode couloir — l'exercice spécifique

```
Même rôle. Cette fois, note séparément ma capacité à reprendre la
main : chaque fois que je ramène la conversation vers un terrain que
je maîtrise, dis "COULOIR OK" ou "COULOIR RATÉ" et explique en une
ligne pourquoi.
```

### L'ordre de passage

| Rang | Desk | Pourquoi |
|---|---|---|
| 1 | Equity derivatives sales | 5 pistes sur 12 |
| 2 | Equity exotics trading | Le plus dur techniquement |
| 3 | FX corporate | Ton terrain — vérifier qu'il tient à l'oral |
| 4 | Taux / IRS | Trou partiellement comblé |
| 5 | Risque de marché | Porte quant-adjacente |
| 6 | Banque privée | Vocabulaire différent |

## 4.2 Les six chiffres du couloir

| Chiffre | Source |
|---|---|
| BNP Equity **+43,2 %** (1 406 M€) vs FICC **−0,4 %** (1 404 M€) | Communiqué T2 2026 |
| Natixis Equity **+59 %**, dérivés **×2,5** | Résultats BPCE T2 2026 |
| CACIB banque d'investissement **+63,8 %** hors change | Résultats CASA T2 2026 |
| DB FIC **2 614 M€, +16 %** (record) | Résultats DB T2 2026 |
| **VIX 15,4** mais **SKEW 146** | 18 septembre 2026 |
| Fed : **première hausse depuis plus de 3 ans** | 16 septembre 2026 |

## 4.3 Les huit vérités techniques

- **N(d2) = probabilité d'exercice. N(d1) = ratio de couverture.**
- **Gamma et thêta sont la même pièce.**
- **Le DV01 est la seule mesure qui s'additionne.**
- **Le client d'un autocall est vendeur de volatilité.**
- **L'acheteur d'un worst-of est vendeur de corrélation.**
- **La devise au taux le plus élevé part en déport.**
- **Le skew actions est du côté des puts parce que les krachs sont à la baisse.**
- **Un trésorier ne cherche pas le meilleur cours, il cherche à tenir son
  budget.**

## 4.4 Les cinq interdits

- Répéter deux fois le même chiffre dans un entretien.
- Confondre **FIC** et **Global Markets**.
- Présenter un **backtest** comme un résultat réel.
- Dire « développeur », dire « trader le Forex ».
- Varier l'intitulé de ton diplôme d'un interlocuteur à l'autre.

## 4.5 Les phrases de secours

**Quand tu ne sais pas :**
> « Je ne l'ai pas pratiqué, mais voici ce que j'en comprends... et ce que je
> voudrais qu'on m'apprenne, c'est... »

**Quand c'est trop technique :**
> « Je ne saurais pas vous le calculer. Mais je comprends pourquoi c'est un
> sujet : ... »

**Quand tu as besoin de reprendre pied :**
> « Est-ce que je peux vous donner un exemple concret de ce que j'ai fait ? »

**Quand on te pousse sur la mécanique :**
> « Sur la technique je serais moins précis que vous. Ce qui m'intéresse, c'est
> le besoin en face : pourquoi un client demande ça plutôt qu'autre chose ? »

## 4.6 Le dernier mot

> ⚠️ **Le seul test qui compte :** si tu peux redire la même chose **avec
> d'autres mots** à deux jours d'intervalle, c'est acquis. Si tu ne sais la
> dire que d'une seule façon, c'est de la récitation — **et une récitation
> s'entend.**
