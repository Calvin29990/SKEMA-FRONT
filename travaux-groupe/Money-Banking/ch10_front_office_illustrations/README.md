# Illustrations — Chapter 10, slides 9–10

Ce dossier rassemble **six illustrations candidates** pour les slides 9–10 du Chapter 10 — *The Banking Business*. Les quatre premières sont des schémas de mécanisme ; les deux dernières sont des graphiques de données. Elles sont conçues comme des visuels de présentation, et non comme de simples éléments décoratifs : chaque image relie un mécanisme financier à une question de banque, de front office ou de gestion des risques.

> **Statut :** options de travail à sélectionner avant la création du PowerPoint final. Le deck des slides 9–10 n’est pas encore généré.

## Vue d’ensemble

| Fichier | Sujet | Utilisation la plus naturelle |
|---|---|---|
| [01 — du subprime au crédit structuré](output/01_subprime_to_structured_credit.png) | Emprunteur → banque/originator → pool/SPV → tranches → investisseurs | Slide 9 : expliquer la chaîne de titrisation |
| [02 — cash-flow et loss waterfalls](output/02_cashflow_and_loss_waterfalls.png) | Priorité des paiements et ordre inverse d’absorption des pertes | Slide 9 : rendre le tranching et la waterfall concrets |
| [03 — cash-flows et protection d’un CDS](output/03_cds_cashflows_and_protection.png) | Prime, événement de crédit, recovery, LGD et paiement contingent | Slide 10 : transfert et couverture du risque de crédit |
| [04 — crise, stress de liquidité et réponse prudentielle](output/04_crisis_to_basel_timeline.png) | Faiblesse d’origination → complexité → levier → défauts → liquidité/contagion → Basel | Slide 10 : relier le front office à la crise et à la régulation |
| [05 — croissance du subprime : graphique combiné](output/05_subprime_growth_combo_chart.png) | Barres = volume annuel ; courbe = part des nouvelles origines hypothécaires | Slide 9 : montrer la croissance du marché sans schéma en cubes |
| [06 — cinq banques, spreads CDS et run de 2008](output/06_bank_cds_spreads_and_funding_stress.png) | Cinq lignes colorées, événements fléchés et niveaux clés de Goldman, Morgan Stanley, Merrill, Lehman et Bear | Slide 10 : relier pricing du risque, funding et choc Lehman |

Les six fichiers sont au format **16:9**, avec un style cohérent et une hiérarchie adaptée à une slide de cours : titre, mécanisme central ou série de données, exemple chiffré, puis une note de prudence en bas de page.

## 01 — From a subprime mortgage to structured credit

![Illustration 1 — du subprime au crédit structuré](output/01_subprime_to_structured_credit.png)

Cette illustration montre comment un prêt individuel devient une exposition structurée :

1. l’emprunteur présente un profil de crédit plus risqué ;
2. la banque accorde et peut gérer le prêt ;
3. les prêts sont regroupés dans un pool et associés à un SPV ;
4. le SPV émet des notes réparties en tranches ;
5. les investisseurs achètent des expositions différentes aux flux, au spread et au risque.

Le cartouche **“What ‘subprime’ means”** évite une simplification excessive : *subprime* désigne ici un profil de crédit plus risqué, et non une catégorie juridique universelle. L’explication utilise les notions de **PD** (*probability of default*) et de **LTV** (*loan-to-value*).

L’exemple pédagogique représente **100 mortgages = €100m**, répartis en **€80m senior, €15m mezzanine et €5m equity**. Les montants sont explicitement illustratifs et ne décrivent pas une transaction historique.

**Pourquoi elle est pertinente pour la slide 9 :** c’est le meilleur schéma d’introduction. Il relie l’origination bancaire, le financement, la structuration, la distribution et les différents mandats d’investisseurs en une seule chaîne.

## 02 — Waterfall: who gets paid, who absorbs the loss?

![Illustration 2 — cash-flow et loss waterfalls](output/02_cashflow_and_loss_waterfalls.png)

Cette illustration isole le point souvent le plus difficile à retenir :

- les **collections** sont distribuées selon la priorité contractuelle — senior, puis mezzanine, puis equity/residual ;
- les **pertes** frappent généralement les protections dans l’ordre inverse — equity, puis mezzanine, puis senior.

Les trois scénarios de **€4m, €7m et €22m de pertes** montrent concrètement quand l’equity est absorbée, quand la mezzanine commence à subir des pertes et quand la protection senior est atteinte.

**Pourquoi elle est pertinente pour la slide 9 :** elle transforme le vocabulaire *tranching*, *subordination* et *waterfall* en une logique immédiatement lisible. Elle rappelle également qu’une tranche senior n’est pas sans risque : elle est touchée plus tard dans cet exemple, mais reste exposée aux pertes extrêmes, à la liquidité et aux hypothèses de la structure.

## 03 — CDS: transferring credit risk without necessarily selling the asset

![Illustration 3 — CDS, prime et protection](output/03_cds_cashflows_and_protection.png)

