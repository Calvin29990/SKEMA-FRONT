# GUIDE MO — CE QUE JE DOIS SAVOIR
## Construit à partir des 3 documents EdR : Final Terms EMTN · Rapport annuel 2025 · Pilier III 2025

**But :** transformer trois PDF réglementaires en arme d'entretien. Tu ne récites pas ces documents — tu en tires **10 faits que personne d'autre ne connaîtra**, et tu les places en une phrase.
**Format des réponses :** 1 minute maximum, 3 phrases.

---

## 0. Carte d'identité des trois sources

| Doc | Ce que c'est vraiment | Ce que tu en tires |
|---|---|---|
| **`Titre.pdf`** | **Un vrai Final Terms** : EMTN indiciel émis par Edmond de Rothschild (France) le 29/09/2026, 8,695 M€, Euro Stoxx 50 | **L'anatomie exacte d'un structuré maison** — ton meilleur atout |
| **`edr-france-rapport-annuel-2025-fr.pdf`** (278 p.) | Le rapport financier annuel d'**EdR France** (entité bancaire, pas le groupe) | Les chiffres France, l'organisation des métiers, le rôle des EMTN dans le financement |
| **`edr-france-pilier-iii-2025-fr.pdf`** (64 p.) | Les informations prudentielles Bâle III d'**EdR France** | Les ratios, les limites de marché, le dispositif incidents — le vocabulaire du contrôle |

> ⚠️ **Piège n°1 :** ces trois documents parlent d'**Edmond de Rothschild (France)**, l'entité bancaire parisienne. **Pas** du groupe (198 Md CHF) ni d'EdR AM (107 Md€). Ne mélange jamais les deux jeux de chiffres.

---

## 1. Le poste MO : qui fait quoi chez EdR France (tiré des docs)

Les documents nomment les acteurs réels. C'est ça, « connaître la maison ».

| Acteur (nom exact dans les docs) | Son rôle |
|---|---|
| **L'Ingénierie financière / équipe de montage** | Monte les structurés : choisit le sous-jacent, la formule, les barrières, le coupon |
| **La Direction des Marchés de Capitaux / table d'exécution** | Couvre et place : desks trésorerie euro, devises, change |
| **La Direction Centrale des Risques — « Contrôle des risques pour compte propre »** | Contrôle des limites, **strictement indépendant du front office** ; prépare le dossier mensuel du Comité des Risques Financiers |
| **Financière Boréale** (filiale) | **Se porte contrepartie des cessions de la clientèle** quand un client sort avant l'échéance — c'est le marché secondaire interne |
| **Le Directoire** | Fixe les limites (ratifiées par le **Conseil de Surveillance**) ; alerté de tout incident grave |
| **Le Comité des Risques Financiers** | Mensuel : Directeur Général, Direction des risques, Salle des Marchés, Trésorerie, Engagements, un représentant d'EdR AM |
| **Toi (MO)** | Entre le montage et le règlement : prix, grecs, booking, cycle de vie, doc |

**Trois phrases à retenir sur le dispositif :**
1. Les limites sont fixées par le **Directoire** et ratifiées par le **Conseil de surveillance**.
2. Elles s'expriment en **montant absolu de portage**, en **sensibilité** ou en **stop loss**.
3. **Tout incident est déclaré sans seuil de montant** — même sans impact financier, s'il aurait pu en avoir.

> La dernière est une pépite : en entretien, ça devient « j'ai noté que chez vous, la déclaration d'incident se fait sans seuil de montant, y compris sans impact financier. C'est exactement la culture qu'on attend d'un middle office. »

---

## 2. ⭐ L'ARME : l'anatomie du vrai EMTN EdR (Final Terms du 29/09/2026)

### La fiche technique, telle qu'elle est écrite dans le document

