# 150 questions d'entretien — FX, LatAm et Front Office

> **A quoi sert ce document.** A verifier que ce que tu as lu est devenu
> disponible a l'oral. Chaque question est suivie d'une reponse **courte, dite
> en douze a vingt secondes**. Ce n'est pas un cours : c'est un banc d'essai.
>
> **Comment s'en servir.** Reponds **a voix haute** avant de lire la reponse.
> Si tu hesites plus de trois secondes, la connaissance est lue, pas acquise :
> coche la question et reviens-y. Ne lis jamais les 150 d'affilee — trente par
> session, maximum.
>
> **Les chiffres.** Ils sont dates de septembre 2026. Un chiffre se perime ; le
> **raisonnement** qui va avec, non. En entretien, si tu n'es pas sur d'un
> niveau, donne l'ordre de grandeur et dis-le : *« autour de 5,15, je n'ai pas
> l'ecran devant moi »*. **Inventer un niveau est plus grave que ne pas savoir.**
>
> **Le perimetre.** Le cœur est FX et Amerique latine. Mais les sections 8 et 9
> couvrent les taux, le credit et les derives exotiques : si un desk te rappelle
> pour autre chose que le FX, tu ne dois pas etre pris de court.

---

## Section 1 — Le marche des changes : structure et vocabulaire (Q1-Q20)

**Q1. Quelle est la taille du marche des changes ?**
Environ **9 600 milliards de dollars par jour** (enquete triennale BRI, avril
2025). C'est le marche le plus liquide du monde, tres loin devant les actions.
A retenir : l'ordre de grandeur, pas la decimale.

**Q2. Comment lit-on une paire de devises ?**
La premiere devise est la **devise de base**, la seconde la **devise de
cotation**. EUR/USD = 1,17 signifie qu'un euro vaut 1,17 dollar. Acheter la
paire, c'est acheter la base et vendre la cotation.

**Q3. Qu'est-ce qu'un pip ?**
La plus petite variation standard d'un cours, generalement la **quatrieme
decimale** (0,0001). Exception : les paires en yen, ou c'est la deuxieme
decimale (0,01).

**Q4. Combien vaut un pip sur 1 million d'euros en EUR/USD ?**
**100 dollars.** 1 000 000 × 0,0001. Sur USD/JPY, un pip sur 1 million de
dollars vaut environ 64 dollars ; sur USD/BRL, environ 19 dollars.

**Q5. Qu'est-ce que le bid et le ask ?**
Le **bid** est le prix auquel le teneur de marche achete, l'**ask** (ou offer)
celui auquel il vend. Le client subit toujours l'ecart. La difference s'appelle
le **spread**, et c'est la remuneration du market maker.

**Q6. Qu'est-ce qu'un market maker ?**
Un intervenant qui affiche en permanence un prix a l'achat et a la vente, et
s'engage a traiter. Il prend un risque d'inventaire en echange du spread.

**Q7. Que signifie « capturer du spread » ?**
Encaisser l'ecart bid-ask sur un flux client. Exemple concret : **0,5 pip sur
10 millions d'EUR/USD, c'est 500 dollars**. Le metier de flux, c'est repeter
cette operation des centaines de fois par jour.

**Q8. Qu'est-ce qu'un RFQ ?**
*Request for quote* : le client demande un prix ferme sur un montant et une
echeance precis. Le sales repond par une fourchette, le client traite ou non.
C'est le mode dominant sur le corporate.

**Q9. Qu'est-ce que le streaming ?**
La diffusion continue de prix executables sur une plateforme electronique, sans
demande prealable. Le client clique et traite. C'est le mode dominant sur les
paires liquides.

**Q10. Qu'est-ce que le hit ratio ?**
La proportion de prix cotes qui sont effectivement traites par le client. Un
hit ratio trop bas signifie qu'on cote trop large ; trop haut, qu'on cote trop
serre et qu'on est en train de perdre de l'argent.

**Q11. Qu'est-ce qu'internaliser un flux ?**
Apparier en interne deux ordres clients de sens opposes, sans passer par le
marche. La banque evite le cout d'execution externe et garde le spread des deux
cotes. **C'est la variable centrale de la rentabilite d'une plateforme eFX.**

**Q12. Qu'est-ce que le last look ?**
Un delai de quelques millisecondes pendant lequel le teneur de marche peut
refuser un ordre apres reception. Pratique controversee, encadree par le
**FX Global Code**, parce qu'elle peut desavantager le client.

**Q13. Qu'est-ce que le FX Global Code ?**
Un code de bonne conduite du marche des changes, publie en 2017 apres les
scandales de manipulation des fixings. Non contraignant juridiquement, mais
signe par toutes les grandes banques.

**Q14. Qu'est-ce que le market impact ?**
Le fait qu'un ordre de taille importante deplace le marche contre celui qui
l'execute. C'est le principal cout cache d'une execution mal geree, et la
raison d'etre des algorithmes d'execution.

**Q15. Qu'est-ce que le skew ?**
L'asymetrie du prix de la volatilite entre options d'achat et de vente. Si le
marche craint une depreciation brutale d'une devise, les options de vente
coutent plus cher : le skew est dit charge. **Sur les devises emergentes, le
skew est structurellement oriente vers la depreciation.**

**Q16. Qu'est-ce qu'un risk reversal ?**
La difference de volatilite implicite entre un call et un put de meme delta.
C'est la mesure standard du skew, et un indicateur direct du sentiment du
marche sur une devise.

