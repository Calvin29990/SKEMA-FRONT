# Dossier Calvin Minang - Front Office

> Partie A : cours FIC complet (FR). Partie B : cours bilingue FR/EN.
> Partie C : le projet ShockDesk, son pitch et ses points faibles.
> Le protocole de simulation est en Partie C, section 5.

---

# PARTIE A - COURS FIC

## Cours d'urgence FIC — 2 h

**Objectif : pouvoir dire « je connais » sur toutes les notions du périmètre.**
Pas de démonstration longue. Des images mentales, des exemples concrets, des
chiffres que tu peux ressortir.

> 🎯 **Comment lire.** Chaque notion suit le même schéma : **l'image mentale**
> d'abord, puis **le chiffre**, puis **la phrase à dire**. Si tu retiens l'image,
> le reste revient. Si tu ne retiens que la formule, tu bloqueras.

**Les 6 blocs :** taux · obligations · dérivés fermes · options · vol · crédit &
FX.

---

## BLOC 1 — Les taux (15 min)

## 1.1 L'actualisation

**L'image :** 100 € dans un an ne valent pas 100 € aujourd'hui. Parce qu'avec
96 € aujourd'hui placés à 4 %, tu as 100 € dans un an. **Donc 100 € dans un an
= 96 € aujourd'hui.**

C'est tout. Toute la finance de taux, c'est ça, répété.

| Recevoir 100 € | À 4 %, ça vaut aujourd'hui |
|---|---|
| dans 1 an | **96,15 €** |
| dans 10 ans | **67,56 €** |

> **À retenir :** plus c'est loin, moins ça vaut. Et **plus le taux monte, moins
> ça vaut**. Cette phrase explique 80 % du marché obligataire.

## 1.2 La courbe des taux

**L'image :** c'est le prix du temps. Sur l'axe horizontal, la durée du prêt
(1 an, 2 ans… 30 ans). Sur l'axe vertical, le taux exigé.

| Forme | Nom | Ce que ça raconte |
|---|---|---|
| Monte | **normale** | Prêter longtemps est plus risqué, on exige plus |
| Plate | **flat** | Incertitude, transition |
| Descend | **inversée** | Le marché anticipe des baisses de taux — souvent une récession |

**Les mouvements — le vocabulaire de desk :**

| Mouvement | Nom |
|---|---|
| L'écart court-long **augmente** | **steepening** (la courbe se pentifie) |
| L'écart **diminue** | **flattening** (elle s'aplatit) |
| Toute la courbe monte/descend | **parallel shift** |

> **Bull ou bear ?** *Bull* = les prix montent = **les taux baissent**.
> **Bull steepener** = le court baisse plus que le long. **Bear flattener** = le
> court monte plus que le long (typique d'une banque centrale qui resserre).

## 1.3 Taux directeurs et marché

**Aujourd'hui (10/09/2026) :** la BCE a monté de **25 bp**, dépôt à **2,50 %**.
Le marché price **~40 %** de proba d'une hausse de plus en décembre.

**Un point de base (bp) = 0,01 %.** On dit **« un bip »**. Sur 10 M€, 1 bp =
1 000 € par an. Ce n'est jamais négligeable.

---

## BLOC 2 — Les obligations (25 min)

## 2.1 Le mécanisme

**L'image :** tu prêtes 100 € à un État pour 5 ans. Il te verse **3 € par an**
(le coupon), et te rend **100 € à la fin** (le nominal).

## 2.2 LA relation à comprendre : prix ↔ taux

**L'image terre à terre.** Tu as acheté une obligation qui paie **3 %**. Le
lendemain, l'État émet la même à **4 %**.

Ton titre à 3 % n'intéresse plus personne au prix de 100. Pour le vendre, tu
dois **baisser ton prix** jusqu'à ce que l'acheteur obtienne l'équivalent de
4 %.

> 🔑 **Le prix d'une obligation et son rendement bougent en sens inverse.
> Toujours.** C'est la question numéro 1 en entretien FIC. Si tu ne retiens
> qu'une chose de ce cours, c'est celle-là.

**Le chiffre :** obligation 5 ans, coupon 3 %

| Rendement du marché | Prix |
|---|---|
| 3 % | **100,00** (au pair) |
| 4 % | **95,55** |
| 5 % | **91,34** |

## 2.3 La duration

**L'image :** c'est le **bras de levier** de l'obligation face aux taux.
Duration 5 → si les taux montent de 1 %, tu perds environ 5 %.

Techniquement c'est la maturité moyenne pondérée des flux — mais **en entretien,
dis « la sensibilité aux taux »**. C'est ce qu'on attend.

$$\Delta P / P \approx -MD \times \Delta y$$

**Le chiffre :** l'obligation ci-dessus a une **duration modifiée de 4,53**.
Pour +100 bp, l'approximation prédit **−4,53 %**. Le vrai calcul donne
**−4,40 %**.

## 2.4 La convexité

**L'écart entre −4,53 % et −4,40 %, c'est elle.**

**L'image :** la relation prix/taux n'est pas une droite, c'est une **courbe**.
Résultat, c'est **asymétrique en ta faveur** quand tu détiens l'obligation :

| Mouvement | Effet réel |
|---|---|
| Taux **+100 bp** | **−4,40 %** |
| Taux **−100 bp** | **+4,66 %** |

> **Tu gagnes plus quand ça baisse que tu ne perds quand ça monte.** C'est la
> convexité, et **c'est pour ça qu'elle se paie**. Retiens l'asymétrie, pas la
> formule.

## 2.5 Le repo

**L'image :** tu as besoin de cash pour la nuit. Tu **vends** ton obligation en
t'engageant à la racheter demain un peu plus cher. C'est un **prêt garanti par
un titre** — c'est comme ça que se finance un desk.

Si tout le monde veut le même titre, il devient **special** : tu te finances
moins cher parce que ton collatéral est recherché.
*"That bond is trading special."*

---

## BLOC 3 — Forwards, futures, swaps (20 min)

## 3.1 Le forward

**L'image :** tu fixes aujourd'hui le prix d'une transaction future. Pas de cash
maintenant, tout à l'échéance.

> ⚠️ **L'erreur que font tous les étudiants :** le prix forward n'est **PAS une
> prévision**. C'est le spot **plus le coût de portage** : ce que ça coûte de
> détenir l'actif jusqu'à l'échéance (le financement, moins ce que l'actif
> rapporte).