| Élément | Valeur |
|---|---|
| **Émetteur** | **Edmond de Rothschild (France)** — LEI 9695002JOWSRCLLLNY11 |
| **Programme** | **EMTN de 850 M€**, prospectus de base du 24/04/2026 + supplément du 26/05/2026 |
| **Série / tranche** | 4434EEUR001A / 1 |
| **Montant** | **8 695 000 €** (nominal unitaire **1 000 €**) |
| **Prix d'émission** | **100 %** du nominal |
| **Dates** | Trade 01/09/2026 · Émission 29/09/2026 · **Échéance 29/09/2032** (6 ans max) |
| **Sous-jacent** | **EURO STOXX 50®** (SX5E, STOXX Ltd, EUREX, cours de clôture) |
| **Coupon** | **5,20 % par an**, « Common Memory Digital/Performance Interest » |
| **Barrière coupon (IB)** | **80 %** du niveau initial, avec **effet mémoire** |
| **Rappel automatique** | Si performance **≥ 100 %** aux dates annuelles (01/09/2027 → 01/09/2031) |
| **Protection du capital** | **Barrière à 50 %** du niveau initial, à l'échéance seulement |
| **Commission de placement** | **Maximum 2,00 %** du montant |
| **ISIN / cotation** | XS3498806879 · **Luxembourg Stock Exchange** |
| **Notation** | **Non noté** · Éligibilité Eurosystem : non |
| **Agent de calcul** | **L'émetteur lui-même** — Edmond de Rothschild (France) |
| **Signature** | Fabrice Coille, P/O Kristina Yordanova |

### Ce que ça veut dire en français (ta phrase d'entretien)

> « Un autocall annuel sur l'Euro Stoxx 50 : le client touche **5,20 % par an avec mémoire** tant que l'indice reste au-dessus de **80 %** de son niveau initial, le produit est **rappelé** dès qu'il revient à 100 %, et à l'échéance le capital est protégé **jusqu'à −50 %**, en dessous de quoi il subit la baisse. »

### Les 4 détails qui te distinguent (à placer, un seul à la fois)

1. **Le coupon est un digital à mémoire** : si la barrière de 80 % n'est pas respectée une année, le coupon est perdu **cette année-là** mais rattrapé plus tard. D'où la somme des taux dans la formule du Final Terms.
2. **L'agent de calcul est l'émetteur lui-même.** Il calcule son propre produit — c'est exactement pour ça qu'un contrôle indépendant du prix et des paramètres existe en interne.
3. **La commission de placement est plafonnée à 2 %** et elle est écrite noir sur blanc. C'est la matérialisation de ce que le client paie au-delà de la valeur économique.
4. **Le produit est non noté et pas éligible Eurosystem** : le risque est donc celui de la banque émettrice, pas celui d'un tiers noté.

### Et le point de contrôle MO sur ce produit précis
> Les 5 dates d'observation du rappel, les 6 dates de paiement de coupon, la barrière coupon à 80 %, la barrière de protection à 50 % observée **une seule fois à l'échéance**, et la convention **Modified Following** avec 8 jours ouvrés maximum de disruption : voilà la liste de ce qu'un MO vérifie sur ce seul term sheet.

---

## 3. Les 12 chiffres EdR France 2025 (≠ groupe)

| Indicateur | 2025 | 2024 |
|---|---|---|
| **Produit net bancaire** | **372,6 M€** | 383,3 M€ (−2,8 %) |
| **Frais de gestion** | 337,9 M€ (+4,8 %) | 322,6 M€ |
| **Résultat brut d'exploitation** | **35,6 M€** | 61 M€ |
| **Résultat net** | **24 M€** | 59 M€ |
| **Total de bilan** | 4 416 M€ | 4 249 M€ |
| **Capitaux propres (part du groupe)** | 372 M€ | 390 M€ |
| **Encours sous gestion** | **53,4 Md€** | — |
| **Crédits / dépôts clientèle** | 1 539 / 1 254 M€ | 1 271 / 1 054 M€ |
| **Ratio CET1** | **15,55 %** | 17,36 % |
| **Ratio de fonds propres totaux** | **16,63 %** | 18,61 % |
| **LCR / NSFR** | **209,2 % / 130,8 %** | 314,3 % / 133,4 % |
| **RWA / Effectif moyen** | 1 831 M€ / **825** | 1 583 M€ / 800 |

**Le commentaire qui montre que tu comprends :**
> « Le produit net bancaire est quasi stable mais le résultat net divise par deux : les frais de gestion augmentent de près de 5 % alors que les revenus reculent. Et le CET1 passe de 17,4 % à 15,6 %, sous l'effet de la hausse des actifs pondérés. »

### ⭐ Le fait que presque personne ne connaît
Dans le rapport annuel : **« les dettes représentées par un titre s'élèvent à 954 M€ et comprennent essentiellement des EMTN émis dans le cadre de l'activité de produits structurés. »**

