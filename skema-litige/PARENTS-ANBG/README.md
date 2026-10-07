# PARENTS-ANBG — dossier de remise en main propre + courriel Campus France
*Constitué le 07/10/2026. Ce dossier est **fait pour être imprimé** : les PDF de `pdf/` se suffisent à eux-mêmes, aucune pièce supplémentaire n'est requise pour le dépôt.*

---

## 1. UN SEUL fichier pour les parents, un pour le courriel

| Fichier | Pages | Poids | Usage |
|---|---|---|---|
| `pdf/DOSSIER-PARENTS-ANBG.pdf` | **26** | 2,8 Mo | **Tout le dossier des parents, en un seul PDF à imprimer.** p. 1 = consignes du porteur (à ne pas remettre) · p. 2-4 = recours gracieux · p. 5 = procuration · p. 6 = récépissé (**à imprimer en 2 exemplaires**) · p. 7 = liste de la chemise · p. 8-10 = consignes (suite, à ne pas remettre) · p. 11-26 = annexes 4 à 10 |
| `pdf/MAIL-CAMPUS-FRANCE.pdf` | 3 | 136 Ko | Le courriel à copier-coller + les 7 pièces jointes à nommer |
| `pdf/PIECES-MAIL-CAMPUS-FRANCE.zip` | 7 fichiers | 1,1 Mo | **Les 7 pièces jointes, déjà renommées exactement comme dans le courriel** (+ le PDF du courriel). Dézipper, tout sélectionner, glisser dans le mail |
| `pdf/pieces-mail/` | idem | | Les mêmes 7 fichiers à l'unité, si le zip ne passe pas |

**Tout est pré-rempli : date (8 octobre 2026), lieu (Lille), pièces, numéro de dossier, noms des services.** Un seul geste reste à faire en France : **signer à la main la page 4** (recours) et la page 5 (procuration), puis envoyer le PDF aux parents. Rien à compléter au Gabon.

Pour régénérer après modification des `.md` : `python3 skema-litige/outils/assembler-dossier.py` (25 s).

## 3. Ce qui manque encore dans ces PDF (à insérer avant impression si possible)

| Manque | Pourquoi ça compte | Comment le récupérer |
|---|---|---|
| **Les 4 captures de notifications eBourse** (p. 11 du dossier = page « à imprimer puis agrafer ») | Horodatages 25/09/2024 16:37 · 17/02/2025 11:06 · 17/02/2025 11:11 · 10/11/2025 15:47 — c'est le moyen n° 2 | Espace étudiant `anbg.online` › **Messages** ; imprimer avec l'horodatage de consultation visible |
| **Attestation de stage BPCE** (08/01/2024 → 05/07/2024) | Seule pièce qui clôt le motif « abs de releve de notes » par un document positif | Demande écrite à `talentandcareers@skema.edu` (Stéphanie Bianchi) **et** au RH de BPCE : la convention met cette délivrance à la charge de l'entreprise |
| **Attestation ANBG du 06/09/2023** (bourse 2023-2025) | Le fichier du dépôt est **illisible** ; c'est la durée exacte de la prise en charge du cycle | **C'est la demande n° 4 du recours** : le parent la fait délivrer en copie certifiée au guichet, à Libreville. C'est l'un des deux objectifs utiles du déplacement |
| **Certificat de scolarité du 17/12/2024** | Cité dans les demandes Campus France (« postérieur au 01/09/2023 ») ; il n'existe pas en fichier autonome | À ressortir de Gmail/Drive ou à redemander au registraire |
| `FACTURE_MINANG_CALVIN_M2_2526.pdf` · `CEGID MINANG CALVIN 05-10-26.pdf` | Le **titre** et l'**assiette** des 14 840,00 € — sans eux, la réponse à la mise en demeure reste une contestation sans pièce | Pièces jointes du courriel du 07/10/2026 : les télécharger dans `skema-litige/pieces/` (le fichier `facture-M2-2425.pdf` du dépôt est **vide, 0 octet**) |

## 4. Message à envoyer aux parents (WhatsApp) — un seul fichier

> Bonjour. Je vous envoie **un seul fichier PDF : « DOSSIER-PARENTS-ANBG »** (26 pages). **Il n'y a rien à écrire** : tout est déjà daté et rempli.
>
> Vous avez juste à : **1)** imprimer en A4 (en couleurs si possible) — **imprimer DEUX FOIS la page 6** (le récépissé) ; **2)** agrafer la photocopie de votre pièce d'identité derrière ; **3)** imprimer les 4 captures d'écran que je vous envoie à part et les agrafer **après la page 11** ; **4)** remettre le tout au **guichet du courrier de l'ANBG** (Direction Générale, Libreville).
>
> **La page 1 et les pages 8, 9, 10 sont pour vous : ne les remettez pas au guichet** (elles sont marquées d'un bandeau). C'est écrit dessus : les quatre étapes, les trois choses à demander — un **numéro d'enregistrement**, la **date sur votre exemplaire**, le **nom du service** — et les phrases à dire.
>
> **Envoyez-moi une photo du récépissé daté.** C'est la seule chose qui compte pour la suite de mon dossier. Ne signez rien d'autre, ne demandez aucun argent, ne parlez ni de politique ni d'avocat.

## 5. Après le dépôt — qui fait quoi

| Quand | Qui | Quoi |
|---|---|---|
| Le jour même | Calvin | Signe les p. 4 et 5, envoie le PDF aux parents, puis envoie le courriel Campus France (`MAIL-CAMPUS-FRANCE.pdf` + le contenu du zip, juriste SKEMA en copie) + la réponse à la mise en demeure ; note la date d'envoi dans `skema-litige/RECONSTITUTION-CHRONOLOGIQUE-2019-2026.md` |
| J+1 | Parents | Photo du récépissé daté → à archiver dans `skema-litige/pieces/` sous `recepisse-ANBG-<date>.jpg` |
| J+10 (**19/10/2026**) | Calvin | Échéance de la mise en demeure ; relance unique si rien |
| J+15 | Parents | Si aucune réponse écrite : rappel au service désigné sur le récépissé, en visant le n° d'enregistrement |
| J+30 | Calvin | Saisine du service des bourses de l'**Ambassade du Gabon en France** (le recours leur est déjà adressé en copie) |

## 6. Confidentialité — à lire avant de partager un lien

Ces PDF contiennent état civil, références de dossier, montants et correspondance avec un service juridique **en cours de contentieux**. Le dépôt `Calvin29990/SKEMA-FRONT` est **public** : y publier ce dossier revient à le rendre lisible par la partie adverse. **Les PDF générés sont hors dépôt** (entrée `.gitignore` sur `skema-litige/PARENTS-ANBG/pdf/`) : ils se régénèrent en 25 secondes et ne doivent pas finir indexés par un moteur de recherche.
**Attention :** les sources markdown sont versionnées localement sur la branche `arena/19bab905-skema-front`, et cette branche **n'a pas été poussée** — tant qu'elle reste locale, rien de ce dossier n'est lisible par un tiers. Un `git push` sur ce dépôt public rendrait immédiatement lisibles le recours, la chronologie C1-C18 et les garde-fous négociés. À décider sciemment (voir aussi `SKEMA-DOSSIER-ARCHIVE.md`).
