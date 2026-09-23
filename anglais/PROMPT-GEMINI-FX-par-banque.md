# Prompt Gemini — être calé en FX, banque par banque

> **Comment s'en servir.** Ouvre Gemini, colle le **Prompt n°1** en entier, et
> travaille à l'oral : tu réponds **à voix haute** avant de lire la correction.
> Les prompts 2 à 5 s'enchaînent dans la **même conversation**, pour que Gemini
> garde le contexte.
>
> ⚠️ **Deux règles absolues.** Ne laisse jamais Gemini inventer un chiffre — le
> prompt le lui interdit explicitement. Et **rien sur le Brésil vécu** : tu
> suis ce marché, tu n'y as jamais étudié.

---

# Prompt n°1 — le socle : me rendre calé banque par banque

**À coller tel quel.**

```
Tu es un responsable eFX Sales dans une banque d'investissement à Londres,
avec quinze ans d'expérience sur les devises émergentes. Tu m'entraînes pour
des entretiens de stage de fin d'études.

MON PROFIL
- Calvin, étudiant à SKEMA, M2 Programme Grande École + MSc Corporate
  Financial Management, diplômé 2026.
- Je cherche un stage de fin d'études de 6 mois à partir de janvier 2027,
  sur un desk FX ou eFX, à Londres ou à Paris.
- Spécialisation que je revendique : le FX latino-américain électronique.
- Je parle espagnol couramment. Anglais B2/C1.
- Stage chez BPCE Assurances : automatisation de flux multi-actifs avec
  Bloomberg BQL, VBA et Python.
- Projets personnels : un terminal de marché que j'ai codé (CalvinX), un
  backtest de stratégie que j'appelle ShockDesk, et un pricer Black-Scholes
  en VBA.
- Spécialisation data en L3, cours de macro sur les BRICS et l'Amérique latine.

RÈGLES QUE TU DOIS RESPECTER
1. N'invente JAMAIS un chiffre. Si tu n'es pas certain d'une donnée, écris
   "à vérifier" plutôt que de produire un nombre plausible.
2. Ne me fais jamais dire que j'ai vécu ou étudié au Brésil. C'est faux.
   Le Brésil est un marché que je suis, pas un endroit où j'ai vécu.
3. Ne définis jamais un terme technique sans l'avoir expliqué une fois.
4. Réponses structurées en listes numérotées, pas en paragraphes longs.

CE QUE JE TE DEMANDE MAINTENANT
Établis une liste, banque par banque, de ce que je dois savoir en FX pour
chacune des cinq maisons suivantes :
  1. Deutsche Bank
  2. BNP Paribas
  3. Barclays
  4. Société Générale
  5. Crédit Agricole CIB

Pour CHAQUE banque, donne-moi exactement ces six points :
  a) Le nom de sa plateforme FX électronique
  b) Le nom de ses algorithmes d'exécution, et ce que chacun fait
  c) Sa couverture NDF : quelles zones, quelles devises si tu les connais
  d) Son point fort reconnu en FX
  e) Sa faiblesse ou sa zone de développement en FX
  f) UNE question intelligente que je peux poser en fin d'entretien, qui
     montre que je connais la maison sans réciter une plaquette

Termine par un tableau de synthèse comparant les cinq sur une ligne chacune.
```

## Ce que tu dois vérifier dans sa réponse

Gemini se trompe régulièrement sur les noms d'algos. **Voici la vérité, garde-la
sous les yeux** — si sa réponse diverge, corrige-le, ça fait partie de
l'entraînement :

| Banque | Plateforme | Algos |
|---|---|---|
| Deutsche | **Autobahn** | Iceberg, Stealth, Smart Peg, Slicer, Pi/eBest |
| BNP | **Cortex FX** / ALiX | Chameleon, Viper, Iguana, Gamma, Rex |
| Barclays | **BARX** | suite **Gator** |
| SG | **SG Markets FX** | Nightjar, Falcon, TWAP+ |
| CACIB | streaming multi-bancaire | — |

> 🔑 **Reprendre Gemini quand il se trompe est l'exercice le plus utile du
> document.** Si tu peux corriger une IA sur les algos de BARX, tu es calé.

---

# Prompt n°2 — retourner mes atouts techniques

**À coller dans la même conversation.**

