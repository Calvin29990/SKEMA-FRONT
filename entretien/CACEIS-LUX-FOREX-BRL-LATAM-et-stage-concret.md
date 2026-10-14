# LE DUR — CACEIS LUXEMBOURG, LE FOREX, LE BRL/LATAM ET LE STAGE CONCRET
## Qui traite quoi, ce que fait vraiment le stagiaire, et ce que l'école peut te donner

> **Créé le 14/10/2026** · Complète `CACEIS-LUX-FOREX-deep-dive.md` (le desk), `CACEIS-LUX-ENTRETIEN-PREPA-pitch-questions-chiffres.md` (les questions) et `CACEIS-LUX-PLAN-CARRIERE-3-5-ANS.md` (le plan)

---

## 1. LA RÉPONSE COURTE À TA QUESTION

**« Le BRL, c'est le desk ou le middle qui s'en occupe ? » → Les deux, mais pas au même moment, et les deux sont à Luxembourg.**

| Étape | Qui | Où |
|---|---|---|
| **Prix, négociation, exécution** du NDF BRL | **Le desk** — Market Solutions sales + traders | **Luxembourg** (salle des marchés du groupe, qui sert toutes les entités CACEIS) |
| **Capture, contrôle, confirmation, cut-off, fixing, règlement du différentiel, réconciliation, litiges** | **Le middle/back office de la salle** — **c'est là que tu serais stagiaire** | **Luxembourg** |
| **Conservation locale des actifs brésiliens, administration** | **Santander CACEIS Brasil** (São Paulo) — ⚠️ **en cours de cession à State Street** | **Brésil** |

**Donc : le Brésil ne traite pas ton FX. Il ne s'occupe que de la conservation locale.** Le change BRL pour les clients européens se **quote et se dénoue à Luxembourg** — et c'est précisément pour ça que l'offre 116280 (« suivi des contreparties et sous-dépositaires en cas de non-réception de fonds en bonne date valeur ») est intéressante : tu es au point où les deux mondes se rencontrent.

---

## 2. LA CHAÎNE FX DE CACEIS LUXEMBOURG (qui fait quoi)

**Le point de départ** — la page « Fx solutions » de CACEIS :
> « The CACEIS group trading room offers competitive advantages for managers and middle-back office teams : **processing of all convertible currencies** ; **hedging via NDF and NDS on non-convertible currencies** ; **extended cut-offs on all currencies** ; **full STP system (no payment instructions are necessary)** and our **audit trail guarantees price traceability** ; no additional fees or settlement fees. Large range of products: **Spot, Forward, SWAP, Non-Deliverable Forwards or Options**. Online Forex trading platform available through **FX-ALL, Bloomberg and 360T**. »

### Lis bien la phrase en italique — elle définit ton futur poste
> **« full STP system (no payment instructions are necessary) »**

**Traduction** : chez CACEIS, la chaîne est **automatisée de bout en bout**. Les instructions partent du desk, sont intégrées, contrôlées et payées sans que personne ne ressaisisse un paiement.