**Q17. Qu'est-ce qu'un fixing ?**
Un cours de reference officiel, calcule a heure fixe, utilise pour valoriser
des contrats ou regler des produits. Le **WM/Reuters de 16 h Londres** est le
plus utilise au monde.

**Q18. Quelles sont les trois grandes sessions de marche ?**
Asie, Europe, Amerique du Nord. Le marche est ouvert **24 heures sur 24, cinq
jours sur sept**. La liquidite culmine sur le **chevauchement Londres-New York**,
entre 13 h et 17 h heure de Paris.

**Q19. Qui sont les intervenants du marche des changes ?**
Les banques (teneurs de marche), les entreprises (couverture), les
gestionnaires d'actifs, les hedge funds, les banques centrales, et les
plateformes electroniques. **Seule une minorite du volume est du commerce
reel** : l'essentiel est financier.

**Q20. Quelle est la difference entre sell-side et buy-side ?**
Le sell-side (la banque) fournit liquidite et service ; le buy-side (le client
final) prend des positions. **Un sales est du cote sell-side : il n'a pas de
position directionnelle, il sert un flux.**

---

## Section 2 — Change a terme et parite des taux (Q21-Q40)

**Q21. Qu'est-ce qu'une operation de change au comptant ?**
Un echange de deux devises livre a **J+2** ouvres. C'est le produit de base du
marche.

**Q22. Qu'est-ce qu'un change a terme ?**
Un echange de deux devises a une date future, a un cours fixe aujourd'hui. On
l'appelle aussi **terme sec** quand il est ferme et sans option.

**Q23. Comment se calcule un cours a terme ?**
Par la **parite des taux d'interet couverte** : le cours a terme egale le
comptant multiplie par le rapport des facteurs de capitalisation des deux
devises. Formule : F = S × (1 + r_cotation × t) / (1 + r_base × t).

**Q24. Pourquoi cette formule, et pas une prevision ?**
Parce que **sinon il y aurait un arbitrage sans risque**. Si le terme s'ecarte
de la parite, on emprunte dans une devise, on place dans l'autre, on couvre au
terme et on encaisse la difference. **Le forward n'est pas une prevision : c'est
un differentiel de taux.**

**Q25. Formule-le en anglais.**
*« The forward isn't a forecast — it's just the rate differential. »* A savoir
par cœur : c'est la phrase de secours la plus rentable de tout l'entretien.

**Q26. Qu'est-ce que le report et le deport ?**
Si la devise cote plus cher a terme qu'au comptant, elle est en **report** ; si
elle cote moins cher, en **deport**. **Regle : la devise dont le taux d'interet
est le plus eleve est en deport.**

**Q27. Pourquoi la devise a taux eleve se deprecie-t-elle a terme ?**
Parce que sinon on emprunterait dans la devise a taux bas pour placer dans
celle a taux haut sans risque. Le deport compense exactement l'ecart de taux.

**Q28. Qu'est-ce qu'un point de terme ?**
La difference entre le cours a terme et le cours comptant, exprimee en pips.
C'est ainsi que le marche cote le terme : on cote les points, pas le cours
complet.

**Q29. Calcul mental d'un point de terme ?**
**Comptant × ecart de taux × duree.** Exemple : USD/BRL a 5,16, ecart de taux
d'environ 10,4 points, trois mois : 5,16 × 0,104 × 0,25 ≈ 0,134, soit environ
1 340 pips.

**Q30. Qu'est-ce qu'un swap de change ?**
L'echange simultane de deux devises au comptant **et** l'operation inverse a
terme. Economiquement, c'est un **pret croise garanti** : on prete une devise et
on emprunte l'autre, sans risque de change.

**Q31. A quoi sert un swap de change pour un corporate ?**
A **decaler une echeance**. Si un client a couvert une recette a trois mois mais
que le paiement glisse d'un mois, on ne defait pas la couverture : on la roule
par un swap.

**Q32. Quelle est la difference entre swap de change et swap de devises ?**
Le swap de change (*FX swap*) porte sur le principal, a court terme, sans
echange d'interets. Le **swap de devises** (*cross-currency swap*) echange aussi
les flux d'interets sur plusieurs annees.

**Q33. Qu'est-ce qu'un NDF ?**
Un *non-deliverable forward* : un terme **sans livraison physique**. A
l'echeance, on ne s'echange que la difference entre le cours convenu et un
**fixing** officiel, reglee en dollars.

**Q34. Pourquoi les NDF existent-ils ?**
Parce que certaines devises ne sont pas librement convertibles ou transferables
hors du pays. Le NDF permet de prendre une exposition **sans jamais toucher la
devise locale**.

**Q35. Comment se calcule le reglement d'un NDF ?**
Nominal × (Forward − Fixing) / Fixing. **Attention : on divise par le fixing**,
parce que le reglement est verse en dollars et non en devise locale. C'est
l'erreur classique.

**Q36. Quelles devises latino-americaines sont non livrables ?**
Le **real bresilien (BRL)**, le **peso colombien (COP)** et le **peso chilien
(CLP)**. Le **peso mexicain (MXN)** est livrable — c'est la grande difference
regionale.

**Q37. Qu'est-ce que la parite des pouvoirs d'achat ?**
La theorie selon laquelle les taux de change s'ajustent pour egaliser le prix
d'un meme panier de biens. **Elle ne fonctionne pas a court terme** : c'est un
ancrage de long terme, pas un outil de trading.

