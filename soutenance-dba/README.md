# Soutenance DBA — dossier de présentation

**Serge Patrick MINANG** — *La gouvernance augmentée des établissements privés d'enseignement
supérieur au Gabon : articulation entre intelligence artificielle et intelligence émotionnelle
en situation de polycrise.*

Deux formats : un **PowerPoint de 18 diapositives dans la mise en page du modèle de l'auteur**
(section 0), et un diaporama web de 26 diapositives en HTML/CSS/SVG pur, sans dépendance ni
ressource distante, qui fonctionne hors ligne (sections suivantes).

---

## 0. Le fichier PowerPoint — mise en page du modèle

**`export/Soutenance-DBA-MINANG-modele-canva-18.pptx`** — **18 diapositives 16:9**, dans la
**mise en page exacte du modèle** fourni par l'auteur (`modele/template-canva.pdf`).

- **Le modèle n'est pas redessiné.** Pour chaque diapositive, on reprend la page du modèle
  (photos, formes, dégradés, illustrations, pastilles, graphiques) telle quelle ; seul le texte
  est remplacé. Rien n'est déplacé, ajouté ni supprimé.
- Les textes sont de vrais blocs PowerPoint **éditables**, posés aux coordonnées du modèle,
  avec ses couleurs et ses graisses : 18 diapositives = 18 fonds-image + ~180 zones de texte
  modifiables (aucun texte n'est « aplati » dans l'image).
- **Couverture** : photo « main robotique » du modèle (page 22), logos **Mundiapolis** et
  **IAE de Nice / Université Côte d'Azur**, mention DBA, titre, direction de thèse,
  date de soutenance, jury et coordonnées — tous éditables.
- **Carte du Gabon** à la place de la carte de l'Afrique (diapositive 2), neuf provinces,
  Libreville / Port-Gentil / Franceville et l'Estuaire nommés sans chevauchement.
- **Mots inventés par l'IA du modèle effacés** (pages 6, 7, 9 et 19 : « Bitariddion »,
  « Gelvcininship », « Emellional Insllient », « Dynamic Cacpabilities », « Auguieated »,
  « Researcheitions », « Tesperative »…) et remplacés par les libellés français corrects,
  **en texte éditable** par-dessus l'illustration d'origine.
- **Notes de l'orateur** sur les 18 diapositives.
- Retouches de données : les 45 participants (15 / 20 / 10) remplacent les 30 du modèle,
  le numéro de page répété dans les pastilles est corrigé en « 01 ».

Régénérer après modification d'un texte :

```bash
python3 -m venv .venv && .venv/bin/pip install python-pptx pymupdf pillow
.venv/bin/python outils/build-pptx-modele.py
```

Le script mesure chaque ligne avant de l'écrire et réduit la taille de police si la police de
substitution est plus large que celle du modèle : il n'y a donc pas de débordement.

---

## 1. Ouvrir la présentation HTML

Deux façons, au choix :

1. **Double-clic sur `index.html`** — le diaporama s'ouvre dans le navigateur, sans installation.
2. **Serveur local** (recommandé si le navigateur bloque certains comportements en `file://`) :

   ```bash
   cd soutenance-dba
   python3 -m http.server 8080 --bind 0.0.0.0
   # puis ouvrir http://localhost:8080/
   ```

### Commandes en séance

| Touche | Effet |
|---|---|
| `→` `Espace` `Entrée` | diapositive suivante |
| `←` | diapositive précédente |
| `Début` / `Fin` | première / dernière diapositive |
| `S` | sommaire (accès direct à une diapositive) |
| `N` | notes de l'orateur (script et « question probable ») |
| `F` | plein écran |
| `P` | imprimer / exporter en PDF |
| `Échap` | fermer un panneau |

Sur tablette ou téléphone : balayage horizontal. L'adresse garde la diapositive courante
(`…/index.html#12`), ce qui permet d'envoyer un lien direct vers une diapositive.

### Exporter en PDF (pour archiver ou projeter sans navigateur)

`P` (ou `Ctrl/Cmd + P`) → **Destination : Enregistrer au format PDF** →
**Orientation : Paysage**, **Marges : Aucune**, **Graphiques d'arrière-plan : activés**.
On obtient 26 pages au format exact 1280 × 720 px.

---

## 2. Ce que contient le dossier

```
soutenance-dba/
├── index.html          Diaporama — 26 diapositives, notes de l'orateur incluses
├── style.css           Charte encre / bronze ; mise en page 16:9, impression
├── deck.js             Navigation, sommaire, notes, ajustement anti-débordement
├── sources.html        Provenance de chaque chiffre et de chaque visuel (à montrer au jury)
├── doc.css             Mise en forme des pages documentaires
├── guide-soutenance.md Plan de l'oral, minutage et questions attendues
├── modele/
│   └── template-canva.pdf            Modèle de l'auteur (32 pages), source de la mise en page
├── export/
│   └── Soutenance-DBA-MINANG-modele-canva-18.pptx   PowerPoint, 18 diapositives, mise en page du modèle
├── medias/
│   ├── gabon.svg       Carte des 9 provinces (province du siège mise en évidence)
│   ├── gabon.png       même carte en 1500 px (PowerPoint, impression)
│   └── logo-upl.png    Logo de l'Université Privée de Libreville
├── data/
│   └── gab_adm1.geojson  Fond de carte geoBoundaries GAB ADM1 (GAUL 2001, CC BY 4.0)
└── outils/
    ├── build-carte.py  Régénère medias/gabon.svg depuis le GeoJSON
    ├── build-pptx-modele.py  Régénère le PowerPoint en remplissant le modèle (python-pptx + pymupdf)
    └── check.mjs       Contrôle du dossier (16 vérifications, sans dépendance)
```