> **Traduction : chez EdR France, les structurés ne sont pas seulement un produit de placement — c'est aussi une source de financement de la banque.** Et le Pilier III confirme qu'ils sont comptés dans les ressources longues qui financent les emplois courts.

---

## 4. Pilier III — le vocabulaire du contrôle (à connaître avant l'entretien)

| Notion | Ce que dit le document |
|---|---|
| **Limites de marché** | Fixées par le **Directoire**, ratifiées par le **Conseil de surveillance**. Trois formes : montant absolu de portage (change), sensibilité (taux, FX), **stop loss** (perte cumulée quotidienne) |
| **Utilisation des limites** | **7,1 % en moyenne** — donc très peu de risque de marché porté |
| **Risque des structurés** | *« Les activités de montage de produits structurés n'induisent pas de risques de marché significatifs »* : le swap est **adossé** au produit vendu ou à l'OPCVM |
| **Où est le vrai risque ?** | Dans l'**adossement** (écarts en période de lancement de fonds à formules), le **marché secondaire**, et surtout le **risque opérationnel** |
| **Risque opérationnel** | Approche **standard**, **59,3 M€** de fonds propres immobilisés ; tolérance définie comme **« Moyenne »**, déclinée en 8 sous-types |
| **Incidents** | **Déclarés sans seuil de montant**, y compris sans impact financier ; remontée au **Directoire** si grave ; comptes d'erreurs dédiés et provisions associées |
| **Comité des Risques Financiers** | Mensuel, avec le DG, la Direction des risques, la Salle des Marchés, la Trésorerie, les Engagements et un représentant d'EdR AM |

**La phrase qui relie tout ça à ton poste :**
> « Puisque le montage est adossé, le risque de marché est faible et le vrai enjeu devient le risque opérationnel : un booking faux, une date de constatation ratée ou un prix mal contrôlé coûtent plus cher qu'un mouvement de marché. C'est précisément le périmètre du middle office. »

---

## 5. Checklist — ce que je dois savoir (3 niveaux)

**Niveau 1 — je dois pouvoir le dire sans hésiter (12 points)**
- [ ] EdR France = banque, filiale à 100 % d'EdR Suisse, régulée ACPR.
- [ ] Le programme EMTN d'EdR France = **850 M€**.
- [ ] Un structuré maison = nominal 1 000 €, prix d'émission 100 %, commission de placement ≤ 2 %.
- [ ] Le produit du Final Terms : **Euro Stoxx 50, 5,20 %/an, coupon à mémoire, barrière coupon 80 %, autocall à 100 %, protection à 50 %, 6 ans**.
- [ ] L'**agent de calcul est l'émetteur** — d'où le contrôle indépendant.
- [ ] **Deux chiffres de résultat** : PNB 372,6 M€, résultat net 24 M€.
- [ ] **Deux ratios** : CET1 15,55 %, LCR 209 %.
- [ ] Les EMTN structurés = **954 M€** de dettes représentées par un titre → source de financement.
- [ ] Les limites sont fixées par le **Directoire**, ratifiées par le **Conseil de surveillance**.
- [ ] Les incidents se déclarent **sans seuil de montant**.
- [ ] Le risque de marché des structurés est **faible car adossé** → le risque réel est **opérationnel**.
- [ ] Financière Boréale = contrepartie du **marché secondaire**.

**Niveau 2 — utile (8 points)**
- [ ] Le prospectus de base date du **24/04/2026**, avec un supplément du **26/05/2026**.
- [ ] Cotation **Luxembourg**, ISIN XS3498806879, **non noté**, non éligible Eurosystem.
- [ ] Convention **Modified Following**, 8 jours ouvrés maximum de disruption.
- [ ] Target market MiFID : retail + professionnels + contreparties éligibles.
- [ ] Interdiction de vente aux investisseurs de détail **britanniques**.
- [ ] Tolérance au risque opérationnel : **« Moyenne »**, approche standard, 59,3 M€.
- [ ] Comité des Risques Financiers **mensuel**.
- [ ] Encours sous gestion EdR France : **53,4 Md€** (≠ 107 Md€ du groupe en AM).

