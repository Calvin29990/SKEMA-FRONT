# Cours d'urgence bilingue — 2 h

**FR / EN en vis-à-vis. Lis la colonne anglaise à voix haute.**

Objectif : tenir une conversation de desk en anglais mardi. Pas devenir
bilingue — **avoir de quoi dire**.

📄 **PDF pour Gemini :** `anglais/COURS-URGENCE-bilingue.pdf` — protocole de
simulation en Partie 5.

---

# Partie 1 — Le socle (20 min)

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

# Partie 2 — Les trois idées du cours (40 min)

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

# Partie 3 — Parler de DB et du marché (20 min)

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

# Partie 4 — Les 3 réponses par cœur (20 min)

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

# Partie 5 — 🤖 PROTOCOLE POUR GEMINI

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

# Le test de 5 minutes — sans notes

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