**Q38. Qu'est-ce que la parite des taux non couverte ?**
L'idee que l'ecart de taux devrait etre compense par une depreciation attendue
de la devise a taux eleve. **Empiriquement fausse** : c'est precisement ce
dementi qui rend le carry trade rentable.

**Q39. Qu'est-ce qu'un cross ?**
Une paire ne contenant pas le dollar, comme EUR/JPY. Historiquement calculee via
le dollar, d'ou parfois une liquidite moindre et un spread plus large.

**Q40. Qu'est-ce qu'une position de change ?**
Le solde net des avoirs et engagements dans une devise. Tant qu'elle n'est pas
nulle, l'entreprise est exposee. **Le premier travail d'un tresorier n'est pas
de couvrir : c'est de mesurer sa position.**

---

## Section 3 — Options de change et structures (Q41-Q62)

**Q41. Qu'est-ce qu'une option de change ?**
Le **droit, non l'obligation**, d'acheter (call) ou de vendre (put) une devise a
un prix fixe, a une date donnee. L'acheteur paie une prime ; le vendeur
l'encaisse et supporte le risque.

**Q42. Quelle est la difference entre europeenne et americaine ?**
L'europeenne ne s'exerce qu'a l'echeance ; l'americaine a tout moment. **Sur le
change, l'europeenne domine largement.**

**Q43. Quel modele utilise-t-on pour pricer une option de change ?**
**Garman-Kohlhagen**, qui est l'adaptation de Black-Scholes au change : on
remplace le dividende par le taux d'interet de la devise etrangere.

**Q44. Quels sont les parametres du modele ?**
Spot, strike, maturite, les **deux** taux d'interet, et la **volatilite**. Tous
sont observables sauf la volatilite : **c'est le seul vrai prix negocie.**

**Q45. Qu'est-ce que le delta ?**
La sensibilite du prix de l'option a une variation du sous-jacent. Un delta de
0,46 signifie qu'une hausse d'un point du spot fait monter l'option de 0,46.
C'est aussi la quantite a detenir pour se couvrir.

**Q46. Qu'est-ce que le gamma ?**
La sensibilite du delta lui-meme. Un gamma eleve signifie que la couverture doit
etre reajustee souvent. **C'est le grec qui coute cher a gerer.**

**Q47. Qu'est-ce que le vega ?**
La sensibilite du prix a la volatilite implicite. Un vendeur d'options est
vega-negatif : il perd si la volatilite monte.

**Q48. Qu'est-ce que le theta ?**
La perte de valeur de l'option due au simple ecoulement du temps. L'acheteur
d'option paie du theta tous les jours ; le vendeur l'encaisse.

**Q49. Qu'est-ce que la volatilite implicite ?**
La volatilite que le marche anticipe, deduite du prix de l'option. A distinguer
de la volatilite **historique**, qui est constatee. **L'ecart entre les deux est
une information de marche a part entiere.**

**Q50. Comment passe-t-on d'une volatilite annuelle a une volatilite
journaliere ?**
On divise par la **racine carree du nombre de jours de bourse**, environ 252.
Une volatilite de 13 % par an donne 13 % / racine(252) ≈ **0,82 % par jour**.

**Q51. Pourquoi la racine carree ?**
Parce que la variance est additive dans le temps, pas l'ecart-type. Sur n jours
independants, la variance est multipliee par n, donc l'ecart-type par racine(n).

**Q52. Que dit cette volatilite journaliere sur le carry bresilien ?**
Qu'elle le domine. **Trois seances a un ecart-type effacent un trimestre de
portage.** C'est la phrase qui montre qu'on a compris le rapport
rendement-risque du carry.

**Q53. Qu'est-ce qu'un tunnel, ou collar ?**
Le client **achete une protection** et **finance cette protection en vendant une
option de l'autre cote**. Cout nul ou quasi nul, mais gain plafonne. *« On
echange du potentiel contre de la gratuite. »*

**Q54. Qu'est-ce qu'un terme booste ?**
Un terme a cours ameliore : le client obtient un meilleur cours que le terme
sec, mais s'engage, si un niveau est franchi, a traiter **le double du
nominal**. On dit aussi « terme a double vitesse ».

**Q55. Quel est le risque du terme booste ?**
Le client **vend de la convexite** sans toujours le comprendre : il double son
exposition precisement dans le scenario qui lui est defavorable. C'est la
structure la plus vendue aux corporates, et la plus dangereuse.

**Q56. Qu'est-ce qu'un accumulateur ?**
Une structure ou le client accumule un montant a cours fixe, periode apres
periode, tant que le marche reste dans une zone. En sortie de zone, le contrat
se desactive ou double. **Les accumulateurs ont fait de gros degats chez des
corporates asiatiques en 2008.**

**Q57. Qu'est-ce qu'une option a barriere ?**
Une option qui s'active (*knock-in*) ou se desactive (*knock-out*) si le spot
touche un niveau. **Elle coute moins cher qu'une vanille**, parce que la
protection peut disparaitre au pire moment.

**Q58. Quand proposer une barriere plutot qu'une vanille ?**
Quand le client a une **vue precise** sur un niveau qu'il juge inatteignable, et
qu'il accepte d'echanger de la securite contre du prix. Jamais a un client qui
ne comprend pas ce qu'il abandonne.

