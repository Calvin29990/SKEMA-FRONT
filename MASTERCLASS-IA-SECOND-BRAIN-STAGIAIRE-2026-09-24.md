# MASTERCLASS — L'IA, LA DATA ET LE « DEUXIÈME CERVEAU » DU STAGIAIRE

**24/09/2026 — 2h de lecture, from zero.**
**Réponse à la vraie question du cours de ce matin — pas au vocabulaire.**

---

## 0. Ce que j'avais compris de travers (et pourquoi le conseil d'hier reste)

Hier j'ai répondu à la **forme** : « recrutement 2.0 » = phrase de cours, à ne jamais dire dans un entretien (vocabulaire du prof, sonne « tu analyses notre RH »). Ce conseil tient, on le garde — une ligne, point.

Mais j'ai raté la **substance**. Ta question n'était pas « est-ce que cette phrase est risquée ». Ta question était :

> Aujourd'hui il y a des vidéos de robots partout en Chine, des PDG IA, et nous on continue les cours Excel comme au 19ᵉ siècle. **Un stagiaire doit-il faire perdre 1 000 000 € chaque année à une banque pour apprendre — ou peut-il stocker sa data dans son GitHub (ou un outil interne), driver ça avec une IA connectée à Excel, pousser jusqu'à la limite de sa data en accumulant** — jusqu'à ce que **son IA ne donne plus le même résultat que l'IA des autres, et que son GitHub devienne son deuxième cerveau** ?

C'est une question de **stratégie d'apprentissage** et d'**infrastructure de data**. C'est la question d'un stagiaire de 2027, pas d'un étudiant qui cherche une phrase à poser. Cette masterclass y répond point par point.

Les robots à Shenzhen, les PDG IA : c'est la **direction de voyage**, pas encore l'emploi du stagiaire. La question n'est pas « est-ce que l'IA va tout prendre ». La question est : **est-ce que TU auras le corpus.** Dans un an, tous les stagiaires auront l'IA. Les meilleurs auront le corpus. C'est tout le sujet.

**La carte :**
1. Pourquoi « perdre 1 M€ pour apprendre » est le mauvais modèle
2. Le trick Bloomberg de ton collègue = *context engineering* (pourquoi ton IA ≠ l'IA d'un autre)
3. La ligne rouge compliance — la moitié de la réponse
4. La stack concrète : Excel + VBA + Python + Git + LLM
5. Application à ton fichier : LABO, notebooks Christian, question Sommer, story entretien, hook Atos
6. Verdict direct, dans tes mots
7. Les 3 règles qui tiennent sur une carte + le calendrier

---

## 1. « Perdre 1 000 000 € par an pour apprendre » — le mauvais modèle

### 1.1 Le modèle ancien (apprenti, 1990-2015)
Tu fais l'Excel manuel, tu fais des erreurs, le senior est censé les attraper, le coût de l'erreur tombe sur la banque (retravail, report retardé, au pire un deal raté). Tu « apprends » en étant à côté. Trois problèmes structurels :

- **(a) Tu ne vois jamais le prix.** Tu apprends la technique sans le coût de la boulette. C'est pour ça que les juniors restent fragiles des années : ils n'ont pas l'intuition du prix d'une erreur.
- **(b) Le senior transmet SES erreurs.** Ses habitudes Excel, ses raccourcis, ses trucs qui ne marchent que sur SA machine. L'apprentissage par l'observation copie aussi le bruit.
- **(c) Le vrai coût pour la banque n'est pas le 1 M€ du titre, c'est le TEMPS.** Un stagiaire qui fait 3 cycles de retravail coûte 3 semaines de temps senior. Et le temps senior, c'est ce qui coûte vraiment.

### 1.2 Le 1 M€ est un mythe — le vrai coût est ailleurs
Un stagiaire ne price pas de deals et ne gère pas de positions : sa grosse erreur coûte rarement 1 M€ de P&L. Ce qu'elle coûte, c'est :

- du **retravail** (coût réel : temps, pas millions),
- et surtout de la **confiance** — et là c'est binaire. Une fois la confiance cassée, t'es fin.

