# CORRECTIONS.md — le log d'hallucinations (l'actif compound)

**Règle : 1 ligne par erreur. Chaque session : relire ce fichier AVANT de lancer l'IA.**
**Test de régression : reposer la même question, vérifier que la correction tient. Si elle ne tient plus, ajuster le prompt dans PROMPTS.md.**

| date | ce que l'IA a fait | ce qu'il faut faire | pourquoi |
|---|---|---|---|
| 24/09/2026 | *(exemple de format)* L'IA a appliqué un WACC avant de normaliser les résultats | Normaliser d'abord (one-offs, restructuration), WACC ensuite | La normalisation change le multiple ; l'ordre inverse fausse la valeur |
| 24/09/2026 | *(exemple de format)* L'IA a cité un nom de plan SG non confirmé | Ne jamais citer un nom de plan non confirmé ; renvoyer à la source | Risque de hallucination de marque — vérifié, jamais confirmé |
