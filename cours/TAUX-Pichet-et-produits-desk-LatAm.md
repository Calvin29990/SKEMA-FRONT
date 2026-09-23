# Taux : ce que Pichet te donne, et ce qu'il ne te donnera pas
## Une heure, niveau desk, orientee produits LatAm

> **Deux avertissements avant de commencer, parce qu'ils changent ta facon de
> lire.**
>
> **① Le Pichet ne parle pas du Bresil.** *Guide pratique des obligations*,
> Eric Pichet, Sefi, 3e edition, collection « BTS Banque - Les pedagogiques ».
> Sommaire reel en deux parties : produits obligataires (histoire, typologie,
> evaluation) puis marches obligataires (fonctionnement, strategies, fiscalite).
> **La fiscalite y est francaise, les exemples y sont francais.** C'est un tres
> bon livre pour le socle. Ce n'est pas un livre sur l'Amerique latine, et aucun
> chapitre ne traitera la Selic ni le DI1.
>
> **② Il n'existe aucun ouvrage bresilien sur ScholarVox.** Tu ecris « les
> livres bresiliens de ScholarVox » — je dois te corriger : le catalogue SKEMA
> n'en contient pas sur les derives ou les taux bresiliens. Les deux seuls
> titres Bresil reperes sont **Dabene** (histoire politique de l'Amerique
> latine) et **Gambacurta-Scopello** sur le **BNDES** (economie politique du
> developpement) — aucun des deux n'est un livre de marches.
>
> **Conclusion : rien ne sera elude, parce qu'il n'y a rien a eluder.** Ce
> document contient donc la totalite du contenu Bresil, et il suppose seulement
> acquis le socle general que tu as deja lu (Ruttiens, Dupuy, Fernandez-Riou).

---

## Comment lire Pichet en une semaine : les trois filtres

Tu lis les livres en entier, c'est ton choix et il est bon. Mais lis-le avec
**trois questions en tete**, parce que ce sont elles qui transforment un manuel
BTS en outil de desk.

**Filtre 1 — « Quelle est la convention ? »** A chaque formule, demande-toi en
quelle base de jours elle est ecrite. Pichet ecrira en ACT/ACT ou 30/360, sans
le souligner, parce que pour un lecteur francais c'est evident. **Au Bresil ce
sera 252 jours ouvres et du compose.** Chaque fois que tu repereras la
convention implicite, tu auras un point de contraste.

**Filtre 2 — « Qui porte le risque ? »** Pichet raisonne en investisseur qui
detient un titre. **Un desk raisonne en teneur de marche qui porte une position
temporaire.** Meme instrument, logique inverse : l'investisseur veut du
rendement, le desk veut de la rotation et du spread.

**Filtre 3 — « Comment je couvre ca ? »** La partie strategies est celle qui te
sert. Le reste est du contexte.

**Ce que tu peux survoler sans remords :** le chapitre fiscalite (francais,
inutile pour toi) et l'histoire des obligations — sauf quelques anecdotes
reutilisables en entretien.

**Ce qu'il faut travailler ligne a ligne :** l'evaluation des obligations
(actualisation, prix pied de coupon, coupon couru) et la sensibilite.

---

## Bloc 1 — Le socle Pichet, traduit en langage de desk (15 min)

### Les trois mesures, et la seule qui compte sur un desk

Pichet te donnera les trois. Voici la hierarchie reelle.

**La duration de Macaulay** est une duree moyenne ponderee des flux, exprimee en
annees. **Elle ne sert presque a rien en salle**, sinon a construire la suivante.

**La duration modifiee** (que Pichet appellera peut-etre « sensibilite ») donne
la variation de prix en pourcentage pour 1 % de variation de taux.

**Le DV01** est la seule des trois qu'on emploie vraiment :

```
DV01 = Nominal x Duration modifiee x 0,0001
```

> 🔑 **Pourquoi le DV01 gagne.** Parce qu'un desk doit additionner des risques
> heterogenes. Tu ne peux pas additionner la duration d'une OAT et celle d'un
> swap : les nominaux different. **Tu peux additionner leurs DV01**, parce
> qu'ils sont tous en euros par point de base. C'est la monnaie commune du
> risque de taux.

### La convexite, et l'erreur qu'elle rattrape

