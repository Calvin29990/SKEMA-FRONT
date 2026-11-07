# Capital Budgeting — QCM clés, méthodes et pièges

Sélection commentée des cinq fichiers QCM disponibles, questions repérées par numéro et page. Montants dans la monnaie du sujet ; M = million. Les résultats sont recalculés, pas seulement recopiés. [Cours](01-resume-cours.md) · [Mémo](03-memo-examen.md).

## Méthode générale

1. Lire « TRUE/FALSE », l'horizon, les unités, l'impôt et la date des flux.
2. Poser « avec − sans », puis écrire les flux sur une ligne de temps. Distinguer valeur comptable, valeur de marché, bénéfice et cash.
3. Identifier le modèle et ses hypothèses ; afficher la formule avant d'arrondir. Si les choix ne concordent pas, vérifier les données plutôt que forcer un résultat.

## Step 1 — Cash flows

Source : [Step 1 Q MCQ](../../Step%201%20Q%20%20MCQ.pdf).

- **Q4, p. 1–2 — baisse du prix, réponse A.** Ancienne marge : `100 000 × (129−50) = 7,90 M`. Nouvelle : `130 000 × (99−50) = 6,37 M`. Variation d'EBIT = **−1,53 M**, soit une baisse d'environ 1,5 M. Piège : hausse du volume ≠ hausse de profit ; comparer les deux situations complètes.
- **Q6, p. 2 — terrain, A.** Coût d'opportunité initial = **650 000**, montant de vente sacrifié, et non valeur comptable de 100 000. L'énoncé ignore l'impôt ; sinon raisonner en produit de vente après impôt.
- **Q7, p. 2–3 — BFR, A.** Ventes année 1 = `2 000 × 18 = 36 000` ; BFR = `(2%+4%+9%−5%) × 36 000 = 3 600`. Piège : les dettes fournisseurs se soustraient. Pour le FCF on utilise **la variation** du BFR, pas son niveau.
- **Q8, p. 3–4 — FCF, C.** `EBIT = 100 000−50 000−30 000 = 20 000` ; résultat non endetté `20 000 × 0,79 = 15 800` ; `FCF1 = 15 800+30 000−5 000 = 40 800`. Piège : l'amortissement réduit l'impôt mais n'est pas une sortie de cash ; le signe donné pour le BFR est déjà négatif.
- **Q9, p. 4 — remplacement, C.** Ancien actif : valeur comptable `50 000 − 2 × 5 000 = 40 000`. Vente 30 000 : économie fiscale `21% × 10 000 = 2 100`. `CF0 = −80 000+30 000+2 100 = −47 900`, sous réserve de pouvoir utiliser la perte. Ne pas déduire à nouveau l'ancien coût historique.
- **Q10–12, p. 4–5 — boucliers.** Amortissement linéaire `540 000/3 = 180 000` ; économie annuelle `×21% = 37 800` (Q10 A). Pour les pertes reportables, `320/(100×80%) = 4 ans` (Q11 C) et `PV = 16,8 × [1−1,10^−4]/0,10 ≈ 53,25 M` (Q12 A). Piège : une perte fiscale de 320 M n'est pas une économie de 320 M et peut être plafonnée.
- **Q13–14, p. 5 — risque.** Plusieurs hypothèses modifiées simultanément = scénario ; une seule à la fois = sensibilité. Distinguer la variation de la VAN de la probabilité des scénarios.

## Step 2 — VAN, TRI, sélection

Source : [Step 2 Q MCQ](../../Step%202%20Q%20%20MCQ.pdf).

