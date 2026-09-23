# J1 — Parité call‑put, Forward, Black‑Scholes‑Merton
### Cours complet avec démonstrations · Bloc A · samedi 05/09/2026

> **Sources Drive (obligatoire à citer en oral)**
> **P :** Hull, *Fundamentals of Futures and Options Markets* — ch. forwards/futures, propriétés des options, Black‑Scholes‑Merton.
> **S :** WORDS *Questions de base* (forward, futures, repo, Sharpe) · WORDS *Questions Produits dérivés* (call/put, EU/US).
> Règle du mois : **un chiffre sans provenance n'est pas un chiffre.**

**Ticket de sortie J1 :** réciter les **6 hypothèses de Black‑Scholes** et écrire **la parité call‑put** les yeux fermés, en 60 secondes, FR puis EN.

---

## Comment lire ce cours

Il est écrit pour être travaillé **crayon en main, sans surligneur**. Chaque
démonstration est découpée en étapes numérotées : tu dois pouvoir refermer le
fichier et refaire l'étape suivante seul. Les blocs marqués

> 🎤 **Oral** — la phrase à sortir en entretien.

sont à dire **à voix haute, debout, chrono 90 s**. Les blocs

> ⚠️ **Piège** — l'erreur qui te fait perdre le Superday.

sont ce que l'intervieweur cherche. Enfin, les blocs

> 🧮 **Maths** — renvoi vers le module de rappel correspondant.

signalent un passage calculatoire dont **la marche est reprise plus lentement
ailleurs**.

### ⚠️ Si les maths sont rouillées, commence par M0

Ce cours suppose exponentielle, log, dérivées, loi normale. Si une ligne comme
$\lim_{m\to\infty}(1+\frac{r}{m})^{mT}=e^{rT}$ te bloque, **ce n'est pas un
problème de niveau, c'est un problème d'ordre de lecture.**

👉 **Lis d'abord [`M0-rappels-maths.md`](M0-rappels-maths.md)** (1 h 30, huit
modules courts avec micro-exercices corrigés). Il ne contient **que** les
maths utilisées ici, chacune reliée à l'endroit du J1 où elle sert.

**Il n'y a aucune honte à ça.** Un desk ne teste pas ta capacité à démontrer
un théorème : il teste ta capacité à manipuler ces objets vite et juste. M0
sert exactement à ça.

**Plan**

| § | Contenu | Ce que ça débloque |
|---|---|---|
| 0 | Briques : AOA, réplication, composition continue | tout le reste |
| 1 | Forward : $F=Se^{(r-q)T}$, FX, commo, forward vs futures | J1, J17, J18 |
| 2 | Parité call‑put : preuve par arbitrage, synthétiques, box | J1, J3 |
| 3 | Bornes de non‑arbitrage, convexité, américain vs européen | J1, J8 |
| 4 | **Black‑Scholes‑Merton : les 3 démonstrations complètes** | J1 → J22 |
| 5 | Lecture du modèle : $N(d_1)$, $N(d_2)$, ce qui casse | J4, J9, J10 |
| 6 | **Les grecs dérivés à la main** | J2, J5 |
| 7 | Application numérique fil rouge | TD |
| 8 | Oral FR/EN, pièges, flashcards | E, H |

---

# § 0. Les trois briques

## 0.1 Composition continue — pourquoi $e$ partout

### D'abord le sens, sans une seule formule

Je place 100 € à 5 % pendant un an. Tout dépend de **combien de fois** on me
verse les intérêts :

| Intérêts versés | Capital final |
|---|---|
| 1 fois (annuel) | $105{,}0000$ |
| 2 fois (semestriel) | $105{,}0625$ |
| 12 fois (mensuel) | $105{,}1162$ |
| 365 fois (quotidien) | $105{,}1267$ |
| **en continu** | $\mathbf{105{,}1271}$ |

Chaque ligne est un peu au-dessus de la précédente : les intérêts du début
produisent eux-mêmes des intérêts. Mais **ça plafonne**. Découper à l'infini ne
fait pas exploser le résultat : ça converge vers une limite, et cette limite
s'appelle $100\,e^{0{,}05}$.

**Voilà tout ce que dit la formule ci-dessous.** Le reste est de la plomberie.

### Maintenant l'écriture compacte

Un capital $A$ placé au taux annuel $r$ composé $m$ fois par an donne
$A\left(1+\frac{r}{m}\right)^{mT}$. On fait $m\to\infty$ :

$$\lim_{m\to\infty}\left(1+\frac{r}{m}\right)^{mT}
=\lim_{m\to\infty}\exp\left(mT\ln\left(1+\frac{r}{m}\right)\right)
=\exp\left(mT\cdot\frac{r}{m}+O(1/m)\right)=e^{rT}.$$

> 🧮 **Cette ligne te paraît brutale ? C'est normal, elle enchaîne trois
> outils d'un coup.** Elle est reprise **pas à pas, en cinq étapes**, dans
> [`M0-rappels-maths.md`](M0-rappels-maths.md), **module M4**. En résumé :
> on passe au log pour casser la puissance, on utilise $\ln(1+x)\approx x$
> quand $x$ est minuscule, **le $m$ se simplifie**, et il reste $rT$.
> Le symbole $O(1/m)$ se lit simplement **« + des poussières qui disparaissent »**.
> Rien à calculer là-dedans.

On garde la composition continue pour **une seule raison technique** : elle est
stable par addition d'intervalles ($e^{rT_1}e^{rT_2}=e^{r(T_1+T_2)}$) et se
dérive sans constante parasite, ce qui rend le calcul stochastique lisible.

**Conversion à connaître de tête** (Hull) : taux continu $r_c$ ↔ taux composé $m$ fois $r_m$ :
$$r_c=m\ln\left(1+\frac{r_m}{m}\right),\qquad r_m=m\left(e^{r_c/m}-1\right).$$

> ⚠️ **Piège** — en salle, un taux monétaire est en **Act/360 linéaire**, pas en continu.
> Le continu est une convention de modèle. Si on te demande le prix d'un dépôt,
> tu utilises $1+r\frac{n}{360}$, pas $e^{rT}$.

## 0.2 Absence d'opportunité d'arbitrage (AOA)

**Définition.** Un arbitrage est un portefeuille de valeur initiale $V_0\le 0$
tel que $V_T\ge 0$ presque sûrement et $\mathbb{P}(V_T>0)>0$. « Gagner sans
risque et sans mise. »

**Conséquence directe — loi du prix unique.** Si deux portefeuilles $A$ et $B$
ont **exactement les mêmes flux futurs dans tous les états du monde**, alors
$V_0(A)=V_0(B)$.

**Preuve.** Supposons $V_0(A)>V_0(B)$. Je vends $A$, j'achète $B$, j'encaisse
$V_0(A)-V_0(B)>0$ que je place au taux sans risque. À maturité les flux de $A$
et $B$ se compensent exactement, il me reste
$(V_0(A)-V_0(B))e^{rT}>0$ sans mise et sans risque : arbitrage. Contradiction.
Idem en inversant. Donc $V_0(A)=V_0(B)$. $\blacksquare$

**Toute la journée J1 est une application de ce théorème.** Parité call‑put,
forward, Black‑Scholes : trois fois le même argument, à trois niveaux de
sophistication (statique, statique, **dynamique**).

## 0.3 Réplication statique vs dynamique

| | Réplication statique | Réplication dynamique |
|---|---|---|
| Idée | on monte le portefeuille à $t=0$, on ne touche plus | on rebalance en continu |
| Outil | AOA + tableau de flux | Itô + EDP |
| Exemples | parité, forward, box spread | Black‑Scholes, delta‑hedge |
| Hypothèses | très peu (juste AOA) | beaucoup (les 6 de BS) |
| Robustesse | **quasi‑indestructible** | casse dès que la vol bouge |

> 🎤 **Oral** — « La parité call‑put ne dépend d'aucun modèle : c'est une
> réplication statique, donc elle tient même si Black‑Scholes est faux.
> Black‑Scholes, lui, est une réplication dynamique : il tient seulement si je
> peux vraiment me couvrir en continu, sans coût, à vol constante. »
> *EN:* “Put‑call parity is model‑free — a static replication. Black‑Scholes is
> a dynamic replication, so it only holds under its own hedging assumptions.”

---

# § 1. Le forward

> 🧮 **Maths** — tout le § 1 repose sur $e^a e^b=e^{a+b}$ et
> $\ln(a/b)=\ln a-\ln b$ : **module M1** de [`M0`](M0-rappels-maths.md).

## 1.1 Définition et payoff

Contrat de gré à gré : livraison de l'actif $S$ à la date $T$ contre le prix
$K$ fixé aujourd'hui. Payoff acheteur à maturité : $S_T-K$ (linéaire, pas
d'optionalité, pas de prime à $t=0$).

Le **prix forward** $F_0$ est le $K$ qui rend le contrat de valeur nulle à
l'initiation. Ne jamais confondre **prix forward** $F_0$ (un niveau de marché)
et **valeur du contrat** $f$ (un P&L latent, nul le jour 1).

## 1.2 Démonstration cash‑and‑carry — actif sans revenu

