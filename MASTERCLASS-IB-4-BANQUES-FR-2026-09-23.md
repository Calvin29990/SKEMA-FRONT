# 🏦 MASTERCLASS « UN COURS = UNE BANQUE D'INVESTISSEMENT »
## CVM (Valuation) + Capital Structure, racontés avec les **données réelles 2025/2026** de BNP Paribas, Société Générale, Crédit Agricole CIB, BPCE et CIC

**À quoi sert ce fichier :** le `MASTERCLASS-ZERO-reprise-24-09-2h-de-lecture.md` reste **le cours Skema 1 — il ne bouge pas, c'est notre socle théorique.** Celui-ci est le **2ᵉ lien** : la même théorie, mais chaque concept est « ancré » dans une vraie banque d'investissement française avec des chiffres réels (résultats FY2025 publiés en fév. 2026 + BNP S1 2026 publié le 18/09/2026). Objectif double :
1. **Comprendre** — la théorie devient lisible parce qu'elle a un visage, un chiffre, une banque.
2. **Prouver une motivation avancée** aux entretiens d'octobre (BNP, CIC, etc.) — on ne vient pas « apprendre », on vient avec le vocabulaire et les données du métier.

> **Règle d'or :** chaque chiffre ci-dessous est un **résultat publié** (communiqué de presse / Universal Registration Document) des banques, daté. C'est ça qui rend le discours crédible en entretien — « d'après vos résultats 2025… » est la phrase qui débloque une conversation.