**Q59. Un client veut se couvrir mais ne veut rien payer. Que proposes-tu ?**
Un **tunnel a prime zero**. Et surtout, je lui explique la contrepartie : il
renonce au gain au-dela d'un niveau. **Le devoir de conseil, c'est d'enoncer ce
qu'on abandonne, pas seulement ce qu'on obtient.**

**Q60. Qu'est-ce qu'une restructuration ?**
Modifier une couverture existante dont le marche s'est ecarte. Exemple : rouler
l'echeance, deplacer un strike, monetiser une partie de la valeur. **Un junior
sait vendre une couverture ; un sales sait quoi faire six mois plus tard quand
elle est a contresens.**

**Q61. Formule-le en une phrase d'entretien.**
*« Une couverture n'est pas un acte unique. Quand le spot a bouge de 8 %, la
valeur ajoutee du sales c'est de proposer une restructuration, pas de constater
la perte avec le client. »*

**Q62. Qu'est-ce que la couverture interne ?**
Reduire l'exposition **sans produit bancaire** : facturer dans sa propre devise,
compenser achats et ventes (*netting*), adosser les devises de cout et de
recette. **Un bon sales sait dire a un client qu'il n'a pas besoin de produit.**

---

## Section 4 — Le carry trade et les strategies (Q63-Q78)

**Q63. Qu'est-ce que le carry trade ?**
Emprunter dans une devise a taux bas pour placer dans une devise a taux eleve,
en laissant la position **non couverte**. Le gain est l'ecart de taux ; le
risque est le change.

**Q64. Pourquoi ne peut-on pas couvrir un carry ?**
Parce que **couvert, le carry est nul par construction**. Le forward integre
exactement l'ecart de taux. **Le carry n'est pas un arbitrage : c'est une prime
de risque.**

**Q65. Chiffre le carry bresilien.**
Selic a 14,00 % contre Fed a 3,50-3,75 % : environ **10,4 points d'ecart**. Sur
1 million de dollars a trois mois, cela represente environ **26 000 dollars**.
Sur le peso colombien environ 14 000, le mexicain 7 200, le chilien 2 200.

**Q66. Et le risque en face ?**
Une volatilite de 13 % par an sur le real, soit 0,82 % par jour. Trois seances
defavorables effacent le trimestre. **Le carry remunere un risque reel, il ne
le supprime pas.**

**Q67. Qu'est-ce qu'un « carry crash » ?**
L'effondrement simultane des devises a haut rendement quand l'aversion au
risque monte. Les positions se denouent toutes ensemble, la liquidite disparait.
**Le carry se comporte comme une vente d'assurance : petits gains reguliers,
perte brutale.**

**Q68. Qu'est-ce que le funding currency ?**
La devise empruntee pour financer le carry, historiquement le yen ou le franc
suisse. **Le vrai risque d'un carry, ce n'est pas la devise achetee : c'est le
cout de financement qui se retourne.**

**Q69. Comment un ecran de carry se lit-il en 2026 ?**
Les plafonds de taux dans le G10 **subventionnent le carry emergent** en
maintenant un cout de financement artificiellement bas. Tant que ce regime dure,
le flux vers l'emergent continue.

**Q70. Qu'est-ce qu'une strategie de couverture systematique ?**
Couvrir une proportion fixe de l'exposition, a intervalle regulier, sans vue de
marche. **Moins performant qu'une couverture opportuniste reussie, mais
beaucoup plus robuste** — et c'est ce que recommande la plupart des politiques
de change d'entreprise.

**Q71. Qu'est-ce qu'une politique de change ?**
Le document interne qui fixe **ce que l'entreprise couvre, dans quelle
proportion, sur quel horizon, et qui decide**. Sans politique de change, un
tresorier improvise, et c'est la que naissent les accidents.

**Q72. Qu'est-ce que le risque de transaction ?**
Le risque sur un flux futur deja engage : une facture en devise, une commande.
C'est le risque le plus simple a couvrir.

**Q73. Qu'est-ce que le risque de translation ?**
Le risque comptable de conversion des comptes d'une filiale etrangere. Il
n'affecte pas la tresorerie mais le bilan consolide. **Beaucoup d'entreprises
choisissent de ne pas le couvrir.**

**Q74. Qu'est-ce que le risque economique ?**
Le risque sur la competitivite future : un concurrent dont les couts sont dans
une devise faible. **C'est le plus difficile a mesurer et le plus dangereux, car
il ne figure sur aucune ligne comptable.**

**Q75. Qu'est-ce qu'un algorithme d'execution ?**
Un programme qui decoupe un ordre important en petits morceaux pour reduire le
market impact. **TWAP** lisse dans le temps, **VWAP** suit le volume,
l'**iceberg** cache la taille.

**Q76. Quand utiliser un algorithme plutot qu'un prix ferme ?**
Quand la taille est grande par rapport a la liquidite et que le client accepte
un risque de prix contre un moindre impact. **Un prix ferme transfere le risque
a la banque ; l'algorithme le laisse au client.**

**Q77. Qu'est-ce que le TCA ?**
*Transaction cost analysis* : la mesure a posteriori de la qualite d'execution,
comparee a un point de reference. De plus en plus demandee par les corporates
sophistiques.

