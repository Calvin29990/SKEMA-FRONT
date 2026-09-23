# Masterclass finale
## Les notions cles et les questions classiques, avant de passer a l'oral

> **Ce document est le dernier.** La suite se fait a voix haute avec Gemini.
> Il n'est donc pas ecrit pour etre relu dix fois : il est ecrit pour etre
> **restitue**. A chaque notion, tu trouveras la reponse telle qu'elle doit
> sortir de ta bouche - pas un cours, une **reponse de 15 a 20 secondes**.
>
> **Regle unique de ce document :** si tu ne peux pas le dire a voix haute sans
> le lire, tu ne le sais pas.

---

## 0. Les cinq reflexes qui valent tout le reste

**① Conclusion d'abord.** On repond, puis on explique. Jamais l'inverse.

**② Un chiffre par reponse.** Un seul. Deux, c'est un etalage ; zero, c'est du
vent.

**③ « Je » et pas « on ».** « J'ai construit », pas « on a fait ».

**④ Trancher, puis nuancer.** « Oui, mais » - jamais « ca depend » tout seul.

**⑤ Finir net et se taire.** Le silence apres une bonne reponse travaille pour
toi. Celui qui rajoute une phrase de trop annule celle d'avant.

> 🔑 **Et la regle qui les depasse toutes : « je ne sais pas » n'elimine
> personne.** Bluffer trente secondes de trop, si. La formule de secours :
> *« Je ne l'ai pas pratique, mais voici ce que j'en comprends... et ce que je
> voudrais qu'on m'apprenne, c'est... »*

---

## 1. LE CHANGE - le socle

### 1.1 Ce qu'est une cotation

Une paire s'ecrit **base / cotee**. Sur EUR/USD = 1,1700, l'euro est la **base**,
le dollar la **cotee** : un euro vaut 1,17 dollar. Quand la paire monte, la base
s'apprecie.

Un **pip** est le dernier chiffre de la cotation standard : la **4e decimale**
sur la plupart des paires, la **2e** sur les paires en yen.

**Le chiffre a connaitre :** 0,5 pip sur 10 millions d'EUR/USD = **500 dollars**.
C'est l'ordre de grandeur de ce que gagne un desk sur un ticket ordinaire.

### 1.2 Le terme - la seule formule vraiment obligatoire

```
F = S x (1 + taux cotee x t) / (1 + taux base x t)
```

> 🗣️ **La reponse type :** « Un cours a terme n'est pas une prevision. C'est
> mecaniquement le comptant corrige de l'ecart de taux entre les deux devises.
> Si ce n'etait pas le cas, il y aurait un arbitrage sans risque. **La devise au
> taux le plus eleve part en deport.** »

**Le calcul mental :** `spot x ecart de taux x duree`. Pour USD/BRL a 5,16, un
ecart de 14 % contre 3,625 % sur 3 mois : environ 5,16 x 0,104 x 0,25 = 0,134,
donc un terme autour de **5,29**. Le chiffre exact est **5,2926**.

### 1.3 Le NDF

**Non-deliverable forward** : un terme regle **en difference, en dollars**, sans
jamais livrer la devise locale. Il existe parce que certaines devises ne sont
pas librement livrables hors du pays.

```
Paiement = Nominal x (Forward - Fixing) / Fixing
```

⚠️ **On divise par le fixing**, pas par le forward. C'est l'erreur classique.

Le fixing brésilien est le **PTAX** : une **moyenne de quatre releves
quotidiens** publiee par la banque centrale.

### 1.4 Le swap de change

L'echange simultane d'une operation au comptant et d'une operation en sens
inverse a terme. **Ce n'est pas une position directionnelle** : c'est un outil
de tresorerie, on deplace une date de valeur. C'est le produit le plus traite du
marche des changes en volume.

### 📝 Exercice 1

Taux euro 2 %, taux dollar 3,5 %, EUR/USD comptant 1,1700, echeance 1 an. Le
terme est-il au-dessus ou en dessous ? Ordre de grandeur ?

<details>
<summary><strong>Correction</strong></summary>

Le dollar - la devise **cotee** - a le taux le plus eleve, donc le **dollar part
en deport** : il faut plus de dollars a terme pour un euro. **Le terme est
au-dessus du comptant.**

`1,17 x 1,035 / 1,02 = 1,1872`, soit environ **+172 pips**.

**Le reflexe a garder :** on determine le SENS avant de calculer. Un sales qui
annonce le bon sens et un ordre de grandeur approximatif s'en sort ; celui qui
donne quatre decimales dans le mauvais sens est mort.

