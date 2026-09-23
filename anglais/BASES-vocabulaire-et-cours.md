# Les bases — vocabulaire FO + cours en bref

**À lire à voix haute.** Tout ce qui est en anglais doit être *dit*, pas lu des
yeux. C'est une fiche d'entraînement oral, pas une fiche de révision.

---

# PARTIE 1 — Le vocabulaire

## 1.1 Les 12 mots à connaître avant tout le reste

Si tu ne retiens que ça, tu tiens une conversation.

| FR | EN | ⚠️ |
|---|---|---|
| une obligation | **a bond** | /bɒnd/ — jamais « bonde » |
| le rendement | **the yield** | /jiːld/ — jamais « yeld » |
| le coupon | **the coupon** | /ˈkuːpɒn/ |
| la courbe des taux | **the yield curve** | |
| point de base | **a basis point** | se dit **« a bip »** à l'oral |
| l'échéance | **the maturity** | |
| l'écart | **the spread** | |
| la volatilité | **vol** | on dit *vol*, jamais *volatility* sur un desk |
| une position acheteuse | **long** | *I'm long duration* |
| une position vendeuse | **short** | *I'm short gamma* |
| couvrir | **to hedge** | /hedʒ/ |
| le résultat | **the P&L** | se dit **« the P and L »** |

## 1.2 Parler du marché

| FR | EN |
|---|---|
| la courbe se pentifie | **the curve steepens** |
| la courbe s'aplatit | **the curve flattens** |
| les taux montent / baissent | **yields are up / down** |
| les spreads se resserrent | **spreads are tightening** |
| les spreads s'écartent | **spreads are widening** |
| c'est cher | **it's rich** *(pas « expensive »)* |
| c'est bon marché | **it's cheap** |
| le marché intègre déjà | **the market is pricing in…** |
| une hausse de 25 bp | **a twenty-five basis point hike** |
| une baisse | **a cut** |
| la banque centrale n'a pas bougé | **the central bank held** |
| prise de bénéfices | **profit-taking** |
| dénouer une position | **to unwind a position** |

> 🗣️ **À dire à voix haute maintenant :**
> *"The ECB hiked twenty-five bips this week. The curve flattened, and the
> market is pricing another hike in December."*

## 1.3 Le desk

| FR | EN |
|---|---|
| tenir un marché | **to make a market** / **to quote a two-way price** |
| l'écart achat-vente | **the bid-offer spread** |
| flux clients | **client flow** |
| le carnet d'ordres | **the order book** |
| le livre / portefeuille | **the book** |
| une adjudication | **an auction** |
| pension livrée | **repo** |
| ce titre est recherché | **the bond is trading special** |
| couvrir en delta | **to delta-hedge** |
| être vendeur de gamma | **to be short gamma** |
| la vol implicite | **implied vol** |
| un point de vol | **a vol point** |

## 1.4 Les 8 phrases qui te sauvent

| Situation | À dire |
|---|---|
| Répéter | *"Sorry, could you repeat that?"* |
| Gagner 3 secondes | *"That's a good question — let me think."* |
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

# PARTIE 2 — Le cours en bref

Tout J1 tient en trois idées. Le reste, c'est du détail.

## 2.1 La parité call-put

**L'idée en une phrase :** acheter un call et vendre un put revient exactement à
détenir l'actif à crédit. Donc leurs prix sont liés — pas par une théorie, par
un **arbitrage**.

$$C - P = S_0 e^{-qT} - K e^{-rT}$$

- **C** = prix du call · **P** = prix du put
- **S₀** = prix spot · **K** = strike
- **r** = taux sans risque · **q** = dividende continu · **T** = maturité

Sans dividende : $C - P = S_0 - K e^{-rT}$

> **Pourquoi c'est vrai :** à l'échéance, le portefeuille (call − put) vaut
> toujours $S_T - K$, quoi qu'il arrive. Deux choses qui valent la même chose
> demain valent la même chose aujourd'hui — sinon on encaisse la différence
> sans risque.

**Le repère chiffré** (TD J1) : S=100, K=100, r=4 %, q=2 %, T=0,5, C=6,20
→ **P = 5,2149**

**À dire en anglais :** *"Put-call parity: a long call and a short put replicate
a forward position on the underlying."*

## 2.2 Le forward

**L'idée :** le prix forward n'est **pas** une prévision. C'est le spot corrigé
du coût de portage — ce que ça coûte de détenir l'actif jusqu'à l'échéance.

$$F = S_0 e^{(r-q)T}$$

| Marché | q représente |
|---|---|
| Action / indice | le dividende |
| **FX** | le **taux étranger** : $F = S_0 e^{(r_d - r_f)T}$ |
| Commodité | le rendement de convenance moins le stockage |

**Les repères** (TD J1) :
- Indice : S=3500, r=3,5 %, q=1,8 %, T=0,75 → **F = 3544,91**, base **+44,91**
- FX : EURUSD 1,0850, r_d=4,25 %, r_f=2,25 %, T=0,25 → **F = 1,090439**, soit
  **+54,4 pips**

> **Le réflexe :** si $r > q$, le forward est **au-dessus** du spot (contango).
> Si $q > r$, il est **en-dessous** (backwardation).

