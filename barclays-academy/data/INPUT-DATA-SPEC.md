# 📥 INPUT DATA SPEC — Ce que Calvin communique pour construire la plateforme

> Principe : **pas de plateforme générique**. Les modules, la difficulté et les drills sont générés à partir de TES performances réelles. Chaque fichier ci-dessous est simple (CSV éditable dans Excel/Google Sheets ou texte).

---

## 1. `shl_sessions.csv` — les sessions de practice (🔥 prioritaire)

Une ligne = une session de practice (mock ou exercise officiel SHL).

```csv
date,session_id,section,nb_questions,nb_correct,temps_total_min,temps_moyen_s,source,notes
2026-10-12,S001,numerical,12,8,14,70,shldirect,"fatigué après 10 questions"
2026-10-12,S002,inductive,8,5,10,75,shl_official,"patterns rotation difficiles"
2026-10-12,S003,deductive,10,7,12,72,shl_official,"calendriers OK"
```

Colonnes :
- `section` : `numerical` | `deductive` | `inductive` | `sjt` | `values_triplets`
- `source` : `shl_official` (practice de l'invitation), `shldirect`, `mock`, `testsolve`, autre
- `notes` : libre — ce que tu as ressenti

---

## 2. `error_log.csv` — le journal des erreurs (🔥 prioritaire)

Une ligne = **une erreur**. C'est le fichier le plus important : il alimente le générateur de drills.

```csv
date,session_id,section,type_erreur,cause,detail
2026-10-12,S001,numerical,calc,temps,"% de croissance : j'ai divisé par la mauvaise base"
2026-10-12,S001,numerical,lecture,inattention,"lue la colonne 2025 au lieu de 2026"
2026-10-12,S002,inductive,methode,concept,"rotation + miroir combinés, je n'ai vu que la rotation"
2026-10-12,S003,deductive,temps,panique,"2 questions sautées par manque de temps"
```

Taxonomie `type_erreur` : `calc` (calcul faux) · `lecture` (mauvaise donnée lue) · `methode` (raisonnement/règle non trouvée) · `temps` (non traité) · `panique` (pression)

---

## 3. `sjt_responses.csv` — scénarios RISES (semaine 1)

```csv
date,scenario_id,resume_scenario,ma_reponse,reponse_attendue,valeur_concernee,ecart
2026-10-14,SC01,"collègue qui livre une donnée fausse au client",B,D,Integrity,"répondu loyauté d'équipe au lieu de remonter"
```

---

## 4. `english_daily.csv` — le bloc anglais quotidien

```csv
date,minutes_input,source_input,minutes_output,enregistrement_fait,cartes_anki_nouvelles,cartes_anky_revues,collocation_notee
2026-10-12,25,FT-article-M&A,20,oui,10,35,"underpin valuations"
```

---

## 5. `captures/` — screenshots

Dossier avec captures des questions SHL/Talent Q/Immersive manquées (anonymisées, nommées `YYYY-MM-DD_session_question.png`). Elles servent à recréer des items équivalents dans la v1.

---

## 6. `report_db_feedback.md` — ✅ déjà fourni

Synthèse déjà intégrée : forces = Collaboration / Detail / Personal Responsibility ; axes = **Analysis** + **Curiosity** → priorité des drills numérique et multi-sources.

---

## Format d'envoi

- Un message avec les fichiers joints ici, ou dépôt direct dans ce dossier `barclays-academy/data/`
- Même imparfait, même partiel : **mieux vaut 3 lignes brutes aujourd'hui qu'un tableur parfait dimanche**
- Dès réception de ≥ 5 sessions → je génère : ton profil de faiblesses, la banque de drills ciblés, et le plan v1 de l'app