</details>

---

## 2. LES OPTIONS

### 2.1 Les definitions qui doivent sortir sans hesiter

Un **call** donne le droit d'acheter, un **put** le droit de vendre. Le droit,
jamais l'obligation - c'est ce qui le distingue d'un terme.

La **prime** est le prix du droit. Le **strike** est le cours d'exercice.
**Europeenne** = exercable a l'echeance seulement ; **americaine** = a tout
moment.

**A la monnaie** (ATM) : strike = cours actuel. **Dans la monnaie** : exercer
serait rentable aujourd'hui. **En dehors** : l'inverse.

### 2.2 Black-Scholes et Garman-Kohlhagen

> 🗣️ « En change, on ne price pas en Black-Scholes mais en
> **Garman-Kohlhagen** : c'est la meme logique, avec **deux taux sans risque**
> au lieu d'un, celui de chaque devise. La devise etrangere se comporte comme
> une action versant un dividende continu egal a son taux. »

**Les hypotheses a savoir critiquer** : volatilite constante (fausse - c'est le
smile), rendements log-normaux (les queues sont plus epaisses dans la realite),
absence de couts de transaction, possibilite de couvrir en continu.

**Le resultat verifie a connaitre.** S = 100, K = 105, r = 3 %, sigma = 25 %,
T = 0,5 an :

| | Valeur |
|---|---|
| Call | **5,5760** |
| Put | **9,0127** |
| Delta (call) | **0,4591** |
| Gamma | **0,0224** |
| Vega (pour 1 point de vol) | **0,2806** |
| Theta par jour | **-0,0225** |

**Approximation utile :** N(x) ≈ 0,5 + 0,4x pour x petit.

### 2.3 La parite call-put

```
C - P = S - K x e^(-rT)
```

> 🗣️ « C'est une relation d'arbitrage, pas un modele. Elle ne depend d'aucune
> hypothese sur la volatilite : si elle est violee, il y a de l'argent gratuit. »

**Verification sur les chiffres ci-dessus :** 5,5760 - 9,0127 = **-3,4368**, et
100 - 105 x e^(-0,015) = **-3,4368**. Identique.

### 2.4 Les grecs, en une ligne chacun

| Grec | Mesure la sensibilite a | Ce qu'il faut dire |
|---|---|---|
| **Delta** | le sous-jacent | La quantite a couvrir. Un call ATM est vers 0,50 |
| **Gamma** | la variation du delta | Fort pres du strike et pres de l'echeance |
| **Vega** | la volatilite | Maximum a la monnaie, croit avec la maturite |
| **Theta** | le temps | Negatif pour l'acheteur. S'accelere en fin de vie |
| **Rho** | le taux d'interet | **En FX il y en a deux** - un par devise |

> 🔑 **La relation a maitriser :** gamma et theta sont les deux faces d'une meme
> piece. « Etre long gamma, c'est etre paye pour rebalancer sa couverture quand
> le marche bouge - et ce privilege se paie en theta chaque jour. »

### 2.5 Smile, skew, surface

La **volatilite implicite** est la volatilite que le marche met dans le prix.
Black-Scholes la suppose unique ; en pratique elle varie selon le strike.

**Smile** : la vol est plus elevee des deux cotes qu'a la monnaie - forme de
sourire. **Skew** : l'asymetrie entre les deux cotes.

> 🗣️ « Sur les actions, le skew est marque du cote des puts : le marche paie
> cher la protection a la baisse, parce que les krachs sont a la baisse. **Sur
> le change c'est different** : le skew dit quelle direction fait peur sur cette
> paire. Sur les devises emergentes il est asymetrique du cote de la
> depreciation locale - ce n'est pas une anomalie, c'est la memoire des crises. »

### 2.6 Volatilite realisee et implicite

**Realisee** : ce que le marche a effectivement fait, mesure historiquement.
**Implicite** : ce que le marche anticipe, extrait des prix d'options.

**La conversion a connaitre :** vol journaliere = vol annuelle / racine(252).
Une vol de **13 % par an donne 0,82 % par jour**.

### 📝 Exercice 2

Un client te dit : « votre option est trop chere ». Que reponds-tu ?

<details>
<summary><strong>Correction</strong></summary>

**La mauvaise reponse :** justifier le prix par le modele. Personne n'a envie
d'entendre parler de Black-Scholes.