**À dire en anglais :** *"The forward is the spot adjusted for cost of carry —
it's not a forecast."*

## 2.3 Black-Scholes

**L'idée fondatrice :** on peut **répliquer** une option en détenant une
quantité d'actif qu'on ajuste en continu. Si la réplication est parfaite,
l'option n'a qu'un seul prix possible — celui du portefeuille qui la copie.

$$C = S_0 e^{-qT} N(d_1) - K e^{-rT} N(d_2)$$

$$d_1 = \frac{\ln(S_0/K) + (r - q + \sigma^2/2)T}{\sigma\sqrt{T}}
\qquad d_2 = d_1 - \sigma\sqrt{T}$$

**Comment lire la formule :**

| Terme | Sens |
|---|---|
| $N(d_2)$ | probabilité (risque-neutre) que l'option finisse dans la monnaie |
| $N(d_1)$ | le **delta** — combien d'actif détenir pour couvrir |
| $Ke^{-rT}$ | ce que tu paieras, actualisé |

**Le repère** (TD J1) : S=100, K=105, r=3 %, q=0, σ=25 %, T=0,5
→ d1 = **−0,102758** · d2 = **−0,279534** · **C = 5,5760** · **P = 9,0127**

### Les 6 hypothèses — à réciter par cœur

1. Mouvement brownien géométrique (rendements log-normaux)
2. **σ constante** et connue
3. **r constant** et connu
4. Pas de coûts de transaction ni de taxes
5. Divisibilité parfaite, vente à découvert autorisée
6. Pas d'arbitrage, option **européenne**

> **Celle qui casse en premier dans la vraie vie : σ constante.** C'est
> précisément l'existence du **smile de volatilité** — et c'est le sujet de J2.
> Si on te pose la question, c'est cette réponse qu'il faut donner.

**L'approximation à connaître** (call ATM, taux nul) :

$$C \approx 0{,}4 \times \sigma\sqrt{T} \times S$$

Vérifié : σ=20 %, T=1, S=100 → approx **8,00** vs vrai prix **7,9656**. Utile
pour un ordre de grandeur de tête en entretien.

## 2.4 Les grecs en une phrase chacun

| Grec | Ce qu'il mesure | En anglais |
|---|---|---|
| **Delta** Δ | sensibilité au **spot** | *"how much the option moves when the underlying moves"* |
| **Gamma** Γ | vitesse de variation du delta | *"how fast my hedge goes stale"* |
| **Vega** | sensibilité à la **vol** | *"my exposure to implied vol"* |
| **Theta** Θ | perte de valeur par jour | *"what I pay to hold the option overnight"* |
| **Rho** ρ | sensibilité au **taux** | *"rate sensitivity — usually the smallest"* |

**Les repères** (Ex5 du TD) : Δ=0,459078 · Γ=0,022449 · vega(1 pt)=0,280609 ·
Θ/jour=−0,022535 · ρ(1 pt)=0,201659

> **La question piège classique — *short gamma* :** tu es vendeur d'options.
> Quand le marché bouge, ton delta évolue **contre toi** : tu es forcé
> d'acheter quand ça monte et de vendre quand ça baisse. Tu **achètes haut,
> tu vends bas**, à chaque ajustement.
> **En anglais :** *"When you're short gamma, you're hedging into the move —
> you buy the highs and sell the lows. You collect theta, but a fast market
> costs you."*
>
> C'est exactement la dynamique que tu as observée sur le crash de mars 2020
> dans ton pricer Excel. **Dis-le, c'est du vécu.**

## 2.5 La relation à retenir

$$\Theta + \tfrac{1}{2}\sigma^2 S^2 \Gamma = 0 \quad \text{(straddle, r = q = 0)}$$

**En clair : le gamma se paie en theta.** Toute la vie d'un desk d'options est
dans cet arbitrage — tu veux de la convexité, tu la paies chaque jour ; tu veux
encaisser du temps, tu prends le risque du mouvement.

Vérifié sur le straddle du TD : Θ = −11,2556, et la somme fait bien **0**.

---

# Le test de 5 minutes

À faire **sans notes**. Réponds **à voix haute, en anglais**.

1. What is put-call parity? Why is it true?
2. Is the forward a forecast of the future spot? Why not?
3. Name three Black-Scholes assumptions. Which one breaks first?
4. What does gamma measure?
5. You're short gamma and the market gaps. What happens?

<details><summary>Les réponses</summary>

1. *A long call plus a short put replicates a forward on the underlying, so
   their prices are linked by arbitrage — otherwise you'd lock in a riskless
   profit.*
2. *No. It's the spot adjusted for cost of carry — funding minus dividends or
   the foreign rate. It's a no-arbitrage price, not a prediction.*
3. *Constant vol, constant rates, no transaction costs, lognormal returns,
   European exercise, no arbitrage. **Constant vol breaks first** — that's
   why the volatility smile exists.*
4. *How fast delta changes when the underlying moves — how quickly my hedge
   goes stale.*
5. *My delta moves against me. I have to buy the highs and sell the lows to
   re-hedge. I collect theta, but a fast market costs me more than I collect.*

</details>

> Si tu réponds aux 5 à voix haute sans bloquer, **tes bases sont là** — et tu
> es au-dessus de la moyenne des étudiants qui seront sur le call mardi.
