# EXTRACTION DU DOSSIER DEPUIS LE PORTAIL ANBG (`anbg.online/etudiant/...`)
**Objectif : transformer le portail en pièces citables, horodatées, numérotées — c'est la seule source qui détient la décision de 2025/2026 (CA24B3) et les traces du parcours des pièces.**

Observation du **mercredi 07/10/2026 21:06:56** (capture) : `FICHE DE DEMANDE DE BOURSE D'ÉTUDES SESSION 2025-2026` · dossier **CA24B3** · **DÉCISION : AVIS DÉFAVORABLE** · « Votre dossier est déjà traité » · onglets `Mon Dossier` / `Pièces Justificatives` / `Messages` / `Synthèse` · **RÉF EXTERNE 110584Z** · liste des dossiers : 2025-2026 CA24B3 · 2024-2025 **1LMK24 (icone rouge)** · 2023-2024 2E4C0B · 2022-2023 LDPMRC · 2021-2022 PNPXWG · 2020-2021 4EO0OO · 2019-2020 WEXQTG. Première ligne de la liste des pièces : « **Facture coût de la scolarité** — 269 kB — **02 sept. 2025 11:38** ».

---

## 1. À télécharger / imprimer, dans cet ordre (≈ 25 min)

| # | Où cliquer | Ce qu'il faut obtenir | Nom de fichier à utiliser |
|---|---|---|---|
| 1 | **CA24B3 › Mon Dossier** | La fiche complète : date de dépôt, date de décision, **libellé exact du motif**, année et établissement visés, catégorie de bourse, montant/octroi | `ANBG-CA24B3-mon-dossier.pdf` |
| 2 | **CA24B3 › Synthèse** | Le récapitulatif de la décision — **c'est la page qui contient l'« AVIS DÉFAVORABLE » et son fondement (article 4 du décret 065 ?)** ; imprimer en entier, sans rogner l'en-tête ni l'horodatage | `ANBG-CA24B3-synthese.pdf` |
| 3 | **CA24B3 › Pièces Justificatives** | **Toute la liste**, avec pour chaque pièce : type, taille, **date-heure de dépôt**, statut (validée / en attente / rejetée). C'est la preuve de ta diligence, pièce par pièce | `ANBG-CA24B3-pieces.png` (1 capture par écran, numérotées `-1`, `-2`…) |
| 4 | **CA24B3 › Messages** | Tous les échanges, **avec dates et expéditeurs** ; en particulier toute trace d'une mise en relation ANBG ↔ Campus France ↔ SKEMA | `ANBG-CA24B3-messages-1..n.png` |
| 5 | **1LMK24 (2024-2025) › les 4 onglets** | L'icône rouge = dossier supprimé : il faut la **date exacte**, le **motif écrit**, et l'état des pièces déposées (dont « Attestation de scolarité » et « Relevé de notes »). **C'est l'année qui a fait basculer le M2 hors couverture** | `ANBG-1LMK24-*.pdf/.png` (même schéma) |
| 6 | **2E4C0B (2023-2024) › Mon Dossier + Pièces** | Le dossier qui a donné le **BC Campus France n° 721622 du 06/05/2024 (16 000 €, « POUR LE COMPTE DE L'ANBG FRAIS FORMATION 2023 2024 »)** réglé le… — à confirmer. Utile pour montrer que le dispositif a fonctionné **sans intervention de l'étudiant** dès lors que les pièces étaient conformes | `ANBG-2E4C0B-*.pdf/.png` |
| 7 | **LDPMRC (2022-2023)** | Idem pour le **BC n° 677745 du 24/01/2023 (15 000 €)** | `ANBG-LDPMRC-*.pdf/.png` |
| 8 | **PNPXWG / 4EO0OO / WEXQTG** | Les 3 captures d'écran suffisent : elles établissent la **continuité 2019-2022** (1ʳᵉ ligne du récit) | `ANBG-<ref>-mon-dossier.png` |
| 9 | Le fichier « **Facture coût de la scolarité** » (269 kB) lui-même | **Télécharger le PDF déposé le 02/09/2025** : c'est la facture que tu as transmise à l'ANBG — celle-là même que Campus France a rejetée 23 jours plus tard faute de certificat. Elle prouve (i) quelle facture SKEMA t'avait délivré, (ii) que tu as agi dès le début septembre 2025 | `ANBG-piece-facture-2025-09-02.pdf` |

**Où les mettre :** dans le repo, dossier `skema-litige/pieces/` (tu peux aussi les déposer dans le Drive › « Dossier reconstitution échange » — mais **le repo me permet de les lire directement**, y compris les captures : je convertis les PDF scannés en images et je les lis). Dépose-les, dis-moi « c'est bon », et j'intègre.

---

## 2. Ce que ces pièces changent dans le dossier (à valider par l'extraction)

| Ce que je croyais | Ce que le portail montre | Conséquence sur le courrier |
|---|---|---|
| « L'ANBG a confirmé avoir contacté SKEMA » (note du 30/09) | À dater et à sourcer dans l'onglet `Messages` | Si trouvé : c'est **la** pièce qui établit que l'école a été avertie par le financeur → à placer en tête du point 2.d du courrier. Sinon : retirer toute mention de cet échange |
| Suppression du dossier 1LMK24 le « 25/09/2024 » (date relevée sur le portail, non sur une décision) | Le portail doit donner la **décision écrite** et sa date de **notification** | La demande n° 4 du courrier à l'ANBG devient : production de la **décision motivée notifiée** + liste des pièces examinées. Sans notification écrite, un avis défavorable opposable est fragilisé — à constater, pas à plaider |
| « Avis défavorable » pour 2025/2026 = la bourse refusée pour le M2 | **CA24B3 = AVIS DÉFAVORABLE, dossier déjà traité** | Le courrier à l'ANBG doit désormais contenir une **demande de réexamen** (recours gracieux) fondée sur une pièce précise : **l'attestation PGE du registraire du 14/05/2024** qui place le M2 en 2025/2026, donc **le calendrier de l'école, pas un choix dilatoire de l'étudiant** |
| Le « parcours insoutenable » reposait sur un etalement choisi par toi | L'étalement a été **accepté le 27/10/2023, confirmé le 15/01/2024, et attesté le 14/05/2024** par le registraire ; et tu as alerté le **08/01/2024** | Le motif « insoutenable » se retourne : la demande à l'ANBG devient « sur quels éléments, datés, cette qualification a-t-elle été retenue, alors que le calendrier a été certifié par l'établissement le 14/05/2024 ? » |

---

## 3. Ce que l'extraction doit me permettre de **remplacer** (les trous du courrier)

À ce stade, dans `REPONSE-MISE-EN-DEMEURE-2026-SK-D-0002.md`, trois énoncés sont encore conditionnels. Les pièces ANBG les lèvent :

1. « *l'attestation d'attribution de bourse Master du 6 septembre 2023 couvrait deux années* » → **version lisible** de l'attestation (ou capture eBourse du dossier 2E4C0B). Tant qu'elle manque, cette phrase reste au conditionnel dans le courrier.
2. « *j'ai appelé l'attention des services le 8 janvier 2024* » → PDF de l'e-mail (ou sa trace dans `Messages`).
3. « *la facture que j'ai transmise à l'ANBG* » → le fichier du **02/09/2025 11:38**, déjà identifié sur le portail : à récupérer en priorité, il est **daté, horodaté et incontestable**.

---

## 4. ⚠️ Trois clauses du contrat que l'escalade doit intégrer (lu dans `2733904447-Contrat-Signe.pdf`)

| Clause | Texte | Ce qu'elle implique pour toi, maintenant |
|---|---|---|
| **3.4.1** | « *SKEMA Business School se réserve le droit de prononcer la **suspension ou la résiliation du contrat de plein droit** du fait de l'inexécution de l'obligation de payer dans les délais requis.* » | La « cessation définitive » annoncée par Boucly n'est pas une décision discrétionnaire à contester sur le fond : c'est une **clause résolutoire**. La seule défense utile est de contester **l'exigibilité** (titre, assiette, échéance) — donc d'écrire, comme le fait le courrier, que le paiement est suspendu à la production des pièces, et **de ne jamais disparaître du dialogue** (une absence = inexécution caractérisée). |
| **Cessation de scolarité (barème)** | « *en cas de cessation définitive de scolarité après la date de début des cours de l'année concernée, les frais restant dus sont de : un tiers du montant annuel dans les 3 mois, deux tiers dans les 6 mois, **cent pour cent** au-delà* » | Une exclusion prononcée **en novembre 2026 ou plus tard** porterait l'année en cours à **100 %**. Autrement dit, leur menace te coûte, à court terme, plus qu'elle ne leur rapporte : **le premier objectif reste la fin du M2 en décembre, pas la victoire d'audience.** Le courrier est calibré là-dessus (aucune provocation, demandes de pièces, proposition d'échéancier). |
| **3.4.2 — droit de rétention** | « *En cas de non-paiement total ou partiel des sommes dues, SKEMA Business School se réserve un **droit de rétention de tout document, notamment du diplôme**, et ce quel que soit le débiteur.* » | Vise **le diplôme**. Le **certificat de scolarité S5** n'est pas un document de constatation du diplôme mais l'attestation de ton inscription en cours : la demande du point 4.4 du courrier doit rester **distincte** et formulée comme un acte dû à tout étudiant inscrit. Ne pas les laisser fusionner les deux. |
| **ARTICLE 6** | « *la seule loi applicable au présent contrat est la loi française […] Toutes difficultés concernant l'interprétation ou l'exécution du présent contrat seront portées devant **les Tribunaux territorialement compétents** nonobstant pluralité de défendeurs ou appel en garantie.* » | Correction utile : SKEMA est une **association loi 1901 (personne privée)** → le contentieux de ce contrat relève des **tribunaux judiciaires**, pas du tribunal administratif. La mention « référé administratif » du dossier d'archives ne vaut que pour le **titre de séjour / préfecture**, pas pour la dette. Le tribunal administratif n'est donc **pas** la porte de sortie du volet financier. |

---

## 5. En parallèle, pendant l'extraction (5 min)

- [ ] **Récupérer dans Gmail** les 2 PJ du mail de Boucly : `FACTURE_MINANG_CALVIN_M2_2526.pdf`, `CEGID MINANG CALVIN 05-10-26.pdf` (+ `contrat_2c969e2f81f11c59018227f437230391.pdf`) → même dossier `skema-litige/pieces/`.
- [ ] **Capturer le portail Campus France / Chorus Pro si tu y as un accès** : l'état de la facture n° **1281253** (rejetée, en attente, ou annulée). Si tu n'y as pas accès, c'est justement la demande n° 2 du courrier à SKEMA.
- [ ] Ne pas modifier les fichiers déjà téléchargés : je m'appuie sur leur horodatage Drive/Git pour dater les pièces.

---

## 6. Ce qui a été relevé le 08/10/2026 (neuf impressions, 01:48:30 → 01:52:27)

Les points 5 à 8 de la liste du § 1 sont couverts. Les images sont déposées dans `skema-litige/pieces/ebourse/` (noms numérotés `01-…` à `09-…`) ; `lettre.py` les assemble une par page, sans retouche, dans `skema-litige/pieces/impressions-ebourse.pdf`, et la cote **E** du bordereau se remplit alors seule. Le détail écran par écran est dans `INDEX-ANNEXES.md`, section A bis.

**Ce que ces écrans apportent — et rien d'autre :**

1. **L'Agence a validé les relevés de la licence avant d'accorder la session suivante.** Validation du « RELEVÉ(S) DES NOTES DU CYCLE PRÉCÉDENT » le **17 août 2023 à 09:25**, « DECISION : ACCORD » de la session 2023-2024, attestation générée le **6 septembre 2023 à 12:23** — soit après la délibération du jury de SKEMA Business School de juillet 2023.
2. **Sa propre fiche du cursus ne mentionne aucun redoublement.** « Mon Cursus », consulté le 08/10/2026 : 2022-2023 « **LICENCE OBTENUE** », 2023-2024 « **ANNEE DE CESURE** », statut « Boursier » sur ces deux lignes ; « Non Boursier » sur 2024-2025 et 2025-2026.
3. **La suppression du 25 septembre 2024 est un message de quatre lignes**, sans signataire, sans visa, sans référence à un texte — c'est l'appui du moyen 1 du recours et de la demande 3° de la lettre.
4. **La plateforme annualise les pièces, non le droit.** Notification du **14 septembre 2022 à 15:35** : l'attestation de maintien « se délivre, à l'issue de douze (12) mois de perception de bourse, aux étudiants en intra-cycle ayant rempli les conditions de maintien de l'allocation pour l'année N+1 et ne saurait remplacer l'attestation d'attribution de bourse à double signatures, délivrée par la Commission Technique des Bourses » lors d'un changement de cycle.

**Ce qu'ils ne disent pas.** Aucune de ces pages ne vaut décision pédagogique de SKEMA Business School, aucune ne résume une délibération, aucune ne détaille le motif au-delà de la ligne « abs de releve de notes / perception de la bourse » du 25/09/2024. Rien ne doit être extrapolé au-delà des quatre points ci-dessus.