**➜ Donc le travail humain du middle office, c'est exactement tout ce qui ne passe pas tout seul** :
- les **exceptions** (un trade mal capturé, un taux incohérent, une date de valeur impossible) ;
- les **cut-offs** (heure limite : au-delà, la date de valeur glisse d'un jour → impact cash et intérêts pour le fonds) ;
- les **confirmations et rapprochements** avec les contreparties ;
- les **fonds qui n'arrivent pas** en bonne date de valeur (le cœur de la fiche de poste) ;
- les **spécificités produit** que le STP ne gère pas nativement — **et le NDF est le cas d'école**.

### Les acteurs de la chaîne

| Acteur | Rôle |
|---|---|
| **Sales (Market Solutions)** | Reçoit le besoin du gérant, cote, négocie. *Vincenzo Ricco dirige les ventes FX de la branche LU* |
| **Traders (dealing room)** | Exécutent et couvrent. *Aurélien Sauvage : « daily flow trading on all deliverable currencies »* — et le desk couvre aussi les **non-livrables**, d'où le NDF |
| **Middle office / back office de la salle** | Capture, contrôle, confirmations, cut-offs, paiements, réconciliation, investigations. **Ton futur poste** |
| **Correspondants cash** | Banques par lesquelles transitent les flux dans les devises que CACEIS ne tient pas en compte propre |
| **CLS** | Système de règlement **paiement contre paiement** (élimine le risque de principal) — **uniquement pour un panier de devises livrables.** Un NDF, par construction, **n'y passe pas** : il n'y a pas de livraison |
| **Sous-dépositaires locaux** | Conservation dans les marchés locaux (ex. Brésil) |
| **Plateformes** | **FX-All, Bloomberg, 360T** |
| **Clients** | Gérants de fonds (le cœur), institutionnels, banques, corporates, banques privées |

**Le flux type d'une demande client** : le gérant a un besoin (souscription en devise, achat de titres en devise, dividende/coupon à convertir, couverture d'une exposition) → le desk cote → exécution → **le middle/back office contrôle et dénoue** → rapport au client.

---

## 3. FOCUS BRL / LATAM — LA MÉCANIQUE COMPLÈTE

### 3.1 Pourquoi le Brésil est un cas à part (et passionnant)

Le Brésil est **l'un des marchés où l'accès au change comptant est le plus fermé, et où les instruments non livrables sont les plus ouverts**. C'est un renversement total par rapport à l'Europe.

- **Accès onshore restreint** : la réglementation brésilienne **limite les entités autorisées à traiter des instruments livrables** (spot, forwards, swaps FX) **sans intérêt économique sous-jacent**. Le registre des opérations passe par les systèmes de la **Banco Central do Brasil (BCB)**, et les opérations de change sont soumises à l'**IOF** (impôt sur les opérations financières).
- **Accès offshore ouvert** : il n'y a **pas de limitation significative à l'usage d'instruments de couverture non livrables**. C'est pour ça que **le NDF est l'outil de référence** — pas un pis-aller.

**➜ À en tirer en entretien** : *« Le Brésil est un cas unique : le comptant est fermé, le non-livrable est ouvert. Donc quand un fonds européen veut couvrir du BRL, l'instrument naturel n'est pas le forward livrable, c'est le NDF — et ça change tout le post-trade. »* Cette phrase-là, très peu de candidats peuvent la dire.

### 3.2 Le PTAX — le taux qui déclenche tout

- **PTAX** = le **taux de référence officiel publié par la Banco Central do Brasil**, calculé à partir des transactions interbancaires.
- Il est publié **une fois par jour**, autour de **13h15 heure de São Paulo** (depuis la réforme de 2011 — avant, c'était ~18h).
- Le BCB publie un **bid** et un **ask** en appliquant un écart de **0,0004** autour du point milieu.
- **C'est la base de règlement de la quasi-totalité des contrats dérivés sur le BRL** — y compris les NDF négociés hors du Brésil.

### 3.3 Le NDF BRL, étape par étape

| Étape | Ce qui se passe | Qui, chez CACEIS |
|---|---|---|
| **1. Trade** | Un client veut se couvrir sur le BRL (ou prendre une exposition) → le desk cote un **NDF USD/BRL** : montant notionnel, taux, **date de fixing**, **date de règlement** | **Desk (LU)** |
| **2. Confirmation** | Les deux parties confirment les termes (standard **EMTA** pour les NDF ; la source de règlement type est le **« BRL PTAX Offer Rate » — code BRL09**, exprimé en BRL par USD, pour un règlement à **deux jours ouvrés brésiliens**) | **Middle office (LU)** — capture et contrôle |
| **3. Fixing** | À la date de fixing, on relève le **PTAX** du jour. **Aucune devise n'est livrée** — c'est une donnée, pas un transfert | **Middle office** — c'est là que le contrôle est critique |
| **4. Calcul du différentiel** | Écart entre le taux du trade et le fixing, appliqué au notionnel → **un montant en USD** | **Middle office** |
| **5. Règlement** | **Seul le différentiel en USD est payé** (un seul flux, dans une devise livrable) — **pas de principal, pas de CLS, pas d'instruction dans une devise exotique** | **Middle office + correspondants** |
| **6. Contrôle final** | Rapprochement du paiement, réconciliation, archivage du taux utilisé, audit trail du prix | **Middle office** |
| **7. Cas d'école** | **Le fixing n'est pas publié** (jour férié brésilien), **le paiement USD n'arrive pas**, **la contrepartie conteste le taux** → on enquête, on relance, on documente | **Toi, le stagiaire** |

**Les trois choses que le NDF t'apprend et que le spot ne t'apprendra jamais :**
1. **Un trade peut exister sans qu'une seule devise soit livrée** — le post-trade devient un travail sur la **donnée** (fixing, source, date) plus que sur le paiement ;
2. **La source du fixing est contractuelle** : si le PTAX n'est pas publié ou est contesté, il faut une **règle de repli** prévue au contrat (c'est là que le jargon EMTA/ISDA prend tout son sens) ;
3. **Le risque de règlement change de nature** : il n'y a plus de risque de principal (pas de livraison), mais un **risque de fixing** et un **risque de cash en USD**.