**Théorème.** Actif de prix spot $S_0$, sans revenu ni coût de portage, taux
sans risque continu $r$, maturité $T$ : $\;F_0=S_0e^{rT}$.

**Preuve par double inégalité (la seule qui compte en oral).**

**(a) Si $F_0>S_0e^{rT}$**, je monte à $t=0$ :

| Opération | Flux en $0$ | Flux en $T$ |
|---|---|---|
| Emprunter $S_0$ au taux $r$ | $+S_0$ | $-S_0e^{rT}$ |
| Acheter l'actif au comptant | $-S_0$ | $+S_T$ (je le détiens) |
| Vendre le forward (prix $F_0$) | $0$ | $F_0-S_T$ |
| **Total** | $\mathbf{0}$ | $\mathbf{F_0-S_0e^{rT}>0}$ |

Mise nulle, gain certain strictement positif : arbitrage. Donc $F_0\le S_0e^{rT}$.

**(b) Si $F_0<S_0e^{rT}$**, je fais l'inverse : vente à découvert de l'actif,
placement du cash, achat du forward. Flux en $T$ : $S_0e^{rT}-F_0>0$, mise
nulle : arbitrage. Donc $F_0\ge S_0e^{rT}$.

Les deux ensemble : $F_0=S_0e^{rT}$. $\blacksquare$

> ⚠️ **Piège** — la branche (b) suppose que **je peux emprunter le titre**
> (short). Sur une action *hard‑to‑borrow*, le repo spécial coûte cher : la borne
> basse se relâche et le forward peut coter durablement sous la théorie. C'est
> exactement le lien avec **J17 (repo special vs GC)**. Dis‑le : ça montre que
> tu sais qu'un desk n'est pas un manuel.

## 1.3 Avec dividende continu $q$ — la version equity/indice

**Théorème.** $\;\boxed{F_0=S_0e^{(r-q)T}}$

**Preuve.** Le rendement de dividende continu $q$ signifie qu'un titre détenu
paie en flux continu et que les dividendes sont **réinvestis en titre** : une
position initiale de $e^{-qT}$ action devient exactement **1 action** en $T$.
Je construis :

| Opération | Flux en $0$ | Position/flux en $T$ |
|---|---|---|
| Emprunter $S_0e^{-qT}$ | $+S_0e^{-qT}$ | $-S_0e^{-qT}e^{rT}$ |
| Acheter $e^{-qT}$ action, réinvestir les div. | $-S_0e^{-qT}$ | $+1$ action $=S_T$ |
| Vendre 1 forward | $0$ | $F_0-S_T$ |
| **Total** | $\mathbf 0$ | $\mathbf{F_0-S_0e^{(r-q)T}}$ |

AOA ⇒ le total doit être nul ⇒ $F_0=S_0e^{(r-q)T}$. $\blacksquare$

**Lecture desk.** $r-q$ est le **coût de portage net** (*cost of carry*). Si
$q>r$ (indice à gros dividendes, taux bas), le forward cote **sous** le spot :
c'est normal, ce n'est pas une anticipation baissière.

> 🎤 **Oral** — « Le forward n'est pas une prévision. C'est le spot capitalisé
> au coût de portage. Si l'indice forward est sous le spot, ça dit que le
> dividende dépasse le taux, pas que le marché est baissier. »

**Dividendes discrets.** Si l'actif verse des dividendes connus de valeur
actuelle $I=\sum_i D_ie^{-rt_i}$, la même preuve avec « acheter 1 action et
emprunter $I$ en plus » donne :
$$F_0=(S_0-I)e^{rT}.$$

## 1.4 FX — parité couverte des taux d'intérêt

Convention : $S$ = prix d'une unité de devise étrangère en devise domestique
(EUR/USD $=1{,}0850$ ⇒ domestique = USD, étrangère = EUR). La devise étrangère
est un actif qui « verse » le taux étranger $r_f$ : c'est un dividende continu.
En posant $q=r_f$ :

$$\boxed{F_0=S_0e^{(r_d-r_f)T}}\qquad\text{(covered interest rate parity)}$$

**Preuve directe.** Emprunter $S_0e^{-r_fT}$ USD, acheter $e^{-r_fT}$ EUR, les
placer au taux EUR ⇒ 1 EUR en $T$ ; vendre le forward. Flux nets en $T$ :
$F_0-S_0e^{(r_d-r_f)T}$, mise nulle ⇒ nul par AOA. $\blacksquare$

**Points de swap** = $F_0-S_0$, cotés en pips. Si $r_d>r_f$, la devise
étrangère est en **report** (premium).

> ⚠️ **Piège** — en pratique la CIP est violée depuis 2008 : c'est la **cross‑currency basis**
> (contrainte de bilan, coût de funding USD, xVA). Cite‑le, c'est un marqueur
> de sérieux. On y revient J16 (xVA) et J17 (repo).

## 1.5 Commodities — storage et convenience yield

Coût de stockage continu $u$ (assurance, entrepôt), **convenience yield** $y$
(valeur non monétaire de détenir le baril physique : sécuriser une raffinerie,
livrer un client) :

$$\boxed{F_0=S_0e^{(r+u-y)T}}$$

**Preuve.** Le stockage est un dividende négatif ($-u$), le convenience yield un
dividende positif ($+y$) : on remplace $q$ par $y-u$ dans §1.3. La borne haute
(a) reste un vrai arbitrage (cash‑and‑carry) ; la borne basse (b) exige
d'**emprunter du pétrole physique**, ce qui n'existe pas : d'où la possibilité
d'un $y$ élevé et durable. **L'asymétrie de la preuve EST la définition du
convenience yield.** $\blacksquare$

| Régime | Courbe | Signe | Lecture |
|---|---|---|---|
| **Contango** | $F>S$, croissante | $r+u>y$ | stocks pleins, marché mou |
| **Backwardation** | $F<S$, décroissante | $y>r+u$ | tension physique, prime au spot |

> 🎤 **Oral** (à recycler J18 et dans le pitch ShockDesk) — « En backwardation le
> marché me paie pour détenir le physique aujourd'hui : le convenience yield
> dépasse le carry. C'est un signal de tension d'offre, et c'est le régime dans
> lequel un choc géopolitique frappe le plus fort le front du Brent. »

## 1.6 Valeur d'un forward en cours de vie

Contrat initié à un strike $K$, il reste $T$ ans, le forward de même maturité
cote aujourd'hui $F_0$ :

$$\boxed{f=(F_0-K)e^{-rT}}$$

**Preuve.** Portefeuille A : le contrat (payoff $S_T-K$). Portefeuille B : un
forward neuf (payoff $S_T-F_0$, valeur 0) + $(F_0-K)e^{-rT}$ de cash (valeur
$F_0-K$ en $T$). Mêmes flux en $T$, donc même valeur en $0$ ; B vaut
$(F_0-K)e^{-rT}$. $\blacksquare$

## 1.7 Forward vs futures — la réponse en 4 lignes

| | Forward | Future |
|---|---|---|
| Lieu | OTC, bilatéral | marché organisé, chambre de compensation |
| Standardisation | sur mesure | contrat standard, taille fixe |
| Flux | **un seul en $T$** | **marge quotidienne (MTM)** |
| Risque de contrepartie | plein (⇒ CVA, J16) | mutualisé, marge initiale + variation |
| Prix | $F=Se^{(r-q)T}$ | idem **si $r$ déterministe** |

**Le seul point technique qui différencie les prix** (Cox‑Ingersoll‑Ross) :
le future verse ses gains **au jour le jour**, donc ils sont réinvestis au taux
court.
- Si $\mathrm{corr}(S,r)>0$ : quand le sous‑jacent monte, j'encaisse de la marge
  *et* je la replace à un taux devenu plus haut ⇒ le future est légèrement
  **plus cher** que le forward.
- Si $\mathrm{corr}(S,r)<0$ : l'inverse.
- Si $r$ est déterministe : **prix identiques** (théorème CIR 1981).

En pratique l'écart est négligeable sur equity court terme, **pas** sur les
contrats de taux longs (Eurodollar/SOFR ⇒ *convexity adjustment*, revu J15).

> 🎤 **Oral EN** — “Same economics, different plumbing. Daily margining makes the
> futures payoff path‑dependent through the reinvestment rate, so futures and
> forwards only price the same when rates are deterministic — otherwise you need
> a convexity adjustment.”

---

# § 2. La parité call‑put

## 2.1 Énoncé

Options **européennes**, même sous‑jacent, **même strike $K$**, **même maturité $T$**,
dividende continu $q$, taux $r$ :

$$\boxed{ C-P=S_0e^{-qT}-Ke^{-rT} }$$

Sans dividende : $C-P=S_0-Ke^{-rT}$. Avec dividendes discrets de VA $I$ :
$C-P=S_0-I-Ke^{-rT}$.

## 2.2 Démonstration par arbitrage — la version tableau

On compare deux portefeuilles, **à construire à $t=0$ et à ne plus toucher**.

- **Portefeuille A** : 1 call européen $(K,T)$ + $Ke^{-rT}$ de cash placé au taux $r$.
- **Portefeuille B** : 1 put européen $(K,T)$ + $e^{-qT}$ action, dividendes réinvestis
  (donc exactement 1 action en $T$).

Valeur en $T$, en séparant les deux états du monde :