La duration suppose une relation **lineaire** entre prix et taux. Elle est en
realite **courbe**. La convexite est la derivee seconde : elle corrige l'erreur
de l'approximation lineaire.

**En pratique :** pour un petit mouvement, la duration suffit. Pour un choc de
100 points de base ou plus, elle sous-estime le gain et surestime la perte. **La
convexite est un ami de l'acheteur d'obligations.**

> 🇧🇷 **Le contraste.** En Europe, la convexite compte parce que les durations
> sont longues (8-9 ans sur une OAT 10 ans). **Au Bresil elle est presque un
> non-sujet sur la partie courte**, qui represente l'essentiel du marche. En
> revanche elle redevient centrale sur les **NTN-B longues**, indexees
> inflation, ou les durations depassent dix ans. **Si on te parle de convexite
> au Bresil, on parle forcement de NTN-B.**

### 📝 Exercice 1 — a faire sans calculatrice

Tu portes 10 M EUR d'OAT 10 ans (duration modifiee 8,5) et tu veux neutraliser
ton risque de taux avec des contrats DI1 bresiliens a 5 ans (DV01 = 4,33 USD par
contrat). Combien de contrats, et **pourquoi cette question est-elle piegee ?**

<details>
<summary><strong>Correction</strong></summary>

**Le calcul :** DV01 de l'OAT = `10 000 000 x 8,5 x 0,0001 = 8 500 EUR/bp`.
A un taux de change EUR/USD proche de 1,17, cela fait environ 9 950 USD/bp.
Divise par 4,33 : environ **2 300 contrats**.

**Le piege, et c'est le vrai sujet :** ce hedge **ne couvre rien**. Il egalise
deux DV01, mais la courbe francaise et la courbe bresilienne ne bougent pas
ensemble. Tu n'as pas supprime un risque, **tu as cree un spread trade
France-Bresil** plus un risque de change EUR/BRL non couvert.

**La lecon de desk :** egaliser des DV01 ne couvre que si les deux jambes sont
sur la **meme courbe**. Entre deux courbes differentes, on ne couvre pas, **on
prend une position relative**. C'est exactement l'erreur que fait un junior qui
a lu la theorie sans avoir vu un book.

</details>

---

## Bloc 2 — Ce que Pichet n'a pas : la structure bresilienne (15 min)

Socle suppose acquis : tu sais ce qu'est une obligation, un coupon, une courbe.
On passe directement a ce qui differe.

### Les cinq titres, et le seul qui n'a pas d'equivalent

| Marche | Technique | Indexation | Equivalent francais |
|---|---|---|---|
| Tesouro Prefixado | **LTN** | Taux fixe, zero coupon | BTF |
| Prefixado c/ juros | **NTN-F** | Taux fixe + coupons | OAT |
| **Tesouro Selic** | **LFT** | **Taux directeur au jour le jour** | **aucun** |
| Tesouro IPCA+ | **NTN-B Principal** | Inflation + taux reel | OATi zero coupon |
| IPCA+ c/ juros | **NTN-B** | Inflation + taux reel + coupons | OAT€i |

**Deux ecarts structurels avec ce que decrit Pichet.**

**① L'indexe inflation n'est pas une niche.** En France, les OATi et OAT€i sont
un segment marginal ; Pichet leur consacrera quelques pages. **Au Bresil, les
NTN-B structurent tout le marche long.** Raison historique : apres
l'hyperinflation, l'epargne longue ne se place qu'avec protection d'inflation.

**② La LFT n'existe nulle part ailleurs, et c'est le point cle du document.**

> 🔑 **Pourquoi la LFT casse la theorie de Pichet.** Elle se reevalue **chaque
> jour** sur la Selic. Quand les taux montent, **son prix ne baisse pas**. Sa
> duration est proche de **zero**, son porteur ne subit aucune moins-value.
>
> Pichet t'expliquera le canal classique : les taux montent, les portefeuilles
> obligataires perdent de la valeur, les agents s'appauvrissent, la demande
> ralentit. **C'est le canal des effets de richesse.**
>
> **Au Bresil, une hausse de Selic enrichit instantanement les detenteurs de
> LFT.** Le canal ne joue pas dans le meme sens. C'est une des raisons pour
> lesquelles la banque centrale doit taper beaucoup plus fort pour obtenir le
> meme effet — **Selic a 14,00 % quand la Fed est a 3,50-3,75 %**.