$$F = S_0 e^{(r-q)T}$$

**L'exemple terre à terre :** or à 2 000 €, taux 4 %. Le forward 1 an vaut
~2 082 €. Pas parce que l'or va monter — **parce que tu empruntes 2 000 € pendant
un an pour le détenir**.

| Cas | q représente |
|---|---|
| Action / indice | le dividende |
| **FX** | le **taux étranger** |
| Commodité | le rendement de convenance − le stockage |

**Les chiffres :** indice S=3500, r=3,5 %, q=1,8 %, T=0,75 → **F = 3544,91**
EURUSD 1,0850, r_d=4,25 %, r_f=2,25 %, T=0,25 → **F = 1,090439** (+54,4 pips)

> **Contango** = forward au-dessus du spot (r > q). **Backwardation** = en
> dessous.

## 3.2 Futures vs forwards

| | Forward | Future |
|---|---|---|
| Où | gré à gré (OTC) | en bourse |
| Sur-mesure | oui | non, standardisé |
| Risque de contrepartie | oui | non (chambre de compensation) |
| Flux | tout à la fin | **appels de marge quotidiens** |

## 3.3 Le swap de taux

**L'image :** deux parties échangent des flux d'intérêts sur un montant
notionnel. L'un paie **fixe**, l'autre paie **variable**.

**L'exemple concret :** une entreprise a emprunté à taux variable et craint une
hausse. Elle **paie fixe / reçoit variable** : elle a transformé sa dette
variable en dette fixe. Elle a acheté de la **tranquillité**.

> **Le notionnel ne s'échange jamais.** Seuls les intérêts circulent. C'est
> pour ça qu'on parle de milliards de notionnel sans mouvement de capitaux.

**Payer fixe = être short duration** : tu gagnes si les taux montent.

---

## BLOC 4 — Les options (35 min)

## 4.1 Le mécanisme

**L'image :** l'option est une **assurance**. Tu paies une **prime** pour avoir
le **droit** — pas l'obligation — d'acheter (call) ou de vendre (put) à un prix
fixé (**strike**).

| | Tu es acheteur | Tu es vendeur |
|---|---|---|
| **Perte max** | la prime | **illimitée** |
| **Gain max** | illimité | la prime |

> **L'asymétrie est tout.** L'acheteur d'option paie pour dormir. Le vendeur
> encaisse pour prendre le risque. Un desk fait surtout… **vendeur**.

**Vocabulaire :** *in the money* (exercer est rentable) · *at the money*
(strike = spot) · *out of the money*.

## 4.2 La parité call-put

**L'image :** acheter un call et vendre un put au même strike, c'est
**exactement** détenir l'actif à crédit. Donc les prix sont liés — pas par une
théorie, par un **arbitrage** : sinon on encaisse la différence sans risque.

$$C - P = S_0 e^{-qT} - K e^{-rT}$$

**Le chiffre :** S=100, K=100, r=4 %, q=2 %, T=0,5, C=6,20 → **P = 5,2149**

## 4.3 Black-Scholes

**L'idée en une phrase :** on peut **fabriquer** une option en détenant une
quantité d'actif qu'on ajuste en continu. Si la copie est parfaite, l'option n'a
qu'**un seul prix possible** — celui de la copie.

$$C = S_0 e^{-qT} N(d_1) - K e^{-rT} N(d_2)$$

**Comment la lire, sans la démontrer :**

| Terme | Ce que c'est |
|---|---|
| $N(d_2)$ | la probabilité de finir **dans la monnaie** |
| $N(d_1)$ | le **delta** — combien d'actif détenir pour couvrir |
| $Ke^{-rT}$ | le strike, actualisé |

**Le chiffre :** S=100, K=105, r=3 %, σ=25 %, T=0,5 → **C = 5,5760**,
**P = 9,0127**

**L'approximation de tête** (call ATM, r=0) :
$$C \approx 0{,}4 \times \sigma\sqrt{T} \times S$$
σ=20 %, T=1, S=100 → **8,00** vs vrai prix **7,9656**. Impressionnant en
entretien.

### Les 6 hypothèses — à réciter

1. Mouvement brownien géométrique (rendements log-normaux)
2. **Volatilité constante**
3. Taux constant
4. Pas de coûts de transaction ni de taxes
5. Divisibilité parfaite, vente à découvert possible
6. Pas d'arbitrage, option **européenne**

> **La question qui tombe : « laquelle casse en premier ? »**
> **La vol constante.** Et la preuve est publique : le **smile de volatilité**.
> Le marché lui-même contredit l'hypothèse du modèle qu'il utilise.

## 4.4 Les grecs

**L'image globale :** ce sont les **cadrans du tableau de bord**. Chacun répond
à « si CE paramètre bouge, je perds combien ? ».

| Grec | Répond à | L'image |
|---|---|---|
| **Delta** Δ | le spot bouge | ta **vitesse** |
| **Gamma** Γ | le delta bouge | ton **accélération** |
| **Vega** | la vol bouge | ta sensibilité à la **peur** |
| **Theta** Θ | un jour passe | le **loyer** que tu paies |
| **Rho** ρ | les taux bougent | le plus petit, souvent ignoré |