**Niveau 3 — inutile pour cet entretien**
Les notes annexes, la durabilité ESRS, les détails du pilier III sur le risque de crédit, l'historique de la famille avant 1953.

---

## 6. Questions types — réponses calibrées **1 minute max**

### Q1. « Vous avez regardé nos documents ? » ⏱ 55 s
> « Oui, j'ai lu votre rapport annuel 2025 et un Final Terms d'EMTN d'octobre.
> Ce qui m'a marqué dans le rapport, c'est que les EMTN émis au titre des produits structurés représentent l'essentiel des 954 millions d'euros de dettes représentées par un titre : chez vous, les structurés sont aussi une source de financement.
> Et le Pilier III précise que le montage n'induit pas de risque de marché significatif parce que le swap est adossé — donc le vrai risque devient opérationnel, ce qui est exactement le périmètre du middle office. »

### Q2. « Décrivez-moi un de nos produits. » ⏱ 60 s
> « J'ai pris un EMTN indiciel émis en septembre 2026, série 4434, sur l'Euro Stoxx 50, six ans maximum, nominal 1 000 euros et prix d'émission à 100 %.
> Le client touche 5,20 % par an avec effet mémoire tant que l'indice reste au-dessus de 80 % de son niveau initial, et le produit est rappelé automatiquement dès qu'il revient à 100 %, à chaque date annuelle.
> À l'échéance, le capital est protégé jusqu'à 50 % ; en dessous, le client subit la baisse. »

### Q3. « Et quel est le point de vigilance pour vous sur ce produit ? » ⏱ 55 s
> « Il y en a trois, et ils sont dans le document.
> L'agent de calcul est l'émetteur lui-même, donc le contrôle indépendant du prix et des paramètres n'est pas une option.
> La commission de placement est plafonnée à 2 %, donc la marge est explicite et doit être justifiée.
> Et les barrières n'ont pas la même nature : 80 % pour le coupon, observée chaque année, contre 50 % pour le capital, observée une seule fois à l'échéance — une confusion entre les deux change complètement le risque. »

### Q4. « Pourquoi le middle office est-il important chez nous ? » ⏱ 55 s
> « Parce que vos structurés sont adossés : le swap est calé sur le produit vendu, donc le risque de marché est faible et l'essentiel du risque devient opérationnel.
> Or le Pilier III indique que tout incident doit être déclaré sans seuil de montant, même sans impact financier — c'est une culture qui met la détection au centre.
> Dans ce cadre, le middle office est la fonction qui garantit que le prix, les dates de constatation et les flux sont justes, avant que l'erreur ne devienne un incident. »

### Q5. « Quels sont nos ratios ? » ⏱ 45 s
> « À fin 2025, un CET1 de 15,55 %, un ratio de fonds propres totaux de 16,63 % pour des exigences très inférieures, un LCR de 209 % et un NSFR de 131 %.
> Sur des actifs pondérés de 1,83 milliard d'euros.
> Le CET1 a baissé parce que les RWA ont augmenté plus vite que les fonds propres. »

### Q6. « Comment se porte Edmond de Rothschild France ? » ⏱ 55 s
> « Un produit net bancaire de 372,6 millions d'euros, en léger recul de 2,8 %, et un résultat net de 24 millions, contre 59 millions l'an dernier.
> L'explication est simple : les frais de gestion ont augmenté de 4,8 % alors que les revenus baissaient.
> Donc un bilan solide mais une marge sous pression — ce qui rend la maîtrise des coûts et la qualité opérationnelle d'autant plus importantes. »

### Q7. « Qui fixe les limites de risque ? » ⏱ 40 s
> « Le Directoire les accorde et le Conseil de surveillance les ratifie.
> Elles s'expriment en montant absolu de portage, en sensibilité ou en stop loss, et leur respect est vérifié en permanence par le front et par le Contrôle des risques pour compte propre, qui est indépendant du front.
> Le taux d'utilisation moyen ressort à 7,1 %. »

### Q8. « Qu'est-ce qu'un incident pour vous ? » ⏱ 50 s
> « Chez vous, la définition est large : tout dysfonctionnement est déclaré, sans seuil de montant, même s'il n'a pas eu d'impact financier mais qu'il aurait pu en avoir.
> C'est la bonne approche, parce que les incidents les plus coûteux sont souvent ceux qui se répètent à faible coût sans être signalés.
> Concrètement, dans mon périmètre, un break non documenté est un incident. »