Cette illustration présente un **Credit Default Swap comme un dérivé de crédit bilatéral** :

- l’acheteur de protection paie une prime périodique, exprimée par le **CDS spread** ;
- le vendeur de protection reçoit cette prime et prend une exposition contingente ;
- si un événement de crédit défini par le contrat survient, un paiement de protection est effectué selon les modalités prévues.

L’exemple pédagogique utilise :

- **€10m de notional** ;
- **250 bps par an**, soit **€250,000 de prime annuelle** ;
- **40 % de recovery**, donc **60 % de LGD** ;
- un paiement illustratif de **€6m** après l’événement de crédit.

Le schéma précise qu’un CDS n’est **pas automatiquement une police d’assurance** : il s’agit d’un dérivé dont la documentation définit notamment l’obligation de référence, les événements de crédit, le règlement, la contrepartie et les éventuelles obligations de collatéral.

**Pourquoi elle est pertinente pour la slide 10 :** elle prolonge la titrisation vers le hedging, le pricing et le monitoring de marché. Elle permet de parler du spread, de la recovery, du risque de contrepartie, du collatéral et de la liquidité sans prétendre que la banque vend nécessairement l’actif sous-jacent.

## 04 — From structured credit to systemic stress and regulation

![Illustration 4 — de la finance structurée à la régulation](output/04_crisis_to_basel_timeline.png)

Cette illustration propose une lecture prudente de la crise :

> faiblesse de l’origination → complexité RMBS/CDO → levier et hors-bilan → défauts et dégradations → margin calls et fire sales → stress de liquidité et contagion.

Elle ne présente **pas la titrisation comme la cause unique de 2008**. Le message est celui d’une combinaison d’incitations mal alignées, de standards de crédit, de levier, d’opacité, de dépendance aux ratings et de liquidité de marché.

La bande réglementaire met en regard **Basel I**, **Basel II**, **Basel III** et **“Basel IV”**. L’astérisque rappelle que **Basel IV est un surnom de marché désignant les réformes finales de Basel III, et non un accord officiel séparé**.

**Pourquoi elle est pertinente pour la slide 10 :** elle relie l’activité de structuration et de distribution aux conséquences de marché, au risque systémique et aux réponses prudentielles. C’est l’option la plus adaptée si la slide 10 doit faire le lien avec la crise de 2008 et la régulation contemporaine.

## 05 — Growth of subprime mortgage lending

![Illustration 5 — graphique combiné de la croissance du subprime](output/05_subprime_growth_combo_chart.png)

Ce graphique reprend la logique du modèle fourni :

- les **barres orange** montrent le volume annuel de nouvelles origines subprime, en **milliards de dollars** ;
- la **courbe bordeaux** montre la part des origines subprime dans l’ensemble des origines hypothécaires ;
- la zone jaune met en évidence l’accélération de **2004 à 2006**.

La série est volontairement limitée à **2001–2006**, période pour laquelle une définition homogène et une table chiffrée sont disponibles dans la source retenue. Les volumes sont : **$190bn, $231bn, $335bn, $540bn, $625bn et $600bn**. La part est calculée à partir de la même table : subprime / (subprime + Alt-A + jumbo + agency), soit environ **9.0 %, 8.3 %, 8.9 %, 20.8 %, 22.7 % et 23.8 %**.

Le graphique est plus simple à lire qu’un schéma de cubes : il montre immédiatement la **taille du marché**, son **accélération** et la **part croissante** du subprime. Il ne prétend pas démontrer à lui seul la causalité de la crise ; il donne l’échelle du phénomène et prépare ensuite l’explication de la titrisation, des incitations et du risque.

**Pourquoi elle est pertinente pour la slide 9 :** c’est désormais le visuel recommandé si l’objectif est de faire comprendre le boom du subprime avant d’expliquer la structuration. Il peut remplacer les illustrations 01–02, qui restent disponibles pour une slide plus technique.

**Source des données :** Ashcraft & Schuermann, *Understanding the Securitization of Subprime Mortgage Credit*, Federal Reserve Bank of New York Staff Report no. 318 (2008), Table 1 ; données d’origination Inside Mortgage Finance. Les parts sont calculées à partir de cette table, et non lues approximativement sur le graphique de référence.

## 06 — Five investment banks: CDS spreads and the 2008 run

![Illustration 6 — cinq banques d’investissement, spreads CDS et run de 2008](output/06_bank_cds_spreads_and_funding_stress.png)

Cette version est volontairement **zoomée sur cinq banques** et utilise cinq couleurs constantes : **Goldman Sachs, Morgan Stanley, Merrill Lynch, Lehman Brothers et Bear Stearns**.

Le graphique donne une vraie chronologie de marché :

