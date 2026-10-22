# Soutenance DBA — dossier de présentation

**Serge Patrick MINANG** — *La gouvernance augmentée des établissements privés d'enseignement
supérieur au Gabon : articulation entre intelligence artificielle et intelligence émotionnelle
en situation de polycrise.*

Diaporama de soutenance doctorale, 26 diapositives 16:9, en HTML/CSS/SVG pur :
**aucune dépendance, aucune ressource distante, fonctionne hors ligne.**

---

## 0. Le fichier PowerPoint (à télécharger)

**`export/Soutenance-DBA-MINANG-Serge-Patrick.pptx`** — 26 diapositives 16:9, **entièrement
éditables** (textes, couleurs, cartes, tableaux), notes de l'orateur incluses.

- S'ouvre dans PowerPoint, Keynote, LibreOffice Impress et **Google Slides** (Fichier → Importer).
- **Canva** : *Créer → Importer un fichier* → choisir le `.pptx`. Canva convertit chaque
  diapositive en page modifiable ; le fond sombre, la typographie et les encarts sont conservés.
  C'est le moyen le plus rapide de retrouver un rendu « type Canva » tout en gardant le contenu DBA.
- Régénérer après modification des textes :

  ```bash
  python3 -m venv .venv && .venv/bin/pip install python-pptx
  .venv/bin/python outils/build-pptx.py     # → export/…pptx + contrôle de mise en page
  ```

Le script imprime un avertissement pour chaque texte qui risque de déborder : « aucun
avertissement de mise en page » signifie que tout tient dans les 26 diapositives.

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
├── export/
│   └── Soutenance-DBA-MINANG-Serge-Patrick.pptx   PowerPoint éditable (26 diapositives)
├── medias/
│   ├── gabon.svg       Carte des 9 provinces (province du siège mise en évidence)
│   ├── gabon.png       même carte en 1500 px (PowerPoint, impression)
│   └── logo-upl.png    Logo de l'Université Privée de Libreville
├── data/
│   └── gab_adm1.geojson  Fond de carte geoBoundaries GAB ADM1 (GAUL 2001, CC BY 4.0)
└── outils/
    ├── build-carte.py  Régénère medias/gabon.svg depuis le GeoJSON
    ├── build-pptx.py   Régénère le PowerPoint éditable (python-pptx)
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