**La bonne :** « Le prix, c'est la volatilite. Si vous la trouvez chere, il y a
trois leviers : on **baisse le strike** et vous acceptez une protection moins
bonne ; on **finance la prime** en vendant une option de l'autre cote, c'est le
tunnel ; ou on **raccourcit la maturite**. Lequel correspond le mieux a votre
contrainte ? »

**Ce que la reponse demontre :** on ne defend pas un prix, on **propose une
alternative**. C'est exactement la difference entre un sales et un pricer.

</details>

---

## 3. LES STRUCTURES CORPORATE

Quatre, par ordre de frequence. **A connaitre par coeur : elles reviennent dans
tous les entretiens FX sales.**

**① Le terme sec.** Gratuit, simple, certitude totale. Inconvenient : le client
perd tout gain favorable. C'est le point de comparaison de tout le reste.

**② Le tunnel** (*collar*). On achete une protection, on la finance en vendant
du potentiel de l'autre cote. Souvent construit a **prime nulle**.
> 🗣️ « On echange du potentiel contre de la gratuite. »

**③ Le terme booste.** Meilleur cours que le terme sec, mais **double nominal**
si un seuil est franchi.
> 🗣️ « Le client ameliore son cours en vendant de la convexite. »

**④ L'accumulateur.** Accumule dans une zone, desactive ou double en dehors.
**A fait des degats considerables chez des corporates asiatiques en 2008** - a
citer si on teste ta conscience du risque.

> 🔑 **Le mot qui fait la difference : RESTRUCTURATION.**
> *« Une couverture n'est pas un acte unique. Quand le spot a bouge de 8 %, la
> valeur ajoutee du sales c'est de proposer une restructuration, pas de
> constater la perte avec le client. »*

### L'option asiatique - le produit FX corporate par excellence

Le paiement depend de la **moyenne** du cours sur la periode, pas du cours final.
On l'appelle **ARO**, *average rate option*.

**Pourquoi elle existe :** un exportateur ne facture pas une fois, il facture
tous les mois. **Son exposition est une moyenne, donc sa couverture doit en etre
une.**

> 🗣️ « L'asiatique est moins chere qu'une vanille parce que la volatilite d'une
> moyenne est plus faible que celle du spot - d'un facteur racine de trois
> environ, soit **42 % de moins**. Ce n'est pas une remise commerciale, c'est
> mecanique. Et elle colle a l'exposition reelle du client. »

---

## 4. LES TAUX - le minimum qui evite l'elimination

### 4.1 Les trois mesures

**Duration de Macaulay** : duree moyenne ponderee des flux, en annees.
**Duration modifiee** : variation de prix en % pour 1 % de taux.
**DV01** : variation en monnaie pour **1 point de base**.

```
DV01 = Nominal x Duration modifiee x 0,0001
```

> 🔑 « Le DV01 est la seule des trois qui s'additionne. On ne peut pas
> additionner la duration d'une obligation et celle d'un swap - les nominaux
> different. **Les DV01 sont tous en euros par point de base.** C'est la monnaie
> commune du risque de taux. »

### 4.2 La convexite

La duration suppose une relation lineaire prix-taux. Elle est en realite
**courbe**. La convexite corrige l'erreur.

**Consequence pratique :** pour un petit mouvement, la duration suffit. Pour un
choc de 100 points de base, elle **sous-estime le gain et surestime la perte**.
**La convexite est un ami de l'acheteur d'obligations.**

### 4.3 La courbe et son inversion

**Pentue** : le long rapporte plus que le court - situation normale.
**Plate** : peu d'ecart. **Inversee** : le court rapporte plus que le long.

> 🗣️ « Une courbe inversee signifie que le marche anticipe des baisses de taux,
> donc un ralentissement. Historiquement c'est le meilleur signal avance de
> recession aux Etats-Unis - mais le delai est long et variable, entre douze et
> vingt-quatre mois. **C'est un signal, pas un calendrier.** »

### 📝 Exercice 3

Obligation 5 ans, coupon 3 %, rendement 4 %. Prix, duration modifiee, DV01 sur
10 M EUR ?

<details>
<summary><strong>Correction</strong></summary>

**Prix = 95,55.** Verifie le sens d'abord : coupon 3 % inferieur au rendement
exige 4 %, donc le titre se vend **sous le pair**. Coherent.

**Macaulay = 4,71 ans**, **duration modifiee = 4,528**.

**DV01** = `10 000 000 x 4,528 x 0,0001` = **4 528 EUR**, soit environ **4 530
euros par point de base**.