| | $S_T\le K$ | $S_T>K$ |
|---|---|---|
| Call | $0$ | $S_T-K$ |
| Cash | $K$ | $K$ |
| **A total** | $\mathbf K$ | $\mathbf{S_T}$ |
| Put | $K-S_T$ | $0$ |
| Action | $S_T$ | $S_T$ |
| **B total** | $\mathbf K$ | $\mathbf{S_T}$ |

Dans **tous** les états, $A_T=B_T=\max(S_T,K)$. Par la loi du prix unique
(§0.2) : $A_0=B_0$, soit
$$C+Ke^{-rT}=P+S_0e^{-qT}\;\Longleftrightarrow\;C-P=S_0e^{-qT}-Ke^{-rT}.\qquad\blacksquare$$

**La table d'arbitrage à savoir dessiner** (cas $C-P>S_0e^{-qT}-Ke^{-rT}$, dit
*conversion* : le call est cher, je le vends) :

| Opération | Flux en $0$ | Flux en $T$, $S_T\le K$ | Flux en $T$, $S_T>K$ |
|---|---|---|---|
| Vendre le call | $+C$ | $0$ | $-(S_T-K)$ |
| Acheter le put | $-P$ | $K-S_T$ | $0$ |
| Acheter $e^{-qT}$ action (financée) | $-S_0e^{-qT}$ | $+S_T$ | $+S_T$ |
| Emprunter $Ke^{-rT}$ | $+Ke^{-rT}$ | $-K$ | $-K$ |
| **Total** | $\;C-P-S_0e^{-qT}+Ke^{-rT}>0$ | $\mathbf 0$ | $\mathbf 0$ |

J'encaisse **aujourd'hui**, je ne dois **rien** demain, dans aucun état : c'est
l'arbitrage. Donc l'écart ne peut pas exister. $\blacksquare$

> ⚠️ **Piège n°1 du J1** — la parité est fausse pour les options **américaines**.
> On n'a qu'un encadrement (§3.4). Si l'intervieweur dit « et sur des
> américaines ? », la bonne réponse commence par « ce n'est plus une égalité ».

> ⚠️ **Piège n°2** — même $K$, même $T$, même sous‑jacent, même **style**. Deux
> maturités différentes ⇒ pas de parité, mais des bornes calendaires.

## 2.3 Ce que la parité te donne gratuitement

**Les synthétiques** (à réciter comme un tableau de multiplication) :

$$\text{Call} = \text{Put} + \text{Forward}\qquad
\text{Put} = \text{Call} - \text{Forward}$$
$$\text{Action synthétique} = \text{Call} - \text{Put} + Ke^{-rT}\ \text{cash}$$
$$\text{Cash synthétique} = \text{Put} - \text{Call} + \text{action}$$

**Conséquences opérationnelles** :

1. **Un market maker cote une seule vol par strike.** Call et put de même
   $(K,T)$ portent **la même volatilité implicite** — sinon arbitrage de parité.
   C'est pour ça qu'on parle du « smile » sans préciser call ou put.
2. **Grecs.** En dérivant la parité : $\Delta_C-\Delta_P=e^{-qT}$,
   $\Gamma_C=\Gamma_P$, $\nu_C=\nu_P$. Le gamma et le véga d'un call et d'un put
   de mêmes caractéristiques sont **identiques** (démonstration en §6.7). Ça
   surprend les candidats moyens ; toi tu le prouves en une ligne.
3. **Reversal / conversion** : le trade d'arbitrage ci‑dessus est le pain
   quotidien d'un desk de market making listé.
4. **Box spread** : $(C_{K_1}-P_{K_1})-(C_{K_2}-P_{K_2})=(K_2-K_1)e^{-rT}$ :
   un prêt/emprunt synthétique. Prix du box ⇒ **taux implicite du marché
   options**. (Rappelle‑toi le blow‑up d'un particulier sur box spreads SPX,
   2017 : le box sur options **américaines** peut être exercé par anticipation.)

## 2.4 Corollaire immédiat : le put ATM forward

Si $K=F_0=S_0e^{(r-q)T}$ alors $Ke^{-rT}=S_0e^{-qT}$, donc
$$C=P.$$
**Au strike forward, le call et le put valent exactement la même chose.** C'est
la définition du *ATM forward*, la référence de cotation des desks de vol
(et le point de départ du smile, J4).

---

# § 3. Bornes de non‑arbitrage et américain vs européen

## 3.1 Bornes élémentaires (européennes, dividende $q$)

$$\max\left(0,\;S_0e^{-qT}-Ke^{-rT}\right)\;\le\;C\;\le\;S_0e^{-qT}$$
$$\max\left(0,\;Ke^{-rT}-S_0e^{-qT}\right)\;\le\;P\;\le\;Ke^{-rT}$$

**Preuve de la borne basse du call.** Portefeuille A (call + $Ke^{-rT}$ cash) vaut
$\max(S_T,K)\ge S_T$ en $T$ ; portefeuille B ($e^{-qT}$ action) vaut $S_T$. A
domine B état par état, donc $A_0\ge B_0$ :
$C+Ke^{-rT}\ge S_0e^{-qT}$. Avec $C\ge 0$ (option = droit) on conclut. $\blacksquare$

*Borne haute :* le call donne au plus l'action, donc il ne peut pas valoir plus
cher que l'action portée. Sinon : vendre le call, acheter $e^{-qT}$ action,
gain immédiat, obligation couverte.

## 3.2 Monotonie et convexité en strike

Pour $K_1<K_2<K_3$ avec $K_2=\lambda K_1+(1-\lambda)K_3$ :

1. $C(K_1)\ge C(K_2)$ — décroissant en strike ; sinon **call spread** de prix négatif = argent gratuit.
2. $C(K_1)-C(K_2)\le (K_2-K_1)e^{-rT}$ — pente bornée.
3. $C(K_2)\le\lambda C(K_1)+(1-\lambda)C(K_3)$ — **convexité** ; sinon le **butterfly** a un prix négatif alors que son payoff est $\ge 0$.

Ces trois inégalités sont exactement les conditions d'absence d'arbitrage
**statique** d'une surface de vol. On les recroise **J10 (`j10_butterfly_arb.py`)**.

> 🎤 **Oral** — « Un butterfly a un payoff toujours positif : son prix doit être
> positif. Donc le prix du call est convexe en strike, donc la densité
> risque‑neutre implicite $\partial^2C/\partial K^2e^{rT}$ est positive. Une
> surface qui viole ça n'est pas une surface, c'est un bug. »

## 3.3 Call américain sans dividende : ne jamais exercer par anticipation

**Théorème.** Sans dividende ($q=0$, $r>0$), un call américain vaut son
équivalent européen : $C_{US}=C_{EU}$, et l'exercice anticipé est strictement
sous‑optimal.

**Preuve.** Par §3.1, $C_{EU}\ge S_0-Ke^{-rT}$. Or $r>0$ ⇒ $Ke^{-rT}<K$ ⇒
$$C_{EU}\ge S_0-Ke^{-rT}>S_0-K=\text{valeur intrinsèque (exercice immédiat)}.$$
Le call **vivant** vaut donc toujours strictement plus que le call exercé :
il vaut mieux le **vendre** que l'exercer. Le droit d'exercice anticipé n'a
aucune valeur, donc $C_{US}=C_{EU}$. $\blacksquare$

**Deux intuitions à donner en plus de la preuve :**
1. **Trésorerie** — exercer, c'est payer $K$ aujourd'hui au lieu de $T$ : je
   perds les intérêts $K(1-e^{-rT})$.
2. **Assurance** — tant que je n'exerce pas, je garde la protection à la baisse
   sous $K$. Exercer, c'est jeter l'option gratuitement.

**Avec dividende**, l'exercice anticipé d'un call peut devenir optimal, juste
**avant** un détachement important (on capture $D$ contre la perte de valeur
temps). Pour un **put américain**, l'exercice anticipé peut toujours être
optimal (récupérer $K$ tôt et le placer), donc $P_{US}>P_{EU}$ en général.

## 3.4 Parité américaine : un encadrement

$$S_0-K\;\le\;C_{US}-P_{US}\;\le\;S_0-Ke^{-rT}\qquad (q=0)$$

À citer tel quel : « sur des américaines, la parité devient un encadrement, la
borne haute étant la parité européenne. »

---

# § 4. Black‑Scholes‑Merton — les démonstrations complètes

C'est le cœur du J1 et la question la plus fréquente en Superday dérivés.
Tu dois savoir faire **trois** démonstrations : l'EDP (Black‑Scholes 1973),
l'espérance risque‑neutre (Harrison‑Pliska), et la limite du binomial (CRR).
Elles ne servent pas au même moment de l'entretien.

## 4.1 Les 6 hypothèses — à réciter mot pour mot

