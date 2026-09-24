# LABO/ — le second cerveau (méthode, pas données)

**Ligne rouge (relire avant chaque commit) : ici il n'y a que MÉTHODE — code, prompts, corrections, data SYNTHÉTIQUE ou PUBLIQUE. JAMAIS de donnée PROD (clients, positions, transactions, documents internes) sur ce repo.**

## Structure

```
LABO/
  NOTEBOOKS/       # .ipynb Python + VBA .bas/.xlsm — data SYNTHÉTIQUE uniquement
  SYNTHETIC/       # datasets synthétiques + réponses « attendues » calculées à la main
  PROMPTS.md       # bibliothèque de prompts (chacun testé avant d'entrer ici)
  CORRECTIONS.md   # log d'hallucinations — 1 ligne par erreur (l'actif compound)
```

## Boucle de travail (à chaque session)

1. Ouvrir `CORRECTIONS.md` **avant** de lancer l'IA.
2. Choisir un prompt dans `PROMPTS.md` (sinon en écrire un et le tester).
3. Produire sur `SYNTHETIC/` — comparer à la réponse « attendue ».
4. Loguer chaque écart (1 ligne dans `CORRECTIONS.md`).
5. Itérer jusqu'à zéro écart. Commit.

## Projet n°1 : tracker Atos (data PUBLIQUE — cours, dilution, effectifs, liquidité)

- Sert à la fois le LABO (premier pipeline) et le réseau (conversation François Henry, vague du 24/11).
- Data publique = OK ici. La discipline = la même que sur du synthétique : réponses attendues + log de corrections.
