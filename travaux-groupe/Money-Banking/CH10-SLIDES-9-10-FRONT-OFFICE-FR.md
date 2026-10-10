# Chapter 10 — Slides 9–10 expliquées en français
## Titrisation avec une approche Sales & Trading

**Cours :** Money, Banking and Financial Markets
**Chapitre :** 10 — *The Banking Business*
**Partie proposée :** slides 9–10
**Objectif :** comprendre la titrisation comme une activité bancaire, de structuration, de financement et de distribution de risque — sans transformer la présentation en cours de produits dérivés.

---

## 1. Où se situe ta partie dans le chapitre ?

La présentation peut suivre cette logique :

| Slides | Sujet | Question principale |
|---:|---|---|
| 1–2 | Introduction et bilan bancaire | Qu'est-ce qu'une banque et comment son bilan fonctionne-t-il ? |
| 3–4 | Actifs, passifs et création de revenus | Comment la banque gagne-t-elle de l'argent ? |
| 5–6 | Risque de liquidité et faillite bancaire | Pourquoi une banque solvable peut-elle manquer de liquidité ? |
| 7 | Risque de crédit et sélection adverse | Pourquoi certains emprunteurs sont-ils plus risqués que d'autres ? |
| 8 | Risque de taux d'intérêt | Que se passe-t-il quand les taux et la courbe changent ? |
| **9** | **Titrisation** | Comment les prêts bancaires deviennent-ils des instruments de marché ? |
| **10** | **Crise de 2008 et pertinence actuelle** | Comment le risque est-il transféré, conservé et contrôlé ? |

Ta partie doit donc servir de **pont entre le métier bancaire traditionnel et les marchés financiers**.

---

# Slide 9 — La titrisation : transformer le crédit bancaire en instrument de marché

## Idée centrale

Une banque accorde des prêts, regroupe ces prêts, puis utilise leurs flux futurs pour créer des titres destinés à des investisseurs.

La question de fond est :

> **Qui reçoit les flux, qui absorbe les pertes et quels risques restent chez la banque ?**

## Mécanisme à comprendre

```text
Emprunteurs
    ↓ remboursements
Banque : origination et gestion des prêts
    ↓ vente réelle ou transfert structuré
SPV : véhicule juridiquement séparé
    ↓ émission de titres
Tranches senior / mezzanine / equity
    ↓ waterfall des paiements
Investisseurs
```

## Les concepts à approfondir

### 1. Origination

La banque accorde un portefeuille de prêts à des ménages, des consommateurs ou des entreprises. Elle devient l'originator et peut aussi rester le servicer, c'est-à-dire gérer les remboursements et la relation administrative.

### 2. Pooling

Les prêts individuels sont regroupés dans un portefeuille. L'investisseur n'achète donc pas directement le risque d'un seul emprunteur, mais une exposition à un ensemble de prêts.

### 3. SPV — Special Purpose Vehicle

Le SPV est une entité juridiquement distincte qui détient les actifs ou référence leur risque et émet les titres. Il permet de séparer la structure de l'opération du bilan ordinaire de la banque, selon les règles juridiques et comptables applicables.

### 4. True sale et synthetic securitisation

- **True sale :** les actifs sont effectivement transférés au véhicule.
- **Synthetic securitisation :** les actifs restent en place, mais le risque de crédit est transféré par un contrat ou une structure financière.

Ne pas dire que ces deux structures ont exactement les mêmes effets comptables, juridiques ou prudentiels.

### 5. Tranching

Les flux et les pertes sont répartis selon une priorité :

| Tranche | Paiement | Absorption des pertes | Profil de l'investisseur |
|---|---|---|---|
| Senior | Première priorité | Dernière protection touchée | Risque et spread plus faibles |
| Mezzanine | Après la senior | Avant l'equity | Risque et spread intermédiaires |
| Equity / residual | Dernière priorité | Première perte absorbée | Risque élevé et rendement résiduel potentiel |

Une tranche senior n'est pas sans risque : elle bénéficie d'une protection relative, mais reste exposée aux pertes extrêmes, à la liquidité et aux hypothèses du modèle.

### 6. Waterfall

Les remboursements sont distribués selon une cascade contractuelle :

```text
Collections des emprunteurs
    ↓
Senior investors
    ↓
Mezzanine investors
    ↓
Equity / residual investors
```

Les pertes suivent généralement l'ordre inverse : l'equity absorbe d'abord les pertes, puis la mezzanine, puis la senior.

### 7. Credit enhancement

Selon la structure, la protection peut utiliser :

- subordination ;
- overcollateralisation ;
- excess spread ;
- reserve accounts ;
- liquidity facilities ;
- garanties ou mécanismes de protection.

## Phrase à retenir pour la slide 9

> **La titrisation ne fait pas disparaître le risque de crédit : elle le transforme, le répartit et le revalorise entre plusieurs entités, tranches et investisseurs.**

---