**C'est ta meilleure reponse a « pourquoi les taux bresiliens sont-ils si
hauts ? »** parce qu'elle est institutionnelle et non descriptive. Tout le monde
repondra « inflation » et « risque budgetaire ». Toi tu ajoutes la structure de
la dette, et tu changes de categorie.

### La ou se lit vraiment la courbe

**Pas sur les obligations. Sur le contrat DI1.**

- Sous-jacent : le taux interbancaire d'un jour, capitalise jusqu'a l'echeance
- **100 000 points a l'echeance**, 1 point = 1 BRL
- **Cote en taux annuel, base 252 jours ouvres**
- **Mais enregistre et regle en PU** — la valeur actualisee
- Echeances **tous les mois**, reglement financier

```
PU = 100 000 / (1 + taux) ^ (jours ouvres / 252)
```

> ⚠️ **Le piege de sens.** Acheter un DI1, c'est acheter du PU, donc **vendre du
> taux** — position dite *aplicada*. Qui parie sur une **baisse** des taux est
> **acheteur**.
>
> **Le contraste a savoir formuler :** en Europe, le future Euribor est cote
> `100 - taux` : l'inversion existe, mais elle est **explicite**, inscrite dans
> la convention de cotation. Au Bresil, le contrat est cote *en taux* et
> negocie *en PU* : **l'inversion est cachee dans l'actualisation**. C'est
> exactement la que se trompe un junior europeen sur son premier ticket.

### 📝 Exercice 2

DI1 a un an, taux 14 %, 252 jours ouvres. Calcule le PU puis le DV01, en BRL
puis en USD (USD/BRL = 5,16).

<details>
<summary><strong>Correction</strong></summary>

**PU** = `100 000 / 1,14 = 87 719,30 BRL`

**DV01** = `87 719,30 / 1,14 x 0,0001 = 7,69 BRL` par contrat
soit `7,69 / 5,16 =` **1,49 USD par contrat**

**L'ordre de grandeur qui parle :** pour porter **10 000 USD par point de
base**, il faut environ **6 700 contrats**. Le DI1 est un contrat *petit* —
d'ou des volumes enormes et une liquidite qui ne se compare a rien d'autre dans
la region.

**Pour situer la courbe :** DV01 ≈ 1,49 USD a 1 an, **2,62 USD a 2 ans**,
**4,33 USD a 5 ans**. La sensibilite croit avec la maturite, exactement comme
chez Pichet — seule la convention change.

</details>

---

## Bloc 3 — Les produits du desk LatAm (20 min)

C'est la partie que tu ne trouveras dans aucun livre, bresilien ou francais.
**Cinq produits, par ordre de frequence sur un desk.**

### ① Le NDF — le produit numero un

**Non-deliverable forward.** Un terme qui ne se denoue pas par livraison de
devise mais par **difference en dollars**.

**Pourquoi il existe :** la loi bresilienne interdit les comptes en devises
domicilies au Bresil. Un non-resident ne peut donc pas recevoir de reals. **Le
NDF contourne l'interdiction sans jamais faire circuler de real.**

```
Paiement = Nominal x (Forward - Fixing) / Fixing
```

⚠️ **On divise par le fixing, pas par le forward.** C'est l'erreur classique.

**Le fixing est le PTAX**, publie par la banque centrale : **moyenne de quatre
releves quotidiens**.

### 📝 Exercice 3

Tu as vendu 20 M USD de NDF USD/BRL 3 mois a **5,2926**. Le PTAX de fixing
sort a **5,30**. Combien, et dans quel sens ?

<details>
<summary><strong>Correction</strong></summary>

`20 000 000 x (5,2926 - 5,3000) / 5,3000 = -27 925 USD`

**Tu perds environ 27 900 USD.** Tu as vendu du dollar a terme a 5,2926, le
dollar s'est fixe plus haut : ta vente etait trop basse.

**Le reflexe de sales :** avant de repondre, verifie le sens. On a vendu du
USD, le USD monte, donc on perd. **Le calcul ne fait que chiffrer une intuition
qui doit venir en premier.**

</details>

### ② Le cupom cambial — le thermometre