### Vérifier le dossier

```bash
node outils/check.mjs          # 15 contrôles : structure, chiffres, sources, liens, confidentialité
python3 outils/build-carte.py  # régénère la carte
```

Le contrôle vérifie notamment les additions affichées dans le diaporama :

- architecture : 8 (introduction) + 61 (chapitres 1 à 6) + 8 (conclusion) = **77 sections** ;
- supports : 4+10+17+17+22+25+20 = **115** avant, 1+5+6+6+7+9+6 = **40** après, soit 27 tableaux + 13 figures ;
- échantillon : 15 + 20 + 10 = **45 participants**.

---

## 3. À compléter avant la soutenance

Trois informations ne figurent dans aucun document disponible et ne peuvent donc pas être
supposées — elles sont signalées en clair sur la couverture :

1. **université d'inscription** au DBA ;
2. **direction de thèse** (directeur / co-directeur, éventuel tuteur) ;
3. **date et lieu de soutenance**.

À modifier dans `index.html`, diapositive 1, bloc `.who .todo` (chercher la mention
`[à compléter par l'auteur`). Les mentions publiques d'usage (nom, fonction, coordonnées)
sont déjà en place.

Deux autres points à valider par l'auteur, sans qu'aucun contenu ne soit inventé :

- la **formulation du titre** retenue pour la soutenance (le diaporama affiche le titre indicatif) ;
- l'ajout éventuel du **nom des membres du jury** sur la couverture, si l'usage de l'établissement le demande.

---

## 4. Ligne de conduite du dossier

Le diaporama suit les règles du dossier de recherche dont il est issu :

| Règle | Traduction dans le diaporama |
|---|---|
| Rien d'inventé | chaque diapositive porte un pied de page « Sources » ; les chiffres sont décomptés, pas estimés |
| Chapitres 5 et 6 préparatoires | aucun résultat de terrain, aucun verbatim, aucune conclusion empirique |
| Rien de présumé | la gouvernance augmentée est une proposition à examiner ; l'absence documentée est une issue prévue |
| Confidentialité | établissements sous codes EPES-A à EPES-E ; participants par catégories (DIR, ACA, ADM, RH, NUM-QRSE) |
| Bibliographie | aucune référence citée, la bibliographie du manuscrit étant en cours d'harmonisation |
| Statuts affichés | « prévisionnel », « indicatif », « à compléter » sont écrits noir sur blanc |

La page **`sources.html`** détaille la provenance de chaque nombre et de chaque visuel : c'est la
page à ouvrir si un membre du jury demande « d'où vient ce chiffre ? ».

---

## 5. Publier sur GitHub Pages (facultatif)

Le dossier est autonome : n'importe quel hébergement statique convient. Avec GitHub Pages,
deux options :

- **Réglages du dépôt** → *Pages* → *Source : Deploy from a branch* → branche `main`,
  dossier `/` (ou `/soutenance-dba`). L'adresse devient
  `https://<compte>.github.io/<dépôt>/soutenance-dba/`.
- **Dépôt dédié** : copier le dossier `soutenance-dba` dans un nouveau dépôt public, puis
  activer Pages sur `main` / racine. C'est la solution la plus propre pour un lien à envoyer.

> **Attention** : ce dépôt-ci contient par ailleurs des documents personnels. Pour diffuser la
> présentation par lien, préférer un dépôt dédié, ou vérifier ce qui est public avant d'activer Pages.

---

## 6. Personnalisation rapide

| Élément | Où le modifier |
|---|---|
| Charte (couleurs, polices) | `style.css`, variables `:root` en tête de fichier |
| Titre / sous-titre | `index.html`, diapositive 1 (`s1`) |
| Textes d'une diapositive | `index.html`, section `id="sN"` |
| Notes de l'orateur | bloc `<aside class="notes">` de la diapositive concernée |
| Pied de page (sources) | bloc `.foot .src` de la diapositive concernée |
| Chiffres du diagramme des supports | diapositive 17 (`s17`), tracé SVG — et valeurs de contrôle dans `outils/check.mjs` |

Après toute modification : `node outils/check.mjs` doit rester vert.

---

## 7. Compatibilité

- Navigateurs récents (Chrome, Edge, Firefox, Safari), sans plugin.
- Sans JavaScript : les 26 diapositives s'empilent et restent intégralement lisibles ; l'impression reste correcte.
- Projection : prévoir un écran 16:9 ; le diaporama se met à l'échelle de la fenêtre.
- Impression papier : fond sombre — prévoir une imprimante couleur ou projeter directement.

---

*Dossier arrêté le 22 octobre 2026. Documents de travail : à vérifier par l'auteur avant diffusion.*
