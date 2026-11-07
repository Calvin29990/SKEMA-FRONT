# Capital Budgeting — mémo à relire le jour J

[Résumé complet](01-resume-cours.md) · [QCM expliqués](02-exercices-qcm.md)

## Les 10 réflexes

1. **Avec projet − sans projet** : coûts d'opportunité et cannibalisation en marge oui ; sunk costs et frais inchangés non.
2. **FCF ≠ bénéfice** : `FCF = EBIT(1−T) + amortissement − CAPEX − ΔBFR` ; `ΔBFR = BFR fin − BFR début`. Une hausse de BFR consomme du cash.
3. Amortissement : bouclier `T × amortissement`, s'il est utilisable. Produit de cession après impôt `prix − T(prix−valeur comptable)`.
4. FCF non endetté : **pas d'intérêts ni remboursement**. Ne pas compter deux fois le bouclier fiscal.
5. `VAN = Σ FCFt/(1+r)^t` : indépendant, accepter si VAN > 0 ; projets exclusifs, choisir la plus grande VAN positive.
6. TRI : VAN = 0. Règle TRI > r seulement pour flux conventionnels et TRI unique ; plusieurs changements de signe = prudence. Payback ignore temps et flux ultérieurs.
7. Ressource rare : `indice = VAN/ressource` selon le cours ; trier décroissant puis tester les combinaisons si projets indivisibles.
8. `rE = rf + βE × prime de marché` : bêta = risque systématique ; volatilité = risque total. YTM de dette risquée ≠ rendement attendu.
9. Poids en **valeurs de marché** : `E/V` et `D/V`, V = E+D. Si D/E = 0,5, alors D/V = 1/3, pas 1/2.
10. Dette : avantage fiscal **contre** coûts de détresse et d'agence ; plus de levier n'est pas toujours mieux.

## Formules à reconnaître

| Sujet | Formule et condition |
|---|---|
| WACC après impôt | `(E/V)rE + (D/V)rD(1−T)` ; taux et poids cohérents avec le projet et la politique de dette |
| MM II sans impôt | `rE = rU + (D/E)(rU−rD)` ; marché parfait |
| Bêta des actifs | `βU = (EβE + DβD)/(E+D)` ; sans cash excédentaire, cadre sans impôt |
| Valeur opérationnelle | `E + D − cash excédentaire` |
| Bouclier intérêts | `T × intérêts`, si pleinement déductibles et utilisables |
| APV | `VL = VU + PV(boucliers)` si pas d'autres effets ; actualiser selon leur risque |
| Dette permanente | `PV(bouclier) = T×D` uniquement sous les hypothèses de dette et bouclier permanents, pleinement utilisables et risque approprié |
| Perpétuité croissante | `PV = FCF1/(r−g)`, si r > g |
| Annuel effectif → mensuel | `rm = (1+ra)^(1/12)−1` |
| Fiscalité personnelle | `T* = 1 − [(1−Tc)(1−Te)/(1−Ti)]` |

## Pièges flash

- Prix de vente d'un actif ≠ valeur comptable ; inclure l'impôt sur gain ou perte.
- `D/E` ≠ `D/V` ; coût de la dette après impôt utilise **1−T**, pas 1+T.
- Un EPS supérieur après rachat à crédit ne prouve pas une création de valeur : le risque des actions peut augmenter.
- Défaut : transfert créanciers/actionnaires ≠ coût de détresse ; perte de clients et frais de procédure = coûts réels.
- **Risk shifting** : trop de risque ; **debt overhang** : renoncement à un bon projet ; covenants : protection mais rigidité.
- QCM Step 4B Q4 : les données donnent **13,265 %**, réponse la plus proche C (13,0 %), malgré la lettre B du corrigé.

## Stratégie QCM

Lire « FALSE » / « NOT », repérer t=0, dates et unités, écrire la formule, vérifier les signes et arrondir à la fin. La capture K2 indique pour le test officiel Steps 1–3 : 30 questions en 50 minutes, une seule bonne réponse, navigation libre et pas de point négatif. Le support d'introduction indique d'autres modalités : **vérifier K2 pour l'épreuve concernée**, sans supposer que cette capture s'applique au final ou aux Steps 4–5.