**Definition :** le taux d'interet **en dollars** implicite au Bresil — ce que
rapporte un dollar place localement, une fois neutralise le risque de change.

On l'extrait en combinant la courbe en reals et le forward. Le future qui le
traite est le **DDI**, cote en **taux annuel lineaire base 360 jours** — donc en
convention internationale, pas en 252 jours ouvres. Les operations structurees
**DOD** (DDI + DOL) et **WDD** (DDI + WDO) ont ete lancees le **02/12/2024**.

> 🔑 **Ce qu'il raconte reellement.** Le cupom cambial est le **thermometre de
> la liquidite en dollars au Bresil**. S'il monte brutalement, les dollars
> deviennent chers localement : quelqu'un a un besoin urgent de financement en
> devise. **C'est souvent un signal de stress avant que le spot ne bouge.**
>
> **L'episode historique a connaitre :** en avril 2011, l'extension de l'**IOF**
> (taxe sur les operations financieres) aux emprunts externes des banques et
> entreprises a fait **exploser le cupom cambial** a des niveaux inedits.
> L'arbitrage entre marche offshore et onshore etait devenu impossible. C'est la
> demonstration grandeur nature que **le cupom mesure une contrainte de
> plomberie, pas une anticipation.**
>
> **L'equivalent conceptuel europeen est la base de swap de change**
> (*cross-currency basis*). Un junior generaliste connait peut-etre le terme.
> **Personne ne fera le rapprochement entre les deux.** Toi si.

### 📝 Exercice 4 — le plus important du document

Spot USD/BRL = 5,16, DI 1 an = 14 %. Calcule le forward 1 an si le cupom cambial
vaut 5 %, puis s'il monte a 8 %. Commente.

<details>
<summary><strong>Correction</strong></summary>

`F = S x (1 + DI) / (1 + cupom)`

- Cupom a 5 % : `5,16 x 1,14 / 1,05 =` **5,6023**
- Cupom a 8 % : `5,16 x 1,14 / 1,08 =` **5,4467**

**Ecart : 0,1556 real, soit environ 1 556 pips.**

**Le commentaire, et c'est lui qui compte :** le spot n'a pas bouge d'un
centavo. **Seul le prix du dollar onshore a change, et le forward s'est
deplace de plus de 1 500 pips.** Un corporate qui couvre a un an voit son cours
garanti bouger enormement sans aucun mouvement du comptant.

**C'est la specificite du metier au Bresil.** Sur EUR/USD, le forward suit le
spot. **Sur USD/BRL, le forward a sa propre vie**, dictee par la liquidite
dollar locale. Un sales qui ne surveille que le spot rate l'essentiel de ce que
paie son client.

</details>

### ③ Les quatre structures corporate

Elles valent pour tout le LatAm, pas seulement le Bresil.

**Le terme sec.** Gratuit, simple, mais le client perd tout gain favorable.

**Le tunnel** (*collar*). On achete une protection, on finance en vendant du
potentiel. Souvent construit a prime nulle. *« On echange du potentiel contre de
la gratuite. »*

**Le terme booste.** Meilleur cours que le terme sec, mais **double nominal** si
un seuil est franchi. La formulation de desk : *« le client ameliore son cours
en vendant de la convexite. »*

**L'accumulateur.** Accumule dans une zone, desactive ou double en dehors. **A
fait des degats considerables chez des corporates asiatiques en 2008** — a citer
si on te teste sur la conscience du risque.

> 🔑 **Le mot qui fait la difference : RESTRUCTURATION.**
> *« Une couverture n'est pas un acte unique. Quand le spot a bouge de 8 %, la
> valeur ajoutee du sales c'est de proposer une restructuration, pas de
> constater la perte avec le client. »*

### ④ Les options de change

Pricees en **Garman-Kohlhagen** — l'adaptation de Black-Scholes au change, avec
**deux taux sans risque** au lieu d'un : celui de chaque devise.

**Sur les devises LatAm, la vol est structurellement plus elevee et le smile
plus asymetrique** qu'en G10 : le marche paie cher la protection contre une
depreciation brutale de la devise locale. **Ce n'est pas une anomalie, c'est la
memoire des crises.**

### ⑤ Le pont, et pourquoi tout se tient

**Un forward n'est pas une prevision, c'est un ecart de taux.**