**Les chiffres (sur l'exemple ci-dessus) :** Δ=0,459 · Γ=0,0224 · vega=0,281 ·
Θ/jour=−0,0225 · ρ=0,202

### Gamma et theta : le couple central

**L'image :** le gamma est une **voiture de sport**, le theta est le **plein
d'essence**.

- **Long gamma** : tu profites des mouvements, mais tu paies du theta chaque
  jour. Tu veux que **ça bouge**.
- **Short gamma** : tu encaisses du theta, mais un mouvement violent te coûte.
  Tu veux que **rien ne se passe**.

$$\Theta + \tfrac{1}{2}\sigma^2 S^2 \Gamma = 0 \quad (r = q = 0)$$

> **Traduction : la convexité se paie en temps.** Toute la vie d'un desk
> d'options est dans cet arbitrage.

### 🚨 La question piège : *short gamma*

**Ce qui se passe concrètement.** Tu es vendeur d'options, tu te couvres en
delta. Le marché monte → ton delta devient négatif → tu dois **acheter** pour
te recouvrir. Le marché baisse → tu dois **vendre**.

**Tu achètes haut, tu vends bas. À chaque ajustement.**

> **En anglais :** *"When you're short gamma, you're hedging into the move — you
> buy the highs and sell the lows. You collect theta, but a fast market costs
> you more than you collect."*
>
> **Et tu l'as vu** sur mars 2020 dans ton pricer Excel. Dis-le : c'est du vécu,
> ça vaut dix réponses théoriques.

---

## BLOC 5 — La volatilité (15 min)

## 5.1 Réalisée vs implicite

| | Ce que c'est |
|---|---|
| **Réalisée** (historique) | ce que le marché **a fait** — un calcul sur le passé |
| **Implicite** | ce que le marché **anticipe** — extraite du prix des options |

> **L'implicite est un prix, pas une prévision.** C'est le niveau de vol qui
> rend la formule cohérente avec le prix coté. Quand un trader dit *« la vol est
> chère »* (*rich*), il dit que l'implicite est au-dessus de ce qu'il pense que
> la réalisée sera.

## 5.2 Le smile

**Le fait :** Black-Scholes suppose une vol unique. Le marché, lui, cote **une
vol différente pour chaque strike**. Tracé, ça fait un **sourire**.

**Pourquoi ?** Parce que les vrais rendements ont des **queues épaisses** : les
krachs sont plus fréquents que ce que suppose la loi normale. Les puts loin de
la monnaie sont donc **plus chers** que le modèle ne le dit — ce sont des
assurances contre le krach.

> **La phrase qui montre que tu comprends :** *"The smile is the market pricing
> in what the model leaves out."*

## 5.3 Les structures à connaître de nom

| Structure | Composition | Pour quoi |
|---|---|---|
| **Straddle** | call + put, **même strike** | tu paries que **ça bouge**, peu importe le sens |
| **Strangle** | call + put, strikes **écartés** | pareil, moins cher, il faut un mouvement plus fort |
| **Call spread** | acheter un call, vendre un plus haut | vue haussière, **moins chère**, gain plafonné |
| **Butterfly** | pari sur la **stabilité** | tu gagnes si ça ne bouge pas |
| **Risk reversal** | acheter un call, vendre un put | vue directionnelle **à coût réduit** |

**Le chiffre :** straddle **24,40** vs strangle **10,69** — le straddle coûte
**2,3×** plus cher. C'est le prix de la zone couverte.

---

## BLOC 6 — Crédit et FX (15 min)

## 6.1 Le spread de crédit

**L'image :** c'est le **supplément** exigé pour prêter à une entreprise plutôt
qu'à un État. C'est le prix du risque de défaut.

**Le chiffre :** un spread de **150 bp** sur 10 M€, c'est **150 000 € par an**.

| Mouvement | Nom | Sens |
|---|---|---|
| Le spread **diminue** | **tightening** | le marché est plus confiant |
| Le spread **augmente** | **widening** | stress, fuite vers la qualité |

**Investment grade** (≥ BBB−) vs **high yield** (en dessous). Le **CDS** est
l'assurance contre le défaut : tu paies une prime annuelle, tu es indemnisé si
l'émetteur fait défaut.

## 6.2 L'OAT-Bund

**L'image :** l'écart entre le taux français et le taux allemand. **La prime de
risque France**, mesurée en direct.

**Le chiffre du jour : ~85 bp** (OAT 10 ans 4,19 %, Bund 3,34 %). La fourchette
sur un an est 59-85 bp → **on est au sommet**. C'est un fait que tu peux citer
mardi.

## 6.3 Le FX

**Une paire est un rapport.** EUR/USD = 1,0850 → 1 € vaut 1,0850 USD.

**Le point clé :** le forward FX ne dit **rien** sur la direction future. Il ne
reflète que **l'écart de taux** entre les deux devises.

> **La parité des taux d'intérêt :** si tu places en dollar à un taux plus élevé
> qu'en euro, le forward EUR/USD sera **plus haut** — exactement de quoi annuler
> ton gain. **Sinon, arbitrage.**

**Un pip** = la 4ᵉ décimale. De 1,0850 à 1,0851 = **1 pip**.

---

## 🎯 Ce que tu dois pouvoir dire mardi

Coche mentalement. Si tu réponds à voix haute sans bloquer, c'est acquis.

| # | Question | La réponse en une ligne |
|---|---|---|
| 1 | Prix et taux d'une obligation ? | **Sens inverse, toujours** |
| 2 | La duration ? | La sensibilité aux taux. Duration 5 → +1 % de taux = −5 % |
| 3 | La convexité ? | La relation est courbe : on gagne plus qu'on ne perd |
| 4 | Le forward est-il une prévision ? | **Non** — spot + coût de portage |
| 5 | Un swap de taux ? | Échange fixe contre variable, **le notionnel ne bouge pas** |
| 6 | La parité call-put ? | Call − put = position forward. Arbitrage |
| 7 | L'idée de Black-Scholes ? | La **réplication** : si on copie l'option, il n'y a qu'un prix |
| 8 | Quelle hypothèse casse ? | **La vol constante** → le smile |
| 9 | Le gamma ? | La vitesse à laquelle mon delta se périme |
| 10 | Short gamma, marché rapide ? | J'achète haut, je vends bas à chaque couverture |
| 11 | Vol implicite ? | Un **prix**, pas une prévision |
| 12 | Un spread de crédit ? | Le prix du risque de défaut. 150 bp sur 10 M = 150 k/an |

---

## Si un recruteur creuse trop

> *"I know the concept and I can use it — I haven't derived it from scratch.
> That's on my list."*

**C'est une bonne réponse.** Elle est honnête, elle montre que tu sais où sont
tes limites, et **personne n'attend d'un M2 qu'il redémontre Black-Scholes**.
Ce qu'on attend, c'est que tu **saches de quoi tu parles** — et après ce cours,
c'est le cas.

> **Ce soir :** lis en entier, sans t'arrêter sur ce qui résiste. Demain, tu
> relis **uniquement les 12 questions** du tableau, à voix haute. Le reste se
> déposera tout seul.


---

# PARTIE B - BILINGUE

## Cours d'urgence bilingue — 2 h

**FR / EN en vis-à-vis. Lis la colonne anglaise à voix haute.**

Objectif : tenir une conversation de desk en anglais mardi. Pas devenir
bilingue — **avoir de quoi dire**.

📄 **PDF pour Gemini :** `anglais/COURS-URGENCE-bilingue.pdf` — protocole de
simulation en Partie 5.

---

## Partie 1 — Le socle (20 min)

## 1.1 Les 15 mots

| FR | EN | Prononciation |
|---|---|---|
| obligation | **a bond** | /bɒnd/ — pas « bonde » |
| rendement | **the yield** | /jiːld/ — pas « yeld » |
| coupon | **the coupon** | /ˈkuːpɒn/ |
| courbe des taux | **the yield curve** | |
| point de base | **a basis point** | dit **« a bip »** |
| échéance | **maturity** | |
| écart | **the spread** | |
| volatilité | **vol** | jamais *volatility* sur un desk |
| acheteur | **long** | *I'm long duration* |
| vendeur | **short** | *I'm short gamma* |
| couvrir | **to hedge** | /hedʒ/ |
| résultat | **the P&L** | dit **« the P and L »** |
| sous-jacent | **the underlying** | |
| échéance/expiration | **expiry** | |
| prix d'exercice | **the strike** | |

## 1.2 Décrire un marché

| FR | EN |
|---|---|
| la courbe se pentifie / s'aplatit | **the curve steepens / flattens** |
| les taux montent / baissent | **yields are up / down** |
| les spreads se resserrent / s'écartent | **spreads are tightening / widening** |
| c'est cher | **it's rich** *(jamais expensive)* |
| c'est bon marché | **it's cheap** |
| le marché anticipe déjà | **the market is pricing in…** |
| hausse de 25 bp | **a twenty-five basis point hike** |
| baisse | **a cut** |
| statu quo | **the central bank held** |
| prise de bénéfices | **profit-taking** |
| dénouer | **to unwind** |

## 1.3 Le desk

| FR | EN |
|---|---|
| tenir un marché | **to make a market** |
| coter à double sens | **to quote a two-way price** |
| écart achat-vente | **the bid-offer spread** |
| flux clients | **client flow** |
| le portefeuille | **the book** |
| adjudication | **an auction** |
| pension livrée | **repo** |
| titre recherché | **the bond is trading special** |
| couvrir en delta | **to delta-hedge** |
| vol implicite | **implied vol** |

> 🗣️ **Dis ça maintenant, à voix haute :**
> *"The ECB hiked twenty-five bips this week. The curve flattened, and the
> market is pricing another hike in December."*

---

## Partie 2 — Les trois idées du cours (40 min)

## 2.1 Parité call-put · *Put-call parity*

**FR —** Acheter un call et vendre un put revient exactement à détenir l'actif à
crédit. Ce n'est pas une théorie : c'est un **arbitrage**. À l'échéance, ce
portefeuille vaut toujours S_T − K, quoi qu'il arrive. Deux choses qui valent la
même chose demain valent la même chose aujourd'hui.

**EN —** *"A long call plus a short put replicates a forward position on the
underlying. At expiry the payoff is always S minus K, whatever happens. So the
two must have the same price today — otherwise you'd lock in a riskless
profit."*

$$C - P = S_0 e^{-qT} - K e^{-rT}$$

**Repère :** S=100, K=100, r=4 %, q=2 %, T=0,5, C=6,20 → **P = 5,2149**

## 2.2 Le forward · *The forward*

**FR —** Le prix forward n'est **pas** une prévision. C'est le spot corrigé du
coût de portage : ce que coûte de détenir l'actif jusqu'à l'échéance
(financement moins dividendes).

**EN —** *"The forward is not a forecast. It's the spot adjusted for cost of
carry — funding minus dividends, or the foreign rate in FX. It's a
no-arbitrage price."*

$$F = S_0 e^{(r-q)T}$$

En FX : $F = S_0 e^{(r_d - r_f)T}$

**Réflexe :** si r > q → forward **au-dessus** du spot (*contango*).
Si q > r → **en-dessous** (*backwardation*).

**Repères :** indice S=3500, r=3,5 %, q=1,8 %, T=0,75 → **F = 3544,91** ·
EURUSD 1,0850, r_d=4,25 %, r_f=2,25 %, T=0,25 → **F = 1,090439** (+54,4 pips)

## 2.3 Black-Scholes

**FR —** L'idée fondatrice est la **réplication** : on peut copier une option en
détenant une quantité d'actif qu'on ajuste en continu. Si la copie est parfaite,
l'option n'a qu'un seul prix possible.

**EN —** *"The core idea is replication. You can copy the option by holding a
quantity of the underlying and adjusting it continuously. If the replication is
perfect, there's only one possible price — otherwise there's an arbitrage."*

$$C = S_0 e^{-qT} N(d_1) - K e^{-rT} N(d_2)$$

$$d_1 = \frac{\ln(S_0/K) + (r - q + \sigma^2/2)T}{\sigma\sqrt{T}}
\qquad d_2 = d_1 - \sigma\sqrt{T}$$

| Terme | FR | EN |
|---|---|---|
| $N(d_2)$ | proba de finir dans la monnaie | *the probability of ending in the money* |
| $N(d_1)$ | le delta | *the delta — how much underlying to hold* |
| $Ke^{-rT}$ | ce que tu paieras, actualisé | *the discounted strike* |

**Repère :** S=100, K=105, r=3 %, q=0, σ=25 %, T=0,5 → d1=−0,102758,
d2=−0,279534, **C = 5,5760**, **P = 9,0127**

**Approximation de tête** (call ATM, r=0) : $C \approx 0{,}4 \times \sigma\sqrt{T} \times S$
→ σ=20 %, T=1, S=100 : approx **8,00** vs vrai **7,9656**

### Les 6 hypothèses · *The six assumptions*

| FR | EN |
|---|---|
| 1. Mouvement brownien géométrique | *geometric Brownian motion, lognormal returns* |
| 2. Volatilité constante | *constant volatility* |
| 3. Taux constant | *constant risk-free rate* |
| 4. Pas de coûts ni de taxes | *no transaction costs, no taxes* |
| 5. Divisibilité, vente à découvert | *perfect divisibility, short selling allowed* |
| 6. Pas d'arbitrage, option européenne | *no arbitrage, European exercise* |

> **La question qui tombe : « laquelle casse en premier ? »**
> **EN —** *"Constant volatility. That's exactly why the volatility smile
> exists — implied vol isn't flat across strikes, so the model's own assumption
> is contradicted by the market that uses it."*

## 2.4 Les grecs · *The Greeks*

| Grec | FR | EN — à dire tel quel |
|---|---|---|
| **Delta** | sensibilité au spot | *"how much the option moves when the underlying moves"* |
| **Gamma** | vitesse du delta | *"how fast my hedge goes stale"* |
| **Vega** | sensibilité à la vol | *"my exposure to implied vol"* |
| **Theta** | perte par jour | *"what I pay to hold the option overnight"* |
| **Rho** | sensibilité au taux | *"rate sensitivity — usually the smallest"* |

**Repères (Ex5) :** Δ=0,459078 · Γ=0,022449 · vega=0,280609 · Θ/jour=−0,022535 ·
ρ=0,201659

### La question piège : *short gamma*

**FR —** Vendeur d'options, ton delta évolue contre toi. Tu es forcé d'acheter
quand ça monte et de vendre quand ça baisse : tu achètes haut, tu vends bas.

**EN —** *"When you're short gamma, you're hedging into the move — you buy the
highs and sell the lows. You collect theta every day, but a fast market costs
you more than you collect. I saw exactly that dynamic when I back-tested the
March 2020 crash on my own pricer."*

> **Cette dernière phrase est ton meilleur atout.** Tu l'as vécu, pas lu.

### La relation clé

$$\Theta + \tfrac{1}{2}\sigma^2 S^2 \Gamma = 0 \quad \text{(straddle, } r = q = 0)$$

**FR —** Le gamma se paie en theta. **EN —** *"You pay for convexity with time
decay. That trade-off is the whole life of an options desk."*

---

## Partie 3 — Parler de DB et du marché (20 min)

## 3.1 Les chiffres à connaître

| Fait | Chiffre |
|---|---|
| FIC 2025 | **9,6 Md€, +13 %** |
| Dernier trimestre | **record : 2,6 Md€, +16 %** |
| Moteurs | **Rates et Credit, +27 %** |
| Positionnement | **#1 European FIC house** |
| Ambition | *the only truly global alternative to US banks* |
| Cible 2028 | **RoTE > 14 %, C/I < 55 %** |

## 3.2 Le marché cette semaine

| Fait | Valeur |
|---|---|
| BCE (10/09) | **hausse de 25 bp, dépôt à 2,50 %** |
| Marché sur décembre | **~40 % de proba** d'une hausse de plus |
| OAT-Bund | **~85 bp** — haut de la fourchette d'un an |
| Inflation 2026 | **3,0 %** |

**EN —** *"The ECB hiked twenty-five bips on Wednesday, taking the deposit rate
to two point five. The market is pricing roughly a forty percent chance of
another hike in December. And the OAT-Bund spread is around eighty-five bips —
close to the top of its one-year range, so there's a real French risk premium
being priced."*

---

## Partie 4 — Les 3 réponses par cœur (20 min)

## ① *Tell me about yourself* (~75 s)

> "I'm Calvin, a final-year Master's student at SKEMA in Paris, focusing on
> market finance. What got me into trading was one concrete thing: I built a lab
> where I model a geopolitical shock on oil and measure the P&L of a hedged book
> on real data. What it taught me is that **timing matters more than
> direction** — in my own numbers, exiting at the peak versus holding to the
> stop was worth about **six hundred thousand dollars on a twenty-five million
> book**. That's what pulled me towards a desk rather than research. I also did
> multi-asset reporting at BPCE Assurances, so I've worked with Bloomberg curves
> daily. Right now I'm going through rates and derivatives fundamentals."

## ② *Why Deutsche Bank?* (~60 s)

> "Two reasons. First, positioning — DB is the **number one European FIC house**,
> and the strategy is explicitly to be the global alternative to US banks. Most
> European players are consolidating regionally; that's a different bet. Second,
> momentum: FIC was **9.6 billion euros in 2025, up 13 percent**, and last
> quarter was a record — **2.6 billion, up 16 percent**, driven by rates and
> credit. What interests me is that management says the franchise is now
> diversified enough not to depend on volatility. That's the harder thing to
> build."

## ③ *Why rates?* (~45 s)

> "Rates is the market where a view has to be **expressed precisely**. In
> equities you can be roughly right about direction. In rates you have to pick
> the point on the curve, the instrument, the carry. I like that the thinking is
> constrained — there's macro, but it has to survive contact with a curve and a
> repo rate. And right now it's the most alive market in Europe: the ECB hiked
> this week, and the OAT-Bund spread is near the top of its one-year range."

## Les 8 phrases de secours

| Situation | À dire |
|---|---|
| Répéter | *"Sorry, could you repeat that?"* |
| Gagner 3 s | *"That's a good question — let me think."* |
| Tu ne sais pas | *"I don't know that one yet. Can you walk me through it?"* |
| Te corriger | *"Actually, let me correct myself."* |
| Vérifier | *"Does that answer your question?"* |
| Reformuler | *"So if I understand correctly, you're asking…"* |
| Nuancer | *"It depends on…"* |
| Conclure | *"That's how I'd approach it."* |

> **« I don't know » dit calmement est un atout.** Un junior qui invente est
> dangereux sur un desk. Un junior qui dit « pas encore, montrez-moi » est
> formable.

---

## Partie 5 — 🤖 PROTOCOLE POUR GEMINI

**Copie-colle le bloc ci-dessous à Gemini, avec le PDF en pièce jointe.**

---

> You are a Deutsche Bank rates trader conducting a 30-minute mock interview
> with me in English. I am a French Master's student, and English Front Office
> conversation is my weak point — I have never practised it.
>
> **Rules:**
> 1. Speak **only English**. Ask **one question at a time** and wait for my
> answer.
> 2. Keep your questions **short and spoken**, like a real desk conversation —
> not written prose.
> 3. After each of my answers, give me **three lines of feedback**: one thing
> that worked, one thing to fix, and **the better way to say it in desk
> English**.
> 4. If I use French-sounding English (*"expensive vol"* instead of *"rich
> vol"*, *"volatility"* instead of *"vol"*), **correct it immediately**.
> 5. If I freeze or stay silent, don't rescue me — prompt me with *"take your
> time"* and wait.
> 6. Be **direct but not harsh**. Trading floors are blunt, not cruel.
>
> **Run this sequence:**
> 1. Tell me about yourself.
> 2. Why Deutsche Bank, not a US bank?
> 3. Why rates?
> 4. What did the ECB do this week, and what's priced for December?
> 5. Walk me through Black-Scholes out loud. Which assumption breaks first?
> 6. You're short gamma and the market gaps. What happens to you?
> 7. I flip a fair coin until heads. Expected number of flips? Think out loud.
> 8. Final one: you're on a call with a hundred people and the host asks for
> questions. Unmute and ask yours.
>
> **At the end**, give me: a score out of 10 on fluency, a score out of 10 on
> technical content, and **the five expressions I should drill before Tuesday**.
>
> The attached PDF contains the material I've studied — use it to judge whether
> my answers match what I'm supposed to know. Start with question 1 now.

---

## Après la simulation

- [ ] Noter les **5 expressions** que Gemini te donne
- [ ] Refaire les questions **1, 2 et 8** une deuxième fois
- [ ] Lundi : uniquement la **question 8**, dix fois

---

## Le test de 5 minutes — sans notes

Réponds **à voix haute, en anglais**.

1. What is put-call parity? Why is it true?
2. Is the forward a forecast? Why not?
3. Name three Black-Scholes assumptions. Which breaks first?
4. What does gamma measure?
5. You're short gamma and the market gaps. What happens?

<details><summary>Réponses</summary>

1. *A long call plus a short put replicates a forward on the underlying, so
   their prices are linked by arbitrage.*
2. *No — it's the spot adjusted for cost of carry. A no-arbitrage price, not a
   prediction.*
3. *Constant vol, constant rates, lognormal returns, no transaction costs,
   European exercise. **Constant vol breaks first** — hence the smile.*
4. *How fast delta changes when the underlying moves — how quickly my hedge
   goes stale.*
5. *My delta moves against me. I buy the highs and sell the lows to re-hedge. I
   collect theta, but a fast market costs me more than I collect.*

</details>

> Si tu passes les 5 sans bloquer, **tes bases sont là**. Tu es au-dessus de la
> moyenne des étudiants qui seront sur le call mardi.


---

# PARTIE C - SHOCKDESK

## ShockDesk — pitch, défense et simulation

**https://shockdesk.onrender.com/** — ton arme, à condition de la manier
correctement.

> ⚠️ **Lis la Partie 3 avant tout le reste.** Il y a trois chiffres sur ton
> propre site qui peuvent se retourner contre toi en entretien. Mieux vaut les
> découvrir ici que devant un trader mardi.

---

## Partie 1 — Ce que ShockDesk prouve vraiment

Ce n'est **pas** « j'ai gagné de l'argent ». C'est bien mieux que ça.

| Ce que le recruteur voit | Pourquoi c'est rare chez un étudiant |
|---|---|
| **Une discipline point-in-time** | `get_forecast()` ne renvoie que la révision publiée **avant** la date du bar. Tu as codé l'**anti-look-ahead bias**. |
| **Un stop fixé ex-ante** | Le stop est porté par la prévision, pas décidé en regardant la courbe. |
| **Les misses affichés** | HYG et TLT sont marqués comme échecs, en public, dans le scorecard. |
| **Le sens mesuré net du drift** | Tu déduis le benchmark pondéré par le beta. Tu ne t'attribues pas le marché. |
| **Des révisions datées, jamais réécrites** | L'historique reste auditable. |

> 🔑 **Ton vrai pitch n'est pas la performance, c'est l'honnêteté
> méthodologique.** N'importe qui peut montrer une courbe qui monte. Presque
> personne, à ton niveau, ne construit un système qui **rend impossible de se
> mentir à soi-même**. C'est exactement ce qu'un desk cherche chez un junior :
> quelqu'un qui ne maquillera pas un P&L.

## Les chiffres exacts (backtest 01/07 → 28/08/2026, 25,5 M USD)

| Métrique | Valeur |
|---|---|
| P&L | **+337 883 USD (+1,32 %)** |
| Sharpe | **1,67** · Sortino 15,91 |
| Drawdown max | **−0,08 %** · Calmar 102,36 |
| Vol annualisée | 2,40 % |
| Trades | 21 · 61,1 M USD échangés |
| Attribution | **BZ=F +187,1 k** · ^GSPC +82,0 k · GC=F +53,0 k · DBC +46,7 k · DX +5,3 k · **HYG −11,7 k** · **TLT −24,6 k** |
| Scorecard | **4/6** en accord de signe · erreur de pic médiane **7 j** · ratio d'amplitude médian **1,07** |
| Le call qui a payé | Brent : prévu **+5 %**, réalisé **+18,4 %** → **×3,68**, pic J+8 vs J+7 prévu |

---

## Partie 2 — Le pitch en anglais (60 secondes)

À dire **tel quel**. C'est ta réponse à *"tell me about a project"*.

> "I built a research desk called ShockDesk. The idea is simple: I publish a
> dated forecast on a macro scenario — say an oil shock — then I trade a
> multi-asset book against it and score myself afterwards.
>
> The part I care about is the **discipline**. The forecast function is
> point-in-time, so the backtest can only see revisions published **before** the
> bar — no look-ahead. The stop is set **ex-ante**, carried by the forecast, not
> decided by looking at the curve. And the scorecard shows the **misses**
> alongside the hits: on the oil book, HYG and TLT both went the wrong way, and
> that's on the public page.
>
> On the July exercise the book made **1.3 percent in six weeks**, Sharpe around
> **1.7**, max drawdown **eight basis points**. The Brent call was right — I
> forecast five percent, it did eighteen — but honestly the more useful lesson
> was the **timing**: exiting at the model peak versus holding to the calendar
> stop was worth about **six hundred thousand dollars** on a twenty-five million
> book. Same view, same direction — the difference was entirely **when you
> get out**."

**Pourquoi ce pitch marche :**

1. Tu **annonces tes échecs toi-même** — le trader n'a plus rien à débusquer
2. Tu cites **un chiffre avec sa provenance**
3. Tu termines sur **une leçon**, pas sur une performance
4. « Same view, same direction — the difference was when you get out » est une
   phrase de **trader**, pas d'étudiant

---

## Partie 3 — 🚨 Les 3 angles d'attaque

**Un trader trouvera ça en trente secondes.** Si tu ne les as pas préparés, ton
arme se retourne contre toi.

## Attaque 1 — « Your alpha is negative »

**Le fait, sur ta propre page :** book **+1,32 %**, benchmark ^GSPC **+3,05 %**,
**alpha −1,73 %**, β −0,05.

**Traduction brutale :** sur cette période, **acheter l'indice et dormir aurait
rapporté plus du double.**

### ✅ La réponse

> "Correct, and it's on the page — the book underperformed the S&P over that
> window. But the book isn't trying to beat the index, it's a **shock hedge**:
> beta is minus 0.05, so it's built to be flat-to-positive when equities fall.
> Judging it on alpha versus a rising S&P is the wrong benchmark — it's like
> judging insurance on a year with no fire.
>
> What I'd actually judge it on is **drawdown of eight basis points** and a
> **Sharpe of 1.7**. That said, you're right that I should be showing it against
> a proper benchmark — a risk-parity or a long-vol book — and that's my next
> change."

> **Ne dis jamais « ce n'est pas grave ».** Tu reconnais, tu recadres le
> benchmark, **tu annonces le correctif**. C'est cette séquence qu'on évalue.

## Attaque 2 — « A 7 % win rate? »

**Le fait :** win rate **7,3 %** sur 21 trades.

**Ce que le trader pense :** *une stratégie qui gagne 1 fois sur 14.*

### ✅ La réponse

> "That number is misleading and I should relabel it. There aren't 21
> independent bets — there are **two entries and one exit**, and each one fans
> out into seven legs, so the counter treats every leg as a trade. The real
> question isn't hit rate, it's whether the **winners are bigger than the
> losers**: Brent made 187k, the equity hedge 82k, gold 53k, against 11k and
> 24k of losses. That's the actual shape of the book."

> ⚠️ **Corrige ce libellé sur le site avant mardi si tu peux.** Un chiffre qui
> demande une explication de trente secondes est un chiffre qui te coûte.

## Attaque 3 — « You're long oil in an oil shock? »

**Le fait, dans ton propre code :** `BZ=F: 0.08` en positif, et le commentaire
dit *« la ligne qui finit négative »* — alors que l'attribution montre
**+187,1 k**, ta meilleure ligne.

**Le problème :** ton commentaire de code **contredit** ton résultat. Un trader
qui lit le code te le dira.

### ✅ La réponse

> "That comment is stale — it's from an earlier revision where the Brent leg was
> sized differently. In the published run it's the biggest contributor at 187k.
> I'll clean it up."

> **Point plus profond, et c'est le meilleur de tout ton projet :** le
> commentaire du book dit *« un choc pétrolier se couvre en vendant les actions,
> pas en achetant du brut »* — et c'est **exactement ce que les chiffres
> montrent**. Le short S&P a rapporté 82 k **sans risque directionnel sur le
> pétrole**. Dis-le : *"The cleanest expression of an oil shock wasn't long oil
> — it was short equities. The hedge paid more reliably than the view."*
> **Ça, c'est du raisonnement de desk.**

## Bonus — la question la plus dangereuse

> *"Is this real money or a backtest?"*

**Réponse, sans détour :**

> "It's a backtest on real market data, and I'd never present it as anything
> else. The forecasts are published with a timestamp before the window, so
> there's no look-ahead — but it hasn't traded live. That's the honest limit of
> it."

> **Un candidat qui gonfle un projet perso est éliminé sur-le-champ.** Un
> candidat qui pose lui-même la limite gagne toute la crédibilité.

---

## Partie 4 — Les 3 questions d'Ali, version ShockDesk

Ali t'a dit : **2-3 questions max, intelligentes, personnalisées à la banque**,
et **plus perso s'il y a des traders**. Voici sa consigne appliquée à ton arme —
une question qui **révèle** ton projet sans jamais le pitcher.

## Q1 — stratégie FIC *(la consigne d'Ali, à poser en premier)*

> "DB is the number one European FIC house and last quarter was a record —
> 2.6 billion, up 16 percent, driven by rates and credit. When you're already
> number one in a region, where does the next point of market share come from:
> product density with existing clients, or taking share from US banks in
> Europe?"

## Q2 — la question qui fait passer ton projet *(la meilleure)*

> "I've been running a small research desk where I publish dated macro forecasts
> and then score myself against them — including the misses. What I keep finding
> is that **getting the direction right matters less than getting the timing
> right**. On a desk, when a macro view is correct but early, how do you
> actually manage that — is it a sizing decision, a stop discipline, or do you
> just carry the position?"

> 🔑 **C'est la question à poser si tu n'en poses qu'une.** Elle fait trois
> choses en une phrase : elle prouve que tu **construis** quelque chose, elle
> montre que tu **mesures tes erreurs**, et elle pose un **vrai problème de
> desk** auquel un trader a envie de répondre. Tu ne vends rien — tu demandes
> conseil, et ton projet passe en contrebande.
>
> Et si quelqu'un enchaîne avec *"what's the desk?"* — **tu as gagné**. Tu
> pitches sur invitation, ce qui n'a rien à voir avec pitcher spontanément.

## Q3 — pour les traders *(la consigne « plus perso » d'Ali)*

> "For the traders on the call — after the first few years, what actually keeps
> you in the seat? Is it the P&L, the intellectual side, or the client
> relationship?"

## ❌ Ce qu'il ne faut PAS faire

- ❌ Pitcher ShockDesk spontanément devant 100 personnes — **arrogant**
- ❌ Citer tes chiffres de P&L en public — personne n'a le contexte
- ❌ Poser une question dont la réponse est sur le site de DB
- ❌ Demander « des conseils pour intégrer DB » — trop générique

---

## Partie 5 — 🤖 Protocole Gemini *(à copier avec le PDF)*

> You are a Deutsche Bank rates trader running a 30-minute mock interview with
> me in English. I'm a French Master's student. English Front Office
> conversation is my weak point — I've never practised it. **Be sceptical, the
> way a real trader is.**
>
> **Rules:**
> 1. English only. **One question at a time**, then wait.
> 2. Keep questions **short and spoken**, like a desk conversation.
> 3. After each answer, give **three lines**: what worked, what to fix, and the
> better way to say it in desk English.
> 4. Correct French-sounding English immediately (*"expensive vol"* → *"rich
> vol"*, *"volatility"* → *"vol"*).
> 5. If I freeze, say *"take your time"* and wait. Don't rescue me.
> 6. **Push back on weak answers.** If I'm vague, say so.
>
> **Sequence:**
> 1. Tell me about yourself.
> 2. Why Deutsche Bank, not a US bank?
> 3. Why rates?
> 4. Tell me about ShockDesk. What is it and why did you build it?
> 5. **Your book returned 1.32% while the S&P did 3.05%. Your alpha is
> negative. Why should I be impressed?**
> 6. **A 7% win rate. Explain that to me.**
> 7. **Is this real money, or a backtest?**
> 8. Your best line was long Brent. But your own code comments say an oil shock
> is hedged by shorting equities, not buying crude. Which is it?
> 9. Walk me through Black-Scholes out loud. Which assumption breaks first?
> 10. You're short gamma and the market gaps. What happens?
> 11. Final one: you're on a call with a hundred people, the host asks for
> questions. Unmute and ask yours.
>
> **At the end:** a score out of 10 on fluency, a score out of 10 on technical
> content, whether you'd take me on your desk as an intern, and **the five
> expressions I should drill before Tuesday**.
>
> The attached PDF is my study material and my project. **Questions 5 to 8 are
> the ones I need to survive — don't go easy on them.** Start with question 1.

---

## Partie 6 — Ta semaine

| Jour | À faire |
|---|---|
| **Jeu 10** | Lire ce document + le cours bilingue **à voix haute** |
| **Ven 11** | Simulation Gemini complète. Noter les 5 expressions. |
| **Sam 12** | Refaire **uniquement les questions 5 à 8** (les attaques) |
| **Dim 13** | Corriger le libellé « win rate » sur le site + le commentaire `BZ=F` |
| **Lun 14** | **Q2 dix fois à voix haute.** Rien d'autre. |
| **Mar 15** | Yahoo Finance le matin. Connexion 17h55. **Q2 dans les 20 premières minutes.** |

---

## Le mot de la fin

Ton arme n'est **pas** le P&L de 337 k USD — c'est un backtest de six semaines,
tout le monde le sait.

**Ton arme, c'est que tu as construit un système qui affiche tes échecs en
public.** HYG et TLT sont marqués comme des misses sur une page que n'importe
qui peut ouvrir. Aucun étudiant ne fait ça, parce que ça demande d'accepter
d'avoir tort par écrit.

Un desk ne recrute pas quelqu'un qui a raison. Il recrute quelqu'un sur qui on
peut **compter quand il a tort**. Ta page le prouve mieux que n'importe quelle
phrase de motivation.

