# Carte interactive + Excel / Power BI

Tout est dans le repo public `Calvin29990/SKEMA-FRONT`.

---

## 1. Les liens

### Carte interactive (aucune installation)

**Lien direct, version qui s'ouvre dans le navigateur :**

```
https://htmlpreview.github.io/?https://github.com/Calvin29990/SKEMA-FRONT/blob/arena/b1d047d9-skema-front/docs/index.html
```

**Lien GitHub (code source de la page) :**

```
https://github.com/Calvin29990/SKEMA-FRONT/blob/arena/b1d047d9-skema-front/docs/index.html
```

> J'ai tenté d'activer GitHub Pages directement : l'API répond `403 — Resource not accessible by integration`,
> les droits du jeton de cette session ne couvrent pas les réglages Pages. À faire en 30 secondes côté interface,
> voir la section 5 — ça te donne une URL propre du type `https://calvin29990.github.io/SKEMA-FRONT/`,
> beaucoup plus présentable dans un post LinkedIn que le lien `htmlpreview`.

### Données téléchargeables

| Format | Lien | Usage |
|---|---|---|
| Classeur Excel (3 onglets) | `https://github.com/Calvin29990/SKEMA-FRONT/raw/arena/b1d047d9-skema-front/linkedin/2026-10-23-FX-football/data/carte-FX.xlsx` | Excel 3D Maps, tableaux croisés |
| CSV clubs & FX | `https://github.com/Calvin29990/SKEMA-FRONT/raw/arena/b1d047d9-skema-front/linkedin/2026-10-23-FX-football/data/clubs_partenaires_fx.csv` | Power BI, Tableau |
| CSV entreprises agrégé | `https://github.com/Calvin29990/SKEMA-FRONT/raw/arena/b1d047d9-skema-front/linkedin/2026-10-23-FX-football/data/entreprises_par_region.csv` | carte choroplèthe |

Aperçu statique de la carte : `assets/04-carte-interactive-preview.png`

---

## 2. Ce que contient la carte

**Deux couches, deux niveaux de granularité.**

**Couche 1 — les entreprises : agrégées, jamais nommées.**
13 régions, 5 classes de densité, aucun nom, aucune commune, aucun montant.
C'est exactement ta règle : « je sous-entends que j'ai fait des recherches, je ne donne pas mes données ».

**Couche 2 — les clubs : nommés, mais uniquement sur source publique.**

| Club | Partenaire FX | Rôle annoncé | Date | Source |
|---|---|---|---|---|
| Olympique Lyonnais | **Ebury** | Partenaire Officiel Fintech / FX | 28/10/2025 | ol.fr |
| AS Monaco | **Ebury** | Partenaire fintech / FX | 10/09/2024 | asmonaco.com |
| AS Monaco | **Sokin** | Official Global Payments & FX Partner | 08/06/2021 | asmonaco.com |
| Olympique de Marseille | **Ebury** | Fournisseur officiel (paiements, FX) | 07/01/2026 | La Provence |
| Toulouse FC | **Corpay Cross-Border** | Fournisseur officiel de services de change | 20/02/2025 | Business Wire |
| Stade de Reims | **Ebury** | Partenaire Premium | 09/07/2025 | stade-de-reims.com |

Hors France (mentionnés en liste, pas sur la carte) : Servette, Botafogo, Parma, Cluj, Fulham, Aston Villa,
Southampton, Rangers, PSV, Copenhague (Ebury) · Everton, Fulham (Sokin) · Everton (CMC Markets),
Nottingham Forest (Marex), Hearts (OFX).

---

## 3. Deux corrections importantes sur l'angle « top 5 fintech »

Tu voulais écrire : « le top 5 des fintech sont clients de l'AS Monaco, de Toulouse ou de Lyon ».
Après vérification, c'est **vrai sur le fond mais faux sur la formulation**, et il faut corriger sinon un RH
de Convera ou d'iBanFirst te reprend en commentaire.

