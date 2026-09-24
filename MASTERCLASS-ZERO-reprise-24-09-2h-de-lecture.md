# 🎓 MASTERCLASS ZÉRO → REPRISE 24/09 — LECTURE DENSE (≈ 2h)
## Corporate Valuation Methods (jeudi 9h45-13h, Amphi C 301) · Capital Structure & Dividend Policy (jeudi 15h-18h15, Room D 117/118)

**Comment utiliser ce fichier :** tout est expliqué comme si tu débutais. Chaque concept est (re)défini à chaque passage — la répétition est volontaire : c'est elle qui grave. Texte en français, notions et formules en anglais (langue du cours et des examens). Les ✏️ = calculs du cours résolus ligne par ligne. Les 🌐 = pourquoi ça sert en front office (salle de marchés). À la fin : dictionnaire express + auto-check.

---
---

# PARTIE 0 — LE SOCLE ABSOLU
## Ce que SKEMA suppose que tu sais — expliqué ici de zéro

---

## 0.1 Une entreprise = une machine à cash

Oublie le produit, les bureaux, le logo. En finance, une entreprise est une **machine à transformer du capital en cash** :

1. Elle **reçoit du capital** (de ceux qui l'ont financée),
2. Elle **achète des actifs** (machines, usines, stocks — *assets*),
3. Les actifs **produisent des ventes**, dont elle paie ses charges (salaires, fournisseurs, impôts) — *operating cash flow*,
4. Le reste = **cash disponible pour ceux qui l'ont financée**.

**Toute la finance d'entreprise tient sur une seule question :** cette machine produira-t-elle assez de cash pour rémunérer ceux qui l'ont financée, et plus ?

- Si oui → elle **crée de la valeur**.
- Si non → elle **détruit de la valeur** (elle aurait mieux fait de rendre le capital).

Les deux cours d'aujourd'hui sont les deux faces de cette question :
- **Valuation (CVM)** : estimer combien le côté « production » vaut.
- **Capital Structure** : comment le côté « financement » influence la valeur.

---

## 0.2 Les deux grands rôles qui financent l'entreprise : **Debt** vs **Equity**

Il n'existe que DEUX grandes familles de pourvoyeurs de capital. Retiens leurs différences par cœur — tout le reste du semestre en découle :

| | **Debt (dette)** | **Equity (fonds propres / actions)** |
|---|---|---|
| Qui ? | Prêteurs : banques, détenteurs d'obligations (*bondholders*, *lenders*, *creditors*) | Actionnaires (*shareholders*) |
| Contre quoi ? | Reçoit des **intérêts** (*interest*) fixes + remboursement du principal, **contractuellement** | Reçoit ce qui **reste** (dividendes non garantis, plus-value) |
| Priorité | **Payé D'ABORD** — claim prioritaire (*senior claim*) | **Payé EN DERNIER** — claim résiduel (*residual claim*) |
| Droit de vote | Non | Oui |
| Risque porté | Faible (montant contractuel) | Élevé (tout le risque résiduel) |
| Rendement exigé | Plus faible (*rD*, cost of debt) | Plus élevé (*rE*, cost of equity) |

**La forme géométrique la plus importante du cours : le « gâteau » (*pie model*).** Tous les cash flows que la machine produit se répartissent entre ces deux familles. La vraie question du cours de Capital Structure : est-ce que **la façon de découper le gâteau** (plus de dette vs plus d'equity) peut **augmenter la taille du gâteau lui-même** (la valeur totale de la firme) ? Réponse complète à la fin de la Partie 2.

**Exemple concret.** Une boulangerie : tu prêtes 50 000 € (dettes — tu recevras 5% par an, quoiqu'il arrive), ton cousin apporte 50 000 € (equity — il aura le reliquat des profits). Si la boulangerie gagne 20 000 € cette année : tu reçois 2 500 €, ton cousin prend les 17 500 € restants. Si elle ne gagne rien : tu reçois quand même tes 2 500 € (jusqu'à la faillite), ton cousin prend 0. Tu es *moins risqué*, donc tu exiges *moins de rendement*. Ton cousin *plus risqué*, donc il exige *plus de rendement*. **Risque = rendement exigé — c'est la loi n°1 des marchés.**

---

## 0.3 Le temps, c'est de l'argent — actualisation (*present value / discounting*)

**Principe de la valeur temps (*time value of money, TVM*) :** 1 € aujourd'hui vaut plus que 1 € dans un an, parce que l'euro d'aujourd'hui peut être **placé** et produire des intérêts.

- Si le taux du marché est **5%**, 100 € aujourd'hui = 105 € dans un an.
- Donc, **100 € dans un an ne valent que 95,24 € aujourd'hui** (100 ÷ 1,05).

**Actualiser = transformer un cash flow futur en son équivalent d'aujourd'hui :**
```
PV (Present Value) = Cash flow futur ÷ (1 + r)^n
```
où *r* = le taux d'actualisation (discount rate) et *n* = nombre d'années d'attente.

- *r* n'est pas n'importe quel chiffre : c'est le **coût d'opportunité du capital** (le rendement qu'un investisseur aurait obtenu dans un placement de risque comparable — voir 0.4).
- **Valuer une entreprise = actualiser TOUS les cash flows qu'elle produira à l'infini.** C'est le DCF (*Discounted Cash Flow*) — le paragraphe 1.2 ici et la S2 de demain.

**Exemple.** Une machine qui produit 11 000 € nets dans 1 an, risque similaire aux actions moyennes du marché (rendement exigé 10%) → sa valeur aujourd'hui = 11 000 ÷ 1,10 = **10 000 €**. Si un vendeur la propose à 8 500 € → tu achètes (écart +1 500 €). Cet écart entre prix demandé et valeur estimée est EXACTEMENT ce qu'un desk cherche toute la journée (implied valuation gap — Partie 1.1).

---

## 0.4 Coût d'opportunité (*opportunity cost*) — la définition la plus importante du semestre

Le **cost of capital (coût du capital)** d'un investissement = le rendement que l'investisseur aurait pu obtenir **ailleurs, à risque comparable**.

- Tu ne fixes pas toi-même le taux : c'est **le marché** qui le fixe, via tous les autres investissements disponibles.
- Un trader qui te dit « carry 8% » signifie : « le marché exige 8% pour un risque comme le mien ». Si ton projet promet 6% → tu refuses ; 12% → tu acceptes. **Le WACC (Partie 2) est exactement ce seuil.**

**Exemple micro.** Prêter à l'État français (sans risque) rapporte ~3%. Prêter à une PME risquée ? Tu n'accepteras jamais moins de ~10% parce que tu exiges une **prime de risque (risk premium = rendement supplémentaire exigé pour compenser le risque supplémentaire)**.

---

## 0.5 La relation risque-rendement formalisée : **CAPM** et le **beta**

**Total risque d'une action a deux composantes :**
1. **Risque systématique (*systematic / market risk*)** : celui qui frappe TOUTES les entreprises à la fois (taux d'intérêt, récession mondiale, guerra). Impossible à éliminer.
2. **Risque idiosyncratique (*idiosyncratic / firm-specific risk*)** : propre à UNE entreprise (PDG démissionne, usine brûle). Éliminable par la **diversification** (détenir 30 actions différentes).

Le marché **ne paie que** le risque systématique (pourquoi paierait-il un risque que tu peux gratuitement diversifier ?). Le **CAPM (Capital Asset Pricing Model)** dit combien :

```
rE = rF + βE × (rM − rF)
```
- **rF (risk-free rate)** : le rendement du placement sans risque (obligation d'État) — par ex. 3%.
- **(rM − rF) = Market Risk Premium (prime de risque du marché)** : le supplément moyen exigé pour porter le marché tout entier — historiquement ~4-6%.
- **βE (equity beta)** : mesure combien MON action monte et descend AVEC le marché :
  - β = 1 → elle bouge comme le marché (moyenne).
  - β = 2 → quand le marché fait +10%, elle fait +20% (plus risquée).
  - β = 0,5 → moitié moins risquée que le marché.

**Exemple tiré du cours (slide 22 CS, recomposé):** rF = 12%, market premium = 5%, βE = 1,6 → rE = 12 + 1,6×5 = **20%**. « Cost of equity = 20% » = « les actionnaires exigent 20% par an vu le risque qu'ils portent ».

> 🌐 **Utilité front.** Le CAPM est le squelette de toute rémunération de risque sur un desk : carry trade FX (tu exiges une prime pour porter la monnaie risquée), crédit (spread = prime de risque de défaut), equity (alpha = surperformance vs le rendement CAPM attendu).

---

## 0.6 Vocabulaire de machine — les briques qui vont revenir SANS ARRÊT

**Revenu/Sales** : ce que la boîte vend. **Charges/Expenses** : ce qu'elle paie pour vendre.

**D&A (Depreciation & Amortization)** : un coût **comptable mais PAS cash** — la consommation économique d'un actif étalée dans le temps. Tu achètes une machine 100 k€ qui dure 10 ans → la compta déclare une dépréciation de 10 k€/an. **L'argent est sorti à l'Achat (année 0), pas chaque année.** D'où : D&A réduit l'EBIT mais il n'y a aucun cash qui sort l'année même. C'est pour cette raison qu'il est *ajouté de* retour dans le FCFF.

**EBIT (Earnings Before Interest and Taxes)** : le bénéfice **opérationnel** — ventes − charges opérationnelles − D&A, AVANT de déduire les intérêts de la dette et AVANT les impôts. C'est la mesure de performance de la **machine**, indépendante du financement. Traduisez : « ce que l'exploitation a gagné ».

**EBITDA (EBIT + D&A)** : le bénéfice avant intérêts, impôts, D&A. Proche conceptuellement du cash opérationnel **MAIS ATTENTION** : l'EBITDA ignore les impôts à payer, les machines à racheter (CapEx) et le stock de marchandise à financer (NWC) → **c'est un proxy, PAS un cash flow libre.** (Erreur classique citée par le prof, voir 1.13.)

**CapEx (Capital Expenditure)** : le cash réellement dépensé pour acheter/réparer des **actifs longue durée** (machines, usines, serveurs). Sortie de cash pleine et entière, l'année où on paie.

**NWC / BFR (Net Working Capital / Besoin en Fonds de Roulement)** : le cash « bloqué » dans la rotation quotidienne :
```
NWC = Inventory (stocks) + Trade receivables (factures clients non encore payées) − Trade payables (factures fournisseurs pas encore payées)
```
- Vendre à crédit = le client te doit de l'argent = cash bloqué.
- Acheter du stock = cash bloqué.
- Ne pas régler tout de suite tes fournisseurs = cash rendu (ça SOUSTRAIT).
- **ΔNWC (augmentation du BFR) = consommation de cash** : si tu vendais 100 en 5 jours et que cette année tu dois attendre 60 jours pour être payé, la machine a absorbé du cash supplémentaire. En croissance, le BFR monte automatiquement — c'est pour ça qu'une croissance rapide peut a-GOULER du cash.

**One-off / non-recurring items** : des éléments exceptionnels (gain sur vente d'un terrain, coût d'une restructuration, rappel produit). Le problème : le management **étiquette « one-off » tout ce qui l'arrange**. Ton métier de valorisateur : trier le VRAIMENT exceptionnel du « exceptionnel récurrent » (voir 1.5).

**Interest expense** : les intérêts de la dette — **coût de financement, pas coût d'exploitation**. (Comparaison : acheter la matière = exploitation ; payer les intérêts du prêt qui a financé l'usine = financement.) Distinction cruciale pour le chapitre taxes (2.9).

**Corporate income tax (τ)** : l'impôt sur les sociétés — l'État prélève un pourcentage du bénéfice **imposable**. Détail capital : l'État permet de **déduire les intérêts de la dette du bénéfice imposable** → moins d'impôts → c'est ça le **tax shield (bouclier fiscal)** — Partie 2.

**Amortization/shorting/payout…** seront définis le jour où on les utilise. Garde les 9 ci-dessus : ils font 80% du cours.

---

## 0.7 Arbitrage — la loi qui fait tenir tous les modèles

**Arbitrage : acheter quelque chose à un endroit pour le revendre immédiatement plus cher ailleurs, sans risque et sans capital.** Exemple : la même bouteille coûte 3 € au marché d'Evry et 4 € sur internet → tu achètes à Evry et revends en ligne → profit sans risque de 1 €. Sur les marchés réels, ce genre d'écart disparaît en secondes car tout le monde fait pareil.

**Règle de la pensée financière (*no-arbitrage*) :** deux choses qui produisent **exactement les mêmes payoffs** doivent avoir **le même prix**. Si ce n'était pas le cas, quelqu'un s'enrichirait sans risque — et son action même ramènerait les prix en ligne.

> **Tout le cours de Capital Structure utilise cette arme :** si deux entreprises produisent les mêmes cash flows opérationnels, elles ont la même valeur totale, PEU IMPORTE comment elles splitent dette et equity. C'est la DÉMONSTRATION de Modigliani-Miller (Partie 2).

---
---

# PARTIE 1 — CORPORATE VALUATION METHODS (Sommer, S1) expliquée de zéro
### Sujet : *Valuation Foundations & Preparing for Valuation* — « des états financiers publiés vers des cash flows vraiment utiles pour la valorisation »

Le problème que la S1 traque : les comptes publiés racontent le **passé**, rempli de bruit comptable (one-offs, mauvaises catégories, conventions). Le valorisateur doit d'abord **nettoyer et ré-organiser** ces chiffres pour dégager les **cash flows opérationnels futurs** — seule matière première valable de la valorisation.

## 1.1 Prix ≠ Valeur : les trois grandeurs à JAMAIS confondre

| Terme | Définition | Qui le donne ? |
|---|---|---|
| **Market price (prix de marché)** | Ce à quoi le titre s'échange aujourd'hui à la bourse. Observable, immédiat | Le marché |
| **Estimated intrinsic value (valeur intrinsèque estimée)** | Ton estimation fondée sur les cash flows futurs + risque + hypothèses | Toi l'analyste |
| **Transaction value** | Ce qu'un acheteur PRECIS paierait (contrôle, synergies, capacité de financement) | Le deal à l'origine |

**Pourquoi le prix peut diverger de la valeur ?** Agrégation des croyances de millions d'agents + humeurs + contraintes de vente/achat ≠ nécessairement la meilleure estimation rationnelle fondée sur les cash flows. C'est LÀ que s'insère le métier : le desk parie sur la **convergence** prix → valeur.

**La formulation à retenir par cœur :** « Valuation is a defensible estimate — not the discovery of one hidden exact number » → la valorisation n'est pas la recherche du chiffre magique : c'est l'art de défendre tes hypothèses.

**✏️ L'exemple pivot (slide 4) :** prix observé 50 €/action ; ton estimation 62 €/action → **implied valuation gap = +24%** ((62−50)/50). C'est-à-dire : le marché sous-price cette boîte de 24% SELON TES hypothèses. Défendre cette estimation = ton cas d'école du semestre (une entreprise cotée que tu choisis toi-même — cap>1 Md$, FCF yield >3%, non émergents, 5 ans de data).

## 1.2 La chaîne de valorisation entière — chaque maillon expliqué

```
Reported Financials → Normalize → Forecast → FCFF
FCFF → WACC → Enterprise Value
Enterprise Value → Equity Value → Value per Share
→ Compare to market price → Implied Gap
```

| Maillon | Ce que tu fais | Détail |
|---|---|---|
| **Reported Financials** | Récupérer compte de résultat, bilan, cash flow (publics) | Le tel quel |
| **Normalize** | Enlèver le bruit comptable → « sustainable earnings » | Voir 1.5 |
| **Forecast** | Projeter les operations futures (croissance, marges) | C'est la **S2 de demain** |
| **FCFF** | Convertir en cash réel disponible | Voir 1.11 |
| **WACC** | Choisir le taux d'actualisation juste | Cours de Capital Structure, Partie 2 |
| **Enterprise Value (EV)** | Actualiser les FCFF au WACC = valeur de TOUTE la machine opérationnelle | Voir 1.4 |
| **Equity Value** | L'EV MOINS ce qui est dû aux créanciers | Voir 1.4 |
| **Value per Share** | ÷ nombre d'actions |  |
| **Implied Gap** | Comparer valeur vs prix de bourse | 1.1 |

## 1.3 Le paysage des méthodes — les 4 familles

- **Intrinsic** : tu projetes les vrais cash flows → tu actualises. Sous-familles : **DDM** (dividendes actualisés, pour les boîtes stables qui versent tout), **FCFE**, **FCFF** (les deux du cours).
- **Relative (trading multiples)** : tu compares à des boîtes similaires cotées (« elle traite à 12× ses bénéfices, les comparables à 15× → décote »). Rapide, mais hérite de toutes les erreurs du marché.
- **Transaction & LBO** : prix payés lors d'acquisitions passées + structure rentabilité du repreneur financier (LBO) → utile pour M&A/desk origination.
- **Asset-based** : **NAV** (Net Asset Value — valeur des actifs moins dettes) ou **liquidation** (combien récupère-t-on si on ferme tout) → plancher de valeur, pour boîtes en détresse ou holdings d'actifs.

**Aucune méthode n'est supérieure — chaque usage son outil :** trader FICC → intrinsic/hurdle rates ; desk M&A → transaction & multiples ; crédit distressed → asset-based.

## 1.4 ⭐ Le concept central : **Enterprise Value (EV)** vs **Equity Value**

**Enterprise Value (EV)** = la valeur de la machine OPÉRATIONNELLE elle-même (tous les actifs qui fabriquent les produits), **INDÉPENDAMMENT** de la manière dont elle est financée. C'est le prix que paierait l'acheteur qui reprend TOUT l'outil productif, à condition d'hériter aussi des dettes.

**Equity Value** = ce qui reste aux actionnaires une fois les créanciers payés.

**La formule la plus importante de l'unité : le pont EV→Equity :**
```
Equity Value = Enterprise Value − Debt + Cash (excédentaire) + Actifs non-opérationnels
```
**Pourquoi −Debt ?** Parce que les prêteurs ont un claim contractuel prioritaire sur les cash flows. Aucun cash disponible aux shareholders avant que les intérêts et le principal soient servis.

**Pourquoi +Cash (excédentaire) ?** Tout cash qui n'est PAS nécessaire à la machine de tous les jours (par ex. : montants placés en excès, « sleeping cash ») appartient DEJA aux shareholders — il ne venait pas de l'exploitation, le modèle EV (qui ne valorise QUE les cash flows opérationnels futurs) ne l'a pas compté. Il faut le rajouter.

**Pourquoi +Actifs non-opérationnels ?** Même logique : une participation minoritaire dans une boîte sans rapport avec le cœur de métier produit un cash que le modèle FCFF n'avait pas prévu — il faut l'ajouter au pont.

**Le path incontournable à ne JAMAIS mélanger (*framework error*, dire le slide) :**
| Chemin | Cash flow | Taux | Valeur obtenue |
|---|---|---|---|
| Route du haut | **FCFF** (cash pour TOUS les apporteurs) | **WACC** | **Enterprise Value** |
| Route du bas | **FCFE** (cash résiduel aux actionnaires) | **Cost of Equity** | **Equity Value** |

> ❌ Actualiser le FCFF au cost of equity = casser le pont : tu prends un cash destiné aux créanciers+actionnaires et tu l'appelles « valeur actionnaire » sous le taux appartenant uniquement aux actionnaires. Toute la Section 1.13 repose sur cette cohérence.

**✏️ Aster SA (slide 8) — résolution détaillée :**
- Operating business value (EV) = 1 250 · Interest-bearing debt = 310 · Cash = 85 · Non-operating investments = 25 · Shares = 40 M
- **Equity = 1 250 − 310 + 85 + 25 = 1 040 M€** (réaction : on retire le claim des prêteurs (310), on remet le cash excédentaire (85) et les placements hors métier (25), vu que ni l'un ni les autres ne rentraient dans l'FCFF utilisé pour aboutis a l'EV).
- **Value per share = 1 040 ÷ 40 = 26 €/action.**
- Question « si on a actualisé du FCFF, quelle valeur avait-on avant ce pont ? » → l'**Enterprise Value**. (Refait à l'envers : si t'avais actualisé du FCFE au cost of equity, tu aurais eu l'Equity Value directement, sans pont.)

**✏️ Northstar Components (Ex 1 du pack) — le même entraînement en dur :**
- EV operating = 1 480 · bank debt = 360 · cash total = 125 dont 45 requis pour l'exploitation → **excess cash = 125 − 45 = 80** ← le calcul « excess » : seule la partie excédentaire revient aux actionnaires ; les 45 servent de réserve de marche quotidienne, ils restent dans la machine.
- Listed equity investment = 38, sans rapport avec les opérations → **à ajouter** (hors FCFF).
- **Equity = 1 480 − 360 + 80 + 38 = 1 238 M€ → 1 238 ÷ 50 M = 24,76 €/action.**
- Questions de rédaction : on soustrait la dette car priorité ; on ajoute l'excess cash car deja disponible et hors exploitation ; l'investissement coté est traité à part car hors cœur de métier / pas compté dans le FCFF.

## 1.5 Normalisation — trier le « exceptionnel » du « exceptionnel récurrent »

Le raisonnement du prof : **Reported Earnings ≠ Sustainable Earnings** — le bénéfice du rapport annuel n'est pas le bénéfice que la boîte reproduira chaque année en moyenne. Avant de projeter, il faut le nettoyer. La règle de décision :

| Item | Traitement | Critère |
|---|---|---|
| Hors exploitation (vente d'un terrain excédentaire) | **REMOVE** | Pas dans l'outil productif |
| Vraiment exceptionnel ET non récurrent (1er cyber-incident) | **ADJUST** (ajouter au EBIT) | Ça ne se reproduira pas |
| Récurrent en fait, même étiqueté « one-off » (restructuration 4 ans d'affilée) | **RETAIN** (conserver dans l'EBIT) | Récurrence économique |
| Mal rangé opérationnel/financement | **RECLASSIFY** | Mauvais bucket |

> **Question magique à te poser pour chaque item :** « dans 3 ans, cette dépense sera-t-elle toujours régulièrement annuellement présente ? » Si oui → RETAIN. L'étiquette du management est un argument, pas une preuve.

**✏️ Exemple (slide 12) :** EBIT rapporté 420 · restructuration 35 (one-off) · gain sur cession de hangar 20 · frais de litige annuels récurrents 8 · cyber incident 12.
- **EBIT normalisé = 420 + 35 − 20 + 12 = 447** (le litige de 8 reste dedans : il RECUR chaque année (frais d'avocats de routine), même présenté comme « exceptionnel »).

**✏️ Helios (Ex 2 du pack) — le test de récurrence élargi item par item :**
| Item | Traitement | Justification |
|---|---|---|
| Restructuring 42 (€28m, €35m, €31m les 3 années passées !) | **RETAIN** | C'est un coût chronique — quasi-annuel → récurrent |
| Gain sur vente de terrain 18 | **REMOVE** (−18) | Hors exploitation, gain ponctuel |
| Cyber 14, premier incident | **ADJUST** (+14) | Non récurrent à ce jour |
| Coûts d'intégration d'acquisition 22 — l'acquisition EST la stratégie déclarée | **RETAIN** | Elle reviendra avec les prochaines acquisitions |
| CEO retention award 9 (3-ans, année 1) | **RETAIN** | Dépense réelle sur 3 années consécutives |
| Product recall 16, aucun depuis 5 ans | **ADJUST** (+16) | Statistiquement non récurrent à ce jour |
- **EBIT normalisé défendable = 510 − 18 + 14 + 16 = 522 M€**
- Réponse « pourquoi pas l'étiquette management ? » : le management vend un narrative — seule l'histoire pluriannuelle fait preuve de récurrence.
- Les 3 infos que tu demanderais avant de finaliser : l'historique complet (10 ans) de chaque item · les notes annexes comptables · les opinions d'auditeurs / guidance sur le caractère “récurrent”.

## 1.6 NOPAT — le bénéfice opérationnel APRÈS impôts opérationnels

```
NOPAT = Normalized EBIT × (1 − Operating tax rate)
```
**Pourquoi fais-t-on ×(1−t) ?** L'État prend une part des profits opérationnels (ex : 25%) — tout simplement. Le NOPAT isole l'économie de l'EXPLOITATION, AVANT de regarder comment elle est financée :

- **On part de l'EBIT** (avant intérêts) → donc on **exclut délibérément** la charge des intérêts. Pourquoi ? Parce que les intérêts sont un coût de FINANCEMENT. Si on les comptait ici, puis qu'on reprenait encore le coût de la dette dans le WACC (Partie 2), on **compterait la dette deux fois**. Le NOPAT est propre : « combien l'exploitation gagne si la boîte n'avait AUCUNE dette ».
- **On utilise l'EBIT NORMALISÉ** quand le rapporté est déformé (one-offs).

**✏️ Exemple :** EBIT 300 × (1−25%) = **NOPAT 225**.

## 1.7 Invested Capital — combien de cash est « embouteillé » dans la machine ?

**Deux façons de le mesurer, mêmes résultats :**
```
Approche opérationnelle :  Invested Capital = Operating Assets − Operating Liabilities
Approche financement   :  ≈ Debt + Equity − Non-operating Assets
```

- **Inclus** : machines, stocks, créances clients (tous les actifs nécessaires à PRODUIRE).
- **Soustrait** : dettes fournisseurs et charges à payer (passif opérationnel non rémunéré — ce sont des « prêts gratuits » que le business s'accorde lui-même).
- **Exclu** : excess cash, placements financiers, participations hors métier (non liés à la production).

**La règle d'hygiène absolue :** le NOPAT (numérateur du ROIC) et le capital investi (dénominateur) doivent être **économiquement cohérents** — si l'excès de cash n'aide pas à produire le NOPAT, il n'appartient pas à l'IC. Inclure 250 M€ de cash dormant dans l'IC → tu gonfles artificiellement le dénominateur → ROIC s'effondre sans raison → **tu juges l'exploitation mal alors qu'elle est saine**. C'est EXACTEMENT le piège de l'Ex 3.

**✏️ Orion (Ex 3) :** NOPAT = 240×75% = **180** · IC = (300 stocks + 260 créances + 1 540 PPE) − (220 dettes fournisseurs + 180 charges à payer) = 2 100 − 400 = **1 700** · ROIC = 180/1 700 = **10,6%**. L'excess cash (250), les marketable securities (90) et l'interest-bearing debt (700) sont EXCLUS — l'un n'est pas productif, l'autre relève du financement.

## 1.8 ROIC — le test définitif de création de valeur

```
ROIC = NOPAT ÷ Invested Capital
```
Traduction directe : « pour 1 € bloqué dans la machine, combien de centimes nets l'exploitation génère-t-elle par an ? »

**La comparaison qui décide de tout — ROIC vs WACC :**
| Situation | Lecture | En desk term |
|---|---|---|
| ROIC > WACC | La machine gagne + que le coût des capitaux → création valeur | Long — quality |
| ROIC ≈ WACC | Ni gain, ni perte de valeur — croissance stérile | Sans conviction |
| ROIC < WACC | La machine coûte + cher qu'elle ne rapporte → destruction | Short/désinvestir |

> 🌐 **Utilité front.** Le spread ROIC−WACC est littéralement le thermomètre du value desk et de tout equity research buyer-side : filtre les longs (spread positif persistant) et les shorts (spread négatif). Le critère **FCF yield > 3%** que ton prof exige pour l'entreprise choisie au semestre est le même réflexe : on rejette les machines qui ne produisent pas un cash libre minimum.

## 1.9 ⭐ La croissance n'est pas gratuite : *Growth = Reinvestment rate × ROIC*

**Un fait économique profond :** pour faire croître une machine, il faut le réinvestir dedans (nouvelles machines, plus de stocks). Le lien est exact :

```
Growth (croissance opérationnelle) ≈ Reinvestment rate × ROIC
⟹ Reinvestment rate = Growth target ÷ ROIC
```
- **Reinvestment rate** = fraction du NOPAT remise dans la machine (%).
- Plus le **ROIC est élevé**, plus chaque € réinvesti rapporte → moins tu dois réinvestir pour la même croissance.

**✏️ Slide 19 — deux entreprises, même NOPAT (200), même croissance visée (6%) :**
| | ROIC | rr = 6%/ROIC | Reinvestment | FCFF |
|---|---|---|---|---|
| HighROIC | 15% | 40% | 80 | **120** |
| LowROIC | 8% | 75% | 150 | **50** |

**Lecture économique qui vaut des points d'interview :** la croissance identique de 6% coûte 150 de cash à la boîte médiocre et seulement 80 à la bonne → la mauvaise qui veut croître s'appauvrit. Moralité desk : on n'achète pas « la croissance », on achète « la croissance **rentable** ».

**✏️ Ex 4 (Atlas/Beacon/Cedar, croissance 7%, WACC 8%) — le calcul complet :**
| | ROIC | rr = 7%/ROIC | Reinvestment | FCFF | Verdict |
|---|---|---|---|---|---|
| Atlas | 20% | 35% | 87,5 | **+162,5** | Crée (ROIC 20 > 8) |
| Beacon | 10% | 70% | 175 | **+75** | Peu de valeur, croissance presque stérile |
| Cedar | 6% | 116,7% | 291,7 | **−41,7** | **Détruit** (ROIC 6 < 8) |

**Le paradoxe Cedar expliqué doucement :** Cedar affiche des bénéfices comptables en hausse (croissance atteinte ✓), mais pour obtenir +7% elle doit injecter 291,7 de cash dans une machine qui ne rend que 6% alors que les capitaux lui coûtent 8% → chaque € investi coûte 0,08 € et rapporte 0,06 € → **plus elle croît, plus elle détruit**. Le FCFF négatif montre que les actionnaires doivent même RAJOUTER du cash pour financer cette « croissance ». Cedar est le short-seller case textbook.

## 1.10 De quoi se compose le Reinvestment ?

```
Reinvestment = Net CapEx + Δ Operating NWC
```
- **Net CapEx = CapEx − D&A** : le cash dépensé en actifs neufs, corrigé de la consommation comptable (la machine « usée » cette année, D&A, n'est pas une sortie de cash — mais elle réduit le parc productif, d'où la convention Net).
- **+ ΔNWC** : le cash supplémentaire coincé dans la rotation quotidienne (stocks, créances).

## 1.11 ⭐ FCFF — le cash réellement disponible pour TOUS ceux qui ont financé

**Deux formes équivalentes :**
```
FCFF = NOPAT − Reinvestment                             (forme économique)
FCFF = NOPAT + D&A − CapEx − Δ Operating NWC            (forme comptable complète)
```
**Pourquoi on ajoute D&A et retire CapEx ?** Le NOPAT est un chiffre COMPTABLE (déjà diminué de la D&A qui n'a coûté aucun cash cette année) → on rajoute D&A pour rétablir le cash ; puis on enlève le CapEx, qui lui est bien une VRAIE sortie de cash. Enfin on enlève l'augmentation du BFR (cash piégé). Il reste : **cash réellement libre, distribuable indifféremment à prêteurs et actionnaires.**

**✏️ Slide 22 (from EBIT to FCFF) :** EBIT 260, t 24%, D&A 45, CapEx 70, ΔNWC 18 → NOPAT = 260×76% = 197,6 → Reinvestment = (70−45)+18 = 43 → **FCFF = 197,6 − 43 = 154,6**.

**✏️ Ex 5 Lumen :** NOPAT = 330×75% = 247,5 · Net CapEx = 82−55 = 27 · Reinvestment = 27+24 = 51 → **FCFF = 247,5 − 51 = 196,5** (vérif : 247,5+55−82−24 = 196,5 ✓) · rr = 51/247,5 = **20,6%**.

> ❌ Rappel slide 22 : **EBITDA n'est PAS le FCFF** — l'EBITDA oublie les impôts, le remplacement des machines (CapEx) et le BFR → c'est un proxy optimiste. Sur un desk, dire « cette boîte affiche 300 d'EBITDA mais son FCFF est à peine 80 » est un argument de trade.

## 1.12 FCFE — l'autre route, réservée aux actionnaires

```
FCFE = Net Income + D&A − CapEx − ΔNWC + Net borrowing
```
- On part du **Net Income** (bénéfice net, c-à-d APRÈS intérêts et impôts — vue actionnaires).
- **Net borrowing** = nouvelles dettes émises − dettes remboursées : emprunter = cash supplémentaire DISPONIBLE pour les actionnaires ; rembourser = cash consommé pour eux.
- **FCFE → Cost of Equity → Equity Value.** Bon quand l'endettement est stable (sinon les flows de dette rendent la projection acrobatique — d'où la préférence des desks pour le FCFF quand la structure peut changer).

## 1.13 Les 8 erreurs classiques (revérifiées une par une)

1. Mélanger EV et equity value (confondre les deux routes du matching — 1.4)
2. Utiliser le profit rapporté sans fouiller les one-offs (1.5)
3. Glisser des items de financement dans le profit opérationnel (l'intérêt n'est PAS un coût d'exploitation — 1.6)
4. NOPAT et invested capital incohérents (ex : ajouter l'excess cash à l'IC — 1.7)
5. Innoventer une croissance sans reinvestment (1.9)
6. Confondre EBITDA et FCFF (1.11)
7. Actualiser du FCFF au cost of equity (1.4)
8. Automatiquement rajouter tout ce qui porte l'étiquette « one-off » (1.5)

> **Vérité du slide 28 : les erreurs graves de valorisation sont des erreurs de COHÉRENCE avant d'être des erreurs de calcul.** Sur un cas d'entretien, on te pardonne une faute d'arrondi ; on ne te pardonne pas d'avoir actualisé le FCFF au mauvais taux.

## 1.14 ⭐ La répétition générale intégrée — Ex 6 Nova Health (le full rehearsal)

**Données :** EBIT rapporté 620 · restructuration 36 (charges dans 3 des 4 dernières années) · gain vente siège 25 · cyber 18 (premier) · t 26% · D&A 80 · CapEx 92 · ΔNWC 28 · IC début 3 100 · cash 310 (dont 110 requis) · debt 1 050.

| Étapes | Calcul commenté |
|---|---|
| 1. Normalisation | Restructuration **3 ans sur 4 → récurrente → RETAIN** (pas de +36 !) · gain siège hors exploitation → REMOVE (−25) · premier cyber → ADJUST (+18) → **EBIT normalisé = 620 − 25 + 18 = 613** |
| 2. NOPAT | 613 × (1 − 0,26) = 613 × 0,74 = **453,6** |
| 3. Reinvestment | (92 − 80) + 28 = **40** |
| 4. FCFF | 453,6 − 40 = **413,6** |
| 5. ROIC | 453,6 / 3 100 = **14,6%** — sain (vs WACC typique ~8%) |
| 6. Reinvestment rate / croissance | rr = 40/453,6 = **8,8%** → g ≈ 8,8% × 14,6% = **1,3%** — croissance organique faible (mature) |
| 7. Excess cash | 310 − 110 = **200** → pour le futur pont EV→equity |
| 8. Taux correct | **WACC** (car FCFF) |
| 9. Ce qu'il reste à prévoir pour un DCF complet | La croissance soutenable, l'horizon de prévision, les reinvestissements futurs, la terminal value, le WACC précis → **c'est la S2** |

---
---

# PARTIE 2 — CAPITAL STRUCTURE & DIVIDEND POLICY (Pilkington, S1) expliquée de zéro
### Sujet : *Cost of Capital and Firm Value* — « est-ce que le mix dette/equity peut changer la valeur de la firme ? »

## 2.1 On repose les définitions

**Capital structure** = la proportion de dette (debt) et d'equity (actions) utilisée pour financer la machine. Exemple : 7 dettes pour 3 actions → D/E = 7/3 ≈ 2,33 (ou D/V = 70%).

**Cost of capital** (rappel 0.4) = coût d'opportunité d'investir dans le portefeuille COMBINÉ des titres de la firme = rendement que les investisseurs exigent parce qu'ils pourraient placer leur argent ailleurs, à risque identique.

**WACC (Weighted Average Cost of Capital)** = la moyenne pondérée du coût de la dette et du coût de l'equity, les poids étant leur part respective dans la structure :
```
WACC = (D/V) × rD × (1 − τ) + (E/V) × rE            [version après impôts]
WACC = (D/V) × rD + (E/V) × rE                     [version sans impôts]
```
- **D/V et E/V** = part de la dette et de l'equity dans le total (D/V + E/V = 1).
- **rD** = coût de la dette (le taux d'intérêt payé aux prêteurs).
- **(1−τ)** = correction fiscale (tax shield — voir 2.9).
- **rE** = coût de l'equity (CAPM — voir 0.5).

**Le WACC est à la fois le « coût » (pour la firme) et le « taux exigé » (pour les investisseurs) — les deux faces de la même pièce.** C'est LE chiffre vers lequel convergent les deux cours : CVM l'utilise pour actualiser le FCFF → EV ; Capital Structure se demande : peut-on le modifier en jouant sur D/V ?

## 2.2 Les 3 questions organisatrices (telles que le prof les a posées)

1. **Firm value** : changer D/E peut-il augmenter la V (valeur de la firme) ?
2. **Cost of capital** : changer D/E peut-il baisser le WACC ?
3. **Optimal** : si oui, sous quelles conditions — et c'est quoi « optimal » ?

*Méthode du cours : commencer par un monde simplifié (marchés parfaits), puis ajouter la réalité une couche à la fois (impôts → distress). Chaque couche change la réponse. C'est la structure Cases I → II → III.*

## 2.3 Case I — le monde des marchés parfaits (les 3 hypothèses et pourquoi on les fait)

- **No transaction costs** — on peut acheter/vendre/shorteur gratuitement.
- **No income taxes** — le financement ne change pas les impôts.
- **No bankruptcy costs** — la détresse financière ne détruit rien de valeur.

Ces hypothèses sont fausses — **but propos intentional** : éliminer tout bruit pour isoler l'effet PUR de la structure (comme le physicien qui fait la chute « dans le vide » d'abord). On remettra la réalité ensuite, couche par couche.

**Dans ce monde, la valeur de la firme : `V = D + E`** (la somme des prix de la dette et de l'equity).

## 2.4 L'expérience U vs L — la démonstration simple (à savoir refaire)

**Setup :** une activité qui rapporte 6 000 dans le très bon scénario et 4 000 dans le mauvais (50/50 → espérance = 5 000). Deux entreprises, même machine opérationnelle :
- **U (Unlevered)** : pas de dette, tout en equity.
- **L (Levered)** : 2 000 de dette au taux sans risque 10% → remboursement dû = 2 000 × 1,10 = 2 200.

**Les payoffs, scénario par scénario :**

| État du monde | U : equity reçoit | L : la dette reçoit (d'abord !) | L : l'equity reçoit (résidu) |
|---|---|---|---|
| Fort (50%) : 6 000 | 6 000 | 2 200 | 6 000 − 2 200 = 3 800 |
| Faible (50%) : 4 000 | 4 000 | 2 200 | 4 000 − 2 200 = 1 800 |
| **Espérance** | **5 000** | **2 200** | (3 800+1 800)/2 = **2 800** |

**L'addition qui change tout :** pour L, le TOTAL reçu par les financiers = 2 200 (debt) + 2 800 (equity) = **5 000 — EXACTEMENT comme U.**

**Conclusions (lire lentement) :**
1. Le gâteau total (5 000) n'a pas changé parce qu'on l'a découpé autrement.
2. Par la loi d'arbitrage (0.7) : deux claim qui produisent le même cash total → même prix total. **VU = VL.**
3. **MAIS** la part de l'equity de L est beaucoup plus VOLATILE que celle de U (elle passe de 6 000/4 000 = ±1 000 à 3 800/1 800 = ±1 000 aussi en valeur absolue mais sur une base equity bien plus petite — selon la valeur). L'equity lever est **plus risqué** → il exige un rendement plus élevé.

→ **Le levier ne crée pas de richesse : il la redéistribue — les actionnaires prennent plus de risque pour (au mieux) le même rendement moyen espéré.**

> **L'intuition du lait (MM, slide 8) :** l'entreprise non financée = le lait entier. Skim milk = l'equity lever (le résidu, plus risqué parce que la crème a été prélevée). Séparer le lait en crème+lait écrémé ne crée pas plus de lait total.

## 2.5 ⭐ Modigliani–Miller Proposition I (1958, sans impôts)

```
VU = VL        Firm value indépendante de la capital structure
WACC           indépendant de la capital structure
```
**Raison économique (à savoir donner en une phrase) :** le financement ne change pas les **cash flows opérationnels** → les mêmes pays ont le même prix, quelle que soit la manière dont on étiquette les bénéficiaires.

## 2.6 Application célèbre I — rachat d'actions financé par dette (slide 11)

**Setup :** 1 000 M d'actions à 20$ (≙ E = 20 000 M) · actifs existants = 20 000 M · pas de cash. L'entreprise émet **5 000 M de dette** et rachète ses propres actions avec tout le produit.

**Résolution pas à pas:**
1. Sous MM I : la valeur de la firme ne bouge pas → **V = 20 000** (inchangée).
2. Nouvelle dette = 5 000 → **E = V − D = 20 000 − 5 000 = 15 000**.
3. À 20$ l'action, 5 000 rachètent 5 000/20 = **250 M d'actions** → il reste 750 M d'actions.
4. Prix par action après opération = 15 000 ÷ 750 = **20$ — INCHANGÉ.**

**La leçon qui vaut en desk :** remplacer de l'equity par de la dette ne fait PAS mécaniquement monter le cours. Quand les vraies boîtes annoncent des buybacks et que le cours monte, c'est pour d'AUTRES raisons (signal de management confiant, discipline de cash, avantage fiscal,…), jamais parce que « equity moins action = plus de prix ».

## 2.7 Application célèbre II — émission d'actions (slide 13) et la « dilution »

**Setup identique ;** maintenant la firme émet 5 000 de NOUVELLES actions à 20$, le cash levé reste dans la boîte pour expansion.

1. Cash de la firme : 5 000 → Total equity = 20 000 + 5 000 = **25 000**.
2. Nouvelles actions : 5 000 ÷ 20 = **250** → total = 1 250 M.
3. Prix = 25 000 ÷ 1 250 = **20$ — INCHANGÉ.**

**Démystifier la dilution :** émettre des actions AUGMENTE le nombre d'actions (250 de plus) MAIS AUGMENTE aussi, du même montant, les actifs qui les portent (5 000 de cash entrant). Ton % de propriété baisse (dilution du %), mais **la valeur de chaque action ne bouge pas** — à condition que l'émission soit faite au juste prix. Au fond : **c'est faire une mauvaise opération (vendre à prix cassé, gaspiller le cash) qui détruit la valeur, pas le mécanisme d'émission.**

## 2.8 ⭐ MM Proposition II — le levier renchérit l'equity (exigé, pas gagné)

Les actionnaires exigent d'autant plus de rendement que le levier est élevé, puisqu'ils absorbent TOUT le risque résiduel après la dette :

```
rE = rWACC + (D/E) × (rWACC − rD)
```
**Comment la lire :**
- **rWACC** ici = le rendement exigé par l'ACTIF opérationnel (risque du business lui-même).
- **(rWACC − rD)** = l'écart entre risque de l'actif et risque de la dette (la dette est prioritaire → moins risquée → rD plus bas).
- **× (D/E)** : plus il y a de dette en face de chaque € d'equity, plus l'equity absorbe ce risque concentré.
- **Le rendement exigé monte donc linéairement avec le levier** (graphique : rE ↗, rD →, WACC → constant).

**Le cas choquant du slide 18 :** même exemple que 2.4, avec WACC = 100% (extrême). VL = espérance des cash flows ÷ 1+WACC = 5 000/2 = 2 500 → D = 2 000, E = 500. Rendement exigé par l'equity de L = 2 800/500 − 1 = **460%**. Intuition : sur une base equity minuscule (500), les actionnaires se partagent un résidu très volatile (3 800 ou 1 800) → il leur faut un rendement astronomique pour exister. C'est ce que vit un actionnaire de firme surendettée.

**✏️ Capital budgeting sans impôts (slide 19-20) — le calcul complet :**
- Actuel : D/E = 0,6, rD = 12%, rE = 20% → convertit D/E en pondérations : D/V = 0,6/1,6 = 37,5% · E/V = 62,5%.
- **WACC actuel = 0,375 × 12% + 0,625 × 20% = 4,5 + 12,5 = 17%.**
- Cible D/E = 1 → **nouveau rE = rWACC + (D/E)(rWACC − rD) = 17 + 1×(17−12) = 22%**.
- Nouveau WACC = 0,5 × 12% + 0,5 × 22% = **17% — INCHANGÉ ✓.**
- **Lecture magic du prof :** la dette à 12% est moins chère que l'equity à 22%... « cheaper debt » NE SIGNIFIE PAS « cheaper firm financing » — quand tu mets plus de dette, rE ajuste à la hausse exactement de quoi garder le WACC constant. La seconde famille soigne sa peur de la première.

## 2.9 La même idée via les **betas** (le fameux pont CAPM ↔ levier)

Traduis la MM II dans le cadre du CAPM (0.5). Il faut séparer :
- **βA (asset beta)** = risque de l'ACTIF (le business lui-même).
- **βE (equity beta)** = risque porté par les actionnaires (βA + risque ajouté par le levier).

```
Sans impôts :    βE = βA × (1 + D/E)      ⟹      βA = βE / (1 + D/E)
```
**✏️ M&M Corporation (slide 22) :** rE = 20%, rF = 12%, market premium = 5% → βE = (20−12)/5 = **1,6**. D/E = 0,6 → **βA = 1,6/(1+0,6) = 1,0.** Si D/E ↑ 1 : **βE = 1,0×(1+1) = 2,0** → **rE = 12 + 2×5% = 22% ✓** — même résultat que MM II. **Les deux routes convergent toujours** (via le matching WACC↔β slogans) — un examinateur adore cette double vérification.

## 2.10 Case II — ajoute les impôts : la dette crée enfin de la vraie valeur

**La physique du tax shield, expliquée sans malice :** l'État prélève l'impôt sur les sociétés sur le **bénéfice imposable = bénéfice APRÈS déduction des intérêts de la dette**. Donc chaque € d'intérêt versé à la banque te coûte vraiment `1 − τ` € car il fait baisser tes impôts de τ € (τ = taux d'impôt, ex. 25%).

- **Année sans dette :** taxable = X → cash après impôt = X(1−τ).
- **Année avec dette :** taxable = X − Interest → cash distribuable = X(1−τ) + Interest. **Bonus = τ × Interest chaque année — un vrai cash flow supplémentaire payé par l'État.**

```
Tax shield annuel = τ × Interest              (τ × rD × D quand la dette est permanente)
⬑ Actualisé sous les hypothèses du cours : PV du bouclier ≈ τ × D (dette permanente)
```

**⭐ Modified MM Proposition I (avec impôts) :**
```
VL = VU + τ × D
```
**⭐ Modified MM Proposition II (avec impôts) :**
```
rE = rU + (D/E) × (rU − rD) × (1 − τ)
```
**After-tax WACC :**
```
WACC = (D/V) × rD × (1 − τ) + (E/V) × rE
```
- Le Δ vs Case I : la dette ne change plus QUE le partage du gâteau — elle change **un vrai cash flow** (moins d'impôts) → **plus de gâteau total** → VL > VU et le WACC peut **baisser**.
- Le graphique Case II : rE monte toujours (mais moins vite, grâce au ×(1−τ) du bouclier) ; **WACC descend** avec D ; VL monte avec D (pente τ).
- **⚠️ Warning du slide 29 :** quand la structure change, mets à jour **à la fois** les poids D/V & E/V **ET** le rE — modifier les poids sans réviser rE = classique erreur de partiel.

**✏️ Recapitalisation avec impôts (slides 31-33, T=40%) — déroulé complet :**

| Étape | Calcul |
|---|---|
| 1. WACC actuel | D/V = 37,5% × 12% × (1−0,4) + E/V = 62,5% × 20% = 2,7 + 12,5 = **15,20%** |
| 2. Désendetté : rendement de l'actif | rU obtenu en résolvant WACC actuel → **rU ≈ 17,88%** (un peu au-dessus de l'actuel à cause du bouclier) |
| 3. Nouveau rE à D/E=1 | rE = 17,88 + 1 × (17,88 − 12) × (1−0,4) = 17,88 + 3,53 = **21,41%** |
| 4. Nouveau WACC | 0,5 × 12% × 0,6 + 0,5 × 21,41% = 3,6 + 10,71 = **14,31%** |
| Conclusion | Le WACC **BAISSE** (15,20 → 14,31) : le tax shield travaille. |
| Vérification via betas | βE = 1,6 → βA = 1,6/[1+0,6×0,6] = **1,176** → à D/E=1 : βE = 1,176×[1+0,6] = **1,882** → rE = 12 + 1,882×5 = **21,41% ✓** — les deux routes marchent toujours pareil. |

## 2.11 Case III — le coût manquant : la détresse financière (*financial distress*)

**Pourquoi 100% de dette est absurde dans la vraie vie :** à mesure que la dette monte, la probabilité d'être incapable de payer les intérêts augmente → la détresse coûte :

- **Coûts directs de faillite** : frais d'avocats, d'administrateurs judiciaires, liquidations precipitées (ventes à perte des actifs).
- **Coûts indirects** : les meilleurs talents fuient avant la chute · les clients hésitent à acheter à une boîte qui pourrait disparaître · les fournisseurs exigent le paiement cash · les banques refusent le refinancement · la direction passe son temps à gérer la crise au lieu de créer de la valeur.

**Le trade-off Case III :** à chaque € supplémentaire de dette, tu compares le **bénéfice marginal (un peu plus de tax shield)** au **coût marginal attendu (un peu plus de probabilité de distress × sa gravité)**.
- Tant que bénéfice > coût → augmente la dette.
- Quand coût dépasse bénéfice → stop.
- **Le point de rencontre = D* (structure optimale) : la valeur y est maximale, le WACC y est minimal.**

**Graphe Case III (la fameuse courbe en U renversé pour V / en U pour WACC) :**
- V = VU + τD − PV(expected distress costs) → monte, atteint un **sommet à D\***, puis redescend.
- WACC = symétrique : descend, atteint un **creux à D\***, puis remonte.

## 2.12 La synthèse Cases I → II → III (à savoir reproduire les yeux fermés)

| | Case I (no taxes) | Case II (+ taxes) | Case III (+ distress) |
|---|---|---|---|
| Hypothèse relâchée | monde parfait | impôt sur les sociétés | coûts de détresse |
| Bénéfice de la dette | aucun | tax shield | tax shield |
| Coût ajouté | aucun | aucun pas encore | expected distress costs |
| Firm value | constante | ↑ avec D | **max en D\*** |
| WACC | constant | ↓ avec D | **min en D\*** |
| Morale | structure **irrelevante** | **+ de dette = toujours mieux** | **il existe un optimum** |

> Argotée la phrase qui impressionne : *« No effect → tax benefit → tax benefit versus distress cost → optimum. »* Cette chronologie est aussi celle des décisions des vrais CFOs rating-cibling.

## 2.13 📐 NOVA Components — le cas de classe entièrement résolu

**La situation :** fabricant aux cash flows stables, projet de rachat d'actions financé par dette. L'actif opérationnel ne changera PAS. Ta mission (groupe de 5 = **Groupe 7** à présenter) : expliquer l'effet sur le risque de l'equity, le WACC et la valeur.

**Partie A (sans impôts) :**
| Question | Réponse commentée |
|---|---|
| 1. Prédictions | rE ↑ (lever ↑ → equity + risquée) · WACC **inchangé** (MM I) · valeur **inchangée** |
| 2. Poids & WACC actuel | D/E=0,5 → D/V = 0,5/1,5 = **1/3** · E/V = **2/3** · WACC = (1/3)×6% + (2/3)×12% = 2% + 8% = **10%** |
| 3. Nouveau rE à D/E=1 | rE = 10 + 1 × (10−6) = **14%** (l'actif exige 10% — le WACC actuel EST le rendement de l'actif) |
| 4. Nouveau WACC | 0,5×6% + 0,5×14% = **10%** — « cheaper debt » n'a PAS baissé le coût total ✓ |
| 5. Explication (3 phrases) | Même gâteau opérationnel, découpé différemment → la dette prioritaire absorbe du rendement fixe et déleste l'equity d'autant de risque, qui exige alors exactement le supplément de rendement nécessaire pour laisser le WACC total inchangé. Le financement ne change pas la production de cash de la machine. |

**Partie B (impôts 25%, rU = 10%, rD = 6%) :**
| Question | Réponse commentée |
|---|---|
| 6. rE à D/E = 0,5 | rE = 10 + 0,5 × (10−6) × (1−0,25) = 10 + 1,5 = **11,5%** |
| 6. rE à D/E = 1 | rE = 10 + 1 × 4 × 0,75 = **13%** |
| 7. WACC à D/E = 0,5 | (1/3)×6%×0,75 + (2/3)×11,5% = 1,5% + 7,67% = **9,17%** |
| 7. WACC à D/E = 1 | 0,5×6%×0,75 + 0,5×13% = 2,25% + 6,5% = **8,75%** → a **baissé** grâce au tax shield |
| 8. VU = 120 M€, D = 30 M€ | PV du bouclier = τ × D = 0,25 × 30 = **7,5 M€** → **VL = 127,5 M€** |
| 9. « La dette baisse le WACC → maximisons-la ! » | Ce qu'on PEUT conclure avec la S1 : le tax shield existe et fait baisser le WACC — réel. Ce qu'on ne peut PAS encore conclure : que la dette illimitée est optimale — il manque les **expected distress costs** (Case III), la flexibilité financière, et le fait que rD ne restera pas à 6% quand l'endettement monte. opti non démontrée sans Case III. |

**Ton deliverable de groupe (3 points, répète-le)** :
1. Le levier augmente le risque de l'equity → rE monte avec D/E (MM II), même si la dette est « pas chère ».
2. Sans impôts le WACC est constant ; AVEC impôts il baisse (tax shield = cash réel versé par l'État).
3. Le seul argument fiscal ne suffit pas à maximiser la dette — il manque les distress costs pour parler d'optimum (Case III, S2 et suite).

## 2.14 🌐 Utilité front de tout cela — pas décorative, opérationnelle

- **Desk crédit / high-yield** : le spread de crédit d'une obligation = le marché qui prixe ses **expected distress costs**. Quand D/E ↑, le spread s'écarte → Case III est ta grille de lecture quotidienne.
- **Desk equity / relative value** : MM I est l'ancêtre conceptuel de tout pair trade (« deux découpages pour le même gâteau → tout écart de prix relatif est une opportunité »).
- **LBO & DCM** : un LBO est une machine à exploiter le tax shield (VL = VU + τD) en garantissant par les cash flows stables que la probabilité de distress reste faible → comprendre le trade-off = comprendre tout DCM (Debt Capital Markets).
- **Ratings (S&P/Moody's)** : ciblage d'un D* = ciblage d'un rating (aux alentours de BB/B). Les bank parlent ce langage.
- **Ton entretien front** : rE = carry exigé vs carry reçu ; levier = ROE amplifié = risque amplifié (même physiquement que ton futur book with risk limits).

---
---

# PARTIE 3 — DEMAIN EN COURS : anticiper comme un pro (15-20 min suffisent)

## 3.1 CVM — S2 : ça va parler **prévisions et DCF**

La S1 s'est finie sur : *« can these operating economics persist? That is Session 2. »* La S2 sert donc à **construire et défendre une prévision** :

- **Horizon explicite** (5-10 ans projections) puis **terminal value** (la valeur de tout ce qui suit, synthétisée — souvent 60-80% de l'EV total).
- **Actualisation des FCFF au WACC → EV → pont → valeur par action.**
- Défendre tes hypothèses de croissance/marge/reinvestissement (le mot clé : **sustainability**).

**Prépare brièvement :**
- Si le prof inférent une terminal value : méthode Gordon (`TV = FCF_terminal × (1+g) / (WACC − g)` — grossissons pas encore : relis-la juste).
- ⚠️ **Choix d'entreprise à annoncer** : criteria = cotée, cap > 1 Md$, **FCF yield > 3%** (FCF / market cap), hors émergents, **5 ans de données historiques**. Avoir une shortlist de 3 (ex. : Sanofi, Schneider, Saint-Gobain — vérifie les critères avant de proposer).

## 3.2 Capital Structure — S2 : **Bond Valuation** (les bases à avoir en tête)

C'est le dossier le plus « marché » du cours — retiens les 5 mots :

1. **Bond (obligation)** = un prêt d'argent à un émetteur (État, entreprise) contre : des **coupons** réguliers (le % du nominal, ex. 3% × 1 000 = 30/an) + le remboursement du **nominal (face value)** à l'échéance.
2. **Bond price = PV des coupons + PV du nominal, actualisés au YTM** (Yield To Maturity, le taux de rendement exigé par le marché pour cette échéance/ce risque).
3. **Prix = 100 → l'obligation est « au pair » : coupon rate = YTM.** Coupon > YTM → l'obligation vaut PLUS que le nominal (premium). Coupon < YTM → elle vaut moins (discount). **La loi inverse : taux ↑ → prix ↓.** C'est la première loi de tout desk FICC.
4. **Yield (Rendement) courant ≠ YTM** : le YTM tient compte de la plus-value finale si tu l'achètes à décote.
5. **Duration** : durée de vie moyenne des cash flows = **sensibilité du prix au taux** (ΔPrix ≈ −Duration × Δtaux). Une duration de 7 → +1% de taux = −7% de prix. C'est LE thermomètre de risque taux partout (cf. Saidane 5/10 — vous y reviendrez en profondeur).

## 3.3 Career Management (vendredi 14h45-18h, Room A 220 — 20% présence)

Rien à rattraper → 15 min ce soir : CV à jour + pitch 30 s : « Stage de fin d'études janvier 2027 en transaction services / salle de marché — domaine FX travaillé depuis 2024 ».

---
---

# PARTIE 4 — DICTIONNAIRE EXPRESS (EN → FR, 0 jargon restant après ça)

| Terme EN | Sens 1 phrase |
|---|---|
| **Market price** | prix auquel le titre s'échange aujourd'hui |
| **Intrinsic value** | valeur estimée fondée sur les cash flows futurs |
| **Implied valuation gap** | écart (%) entre ta valeur estimée et le prix du marché |
| **Debt / Equity** | dette (prêteurs, prioritaires) vs actions (propriétaires, résiduels) |
| **Claim** | droit de recevoir des cash flows |
| **Residual claimant** | l'actionnaire = celui qui prend ce qui reste |
| **Interest / Coupon** | charges d'intérêt / paiement régulier d'une obligation |
| **Opportunity cost** | ce que tu abandonnes comme rendement ailleurs à risque égal |
| **Risk premium** | rendement supplémentaire exigé pour porter du risque |
| **Risk-free rate (rF)** | taux du placement sans risque (obligation d'État) |
| **CAPM** | rE = rF + β(rM−rF) — rendement exigé = sans risque + prime liée au marché |
| **Beta (β)** | sensibilité d'une action au marché (β=1 : comme le marché ; β=2 : ×2) |
| **Systematic / idiosyncratic risk** | risque du marché entier vs risque propre à une boîte (diversifiable) |
| **EBIT** | bénéfice avant intérêts et impôts = performance de l'exploitation |
| **EBITDA** | EBIT + D&A (proxy de cash, non un vrai cash flow) |
| **NOPAT** | EBIT normalisé × (1−t) : profit opérationnel après impôts, indépendant du financement |
| **D&A** | dépréciation & amortisation : coût comptable non-cash des actifs |
| **CapEx** | dépenses en nouvelles machines/actifs (sortie de cash réelle) |
| **NWC / ΔNWC** | besoin en fonds de roulement / sa variation (= cash bloqué en +) |
| **Inventory / Receivables / Payables** | stocks / factures clients non encaissées / factures fournisseurs non payées |
| **Invested Capital (IC)** | capital réellement engagé dans l'exploitation |
| **ROIC** | NOPAT/IC : rentabilité économique de ce capital |
| **WACC** | coût moyen pondéré du capital (D/V·rD(1−t) + E/V·rE) |
| **FCFF** | cash libre pour TOUS les financiers → actualisé au WACC → EV |
| **FCFE** | cash libre pour les actionnaires → actualisé au rE → Equity Value |
| **Net borrowing** | dettes émises − dettes remboursées (ajouté au FCFE) |
| **Enterprise Value (EV)** | valeur de la machine opérationnelle, tout financement confondu |
| **Equity Value** | EV − dette + cash excédentaire + actifs hors métier |
| **EV-to-equity bridge** | le pont exact EV → equity |
| **Excess cash** | cash NON nécessaire à l'exploitation courante |
| **Non-operating assets** | actifs hors cœur de métier (participations, placements) |
| **Normalize** | nettoyer les résultats du bruit comptable |
| **One-off / non-recurring** | exceptionnel (étiquette caution à vérifier vs RÉCURRENCE) |
| **Sustainable earnings** | résultats que la boîte reproduira vraisemblablement |
| **Reinvestment** | cash remis dans la machine (Net CapEx + ΔNWC) |
| **Reinvestment rate (rr)** | part du NOPAT réinvestie |
| **Fundamental growth** | croissance induite = rr × ROIC |
| **Arbitrage** | profit sans risque par écart de prix — force qui aligne les prix |
| **MM Proposition I** | VU = VL : la structure ne change pas la valeur (sans impôts) |
| **MM Proposition II** | rE = rWACC + (D/E)(rWACC−rD) : le levier renchérit l'equity |
| **Stock repurchase** | rachat de ses propres actions par l'entreprise |
| **Stock issuance** | émission de nouvelles actions |
| **Dilution** | baisse du % de propriété (≠ destruction de valeur si émis au juste prix) |
| **Corporate income tax (τ)** | impôt sur les sociétés (% du bénéfice imposable) |
| **Tax shield** | impôts économisés grâce à la déductibilité des intérêts (τ × Interest) |
| **Modified MM I / II** | VL = VU + τD ; rE = rU + (D/E)(rU−rD)(1−τ) |
| **rU (unlevered return)** | coût de l'equity de la firme SANS dette = rendement exigé de l'actif |
| **Asset beta (βA) / equity beta (βE)** | risque de l'actif vs risque porté par les actionnaires |
| **Financial distress** | difficulté financière grave (coûts directs + indirects) |
| **Expected distress costs** | coûts de détresse pondérés par leur probabilité |
| **Optimal capital structure (D*)** | D où V est max et WACC min (tax shield vs distress) |
| **Trade-off theory** | théorie qui arbitre tax shield vs distress |
| **Bond** | titre de dette = coupons réguliers + nominal remboursé à l'échéance |
| **Coupon rate** | le % régulier par rapport au nominal |
| **Nominal / face value** | le montant remboursé à l'échéance |
| **YTM (yield to maturity)** | taux de rendement exigé → équilibre prix & cash flows de l'obligation |
| **Par / premium / discount** | prix = nominal / au-dessus / en dessous |
| **Duration** | sensibilité du prix au taux (≈ durée moyenne des cash flows) |
| **Present value / discount rate** | valeur d'aujourd'hui / taux d'actualisation |
| **Terminal value** | valeur de la boîte après l'horizon de prévision (méthode Gordon) |
| **DCF** | valorisation par actualisation des cash flows futurs |

---

# AUTO-CHECK FINAL (fais-les sans relire — 10 min)

1. L'Aster : EV 1 250, dette 310, cash 85, investissements hors métier 25, 40 M actions → value/share = **?** *(26 €)*
2. Pourquoi ajoute-t-on le cash excédentaire dans le pont ? *(il n'est pas produit par l'FCFF, il appartient deja aux actionnaires)*
3. Un EBIT de 420 + restruct one-off 35 − gain cession 20 + cyber 12 = ? *(447)* ; le litige annuel de 8 on le garde ou pas ? *(on le GARDE — récurrent)*
4. NOPAT d'un EBIT 300 à t=25% ? *(225)* ; pourquoi l'EBIT exclut l'intérêt ? *(pour ne pas compter la dette deux fois — on la retrouve dans le WACC)*
5. Growth 6% avec ROIC 8% → rr = ? *(75%)* → FCFF = 200 − 150 = **50**.
6. Deux formes du FCFF : *(NOPAT − Reinvestment = NOPAT + D&A − CapEx − ΔNWC)*
7. Lumen : NOPAT = ? *(247,5)* · Reinvestment = ? *(51)* · FCFF = **?** *(196,5)*
8. rE à D/E=1 sans impôts, WACC 17%, rD 12% ? *(22%)* → le WACC bouge ? *(non : 17%)*
9. Avec impôts 25% : WACC à D/E=1 si rU=10%, rD=6% ? **?** *(8,75%)* → VL si VU=120, D=30 ? **?** *(127,5)*
10. Pourquoi ne pas utiliser 100% de dette si le tax shield existe ? *(à cause des expected distress costs → optimum D* en Case III)*
11. Obligation coupon 4%, le marché exige 6% → elle cote au-dessus ou en dessous de 100 ? *(en dessous — discount → car coupon < YTM)*
12. Nommer les 3 conditions de l'entreprise à choisir pour CVM : *(cap>1 Md$ · FCF yield>3% · hors marchés émergents, 5 ans de données)*

---

*Masterclass v2 — construite intégralement sur le contenu RÉEL des slides S1 + exercices + activité de classe (23/09/2026). Sinon la règle d'or : lis une fois, fais l'auto-check, refais UN calcul de mémoire, dors. Demain 9h45 — Amphi C 301.*