### 3.4 Qui gère quoi, pour le BRL, chez CACEIS

| Sujet | Où c'est traité |
|---|---|
| Cotation et exécution du NDF BRL pour un gérant européen | **Desk LU** |
| Confirmation, fixing, calcul du différentiel, paiement USD, réconciliation | **Middle/back office de la salle, LU** ← **ton stage** |
| Conservation des actions/obligations brésiliennes des fonds | **Santander CACEIS Brasil (São Paulo)** — Rua Amador Bueno, 474 |
| Marques du groupe | **CACEIS** en Europe · **Santander CACEIS** au Brésil et en Colombie · **S3 CACEIS** au Mexique |

### 3.5 ⚠️ L'INFORMATION STRATÉGIQUE À CONNAÎTRE (et à ne pas raconter de travers)

**En août 2026, State Street a annoncé l'acquisition de la coentreprise Santander CACEIS Latam Securities Services (Brésil, Mexique, Colombie)** — environ **470 Md$ d'actifs en conservation** et **225 Md$ sous administration** ; **closing attendu en 2027**, sous réserve des autorisations réglementaires.

**Ce que ça change pour toi — et ce que ça ne change pas :**
- ❌ **Ne construis pas ton pitch sur « je veux rejoindre CACEIS Brésil »** : cette entité est en train de sortir du groupe.
- ✅ **Ne construis pas ton pitch sur le Brésil du tout** — construis-le sur **le change**, dont le BRL est l'illustration la plus intéressante.
- ✅ **Ce que ça ne change pas** : le **desk FX de Luxembourg** continue de traiter des flux en BRL et de couvrir ses clients avec des NDF. La cession porte sur la **conservation locale**, pas sur la capacité de la salle des marchés à coter du change.
- ✅ **En entretien**, c'est un excellent sujet si on te demande « suivez-vous l'actualité du groupe ? » : *« J'ai vu que la JV Latam partait chez State Street avec un closing attendu en 2027 — ça ne change rien à la salle des marchés de Luxembourg, qui reste le centre d'exécution pour les clients européens. »* **Tu montres que tu lis, et que tu comprends la différence entre le métier (le change) et la structure (la conservation).**

---

## 4. LE STAGE « FOREX OFFICER » — CE QUE TU FAIS VRAIMENT

### 4.1 La fiche de poste, décodée ligne par ligne

