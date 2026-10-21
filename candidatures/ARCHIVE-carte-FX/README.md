# ARCHIVE — Cartes du marché FX corporate France (régénération complète)

Ce dossier permet de **régénérer à l'identique** toutes les cartes et données du projet
« photographie du marché FX à instant T », depuis n'importe quelle session Arena.
Étude académique personnelle — aucune donnée client, aucune finalité commerciale.

## Produits générés (dans `candidatures/`)

| Fichier | Contenu |
|---|---|
| `CARTE-2026-10-20-qui-achete-le-FX-et-ou.pdf` (2 p) | Carte **nominative** : 39 015 sièges cœur+contingent, 221 comptes ≥ 250 M$ nommés, zoom Île-de-France ; page 2 = mode d'emploi, top 15 France/Sud, phrase d'entretien |
| `CARTE-2026-10-20-page1.png` / `page2.png` | mêmes pages en image (partage mobile) |
| `CARTE-2026-10-20-gateau-regions.pdf/.png` | Carte **simplifiée sans noms** : choroplèthe régionale, % sièges + % CA, IDF (vert) vs Grand Sud (or) vs reste (neutre), barres 100 % |
| `ORBIS-2026-10-20-univers-FX-64646-geo.xlsx` | Classeur : univers 64 646 lignes (région/dép/ville/INSEE/lon-lat/classe FX) + GRAND SUD mesuré 8 718 + PRESTIGE 3 149 + PIVOTS |

## Extension : segment <5M€ (21/10 — trois exports Moody's)

Trois exports Orbis « Export 21_10_2026 09_33 / 09_56 / 09_59.xlsx » (origin/main), requête actives × France × CA **max 5 m€** (2 316 251 entités ; + tendance positive = 1 254 798) :
- **09_33** : 45 000 lignes, tranche ≈2,2–5,6 M€, **sans** colonne de localisation → profil NACE/CA seulement.
- **09_56** : 6 000 lignes (limite Moody's 6k/page) avec **Ville + Code postal + GUO**, tri descendant → **tranche 3,8–5 M€, contiguë à la carte principale** → géocodée par CP (5 853 métropole) : **IDF 27,4 % sièges / 27,4 % CA ; Grand Sud 22,9 % / 22,9 %** — vs 32,9/68,1 et 20,3/9,0 sur l'univers ≥5M€.
- **09_59** : 6 001 lignes toutes au plancher 90 k€ (bas de requête) → usage limité (pas de profil).
Fusion dédupliquée (12 001 lignes) : feuille `SOUS-5ME-12K` du classeur ; synthèse : `SEGMENT-SOUS-5ME`.

**Nouveau livrable : `candidatures/CARTE-2026-10-21-gateau-regions-PME.pdf/.png`** — gâteau régional de la tranche 3,8–5 M€, comparaison directe avec l'univers ≥5M€ (régénération : `04_carte_simplifiee_PME.py` lisant `/tmp/seg5.pkl`, produit par la fusion des deux exports ; geojson identiques).

**Couverture restante** : 6 000/1 254 798 (0,5 %) → pour aller plus loin, **découper la requête** (par région ou NACE) avec colonnes Ville + CP conservées — `01_pipeline_geo.py`  et `04` s'appliquent ensuite tels quels.

## Chiffres clés validés (contrôle après régénération)

- Univers Orbis (actives, France, CA ≥ 5 M€, derniers comptes) : **64 646** ; hors financières (NACE 64‑66) : **61 199**
- Géolocalisées : **45 837 (70,9 %)** — ≥ 99 % par tranche ≥ 25 M$ ; validation croisée colonne région native : **98,7 %**
- Île-de-France : **14 823 sièges = 32,9 % · 5 910 Md$ = 68,1 % du CA**
- Grand Sud (NA+Occ+PACA) : **9 167 = 20,3 % · 780 Md$ = 9,0 %** (projection ~13 200 = estimation étalonnée, non nominative)
- Classes FX : CŒUR 32 994 · CONTINGENT 23 861 · DOMESTIQUE 7 791 ; prestige (≥250 M$) : 3 149

## Reconstruction (≈ 6 min, sandbox Arena)

```bash
# 1) dépendances (le /tmp des sandboxes est effacé entre sessions — tout est ici ou en ligne)
pip install pandas openpyxl pyxlsb matplotlib adjustText --target /tmp/pydeps

# 2) exports Orbis (stockés sur la branche main du repo)
cd /home/user/SKEMA-FRONT
git fetch origin main
git show origin/main:"FINAL BASEZ.xlsb"              > /tmp/final_basez.xlsb   # 45 000 × 22 col (ville siège, mEUR) — même univers, plafond export 45k
git show origin/main:"Export 20_10_2026 19_50 (1).xlsx" > /tmp/exp1950.xlsx     # 64 646 univers complet (kUSD)
git show origin/main:"Nouveau excel arena.xlsx"      > /tmp/o3.xlsx            # 10 037 (colonne région native × validation + complément petite tranche)

# 3) référentiels publics (GitHub, hôtes autorisés)
cd /tmp
curl -sL -o decoup.tar.gz https://codeload.github.com/etalab/decoupage-administratif/tar.gz/refs/heads/master && tar xzf decoup.tar.gz
curl -sL -o fgeo.tar.gz https://codeload.github.com/gregoiredavid/france-geojson/tar.gz/refs/heads/master && tar xzf fgeo.tar.gz france-geojson-master/communes-version-simplifiee.geojson france-geojson-master/regions-version-simplifiee.geojson france-geojson-master/departements-version-simplifiee.geojson

# 4) pipeline
PYTHONPATH=/tmp/pydeps python3 candidatures/ARCHIVE-carte-FX/01_pipeline_geo.py   # → /tmp/univ_xy.pkl (géocodage ville→COG→région, classes, tranches, centroïdes)
PYTHONPATH=/tmp/pydeps python3 candidatures/ARCHIVE-carte-FX/02_carte_nominative.py
PYTHONPATH=/tmp/pydeps python3 candidatures/ARCHIVE-carte-FX/03_carte_simplifiee.py
```

Contrat de sortie du script 01 (attendu) : `BASEZ: 44893 / 45000 · o3: 4883 / 10037 · univers: 64646 | géo mesurée: 45837 (70,9%) | coords: 44975`.

## Prompt prêt à coller dans une nouvelle Arena

> Régénère mes cartes du marché FX corporate France à partir de
> `candidatures/ARCHIVE-carte-FX/README.md` (repo Calvin29990/SKEMA-FRONT, branche de session).
> Lis le README, réinstalle les dépendances, rejoue 01_pipeline_geo.py puis 02/03, et pousse
> les outputs régénérés dans `candidatures/`. Pose-moi la question avant tout changement de
> contenu (seuils, couleurs, libellés). Ne modifie pas les exports sources sur `main`.

