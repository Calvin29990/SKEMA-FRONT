# MÉMOS PAR TEST — Assessment Trainer (skema-training)

> **Objectif : zéro réponse au hasard à ton prochain test.** Chaque mémo = histoire / ce qui est évalué /
> ce qui est valorisé / nb de questions / vitesse / repères humains / structure / correction / pièges.
> Les mémos collent **exactement** au contenu de ton trainer (`skema-training/standalone/index.html`).

⚠️ **Trois avertissements honnêtes**
1. Ces mémos documentent **ta plateforme d'entraînement** (contenu original), PAS les tests réels UBS/BNP/Aon.
   Le jour J, tu passes seul, sans support — c'est la règle des recruteurs.
2. Les « repères humains » (dauphine, senior entraîné) sont des **ordres de grandeur indicatifs, non
   vérifiés**, donnés pour te situer. Ne les traite pas comme des statistiques officielles.
3. Les images `img/*.png` sont des **figures annotées rendues fidèlement depuis les données du trainer**
   (pas des captures d'écran pixel-perfect) : elles montrent exactement quelles cellules/points regarder
   ou ignorer. Numérique & verbal indiquent **en gras**, question par question, la cellule ou le passage à lire.

**Nouveautés v2 des mémos** : numérique = tables de référence + où regarder en gras par question + 4
graphes annotés · verbal = les 6 fiches + passage-clé en gras par question · anglais = doc auto-suffisant
(listes de mots/phrases traduites, ×2-3) · inductif/déductif/concentration/mailing = figures annotées +
items travaillés + « pourquoi cette réponse plutôt qu'une autre ».

**Légende des réponses** : TRUE = absolument vrai sur la seule base du dossier · FALSE = absolument faux ·
CANNOT SAY = on ne peut pas trancher sans info supplémentaire. **CANNOT SAY est une vraie réponse** —
c'est elle qui piège les gens qui devinent.

| # | Test | Mémo | Durée réelle | Nb |
|---|---|---|---|---|
| 1 | Anglais (3 sections) + 4 sous-docs (vocab 950 / grammaire / fautes / synonymes) | [01-anglais.md](01-anglais.md) | 4+4+2 min | ~59 items |
| 2 | Raisonnement numérique | [02-numerique.md](02-numerique.md) | 12:00 | 37 |
| 3 | Raisonnement verbal | [03-verbal.md](03-verbal.md) | 12:00 | 49 |
| 4 | Raisonnement inductif | [04-inductif.md](04-inductif.md) | 6:00 | ~8-12 |
| 5 | Raisonnement déductif (+switch) | [05-deductif.md](05-deductif.md) | 6:00 | ~12 |
| 6 | Concentration | [06-concentration.md](06-concentration.md) | 2:00 | en continu |
| 7 | Traitement de l'information (mailing) | [07-mailing.md](07-mailing.md) | 15:00 | boîte vivante |

**Méthode d'utilisation** : lis le mémo AVANT de lancer l'épreuve sur le trainer, fais une passe, puis
relis la correction en notant chaque erreur dans une colonne « pourquoi je me suis trompé ». Refais
jusqu'à 0 erreur. C'est ça, « zéro réponse au hasard ».

## Exercices volontaires (avant chaque test)

570 items corrigés, un fichier par test, **le piège indiqué à chaque item** —
dans `exos/` (et en PDF dans `pdf/` pour la lecture sur téléphone).

| Fichier | Items | Contenu |
|---|---|---|
| [exos-01-anglais.md](exos/exos-01-anglais.md) | 217 | Aisance 69 · Vocabulaire 87 · Orthographe 61 |
| [exos-02-numerique.md](exos/exos-02-numerique.md) | 65 | ROE · capitalisation · effectifs · outlook · marge |
| [exos-03-verbal.md](exos/exos-03-verbal.md) | 60 | 10 textes × 6 affirmations |
| [exos-04-inductif.md](exos/exos-04-inductif.md) | 50 | suites numériques · lettres · matrices 2×2 |
| [exos-05-deductif.md](exos/exos-05-deductif.md) | 68 | règle → cas (seuils, info manquante) |
| [exos-06-concentration.md](exos/exos-06-concentration.md) | 50 | comptage · lignes · intrus |
| [exos-07-mailing.md](exos/exos-07-mailing.md) | 60 | priorité + action (règles réelles) |

Générateur : `skema-training/scripts/gen_exos.py` (les items numériques/déductifs/concentration/mailing
sont **calculés**, donc les réponses sont vérifiables) ; PDF : `skema-training/scripts/md2pdf.py`.