Le « 1 000 000 € » n'est pas un budget d'apprentissage. **Personne ne paie 1 M€ pour qu'un stagiaire apprenne.** Et le stagiaire qui fait LA grosse erreur ne « profite pas de l'apprentissage » — il est sorti. Le modèle n'existe pas, sauf dans le mythe.

### 1.3 La vraie question (celle à laquelle cette masterclass répond)
Pas « faut-il perdre 1 M€ pour apprendre ». Mais :

> **Comment livrer en semaine 2 ce que le stagiaire Excel manuel livre en mois 3 — sans jamais toucher de donnée PROD avant d'avoir compris la politique ?**

C'est exactement là que tombe le trick Bloomberg de ton collègue.

---

## 2. Le trick Bloomberg = *context engineering* — pourquoi ton IA ≠ l'IA d'un autre

### 2.1 From zero : l'équation
Un LLM = un **a priori généraliste**. Le même modèle, pour tout le monde, le même jour (et de plus en plus, le même modèle à la maison et dans la banque). L'output s'écrit :

```
output = f(modèle, contexte)
```

Même modèle pour tous ⇒ **la différence est dans le contexte.** Deux stagiaires, même modèle, même data de base → **deux outputs différents**, parce que les contextes sont différents. C'est mathématique, pas mystique. C'est pour ça que ton IA ne donnera jamais le même résultat que l'IA d'un autre : c'est **structurel**, pas un hasard.

### 2.2 Les 4 couches du contexte de ton collègue Bloomberg
Ce que son collègue fait — « tu consignes tout et tu donnes à l'IA » — décompose en 4 couches :

| Couche | Contenu | Exemple |
|---|---|---|
| **1. Méthode** | Comment il interroge, ce qu'il consigne | searches, outputs, dates, format de la requête |
| **2. Pratiques internes** | Comment le desk fait | naming, templates, cutoffs, arrondis, qui valide quoi |
| **3. Stratégie** | Ce que le desk travaille, ce qui compte | les deals en cours, les priorités, ce qu'on ne fait PAS |
| **4. Corrections** | Chaque hallucination repérée, avec le pourquoi | « ne dis jamais X, dis Y, parce que Z » |

Les couches 1-3 = « le desk ». La couche 4 = **l'actif compound**. C'est la couche 4 qui fait que dans 6 mois son IA « connaît » le desk mieux qu'un stagiaire de 6 mois.

### 2.3 Le log de corrections = l'actif compound (le cœur du truc)
Chaque correction que tu notes = **un prompt futur qui évitera l'erreur**. Tu ne retraines pas le modèle (tu ne peux pas, et tu n'as pas besoin) : tu **curates le contexte**. C'est la même chose qu'un carnet de bord qui devient, avec le temps, le manuel d'usage.

Le mécanisme, répété parce que c'est le cœur :
1. L'IA dit X.
2. Tu vérifies (data, formule, pratique du desk). C'est faux.
3. Tu notes **une ligne** : date | ce que l'IA a fait | ce qu'il faut faire | pourquoi.
4. La prochaine session, tu ouvres le fichier AVANT de lancer l'IA.
5. L'erreur ne revient plus. L'IA « a appris » sans être touchée.

Cela fait, en un an, des milliers d'heures d'écart avec un stagiaire qui relance le modèle à vide chaque matin. **Le modèle est une commodité. Le corpus est la moat.** C'est la phrase à retenir.

### 2.4 « Pousser jusqu'à la limite de sa data » = cohérence du corpus
La « limite » n'est pas la puissance du modèle. C'est **la cohérence de ton corpus**. Le log d'hallucinations est un **test de régression** : tu reposes la même question, tu vérifies que la correction tient. Si elle ne tient plus, tu rajustes le prompt. C'est ça, pousser la limite : pas « demander plus » à l'IA, mais **maintenir un corpus qui répond de mieux en mieux** aux mêmes questions.

