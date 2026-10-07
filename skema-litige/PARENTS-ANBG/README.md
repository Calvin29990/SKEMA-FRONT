# PARENTS-ANBG — dossier de remise en main propre + courriel Campus France
*Constitué le 07/10/2026. Ce dossier est **fait pour être imprimé** : les PDF de `pdf/` se suffisent à eux-mêmes, aucune pièce supplémentaire n'est requise pour le dépôt.*

---

## 1. Quel fichier pour qui

| Fichier | Pages | Poids | Qui l'utilise |
|---|---|---|---|
| `pdf/DOSSIER-A-REMETTRE-ANBG.pdf` | 18 | 995 Ko | **Le parent porteur le remet au guichet ANBG.** Recours (p. 1-3) · procuration (p. 4) · récépissé à faire viser (p. 5) · annexes 4 à 9 (p. 6-18) |
| `pdf/DOSSIER-FAMILLE-COMPLET.pdf` | 22 | 1 022 Ko | **La famille le garde.** Le même dossier, plus : **mémo des parents (p. 6-7)**, liste de la chemise (p. 8), note interne (p. 9). **Détacher les p. 6 à 9 avant la remise au guichet** — ou n'imprimer que le fichier de 18 pages |
| `pdf/MAIL-CAMPUS-FRANCE.pdf` | 3 | 144 Ko | **Calvin uniquement** : texte du courriel à coller, destinataires, pièces jointes à nommer, garde-fous, calendrier après envoi |

Sources éditable : `RECOURS-GRACIEUX-ANBG.md` et `MAIL-CAMPUS-FRANCE-BOUCLY-CC.md`.
Pour régénérer les PDF après une modification : `python3 skema-litige/outils/assembler-dossier.py`.

## 2. À compléter **à la main** avant l'impression (5 champs)

| Où | Champ |
|---|---|
| Recours, dernière ligne | **Lieu et date** de signature, puis **signature** précédée de « lu et approuvé » |
| Procuration, 1er paragraphe | **Adresse de l'étudiant** (résidence française) |
| Procuration, 2e paragraphe | **Nom, prénom, date de naissance, adresse et n° de pièce d'identité du parent porteur**, et lien de parenté |
| Récépissé, ligne « Remis par » | Nom du porteur (le même qu'à la procuration) |
| Récépissé, lignes « Date et heure », « Nombre de pièces » | À remplir **au guichet**, pas avant |

**Joindre impérativement** : la **photocopie de la pièce d'identité du parent** (sans elle, une procuration n'est pas recevable) et une copie de la **pièce d'identité ou du passeport de l'étudiant**.

## 3. Ce qui manque encore dans ces PDF (à insérer avant impression si possible)

| Manque | Pourquoi ça compte | Comment le récupérer |
|---|---|---|
| **Les 4 captures de notifications eBourse** (p. 6 du dossier = page « à imprimer puis agrafer ») | Horodatages 25/09/2024 16:37 · 17/02/2025 11:06 · 17/02/2025 11:11 · 10/11/2025 15:47 — c'est le moyen n° 2 | Espace étudiant `anbg.online` › **Messages** ; imprimer avec l'horodatage de consultation visible |
| **Attestation de stage BPCE** (08/01/2024 → 05/07/2024) | Seule pièce qui clôt le motif « abs de releve de notes » par un document positif | Demande écrite à `talentandcareers@skema.edu` (Stéphanie Bianchi) **et** au RH de BPCE : la convention met cette délivrance à la charge de l'entreprise |
| **Attestation ANBG du 06/09/2023** (bourse 2023-2025) | Le fichier du dépôt est **illisible** ; c'est la durée exacte de la prise en charge du cycle | **C'est la demande n° 4 du recours** : le parent la fait délivrer en copie certifiée au guichet, à Libreville. C'est l'un des deux objectifs utiles du déplacement |
| **Certificat de scolarité du 17/12/2024** | Cité dans les demandes Campus France (« postérieur au 01/09/2023 ») ; il n'existe pas en fichier autonome | À ressortir de Gmail/Drive ou à redemander au registraire |
| `FACTURE_MINANG_CALVIN_M2_2526.pdf` · `CEGID MINANG CALVIN 05-10-26.pdf` | Le **titre** et l'**assiette** des 14 840,00 € — sans eux, la réponse à la mise en demeure reste une contestation sans pièce | Pièces jointes du courriel du 07/10/2026 : les télécharger dans `skema-litige/pieces/` (le fichier `facture-M2-2425.pdf` du dépôt est **vide, 0 octet**) |