**Q78. Comment ton projet ShockDesk se presente-t-il sur un desk ?**
Un backtest sur 25,5 millions de dollars, du 1er juillet au 28 aout 2026 :
**Sharpe de 1,67, drawdown maximum de 8 points de base, 21 trades**. Je dis
« backtest » spontanement, parce que confondre un backtest et un track record
est disqualifiant.

---

## Section 5 — L'Amerique latine : la region (Q79-Q100)

**Q79. Pourquoi l'Amerique latine plutot qu'une autre region emergente ?**
Parce que c'est la seule region emergente ou **le francais est inutile,
l'anglais insuffisant et l'espagnol decisif** — et que je parle espagnol. Et
parce que la plomberie de marche y est encore en construction, contrairement a
l'Asie.

**Q80. Quelles sont les principales devises de la region ?**
Le **real bresilien (BRL)**, le **peso mexicain (MXN)**, le **peso colombien
(COP)**, le **peso chilien (CLP)**, et plus marginalement le sol peruvien (PEN).

**Q81. Qu'est-ce qui distingue le MXN du BRL pour un desk ?**
Le peso est **livrable, tres liquide, negocie 24 h sur 24** : environ
153 milliards de dollars par jour, dont **82 % hors du Mexique**. Le real est
**non livrable**, traite en NDF, et l'essentiel de sa liquidite est onshore, sur
des horaires bresiliens.

**Q82. Pourquoi cette difference ?**
Choix de politique economique. Le Mexique a ouvert son compte de capital ; le
Bresil a conserve des contraintes sur la convertibilite. **Ce n'est pas une
question de taille d'economie, c'est une question de regime.**

**Q83. Pourquoi le MXN et le BRL ne reagissent-ils pas aux memes chocs ?**
Le Mexique exporte des **biens manufactures** vers les Etats-Unis : il suit le
cycle americain. Le Bresil exporte des **matieres premieres** vers la Chine : il
suit le cycle chinois et les termes de l'echange.

**Q84. Qu'est-ce que les termes de l'echange ?**
Le rapport entre les prix des exportations et ceux des importations d'un pays.
Quand le minerai de fer monte, les termes de l'echange bresiliens s'ameliorent
et le real a tendance a s'apprecier.

**Q85. Le petrole monte : que se passe-t-il sur les devises emergentes ?**
**Deux canaux opposes.** Canal des termes de l'echange : les exportateurs
s'apprecient. Canal financier : hausse de l'inflation, Fed plus dure, dollar
fort, sorties de capitaux emergents. **Le second l'emporte souvent a court
terme.**

**Q86. Pourquoi cette reponse est-elle bonne en entretien ?**
Parce que la mauvaise reponse est monocausale. Dire « ca depend, il y a deux
canaux et voici lequel domine quand » montre qu'on a une grille, pas une
opinion.

**Q87. Quelles sont les banques centrales de la region et leurs taux ?**
Bresil **Selic 14,00 %**, Colombie **BanRep 9,25 %**, Mexique **Banxico
6,50 %**, Chili **BCCh 4,50 %**. Pour reference, Fed a 3,50-3,75 %.

**Q88. Pourquoi les taux reels latino-americains sont-ils si eleves ?**
Parce que la **credibilite monetaire y a ete detruite puis reconstruite**. Apres
des decennies d'inflation, ces banques centrales paient une prime permanente
pour etre crues. **Ce n'est pas une anomalie de marche, c'est un heritage.**

**Q89. Quelle est la phrase a placer la-dessus ?**
*« Le taux reel bresilien n'est pas une anomalie, c'est le prix d'une
credibilite reconstruite apres l'hyperinflation. C'est pour ca que la prime ne
disparait pas quand l'inflation baisse. »*

**Q90. Qu'est-ce que la decennie perdue ?**
Les annees 1980 en Amerique latine : crise de la dette, hyperinflation,
stagnation. C'est le traumatisme fondateur qui explique les institutions
monetaires actuelles de la region.

**Q91. Qu'est-ce que le Plano Real ?**
Le plan de stabilisation bresilien du **1er juillet 1994**, qui a mis fin a
l'hyperinflation en creant une nouvelle monnaie indexee puis ancree au dollar.
**C'est l'acte de naissance du real.**

**Q92. Quand le real est-il passe en change flottant ?**
En **janvier 1999**, apres l'echec de la defense de l'ancrage. Le Bresil adopte
alors le triptyque moderne : **change flottant, ciblage d'inflation,
discipline budgetaire affichee**.

**Q93. Qu'est-ce que la crise du peso mexicain ?**
**Decembre 1994**, l'« effet tequila » : devaluation brutale apres epuisement des
reserves, contagion regionale, sauvetage international. Le cas d'ecole de la
crise de change en regime d'ancrage.

**Q94. Quel est le calendrier politique regional en 2026 ?**
La **presidentielle bresilienne d'octobre 2026** domine tout. Un calendrier
electoral se traduit directement en prime de risque sur la courbe locale et sur
le skew des options.

**Q95. Comment un sales parle-t-il de politique sans se griller ?**
En parlant **de la reaction du marche, jamais de son opinion**. On dit « le
marche price une prime electorale sur la partie longue », jamais « je pense que
tel candidat serait meilleur ».

**Q96. Qu'est-ce que le risque souverain ?**
Le risque qu'un Etat ne puisse ou ne veuille honorer sa dette. Il se lit dans
les spreads de CDS et dans l'ecart de rendement avec le Tresor americain.