**Les 5 maisons (les « 4 banques » + CIC) :**
| Maison | Groupe / modèle | Le CIB (banque d'investissement) |
|---|---|---|
| **BNP Paribas** | coté, le plus grand de France | **CIB** (Global Banking, Global Markets, Securities Services, Private Banking) |
| **Société Générale** | coté, forte en Marchés (FICC) | **Banque de Grande Clientèle & Solutions Investisseurs (BGCSI)** |
| **Crédit Agricole** | groupe coopératif/mutuel | **CA CIB** (Services Financiers aux Institutionnels) |
| **BPCE** | mutualiste (Banque Populaire + Caisse d'Epargne) | **Natixis** |
| **CIC** | Crédit Mutuel – CMAF (mutualiste) | marchés CIC (au sein du groupe CMAF) |

---
---

# PARTIE 0 — LA GRANDE IMAGE : pourquoi « un cours = une banque d'investissement »

Une banque d'investissement, c'est **une machine à créer de la valeur en la faisant circuler** : elle relie ceux qui **ont besoin de cash** (une entreprise qui veut croître) à ceux qui **veulent prêter/investir** (fonds, assureurs, épargnants). Les 2 cours de demain sont **exactement** les 2 questions que cette machine se pose **toute la journée** :

| Question de la banque d'inv. | Cours qui y répond |
|---|---|
| **« Combien ça vaut ? »** (valuer une entreprise, une transaction, un titre) | **CVM — Corporate Valuation** (Partie 1) |
| **« Comment financer ça au meilleur coût, avec le bon mix dette/equity ? »** | **Capital Structure** (Partie 2) |

**La boucle d'or d'une deal (une opération) :**
1. Le client (entreprise) veut **grandir / racheter / lever des fonds**.
2. Le banker **value** l'entreprise (DCF, comparables, EV→equity) → CVM.
3. Le banker **construit la structure de financement** : combien de dette (bon marché, tax shield) vs equity (cher mais pas de rembourse), quel WACC, quel rating → Capital Structure.
4. Le banker **place les tranches** (obligations, actions, prêts) auprès des investisseurs.
5. Le client paie des **commissions** ; la banque a **créé de la valeur** en optimisant le coût du capital.

> **En entretien, c'est ta phrase d'ouverture :** « Ce que j'ai trouvé fascinant dans les cours de Valuation et de Capital Structure, c'est que ce sont littéralement les deux questions d'une opération de banque d'investissement — combien ça vaut, et comment le financer. C'est exactement ce que j'ai voulu comprendre en profondeur. »

---
---

# PARTIE 1 — COURS DE VALUATION (CVM) → BANQUE D'INVESTISSEMENT
### « Combien ça vaut ? » avec des chiffres français

## 1.1 Le DCF et l'EV — le cœur de toute valorisation

Rappel du cours : **DCF = actualiser les FCFF au WACC → Enterprise Value (valeur de la machine opérationnelle).** C'est **LE** outil d'une banque d'investissement.

**Où tu le verras vraiment :**
- **M&A (advisory)** : quand BNP CIB conseille un client sur une acquisition, le premier livrable est un **modèle de valorisation** (DCF + comparables). C'est ce modèle qui définit le **prix** proposé au vendeur.
- **ECM (Equity Capital Markets)** : quand une banque accompagne une IPO ou une augmentation de capital, elle doit **définir une fourchette de prix** pour les actions → DCF + multiples sectoriels.
- **LBO** : le sponsor (fonds private equity) et la banque (ex. Natixis) valuent la cible pour dimensionner le levier.

**L'exemple réel qui rend ça concret — le cas Société Générale / Bernstein :**
- SG a **pris le contrôle du courtier américain Bernstein** et le **consolide à partir du 1er janvier 2026**.
- Le communiqué de résultats T4 2025 (publié le 06/02/2026) annonce pour 2026 : *« Des revenus des activités de Marché au-dessus de la fourchette cible de 5,1 à 5,7 Md€, **incluant la consolidation de Bernstein aux États-Unis à partir du 1er janvier 2026 (~200 M€ de contribution aux revenus annuels)** »*.
- **Traduction en cours :** ces « ~200 M€ de contribution » = la **valeur estimée des cash flows** que Bernstein va apporter. C'est **un mini-DCF** que le desk a fait avant de dire « ça vaut ~200 M€/an pour nous ». C'est exactement la logique `Reported → Forecast → FCFF → Value` du cours, appliquée à une acquisition réelle.

**Le pont EV → Equity, en opération M&A :**
```
Enterprise Value  = ce que paierait l'acquéreur pour la MACHINE (actifs opérationnels)
− Debt            = la dette que l'acquéreur prend en charge avec
+ Excess cash     = la trésorerie excédentaire (hors exploitation)
= Equity Value    = ce qui revient aux actionnaires du vendeur
```
- **En deal :** quand BNP CIB « vend » une filiale ou une partie d'activité (comme les **cessions d'actifs** de SG en 2024-2025 — on verra que SG retraitte ses résultats « hors cessions d'actifs »), le prix de cession se négocie sur **l'EV** de l'actif, pas sur le prix boursier.

> **Mot d'ordre pour l'entretien :** « Quand vous retraittez vos résultats *hors cessions d'actifs* (SG 2025 : +1,7% en publié vs +6,8% hors cessions), vous appliquez exactement la logique de normalisation du cours — séparer le **sustainable** du **one-off**. »

## 1.2 Les comparables et les multiples — l'outil quotidien du desk

Le cours distingue **intrinsic (DCF)** de **relative (comparables)**. En banque d'inv., les **deux** sont utilisés en permanence, et le desk parle en **multiples** :

| Multiple | Ce qu'il mesure | Où tu l'entendras |
|---|---|---|
| **EV / EBITDA** | prix payé pour 1€ de bénéfice opérationnel (avant financement) | M&A, LBO — LE multiple des transactions |
| **P / E (PER)** | prix / bénéfice net | Equity research, actions |
| **P / BV (tangible book)** | prix / fonds propres tangibles | **banques** (toujours ! une banque se value en P/BNPA) |
| **FCF Yield** | FCF / market cap | le critère que Sommer impose pour ton projet (≥3%) |

**Le cas des banques — P/BVPA (Price / Book Value per share) :**
Une banque ne se value presque **jamais** au PER (son « bénéfice » est volatil, son actif est des crédits). Elle se value en **Price / Tangible Book Value** :
- **BNP Paribas 2025** : Actif Net Tangible par action = **104,30 €**, BPA = **10,29 €**, PER ≈ **10,4x**.
- **Société Générale 2025** : BPA = **6,80 €**, PER ≈ **12,3x**.

> **Le point d'entretien le plus puissant :** « Une banque se value en **P/BVPA**, pas en PER. BNP traite à ~10,4x son BPA 2025 et SG à ~12,3x — l'écart reflète la perception du marché sur la **qualité du WACC** et le **ROTE** de chacune. » **Liaison directe cours → marché.**

## 1.3 Le ROE / ROTE / ROIC — le « rentabilité » que les banques s'évaluent à elles-mêmes

Le cours : **ROIC = NOPAT / Invested Capital** ; le test est **ROIC vs WACC**.
Pour une **banque**, la métrique reine n'est pas le ROIC mais le **ROTE (Return on Tangible Equity)** ou **RONE (Return on Net Equity)** — c'est le **ROIC bancaire** : la rentabilité des fonds propres.

**Les chiffres réels (FY2025) — à connaître par cœur :**
| Banque | ROTE / RONE 2025 | Cible |
|---|---|---|
| **BNP Paribas** | **11,6%** (2024 : 10,9%) | **13% d'ici 2028** (annoncé 20/11/2025) |
| **Société Générale** | **10,2%** (2024 : 6,0%) | **>10% en 2026** (cible relevée) |
| **Crédit Agricole** | **13,5%** | élevé et récurrent |
| **CA CIB** (division) | RONE **~16,7%** (2025) | — |
| **SG BGCSI** (division) | RONE **16,7%** (2025) | — |
| **SG Retail France** | RONE **13,9%** (2025) | — |

**La leçon en cours :** BNP veut passer de 11,6% à **13% de ROTE d'ici 2028** = +210 points de base. C'est **exactement** l'objectif « **augmenter le spread ROIC − WACC** » du cours, appliqué à une banque entière. SG a fait le même mouvement : **6,0% → 10,2% en un an** (le « turnaround » de Krupa).

> **Phrase d'entretien :** « Ce qui m'a frappé, c'est que BNP vise 13% de ROTE d'ici 2028 et SG >10% en 2026. En termes de cours, c'est la poursuite du spread entre rentabilité du capital et coût du capital — c'est littéralement la définition de la création de valeur. »

## 1.4 La « normalisation » — l'art du desk en chiffres réels

Le cours : **Reported ≠ Sustainable** → normaliser (retraiter les one-offs).
**En banque, c'est quotidien**, et le mot magique est **« à périmètre et change constant »** :

- **SG 2025** : PNB publié **+1,7%** mais **« +6,8% hors cessions d'actifs » / « +7,2% à périmètre et change constant »**.
  - **Traduction :** le PNB « brut » masque les **cessions** (one-offs à enlever) et les **effets de change** (bruit non opérationnel). Le desk compare les banques **retraitées**, jamais en publié brut. **C'est la normalisation du cours, mot pour mot.**
- **CA 2025** : le résultat **intègre une surtaxe exceptionnelle d'IS de ~280 M€** (on y revient en Partie 3) → le desk regarde aussi « hors surtaxe ».

> **Phrase d'entretien :** « Le cours insiste sur la différence entre *reported* et *sustainable earnings*. C'est exactement ce que les banques font avec le *périmètre et change constant* — retraiter le bruit pour isoler la performance **récurrente**. »

---
---

# PARTIE 2 — CAPITAL STRUCTURE → BANQUE D'INVESTISSEMENT
### « Comment financer ça ? » — le cœur du métier de DCM / Structured Finance

## 2.1 Le WACC — le « coût du capital » que les banques **optimisent** pour leurs clients

Le cours : **WACC = (D/V)·rD·(1−τ) + (E/V)·rE**. C'est le **taux d'actualisation** ET le **seuil de rentabilité** (hurdle rate) d'un projet.

**En banque d'inv., c'est le cœur de 3 métiers :**
1. **DCM (Debt Capital Markets)** : placer des **obligations** et des **EMTN** pour les clients → dimensionner la **dette** au meilleur coût.
2. **Structured Finance** : construire des montages (titrisation, leveraged finance) → mixer dette + equity.
3. **M&A / LBO** : définir la **levure** (le ratio de levier) d'une acquisition.

**Le cas réel — Natixis (le CIB de BPCE) et le LBO :**
- **Natixis** est un acteur de référence du **leveraged finance / LBO** en France et en Europe.
- **2025 : PNB record de 4,8 Md€ (+10%)** — le communiqué BPCE le cite explicitement : *« Natixis CIB : PNB record de 4,8 Md€ (+10%) »*.
- **En cours :** un LBO = **emprunter au maximum (levier) pour acheter une entreprise**, en comptant sur le **tax shield** de la dette et les cash flows de la cible pour rembourser. **Chaque euro de levier supplémentaire** augmente le ROE du sponsor **mais aussi le risque de distress** → c'est **littéralement le trade-off Case III du cours** (tax shield vs coûts de détresse) appliqué à des milliards d'euros.

> **Phrase d'entretien :** « Dans un LBO, le sponsor et la banque (Natixis ici) dimensionnent le levier en arbitrant **tax shield** contre **coûts de distress** — c'est le Case III du cours de Capital Structure, appliqué à un deal réel. Le PNB record de 4,8 Md€ de Natixis en 2025, c'est ce métier-là qui tourne bien. »

## 2.2 Le tax shield — et pourquoi la « surtaxe IS » de 2025 est LE sujet parfait

**Le cours (Case II) :** la dette crée de la valeur grâce au **tax shield** : `VL = VU + τ·D` (les intérêts sont déductibles).
**La réalité 2025 :** l'État français a **pris une surtaxe** sur les bénéfices des grandes entreprises, qui a **directement** touché les banques. **C'est le point d'entretien le plus frais et le plus impressionnant que tu puisses avoir.**

### La surtaxe — ce qu'il faut savoir par cœur (source : loi de finances 2025, art. 48 ; FBF ; Les Échos)
- **Mécanisme :** une **contribution exceptionnelle** sur les bénéfices des grandes entreprises, créée par la **loi n° 2025-127 du 14/02/2025 (art. 48)**.
  - **Taux de 20,6%** en plus de l'IS pour les entreprises à **1–3 Md€** de CA français.
  - **Taux de 41,2%** pour les groupes au-delà de **3 Md€**.
  - S'applique à la **moyenne** de l'IS de l'exercice en cours et du précédent.
- **Montant visé :** **~8 Md€** au profit de l'État en 2025 (imagine par le gouvernement Barnier), **reconduite en 2026** (budget voté en 49.3).
- **L'effort des banques :** **au moins ~1 Md€** au total (le secteur bancaire est l'un des plus gros contributeurs, ~15% de l'effort).
- **Par banque (FY2025) :**
  - **Crédit Agricole** : **~280 M€** intégrés au résultat 2025.
  - **BPCE** : **~200 M€** (résultat net publié de 4 061 M€ malgré cette charge).
  - **CIC** : **78 M€** (résultat net de 1,9 Md€, **>2,0 Md€ hors surtaxe**).
  - **BNP Paribas** : **« quelques millions »** seulement — parce que **la surtaxe ne vise que le CA en France**, et BNP est très **internationalisée** (sa majorité de revenus est hors France) → **peu taxable**.
  - **Société Générale** : impact **« limité »** (selon Krupa) — même raison.
- **La réaction du secteur :** la **Fédération Bancaire Française** (présidée par **Daniel Baal**, président du Crédit Mutuel) dit que la taxe **« n'a aucun sens »**. Les Échos notent que **Crédit Mutuel et Crédit Agricole, très exposés au marché français, sont en première ligne — « une raison de plus pour accélérer leur internationalisation »**.

### Pourquoi c'est un **chef-d'œuvre pédagogique** (et un **carré d'entretien**)
1. **C'est le cours, en vrai :** le cours dit `VL = VU + τ·D` — **plus τ est haut, plus le tax shield de la dette est gros, mais plus l'impôt pèse sur la valeur**. En 2025, **τ a bondi** pour les grandes banques → **valeur du groupe pée**, et **l'arbitrage dette/equity a bougé** (la dette est devenue *relativement* encore plus « chère » en terme de valeur après impôt pour les banques françaises à CA local).
2. **C'est un fait 100% récents et vérifiable** (loi de 02/2025, reconduction 2026, résultats publiés 02/2026) → tu parles en connaissance de cause.
3. **C'est un argument stratégique** (l'internationalisation comme **arbitrage fiscal**) → tu montres que tu lis **au-delà des chiffres**, comme un banker.

> **La phrase d'entretien (à réciter) :**
> « Le point qui m'a le plus parlé dans Capital Structure, c'est le **tax shield**. Et la **surtaxe sur l'IS de 2025** (loi de finances, art. 48) est l'illustration parfaite : elle a pesé **~280 M€ sur Crédit Agricole**, **~200 M€ sur BPCE**, **78 M€ sur CIC**, mais seulement **« quelques millions » sur BNP** — parce qu'elle ne taxe que le **chiffre d'affaires en France**. C'est une raison donnée par les Échos pour **accélérer l'internationalisation**. C'est le trade-off du cours qui devient une décision de stratégie de groupe. »

## 2.3 Le levier, le rE et le « cheap debt » — la leçon MM appliquée

Le cours (Proposition II) : **rE = rWACC + (D/E)(rWACC − rD)** → **le levier renchérit l'equity**. « Cheap debt » ne signifie pas « cheap firm ».

**En banque, c'est la gestion du **bilan** :**
- Une banque **est** levier par nature (elle emprunte des dépôts pour prêter). Son **cœur** de Capital Structure, c'est le **ratio CET1** (Common Equity Tier 1 — le « fonds propres de base ») :
  - **BNP** : **12,5%** (fin sept. 2025) → **objectif relevé à 13% à l'horizon 2027** (annoncé **20/11/2025**).
  - **SG** : **13,5%** (fin 2025) → le plan **maintient >13%** sur toute la durée du nouveau plan (sept. 2026).
  - **BPCE** : **16,5%** (fin déc. 2025) — un niveau très prudent (mutualiste).
- **Le lien cours ↔ bilan :** le **CET1** est le coût du capital « **cher** » (equity de base). Plus une banque est **levée** (peu de CET1), plus elle peut prêter, mais plus elle est **risquée** en cas de **distress**. L'objectif de **relever le CET1** de BNP (12,5→13%) = **réduire le levier pour réduire le risque** = **retourner vers la « U » (moins de levier) du cours MM**.

> **Phrase d'entretien :** « Le cours de Capital Structure dit que le levier renchérit l'equity (Proposition II). Une banque, c'est du levier par nature : son **CET1** est son équivalent d'« equity de base ». BNP a **relevé sa cible CET1 de 12,5% à 13% pour 2027** — c'est le choix de **réduire le levier et donc le risque de distress**, exactement le trade-off du cours. »

## 2.4 La « structure optimale » (D*) — et la leçon du plan SG 2026

Le cours (Case III) : il existe un **D\*** où la valeur est max / le WACC min (tax shield vs distress).

**Le plan stratégique SG de septembre 2026** (présenté le **21/09/2026**, l'action a bondi de **220%** depuis le « fiasco » de 2023) est une **poursuite** de l'optimisation :
- **~1,9 Md€ de réductions de coûts brutes** sur la période (1 Md€ d'inflation + 600 M€ d'investissements).
- **CET1 maintenu >13%** → la banque reste du bon côté du risque.
- **Croissance modérée** + **Boursobank : 14 M de clients d'ici 2029** (digital).
- **La leçon en cours :** le D\* de SG = **un levier prudent (CET1 >13%)** + **des coûts maîtrisés** (le cost/income ratio est passé de **69% → 63,6%** en 2025). C'est **l'optimisation du WACC** de la banque : **moins de coût, même rentabilité, capital sécurisé**.

> **Phrase d'entretien :** « Le nouveau plan de SG (sept. 2026) vise ~1,9 Md€ d'économies tout en maintenant le CET1 >13%. C'est l'optimisation du « WACC » de la banque : réduire le coût de structure tout en gardant le capital du bon côté du risque — la recherche du **D\*** du cours, version 14 M de clients Boursobank. »

---
---

# PARTIE 3 — LES 5 BANQUES « SUR LE BOUT DES DOIGTS »
### Les données à connaître (toutes publiées, FY2025 sauf mention). Format : Position → Chiffres → Stratégie → Angle d'entretien.

## 3.1 🏦 BNP PARIBAS — « le n°1, le global »

**Position :** la **plus grande banque française** (et une des plus grandes d'Europe). Modèle **intégré global** : banque de détail + **CIB** + gestion d'actifs + assurance. Le CIB = **~37% des revenus** du groupe.

**Les chiffres FY2025 (publiés 05/02/2026) :**
| Indicateur | FY2025 | Var. |
|---|---|---|
| **Produit net bancaire (PNB / revenus)** | **51,2 Md€** | +4,9% |
| **Résultat net part du groupe** | **12,2 Md€** (record) | +4,6% |
| **BPA (bénéfice par action)** | **10,29 €** | +7,5% |
| **ROTE** | **11,6%** | vs 10,9% en 2024 |
| **Dividende par action** | **5,16 €** | +7,7% |
| **Actif net tangible par action** | **104,30 €** | — |
| **CET1** | **12,5%** (fin sept. 2025) | → cible **13% en 2027** |

**Le CIB (Corporate & Institutional Banking) — FY2025 :**
- **Revenus : 18,997 Md€ (+5,6%)** · Charges 11,061 Md€ · **GOI 7,936 Md€ (+9,3%)** · **Cost/income 58,2%** · **RONE 21,3%** · **RWA 258,2 Md€**.
- **S1 2026 (publié le 18/09/2026 — TRÈS récent) :** PNB groupe **14,091 Md€ (+12,0%)** ; **CIB PNB 5,281 Md€ (+12,7%)** — *« CIB réalise une très solide performance, **ancrant sa position de numéro 1 en EMEA parmi les banques européennes** »*.

**Stratégie (à connaître) :**
- **Cible ROTE 13% d'ici 2028** (+210 pts de base vs 2024) — annoncé le **20/11/2025**.
- **CET1 relevé à 13% pour 2027** (au lieu de 12,5%).
- **Programme de rachat d'actions de 1,15 Md€** (autorisé par la BCE) — **rappel du cours : un buyback, à prix juste, ne dilue pas la valeur (Proposition I)**.
- **Le plan 2027-2030 sera présenté début 2027.**

**Angle d'entretien :**
- « BNP est **n°1 CIB en EMEA** — votre S1 2026 (18/09) le confirme avec un CIB à +12,7%. »
- « La cible **ROTE 13% en 2028** et le **rachat d'actions de 1,15 Md€**, c'est la création de valeur actionnariale du cours, en politique de dividende/rachat. »
- Le **PER ~10,4x** et le **P/BNPA** → la valorisation d'une banque.
- **Point d'attention à poser intelligemment :** les **incertitudes juridiques aux États-Unis** (le groupe a des activités US). → « Je vois que le groupe mentionne des incertitudes US ; comment cela pèse-t-il sur la valorisation du CIB ? »

## 3.2 🏦 SOCIÉTÉ GÉNÉRALE — « le turnaround, forte en Marchés/FICC »

**Position :** banque **intégré**, historiquement **très forte en Marchés (FICC = Fixed Income, Currencies, Commodities)** et en banque de détail France. **Turnaround** sous **Slawomir Krupa** (DG depuis 2024) : de la médiocrité 2023 au record 2025.

**Les chiffres FY2025 (publiés 06/02/2026) :**
| Indicateur | FY2025 | Var. |
|---|---|---|
| **PNB (revenus)** | **27,3 Md€** (record) | +1,7% publié / **+6,8% hors cessions** |
| **Résultat net part du groupe** | **6,0 Md€** (record) | **+42,9%** |
| **BPA** | **6,80 €** | vs 4,38 € en 2024 |
| **ROTE** | **10,2%** (9,6% hors gains non récurrents) | cible ~9% dépassée |
| **Cost/income ratio** | **63,6%** | vs 69% en 2024 |
| **CET1** | **13,5%** | plan le maintient >13% |
| **Distribution totale 2025** | **4,7 Md€** | +169% (dividende 1,61 € + **rachat 1,462 Md€**) |

**Le CIB (Banque de Grande Clientèle & Solutions Investisseurs — BGCSI) — FY2025 :**
- **Revenus : 10,419 Md€ (record, +2,6%)** · **Résultat net 2,915 Md€ (+3,7%)** · **RONE 16,7%**.
- **Retail France + Private Banking + Assurance** : revenus +6,3%, **résultat net +80,3% à 1,815 Md€**, **RONE 13,9%**.
- **Bernstein** : prise de contrôle, **consolidation depuis le 1er janvier 2026** (~200 M€/an de contribution aux revenus Marchés).

**Stratégie (le NOUVEAU plan, présenté le 21/09/2026) :**
- **~1,9 Md€ de réductions de coûts** brutes sur la période.
- **CET1 maintenu >13%** sur toute la durée du plan.
- **Croissance modérée** + **Boursobank : 14 M de clients d'ici 2029**.
- **Cible 2026 : ROTE >10%** (relevée) ; BGCSI cost/income <65% ; revenus Marchés 5,1–5,7 Md€ (incl. Bernstein).
- **Social :** **1.800 suppressions de postes d'ici fin 2027** (départs naturels, pas de licenciements ; ~1.000 en banque de détail) — **c'était déjà ~900 postes au siège en 2024**. Cessation de **Gilbert Dupont** (courtier).

**Angle d'entretien :**
- « SG est passée de **6,0% de ROTE en 2024 à 10,2% en 2025** — c'est le **turnaround** du cours (relever le spread rentabilité − coût). »
- « La **consolidation de Bernstein** (~200 M€/an), c'est une **acquisition value** : vous avez dû la valuer (DCF + synergies) avant de la payer. »
- « Le **coût d'exploitation à 63,6%** (vs 69%), c'est la maîtrise du **WACC**/des coûts de structure. »
- **Point d'attention à poser :** le **plan social de 1.800 postes** → « Comment le groupe articule la **réduction de coûts** et l'**investissement dans le digital (Boursobank)** sans casser la culture ? »

## 3.3 🏦 CRÉDIT AGRICOLE / CA CIB — « le coopératif, leader de la finance durable »

**Position :** le **plus grand groupe bancaire coopératif/mutuel** d'Europe (modèle unique : réseau de **Caisses Régionales** + **SICa**). **10e groupe bancaire mondial par les actifs** (The Banker, 07/2025). **CA CIB** = la banque d'investissement du groupe, **~10.000 collaborateurs**, **leader mondial de la finance durable/climat**.

**Les chiffres FY2025 (publiés 04/02/2026) :**
- **Groupe Crédit Agricole** : PNB **39,6 Md€ (+3,9%)** · Résultat net part du groupe **8,75 Md€ (+1,3%)** (intègre la **surtaxe ~280 M€**).
- **Crédit Agricole S.A.** (la société mère cotée) : PNB **28,1 Md€ (+3,3%, record)** · Résultat net **7,07 Md€** (stable) · BPA **2,18 €** · dividende **1,13 €**.
  - ⚠️ **T4 2025 :** résultat net CASA à **1,025 Md€ (−39,3%)**, impacté par la **mise en équivalence de Banco BPM (−607 M€)** — l'opération en Italie.
- **ROTE groupe : ~13,5%.**

**CA CIB (Services Financiers aux Institutionnels) — FY2025 :**
- **PNB : 6,783 Md€ (record, +3,3% publié / +5,2% à change constant)** — record à la fois en banque de marché/investissement ET en banque de financement.
- **Résultat net : 2,261 Md€ (+5,1%)**.
- **T4 2025 : PNB 543 M€ (+1,5%)**, résultat net 220 M€ (−2,6%).
- **Amundi** (gestion d'actifs du groupe) : PNB 3,342 Md€ (−1,9% publié, **+6,2% hors déconsolidation d'Amundi US**).

**Stratégie (à connaître) :**
- **Plan à moyen terme 2028 « ACT 2028 »** (présenté le **18/11/2025**) : 3 piliers — **A**ccélération, **C**ohésion, **T**ransformation. Ambition : **leader européen des transitions et des nouvelles technologies**.
- **CA CIB** se réorganise en **value chains « front-to-accounting »** (de la première relation client à la comptabilisation) pour plus d'agilité.
- **Leader mondial de la finance durable / climat** (green bonds, transition).

**Angle d'entretien :**
- « CA CIB est **leader de la finance durable** — c'est un avantage compétitif qui se **valorise** auprès des investisseurs ESG. »
- « Le plan **ACT 2028** (Accélération, Cohésion, Transformation), c'est la stratégie de **croissance du spread rentabilité** du cours, appliquée au groupe. »
- **La surtaxe** : CA est **en première ligne** (~280 M€, CA local élevé) → « une raison pour accélérer l'internationalisation » (Les Échos). **C'est ton argument le plus frais.**
- **Point d'attention à poser :** **Banco BPM** (Italie) — « Comment l'intégration de Banco BPM pèse-t-elle sur le résultat CASA (−607 M€ au T4) et sur la valorisation groupe ? »

## 3.4 🏦 BPCE — « le mutualiste, celui où tu as stage »

**Position :** le **2e groupe bancaire mutualiste** français — réseau **Banque Populaire** + **Caisse d'Epargne** + **Natixis** (le CIB) + **BRED** + **Oney** + **CASDEN** (la banque des étudiants et de la fonction publique). **~35 M de clients, ~100.000 collaborateurs.**

**Les chiffres FY2025 (publiés 03/02/2026 — « ouvre le bal » des résultats) :**
| Indicateur | FY2025 | Var. |
|---|---|---|
| **PNB (revenus)** | **25,7 Md€** | **+10%** (record historique) |
| **Résultat net part du groupe (publié)** | **4,061 Md€** | **+15%** (record) |
| **CET1** | **16,5%** (fin déc. 2025) | prudent (mutualiste) |
| **Crédits produits (ménages + entreprises)** | **102 Md€** | +20% |
| **Nouveaux clients** | **~820.000** | — |

**Détail par pôle (FY2025) :**
- **Banque de proximité & Assurance** : PNB **17,5 Md€ (+14%)**.
- **Banque Populaire** : résultat net **1,687 Md€ (+26%)**, PNB 6,8 Md€.
- **Caisse d'Epargne** : résultat net **1,832 Md€ (+45%)**, PNB 6,89 Md€.
- **Natixis (le CIB)** : **PNB record 4,8 Md€ (+10%)** — leader du **LBO / leveraged finance**.
- Intègre la **surtaxe ~200 M€** dans le résultat publié.

**Stratégie :** plan stratégique visant à faire de **BPCE un « géant bancaire européen »** ; forte **croissance commerciale** (820.000 nouveaux clients), **crédits +20%**.

**Angle d'entretien — TON avantage (l'ancien stagiaire) :**
- Tu as **stagié à BPCE en 2024** (6 mois). **C'est ton atout n°1** ici.
- « J'ai fait mon stage à BPCE en 2024, et je suis impressionné par la trajectoire : **PNB +10% et résultat net record à 4,06 Md€ en 2025**, porté par **Natixis (4,8 Md€ de PNB record)** et les réseaux. »
- « Le **CET1 à 16,5%**, c'est le modèle mutualiste **prudent** — c'est le **Case III** du cours : rester bien loin du distress. »
- « **Natixis**, c'est le **LBO** du cours : le levier qui arbitre **tax shield** et **distress**. »
- **Point d'attention à poser :** « Comment le groupe mutualiste articule sa **prudence capitalistique (CET1 16,5%)** avec l'ambition de **devenir un géant européen** (qui demande des M&A = du levier) ? »

## 3.5 🏦 CIC (Crédit Mutuel – CMAF) — « le mutualiste, forte en région »

**Position :** le **CIC** est la banque de détail du groupe **Crédit Mutuel – CMAF** (mutualiste), **headquarters à Toulouse**, très implantée dans le **Sud-Ouest / Nouvelle-Aquitaine** (ta région). Ne pas confondre avec BPCE.

**Les chiffres FY2025 (communiqué CMAF) :**
| Indicateur | FY2025 | Var. |
|---|---|---|
| **PNB** | **6,8 Md€** | **+7,7%** |
| **Résultat net** | **1,9 Md€** | **+12,7%** (**>2,0 Md€ hors surtaxe de 78 M€**) |
| **Cost/income ratio** | **56,7%** | excellent |
| **Effectifs / clients** | **20.000 / 5,8 M** | — |

- **Banque de détail** : PNB **+7,2%** (marge d'intérêt + reprise des crédits à l'habitat).
- **Activités de marché** : PNB **+12,9%**.
- **Stratégie :** **plan stratégique 2024-2027** ; les résultats « confirment les objectifs ».

**Angle d'entretien :**
- « Le **cost/income ratio à 56,7%**, c'est l'un des **meilleurs du secteur** — c'est la **maîtrise du WACC/coûts** du cours. »
- « La **surtaxe** pèse **78 M€** (résultat >2,0 Md€ hors taxe) — le groupe est **exposé au marché français**, d'où l'internationalisation du **Crédit Mutuel** (qui a payé **~400 M€** de surtaxe, le plus gros contributeur). »
- **Point d'attention à poser :** « Comment le CIC articule sa **force régionale** (Nouvelle-Aquitaine) avec la **croissance des activités de marché (+12,9%)** qui sont plus concurrentielles et globales ? »

---
---

# PARTIE 4 — LE TABLEAU COMPARATIF « SUR LE BOUT DES DOIGTS »
### À savoir reconstituer de mémoire en entretien (FY2025, publié fév. 2026)

| | **BNP Paribas** | **Société Générale** | **Crédit Agricole** | **BPCE** | **CIC (CMAF)** |
|---|---|---|---|---|---|
| **Modèle** | Coté, global | Coté, FICC/detail | Coopératif/mutuel | Mutualiste | Mutualiste |
| **Le CIB** | **CIB** | **BGCSI** | **CA CIB** | **Natixis** | marchés CIC |
| **Revenus / PNB** | **51,2 Md€** (+4,9%) | **27,3 Md€** (+1,7% / +6,8% h.cessions) | **39,6 Md€** (+3,9%) | **25,7 Md€** (+10%) | **6,8 Md€** (+7,7%) |
| **Résultat net** | **12,2 Md€** (+4,6%) | **6,0 Md€** (+42,9%) | **8,75 Md€** (+1,3%) | **4,06 Md€** (+15%) | **1,9 Md€** (+12,7%) |
| **ROTE / RNE** | **11,6%** | **10,2%** | **~13,5%** | (mutuel) | — |
| **CET1** | **12,5%** → 13% (2027) | **13,5%** (maintenu >13%) | — | **16,5%** | — |
| **Revenus CIB** | **19,0 Md€** (+5,6%) | **10,4 Md€** (record) | **6,8 Md€** (record) | **4,8 Md€** (record, +10%) | (+12,9% marchés) |
| **RONE CIB** | **21,3%** | **16,7%** | **~16,7%** | — | — |
| **BPA / Dividende** | 10,29 € / 5,16 € | 6,80 € / 1,61 € | 2,18 € / 1,13 € | (non coté) | (CMAF) |
| **Surtaxe IS 2025** | « quelques M€ » (CA intl.) | « limité » (Krupa) | **~280 M€** | **~200 M€** | **78 M€** |
| **Plan / cibles** | ROTE 13% (2028) · CET1 13% (2027) · rachat 1,15 Md€ | Nouveau plan (09/2026) : −1,9 Md€ coûts · CET1 >13% · Boursobank 14M (2029) | **ACT 2028** (Accélération, Cohésion, Transformation) | « Géant européen » | Plan 2024-2027 |
| **Événement marquant** | **N°1 CIB EMEA** (S1 2026, +12,7%) | **Turnaround** 6%→10,2% ROTE · **Bernstein** | **Leader finance durable** · **Banco BPM** | **Record historique** · **Natixis LBO** | **Cost/income 56,7%** |

> **Mnémotechnique :** « **B**NP = le **B**ig global (n°1 EMEA) · **S**G = le **S**print (turnaround + Bernstein) · **C**A = le **C**oopératif durable (ACT 2028) · **B**PCE = le **B**on mutualiste prudent (CET1 16,5%) · **C**IC = le **C**oût maîtrisé (56,7%). »

---
---

# PARTIE 5 — LE « PITCH » D'ENTRETIEN (comment tu utilises ça sans paraître robot)

## 5.1 La structure de ton discours (60-90 secondes)

1. **L'accroche métier** : « Ce que j'ai trouvé fascinant dans mes cours de **Valuation** et de **Capital Structure**, c'est que ce sont **les deux questions d'une opération de banque d'investissement** — combien ça vaut, et comment le financer au meilleur coût. »
2. **L'ancrage réel** (choisis 1-2, selon la banque) :
   - Pour **BNP** : « J'ai vu vos **résultats S1 2026** : CIB à **+12,7%**, n°1 en EMEA. Et la cible **ROTE 13% en 2028**, c'est la création de valeur du cours en politique de capital. »
   - Pour **SG** : « Le **turnaround** de **6% à 10,2% de ROTE**, et la **consolidation de Bernstein** (~200 M€/an) — c'est une acquisition qu'il a fallu **valuer**. »
   - Pour **CA** : « La **surtaxe IS de 2025** a pesé **~280 M€** sur CA, « quelques M€ » sur BNP — c'est le **tax shield** du cours qui devient une décision d'internationalisation. »
   - Pour **BPCE** : « J'ai **stagié** chez vous en 2024. Le **record 2025** (résultat +15%, **Natixis 4,8 Md€**), et le **CET1 16,5%**, c'est le **Case III** du cours : la prudence du capital. »
   - Pour **CIC** : « Le **cost/income 56,7%**, c'est l'une des meilleures du secteur — la **maîtrise des coûts** du cours. »
3. **La question que tu poses** (montre que tu penses, pas que tu récites) :
   - « **Comment** le groupe articule **croissance des revenus** (CIB) et **discipline capitalistique** (CET1/ROTE) ? »
   - « Quel est le **rôle du digital** (Boursobank, front-to-accounting) dans l'optimisation du **coût** du modèle ? »
   - « Comment **valorisez-vous** vos activités les plus récentes (Bernstein, Banco BPM) ? »

## 5.2 Les 5 « questions tranchantes » à avoir en poche (une par banque)

| Banque | La question tranchante |
|---|---|
| **BNP** | « Avec un **PER ~10,4x** et une cible **ROTE 13% en 2028**, pensez-vous que le **marché sous-valorise** encore le CIB par rapport aux pairs ? » |
| **SG** | « La **consolidation de Bernstein** (~200 M€/an) — quelle **méthode de valorisation** (DCF, comparables, synergies) a déterminé le **prix payé** ? » |
| **CA** | « La **surtaxe IS** (loi 2025) pèse **~280 M€** sur CA. C'est, comme le disent les Échos, un **accélérateur d'internationalisation** — comment cela change-t-il votre **arbitrage dette/equity** ? » |
| **BPCE** | « Avec un **CET1 à 16,5%**, le groupe est **sous-levé** par rapport aux pairs. Est-ce une **contrainte** ou un **avantage** pour financer des **acquisitions** et devenir « géant européen » ? » |
| **CIC** | « Le **cost/income 56,7%** est excellent. Quel **levier** (IA, digital, Boursobank-like) comptez-vous actionner pour **garder** cette efficacité en **augmentant les revenus de marché (+12,9%)** ? » |

## 5.3 Les 3 pièges à éviter en entretien

1. **Ne pas confondre CIC et BPCE** — deux groupes mutualistes **différents** (CIC = Crédit Mutuel-CMAF ; BPCE = Banque Populaire + Caisse d'Epargne + Natixis).
2. **Ne pas citer un chiffre sans sa date** — dis toujours « **vos résultats 2025** (publiés en février) » ou « **votre S1 2026** (18/09) ». Un chiffre daté = crédibilité.
3. **Ne pas paraître « réciter le cours »** — le cours est **ton vocabulaire**, pas ton discours. Tu parles de la **banque d'abord**, et tu **utilises** les concepts (WACC, tax shield, ROE, D*) comme **langage**, pas comme leçon.

---
---

# AUTO-CHECK « BANQUES » (à savoir reconstituer de mémoire — 10 min)

1. **BNP FY2025** : PNB **?** · Résultat net **?** · ROTE **?** · CET1 **?** → *(51,2 Md€ · 12,2 Md€ · 11,6% · 12,5% → cible 13% en 2027)*
2. **Le CIB de BNP en 2025** : revenus **?** · RONE **?** → *(19,0 Md€ · 21,3%)* — et en **S1 2026** ? → *(+12,7%, n°1 EMEA)*
3. **SG FY2025** : PNB publié **?** / hors cessions **?** · Résultat net **?** · ROTE **?** · Cost/income **?** → *(27,3 / +6,8% · 6,0 Md€ · 10,2% · 63,6%)*
4. **L'événement SG 2026** : consolidation de **?** (~**?**/an) · nouveau plan (sept.) : **?** de réductions de coûts, CET1 **?** → *(Bernstein · ~200 M€ · ~1,9 Md€ · >13%)*
5. **Crédit Agricole FY2025** : PNB **?** · Résultat net **?** · ROTE **?** → plan **?** (3 piliers) → *(39,6 Md€ · 8,75 Md€ · ~13,5% · ACT 2028)*
6. **CA CIB 2025** : PNB **?** · Résultat net **?** · position **?** → *(6,8 Md€ · 2,26 Md€ · leader finance durable)*
7. **BPCE FY2025** : PNB **?** · Résultat net **?** · CET1 **?** · le CIB **?** → *(25,7 Md€ +10% · 4,06 Md€ +15% · 16,5% · Natixis 4,8 Md€ record)*
8. **CIC FY2025** : PNB **?** · Résultat net **?** · cost/income **?** → *(6,8 Md€ · 1,9 Md€ · 56,7%)*
9. **La surtaxe IS 2025** : création (loi **?**), taux **?%** / **?%** sur le CA **?**, montant visé **?**/an, effort banques **?** → impact **CA / BPCE / CIC / BNP** → *(loi LF2025 art.48 · 20,6% / 41,2% · CA France · ~8 Md€ · ~1 Md€ · 280 M€ / 200 M€ / 78 M€ / « quelques M€ »)*
10. **La leçon de cours derrière** : `VL = VU + τ·D` → quand **τ monte** (surtaxe), le **tax shield** de la dette devient… *(relativement moins attractif en valeur après impôt pour les banques à CA local ; d'où l'arbitrage international)*
11. **Pourquoi une banque se value en P/BVPA et pas en PER ?** → *(actif = crédits, bénéfice volatil, on value le **book** tangible / le capital, pas le flux de bénéfices)*
12. **Le lien Capital Structure ↔ bilan d'une banque** : le « equity de base » d'une banque = **?** ; le relever = **?** → *(CET1 ; réduire le levier/le risque de distress — retour vers le Case III / le D\*)*

---

*MASTERCLASS IB — 2ᵉ lien, conçu avec les **résultats publiés** des 5 banques (FY2025, fév. 2026 ; BNP S1 2026, 18/09/2026 ; surtaxe IS loi LF2025). Le cours Skema 1 (`MASTERCLASS-ZERO-reprise-24-09-2h-de-lecture.md`) reste le socle théorique, inchangé. Généré le 23/09/2026.*