> **H1.** Le sous‑jacent suit un **mouvement brownien géométrique** à
> paramètres constants : $dS_t=\mu S_t dt+\sigma S_t dW_t$. Trajectoires
> **continues** (pas de saut), rendements log‑normaux.
> **H2.** La **volatilité $\sigma$ est constante** et connue (et le taux $r$ aussi).
> **H3.** **Pas de friction** : ni coûts de transaction, ni taxes, ni bid‑ask ;
> actifs parfaitement divisibles.
> **H4.** **Vente à découvert autorisée** sans restriction, et emprunt/prêt
> **au même taux sans risque $r$**, constant.
> **H5.** **Pas d'arbitrage** et **négociation en continu** (le hedge peut être
> rebalancé à tout instant).
> **H6.** L'option est **européenne**, et le sous‑jacent ne verse pas de
> dividende sur la période (ou un dividende continu $q$ connu, extension Merton).

**Mnémotechnique orale (30 s) :** *« Brownien géométrique · vol et taux
constants · pas de frictions · short et funding libres au taux sans risque ·
AOA et trading continu · européenne, dividende connu. »*

*EN:* “Geometric Brownian motion, constant vol and rates, no frictions, unrestricted
shorting and borrowing at the risk‑free rate, no arbitrage with continuous
trading, European exercise with known dividend yield.”

> ⚠️ **Piège** — beaucoup de candidats disent « les rendements sont normaux ».
> **Faux :** ce sont les **log‑rendements** qui sont normaux, donc $S_T$ est
> **log‑normale** (et positive). Dis‑le correctement, c'est un filtre.

## 4.2 Boîte à outils : le lemme d'Itô

Pour $X_t$ vérifiant $dX_t=a dt+b dW_t$ et $f(X,t)$ deux fois dérivable :

$$df=\left(\frac{\partial f}{\partial t}+a\frac{\partial f}{\partial X}
+\frac12 b^2\frac{\partial^2f}{\partial X^2}\right)dt
+b\frac{\partial f}{\partial X} dW_t.$$

> 🧮 **Maths** — dérivées partielles ($f_t$, $f_X$, $f_{XX}$) et règle de la
> chaîne : **module M8** de [`M0`](M0-rappels-maths.md). Approximation de
> Taylor : **module M3**.

**D'où vient le terme en $\frac12 b^2 f_{XX}$ ?** Développement de Taylor à
l'ordre 2 :
$$df=f_t dt+f_X dX+\tfrac12 f_{XX}(dX)^2+\dots$$
avec les règles du calcul d'Itô $\;(dt)^2=0$, $dt dW=0$, $\boxed{(dW)^2=dt}$ :
$$(dX)^2=(a dt+b dW)^2=b^2(dW)^2=b^2dt.$$
Le terme d'ordre 2, qui serait négligeable en calcul classique, **survit** parce
que le brownien a une variation quadratique non nulle. **Ce terme, c'est le
gamma.** Toute la finance d'options tient dans ce $\frac12$.

**Application — solution du GBM.** Avec $f=\ln S$, $a=\mu S$, $b=\sigma S$ :
$f_S=1/S$, $f_{SS}=-1/S^2$, $f_t=0$ :
$$d\ln S_t=\left(\mu-\frac{\sigma^2}{2}\right)dt+\sigma dW_t
\;\Longrightarrow\;
\boxed{S_T=S_0\exp\left[\left(\mu-\tfrac{\sigma^2}{2}\right)T+\sigma W_T\right]}$$
avec $W_T\sim\mathcal N(0,T)$. Donc
$$\ln S_T\sim\mathcal N\!\left(\ln S_0+\left(\mu-\tfrac{\sigma^2}{2}\right)T,\;\sigma^2T\right).$$

> 🧮 **Maths** — log-normale et origine du $-\sigma^2/2$ : **module M7** de
> [`M0`](M0-rappels-maths.md), avec l'exemple chiffré moyenne $110{,}52$ vs
> médiane $105{,}65$.

> ⚠️ **Piège classique d'entretien** — « pourquoi $-\sigma^2/2$ ? »
> Réponse : parce que $\mathbb E[S_T]=S_0e^{\mu T}$ **impose** ce terme
> correcteur (inégalité de Jensen : $\mathbb E[e^X]=e^{\mathbb E X+\frac12\mathrm{Var}X}$).
> Le drift **arithmétique** est $\mu$, le drift **géométrique/médian** est
> $\mu-\sigma^2/2$. C'est aussi pourquoi la moyenne d'un portefeuille volatile
> dépasse sa médiane : le *volatility drag*.

## 4.3 Démonstration 1 — l'EDP de Black‑Scholes par delta‑hedging

**Étape 1. Dynamique de l'option.** Soit $V(S,t)$ le prix de l'option. Itô :
$$dV=\left(V_t+\mu S V_S+\tfrac12\sigma^2S^2V_{SS}\right)dt+\sigma S V_S dW_t.$$

**Étape 2. Le portefeuille couvert.** Je construis
$$\Pi=V-\Delta S,\qquad \Delta:=V_S \;\text{(quantité gelée sur }[t,t+dt]).$$
Sur l'intervalle infinitésimal, avec un sous‑jacent versant $q$ (la position
$-\Delta$ action **coûte** le dividende $q\Delta S dt$) :
$$d\Pi=dV-\Delta dS-q\Delta S dt.$$
En substituant :
$$d\Pi=\left(V_t+\mu SV_S+\tfrac12\sigma^2S^2V_{SS}\right)dt+\sigma SV_S dW
-V_S\left(\mu S dt+\sigma S dW\right)-qSV_S dt.$$

**Étape 3. Le miracle.** Les termes en $\mu S V_S dt$ s'annulent **et** les
termes en $\sigma SV_S dW$ s'annulent :
$$\boxed{d\Pi=\left(V_t+\tfrac12\sigma^2S^2V_{SS}-qSV_S\right)dt}$$
Plus de $dW$ : le portefeuille est **localement sans risque**. Plus de $\mu$ :
**le rendement espéré du sous‑jacent a disparu du prix de l'option.** C'est le
résultat le plus contre‑intuitif et le plus important de la finance de marché.

**Étape 4. AOA.** Un portefeuille sans risque doit rapporter exactement $r$ :
$$d\Pi=r\Pi dt=r\left(V-SV_S\right)dt.$$
Égalité des deux expressions :
$$V_t+\tfrac12\sigma^2S^2V_{SS}-qSV_S=rV-rSV_S$$

$$\boxed{\;\frac{\partial V}{\partial t}+(r-q)S\frac{\partial V}{\partial S}
+\frac12\sigma^2S^2\frac{\partial^2V}{\partial S^2}-rV=0\;}$$

C'est **l'EDP de Black‑Scholes**. Elle est valable pour **tout** dérivé
européen sur $S$ ; ce qui distingue un call d'un put d'un digital, c'est
uniquement la **condition terminale** :
- call : $V(S,T)=\max(S-K,0)$ ;
- put : $V(S,T)=\max(K-S,0)$ ;
- forward : $V(S,T)=S-K$ ;
- digital cash‑or‑nothing : $V(S,T)=\mathbb 1_{S>K}$.

**Étape 5. Lecture en grecs (à ressortir J2).** L'EDP se réécrit :
$$\Theta+(r-q)S\Delta+\tfrac12\sigma^2S^2\Gamma=rV.$$
Pour un portefeuille **delta‑neutre** ($\Delta=0$) et $r=0$ :
$$\boxed{\Theta=-\tfrac12\sigma^2S^2\Gamma}$$
**Le theta est le loyer du gamma.** Long gamma ⇒ theta négatif : je paie tous
les jours pour le droit de gagner sur les mouvements. Short gamma ⇒ j'encaisse
du theta et je prie. Cette relation est la phrase la plus rentable de tout J1 :
elle répond à « pourquoi un long straddle perd de l'argent si rien ne bouge ? »
et à « quel est le P&L d'un market maker delta‑hedgé ? ».

**Étape 6. Le P&L du hedgeur (bonus élite, prépare J5).** Sur un pas $\delta t$,
avec un mouvement réalisé $\delta S$, le P&L d'un vendeur d'option delta‑hedgé
est
$$\mathrm{PnL}\approx\frac12\Gamma\left[(\delta S)^2-\sigma^2S^2\delta t\right]
=\frac12\Gamma S^2\left[\sigma_{\text{réalisée}}^2-\sigma_{\text{implicite}}^2\right]\delta t.$$
**Le gamma trading, c'est parier vol réalisée contre vol implicite.** Rien
d'autre. (`j05_delta_hedge_mc.py` le vérifiera numériquement.)

## 4.4 Démonstration 2 — l'espérance risque‑neutre (la voie moderne)

**Étape 1. Le théorème fondamental.** AOA ⟺ il existe une mesure de probabilité
$\mathbb Q$ (dite *risque‑neutre*, équivalente à $\mathbb P$) sous laquelle tout
prix d'actif **actualisé** est une martingale. Marché complet ⟺ $\mathbb Q$ est
unique. Sous $\mathbb Q$ :
$$dS_t=(r-q)S_t dt+\sigma S_t dW^{\mathbb Q}_t,\qquad
V_0=e^{-rT} \mathbb E^{\mathbb Q}\!\left[V(S_T)\right].$$
Le drift réel $\mu$ est **remplacé par $r-q$** (théorème de Girsanov : changer
de mesure change le drift, jamais la volatilité). C'est le pendant probabiliste
de la disparition de $\mu$ à l'étape 3 de §4.3.