**Ce qui est vrai :**
- **Ebury** est présent chez 4 clubs français : OL, AS Monaco, OM, Stade de Reims. Plus une division
  « Ebury Sports » dédiée, dirigée par Maurits Zwart.
- **Sokin** (fintech paiements UK) était le partenaire paiements/FX officiel de l'AS Monaco (2021-2024)
  et de Fulham et Everton.
- **Corpay Cross-Border** (NYSE : CPAY) est fournisseur officiel FX du Toulouse FC.

**Ce qui est faux :**
- **iBanFirst n'a aucun partenariat club de football public.** Aucune annonce trouvée. Si tu l'écris,
  c'est le seul point qui peut te coûter l'entretien.
- **Convera** n'a pas non plus de partenariat club public identifié (partenariats logiciels et
  institutionnels uniquement).
- Les clubs cités ne sont pas « clients » des fintechs au sens comptable : ce sont des **partenariats
  de sponsoring** qui incluent une brique de service FX. La nuance est importante, et elle est
  justement intéressante à défendre : le sponsoring est le cheval de Troie commercial.

**Formulation à utiliser à la place :**

> Trois des grands acteurs du change B2B — Ebury, Corpay et Sokin — sont déjà visibles dans le football
> français : Ebury chez Lyon, Monaco, Marseille et Reims, Corpay chez Toulouse, Sokin chez Monaco.
> Sept des douze clubs de Ligue 1 que j'ai regardés n'ont, à ce jour, aucun partenaire FX annoncé.

C'est plus fort que « le top 5 », parce que c'est vérifiable, et ça laisse une place vide — celle que
Convera ou iBanFirst pourraient occuper. C'est exactement l'argument qui intéresse un commercial.

---

## 4. Utiliser la carte dans Excel / Power BI

**Excel 3D Maps :** ouvrir `carte-FX.xlsx` → onglet `Clubs & FX` → Insertion > Carte 3D → Nouvelle visite →
glisser `latitude` en Y, `longitude` en X, `fintech_ou_prestataire_fx` en Catégorie.
Attention : 3D Maps attend des colonnes nommées explicitement, d'où les en-têtes anglais.

**Power BI :** Obtenir les données > Fichier CSV → `clubs_partenaires_fx.csv`.
Visuel « Carte » avec latitude/longitude, ou « Carte choroplèthe » en important aussi
`entreprises_par_region.csv` et en reliant la colonne `region` au référentiel géographique français.

**Pourquoi deux fichiers :** si tu donnes la carte détaillée à quelqu'un, il peut la republier.
Si tu donnes un CSV agrégé + un CSV de clubs sourcés, il peut vérifier ta méthode sans récupérer ton travail.

---

## 5. Activer GitHub Pages (30 secondes, côté interface)

1. https://github.com/Calvin29990/SKEMA-FRONT/settings/pages
2. **Source** : `Deploy from a branch`
3. **Branch** : `arena/b1d047d9-skema-front` · **Folder** : `/docs`
4. Save → attendre ~1 minute.

URL obtenue : `https://calvin29990.github.io/SKEMA-FRONT/`

> Point de vigilance : la branche `arena/...` est une branche de travail. Si elle est supprimée ou
> renommée plus tard, la page tombe. Si tu veux la garder en ligne durablement, fusionne-la dans `main`
> d'abord, puis pointe Pages sur `main /docs`.

---

## 6. Ce qui n'est pas dans la page (volontairement)

- Les 170 noms d'entreprises de ton visuel d'origine.
- Les communes et les codes INSEE.
- Les montants société par société.
- Le croisement flux récurrents / flux épisodiques.
- Toute donnée client ou sous licence nominative.

Le script `build_map.py` régénère page + CSV + Excel depuis les mêmes données : si tu veux ajouter un
club, tu l'ajoutes dans la liste `CLUBS` avec sa source, tu relances, et tout se met à jour.