# Slide 10 — Vision front office : structuration, pricing, distribution et risque

## Ce qu'un Sales regarde

Le Sales ne se limite pas à vendre un produit. Il doit comprendre si la tranche correspond au mandat et au profil de risque de l'investisseur.

Questions principales :

- Quel investisseur peut acheter cette tranche ?
- Quel rendement, spread, rating et niveau de liquidité recherche-t-il ?
- Les risques de défaut, de prépaiement et de taux sont-ils compréhensibles ?
- Le produit respecte-t-il les limites et la politique d'investissement du client ?
- Comment expliquer clairement la waterfall et la première perte ?

## Ce qu'un Trader / Markets regarde

Le Trader ou le professionnel de marchés surveille :

- le risque de spread de crédit et le mark-to-market ;
- la sensibilité aux taux et à la duration ;
- le risque de prépaiement ou d'extension ;
- le risque de liquidité et le bid-ask spread ;
- le coût de couverture ;
- l'inventaire détenu par le desk ;
- le risque de modèle et les hypothèses de cash flows ;
- la corrélation entre les défauts du portefeuille.

## Cycle d'une opération

```text
1. Origination
2. Sélection du portefeuille et due diligence
3. Structuration du SPV et des tranches
4. Credit enhancement et documentation
5. Pricing et distribution aux investisseurs
6. Servicing, monitoring et hedging
```

## Variables financières importantes

- **PD — Probability of Default :** probabilité de défaut ;
- **LGD — Loss Given Default :** perte en cas de défaut ;
- **EAD — Exposure at Default :** exposition au moment du défaut ;
- **Expected Loss :** approximation PD × LGD × EAD ;
- **WAL — Weighted Average Life :** durée moyenne pondérée des flux ;
- **Credit spread :** rémunération du risque de crédit ;
- **Duration :** sensibilité aux mouvements de taux ;
- **Prepayment risk :** remboursement anticipé ;
- **Liquidity risk :** difficulté à revendre au prix théorique ;
- **Model risk :** risque que les hypothèses de défaut, de corrélation ou de remboursement soient mauvaises.

## Le lien avec la crise de 2008

Il ne faut pas dire que la titrisation seule a causé la crise. Le problème venait de la combinaison de plusieurs facteurs :

- standards de crédit insuffisants ;
- structures complexes et opaques ;
- levier excessif ;
- confiance excessive dans les ratings ;
- incitations mal alignées entre originator, arranger, distributeur et investisseur ;
- corrélation des défauts sous-estimée ;
- dépendance à la liquidité de marché.

## Pertinence contemporaine

La question reste actuelle pour les banques :

- Le risque est-il véritablement transféré ou seulement transformé ?
- Quelle exposition reste chez l'originator ?
- Les investisseurs comprennent-ils les cash flows et la waterfall ?
- Les exigences de capital, de liquidité et de stress testing sont-elles suffisantes ?
- Les intérêts de l'originator, du Sales, du Trader et de l'investisseur sont-ils alignés ?

## Phrase à retenir pour la slide 10

> **Pour le front office, la titrisation n'est pas seulement une technique de financement : c'est un exercice de structuration, de pricing, de distribution et de gouvernance du risque.**

---

## 2. Ce qu'il faut approfondir avant de créer les slides

Priorité 1 — comprendre parfaitement :

1. SPV ;
2. true sale versus synthetic securitisation ;
3. senior, mezzanine et equity ;
4. waterfall des flux et des pertes ;
5. credit enhancement ;
6. risques conservés par la banque ;
7. rôle respectif du Sales et du Trader.

Priorité 2 — ajouter une seule phrase sur 2008 : la titrisation a amplifié certains risques lorsqu'elle était combinée à un mauvais underwriting, au levier, à l'opacité et à une mauvaise gestion de la liquidité.

Priorité 3 — ne pas ajouter Hull pour l'instant. L'angle front office est déjà suffisamment riche et reste davantage connecté au chapitre 10.

---

## 3. Sources à vérifier

1. **Livre du cours :** *Money, Banking and International Finance*, Chapter 10 — *The Banking Business*. Ajouter les pages exactes après vérification dans le PDF du cours.
2. [Financial Crisis Inquiry Commission Report](https://www.govinfo.gov/content/pkg/GPO-FCIC/pdf/GPO-FCIC.pdf)
3. [Federal Reserve History — The Great Recession and Its Aftermath](https://www.federalreservehistory.org/essays/great-recession-and-its-aftermath)
4. [Basel Committee — Revisions to the Securitisation Framework](https://www.bis.org/bcbs/publ/d374.htm)
5. [Basel Committee — Basel III: Post-Crisis Reforms](https://www.bis.org/bcbs/publ/d424.htm)

**Source footer possible :**

> Sources: Assigned textbook, Chapter 10; Financial Crisis Inquiry Commission; Federal Reserve History; Basel Committee on Banking Supervision. Accessed 10 October 2026.