### 2.5 Tu le fais déjà — sur toi
Tes masterclasses, c'est exactement ça : corrections, nuances, « ne dis jamais X », « le plan SG, ne JAMAIS dire "New Horizon" ». Ton repo est déjà un **corpus de toi**. Tu pratiques déjà le context engineering, sur ta propre préparation. Le LABO (section 5.1) fait la même chose pour la partie data/code.

---

## 3. LA LIGNE ROUGE — la moitié de la réponse (compliance)

C'est la moitié de la réponse que personne ne te dira dans le cours Excel. C'est elle qui sépare l'automate utile du problème.

### 3.1 Ce qui peut aller sur un GitHub personnel
- la **méthode** : formules, snippets VBA/Python, structure des pipelines,
- les **prompts** testés,
- le **log de corrections**,
- la **data publique** (cours de Bourse, résultats publiés, statuts légaux),
- la **data SYNTHÉTIQUE** (mêmes structures que du réel : 5 ans de quotes, 100 bonds synthétiques, cashflows fictifs) — et les réponses « attendues » que tu as calculées toi-même.

### 3.2 Ce qui n'y va JAMAIS
- la **data PROD** : clients, positions, transactions, comptes,
- l'**information de marché confidentielle**,
- les **documents de stratégie interne**,
- tout ce qui est **price-sensitive** (MAD),
- tout document marqué **interne / confidentiel**.

### 3.3 Le coût de la traversée
Un GitHub personnel avec de la data PROD, c'est : **data exfiltration → licenciement immédiat** (la carrière est finie en une semaine, pas « apprise »), + risque **secret de fabrique**, + si la data est price-sensitive, **délit d'initié — pénal**. Personne n'a « appris l'IA » en faisant ça. Les fins de carrière qui sont passées par là n'ont pas eu de deuxième chance. Le risque n'est pas « perdre 1 M€ pour la banque » — c'est que **ton** nom soit le risque.

### 3.4 La carte
> **LE DEUXIÈME CERVEAU = LA MÉTHODE, PAS LES DONNÉES.**

À relire avant chaque commit. C'est la seule règle non négociable.

### 3.5 Dans la banque : l'outil interne autorisé = le second domicile
C'est le « autre outil interne » dont tu parlais — il existe. Les grandes banques ont déployé des copilotes IA internes en 2025-2026 (à vérifier en semaine 1 : quel outil est autorisé, quelle est la politique — ce qu'on peut y entrer, ce qui en sort). **Là, et seulement là**, la vraie data rencontre l'IA. Ta semaine 1 de stage a une question prioritaire : « quel est l'outil IA autorisé, et quelle est la politique ? »

### 3.6 L'architecture à deux cerveaux
- **Cerveau public** (GitHub perso) : méthode + prompts + corrections + data synthétique/publique.
- **Cerveau interne** (outil interne autorisé) : data réelle + IA sur la data réelle.
- **Le flux entre les deux = anonymisation / methodisation.** Ce qui sort du cerveau interne vers le cerveau public, ce sont des **méthodes**, jamais des **données**. Une méthode est « on normalise les one-offs avant de calculer le multiple » ; une donnée est « le client X a une position Y ». Tu sais faire la différence, c'est tout l'enjeu.

---

## 4. La stack concrète — et « l'IA connectée à Excel »

### 4.1 Excel est mort, non : le 19ᵉ siècle, c'est la pédagogie
Le desk tourne **encore** sur Excel en 2026 : middle/back office, modèles, recos, tout. La preuve par Christian : un **trader actif** qui te demande des **notebooks VBA** — les vieux de la vieille travaillent en Excel/VBA, point. Ce qui est au 19ᵉ siècle, c'est **l'enseignement** (3h de VLOOKUP manuel au tableau). L'outil est la **langue** du desk. L'IA est l'**accélérateur**. On ne saute pas la langue pour montrer l'accélérateur — c'est ça qui te ferait rater l'entretien.

### 4.2 La stack du stagiaire 2027
```
Excel        → la langue du desk (tu parles, tout le temps)
VBA          → l'automatisation de l'ennui (le vieux, Christian, le desk)
Python/pandas→ le data processing à l'échelle (le neuf, l'exam 07/12)
Git          → le versioning du deuxième cerveau (ton repo, déjà)
LLM          → la génération de code, l'audit, la synthèse
```