> 🎤 **Oral** — « Risque‑neutre ne veut pas dire que les investisseurs sont
> indifférents au risque. Ça veut dire que, comme je peux répliquer l'option par
> du sous‑jacent et du cash, le prix ne peut pas dépendre de la prime de risque :
> elle est déjà dans le spot. Donc je peux calculer *comme si* tout le monde
> exigeait $r$. »

**Étape 2. Loi de $S_T$ sous $\mathbb Q$.**
$$S_T=S_0\exp\left[\left(r-q-\tfrac{\sigma^2}{2}\right)T+\sigma\sqrt T Z\right],
\qquad Z\sim\mathcal N(0,1).$$
Notons $m=\ln S_0+(r-q-\frac{\sigma^2}{2})T$ et $s=\sigma\sqrt T$, de sorte que
$\ln S_T\sim\mathcal N(m,s^2)$.

**Étape 3. Poser l'intégrale.**
$$C=e^{-rT} \mathbb E^{\mathbb Q}\left[(S_T-K)^+\right]
=e^{-rT}\underbrace{\mathbb E^{\mathbb Q}\!\left[S_T\mathbb 1_{S_T>K}\right]}_{(\text{I})}
-e^{-rT}K\underbrace{\mathbb Q(S_T>K)}_{(\text{II})}.$$

**Étape 4. Calcul de (II) — la probabilité d'exercice.**
$$S_T>K\iff m+sZ>\ln K\iff Z>\frac{\ln K-m}{s}=:-d_2.$$
Donc, par symétrie de la loi normale centrée réduite,
$$\mathbb Q(S_T>K)=\mathbb P(Z>-d_2)=N(d_2),\qquad
\boxed{d_2=\frac{\ln(S_0/K)+\left(r-q-\frac{\sigma^2}{2}\right)T}{\sigma\sqrt T}}$$

**Étape 5. Calcul de (I) — l'astuce du changement de mesure.**
$$\mathbb E\left[S_T\mathbb 1_{S_T>K}\right]
=\int_{-d_2}^{+\infty}S_0e^{(r-q-\frac{\sigma^2}{2})T+s z} 
\frac{1}{\sqrt{2\pi}}e^{-z^2/2} dz.$$
On complète le carré à l'exposant :
$$-\frac{z^2}{2}+sz=-\frac{(z-s)^2}{2}+\frac{s^2}{2},
\qquad s^2=\sigma^2T,$$

> 🧮 **Maths** — c'est **le seul passage calculatoire dur du J1**, et c'est un
> exercice de collège déguisé (celui de l'équation du second degré). Repris
> pas à pas au **module M6** de [`M0`](M0-rappels-maths.md). À retenir en une
> phrase : *multiplier une cloche par $e^{sz}$, c'est déplacer son centre de
> $s$* — et ce décalage est exactement ce qui transforme $d_2$ en $d_1$.

donc
$$\mathbb E\left[S_T\mathbb 1_{S_T>K}\right]
=S_0e^{(r-q-\frac{\sigma^2}{2})T+\frac{\sigma^2T}{2}}
\int_{-d_2}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-(z-s)^2/2}dz
=S_0e^{(r-q)T}\int_{-d_2-s}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-u^2/2}du$$
(par le changement de variable $u=z-s$). L'intégrale vaut $N(d_2+s)$, et
$$d_2+s=d_2+\sigma\sqrt T=:d_1
=\frac{\ln(S_0/K)+\left(r-q+\frac{\sigma^2}{2}\right)T}{\sigma\sqrt T}.$$
Donc $(\text{I})=S_0e^{(r-q)T}N(d_1)$.

**Étape 6. Recollage.**
$$C=e^{-rT}\left[S_0e^{(r-q)T}N(d_1)-KN(d_2)\right]$$

$$\boxed{ C=S_0e^{-qT}N(d_1)-Ke^{-rT}N(d_2) }$$

et par la parité call‑put (§2.1) — **jamais en refaisant l'intégrale** :
$$P=C-S_0e^{-qT}+Ke^{-rT}
=Ke^{-rT}\left[1-N(d_2)\right]-S_0e^{-qT}\left[1-N(d_1)\right]$$

$$\boxed{ P=Ke^{-rT}N(-d_2)-S_0e^{-qT}N(-d_1) }\qquad\blacksquare$$

> 🎤 **Oral EN (90 s, à chronométrer)** — “Under the risk‑neutral measure the
> discounted stock is a martingale, so the drift is $r-q$ and $S_T$ is
> lognormal. The call price is the discounted expectation of $(S_T-K)^+$, which
> splits into two pieces: the expected stock conditional on exercise, and $K$
> times the exercise probability. The second gives $N(d_2)$ directly; the first
> requires completing the square, which shifts the integration bound by
> $\sigma\sqrt T$ and gives $N(d_1)$. Hence
> $C=Se^{-qT}N(d_1)-Ke^{-rT}N(d_2)$.”

## 4.5 Démonstration 3 — la limite du binomial (CRR)

Utile quand l'intervieweur veut voir si tu comprends **d'où vient la
probabilité risque‑neutre**, sans stochastique.

**Un pas.** Sur $\delta t$, $S$ passe à $uS$ ou $dS$. Je réplique l'option par
$\Delta$ actions + $B$ cash :
$$\Delta uS+Be^{r\delta t}=V_u,\qquad \Delta dS+Be^{r\delta t}=V_d.$$
Soustraction :
$$\boxed{\Delta=\frac{V_u-V_d}{S(u-d)}}\quad\text{(le delta = ratio de couverture)}$$
En réinjectant et en réarrangeant :
$$V=e^{-r\delta t}\left[pV_u+(1-p)V_d\right],\qquad
\boxed{p=\frac{e^{(r-q)\delta t}-d}{u-d}}$$
$p$ n'est **pas** la probabilité réelle de hausse : c'est la probabilité qui
rend $\mathbb E[S_{\delta t}]=Se^{(r-q)\delta t}$. La probabilité risque‑neutre
**tombe** de l'algèbre de la réplication, on ne la postule pas.

**Passage à la limite (CRR).** On pose $u=e^{\sigma\sqrt{\delta t}}$,
$d=1/u$. Alors $\ln S_T$ est une somme de $n=T/\delta t$ variables i.i.d.
$\pm\sigma\sqrt{\delta t}$ de moyenne $(2p-1)\sigma\sqrt{\delta t}$. Un
développement limité de $p$ à l'ordre $\sqrt{\delta t}$ donne
$$p\simeq\frac12+\frac{r-q-\frac{\sigma^2}{2}}{2\sigma}\sqrt{\delta t},$$
d'où $\mathbb E[\ln S_T]\to\ln S_0+(r-q-\frac{\sigma^2}{2})T$ et
$\mathrm{Var}[\ln S_T]\to\sigma^2T$. Le **théorème central limite** donne la
log‑normalité, et l'espérance actualisée converge vers la formule de
Black‑Scholes. $\blacksquare$

> 🎤 **Oral** — « Le binomial, c'est Black‑Scholes avec les mains : le delta
> tombe de deux équations à deux inconnues, la probabilité risque‑neutre est
> celle qui fait croître le sous‑jacent au taux sans risque, et le TCL fait le
> reste. »

---

# § 5. Lire la formule comme un trader

> 🧮 **Maths** — la loi normale, $\phi$ contre $N$, la symétrie
> $N(-x)=1-N(x)$ : **module M5** de [`M0`](M0-rappels-maths.md).

## 5.1 Décomposition économique

$$C=\underbrace{S_0e^{-qT}N(d_1)}_{\text{ce que je reçois}}
-\underbrace{Ke^{-rT}N(d_2)}_{\text{ce que je paie}}$$

- $N(d_2)=\mathbb Q(S_T>K)$ : **probabilité risque‑neutre d'exercer**.
  $Ke^{-rT}N(d_2)$ = valeur actuelle du strike, pondérée par la probabilité de
  le payer.
- $N(d_1)$ : **ce n'est pas une probabilité**. C'est le delta ($\Delta=e^{-qT}N(d_1)$),
  et aussi $\mathbb Q^S(S_T>K)$ : la probabilité d'exercice sous la mesure
  *stock numéraire*, c'est‑à‑dire pondérée par la valeur du sous‑jacent.
  $S_0e^{-qT}N(d_1)$ = valeur actuelle de l'action **conditionnelle à l'exercice**.
- Toujours $d_1>d_2$ (car $d_1-d_2=\sigma\sqrt T>0$), donc $N(d_1)>N(d_2)$ : la
  version pondérée par le prix est plus optimiste, parce que les scénarios où
  l'on exerce sont ceux où $S$ est grand.

> ⚠️ **Piège** — « $N(d_1)$ est la probabilité que l'option finisse dans la
> monnaie » : **faux**, c'est $N(d_2)$. Erreur classique, sanctionnée.

**Digitale (cash‑or‑nothing)** : $\;e^{-rT}N(d_2)$ pour un call digital payant 1.
Donc $\;\partial C/\partial K=-e^{-rT}N(d_2)$ : la dérivée du call en strike
donne la digitale, et la dérivée seconde donne la **densité risque‑neutre**
(Breeden‑Litzenberger, revu J10) :
$$\frac{\partial^2C}{\partial K^2}=e^{-rT}\phi_{\mathbb Q}(K).$$

