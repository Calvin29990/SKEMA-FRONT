# ShockDesk — pitch, défense et simulation

**https://shockdesk.onrender.com/** — ton arme, à condition de la manier
correctement.

> ⚠️ **Lis la Partie 3 avant tout le reste.** Il y a trois chiffres sur ton
> propre site qui peuvent se retourner contre toi en entretien. Mieux vaut les
> découvrir ici que devant un trader mardi.

---

# Partie 1 — Ce que ShockDesk prouve vraiment

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

# Partie 2 — Le pitch en anglais (60 secondes)

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

# Partie 3 — 🚨 Les 3 angles d'attaque

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

# Partie 4 — Les 3 questions d'Ali, version ShockDesk

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

# Partie 5 — 🤖 Protocole Gemini *(à copier avec le PDF)*

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

# Partie 6 — Ta semaine

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