- **Q2, p. 1 — coût d'opportunité, D.** Encaisser 11 M aujourd'hui contre renoncer à 8 M à t=1 : `VAN = 11 − 8/1,10 = 3,727 M`. Piège : 11−8 ne tient pas compte de la date.
- **Q3 et Q6, p. 1–3 — VAN et TRI, A et C.** Flux `−450 000 ; 200 000 ; 225 000 ; 275 000 ; 200 000` : à 16 %, `VAN ≈ 176 265` ; `TRI ≈ 34,12 %`. Le corrigé de Q3 écrit par erreur 1,15 à certaines années : utiliser **1,16 à toutes les années**. Q11 comporte aussi une coquille de 2 000 000 au lieu de 200 000 en année 4.
- **Q4, p. 1–2 — fréquence, D.** Avance 30 000 aujourd'hui, coût d'opportunité 2 000 en fin de mois pendant 12 mois. `rm = 1,12^(1/12)−1 ≈ 0,9489 %` ; `VAN = 30 000−2 000 × [1−(1+rm)^−12]/rm ≈ 7 417`. Ne pas diviser mécaniquement un taux annuel **effectif** par 12.
- **Q7–8, p. 3 — payback, C puis B.** `100/16 = 6,25 ans` en payback simple. Le coût de restauration en année 12 arrive après la récupération : le payback l'ignore, contrairement à la VAN. Il ne tient pas compte de l'actualisation.
- **Q9, p. 3–4 — exclusivité, C.** À 15 %, `VAN A ≈ 12,04`, `VAN B ≈ 12,65` : choisir **B**, VAN positive la plus élevée. Ici B a aussi le TRI le plus élevé, mais ce n'est pas la justification générale.
- **Q10–11, p. 4–5 — ressources, A puis C.** Selon la convention du cours `IP = VAN/investissement = 176 265/450 000 ≈ 0,39`. Classer par ordre décroissant, puis vérifier les combinaisons de projets indivisibles ; certaines sources définissent l'indice autrement.

## Step 3 — Coût du capital

Source : [Step 3 Q MCQ](../../Step%203%20Q%20%20MCQ.pdf).

- **Q1 et Q9–10, p. 1–4 — risque et régression.** Le risque total est la volatilité ; bêta = pente de la régression sur les rendements excédentaires du marché. La mesure passée est une estimation, pas une certitude future. Ne pas substituer volatilité au bêta dans le CAPM.
- **Q11–12, p. 4–5 — dette, B et D.** Avec `rf=3 %`, `βD=0,1`, prime de marché 5 %, `rD = 3%+0,1×5% = 3,5%`. Autre estimation simplifiée à partir du YTM : `7%−0,5%×70% = 6,65%`. Ce sont deux méthodes et hypothèses différentes ; le YTM promis n'est pas forcément le rendement attendu.
- **Q15, p. 6 — cash et bêta opérationnel.** `E=50`, `D=30`, `cash=8` milliards ; βE=1,15, βD=0,10, βcash=0. `βop = (50×1,15+30×0,10−8×0)/(50+30−8) ≈ 0,840`. Le QCM retient l'option **A (0,83)** via une approximation dette nette : `(50×1,15+22×0,10)/72 ≈ 0,829`. Les deux méthodes reposent sur des hypothèses différentes sur le risque de la dette nette.
- **Q16, p. 6 — comparable, B.** Capitalisation `25×16 = 400 M` ; dette 220 M ; `βU = (400×1,18+220×0,08)/620 ≈ 0,790`. Utiliser les valeurs de marché et tenir compte du bêta de la dette.
- **Q17, p. 6–7 — levier opérationnel, B.** À risque des ventes constant, une proportion supérieure de coûts fixes amplifie la sensibilité du résultat au marché. Ce n'est pas la même chose que le levier financier.

## Step 4A — Modigliani–Miller sans impôt

Source : [Step 4A Q and MCQ](../../Step%204A%20Q%20and%20MCQ.pdf).

- **Q9, p. 3–4 — répartition des flux.** Dette 10 000, intérêt 5 % : dette reçoit 500. Pour FCF 1 000 ou 2 000, actions endettées reçoivent respectivement **500 ou 1 500** ; sans dette elles reçoivent 1 000 ou 2 000. Les flux totaux sont identiques, mais l'action endettée est plus risquée.
- **Q10, p. 4 — coût des fonds propres, C.** `rU=12 %`, `rD=6 %`, `D/E=0,5` : `rE = 12%+0,5×(12%−6%) = 15%`. Piège : 0,5 est D/E, pas D/V ; formule ici en marché parfait sans impôt.
- **Q13, p. 5 — valeur d'entreprise, A.** Valeur totale de marché 20 Md dont cash 4 Md : valeur opérationnelle **16 Md**. Formule générale `E+D−cash` ; vérifier ce que l'énoncé appelle « market value ».
- **Q14–15, p. 5 — EPS, C puis D.** Avant : `20 M/8 M = 2,50`. Après emprunt de 50 M à 8 % et rachat à 20 : actions `8−50/20=5,5 M`, résultat `20−4=16 M`, EPS `16/5,5 ≈ 2,91`. Piège : hausse d'EPS ne démontre pas hausse du prix, car le risque augmente.
- **Q16, p. 6 — cours inchangé.** Rose : avant, `EPS=6/5=1,20`, `rU=1,20/12=10%`. Dette 12 M, rachat d'1 M d'actions ; `rE=10%+(12/48)×(10%−6%)=11%`, nouvel EPS `(6−0,72)/4=1,32`, donc `prix=1,32/0,11=12`. Hypothèses : sans impôt, dividendes perpétuels et bénéfices constants.

