# PROMPTS.md — la bibliothèque de prompts (testés)

**Règle : un prompt sans test sur data synthétique/publique n'entre pas ici.**
**Format : contexte (2-3 lignes) | instruction | format de sortie | test (date, OK/KO).**

---

## P-01 — Audit de formule Excel
- **Contexte** : tableau {N} lignes, colonnes {liste}, formule cible {référence}.
- **Instruction** : vérifie les références absolues/relatives, les plages cassées, les arrondis incohérents, les périodes qui ne matchent pas. Liste chaque défaut + la correction.
- **Sortie** : tableau (cellule | défaut | correction | risque si non corrigé).
- **Test** : — (à tester avant usage).

## P-02 — Génération VBA
- **Contexte** : tâche répétitive décrite en 3 lignes + structure de la feuille.
- **Instruction** : écrire le code VBA commenté ligne à ligne, avec les 3 pièges classiques (scope des variables, `UsedRange` vs vraie fin de data, hardcoding de noms de feuilles).
- **Sortie** : code bloc + liste des pièges à vérifier avant de coller.
- **Test** : — (à tester avant usage).

## P-03 — Pipeline Python (pandas)
- **Contexte** : dataset de `SYNTHETIC/` (nom + colonnes) + résultat attendu.
- **Instruction** : écrire le pipeline pandas ; après chaque étape intermédiaire, afficher la forme et 3 lignes d'exemple.
- **Sortie** : code + assertions (checks) qui prouvent le résultat attendu.
- **Test** : — (à tester avant usage).

## P-04 — Synthèse de fiche (trader)
- **Contexte** : fiche/notes brutes fournies + le mapping fiche→desk voulu.
- **Instruction** : extraire les formules et conventions, les reformuler en notation unique, signaler chaque ambiguïté ou manque.
- **Sortie** : fiche structurée (formule | convention | ambiguïté | source dans le texte).
- **Test** : — (à tester sur la synthèse Christian du 26/09).

## P-05 — Chasse aux hallucinations
- **Contexte** : réponse précédente de l'IA sur {sujet} + les données fournies.
- **Instruction** : relis ta réponse ; signale chaque affirmation qui n'est pas dans les données fournies ; marque [VÉRIFIÉ] / [À VÉRIFIER] / [HALLUCINATION].
- **Sortie** : liste classée des 3 pires risques, avec la ligne exacte incriminée.
- **Test** : — (à tester avant usage).