- en janvier 2006, les cinq spreads sont proches de **21–25 bps** ; le marché différencie encore peu les banques ;
- en août 2007, après le run de Countrywide, Bear Stearns atteint **165 bps** ;
- le 14 mars 2008, Bear Stearns atteint **737 bps** et JPMorgan reprend la banque ; le spread de JPMorgan augmente de **32 bps** dans la fenêtre d’événement étudiée ;
- le 15 septembre 2008, Lehman dépose son bilan à **703 bps** ;
- le 17 septembre, Morgan Stanley atteint **909 bps**, Goldman Sachs **596 bps** et Merrill Lynch **530 bps** dans la table de référence.

Les flèches et les lignes verticales ne sont pas décoratives : elles relient chaque événement à un **niveau de spread observable**. L’échelle linéaire **0–1 000 bps** est choisie pour conserver à la fois la zone pré-crise et l’explosion de septembre 2008. Les lignes relient des dates publiées dans la table ; elles ne prétendent pas reconstituer chaque cotation quotidienne.

Le message Sales/Trading est le suivant : le risque devient d’abord **différencié** — Bear puis Lehman s’écartent — avant de devenir **systémique** après Lehman, lorsque Morgan Stanley, Goldman Sachs et Merrill Lynch repricent simultanément leur risque de crédit et de financement.

Un spread CDS est un **prix de protection de crédit**, pas automatiquement une probabilité de défaut. Le run est un événement de financement et de liquidité ; le CDS enregistre la revalorisation du risque et de la protection demandée par le marché.

**Source des données :** Flannery, Houston & Partnoy, *Credit Default Swap Spreads as Viable Substitutes for Credit Ratings*, University of Pennsylvania Law Review (2010), Table 2 ; données Markit. Les événements et variations autour de Bear Stearns, Lehman et JPMorgan sont décrits dans la même étude.

**Pourquoi elle est pertinente pour la slide 10 :** elle transforme la crise en une lecture de marché concrète : un desk observe le spread, la vitesse de widening, la comparaison entre noms, le risque de contrepartie et l’effet d’un sauvetage sur le pricing.

## Quelle combinaison retenir pour deux slides ?

Une sélection possible, à valider avant le PowerPoint :

- **Slide 9 — 05 :** commencer par le graphique combiné pour rendre le boom du subprime immédiatement lisible ; utiliser **01** ou **02** seulement si le texte doit ensuite détailler la chaîne de titrisation ou la waterfall.
- **Slide 10 — 06 :** retenir le graphique CDS si l’objectif est de montrer la revalorisation du risque, le run de Bear Stearns et le choc Lehman ; utiliser **03** si l’objectif est d’expliquer le contrat CDS lui-même, ou **04** si l’objectif est la régulation.

Si une seule illustration doit être retenue par slide :

| Slide | Choix recommandé | Raisonnement |
|---|---|---|
| 9 | **05** | Lecture immédiate de la croissance du volume et de la part de marché, sans schéma abstrait. |
| 10 | **06** | Le meilleur visuel pour relier risque de crédit, funding, contagion et crise de 2008. |

Les illustrations **01** et **02** restent utiles en réserve si la slide 9 doit aller plus loin dans la mécanique de la titrisation. L’illustration **03** reste la meilleure option si la slide 10 doit d’abord définir le fonctionnement contractuel d’un CDS.

## Précautions de contenu

- Tous les montants et paramètres chiffrés sont **pédagogiques/illustratifs**, pas des transactions historiques.
- La titrisation transforme et répartit le risque ; elle ne le fait pas disparaître.
- Une tranche senior bénéficie d’une protection relative dans la waterfall, mais n’est pas sans risque.
- Un CDS est présenté comme un dérivé de crédit, pas automatiquement comme une assurance.
- La crise de 2008 est présentée comme le résultat d’une combinaison de facteurs, et non de la titrisation seule.
- Les repères réglementaires doivent être recroisés avec l’édition exacte du cours et les sources retenues avant la version finale du deck.

## Sources de cadrage

- [Guide français des slides 9–10](../CH10-SLIDES-9-10-FRONT-OFFICE-FR.md)
- [Financial Crisis Inquiry Commission Report](https://www.govinfo.gov/content/pkg/GPO-FCIC/pdf/GPO-FCIC.pdf)
- [Federal Reserve History — The Great Recession and Its Aftermath](https://www.federalreservehistory.org/essays/great-recession-and-its-aftermath)
- [Flannery, Houston & Partnoy — CDS spreads and credit ratings](https://www.law.upenn.edu/live/files/22-flannery158upalrev20852010pdf)
- [Federal Reserve Bank of New York — Bear Stearns and Lehman context](https://www.newyorkfed.org/newsevents/speeches/2010/bax100901)
- [Basel Committee — Revisions to the Securitisation Framework](https://www.bis.org/bcbs/publ/d374.htm)
- [Basel Committee — Basel III: Post-Crisis Reforms](https://www.bis.org/bcbs/publ/d424.htm)

## Régénérer les PNG

Depuis la racine du dépôt, avec un environnement Python contenant `matplotlib` :

```bash
python travaux-groupe/Money-Banking/ch10_front_office_illustrations/build_illustrations.py
```

Le script régénère les six fichiers dans `output/`.