## Step 4B — Dette et impôts

Source : [Step 4B Q and MCQ](../../Step%204B%20Q%20and%20MCQ.pdf).

- **Q1–3, p. 1 — bouclier, B, B, D.** EBIT 450 M, intérêts 175 M, impôt 21 % : résultat endetté `(450−175)×0,79=217,25 M` ; investisseurs `217,25+175=392,25 M` ; sans dette `450×0,79=355,50 M`. Différence `36,75 M = 175×21%`. Ne pas confondre résultat des actionnaires et montant total aux investisseurs.
- **Q4, p. 2 — incohérence du corrigé.** Avec WACC avant impôt 14 %, D/V 0,5, rD 7 %, T 21 %, `WACC après impôt = 14%−0,5×7%×21% = 13,265%`. L'option la plus proche est **C : 13,0 %**, non B : 12,8 % indiqué dans le PDF. Le calcul du corrigé donne lui-même 13,265 % mais omet le poids 0,5 dans son écriture.
- **Q6, p. 2 — ratio, C.** `16% − (1/3)×9%×21% = 15,37% ≈ 15,4%`. Ne pas oublier le poids de dette ; le corrigé l'omet dans sa formule imprimée.
- **Q9–10, p. 3–4 — dette/fonds propres.** `D/E=0,5` implique `D/V=1/3`, `E/V=2/3`. WACC avant impôt `2/3×13%+1/3×7%=11%` (Q9 B) ; `VU=8/(11%−3%)=100 M` (Q10 B), flux perpétuel croissant sous les hypothèses de l'énoncé.
- **Q11, p. 4 — risque du bouclier, C.** Dette permanente 70 M, coupon 8 %, impôt 21 %, taux du bouclier 6 % : `PV = 70×8%×21%/6% = 19,6 M`. Ici **T×D = 14,7 M est incorrect** car le taux de risque du bouclier diffère du taux de la dette.
- **Q13–14, p. 5 — dette permanente, C puis D.** `VU=10/10%=100 M` ; `PV bouclier=40×21%=8,4 M` ; `VL=108,4 M`. Cette simplification suppose bouclier permanent pleinement utilisable et risque approprié.
- **Q16–17, p. 5–6 — fiscalité personnelle, C puis B.** Taux personnel actions moyen `Te=(40%+20%)/2=30%` selon l'hypothèse du sujet. Taux combiné actions `1−(1−35%)(1−30%)=54,5%` ; avantage relatif dette `T* = 1−[(1−35%)(1−30%)/(1−40%)] ≈ 24,17%`. Ne pas additionner simplement les taux.

## Step 5 — entraînement conceptuel

Aucun fichier QCM Step 5 n'est présent dans les documents fournis. À partir du [support Step 5](../../Capital%20budgeting%20Step%205.pptx), s'entraîner sur :

1. **Une perte pour un créancier est-elle toujours un coût de détresse ?** Non : un transfert entre investisseurs ne détruit pas nécessairement de valeur ; une perte de clients ou des frais juridiques, oui.
2. **Pourquoi refuser un projet à VAN positive ?** En situation de debt overhang, les actionnaires paient l'investissement mais une partie importante de son bénéfice revient aux créanciers.
3. **Pourquoi choisir un projet trop risqué ?** Responsabilité limitée : les actionnaires profitent du potentiel de hausse tandis qu'une part des pertes incombe aux créanciers. Les covenants peuvent limiter ce conflit, au prix d'une moindre flexibilité.
