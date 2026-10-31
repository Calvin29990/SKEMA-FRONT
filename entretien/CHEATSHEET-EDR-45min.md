# CHEAT-SHEET — EdR Middle Office Structurés · à relire dans les 45 min

## 1. Les 3 pitchs (à dire, pas à lire)

**« Parlez-moi de vous » (45 s)**
> « M2 marchés à SKEMA. Six mois chez BPCE en reporting dérivés multi-actifs : taux, FX, indices, P&L et sensibilités. Et un outil de pricing/stress d'options pétrole codé de A à Z, du Black-76 à l'attribution du P&L par grecque. **C'est le croisement que je cherche : comprendre le payoff et sécuriser le trade.** »

**« Pourquoi le middle office ? » (30 s)**
> « Parce qu'on ne regarde pas un prix pour le commenter, on le contrôle. Prix, grecs, barrière, flux — et savoir dire non. Technique + rigueur opérationnelle, plus qu'un rôle commercial. »

**« Pourquoi EdR ? » (35 s)**
> « Une maison indépendante où le structuré est un outil patrimonial, pas un volume. Un groupe qui grossit : 198 Md CHF d'encours, 10 Md de collecte en 2025. Et une culture du produit maison : structurer, pricer, suivre le cycle de vie. »

**Secours si je sèche :** « Je ne l'ai pas pratiqué en production, mais voilà comment je le comprends : … Est-ce que c'est bien comme ça ici ? »

---

## 2. Définitions en 1 ligne (réciter dans cet ordre)

- **Structuré** = zéro-coupon (bond floor) + options → payoff conditionnel.
- **Forward** = contrat OTC ferme à prix fixé, valeur nulle au départ ; F = S·e^((r−q)T).
- **Future** = même logique, standardisé et compensé, avec appels de marge.
- **Call / Put** = droit d'acheter / vendre à un strike, à une échéance.
- **Call ATM** = strike = spot → valeur 100 % temps, delta ≈ 0,5, gamma et vega maximaux.
- **Delta** = variation du prix pour +1 de spot ; aussi le ratio de couverture.
- **Gamma** = variation du delta ; la convexité, forte ATM proche échéance.
- **Vega** = sensibilité à +1 pt de vol implicite.
- **Theta** = perte de valeur temps par jour.
- **Rho** = sensibilité aux taux (essentiel sur les maturités longues).
- **Vol implicite / réalisée** = prix du risque futur / ce qui s'est passé ; l'écart = P&L de couverture.
- **Skew** = les puts OTM sont plus chers que les calls : prime au risque de krach.
- **Autocall** = rappel anticipé si le sous-jacent dépasse un seuil à une date d'observation.
- **Phoenix** = autocall + coupons périodiques conditionnels avec mémoire.
- **Worst-of** = payoff indexé sur le pire titre du panier : plus de coupon, plus de risque.
- **Barrière** = niveau qui active/désactive coupon, rappel ou protection.
- **Marge de structuration** = écart entre le prix payé (100 %) et la valeur de marché réelle.
- **Break** = écart non expliqué entre deux sources → qualifier, expliquer, escalader.
- **PnL explain** = delta + gamma + vega + theta + carry + fees, le reste = inexpliqué.
- **IPV** = vérification indépendante des prix et paramètres.
- **T+1 Europe** = 11/10/2027 ; échéance ESMA allocations/confirmations = 07/12/2026.

---

## 3. Cinq chiffres EdR (et pas un de plus)

1. **198 Md CHF** d'encours fin 2025 (+8 %, record).
2. **> 10 Md CHF** de collecte nette 2025 (+5,5 %).
3. **107 Md€** gérés par EdR AM (+5,4 Md€ collectés en 2025, 5e année positive).
4. **73 M CHF** de résultat net 2025 ; solvabilité **19,1 %**.
5. **2026 = centenaire** d'Edmond de Rothschild (né le 30/09/1926).

**Trois actus :** CACEIS élargit le partenariat *asset servicing* au Luxembourg (09/10/2026) · REIM lance une stratégie logistique *value-add* (21/09/2026) · EdR AM accélère dans le quant et prépare des ETF actifs (juin 2026).

---

## 4. Trois phrases de marché (octobre 2026)

- **BCE +25 pb en septembre 2026**, inflation zone euro ~3,3 %, ton encore prudent.
- **OAT-Bund à 172 pb**, record : incertitude budgétaire française.
- **Énergie / Ormuz** : prix du pétrole soutenus, risque de stagflation en Europe.

**Traduction structurés :** taux hauts → protection moins chère ; vol et dispersion → coupons plus élevés mais barrières plus risquées ; pression AMF sur les coûts → la marge doit être justifiée.

---

## 5. Trois questions à poser

1. « Quelle est la répartition réelle entre contrôle prix/grecs, cycle de vie et reporting ? »
2. « Quels outils au quotidien — Sophis, Calypso, Murex, Python — et quelle place du scripting ? »
3. « Qu'est-ce qui distingue un bon stagiaire dans votre équipe au bout de trois mois ? »

---

## 6. Ma règle unique

**3 phrases. Je m'arrête. Je regarde la personne.**