| Ce que dit la fiche (réf. 116280) | Ce que ça veut dire concrètement |
|---|---|
| « Saisie, intégration, contrôle et paiements des opérations de change et de loans & deposits » | Tu récupères les deals du desk, tu les intègres dans le système, tu **contrôles** (devise, montant, taux, date de valeur, contrepartie) et tu **valides le paiement** — ou plutôt tu traites ce que le STP n'a pas passé |
| « Dans le respect des cut-offs » | Chaque devise a une **heure limite**. Rater le cut-off, c'est faire **glisser la date de valeur d'un jour** → impact trésorerie et intérêts du fonds. **C'est la mesure n°1 de ta performance** |
| « Suivi clientèle de qualité » | Tu réponds aux gérants et à leurs middle-offices : « où en est mon change ? », « pourquoi telle date de valeur ? » |
| « Suivi des contreparties et sous-dépositaires en cas de non-réception de fonds en bonne date de valeur » | **Le cœur du métier** : un flux n'arrive pas → tu identifies qui détient le cash, tu relances la contrepartie ou le correspondant, tu documentes, tu escalades |
| « Relations avec les correspondants cash et les banques intervenantes » | Tu travailles avec les banques de règlement et les **nostros** (comptes de CACEIS dans chaque devise) |
| « Loans & deposits » | La **trésorerie de la salle** : placer/emprunter au jour le jour — c'est le « money market » qui figure aussi dans l'intitulé du poste |
| « Excel » (outils : Pack Office, VBA/… ) | Les contrôles et le reporting du desk vivent dans Excel. **Ceux qui codent dominent ceux qui subissent** |

### 4.2 Une journée type (reconstruite à partir de la fiche et des standards de marché)

> ⚠️ C'est une **reconstruction raisonnée**, pas un document interne — présente-la en entretien comme ton **hypothèse de travail**, et demande à la valider : ça te fera marquer des points.

| Créneau | Ce qui se passe pour toi |
|---|---|
| **8h00 - 9h00** | **Le contrôle du matin** : les deals de la nuit (Asie) sont-ils tous capturés ? Un taux incohérent, un montant inattendu, une date de valeur impossible ? Tu remontes les exceptions |
| **9h00 - 10h30** | **Cut-offs des devises asiatiques et périphériques.** Validation des paiements. Rapprochement des confirmations avec les contreparties |
| **10h30 - 12h00** | **Demandes clients** : les gérants et leurs middle-offices appellent. Tu réponds, tu cherches, tu confirmes |
| **12h00 - 14h00** | **Le moment NDF** : calendrier des fixings, vérification du taux du jour (PTAX pour le BRL), calcul du différentiel, préparation du paiement en USD |
| **14h00 - 16h00** | **Cut-off EUR/USD** : la séquence la plus tendue de la journée. Chaque erreur ici a un coût pour le client |
| **16h00 - 18h00** | **Chasse aux fonds non reçus** : relance des contreparties et des correspondants, mise à jour des statuts, escalade de ce qui ne se règle pas |
| **Fin de journée** | **Reporting au desk** : ce qui est réglé, ce qui ne l'est pas, ce qui coince. **C'est le moment où tu deviens visible** — ou pas |
| **Mensuel** | KPIs, commissions, contrôles, revue avec le management |

**Le rythme** : la journée est scandée par les **cut-offs**, pas par ton agenda. Tu es dans un environnement où **l'erreur est datée** — elle se voit, elle se chiffre, elle s'explique.

### 4.3 Les trois choses que tu peux faire pendant ces 6 mois et que personne d'autre ne fera

1. **Tenir le score de ta propre performance** : zéro cut-off manqué, zéro paiement en retard, incidents documentés. Un stagiaire qui arrive avec **ses chiffres** au mois 4 est inarrêtable.
2. ⭐ **Automatiser un contrôle** : un fichier qui détecte en avance les trades à risque (cut-off proche, contrepartie habituellement en retard, devise à fixing). C'est **exactement** ce que demande l'offre « Sales & Trader Assistant – Forex » (« production et développement d'outils de suivi des KPIs liés à l'activité client »).
3. **Rédiger la note du desk sur les NDF** : « ce que le STP ne gère pas nativement sur les non-livrables ». Tu deviens **la personne du desk qui comprend les non-livrables** — dans une salle qui sert des gérants exposés aux marchés émergents, c'est un vrai différenciateur.