```
F = S x (1 + taux cote x t) / (1 + taux base x t)
```

**Le taux le plus eleve part en deport.** Donc : impossible de coter un forward
USD/BRL sans courbe de taux BRL. **Le FX LatAm est un metier de taux deguise —
c'est toute la raison d'etre de ce document.**

### 📝 Exercice 5

Pourquoi le carry bresilien, une fois **couvert** par un forward, rapporte-t-il
exactement zero ?

<details>
<summary><strong>Correction</strong></summary>

Parce que le forward est **construit** sur l'ecart de taux. Placer en reals a
14 % puis revendre ses reals a terme : le cours a terme integre deja, par
construction, l'ecart entre 14 % et 3,625 %. Les deux se compensent exactement.

**Couvert, le carry est nul par construction.** Ce qu'encaisse un carry trader
n'est donc pas un ecart de taux, **c'est une prime de risque de change non
couverte**. On est paye pour porter le risque.

**Le chiffre qui recadre :** le portage BRL sur 3 mois pour 1 M USD represente
environ **25 900 USD**. Et **trois seances a un ecart-type effacent un trimestre
de portage.**

</details>

---

## Bloc 4 — Le tableau de bascule (5 min)

**Si tu ne retiens qu'une page, c'est celle-ci.**

| | 🇫🇷 Ce que donne Pichet | 🇧🇷 Ce qu'il faut ajouter |
|---|---|---|
| **Comptage** | ACT/ACT, 30/360, lineaire court | **252 jours ouvres, compose** |
| **Taux au jour le jour** | ESTR | **Selic over** (≠ Selic meta, la cible) |
| **Benchmark du marche** | Euribor | **CDI** — tout se cote en « % du CDI » |
| **Ou se lit la courbe** | Swaps, futures Euribor et Bund | **DI1 sur la B3** |
| **Sens du contrat** | `100 - taux`, inversion explicite | **Cote en taux, regle en PU** : cachee |
| **Reference sans risque** | OAT, Bund | Aucune — **la LFT joue ce role** |
| **Duration souveraine** | Longue, 8-9 ans | **Courte** : risque de refinancement |
| **Indexe inflation** | OATi, OAT€i — niche | **NTN-B — pilier du marche long** |
| **Convexite** | Centrale | **Non-sujet sauf NTN-B longues** |
| **Transmission monetaire** | Effets de richesse par le prix | **Cassee par la LFT** → taper plus fort |
| **Pont vers le FX** | Cross-currency basis | **Cupom cambial**, via DDI base 360 |
| **Terme de change** | Suit le spot | **Vie propre** : +1 556 pips sans le spot |

---

## Les cinq phrases a savoir dire

1. *« La courbe bresilienne se compte en 252 jours ouvres et se capitalise en
   compose. Un pricer cale sur ACT/360 est faux des le premier mois. »*
2. *« La courbe ne se lit pas sur les obligations, elle se lit sur les DI
   futurs — cotes en taux, regles en PU. »*
3. *« La LFT a une duration nulle, donc une hausse de Selic n'appauvrit pas ses
   detenteurs. Le canal des effets de richesse est casse : c'est une raison
   structurelle du niveau des taux, au-dela de l'inflation. »*
4. *« Le cupom cambial est le thermometre de la liquidite dollar onshore. En
   2011, l'IOF l'a fait exploser en cassant l'arbitrage offshore. »*
5. *« Sur EUR/USD le forward suit le spot. Sur USD/BRL le forward a sa propre
   vie : le cupom peut le deplacer de 1 500 pips sans que le comptant bouge. »*

---

## Ce qu'il faut retenir

- **Pichet est un bon socle, pas une source Bresil.** Lis-le avec les trois
  filtres : convention, porteur du risque, methode de couverture.
- **Le DV01 est la monnaie commune du risque de taux** — la seule des trois
  mesures qui s'additionne.
- **Egaliser deux DV01 sur deux courbes differentes ne couvre pas : ca cree un
  spread trade.**
- **La LFT est le point de rupture theorique** entre le manuel francais et la
  realite bresilienne.
- **Le cupom cambial est le concept signature** : personne ne le connait, il se
  verifie, et il relie les taux au change.
- **Couvert, le carry est nul par construction** : ce qu'on encaisse est une
  prime de risque.