### Q9. « Que fait l'ingénierie financière ? » ⏱ 45 s
> « Elle monte le produit : choix du sous-jacent, formule, barrières, coupon, puis le calage avec la couverture.
> La table d'exécution et la trésorerie assurent la contrepartie et le financement, et Financière Boréale se porte contrepartie quand un client sort avant l'échéance.
> Le middle office intervient entre les deux : il vérifie que ce qui a été monté est bien ce qui est booké et valorisé. »

### Q10. « Pourquoi un EMTN plutôt qu'un fonds ? » ⏱ 50 s
> « Parce que l'EMTN est un titre de créance émis par la banque : le client est exposé au risque de crédit de l'émetteur, pas à un portefeuille mis de côté.
> En contrepartie, la formule est contractualisée dès le départ : barrières, dates, coupon.
> Et pour la banque, c'est aussi un refinancement, puisqu'une partie de ces émissions figure en ressources longues au bilan. »

### Q11. « Quelle différence entre EdR et EdR France ? » ⏱ 45 s
> « EdR France est l'entité bancaire parisienne, filiale à 100 % de la banque suisse, régulée par l'ACPR : c'est elle qui émet ces EMTN.
> Le groupe, basé à Genève, gère 198 milliards de francs d'encours, et la société de gestion en gère 107 milliards d'euros.
> Donc quand on parle de résultats, il faut toujours préciser de quelle entité on parle : 24 millions de résultat net pour EdR France, 73 millions de francs pour le groupe. »

### Q12. « Une question pour nous ? » ⏱ 40 s
> « Oui : sur ce type d'EMTN à barrière coupon de 80 % et protection à 50 %, comment est organisé le contrôle des paramètres entre le modèle interne et un contributeur externe ?
> Et est-ce que l'agent de calcul interne change quelque chose à la façon dont vous documentez les constatations ? »

---

## 7. Les 3 phrases à placer, et les 2 pièges

**À placer (une seule fois chacune, jamais deux dans la même réponse) :**
> « J'ai lu un de vos Final Terms : 5,20 % avec mémoire, barrière coupon à 80 %, rappel à 100 %, protection à 50 % sur l'Euro Stoxx 50. »

> « Ce qui m'a frappé, c'est que les EMTN structurés représentent l'essentiel des 954 millions de dettes représentées par un titre : c'est aussi du financement pour la banque. »

> « Comme le montage est adossé, le risque de marché est faible — donc le vrai risque est opérationnel, et c'est là que le middle office compte. »

**Les 2 pièges :**
1. **Ne cite pas les chiffres du groupe en croyant citer ceux d'EdR France.** 198 Md CHF / 73 M CHF = groupe. 372,6 M€ / 24 M€ = EdR France. Une confusion ici annule l'effet de tout le reste.
2. **Ne récite pas le Final Terms ligne par ligne.** Un seul produit, trois chiffres, une conclusion. Si tu récites, tu retombes dans « trop long ».

---

## Sources (pages des documents, pour recouper)

- **`Titre.pdf`** — Final Terms du 29/09/2026 : p. 2 (émetteur, programme 850 M€, montant, nominal), p. 3 (dates, paiements), p. 4-5 (coupon 5,20 %, barrière 80 %, mémoire), p. 6-8 (autocall 100 %, protection 50 %), p. 9 (Euro Stoxx 50, SX5E), p. 11 (agent de calcul = émetteur), p. 12 (Luxembourg, non noté), p. 13 (commission 2 %, ISIN).
- **Rapport annuel 2025** — p. 9 (chiffres clés, ratios), p. 12 (PNB, frais), p. 32 (EMTN et dettes représentées par un titre), p. 215 (secteurs opérationnels), p. 228 (activités génératrices de risque de marché, adossement, Financière Boréale), p. 229 (limites, contrôle des risques pour compte propre).
- **Pilier III 2025** — p. 4 (encours 53,4 Md€), p. 5-6 (CET1 15,55 %, RWA, LCR, NSFR), p. 37 (limites de marché, Comité des Risques Financiers, utilisation 7,1 %), p. 38-39 (risque opérationnel, 59,3 M€, tolérance « Moyenne », déclaration des incidents).