## 4. Message à envoyer aux parents avec les deux documents (WhatsApp)

> Bonjour. Je vous envoie **deux fichiers PDF**.
> **1) « DOSSIER-A-REMETTRE-ANBG »** (18 pages) : c'est le dossier à déposer à l'ANBG. Merci de l'**imprimer en couleurs** si possible, de **remplir à la main** la date, mon adresse, votre nom et votre numéro de pièce, de joindre la **photocopie de votre pièce**, et de joindre les **4 captures d'écran** que je vous envoie à part.
> **2) « DOSSIER-FAMILLE-COMPLET »** (22 pages) : à garder à la maison. **Les pages 6, 7, 8 et 9 ne se remettent pas** au guichet (c'est le mémo pour vous).
>
> **Au guichet, dans l'ordre :** demander la **Direction des bourses / le service des bourses de l'étranger**, remettre la chemise, et **demander trois choses** : un **numéro d'enregistrement**, la **date sur le double**, et le **nom du service** qui traite. Si on refuse d'enregistrer : demander juste le **tampon daté sur le double**. Ne rien signer d'autre, ne rien réclamer d'argent, ne parler ni de politique ni d'avocat. **M'envoyer une photo du récépissé tamponné** — c'est la pièce dont j'ai besoin pour mon école.
> Les phrases à dire sont écrites en **pages 6 et 7** du dossier famille.

## 5. Après le dépôt — qui fait quoi

| Quand | Qui | Quoi |
|---|---|---|
| Le jour même | Calvin | Envoie le courriel Campus France (`MAIL-CAMPUS-FRANCE.pdf`, juriste SKEMA en copie) + la réponse à la mise en demeure ; note la date d'envoi dans `skema-litige/RECONSTITUTION-CHRONOLOGIQUE-2019-2026.md` |
| J+1 | Parents | Photo du récépissé tamponné → à archiver dans `skema-litige/pieces/` sous `recepisse-ANBG-<date>.jpg` |
| J+10 (**19/10/2026**) | Calvin | Échéance de la mise en demeure ; relance unique si rien |
| J+15 | Parents | Si aucune réponse écrite : rappel au service désigné sur le récépissé, en visant le n° d'enregistrement |
| J+30 | Calvin | Saisine du service des bourses de l'**Ambassade du Gabon en France** (le recours leur est déjà adressé en copie) |

## 6. Confidentialité — à lire avant de partager un lien

Ces PDF contiennent état civil, références de dossier, montants et correspondance avec un service juridique **en cours de contentieux**. Le dépôt `Calvin29990/SKEMA-FRONT` est **public** : y publier ce dossier revient à le rendre lisible par la partie adverse. **Les PDF générés sont hors dépôt** (entrée `.gitignore` sur `skema-litige/PARENTS-ANBG/pdf/`) : ils se régénèrent en 25 secondes et ne doivent pas finir indexés par un moteur de recherche.
**Attention :** les sources markdown, elles, sont versionnées localement sur la branche `arena/19bab905-skema-front`, et cette branche **n'a pas été poussée** — tant qu'elle reste locale, rien de ce dossier n'est lisible par un tiers. Un `git push` sur ce dépôt public rendrait immédiatement lisibles le recours, la chronologie C1-C18 et les garde-fous négociés. À décider sciemment (voir aussi `SKEMA-DOSSIER-ARCHIVE.md`).
