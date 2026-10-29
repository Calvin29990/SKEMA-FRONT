# CV — Cléanne MINANG

CV « vitrine » d'une page, en français, pour un **premier job / une alternance**. Dossier
créé le 29 octobre 2026 pour remplacer `CV_Cléanne_MINANG.pdf` (version job étudiant, à la
racine du repo), qui reste en place mais n'est plus à jour.

## Fichiers

| Fichier | Rôle |
|---|---|
| `CV_Cleanne_MINANG.pdf` | **le livrable** — A4, une page, prêt à envoyer |
| `build_cv.py` | génère le PDF (fpdf2) ; tout le contenu éditable est dedans |
| `fonts/` | Lora + Source Sans 3, SIL Open Font License |
| `../linkedin-cleanne/A-COLLER-LINKEDIN.md` | **le texte à envoyer à Cléanne** — section par section, prêt à coller |
| `../linkedin-cleanne/LINKEDIN-CLEANNE-EN.md` | version détaillée : stratégie, ce qui a été retiré et pourquoi |

## Optimisation ATS (filtres type Deloitte / cabinets)

Le PDF est contrôlé par script : texte extractible, **aucune image**, ordre de lecture linéaire,
polices embarquées, une page. Couverture mots-clés d'une offre conseil en stratégie : **28/28**
(analyse, stratégie, résolution de problème, gestion de projet, Excel, PowerPoint, synthèse,
recherche, veille, risque, international, conseil, coordination, planification, rédaction,
sources, restitution, recommandation, géopolitique, équipe, données, statistiques, McKinsey,
Nations unies…).

Vérifier après toute modification :

```bash
python3 -c "
import pymupdf, re, unicodedata
t = pymupdf.open('documents/cv-cleanne/CV_Cleanne_MINANG.pdf')[0].get_text()
n = re.sub(r'\s+',' ', unicodedata.normalize('NFD', t.lower()))
print('mots-clés', sum(k in n for k in ['analyse','strateg','resolution de probleme']), '/3')
print('images', len(pymupdf.open('documents/cv-cleanne/CV_Cleanne_MINANG.pdf')[0].get_images()))
"
```

Deux règles ATS respectées : pas de tableau, pas de colonne, pas d'en-tête graphique. Les seuls
éléments non textuels sont deux carrés de couleur et un filet — sans impact sur l'extraction.

## Régénérer le PDF

```bash
pip install fpdf2 pymupdf
python3 documents/cv-cleanne/build_cv.py
```

Le script affiche la position du bas de texte : si elle dépasse **285 mm**, le CV déborde sur
une deuxième page. Ajuster alors la densité sans toucher au contenu :

```bash
CV_SCALE=0.97 CV_VSCALE=0.94 python3 documents/cv-cleanne/build_cv.py
```

`CV_SCALE` = taille du texte · `CV_VSCALE` = interlignage.

## Ce qui a changé par rapport à l'ancien CV

L'ancien CV était construit pour la **vente en magasin** : titre « Employée / Vendeuse
Polyvalente », bloc « disponibilités week-end », compétences caisse et mise en rayon. C'est
efficace pour un job étudiant, disqualifiant pour un premier poste.

La nouvelle version construit une **trajectoire** :

1. **McKinsey Skills for Success 2026** en premier — le signal le plus fort du profil.
2. **MUNDUS** (simulation ONU de l'Université de Lille) — rédaction, vérification des sources,
   coordination éditoriale : la preuve que le profil produit, pas seulement qu'il suit des cours.
3. **Stade Bollaert-Delelis** — conservé, mais reformulé en tenue de poste sous pression
   (3 500 spectateurs/jour), pas en « vente ».
4. **Association audiovisuelle** — conservé pour la coordination d'équipe et la formation.

Le profil, l'accroche et les compétences suivent la même ligne : analyse, gestion des risques,
communication. Le job étudiant est **assumé** dans le CV (un CV d'étudiante sans expérience
salariée paraît vide), mais il passe après ce qui distingue.

## Points à vérifier avant envoi

- [ ] **URL LinkedIn** : le CV indique `linkedin.com/in/cleanne-minang`, alors que l'URL actuelle
      du profil est `.../cléanne-minang-95772a2b0`. Choisir l'une des deux et aligner les deux
      documents (variable `CONTACT` dans `build_cv.py`).
- [ ] **Téléphone / email** : `+33 7 45 42 93 53` · `minangcalvin0@gmail.com` (repris de l'ancien
      CV — à confirmer si l'adresse a changé).
- [ ] **Niveau d'anglais** : B1 partout, y compris LinkedIn. Ne pas survendre.
- [ ] **Nom du poste chez MUNDUS** : « Pôle presse et communication » est une formulation large ;
      remplacer par l'intitulé réel si MUNDUS en a un.
- [ ] Envoyer le **PDF**, jamais un .docx qui se déforme.

## Limites assumées

- Pas de photo sur le CV (standard français pour un CV hors candidature spontanée design).
- Pas de rubrique « centres d'intérêt » développée : trois lignes suffisent, elles servent
  surtout à humaniser.
- Aucune compétence ou certification ajoutée qui ne figure pas dans les documents fournis.