## 5.2 Cas limites (à vérifier en oral pour montrer qu'on maîtrise)

| Limite | Comportement | Pourquoi |
|---|---|---|
| $\sigma\to0$ | $C\to e^{-rT}(F_0-K)^+$ | plus d'incertitude : forward pur |
| $\sigma\to\infty$ | $C\to S_0e^{-qT}$ | l'option devient l'action |
| $T\to0$ | $C\to(S_0-K)^+$ | valeur intrinsèque |
| $S\to\infty$ | $C\to S_0e^{-qT}-Ke^{-rT}$ | forward, deep ITM |
| $S\to0$ | $C\to0$, $P\to Ke^{-rT}$ | put = zéro‑coupon |
| $K=F_0$ | $C=P$ | ATM forward (§2.4) |

**Approximation ATM à connaître de tête** (pour le mental math et le bloc 0) :
$$C_{ATMF}\approx0{,}4\sigma\sqrt T S e^{-rT}.$$
**Dérivation :** à $K=F$, $d_1=\frac{\sigma\sqrt T}{2}$, $d_2=-\frac{\sigma\sqrt T}{2}$, et
$N(x)\approx\frac12+\frac{x}{\sqrt{2\pi}}$ pour $x$ petit, d'où
$C\approx Fe^{-rT}\frac{\sigma\sqrt T}{\sqrt{2\pi}}$ et $1/\sqrt{2\pi}\approx0{,}399$.
**Exemple à sortir sans calculette :** $S=100$, $\sigma=20$ %, $T=1$ ⇒ call ATM
$\approx 0{,}4\times0{,}20\times100=8$.

## 5.3 Ce qui casse dans le vrai monde — la liste de l'intervieweur

| Hypothèse | Réalité | Conséquence marché | Vu au jour |
|---|---|---|---|
| H1 continuité | **sauts** (gaps, résultats, OPA) | queues épaisses, le hedge saute | J4, J7 |
| H2 vol constante | vol **stochastique**, clusters | **smile / skew**, surface | J4, J10 |
| H3 sans friction | bid‑ask, coûts | on ne hedge pas en continu ⇒ bande de rebalancement | J5 |
| H4 même taux | funding ≠ dépôt, repo spécial | **xVA**, FVA, basis | J16, J17 |
| H5 continu | discret | erreur de réplication $\propto\sqrt{\delta t}$ | J5 |
| H6 européenne | américaines, exotiques | early exercise, barrières | J7, J8 |

**La phrase qui clôt le sujet** (à mémoriser) :

> 🎤 « Black‑Scholes est **faux mais universel** : le marché ne l'utilise pas
> pour croire au modèle, il l'utilise comme un **dictionnaire prix ↔ volatilité
> implicite**. La preuve, c'est le smile : si le modèle était vrai, la surface
> serait plate. On cote la vol, pas le prix. »
> *EN:* “Nobody believes Black‑Scholes; everybody quotes in it. It's a
> price‑to‑vol dictionary. The existence of the smile is the market telling you
> the model is wrong — and by how much.”

---

# § 6. Les grecs, dérivés à la main

> 🧮 **Maths** — un grec **est** une dérivée. Les six dérivées utiles et la
> règle de la chaîne : **module M2** de [`M0`](M0-rappels-maths.md).
> Le dictionnaire grec ↔ dérivée partielle : **module M8**.

Notations : $\phi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ (densité), $N$ (répartition),
$C=Se^{-qT}N(d_1)-Ke^{-rT}N(d_2)$.

## 6.1 Le lemme qui fait tout tomber

$$\boxed{\;S e^{-qT}\phi(d_1)=Ke^{-rT}\phi(d_2)\;}$$

**Preuve.** $d_2=d_1-\sigma\sqrt T$, donc
$$\frac{\phi(d_1)}{\phi(d_2)}=\exp\left[-\tfrac12 d_1^2+\tfrac12(d_1-\sigma\sqrt T)^2\right]
=\exp\left[-d_1\sigma\sqrt T+\tfrac12\sigma^2T\right].$$
Or, par définition de $d_1$, $\;d_1\sigma\sqrt T=\ln(S/K)+(r-q)T+\frac{\sigma^2}{2}T$, donc
$$\frac{\phi(d_1)}{\phi(d_2)}=\exp\left[-\ln(S/K)-(r-q)T\right]=\frac{K}{S}e^{-(r-q)T},$$
c'est‑à‑dire $S e^{-qT}\phi(d_1)=Ke^{-rT}\phi(d_2)$. $\blacksquare$

**Conséquence :** en dérivant $C$, tous les termes contenant $\partial d_1$ et
$\partial d_2$ se compensent (car $\partial d_1=\partial d_2$ pour $S$, $\sigma$
étant fixé... voir ci‑dessous). C'est pour ça que le delta est simplement
$e^{-qT}N(d_1)$ et pas une expression monstrueuse.

## 6.2 Delta

$$\frac{\partial C}{\partial S}=e^{-qT}N(d_1)+Se^{-qT}\phi(d_1)\frac{\partial d_1}{\partial S}
-Ke^{-rT}\phi(d_2)\frac{\partial d_2}{\partial S}.$$
Comme $\frac{\partial d_1}{\partial S}=\frac{\partial d_2}{\partial S}=\frac{1}{S\sigma\sqrt T}$
et par le lemme §6.1, les deux derniers termes s'annulent :
$$\boxed{\Delta_C=e^{-qT}N(d_1)\in(0,e^{-qT}),\qquad \Delta_P=-e^{-qT}N(-d_1)}$$

## 6.3 Gamma

$$\Gamma=\frac{\partial\Delta}{\partial S}=e^{-qT}\phi(d_1)\frac{\partial d_1}{\partial S}
\quad\Longrightarrow\quad
\boxed{\Gamma=\frac{e^{-qT}\phi(d_1)}{S\sigma\sqrt T}>0}$$

Maximal près de l'ATM et **explose quand $T\to0$** (en $1/\sqrt T$) : c'est le
cauchemar du market maker la veille de l'expiration (le *pin risk*). Identique
call/put.

## 6.4 Vega

$$\frac{\partial C}{\partial\sigma}=Se^{-qT}\phi(d_1)\frac{\partial d_1}{\partial\sigma}
-Ke^{-rT}\phi(d_2)\frac{\partial d_2}{\partial\sigma}
=Se^{-qT}\phi(d_1)\left(\frac{\partial d_1}{\partial\sigma}-\frac{\partial d_2}{\partial\sigma}\right)$$
(lemme §6.1), et $d_1-d_2=\sigma\sqrt T$ ⇒ la différence des dérivées vaut $\sqrt T$ :

$$\boxed{\nu=Se^{-qT}\phi(d_1)\sqrt T>0}$$

**Toujours positif** pour une option vanille, call **et** put. Maximal ATM.
Croît en $\sqrt T$ : **le véga est dans les maturités longues, le gamma dans les
courtes.** (Note : $\nu=\Gamma S^2\sigma T$ — relation à ressortir J2.)
Convention desk : on divise par 100 pour avoir le véga « par point de vol ».

## 6.5 Theta

$$\boxed{\Theta_C=-\frac{Se^{-qT}\phi(d_1)\sigma}{2\sqrt T}
+qSe^{-qT}N(d_1)-rKe^{-rT}N(d_2)}$$
$$\Theta_P=-\frac{Se^{-qT}\phi(d_1)\sigma}{2\sqrt T}
-qSe^{-qT}N(-d_1)+rKe^{-rT}N(-d_2)$$

Le premier terme (**décroissance de la valeur temps**) est toujours négatif :
c'est le loyer du gamma (§4.3, étape 5). Convention desk : theta **par jour** =
$\Theta/365$.

> ⚠️ **Piège** — « le theta est toujours négatif » : **faux**. Un put européen
> deep ITM sans dividende a un **theta positif** (le terme $+rKe^{-rT}N(-d_2)$
> domine : plus le temps passe, plus la valeur actuelle du strike encaissé se
> rapproche). Idem pour un call deep ITM sur sous‑jacent à gros dividende.

## 6.6 Rho

$$\boxed{\rho_C=KTe^{-rT}N(d_2)>0,\qquad \rho_P=-KTe^{-rT}N(-d_2)<0}$$

Un call est long taux (je diffère le paiement du strike), un put est short taux.
Faible sur du court terme equity, **dominant** sur les options de taux longues.

## 6.7 Les relations à sortir sans réfléchir

| Relation | Preuve en une ligne |
|---|---|
| $\Delta_C-\Delta_P=e^{-qT}$ | dériver la parité en $S$ |
| $\Gamma_C=\Gamma_P$ | dériver deux fois : le terme de parité est linéaire en $S$ |
| $\nu_C=\nu_P$ | la parité ne dépend pas de $\sigma$ |
| $\Theta_C-\Theta_P=-qSe^{-qT}+rKe^{-rT}$ | dériver la parité en $t$ |
| $\Theta+(r-q)S\Delta+\frac12\sigma^2S^2\Gamma=rV$ | c'est l'EDP elle‑même |
| $\nu=\Gamma S^2\sigma T$ | comparer §6.3 et §6.4 |

**Tableau des signes — le réflexe de J2, à préparer dès ce soir :**

