# MÉMO — MONEY, BANKING AND FINANCIAL MARKETS (Dhafer SAIDANE)

> **Syllabus vérifié :** `cours/syllabus_MONEY, BANKING AND FINANCIAL MARKETS - Dhafer SAIDANE (104632202260SM1).pdf`.
> **Évaluation : examen final 100 %** (pas de continu). **Calculatrice imposée : TI BA II Plus physique** (pas l'app) — la même que le CFA.
> **Format :** sessions 1 et 7 en full cohort, sessions 2-6 **en groupes** → c'est un cours interactif : la participation se voit,
> et c'est exactement le type de cours où Saïdane repère les étudiants motivés (utile pour ton projet de thèse, voir `THESE-SAIDANE-pitch.md`).

---

## 1. La carte du cours (7 sessions)

| S | Thème | À maîtriser (ce qui se teste) |
|---|---|---|
| 1 | Money + vue d'ensemble | Définition/fonctions/création de la monnaie, masse monétaire ; money vs capital markets ; structure d'une banque d'investissement ; origination/sales/trading ; primaire vs secondaire ; syndication ; asset classes |
| 2 | Bilan bancaire + régulation + valeur temps | Actifs/passifs/capital d'une banque ; **Bâle** (CAR, liquidité), dépôt insurance, KYC/FATCA/MIFID-2, AML ; **intérêt simple (money market)** vs **composé (capital market)** ; conventions de marché |
| 3 | Money market + titrisation + obligations | Instruments escomptés vs à intérêt ; **taux forward** ; **repo** ; equity/loan/debt financing ; CMO/CCR/CLN ; subprime → crise ; Eurobonds ; terminologie US (WI, on/off-the-run) |
| 4 | Pricing obligataire | Prix d'un bond annuel ; **accrued interest** ; **duration** (sensibilité) & **convexité** (courbure) |
| 5 | Futures & options (bases) | Margining/gearing, CCP ; **pricing cash-and-carry** ; 4 positions de base (long/short call/put) ; **binomial** → Black-Scholes ; Grecques (delta, gamma, theta, vega, rho) |
| 6 | Stratégies options + parity | Straddle/strangle/spreads/butterfly/(condor) ; **put-call parity** (future synthétique, arbitrage) ; ajustement dynamique vue volatilité/direction ; repo sell-buy-back & securities lending |
| 7 | Révision + produits structurés + macro | Produits structurés à capital protégé/levier/participation ; indicateurs macro (démographie, PPP, inflation, PIB, emploi, commodities) ; intégration des marchés |

---

## 2. Les 12 réflexes « banque & marchés » (ce que Saïdane veut entendre)

1. **La monnaie** : unité de compte / réserve de valeur / moyen d'échange ; créée surtout par le **crédit bancaire**, pas par la planche à billets.
2. **Money market** = court terme, **intérêt simple** ; **capital market** = long terme, **intérêt composé**. Ne jamais mélanger les conventions.
3. **Une banque = un bilan** : elle transforme des échéances et porte du risque ; le capital (CAR Bâle) absorbe les pertes, la liquidité (LCR/NSFR) évite la course au guichet.
4. **Repo** = un prêt collatéralisé (vente + rachat) : le taux repo ≈ taux sans risque de marché ; c'est l'outil de politique monétaire.
5. **Titrisation** : transfère le risque de crédit hors du bilan ; le subprime a montré que le risque **mal réparti** devient systémique.
6. **Prix d'un bond** = somme des flux actualisés ; le prix bouge **inversement** au taux ; **duration** = sensibilité au 1er ordre, **convexité** = au 2e (la convexité est amie de l'investisseur).
7. **Accrued interest** : l'acheteur paie au vendeur les intérêts courus → prix « dirty » = prix « clean » + accrued.
8. **Futures** : prix théorique = spot × (1 + r − carry) (cost of carry) ; la **base** se resserre vers 0 à l'échéance.
9. **Put-call parity** : C − P = S − PV(K) ; toute violation = arbitrage ; elle crée le **future synthétique**.
10. **Grecques** : delta (direction), gamma (accélération du delta), theta (découragement temps — l'acheteur d'option paie theta), vega (volatilité), rho (taux).
11. **Straddle** = pari sur la **volatilité** (direction indifférente) ; **spreads** = pari directionnel à coût limité ; **butterfly** = pari sur une zone de prix.
12. **Macro** : les marchés intègrent inflation + taux centraux + emploi ; un indicateur ne se lit jamais seul, mais **contre les attentes**.

---

## 3. Formules minimum viables (TI BA II Plus en main)

| Bloc | Formule / touche |
|---|---|
| Intérêt simple (MM) | I = P × r × (jours/convention) — conventions 360 (USD) / 365 (GBP) / ACT/360 EUR money market |
| Intérêt composé | FV = PV(1+r)ⁿ — touches N, I/Y, PV, FV |
| Prix bond | PV des coupons + PV du nominal ; semi-annuel : N×2, I/Y÷2, PMT÷2 |
| Duration | ΔP/P ≈ −D × Δy/(1+y) ; convexité corrige au 2e ordre |
| Forward rate | (1+z₂)² = (1+z₁)(1+f₁,₂) |
| Future (carry) | F = S × e^{(r−q)T} ou S(1 + r − carry) selon convention |
| Put-call parity | C + K·e^{−rT} = P + S |
| Binomial 1 pas | p* = (e^{rΔt} − d)/(u − d) ; C = e^{−rΔt}[p*Cᵤ + (1−p*)C_d] |
| Rendement money market | discount vs add-on : ne pas confondre face value et prix |

---

## 4. Comment travailler ce cours d'ici l'examen final

1. **Relire une session = produire sa fiche 1 page** (thème, 3 définitions, 2 formules, 1 exemple de marché actuel via ft.com — la référence du syllabus).
2. **S'entraîner à la TI BA II Plus** dès maintenant : prix de bond, FV/PV, breakeven d'un straddle. L'examen autorise **seulement** cette calculatrice : la maîtriser = minutes gagnées.
3. **Relier chaque session à l'actualité** (taux BCE, courbe US, volatilité) : c'est l'esprit du cours (« how banks think »).
4. **Participer aux sessions 2-6** : les groupes sont notés dans l'esprit du prof, et c'est ton canal pour le projet de thèse.