---

## 5. LES CHIFFRES CLÉS À AVOIR EN TÊTE

### 5.1 Le marché FX
| Chiffre | Valeur |
|---|---|
| Volume quotidien du marché des changes (enquête triennale **BIS 2022**) | **~7 500 Md$ par jour** — le plus grand marché du monde |
| Statut du BRL | **Devise non livrable en offshore** ; l'un des NDF les plus liquides du monde, avec le KRW, l'INR et le TWD |
| Liquidité du NDF BRL | Teneurs liquides **jusqu'à 2 ans** ; pricing possible jusqu'à 5 ans à spreads plus larges |
| PTAX | Publié par la **Banco Central do Brasil** vers **13h15, heure de São Paulo** |
| Source standard de règlement | **« BRL PTAX Offer Rate » (BRL09)**, en BRL par USD, règlement à **2 jours ouvrés brésiliens** |

### 5.2 CACEIS et le FX
| Chiffre | Valeur |
|---|---|
| Le desk FX | **À Luxembourg** — la salle des marchés du groupe sert **toutes les entités CACEIS** |
| Produits | **Spot, Forward, Swap, Options, NDF/NDS** |
| Plateformes | **FX-ALL, Bloomberg, 360T** |
| Modèle de traitement | **Full STP**, **aucune instruction de paiement** de la part du client, **audit trail** du prix, **pas de frais de règlement** |
| Cut-offs | **Étendus sur toutes les devises** (argument commercial affiché) |
| Clients / volume | **> 1 000 clients** · plusieurs millions d'ordres par an |
| Salles | **4** : France, Luxembourg, Pays-Bas, Espagne · **> 50 sales et traders** |
| Share class hedging | **~20 000 ordres/mois** · **> 1 200 classes de parts** · **> 15 Md€** · ~**10 devises** |

### 5.3 Le groupe et l'Amérique latine
| Chiffre | Valeur |
|---|---|
| CACEIS groupe | ~**7 700 collaborateurs**, **18 pays** · **> 5 900 Md€** en conservation · **> 3 700 Md€** sous administration (31/12/2025) |
| Latam | **Brésil, Mexique, Colombie**, apportés par Santander fin 2019 ; CACEIS détient **50 % moins une action** de la JV |
| La JV Latam | **~470 Md$** en conservation · **~225 Md$** sous administration — **cession à State Street annoncée en août 2026, closing attendu en 2027** |
| São Paulo | **S3 CACEIS Brasil Participações S.A.**, Rua Amador Bueno, 474 |
| Marques | **CACEIS** (Europe) · **Santander CACEIS** (Brésil, Colombie) · **S3 CACEIS** (Mexique) |

---

## 6. L'ÉCOLE — CE QUE SKEMA PEUT RÉELLEMENT TE DONNER

### 6.1 Son rôle n°1 : la convention (sans elle, rien n'existe)