| Position | $\Delta$ | $\Gamma$ | $\nu$ | $\Theta$ | $\rho$ |
|---|---|---|---|---|---|
| Long call | $+$ | $+$ | $+$ | $-$ | $+$ |
| Long put | $-$ | $+$ | $+$ | $-$ (sauf deep ITM) | $-$ |
| Short call | $-$ | $-$ | $-$ | $+$ | $-$ |
| Short put | $+$ | $-$ | $-$ | $+$ | $+$ |
| **Long straddle** | $\approx0$ | $+$ | $+$ | $-$ | $\approx0$ |

---

# § 7. TD manuscrit — 7 exercices corrigés

**Règle du bloc B :** papier, crayon, calculatrice simple. Tu poses les
formules **avant** les chiffres. Tous les résultats ci‑dessous ont été
recalculés et vérifiés (voir `livrables/j01_bs_closed_form.py`, section
`--td`) : si ton papier tombe dessus à l'arrondi près, c'est validé.

---

### Exercice 1 — Parité, cas de base

> **Énoncé.** Action à $S_0=100$, $q=2$ %, $r=4$ %, $T=6$ mois,
> call $K=100$ coté $6{,}20$. Prix du put ?

$$P=C-S_0e^{-qT}+Ke^{-rT}=6{,}20-100e^{-0.01}+100e^{-0.02}$$
$$S_0e^{-qT}=99{,}0050\quad;\quad Ke^{-rT}=98{,}0199$$
$$P=6{,}20-99{,}0050+98{,}0199=\mathbf{5{,}2149}$$

**Contrôle de bon sens :** $C>P$ parce que $S_0e^{-qT}>Ke^{-rT}$, c'est‑à‑dire
parce que le forward $F_0=100e^{0.01}=101{,}005>K$ : on est **ITM forward**.

---

### Exercice 2 — Forward sur indice

> **Énoncé.** Indice à $3500$, $r=3{,}5$ %, $q=1{,}8$ %, $T=9$ mois.

$$F_0=3500e^{(0.035-0.018)\times0.75}=3500e^{0.01275}=\mathbf{3544{,}91}$$
Base = $+44{,}91$ points (contango technique : $r>q$).

**Variante orale.** Si $q$ passait à $5$ %, $F_0=3500e^{-0.01125}=3460{,}86<S_0$.
**Backwardation sur un indice sans que personne ne soit baissier.**

---

### Exercice 3 — FX, parité couverte

> **Énoncé.** EUR/USD spot $1{,}0850$ ; $r_{USD}=4{,}25$ % ;
> $r_{EUR}=2{,}25$ % ; $T=3$ mois.

$$F=1{,}0850e^{(0.0425-0.0225)\times0.25}=1{,}0850e^{0.005}=\mathbf{1{,}090439}$$
Points de swap $=+54{,}4$ pips. L'EUR est **en report** contre USD, parce que
le taux USD est plus haut : celui qui détient des USD reçoit plus d'intérêts, le
forward le lui reprend. **Aucun avis directionnel là‑dedans.**

> 🎤 *Question piège :* « Le forward EUR/USD est au‑dessus du spot, le marché est
> haussier EUR ? » — **Non.** Le forward est un différentiel de taux. Si tu
> voulais y lire une prévision, tu confondrais carry et anticipation ; c'est
> exactement le sujet du *forward premium puzzle*.

---

### Exercice 4 — Pétrole : storage et convenience yield

> **Énoncé.** Brent spot $68{,}40$ USD/bbl, $r=4$ %,
> coût de stockage $u=1{,}5$ %, convenience yield $y=6$ %, $T=6$ mois.

$$F_0=68{,}40e^{(0.04+0.015-0.06)\times0.5}=68{,}40e^{-0.0025}=\mathbf{68{,}2292}$$
Spread $=-0{,}17$ USD ⇒ **backwardation** : $y>r+u$, tension physique.

*Question inverse (celle qui est posée en entretien) :* le marché cote
$F=69{,}10$. Quel $y$ implicite ?
$$y=r+u-\frac1T\ln\frac{F}{S}=0{,}04+0{,}015-2\ln\frac{69{,}10}{68{,}40}=0{,}0346$$

soit **3,46 %**.
Le convenience yield est passé sous le carry : le marché est repassé en
**contango**, signe de stocks confortables. **C'est un indicateur, pas une
donnée observable :** on ne l'observe jamais, on le déduit de la courbe.

> Lien ShockDesk (à replacer le 11/09) : le régime de courbe conditionne
> l'amplitude du choc. Brent réalisé **+18,4 %** vs **+5 %** prévu, soit
> **×3,68** — *provenance : yfinance, `shock-lab-oil`, 25,5 M USD, 2026‑07‑01 →
> 2026‑08‑29, 42 barres.*

---

### Exercice 5 — Black‑Scholes complet, à la main

> **Énoncé.** $S_0=100$, $K=105$, $r=3$ %, $q=0$, $\sigma=25$ %, $T=6$ mois.

**Étape 1 — $d_1$, $d_2$.**
$$\ln(S/K)=\ln(100/105)=-0{,}048790\quad;\quad
\left(r+\tfrac{\sigma^2}{2}\right)T=(0{,}03+0{,}03125)\times0{,}5=0{,}030625$$
$$\sigma\sqrt T=0{,}25\times0{,}707107=0{,}176777$$
$$d_1=\frac{-0{,}048790+0{,}030625}{0{,}176777}=\mathbf{-0{,}102758}
\qquad d_2=d_1-0{,}176777=\mathbf{-0{,}279534}$$

**Étape 2 — les $N$.** $N(d_1)=0{,}459078$, $N(d_2)=0{,}389917$.

**Étape 3 — les prix.**
$$C=100\times0{,}459078-105e^{-0.015}\times0{,}389917
=45{,}9078-40{,}3318=\mathbf{5{,}5760}$$
$$P=C-S_0+Ke^{-rT}=5{,}5760-100+103{,}4368=\mathbf{9{,}0127}$$
Vérification parité : résidu $\approx-7\times10^{-15}$ ⇒ **numériquement exact**.

**Étape 4 — les grecs (§6), conventions desk.**

| Grec | Formule | Valeur | Lecture |
|---|---|---|---|
| $\Delta$ | $N(d_1)$ | $0{,}4591$ | +1 USD de spot ⇒ +0,46 USD |
| $\Gamma$ | $\phi(d_1)/(S\sigma\sqrt T)$ | $0{,}02245$ | +1 USD ⇒ delta +0,022 |
| $\nu$ (1 pt de vol) | $S\phi(d_1)\sqrt T/100$ | $0{,}2806$ | +1 pt d'IV ⇒ +0,28 USD |
| $\Theta$ (par jour) | $\Theta_{an}/365$ | $-0{,}02254$ | −2,3 cents par jour |
| $\rho$ (1 pt) | $KTe^{-rT}N(d_2)/100$ | $0{,}2017$ | +1 pt de taux ⇒ +0,20 USD |

**Étape 5 — contrôle par le véga.** Repricer à $\sigma=35$ % (+10 pts) :
$C=8{,}3918$, soit $+2{,}8158$. L'estimation linéaire par véga donnait
$10\times0{,}2806=2{,}806$. **Écart de +0,010 : c'est le *volga* (convexité en
vol), positif.** Savoir dire ça vaut cher.

---

### Exercice 6 — Arbitrage sur forward (cash‑and‑carry chiffré)

> **Énoncé.** Reprise de l'exercice 2 ($F^{th}=3544{,}91$).
> Le forward 9 mois cote $3600$. Que fais‑tu, et combien gagnes‑tu ?

Le forward est **cher** ⇒ je le **vends** et je porte le sous‑jacent :

| Opération | $t=0$ | $t=T$ |
|---|---|---|
| Emprunter $3500e^{-qT}=3453{,}07$ | $+3453{,}07$ | $-3453{,}07e^{0.035\times0.75}=-3544{,}91$ |
| Acheter $e^{-qT}=0{,}98659$ indice, div. réinvestis | $-3453{,}07$ | $+1$ indice $=S_T$ |
| Vendre le forward à $3600$ | $0$ | $3600-S_T$ |
| **Total** | $\mathbf 0$ | $\mathbf{+55{,}09}$ points, **certains** |

Valeur actuelle : $55{,}09e^{-0.035\times0.75}=\mathbf{53{,}66}$ points.
Mise nulle, risque nul. **C'est ça, un arbitrage** — et c'est pour ça que ça
n'existe presque jamais : le premier qui le voit le ferme.

> ⚠️ *Ce qui pourrait rendre l'« arbitrage » faux :* dividende estimé faux
> (risque de dividende), coût de repo/borrow réel, marge sur le short, funding
> au‑dessus d'OIS, taxes sur dividendes. **Dis toujours ces cinq mots :** en
> pratique, un arbitrage propre sur listé, c'est un **basis trade**, pas de
> l'argent gratuit.

---

### Exercice 7 — Valeur d'un forward en cours de vie

> **Énoncé.** Contrat long forward 1 an initié quand $S=3500$
> ($r=3{,}5$ %, $q=1{,}8$ %) : $K=3500e^{0.017}=3560{,}01$.
> Six mois plus tard, $S=3650$. Valeur du contrat ?