</details>

---

## 5. LE METIER

### 5.1 Sales ou trader

> 🗣️ « Le trader porte le risque, le sales porte la relation. Le trader gagne
> sur la position, le sales sur le spread et le flux. Les deux se parlent toute
> la journee, mais on ne mesure pas leur performance de la meme facon. »

### 5.2 Une journee

Avant l'ouverture : lecture des niveaux, des publications du jour, des positions
clients. Puis les **RFQ** - le client demande un prix, le sales va le chercher
aupres du trader, le renvoie avec sa marge, execute si le client traite. Entre
deux : appels sortants, explication des niveaux, **propositions de couverture
avant que le client ne les demande**.

### 5.3 Le lexique a placer naturellement

**RFQ** (demande de prix) · **streaming** (prix diffuse en continu) · **hit
ratio** (part des prix cotes qui se transforment en transactions) ·
**internaliser** (croiser deux flux clients en interne sans passer par le
marche) · **skew** · **last look** (droit de derniere verification avant
execution) · **spread capture** · **fixing** · **market impact** (l'effet de
mon propre ordre sur le prix).

### 5.4 Le piege eliminatoire

⚠️ **Ne confonds jamais Global Markets et FIC.** Au T2 2026, Deutsche Bank a
realise **2 614 M EUR en FIC**, en hausse de 16 %, un record. Global Markets est
un perimetre plus large. Confondre les deux devant un professionnel te sort du
process en une phrase.

---

## 6. LES QUINZE QUESTIONS CLASSIQUES

Les reponses sont **volontairement courtes**. Toute reponse qui depasse 20
secondes a l'oral est trop longue.

**1. Parlez-moi de vous.**
> M2 a SKEMA, je cherche un stage de fin d'etudes en FX Sales a partir de
> janvier 2027. Ce qui m'attire dans le change, c'est que c'est le marche le
> plus liquide du monde et que pourtant tout n'y est pas resolu : sur EUR/USD
> l'electronification est terminee et les marges sont ecrasees, la valeur
> ajoutee d'un sales est ailleurs.

**2. Pourquoi le FX plutot qu'une autre classe d'actifs ?**
> Parce que c'est le seul marche ou chaque transaction a deux jambes et ou le
> prix se forme 24 heures sur 24. Et parce que la ou la plomberie n'est pas
> encore standardisee, un sales sert encore a quelque chose.

**3. Sales ou trading ?**
> Sales. Ce qui m'interesse c'est le contact client et la decision rapide, pas
> la modelisation. J'ai construit un pricer, je sais ce qu'il y a derriere un
> prix - mais ce n'est pas la que je serai le meilleur.

**4. Qu'est-ce qu'un cours a terme ?**
> Un engagement d'echanger deux devises a une date future a un cours fixe
> aujourd'hui. Ce cours n'est pas une prevision : c'est le comptant corrige de
> l'ecart de taux. La devise au taux le plus eleve part en deport.

**5. Un client veut couvrir 10 millions a six mois. Que proposez-vous ?**
> D'abord je lui demande son budget et son horizon, parce que c'est ca qui
> determine la structure. S'il veut de la certitude, un terme sec - gratuit mais
> il perd tout gain favorable. S'il veut garder du potentiel, un tunnel, souvent
> a prime nulle. Et je lui dis des le depart qu'une couverture se restructure si
> le marche bouge.

**6. Qu'est-ce que le delta ?**
> La sensibilite du prix de l'option au sous-jacent, et donc la quantite a
> couvrir. Un call a la monnaie est autour de 0,50.

**7. Gamma et theta ?**
> Les deux faces d'une meme piece. Etre long gamma, c'est etre paye pour
> rebalancer sa couverture quand le marche bouge - et ce privilege se paie en
> theta chaque jour.

**8. Qu'est-ce que le smile ?**
> Black-Scholes suppose une volatilite unique ; le marche en cote une differente
> par strike. Le smile est cette courbe, et le skew son asymetrie. Il dit quelle
> direction fait peur au marche.

**9. Qu'est-ce que le DV01 ?**
> La variation de valeur pour un point de base. C'est la seule mesure de
> sensibilite qui s'additionne entre instruments differents.

**10. Que signifie une courbe inversee ?**
> Que le marche anticipe des baisses de taux, donc un ralentissement.
> Historiquement c'est le meilleur signal avance de recession, mais avec un
> delai de douze a vingt-quatre mois. C'est un signal, pas un calendrier.