**Q97. Qu'est-ce qu'un CDS ?**
*Credit default swap* : un contrat d'assurance contre le defaut d'un emetteur.
L'acheteur paie une prime periodique ; le vendeur indemnise en cas de defaut.
**Le niveau du CDS souverain est le thermometre du risque pays.**

**Q98. Qu'est-ce que le dollar index, et pourquoi compte-t-il ici ?**
Un indice du dollar contre un panier de devises developpees. **Quand le dollar
se renforce globalement, les devises emergentes souffrent presque
mecaniquement**, quels que soient leurs fondamentaux propres.

**Q99. Qu'est-ce que le « risk-on / risk-off » ?**
Un regime de marche ou tous les actifs risques montent ou baissent ensemble,
independamment de leur valeur propre. **En risk-off, la correlation entre
devises emergentes tend vers 1** : la diversification disparait quand on en a
besoin.

**Q100. Pourquoi le desk LatAm est-il souvent a New York ou Londres ?**
Fuseau horaire et proximite des investisseurs. Cela dit, **les corporates
europeens exposes a la region sont couverts depuis Paris** : c'est precisement
l'espace que je vise.

---

## Section 6 — Le Bresil en profondeur (Q101-Q125)

**Q101. Qu'est-ce que la Selic ?**
Le taux directeur bresilien, l'equivalent du taux des fonds federaux americains.
Fixe par le **Copom**, le comite de politique monetaire de la banque centrale.
Actuellement a **14,00 %**.

**Q102. Qu'est-ce que le Copom ?**
*Comite de politique monetaire* du Banco Central do Brasil. Il se reunit **huit
fois par an**, sur deux jours, et publie sa decision le mercredi soir. Les
minutes paraissent le mardi suivant.

**Q103. Donne le calendrier 2026 du Copom.**
27-28 janvier, 17-18 mars, 28-29 avril, 16-17 juin, 4-5 aout, **15-16 septembre**,
3-4 novembre, 8-9 decembre. **Savoir citer la prochaine date est le detail qui
fait la difference.**

**Q104. Qu'est-ce que le PTAX ?**
Le cours de reference officiel USD/BRL publie par la banque centrale. Il est
calcule comme la **moyenne de quatre releves** effectues dans la journee aupres
des teneurs de marche.

**Q105. Pourquoi le PTAX est-il important pour un sales ?**
Parce que **tous les NDF sur le real se reglent contre lui**. Ce n'est pas un
cours de marche instantane mais une moyenne : cela cree une **vraie contrainte
d'execution** les jours de fixing, que l'Asie ne connait pas sous cette forme.

**Q106. C'est quoi, le detail qui prouve la passion ?**
Exactement celui-la. **Le PTAX est une moyenne de quatre releves quotidiens** :
c'est technique, verifiable, et aucun candidat generaliste ne le sait.

**Q107. Quelle est la part du flux bresilien sur USD/BRL ?**
Environ **90 %**. Le marche bresilien est massivement un marche dollar-real : les
crosses y sont marginaux.

**Q108. Qu'est-ce que la B3 ?**
La bourse bresilienne, nee de la fusion de la Bovespa et de la BM&F. **Elle
concentre une part inhabituellement elevee du volume de change bresilien**, sous
forme de futures plutot que d'OTC.

**Q109. Qu'est-ce que le contrat DOL ?**
Le future dollar-real de la B3, d'un nominal de **50 000 dollars**, cote en
reais pour 1 000 dollars, a reglement financier. Le mini, **WDO**, vaut un
cinquieme, soit 10 000 dollars.

**Q110. Pourquoi le future domine-t-il l'OTC au Bresil ?**
Histoire et reglementation : le marche s'est structure autour de la bourse, avec
une chambre de compensation centrale. **Consequence pratique : le prix directeur
du real se forme souvent sur le future, pas sur le spot.**

**Q111. Qu'est-ce que le cupom cambial ?**
Le **taux d'interet en dollars au Bresil** : ce que rapporte un dollar place
localement. C'est l'ecart entre le taux en reais et la depreciation implicite du
real. Le future correspondant s'appelle **DDI**.

**Q112. Pourquoi le cupom cambial est-il un bon sujet ?**
Parce que c'est **l'indicateur de tension sur la liquidite en dollars au
Bresil**. Quand les dollars deviennent rares localement, il bouge avant tout le
reste. C'est un signal que peu de candidats savent lire.

**Q113. Qu'est-ce que le contrat 6L du CME ?**
Le future dollar-real listé a Chicago, **regle en cash contre le PTAX**. Il
permet une exposition au real depuis les Etats-Unis sans acces au marche local.

**Q114. Quel est le montant de la dette federale bresilienne ?**
Environ **8 635 milliards de reais** en mars 2026, dont **96,2 % libelles en
reais**, a un cout moyen de **13,92 %**.

**Q115. Pourquoi le fait qu'elle soit en monnaie locale est-il decisif ?**
Parce que **le Bresil ne peut pas faire defaut sur une dette qu'il imprime**. Le
risque n'est pas le defaut : c'est l'inflation et la depreciation. **C'est
exactement la lecon des crises des annees 1990, ou la dette etait en dollars.**

**Q116. Quel est le niveau de dette rapporte au PIB ?**
Environ **81,9 % du PIB** en dette brute. Eleve pour un pays emergent, mais a
lire avec la structure de financement.