### 4.3 « IA connectée à Excel », concrètement
L'IA ne « remplace » pas l'Excel : elle le **génére** et l'**audite**.
- elle écrit le VBA / la formule / le script pandas,
- elle **audit** ta feuille : références absolues/relatives cassées, plages mal bornées, arrondis incohérents, périodes qui ne matchent pas,
- elle explique le défaut et propose la correction.

L'Excel reste l'interface que le desk lit. L'IA est le moteur que le desk ne voit pas — et c'est exactement le positionnement : **le desk voit l'Excel propre, toi tu gardes le moteur.**

### 4.4 « Pousser jusqu'à la limite de sa data » sur ta machine
La méthode, en boucle :
1. Tu construis un **dataset synthétique** (mêmes structures que du réel : 5 ans de quotes quotidiennes, 100 bonds synthétiques, cashflows fictifs) + la **réponse « attendue »** que tu as calculée à la main.
2. Tu fais tourner le pipeline 100 fois.
3. Tu compares à la réponse attendue.
4. Tu logs chaque écart dans `CORRECTIONS.md`.
5. Tu itères jusqu'à **zéro écart**.

C'est comme ça qu'on apprend à perdre 0 € : **toutes les erreurs se font sur de la data qui ne coûte rien.** Le 1 M€ de ta question, il est remplacé par le dataset synthétique : le risque d'apprentissage est déporté en amont, là où il coûte zéro.

### 4.5 `CORRECTIONS.md` — le format (1 ligne par erreur)
```
| date | ce que l'IA a fait | ce qu'il faut faire | pourquoi |
```
Chaque session : **relire le fichier avant** de lancer l'IA. C'est l'actif compound (section 2.3). C'est LE fichier.

### 4.6 `PROMPTS.md` — la bibliothèque de prompts testés
Un prompt sans test sur data synthétique n'entre pas dans le fichier. Chaque prompt : contexte (2-3 lignes) | instruction | format de sortie | date du test + OK/KO. La bibliothèque grandit d'un prompt par session. Dans un semestre, elle vaut plus que le cours.

---

## 5. Application à TON fichier (concret, daté)

### 5.1 Le repo est déjà le deuxième cerveau — il lui manque le LABO
Masterclasses, fiches Christian, deadlines, IB : c'est déjà un corpus. Il manque la partie **code + data**. La structure à créer (elle est créée dans le repo avec cette masterclass) :

```
LABO/
  NOTEBOOKS/       # .ipynb Python + VBA .bas/.xlsm — data SYNTHÉTIQUE uniquement
  SYNTHETIC/       # datasets synthétiques + réponses « attendues » calculées à la main
  PROMPTS.md       # bibliothèque de prompts (chacun testé)
  CORRECTIONS.md   # log d'hallucinations — 1 ligne par erreur (l'actif compound)
```

### 5.2 Les notebooks de Christian = le deuxième cerveau en action
Christian a demandé des notebooks Python/VBA. Tu ne lui envoies pas « un exo » : tu lui envoies **le système** — un notebook sur data synthétique + le `CORRECTIONS.md` qui va avec. C'est le trick Bloomberg en version junior : il est trader, il va reconnaître exactement ce que son collègue Bloomberg fait, en plus jeune. **Ce n'est pas un devoir, c'est une vitrine de méthode.** C'est ton meilleur artifact de réseau de tout le plan.