$$F_{1/2}=3650e^{0.017\times0.5}=3681{,}16$$
$$f=(F_{1/2}-K)e^{-rT}=(3681{,}16-3560{,}01)e^{-0.0175}=\mathbf{+119{,}05}\ \text{points}$$

Le contrat valait $0$ à l'initiation : le P&L latent est bien du **MTM**, et
c'est exactement ce qu'un future aurait déjà appelé en marge, jour par jour.

---

# § 8. Le reste de la journée

## 8.1 Bloc C — Lab ShockDesk (45 min)

Onglet **Options**. Construire, sur le même sous‑jacent et la même maturité :
**long call**, **long put**, **call spread**. Noter dans un tableau papier :
prime, **break‑even**, payoff max/min.

$$\text{BE}_{\text{call}}=K+\text{prime}\qquad
\text{BE}_{\text{put}}=K-\text{prime}\qquad
\text{BE}_{\text{call spread}}=K_1+\text{prime nette}$$

**Consigne stricte du programme : ne pas toucher `iv_shift` aujourd'hui.**
Le choc de vol, c'est J2 (cibles : prime $10{,}69\to23{,}91$, véga
$1{,}242\to1{,}374$, theta $-0{,}344\to-0{,}608$). Aujourd'hui on regarde la
**structure de prime**, pas la sensibilité.

Journal de bord (5 lignes, dans `recherche/journal-de-bord-recherche.md`) :
date · onglet · paramètres exacts · 3 nombres relevés · une phrase de lecture.

## 8.2 Bloc D — Marché (20 min)

Ouvrir une chaîne d'options **SPY**, échéance ~30 jours. Relever :
spot, un strike ITM, l'ATM, un OTM. Pour chacun : prime call, prime put, IV.

**Trois vérifications à faire à la main :**
1. **Parité** : $C-P\approx S-Ke^{-rT}$ (à quelques cents, écart = dividende + bid‑ask).
2. **ATM forward** : le strike où $C\approx P$ est **au‑dessus** du spot si $r>q$.
3. **Skew** : la vol implicite du put OTM est‑elle au‑dessus de celle du call
   OTM ? (Oui sur indice — préparation J4.)

**5 lignes FR + 5 lignes EN** : ce qui a bougé, ta vue, un risque.

## 8.3 Bloc E — Oral WORDS (45 min, debout, chrono)

| # | FR — 90 s | EN — 90 s |
|---|---|---|
| 1 | Pourquoi un call vaut plus cher si la vol monte ? | *Prove put‑call parity by no‑arbitrage.* |
| 2 | Différence forward / future ? | *Why does $\mu$ disappear from the Black‑Scholes price?* |
| 3 | Les 6 hypothèses de Black‑Scholes. | *What is $N(d_2)$? And $N(d_1)$?* |
| 4 | Contango vs backwardation. | *When is early exercise of an American call optimal?* |
| 5 | Que vaut un call ATM forward vs le put ? | *Why is the volatility smile evidence against Black‑Scholes?* |

**Réponse modèle n°1 (à apprendre et à dire en 90 s) :**
« Un call est une option, pas une obligation : mon pire cas est borné à la
prime, mon meilleur cas ne l'est pas. Quand la volatilité monte, la
distribution de $S_T$ s'élargit des deux côtés, mais la partie basse ne me coûte
rien de plus — le payoff est **convexe**. Formellement, le véga
$Se^{-qT}\phi(d_1)\sqrt T$ est strictement positif, pour un call **comme** pour
un put, et par la parité call‑put c'est nécessairement le même véga, puisque la
relation de parité ne contient pas $\sigma$. »

## 8.4 Bloc F — Brainteasers (30 min)

**Heard on The Street × 3** (jours impairs), section *markets / options*. Règle :
un teaser raté est refait **le lendemain avant** les nouveaux.

Trois classiques cohérents avec J1, à traiter ce soir :

1. **Deux options identiques sauf le strike.** Laquelle vaut plus ? *Monotonie
   §3.2 : $C$ décroît en $K$, $P$ croît en $K$. Argument : le call spread a un
   payoff $\ge0$.*
2. **Une option de maturité 2 ans peut‑elle valoir moins qu'une 1 an (même
   strike, européennes) ?** *Oui : avec un gros dividende ou un taux négatif, la
   monotonie temporelle n'est garantie que pour les **américaines** — le
   deep‑ITM put européen long est le contre‑exemple.*
3. **Prix d'un call de strike 0 ?** *$Se^{-qT}$ : c'est l'action portée. Test
   de cohérence des bornes §3.1.*

## 8.5 Bloc G — Python (30 min)

`livrables/j01_bs_closed_form.py` : call, put, parité numérique (écart $<10^{-10}$).
**Fait, et enrichi** : grecs analytiques, corrigé complet du TD, vérification
par différences finies, Monte‑Carlo de contrôle.

```bash
python3 livrables/j01_bs_closed_form.py          # auto-tests
python3 livrables/j01_bs_closed_form.py --td     # corrigé du TD
```

## 8.6 Bloc H — Fit / redites (20 min)

Une question fit (WORDS *Questions‑SG* ou *Why Quant*) : **« Pourquoi les
dérivés actions ? »** — 60 s, structure obligatoire : *un déclencheur concret →
une preuve (ShockDesk) → ce que je veux apprendre sur le desk.* Pas de
généralités.

---

# § 9. Flashcards — les 12 du J1

Recto / verso. À réciter demain matin **avant** d'ouvrir le J2.

| # | Question | Réponse |
|---|---|---|
| 1 | Parité call‑put | $C-P=Se^{-qT}-Ke^{-rT}$, européennes, même $K$, même $T$ |
| 2 | Les 6 hypothèses BS | GBM · $\sigma$ et $r$ constants · pas de frictions · short et funding à $r$ · AOA + trading continu · européenne, $q$ connu |
| 3 | Forward equity / FX / commo | $Se^{(r-q)T}$ / $Se^{(r_d-r_f)T}$ / $Se^{(r+u-y)T}$ |
| 4 | Valeur d'un forward en vie | $f=(F_0-K)e^{-rT}$ |
| 5 | Prix du call | $Se^{-qT}N(d_1)-Ke^{-rT}N(d_2)$ |
| 6 | $d_1$, $d_2$ | $d_1=\frac{\ln(S/K)+(r-q+\frac{\sigma^2}{2})T}{\sigma\sqrt T}$ ; $d_2=d_1-\sigma\sqrt T$ |
| 7 | $N(d_2)$ ? | Probabilité **risque‑neutre** d'exercice ; $N(d_1)$ = delta (hors $e^{-qT}$), **pas** une proba sous $\mathbb Q$ |
| 8 | EDP de BS | $V_t+(r-q)SV_S+\frac12\sigma^2S^2V_{SS}=rV$ |
| 9 | Theta ↔ gamma ($r=0$, $\Delta$‑neutre) | $\Theta=-\frac12\sigma^2S^2\Gamma$ |
| 10 | Call US sans dividende | $=$ call EU, exercice anticipé jamais optimal car $C\ge S-Ke^{-rT}>S-K$ |
| 11 | Call ATM approx | $0{,}4\sigma\sqrt T S$ (⇒ $S{=}100$, $\sigma{=}20$ %, $1$ an ⇒ $\approx 8$) |
| 12 | Pourquoi le smile existe | Les hypothèses H1/H2 sont fausses (sauts, vol stochastique) : BS est un dictionnaire prix↔vol |

---

# § 10. Ticket de sortie J1

Coche uniquement ce que tu as fait **sans regarder** :

- [ ] Je récite les **6 hypothèses** en moins de 30 s.
- [ ] J'écris la **parité** et je la **prouve** par le tableau à 2 états.
- [ ] Je pose les **3 formules de forward** et j'explique le convenience yield.
- [ ] Je dérive **l'EDP** en 5 lignes (Itô → portefeuille → $\mu$ disparaît → AOA).
- [ ] Je calcule $d_1,d_2$ et j'obtiens $C=5{,}58$ sur l'exercice 5.
- [ ] Je dis pourquoi **$N(d_1)\ne$ proba d'exercice**.
- [ ] `livrables/j01_bs_closed_form.py` tourne, tous les tests **OK**.

**Bloc à coller dans le chat pour la reprise :**

```
JOUR : J1  DATE : 05/09  MODE : E / C / F
FAIT : cours[ ] td[ ] lab[ ] oral[ ] brain[ ] py[ ]
TICKET : oui / non — détail :
REDITES :
CHIFFRE DU JOUR (provenance) :
QUESTION POUR LA SESSION :
```

---

## Pont vers J2 (07/09) — grecs 1 et 2

Ce que J1 a déjà posé et que tu réutiliseras **tel quel** demain :
les cinq formules de grecs (§6), le lemme $Se^{-qT}\phi(d_1)=Ke^{-rT}\phi(d_2)$,
la relation $\Theta=-\frac12\sigma^2S^2\Gamma$, le tableau des signes, et
$\nu=\Gamma S^2\sigma T$.

**Le seul piège de J2 à mémoriser dès maintenant :** dans ShockDesk, le champ
de choc d'IV lit des **points**. Un « 10 » = **+10 points de vol**, pas +10 %,
pas +0,10.