**Q117. Quels sont les soldes budgetaires ?**
Un deficit primaire d'environ **1,19 %** du PIB et un deficit nominal d'environ
**9,99 %**. **Presque tout l'ecart entre les deux, c'est le service de la
dette.**

**Q118. Fais l'analyse en une phrase.**
*« Le Bresil emprunte a 14,39 % sur dix ans avec une dette a 81,9 % du PIB.
Deficit primaire 1,2 %, nominal 10 % : presque tout l'ecart, c'est le service de
la dette. C'est ca qui tient le real — le carry est enorme, mais il remunere un
risque budgetaire reel. »*

**Q119. A quoi ressemble la courbe des taux bresilienne ?**
Au 10 septembre 2026 : environ **13,60 % a un an, 14,30 % a cinq ans, 14,39 % a
dix ans**. Une courbe presque plate a un niveau tres eleve.

**Q120. Que signifie une courbe plate a 14 % ?**
Que le marche n'anticipe **ni detente durable, ni normalisation**. Il exige la
meme remuneration a un an et a dix ans : c'est un signal de defiance budgetaire
plus que de tension monetaire.

**Q121. Qu'est-ce que la BNDES ?**
La banque publique de developpement bresilienne, acteur central du financement
des entreprises du pays. **Elle influence directement la demande de couverture
de change des corporates locaux.**

**Q122. Qu'est-ce que le regime de ciblage d'inflation bresilien ?**
La banque centrale s'engage sur une cible d'inflation annuelle, avec un
intervalle de tolerance, et doit s'expliquer publiquement en cas de depassement.
En place depuis **1999**, juste apres le passage au flottement.

**Q123. La banque centrale bresilienne est-elle independante ?**
Oui, depuis une loi de 2021 qui a fixe des mandats decales entre le president de
l'institution et le pouvoir politique. **C'est un sujet sensible et recurrent
dans le debat public bresilien.**

**Q124. Comment suis-tu le Bresil au quotidien ?**
La chaine YouTube du **Banco Central do Brasil** pour les conferences de presse
apres chaque Copom, le site de la banque centrale pour les series, et
**Bloomberg Linea** pour l'actualite regionale. Je lis le portugais suffisamment
pour les communiques.

**Q125. Qu'est-ce que le « repasse cambial » ?**
Le **coefficient de transmission du taux de change a l'inflation**. Au Bresil il
est eleve : une depreciation se retrouve vite dans les prix, ce qui contraint la
banque centrale a reagir au change. **C'est le lien direct entre FX et politique
monetaire.**

---

## Section 7 — Le metier de sales et le comportement de desk (Q126-Q140)

**Q126. Quelle est la difference entre un sales et un trader ?**
Le trader tient un book et gere un risque. Le **sales est l'interface client** :
il comprend le besoin, propose une structure, negocie le prix avec son trader et
execute. **Il n'a pas de position directionnelle.**

**Q127. Quelle est la difference entre un sales et un strategist ?**
Le strategist produit de la recherche et des recommandations ; il ne traite pas.
**Confondre les deux en entretien est une erreur frequente et visible.**

**Q128. Comment gagne l'argent un desk de flux ?**
Par le **spread** sur un volume important, pas par la direction du marche. La
performance se mesure en marge par million traite, pas en gain de position.

**Q129. Un client demande un prix hors de ta grille. Que fais-tu ?**
Trois cas. Dans la grille : je cote seul. Hors norme mais dans mon perimetre :
je cote **large** et j'escalade en parallele. Au-dela : je le dis, je prends la
demande et je reviens. **Je n'invente jamais un prix.**

**Q130. Tu ne connais pas un niveau. Que reponds-tu ?**
*« I don't have that in front of me — where is it trading? »* **Inventer un
niveau est infiniment plus grave que ne pas savoir.** Sur un desk, un chiffre
faux se propage.

**Q131. Quelles sont les qualites d'un bon sales ?**
La clarte sous pression, la memoire des besoins clients, et **la capacite a dire
non**. Un sales qui vend une structure inadaptee gagne une fois et perd le
client.

**Q132. Quelle est la structure d'une bonne reponse orale ?**
**La conclusion d'abord**, puis un chiffre, puis on s'arrete. Sur un desk, on
n'a pas le temps d'ecouter une introduction. **Finir net et se taire fait partie
de la reponse.**

**Q133. Quelle est la taille d'un desk FX corporate en France ?**
Typiquement **cinq a quinze personnes** par segment de clientele, avec une
separation entre grands corporates et entreprises de taille intermediaire. Les
desks LatAm dedies sont beaucoup plus petits, souvent deux a quatre personnes.

**Q134. Pourquoi le FX plutot qu'une autre classe d'actifs ?**
*« C'est le marche le plus liquide du monde et pourtant tout n'y est pas resolu.
Sur EUR/USD l'electronification est terminee, les marges sont ecrasees. Sur le
LatAm, la plomberie se construit encore : les fixings locaux comme le PTAX
creent de vraies contraintes d'execution. C'est la que quelqu'un qui comprend a
la fois le flux client et l'outil a encore quelque chose a apporter. »*

**Q135. Comment presentes-tu Python sans passer pour un developpeur ?**
**Outil, decision, temps.** « J'automatise la recuperation des donnees de la
banque centrale bresilienne pour avoir la courbe a jour le matin : ca me fait
gagner vingt minutes et ca evite les erreurs de recopie. » **Jamais le langage
pour lui-meme.**