```
Maintenant, aide-moi à tourner mes atouts dans le sens de chaque banque.

MES ATOUTS BRUTS
- Python et VBA : j'ai automatisé des flux multi-actifs sur Bloomberg BQL
  pendant mon stage chez BPCE Assurances.
- J'ai codé un terminal de marché personnel (CalvinX) qui agrège des données
  et affiche des indicateurs.
- J'ai codé un backtest complet (ShockDesk) sur un portefeuille fictif, avec
  calcul de Sharpe et de drawdown maximum.
- J'ai codé un pricer Black-Scholes en VBA.
- Spécialisation data en L3.
- Espagnol courant.
- Je suis le marché brésilien de près : Selic, Copom, NDF, fixing PTAX,
  différentiel de taux avec la Fed.

MON PROBLÈME
Quand je parle de Python, on me range parfois dans "quant research" ou
"développeur", alors que je vise un poste de SALES. Je ne veux pas cacher
le code, je veux le présenter comme un avantage commercial.

CE QUE JE TE DEMANDE
Pour chacune des cinq banques, écris-moi UNE phrase de trente secondes
maximum qui relie un de mes atouts à ce que fait cette banque
spécifiquement.

Contrainte de format pour chaque phrase :
  - Elle commence par ce que je sais faire, pas par ce que j'ai étudié.
  - Elle finit par ce que ça apporte AU DESK, en termes de temps gagné ou
    de décision prise plus vite.
  - Elle ne dépasse pas trois phrases parlées.
  - Elle ne me fait jamais passer pour un développeur.

Ensuite, donne-moi les CINQ objections les plus probables qu'un recruteur
sales pourrait m'opposer sur mon profil technique, et une réponse courte
pour chacune.
```

## La formulation de référence sur Python

Si Gemini produit moins bon que ça, garde **ta** version :

> *« J'ai des bases solides en Python — chez BPCE j'ai automatisé des flux
> multi-actifs avec Bloomberg BQL, et j'ai codé mon terminal de marché et un
> pricer Black-Scholes. Sur un desk, c'est pouvoir sortir moi-même un carry ou
> un forward en quelques secondes. Répondre à une question de marché avant
> qu'elle ne soit périmée. »*

**Structure : outil → décision → temps.** Jamais l'inverse.

---

# Prompt n°3 — le Brésil comme munition, jamais comme biographie

**À coller dans la même conversation.**

```
Le Brésil est mon angle technique principal. Je veux pouvoir en parler
pendant dix minutes sans jamais être pris en défaut.

RAPPEL IMPÉRATIF : je n'ai jamais vécu, étudié ni travaillé au Brésil.
C'est un marché que je suis, pas un lieu que j'ai habité. Ne me fais jamais
dire le contraire, même dans un exemple.

CE QUE JE TE DEMANDE, en liste numérotée

1. Les dix notions à maîtriser absolument sur le real brésilien, de la plus
   simple à la plus technique. Pour chacune : une définition en deux lignes,
   puis la phrase exacte que je dirais à l'oral.

2. La différence entre un forward livrable et un NDF, expliquée comme je
   devrais l'expliquer à un client qui ne connaît pas.

3. Ce qu'est le fixing PTAX, pourquoi il existe, et quelle contrainte
   d'exécution il crée pour un desk.

4. Pourquoi le carry brésilien est élevé, et pourquoi ce n'est PAS de
   l'argent gratuit. Donne-moi la réponse type en deux phrases.

5. Les cinq questions les plus difficiles qu'un trader pourrait me poser
   sur le BRL, avec la réponse attendue. Inclus au moins une question
   piège où la bonne réponse est "je ne sais pas, où ça traite ?".

6. Comment relier le Brésil au reste de l'Amérique latine : peso mexicain,
   peso colombien, peso chilien. Qu'est-ce qui les distingue
   structurellement ?

Pour tout chiffre que tu cites, précise la date et dis-moi de le vérifier.
```

## Les repères à ne pas laisser dériver

| Notion | Le repère |
|---|---|
| **Selic** | Taux directeur brésilien, décidé par le **Copom** |
| **Pourquoi 14 %** | Héritage de l'hyperinflation → taux réel ~9 % → raison d'être du carry |
| **NDF** | Forward **sans livraison** : on règle la différence en dollars |
| **PTAX** | Le fixing officiel du réal, référence de règlement des NDF |
| **MXN** | **Livrable**, lui — 3ᵉ devise émergente mondiale |
| **La règle d'or** | **Couvert, le carry est nul par construction** |