**11. Quel est votre plus gros defaut ?**
> Je vais trop vite au resultat. J'ai appris a le corriger en me forcant a
> verifier le sens d'un calcul avant sa valeur - sur un desk, se tromper de sens
> coute plus cher que se tromper de decimale.

**12. Vous n'avez jamais travaille en salle de marche.**
> C'est exact, et c'est ce que je viens chercher. Ce que j'apporte, c'est le
> socle technique et l'habitude de me preparer : je ne decouvrirai pas les
> produits le premier jour.

**13. Vous parlez de Python. Vous etes developpeur ?**
> Non, et je ne cherche pas a l'etre. Python est un outil : il me fait gagner du
> temps sur l'analyse pour que je le passe sur la decision.

**14. Qu'est-ce qui bouge sur le marche en ce moment ?**
> Le repricing du taux neutre, avec le petrole pres de 100 dollars et des
> rendements obligataires au plus haut depuis des annees. Et cote change,
> l'intervention conjointe Etats-Unis-Japon de cet ete reste la reference : la
> plus grosse depuis quinze ans, executee sur une fenetre tres courte.

**15. Et si ce n'est pas le FX ?**
> Mon objectif est d'apprendre le metier en salle. Le FX est ce que je connais
> le mieux et ce que je vise, mais je ne refuserai pas un desk ou j'apprends. Je
> prefere etre honnete : je ne pretendrai pas maitriser ce que je n'ai pas
> pratique.

---

## 7. LES TROIS QUESTIONS A POSER

Jamais « quelles sont les prochaines etapes » en premier.

> Quelle part du flux le desk internalise-t-il ?

> Est-ce que les fixings locaux imposent une execution differente de ce que vous
> faites en G10 ?

> Qu'est-ce qui distingue un bon sales d'un sales moyen sur ce desk ?

---

## 8. LE PROMPT GEMINI - pour la suite

```
Tu es un professionnel qui recrute un stagiaire de fin d'etudes pour un desk
[FX Sales / taux / credit / commodities] a Paris.

Mene un entretien de 20 minutes en francais, ton direct, sans complaisance.
Alterne : une question de motivation, une question technique, une mise en
situation client. Si je reste vague ou si je bluffe, creuse jusqu'a ce que ca
casse. Ne me felicite pas par politesse.

A la fin, donne-moi exactement 4 points :
1. Ou j'ai bluffe
2. Ou j'aurais du dire "je ne sais pas" et ne l'ai pas fait
3. Quelle reponse etait trop longue
4. Est-ce que tu me prendrais, et pourquoi

Ensuite on recommence en anglais.
```

**Comment t'en servir :** commence par le desk que tu connais **le moins**.
C'est inconfortable, c'est exactement le but.

> ⚠️ **Le seul vrai test :** si tu peux redire la meme chose **avec d'autres
> mots** a deux jours d'intervalle, c'est acquis. Si tu ne sais la dire que
> d'une seule facon, c'est de la recitation - et une recitation s'entend.

---

## 9. LES CHIFFRES A AVOIR EN TETE

| Sujet | Valeur |
|---|---|
| Marche FX mondial | **~9 600 Md USD/jour** |
| 0,5 pip sur 10 M EUR/USD | **500 USD** |
| Vol 13 %/an en journalier | **0,82 %** |
| Reduction de vol, option asiatique | **~42 %** (racine de 3) |
| Call BS (100/105/3 %/25 %/0,5 an) | **5,5760** |
| DV01, 10 M EUR, duration mod. 4,53 | **4 530 EUR/bp** |
| Deutsche Bank, part de marche FX | **15,18 %** (Euromoney 2025) |
| Deutsche Bank FIC T2 2026 | **2 614 M EUR, +16 %** |
| ShockDesk | **Sharpe 1,67, DD max 8 bp** |

---

## 10. Ce qu'il faut retenir, et rien d'autre

- **Conclusion d'abord, un chiffre, puis se taire.**
- **Le sens avant la valeur.** Se tromper de sens coute plus cher que se tromper
  de decimale.
- **Un forward est un ecart de taux, pas une prevision.**
- **Gamma et theta sont la meme piece.**
- **Le DV01 est la seule mesure qui s'additionne.**
- **On ne defend pas un prix, on propose une alternative.**
- **« Je ne sais pas » n'elimine personne. Bluffer, si.**
- **Une recitation s'entend.** Le but n'est pas de retenir les mots, c'est que
  la structure du raisonnement soit automatique.