**Q136. Qu'est-ce que le VBA vient faire la-dedans ?**
Il est cite dans presque toutes les offres de FX sales corporate en France.
**L'atout automatisation vaut plus a Paris qu'a Londres**, parce que les desks
parisiens ont moins d'equipes quantitatives dediees.

**Q137. Pourquoi la France et pas Londres ?**
*« Le marche francais m'interesse parce que la clientele corporate y est tres
dense et que la relation de conseil y est plus forte. Et honnetement, un desk
parisien laisse plus de place a quelqu'un qui construit ses propres outils. »*
**Ne jamais mettre le visa en premier.**

**Q138. Quelles questions poses-tu a la fin ?**
Trois, et pas une de plus : quelle part du flux est internalisee ; est-ce que
les fixings locaux imposent une execution differente de l'Asie ; qu'est-ce qui
distingue un bon sales d'un sales moyen sur ce desk.

**Q139. Pourquoi ces questions-la ?**
Parce qu'elles sont **impossibles a poser sans connaitre le metier**, et qu'elles
laissent l'interlocuteur parler de son quotidien. Une question de candidat est
un test deguise.

**Q140. Comment montrer sa passion sans la declarer ?**
**Par un detail verifiable.** « Je suis passionne par le FX » ne vaut rien. « Le
Copom et la Fed decident les memes jours cette semaine, en sens opposes » vaut
tout. **La passion ne se declare pas, elle se deduit.**

---

## Section 8 — Si le desk est taux, credit ou exotique (Q141-Q150)

**Q141. Qu'est-ce que la duration ?**
La sensibilite du prix d'une obligation a une variation de taux, exprimee en
annees. Plus la duration est longue, plus le prix bouge pour un meme mouvement
de taux.

**Q142. Qu'est-ce que le DV01 ?**
La variation de valeur d'une position pour **un point de base** de mouvement de
taux. Sur 10 millions d'euros d'une obligation de duration modifiee 4,528, cela
fait environ **4 530 euros par point de base**.

**Q143. Donne un calcul obligataire complet.**
Une obligation a cinq ans, coupon 3 %, rendement 4 % : prix **95,55**, duration
modifiee **4,528**. C'est le calcul de base que tout entretien taux verifie.

**Q144. Qu'est-ce qu'une courbe des taux inversee ?**
Quand les taux courts depassent les taux longs. Historiquement un signal de
recession anticipee, parce que le marche price des baisses de taux futures.

**Q145. Qu'est-ce qu'un swap de taux ?**
L'echange d'un taux fixe contre un taux variable sur un nominal donne, sans
echange de principal. C'est le produit de couverture de taux le plus utilise par
les entreprises.

**Q146. Qu'est-ce qu'une option exotique ?**
Toute option dont le payoff n'est pas celui d'une vanille : barrieres,
asiatiques (moyenne), digitales (tout ou rien), lookback. **Elles se pricent
rarement en formule fermee : on passe par Monte-Carlo ou arbre.**

**Q147. Qu'est-ce qu'une option digitale ?**
Une option qui paie un montant fixe si une condition est remplie, rien sinon.
**Le risque de couverture explose pres du strike a l'echeance**, car le delta
devient instable.

**Q148. Qu'est-ce que Monte-Carlo ?**
Une methode de valorisation par simulation d'un grand nombre de trajectoires du
sous-jacent, dont on moyenne les payoffs actualises. **C'est la ou mon Python
sert vraiment** : simuler, tester, verifier un ordre de grandeur.

**Q149. Pourquoi tu ne vises pas le structuring ?**
*« Parce que ce qui m'interesse, c'est le contact client et la decision rapide,
pas la modelisation. J'ai les outils quantitatifs, je m'en sers pour aller plus
vite, mais mon metier c'est de comprendre un besoin et d'y repondre. »*
**Reponse ferme, assumee, sans s'excuser.**

**Q150. Et si on te propose un desk qui n'est pas le FX ?**
*« Ma specialisation aujourd'hui c'est le change et l'Amerique latine, parce que
j'ai construit quelque chose de precis dessus. Mais le socle — comprendre un
risque, le chiffrer, le dire clairement a un client — est le meme. Je suis
preneur de la conversation. »* **Ferme sur l'identite, ouvert sur
l'opportunite.**

---

## Comment s'entrainer avec ce document

**Trois passages, pas un.**

1. **Passage a plat.** Tu lis question et reponse, tu coches celles que tu ne
   savais pas. Duree : deux heures, sur deux jours.
2. **Passage a voix haute.** Question cachee, tu reponds, puis tu verifies.
   **Chronometre-toi : au-dela de vingt secondes, la reponse est trop longue.**
3. **Passage aleatoire.** Tirage au hasard, sans ordre, comme en entretien reel.
   C'est le seul qui compte vraiment.

**Les vingt questions a savoir sans reflechir :** Q4, Q7, Q11, Q23, Q24, Q26,
Q33, Q35, Q50, Q53, Q60, Q63, Q64, Q65, Q81, Q101, Q104, Q118, Q129, Q134.
Ce sont celles qui reviennent dans presque tous les entretiens de ce type.

> ⚠️ **Le piege de ce document.** Le connaitre par cœur ne suffit pas et peut
> meme nuire : une reponse recitee s'entend. **Le but est que la structure du
> raisonnement devienne automatique**, pas les mots. Si tu peux repondre la meme
> chose avec des mots differents deux jours de suite, c'est acquis.