Le stage de fin d'études repose sur une **convention de stage tripartite** validée par SKEMA. Ce n'est pas de la paperasse : **c'est la pièce sans laquelle tu ne peux ni partir, ni obtenir l'autorisation de séjour « stagiaire » luxembourgeoise** (qui exige la convention, une assurance et une attestation de prise en charge par l'entreprise).
➜ **Action** : récupère le modèle de convention **dès maintenant**, pour pouvoir la présenter au premier entretien sérieux.

### 6.2 Son rôle n°2 : le réseau — et il est réel

**Chiffres SKEMA** : **~63 000 alumni**, présents dans **145 pays** · **~11 000 étudiants**, **130 nationalités** · **6 000 entreprises partenaires** · **197 universités partenaires** · campus notamment à **Belo Horizonte (Brésil)** — ton propre lien avec le pays.
Et une affiliation qui compte : **SKEMA est dans le « CFA Institute University Affiliation Program »** (son Master in Management propose même une *track* CFA Level 1).

### 6.3 ⭐ Des SKEMA DÉJÀ CHEZ CACEIS LUXEMBOURG (et pas n'importe où)

Recherche faite : voici des profils que tu peux contacter **légitimement** (même école, même diplôme) :

| Nom | Ce qu'il/elle fait | Pourquoi c'est une porte |
|---|---|---|
| **Arthur Fievez** | **CACEIS — OTC derivatives, CFD and structured product pricing, Luxembourg** (MSc Financial Markets) | ⭐ Il est **sur le desk OTC dérivés** — celui des stages **116275 (OTC Pricing)**, 116273, 116274. **C'est la porte la plus directe de toute ta liste** |
| **Jade Aboudaram** | Stage de 6 mois chez **CACEIS Bank Luxembourg, Collateral Services (janv.-juil. 2024)** | ⭐ Elle a **fait exactement** ce que tu vises (collatéral à Luxembourg) — elle peut te dire comment ça se passe **vraiment** |
| **Alison Scullard** | **Business Coordination Officer, CACEIS Luxembourg** (SKEMA PGE + MSc, 2020-2024) | Elle est **dans la maison**, à Luxembourg, et pas en RH : elle sait qui recrute |
| **Quentin Alliel** | **FX & Money Market trading, Luxembourg** (SKEMA, class of 2015) | Il fait **du FX et du money market** au Luxembourg — pas chez CACEIS, mais il connaît l'écosystème |
| *(autres SKEMA au Luxembourg)* | Jérémy Tricot (Alpha FMC) · Riccardo Viccario (Intesa Sanpaolo) · Chloé Lemercier (BNP Paribas) · Thomas Tsimba (PwC) · Pascal Solyga (NEAM) | Le **vivier local** : les gens qui savent qui recrute à Luxembourg en finance |

**Le message type à envoyer (3 lignes, aucun CV en pièce jointe) :**
> Bonjour [Prénom], je suis en M2 à SKEMA et je candidate aux **stages du desk de dérivés OTC / de la salle des marchés de CACEIS Luxembourg**. Je cherche à comprendre **comment l'équipe est organisée et ce qui distingue un stagiaire qui réussit**. Auriez-vous **15 minutes**, ou une personne à me recommander ? Merci.

**Pourquoi ça marche ici et pas avec David Ranc** : même école = **une raison légitime de se parler**, sans devoir se justifier. C'est le contraire d'un contact froid.

### 6.4 Son rôle n°3 : les bourses CFA (tu es éligible)

Parce que SKEMA est affiliée au **CFA Institute University Affiliation Program**, tu as accès à la **bourse Student** du CFA Institute : elle **exonère les frais d'inscription au programme** et **ramène l'inscription à l'examen à ~400 $** au lieu de **1 490 $**.
➜ **Action** : vérifie ton éligibilité auprès du service carrières de SKEMA **avant** de payer quoi que ce soit. (Tu restes sur la ligne établie : tu ne demandes pas à CACEIS de financer le CFA — tu demandes **leur dispositif**. Mais tu ne paies pas plein tarif si ta propre école ouvre une bourse.)

---

## 7. CE QUE L'OPPORTUNITÉ DE JULIANA PEUT TE PROPOSER — LA SYNTHÈSE

**Elle ne te promet pas le FX** (son annonce est généraliste : fonctions opérationnelles, risk, investor relations, compliance, IT, RH). Mais elle te donne **quatre choses** :

1. **La date qui colle** : stages de **6 mois, à partir de janvier 2027** — exactement ton créneau de fin d'études ;
2. **Le périmètre** : les **fonctions opérationnelles** sont explicitement dans sa liste, et le profil recherché inclut **« Finance de marché »** et **VBA/Access/SQL en atout** — ton profil exact ;
3. **Le tunnel vers les contrats** : c'est elle qui porte le **« Youth Plan »** (leur dispositif de conversion stage/VIE → CDI) et la campagne **« Jeunes diplômés – Middle Office Derivatives, Securities Financing & REPO »** ;
4. **Le routage** : la seule personne à qui tu peux poser **la** question utile — *« ces stages relèvent-ils de votre périmètre, ou faut-il un contact dédié à Banking Services ? »*

**Et en parallèle, deux canaux que tu tiens désormais toi-même** : les **alerses jobs.caceis.com** (pour « Sales & Trader Assistant », « Trader Assistant », « Assistant Sales Front Office ») et le **réseau SKEMA** (Fievez vers l'OTC, Aboudaram vers le collatéral, Scullard dans la maison).

---

## 8. TES TROIS PHRASES « LE DUR » POUR L'ENTRETIEN

1. **Sur le BRL** : *« Le Brésil est un cas unique : le comptant est fermé aux non-résidents sans intérêt économique, mais le non-livrable est ouvert. Donc la couverture d'un fonds exposé au BRL passe par un **NDF**, qui est un trade sans livraison : le post-trade porte sur la **donnée** — la source du fixing, le PTAX, la date — et pas seulement sur un paiement. »*
2. **Sur la chaîne** : *« Votre salle fonctionne en STP complet, sans instruction de paiement client. Donc ce que je trouverais dans le poste, c'est **tout ce que le STP ne passe pas** : les exceptions, les cut-offs, les fixings et les fonds qui n'arrivent pas en date de valeur. C'est exactement ce qu'une fiche de poste ne dit jamais en clair, et c'est ce qui m'intéresse. »*
3. **Sur toi** : *« Je n'ai jamais passé un ordre. Ce que j'ai fait, c'est étudier les produits — et le NDF est celui qui m'a le plus appris, parce qu'il oblige à comprendre que le change ce n'est pas toujours deux jambes de devises qui se croisent. »*

---

*Sources : caceis.com « Fx solutions » (STP complet, NDF/NDS sur devises non convertibles, cut-offs étendus, FX-ALL/Bloomberg/360T) et « Brazil » (S3 CACEIS, São Paulo) · caceis.com, brochure corporate 2020-2021 et CACEIS News nº 59 (apport Santander des activités Espagne + Latam : Brésil, Mexique, Colombie ; marques CACEIS / Santander CACEIS / S3 CACEIS) · Asset Servicing Times / « Transforming together » (CACEIS 50 % moins une action de la JV, centres de production, Malaisie) · Funds Society, août 2026 (acquisition par State Street de Santander CACEIS Latam — ~470 Md$ AUC / ~225 Md$ AUA, closing attendu 2027) · CME Group (rapport exécutif relatif au PTAX), ICE Clear Europe (spécifications USD/BRL des NDF, EMTA, BRL09), obligations World Bank libellées en BRL (définition BRI PTAX, 13h15 heure de São Paulo), IMF Country Report 18/345 (accès restreint aux instruments livrables, ouverture des non-livrables, IOF, B3) · EMTA (templates et pratiques de marché BRL) · Export Finance Insider (PTAX, NDF jusqu'à 2-5 ans) · jobs.caceis.com réf. 116280 · skema.edu (affiliation CFA Institute University Affiliation Program, track CFA Level 1), Thotis et Goal ISB (chiffres SKEMA : ~63 000 alumni, 145 pays, 6 000 entreprises partenaires, campus Belo Horizonte ; MSc Financial Markets & Investments classé par le Financial Times), CFA Society North Carolina / MSU Broad (bourse Student : exonération des frais d'inscription, examen à ~400 $) · LinkedIn (profils SKEMA : Arthur Fievez — CACEIS OTC derivatives pricing Luxembourg ; Jade Aboudaram — stage Collateral Services CACEIS LU 2024 ; Alison Scullard — Business Coordination Officer CACEIS Luxembourg) · liste alumni MSc Financial Markets de SKEMA Business School.*