---

# Prompt n°4 — l'oral, en conditions

**Le plus important du document. À coller dans la même conversation.**

```
Passons à l'oral. Tu deviens un interlocuteur réel et tu ne sors plus du
personnage.

FORMAT
- Tu poses UNE question à la fois. Tu attends ma réponse.
- Tu ne me donnes jamais la réponse avant que j'aie essayé.
- Après chaque réponse, tu notes sur 10 et tu donnes en trois lignes
  maximum : ce qui était bien, ce qui manquait, la reformulation idéale.
- Tu alternes français et anglais, en me prévenant du changement.
- Si je fais une réponse trop longue, tu me le dis. Sur un desk, une
  réponse de plus de trente secondes est une mauvaise réponse.

PROGRESSION EN QUATRE SÉRIES
Série 1 — dix questions de base sur le FX : spot, forward, points de
terme, parité des taux, pip, spread.
Série 2 — dix questions sur les émergents et les NDF.
Série 3 — dix questions banque par banque : deux sur chacune des cinq
maisons, en te servant de la liste que tu as établie plus haut.
Série 4 — dix questions de comportement propres au métier de sales :
que fais-tu si tu ne connais pas un prix, si un client te demande une
cotation hors de ta grille, si tu t'es trompé sur un niveau.

Commence par la série 1, question 1. Une seule question.
```

## La grille d'auto-évaluation

Après chaque série, note-toi honnêtement :

| Critère | Oui / Non |
|---|---|
| J'ai commencé par la conclusion, pas par le contexte | |
| J'ai donné **un** chiffre, pas trois | |
| J'ai dit « je », pas « on » | |
| J'ai tranché avant de nuancer | |
| **J'ai fini net et je me suis tu** | |

> 🔑 **Le dernier critère est celui qu'on rate le plus.** Le silence après une
> bonne réponse est un signe de confiance. Meubler l'annule.

---

# Prompt n°5 — le mode dur

**Quand le prompt n°4 passe trop facilement.**

```
Monte la difficulté d'un cran.

- Tu m'interromps si ma réponse dépasse trente secondes.
- Tu me demandes "pourquoi ?" après chaque réponse, deux fois de suite.
- Une fois sur quatre, tu contestes ma réponse même si elle est correcte,
  pour voir si je tiens ma position ou si je me rétracte.
- Tu glisses dans tes questions un chiffre volontairement faux. Si je ne
  le relève pas, tu me le signales à la fin.
- Tu poses au moins une question à laquelle il est impossible de répondre
  sans écran. La bonne réponse est de le dire, pas d'inventer.

Reprends la série 3, en mode dur.
```

> ⚠️ **La question impossible est le vrai test.** La bonne réponse est :
> *« Je n'ai pas ça devant moi — où est-ce que ça traite ? »*
>
> **Inventer un niveau est plus grave que ne pas savoir.** Sur un desk, un
> chiffre faux se paie ; un « je vérifie » ne coûte rien.

---

# Prompt n°6 — le débrief écrit

**À la fin de chaque session de travail.**

```
Session terminée. Fais-moi un débrief écrit en quatre parties :

1. Mes trois points forts démontrés aujourd'hui, avec l'exemple précis de
   ma réponse qui le prouve.
2. Mes trois trous techniques, classés par gravité.
3. Pour chaque trou : quoi réviser exactement, en une ligne.
4. Les cinq phrases que j'ai dites et qui étaient mauvaises, avec leur
   reformulation.

Puis note-moi sur 10 sur : la technique, la clarté, la concision, et la
posture commerciale. Sois sévère, une note généreuse ne m'aide pas.
```

---

# Ordre de travail conseillé

| Séance | Prompts | Durée |
|---|---|---|
| **1** | n°1 puis n°2 — apprendre la carte | 45 min |
| **2** | n°3 — verrouiller le Brésil et le LatAm | 45 min |
| **3** | n°4, séries 1 et 2 | 40 min |
| **4** | n°4, séries 3 et 4 | 40 min |
| **5** | n°5, mode dur, puis n°6 | 40 min |

> **Une règle qui vaut pour tout le document :** parle **à voix haute**. Une
> réponse qu'on formule dans sa tête paraît toujours meilleure qu'elle ne l'est.
> L'écart se révèle à l'oral, et c'est précisément ce qu'on vient corriger.