### 5.3 Les exams S5 = de l'infrastructure de data, pas du 19ᵉ siècle
- **Prérequis Excel** (final, K2) = la langue du desk — à réviser avec l'IA qui audite tes formules.
- **Power BI 11/11** = le « connecté » : c'est la pipeline en UI.
- **Python 07/12** = la stack (pandas = le data processing).
L'école ajoute Python et Power BI **parce que les desks le demandent** — c'est la preuve que le 19ᵉ siècle, c'était le programme, pas l'outil. Tu révises avec la stack (l'IA écrit, teste, logue les corrections) : la règle de l'exam est la règle de l'exam, mais la **méthode de préparation** est la stack.

### 5.4 La question pour Sommer — traduite cette fois (cours du 24/09)
Prof praticien (`-ext`), règle major : « les 3 qui posent des questions sont cités pour les stages ». Ta question, en substance, en deux phrases de praticien :

1. « **Dans un an, avec l'IA, qu'est-ce qui change concrètement dans le quotidien d'un stagiaire de valorisation ? Ce que vous attendez d'un stagiaire en 2027, par rapport à 2017 ?** »
2. « **Vos stagiaires sont-ils autorisés à utiliser l'IA ? Sur quel périmètre, avec quelles limites ?** »

Zéro risque (c'est une question de praticien, pas d'étudiant), et c'est **exactement** la substance de ta question du matin — mais posée comme quelqu'un qui va travailler, pas comme quelqu'un qui assiste. La question 2 vaut de l'or : la réponse te donne **la politique IA du desk avant même d'y être** — c'est l'avance que 99 % des stagiaires n'auront pas.

### 5.5 La story « deuxième cerveau » pour l'entretien (70 % technique)
Trois phrases, une minute, à glisser quand on te demande « qu'est-ce qui te distingue » :

> « Je construis un système de validation : je produis d'abord sur data synthétique, ensuite audit par IA, avec un log de corrections que je relis avant chaque session. Je sépare strictement **méthode et données** : ma bibliothèque de méthode est versionnée chez moi, les données réelles ne restent que sur les outils internes autorisés. Je sais ce que je ne ferai **jamais** : mettre une donnée PROD sur un outil perso — c'est la ligne qui sépare l'automate utile du problème de compliance. »

Technique + **compliance-aware** = exactement ce qu'un desk head veut entendre en 2027. La phrase 3 est ce qui te met dans les 1 % : la plupart des stagiaires « utilisent l'IA » ; très peu peuvent dire **où est leur ligne**.

### 5.6 François Henry (front office) + l'appel Atos = ton hook du 24/11
Si c'est ton **FRANÇOIS de la vague froide du 24/11** (1 message + 1 canal, vague 23→30/11) : sa thèse Atos est **le hook parfait** — un message froid qui montre la méthode sans montrer la data. C'est la ligne, en action.

**L'état du dossier Atos** (pour que tu tiennes la conversation — données publiques) : le titre a déjà « tombé » en prix. Après les levées dilutives (dilution estimée ~99 %), l'action cotait **sous 1 centime** début 2025 ; **regroupement d'actions 1 pour 10 000** pour sortir du statut penny ; plan **Genesis** (~15 000 postes supprimés, 78 000 → 63 000) ; cession de **Advanced Computing** (supercalculateurs) à l'AP pour ~410 M€ ; CA organique **-5,4 %** à ~9,57 Md€. Février 2026 : la direction annonce une liquidité au-dessus du seuil de 650 M€ mais **431 M€ d'impact de restructuration**, et la vue bear du marché vise l'« **effet Foncia** » (fuite des talents → dégradation du delivery).

Donc le 24/11, tu ne demandes pas « est-ce que ça va tomber » — **c'est déjà dans le prix**. Tu demandes la suite :

> « Bonjour M. Henry, j'ai entendu votre thèse sur Atos. Le titre a déjà beaucoup tombé (regroupement 1:10 000, statut penny) — ma question n'est plus là : pour vous, c'est quoi la suite — delisting, redressement, vente à la découpe de MCS — et où est le point d'inflexion ? J'ai passé la semaine à monter un pipeline data + IA sur le sujet (data publique, log de corrections, validation avant PROD). 15 min par téléphone ? »

**Et le projet LABO n°1 tombe tout seul : un tracker Atos sur data publique** (cours, dilution, effectifs, liquidité) — data publique = OK sur GitHub perso. C'est ton premier `SYNTHETIC/` (ici : data réelle publique, même discipline), ton premier notebook, et **le sujet** de ta conversation avec François. Un projet qui sert en même temps le LABO et le réseau — c'est ça, l'accumulateur.

---

## 6. Verdict direct — ta question, tes mots

**Q1 : Un stagiaire doit-il faire perdre 1 000 000 € par an à une banque pour apprendre ?**
→ **Non.** Personne ne paie 1 M€ pour un apprentissage ; le modèle ancien coûtait à la banque du **temps**, et le stagiaire qui fait LA grosse erreur est **sorti**, pas formé. Le risque d'apprentissage se déporte en amont : sur de la **data synthétique**, où il coûte zéro.

**Q2 : Peut-il stocker sa data dans son GitHub (ou un outil interne), driver ça avec une IA connectée à Excel, pousser jusqu'à la limite en accumulant ?**
→ **Oui. C'est exactement le trick Bloomberg, c'est le context engineering, c'est LE différenciateur 2027** — avec 3 règles (section 7). « Pousser jusqu'à la limite » = maintenir un corpus de plus en plus cohérent (log de corrections = test de régression), pas « demander plus » au modèle.

**Q3 : Au final, ton IA ne donne pas le même résultat que l'IA d'un autre ?**
→ **Oui, structurellement.** `output = f(modèle, contexte)`. Même modèle, **corpus différent** (méthode + pratiques + stratégie + corrections) → outputs différents. Le modèle est une commodité ; **le corpus est la moat**. Le jour où tout le monde aura le même modèle (c'est déjà le cas), l'écart se joue **entièrement** dans le corpus.

**Q4 : Est-ce que ça remplace les cours Excel ?**
→ **Non.** Excel est la **langue** du desk en 2026 (Christian, trader actif, demande du VBA — les desks tournent dessus). L'IA est l'**accélérateur**. On ne saute pas la langue pour montrer l'accélérateur : le desk doit voir un **Excel propre**, et toi tu gardes le moteur. Le 19ᵉ siècle, c'était l'enseignement, pas l'outil — et l'école a d'ailleurs déjà ajouté Python (07/12) et Power BI (11/11).

---

## 7. Les 3 règles qui tiennent sur une carte

1. **Méthode sur GitHub perso. Données réelles uniquement sur l'outil interne autorisé.**
   (`LE DEUXIÈME CERVEAU = LA MÉTHODE, PAS LES DONNÉES.`)
2. **1 ligne par correction. Relire le log AVANT chaque session.** (Le log = l'actif compound.)
3. **Zéro écart sur data synthétique avant de toucher de la PROD.** (Le 1 M€ est remplacé par le dataset synthétique.)

---

## 8. Ce que ça change dans ton calendrier (dates)

| Date | Action |
|---|---|
| **24/09 (aujourd'hui)** | `LABO/` créé dans le repo + `CORRECTIONS.md` + `PROMPTS.md` amorcés. Poser la question traduite à Sommer au prochain cours (CVM). |
| **26/09 14h-16h** | Synthèse fiches Christian : déjà générée avec l'IA + log de corrections = première vitrine de méthode. Premier dataset (Atos, data publique) dans `SYNTHETIC/`. |
| **04/10** | Finals prérequis (Excel/Accounting/CFP) — Excel = la langue, réviser avec l'IA qui audite. |
| **11/11** | Power BI — le « connecté », la pipeline en UI. |
| **07/12** | Python — la stack. |
| **24/11** | Vague froide : **hook Atos → François Henry** (brouillon prêt, section 5.6). |
| **Jan 2027** | Tu arrives avec le LABO + la story = pas un « étudiant qui fait de l'Excel », un **automate qui a sa ligne**. |

---

## 9. Une phrase pour finir

Ton collègue Bloomberg a compris avant tout le monde que **la donnée brute ne vaut rien et le contexte se capitalise**. Tu as la même intuition — « ton GitHub devient ton deuxième cerveau » — c'est la bonne. Ce qui te manquait, c'était la **moitié compliance** (méthode ≠ données) et le **support** (le log de corrections + le dataset synthétique). Les deux sont là, dans le repo, dès aujourd'hui. L'IA, tout le monde l'aura dans un an. **Le corpus, c'est toi qui l'accumules — ou tu ne l'auras pas.**
