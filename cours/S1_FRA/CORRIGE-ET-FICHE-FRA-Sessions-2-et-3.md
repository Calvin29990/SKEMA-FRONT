# FINANCIAL REPORTING & ANALYSIS (FRA) — Fiche Sessions 2 & 3 + Corrigé Intégral des Exercices & Quiz

> **Professeur :** Heritiana Rakotovololona (`heri.rakoto-ext@skema.edu`)
> **Séances de la semaine :**
> - **Session 2 (Current Assets)** : **Lundi 19/10/2026, 09:45–13:00** — *Lille Room A 220*
> - **Session 3 (Non-Current Assets)** : **Mardi 20/10/2026, 15:00–18:15** — *Lille Room A 220*
>
> 🔴 **ALERTE MID-TERM EXAM (vérifié dans `CFM_FRAL (Session 1) Pack`, p. 5 / slide 6) :**
> - **Mid-term examination : PENDANT LA SESSION #4 (la toute prochaine séance de FRA !), durée 1 heure, coeff. 40 %.**
> - **Final examination : Mercredi 2 décembre 2026, durée 2 heures, coeff. 60 %** *(calculatrice autorisée aux deux ; notes personnelles limitées autorisées au Final uniquement).*
> - 👉 **Tout le contenu ci-dessous (Sessions 2 & 3 + tous les exercices résolus) constitue le cœur du Mid-term de la Session 4.**

---

## PARTIE 1 — SYNTHÈSE DE COURS : SESSIONS 2 & 3 + READINGS CLÉS

### A. Session 2 — Current Assets (IFRS 13, IAS 2 Inventories, Accounts & Notes Receivable)

1. **Rappel Conceptual Framework (2018) & IFRS 13 Fair Value**
   - **Définition d'un actif** : *« A present economic resource controlled by the entity as a result of past events. An economic resource is a right that has the potential to produce economic benefits. »* (Le **contrôle** prime sur la propriété juridique — d'où l'inscription à l'actif des biens loués sous IFRS 16).
   - **IFRS 13 Fair Value Measurement** : mesure fondée sur le marché (*market-based*, pas *entity-specific*). C'est un **exit price** : le prix qui serait reçu pour vendre un actif ou payé pour transférer un passif lors d'une transaction normale (*orderly transaction*) entre intervenants de marché à la date d'évaluation.
   - **3 exceptions majeures hors champ d'IFRS 13** : ① **IFRS 2** (Share-based payments), ② **IFRS 16** (Leases), ③ mesures proches mais distinctes de la juste valeur comme la **NRV (IAS 2)** ou la **Value in Use (IAS 36)**.

2. **IAS 2 — Inventories (Stocks)**
   - **Coût d'entrée** : coûts d'achat + coûts de transformation + autres coûts engagés pour amener les stocks à l'endroit et dans l'état où ils se trouvent.
   - **Systèmes d'inventaire** :
     - **Periodic (intermittent)** : le COGS et le stock final sont calculés uniquement en fin de période ($\text{COGS} = \text{Beginning Inventory} + \text{Purchases} - \text{Ending Inventory}$).
     - **Perpetual (permanent)** : le COGS et le coût moyen (ou les couches FIFO) sont recalculés **à chaque vente**.
   - **Méthodes de valorisation des sorties** : Specific Identification, **FIFO** (First-In, First-Out), **Weighted-Average Cost (CMP)**.
   - **Divergence clé IFRS vs US GAAP (question classique de Mid-term !)** :

     | Critère | IFRS (IAS 2) | US GAAP (ASC 330) |
     |---|---|---|
     | **LIFO (Last-In, First-Out)** | ❌ **INTERDIT** | ✅ **Autorisé** |
     | **Évaluation à la clôture** | **LCNRV** (*Lower of Cost and Net Realizable Value*), avec $\text{NRV} = \text{Prix de vente estimé} - \text{Coûts d'achèvement et de vente}$ | **LCM** (*Lower of Cost or Market* pour LIFO/Retail, où Market = coût de remplacement borné entre $[\text{NRV}-\text{marge}, \text{NRV}]$) |
     | **Reprise de dépréciation (Reversal of write-down)** | ✅ **AUTORISÉE** (plafonnée au montant de la dépréciation initiale) | ❌ **INTERDITE** |

   - **Ratios d'analyse des stocks** :
     $$\text{Inventory Turnover} = \frac{\text{COGS}}{\text{Average Inventory}} \qquad ; \qquad \text{Days in Inventory (DIO)} = \frac{365}{\text{Inventory Turnover}}$$

3. **Accounts Receivable & Notes Receivable (Créances clients et effets à recevoir)**
   - **Comptabilisation à la valeur nette de réalisation (Carrying Amount / NRV)** : $\text{Gross Accounts Receivable} - \text{Allowance for Doubtful Accounts}$.
   - **Allowance Method (obligatoire en IFRS/GAAP, principe de rattachement / matching)** vs *Direct Write-Off* (interdit sauf si non significatif) :
     1. **Dotation / Ajustement de fin de période** *(via Aging Schedule)* :
        - On calcule la cible de provision requise ($\text{Target Allowance}$) par ancienneté des créances.
        - Si le compte *Allowance* a déjà un **solde créditeur** de $X$, la charge de l'exercice est $\text{Bad Debt Expense} = \text{Target} - X$. (S'il avait un **solde débiteur** de $Y$, la charge serait $\text{Target} + Y$).
        - Écriture : **Dr. Bad Debts Expense / Cr. Allowance for Doubtful Accounts** *(diminue le résultat et l'actif net)*.
     2. **Passage en perte d'une créance irrécouvrable (Write-off)** :
        - Écriture : **Dr. Allowance for Doubtful Accounts / Cr. Accounts Receivable**.
        - ⚠️ **Piège classique d'examen** : un *write-off* sous l'Allowance Method n'a **AUCUN impact sur le résultat (Net Income)** et **AUCUN impact sur la valeur nette comptable (Carrying Amount / NRV)** des créances clients, car la créance brute et la provision diminuent du même montant !
     3. **Recouvrement ultérieur d'une créance passée en perte (Recovery)** — en 2 écritures :
        - (a) Rétablir la créance : **Dr. Accounts Receivable / Cr. Allowance for Doubtful Accounts**
        - (b) Encaisser le cash : **Dr. Cash / Cr. Accounts Receivable**
   - **Notes Receivable (Effets à recevoir)** : $\text{Interest} = \text{Principal} \times \text{Annual Rate} \times \text{Time (en fraction d'année, ex. } n/360 \text{ ou } n/12)$.
   - **Ratios d'analyse des créances** :
     $$\text{Receivables Turnover} = \frac{\text{Net Credit Sales}}{\text{Average Accounts Receivable}} \qquad ; \qquad \text{Average Collection Period (DSO)} = \frac{365}{\text{Receivables Turnover}}$$

---

### B. Session 3 — Non-Current Assets (IAS 16 PPE, Depletion, IAS 38 Intangibles, IAS 36 Impairment, IFRS 16 Leases)

1. **IAS 16 — Property, Plant & Equipment (Immobilisations corporelles)**
   - **Coût initial capitalisable** : Prix d'achat (net de remises) $+$ droits de douane et taxes non récupérables $+$ **tous les coûts directement attribuables** pour amener l'actif à l'endroit et dans l'état nécessaires à son exploitation (préparation du site, livraison, installation, honoraires, peinture du logo sur un camion neuf) $+$ **estimation initiale des coûts de démantèlement et de remise en état du site (IAS 37 ARO)**.
   - ⚠️ **Exclus du coût du camion/équipement (passés en charges)** : assurance annuelle, vignette/immatriculation annuelle (*motor vehicle licence*), formation du personnel, maintenance courante.
   - ⚠️ **Coût d'un terrain (Land)** : inclut le prix d'achat $+$ frais de démolition d'un ancien bâtiment $-$ produits de revente des matériaux récupérés (*salvaged materials*). Le terrain **ne s'amortit jamais** (durée de vie illimitée), contrairement aux *Land improvements* (parkings, clôtures) qui ont une durée de vie finie et s'amortissent.
   - **Approche par composants (Component depreciation, obligatoire en IFRS)** : chaque partie significative ayant une durée d'utilité différente doit être amortie séparément.
   - **Les 3 méthodes d'amortissement autorisées** *(le mode « increasing-balance » n'existe pas / est interdit)* :
     - **Straight-Line (Linéaire)** : $\text{Annual Expense} = \dfrac{\text{Cost} - \text{Residual Value}}{\text{Useful Life}}$.
     - **Diminishing-Balance / Double-Declining Balance (Dégressif)** : $\text{Expense}_t = \text{Carrying Amount}_{\text{début } t} \times \left(\frac{1}{\text{Life}} \times m\right)$. ⚠️ On **ne soustrait pas** la valeur résiduelle au départ dans la base dégressive, mais la valeur nette comptable ($\text{Carrying Amount}$) ne doit jamais descendre en dessous de la valeur résiduelle.
     - **Units-of-Production (Unités d'œuvre)** : $\text{Expense}_t = \dfrac{\text{Cost} - \text{Residual Value}}{\text{Total Estimated Units}} \times \text{Actual Units}_t$.
   - **Changement de durée d'utilité ou de valeur résiduelle (IAS 8)** : traité **prospectivement** (changement d'estimation comptable sur l'exercice en cours et les exercices futurs ; **jamais** de retraitement rétroactif).

2. **Natural Resources — Depletion (Épuisement des ressources naturelles, Reading #1 Oil & Gas)**
   - Formule standard : $\text{Depletion per unit} = \dfrac{\text{Cost} + \text{Decommissioning (ARO)} + \text{Future Development Costs (FDC)} - \text{Residual Value}}{\text{Total Estimated Reserves}}$.
   - $\text{Depletion Expense} = \text{Depletion per unit} \times \text{Units Extracted}$.

3. **IAS 38 — Intangible Assets & Goodwill**
   - **Critères IAS 38** : actif non monétaire sans substance physique, **identifiable** (séparable OU issu de droits contractuels/légaux).
   - **R&D (IAS 38)** :
     - **Research costs (Frais de recherche)** : **TOUJOURS en charges (expensed)** immédiatement.
     - **Development costs (Frais de développement)** : **Capitalisés** si et seulement si la faisabilité technique et commerciale est démontrée (sous US GAAP, R&D = 100% en charges sauf logiciels).
   - **Goodwill** : seul le **purchased goodwill** (acquis lors d'un regroupement d'entreprises, IFRS 3 = excédent du prix d'acquisition sur la juste valeur des actifs nets identifiables) est inscrit au bilan. Le **goodwill généré en interne** n'est **JAMAIS** comptabilisé à l'actif.
   - **Amortissement des incorporels** :
     - *Durée de vie finie* (brevets/patents, copyrights, logiciels, coûts de développement) $\rightarrow$ **amortis** sur la plus courte de la durée d'utilité économique et de la durée légale.
     - *Durée de vie indéfinie* (marques/trademarks renouvelables, franchises perpétuelles, **Goodwill**) $\rightarrow$ **NON amortis**, mais soumis à un **test de dépréciation (impairment test) au moins annuel**.

4. **IAS 36 — Impairment of Non-Financial Assets (et Reading #2 PwC)**
   - Perte de valeur si **$\text{Carrying Amount} > \text{Recoverable Amount}$**, où :
     $$\text{Recoverable Amount} = \max\big(\text{Fair Value Less Costs of Disposal (FVLCD)},\; \text{Value in Use (VIU)}\big)$$
   - **Erreurs fréquentes pointées par PwC (Reading #2)** :
     - *Value in Use (VIU)* = DCF spécifique à l'entité dans l'état actuel de l'actif (exclut les restructurations futures non engagées et les CapEx d'amélioration).
     - Ne pas compter deux fois les risques (géopolitiques, climatiques, devises) à la fois dans les cash-flows et dans le taux d'actualisation.
     - L'ordre des tests : tester d'abord les actifs individuels, puis l'UGT (CGU), puis le Goodwill.

5. **IFRS 16 — Leases (Contrats de location, et Reading #5 HLB)**
   - **Chez le preneur (Lessee)** : suppression de la distinction Operating vs Finance Lease au bilan (sauf exemptions : **contrats court terme $\le 12\text{ mois}$** et **actifs de faible valeur $\le 5\,000\text{ \$}$**).
   - **Pour tout contrat $> 12\text{ mois}$ (IFRS 16)** :
     - **Au bilan à $t=0$** : inscription d'un **Right-of-Use (ROU) Asset** et d'une **Lease Liability** égaux à la **valeur actuelle (PV) des paiements de loyers futurs** actualisés au taux implicite du contrat (ou taux marginal d'endettement).
     - **Au compte de résultat chaque année** : le loyer unique d'exploitation est remplacé par ① une **dotation aux amortissements du ROU Asset** (en EBIT/Operating) $+$ ② une **charge d'intérêts sur la Lease Liability** ($\text{Solde début} \times r$, en résultat financier). *Effet front-loaded : la charge totale est plus élevée les premières années qu'en operating lease.*
   - **Impact d'IFRS 16 sur les ratios financiers (Slide 55, ultra-classique au Mid-term !)** :
     - **Working Capital Ratio (Current Assets / Current Liabilities)** : **Plus bas (Lower)** (car la part à $<1$ an de la dette de loyer entre en passif courant).
     - **Gearing / Leverage (Interest-Bearing Debt / Equity)** : **Plus élevé (Higher)** (hausse de la dette financière + baisse initiale des capitaux propres).
     - **EBITDA & EBIT** : **Plus élevés** (le loyer n'est plus une charge opérationnelle externe ; en EBIT seul l'amortissement est déduit).
     - **Operating Cash Flow (IAS 7)** : **Plus élevé** (le remboursement du principal du loyer sort en *Financing cash flows*).

---

## PARTIE 2 — CORRIGÉ INTÉGRAL DES EXERCICES DE LA SESSION 2 (*Current Assets*)

### I — Inventory Management

#### Exercice 5.1 — The Kissner's Consulting Group (Periodic Inventory System)

**Données de l'exercice :**
- `1/1` Beginning Inventory : $12\text{ unités} \times 40\text{ \$} = 480\text{ \$}$
- `2/12` Purchase : $8\text{ unités} \times 45\text{ \$} = 360\text{ \$}$
- `5/17` Purchase : $10\text{ unités} \times 46\text{ \$} = 460\text{ \$}$
- `9/28` Purchase : $15\text{ unités} \times 50\text{ \$} = 750\text{ \$}$
- **Total Goods Available for Sale (GAS)** : $12 + 8 + 10 + 15 = \mathbf{45\text{ unités}}$ pour un coût total de $480 + 360 + 460 + 750 = \mathbf{2\,050\text{ \$}}$.
- **Unités vendues dans l'année** : $15\text{ (le 4/15)} + 5\text{ (le 5/19)} + 5\text{ (le 11/2)} = \mathbf{25\text{ unités vendues}}$.
- **Unités en stock final (Ending Inventory)** : $45 - 25 = \mathbf{20\text{ unités}}$.

**Calculs selon les 3 méthodes (en inventaire intermittent / periodic) :**

1. **Weighted-Average (Coût Moyen Pondéré)** :
   - $\text{Coût unitaire moyen pondéré} = \dfrac{2\,050\text{ \$}}{45\text{ unités}} = 45{,}5556\text{ \$/unité}$.
   - **Ending Inventory** ($20\text{ unités}$) $= 20 \times 45{,}5556 = \mathbf{911{,}11\text{ \$}}$ *(ou $911\text{ \$}$ arrondi à l'unité)*.
   - **Cost of Goods Sold (COGS)** ($25\text{ unités}$) $= 25 \times 45{,}5556 = \mathbf{1\,138{,}89\text{ \$}}$ *(ou $1\,139\text{ \$}$)*. *(Vérification : $911{,}11 + 1\,138{,}89 = 2\,050\text{ \$}$).*
2. **FIFO (First-In, First-Out)** :
   - Les $20\text{ unités}$ restantes en stock final sont les **plus récentes** : $15\text{ unités à } 50\text{ \$ (du 9/28)} + 5\text{ unités à } 46\text{ \$ (du 5/17)} = 750 + 230 = \mathbf{980\text{ \$}}$.
   - **Cost of Goods Sold (COGS)** $= 2\,050 - 980 = \mathbf{1\,070\text{ \$}}$ *(soit $12\times 40 + 8\times 45 + 5\times 46 = 480 + 360 + 230 = 1\,070\text{ \$}$)*.
3. **LIFO (Last-In, First-Out)** :
   - Les $20\text{ unités}$ restantes en stock final sont les **plus anciennes** : $12\text{ unités à } 40\text{ \$ (du 1/1)} + 8\text{ unités à } 45\text{ \$ (du 2/12)} = 480 + 360 = \mathbf{840\text{ \$}}$.
   - **Cost of Goods Sold (COGS)** $= 2\,050 - 840 = \mathbf{1\,210\text{ \$}}$ *(soit $15\times 50 + 10\times 46 = 750 + 460 = 1\,210\text{ \$}$)*.

| Méthode (Periodic) | Ending Inventory ($) | Cost of Goods Sold ($) | Total GAS ($) |
|---|---:|---:|---:|
| **Weighted-Average** | **$911.11** | **$1,138.89** | $2,050.00 |
| **FIFO** | **$980.00** | **$1,070.00** | $2,050.00 |
| **LIFO** *(US GAAP only)* | **$840.00** | **$1,210.00** | $2,050.00 |

---

#### BE 6-6 — Battery Limited (Perpetual Inventory System)

**Suivi chronologique des quantités (`Ending in Units`) :**
- `02/08` Achat $250$ à $70\text{ €}$ ($17\,500\text{ €}$) $\rightarrow$ Stock $= \mathbf{250\text{ u}}$
- `03/08` Achat $500$ à $100\text{ €}$ ($50\,000\text{ €}$) $\rightarrow$ Stock $= \mathbf{750\text{ u}}$ (Coût cumulé $= 67\,500\text{ €}$)
- `10/08` Vente $(300)$ $\rightarrow$ Stock $= \mathbf{450\text{ u}}$
- `15/08` Achat $900$ à $120\text{ €}$ ($108\,000\text{ €}$) $\rightarrow$ Stock $= \mathbf{1\,350\text{ u}}$
- `25/08` Vente $(325)$ $\rightarrow$ Stock final $= \mathbf{1\,025\text{ u}}$

**1. Méthode FIFO (Perpetual) :**
- **Vente du 10/08 ($300\text{ u}$)** : on sort $250\text{ u} \times 70\text{ €} + 50\text{ u} \times 100\text{ €} = 17\,500 + 5\,000 = \mathbf{22\,500\text{ €}}$. *(Reste en stock : $450\text{ u à } 100\text{ €} = 45\,000\text{ €}$).*
- **Achat du 15/08 ($900\text{ u à } 120\text{ €}$)** : en stock $450\text{ u à } 100\text{ €} + 900\text{ u à } 120\text{ €} = 153\,000\text{ €}$.
- **Vente du 25/08 ($325\text{ u}$)** : prises sur la couche à $100\text{ €} \implies 325 \times 100\text{ €} = \mathbf{32\,500\text{ €}}$.
- **Résultat FIFO** :
  - **Total COGS** $= 22\,500 + 32\,500 = \mathbf{55\,000\text{ €}}$
  - **Ending Inventory** ($125\text{ u à } 100\text{ €} + 900\text{ u à } 120\text{ €}$) $= 12\,500 + 108\,000 = \mathbf{120\,500\text{ €}}$.

**2. Méthode Average Cost / Moving Average (Perpetual) :**
- **Après l'achat du 03/08** : $\text{Coût moyen} = \dfrac{17\,500 + 50\,000}{250 + 500} = \dfrac{67\,500}{750} = \mathbf{90{,}00\text{ €/u}}$.
- **Vente du 10/08 ($300\text{ u}$)** : $\text{COGS}_1 = 300 \times 90\text{ €} = \mathbf{27\,000\text{ €}}$. *(Stock restant : $450\text{ u à } 90\text{ €} = 40\,500\text{ €}$).*
- **Après l'achat du 15/08 ($900\text{ u à } 120\text{ €} = 108\,000\text{ €}$)** : $\text{Nouveau coût moyen} = \dfrac{40\,500 + 108\,000}{450 + 900} = \dfrac{148\,500}{1\,350} = \mathbf{110{,}00\text{ €/u}}$.
- **Vente du 25/08 ($325\text{ u}$)** : $\text{COGS}_2 = 325 \times 110\text{ €} = \mathbf{35\,750\text{ €}}$.
- **Résultat Moving Average** :
  - **Total COGS** $= 27\,000 + 35\,750 = \mathbf{62\,750\text{ €}}$
  - **Ending Inventory** ($1\,025\text{ u} \times 110\text{ €}$) $= \mathbf{112\,750\text{ €}}$. *(Vérification : $62\,750 + 112\,750 = 175\,500\text{ €}$).*

---

#### BE 6-10 — Tech-IT (Lower of Cost and Net Realizable Value — IAS 2)

**1. Calcul du LCNRV ligne par ligne (Item-by-item basis, exigé par IAS 2) :**

| Inventory Category | Cost (€) | NRV (€) | LCNRV = min(Cost, NRV) (€) | Dépréciation requise (€) |
|---|---:|---:|---:|---:|
| Desktops | 347 000 | 326 000 | **326 000** | $-21\,000$ |
| Tablets and readers | 168 700 | 224 000 | **168 700** | $0$ |
| Laptops | 221 020 | 285 000 | **221 020** | $0$ |
| Accessories & parts | 97 400 | 94 300 | **94 300** | $-3\,100$ |
| **Total** | **834 120 €** | **929 300 €** | **810 020 €** | **$-\mathbf{24\,100\text{ €}}$** |

**2. Écriture d'ajustement au 31 décembre :**
- Perte de valeur totale à constater $= 834\,120 - 810\,020 = \mathbf{24\,100\text{ €}}$ ($21\,000\text{ €}$ sur Desktops $+ 3\,100\text{ €}$ sur Accessories & parts).
- **Journal Entry :**
  - **Dr. Cost of Goods Sold (ou Loss on Inventory Write-Down)** : `24,100 €`
  - **Cr. Inventory (ou Allowance to Reduce Inventory to NRV)** : `24,100 €`

---

#### BE 6-12 — Michelin Tire Corporation (Inventory Turnover & Days in Inventory)

| Ratio | Formule | 2024 | 2025 | Évolution 2024 $\rightarrow$ 2025 |
|---|---|---|---|---|
| **Average Inventory** | $(\text{Inv}_t + \text{Inv}_{t-1})/2$ | $\frac{1\,623{,}8 + 1\,481{,}0}{2} = \mathbf{1\,552{,}40\text{ M€}}$ | $\frac{1\,765{,}5 + 1\,623{,}8}{2} = \mathbf{1\,694{,}65\text{ M€}}$ | $+9{,}2\%$ de stock moyen |
| **Inventory Turnover** | $\frac{\text{COGS}}{\text{Average Inventory}}$ | $\frac{8\,033{,}2}{1\,552{,}40} = \mathbf{5{,}17\text{ times}}$ *(4,95x sur stock fin)* | $\frac{7\,747{,}1}{1\,694{,}65} = \mathbf{4{,}57\text{ times}}$ *(4,39x sur stock fin)* | **Baisse** ($-0{,}60\times$) |
| **Days in Inventory (DIO)** | $\frac{365}{\text{Inventory Turnover}}$ | $\frac{365}{5{,}1747} = \mathbf{70{,}5\text{ days}}$ *(73,8 j sur stock fin)* | $\frac{365}{4{,}5715} = \mathbf{79{,}8\text{ days}}$ *(83,2 j sur stock fin)* | **Allongement de $+9{,}3\text{ jours}$** |

**2. Conclusion :** La gestion des stocks de Michelin s'est **détériorée en 2025** : alors que le chiffre d'affaires et le COGS ont légèrement baissé, les stocks ont augmenté à $1\,765{,}5\text{ M€}$, faisant chuter la rotation de $5{,}17\times$ à $4{,}57\times$ et allongeant la durée d'écoulement des stocks d'environ **9,3 jours** (de $70{,}5\text{ j}$ à $79{,}8\text{ j}$).

---

### II — Current Assets : Accounts Receivable

#### Exercice 5.3 — Dr. Branson (Aging Schedule & Write-Off)

**1. Calcul de la provision cible (Target Allowance) :**
- `0–30 days` : $120\,000\text{ \$} \times 1\% = 1\,200\text{ \$}$
- `31–90 days` : $45\,000\text{ \$} \times 3\% = 1\,350\text{ \$}$
- `91–120 days` : $15\,000\text{ \$} \times 10\% = 1\,500\text{ \$}$
- `More than 120 days` : $3\,000\text{ \$} \times 40\% = 1\,200\text{ \$}$
- **Total Target Allowance** $= 1\,200 + 1\,350 + 1\,500 + 1\,200 = \mathbf{5\,250\text{ \$}}$.
- Solde créditeur existant avant ajustement $= 3\,000\text{ \$} \implies \text{Ajustement à doter} = 5\,250 - 3\,000 = \mathbf{2\,250\text{ \$}}$.

**2. Écritures comptables (Journal Entries) :**

| Opération | Account Titles and Explanation | Debit ($) | Credit ($) |
|---|---|---:|---:|
| **(1) Adjusting entry** | **Bad Debts Expense** | **2,250** | |
| | &nbsp;&nbsp;&nbsp;&nbsp;**Allowance for Bad Debts (Doubtful Accounts)** | | **2,250** |
| | *(To bring allowance from $3,000 Cr to $5,250 target)* | | |
| **(2) Write-off (Mr. Beckett)** | **Allowance for Bad Debts (Doubtful Accounts)** | **150** | |
| | &nbsp;&nbsp;&nbsp;&nbsp;**Accounts Receivable — Mr. Beckett** | | **150** |
| | *(To write off uncollectible account of Mr. Beckett)* | | |

---

#### BE 8-5 — Calafate Ltd (Aging Schedule)

- **Calcul de la cible (Total Estimated Uncollectible Accounts)** :
  - `0–45 days` : $726\,000\text{ €} \times 2\% = \mathbf{14\,520\text{ €}}$
  - `46–90 days` : $248\,000\text{ €} \times 5\% = \mathbf{12\,400\text{ €}}$
  - `Over 90 days` : $112\,000\text{ €} \times 16\% = \mathbf{17\,920\text{ €}}$
  - **Total Target Allowance** $= 14\,520 + 12\,400 + 17\,920 = \mathbf{44\,840\text{ €}}$.
- **Question 1 (Solde créditeur initial de $13\,175{,}00\text{ €}$)** :
  $$\text{Bad Debt Expense} = 44\,840 - 13\,175 = \mathbf{31\,665{,}00\text{ €}}$$
- **Question 2 (Solde créditeur initial de $8\,920{,}00\text{ €}$)** :
  $$\text{Bad Debt Expense} = 44\,840 - 8\,920 = \mathbf{35\,920{,}00\text{ €}}$$
  *(Note de sécurité : si dans l'exercice original du manuel Kieso la question 2 supposait un solde **débiteur** de $8\,920\text{ €}$ corrigé en « credit » par coquille dans le poly, la dotation avec un solde débiteur serait $44\,840 + 8\,920 = \mathbf{53\,760{,}00\text{ €}}$. Mentionner les deux en classe montre que tu maîtrises parfaitement la mécanique !)*

---

#### BE 8-6 — Canton Imports (Aging Schedule)

- **1. Tableau d'ancienneté complété :**
  - `0–30 days` : $368\,000\text{ €} \times 1\% = \mathbf{3\,680\text{ €}}$
  - `31–60 days` : $120\,000\text{ €} \times 4\% = \mathbf{4\,800\text{ €}}$
  - `61–90 days` : $72\,000\text{ €} \times 10\% = \mathbf{7\,200\text{ €}}$
  - `Over 90 days` : $40\,000\text{ €} \times 20\% = \mathbf{8\,000\text{ €}}$
  - **Total Estimated Uncollected Accounts (Target Allowance)** $= 3\,680 + 4\,800 + 7\,200 + 8\,000 = \mathbf{23\,680\text{ €}}$.
- **2. Ajustement de Bad Debt Expense (avec solde créditeur initial de $3\,600{,}00\text{ €}$) :**
  $$\text{Bad Debt Expense} = 23\,680 - 3\,600 = \mathbf{20\,080{,}00\text{ €}}$$

---

#### BE 8-7 — Searcy Corp (Write-Off & Carrying Amount)

1. **Ajustement au bilan lors du write-off de $11\,000\text{ €}$ (Hutley Inc.) :**
   - On débite **Allowance for Doubtful Accounts** de $11\,000\text{ €}$ (qui passe de $29\,000\text{ €}$ à $18\,000\text{ €}$) et on crédite **Accounts Receivable** de $11\,000\text{ €}$ (qui passe de $480\,000\text{ €}$ à $469\,000\text{ €}$).
2. **Carrying Amount (Valeur nette comptable / NRV) :**
   - **a) Avant le write-off** : $480\,000 - 29\,000 = \mathbf{451\,000\text{ €}}$
   - **b) Après le write-off** : $469\,000 - 18\,000 = \mathbf{451\,000\text{ €}}$ *(inchangé ! Le write-off ne modifie pas la valeur nette des créances).*

---

#### BE 8-15 — Canfor Corporation (Receivables Turnover & Collection Period)

| Ratio | Formule (sur créances brutes / Gross AR) | 2024 | 2025 | Sur créances nettes (Net AR) 2024 $\rightarrow$ 2025 |
|---|---|---|---|---|
| **Average Receivables** | $(\text{AR}_t + \text{AR}_{t-1})/2$ | $\frac{95{,}0 + 115{,}3}{2} = \mathbf{105{,}15\text{ M€}}$ | $\frac{196{,}3 + 95{,}0}{2} = \mathbf{145{,}65\text{ M€}}$ | $101{,}95\text{ M€} \rightarrow 141{,}55\text{ M€}$ |
| **Receivables Turnover** | $\frac{\text{Net Sales}}{\text{Avg Receivables}}$ | $\frac{3\,347{,}6}{105{,}15} = \mathbf{31{,}84\text{ times}}$ | $\frac{3\,925{,}3}{145{,}65} = \mathbf{26{,}95\text{ times}}$ | $32{,}84\times \rightarrow 27{,}73\times$ |
| **Average Collection Period (DSO)** | $\frac{365}{\text{Receivables Turnover}}$ | $\frac{365}{31{,}836} = \mathbf{11{,}5\text{ days}}$ | $\frac{365}{26{,}950} = \mathbf{13{,}5\text{ days}}$ | $11{,}1\text{ days} \rightarrow 13{,}2\text{ days}$ |

**2. Conclusion :** La gestion des créances clients de Canfor est **moins bonne (worse) en 2025** qu'en 2024 : les créances brutes ont plus que doublé (de $95{,}0\text{ M€}$ à $196{,}3\text{ M€}$ pour une hausse de CA de $+17{,}3\%$), ralentissant la rotation de $31{,}84\times$ à $26{,}95\times$ et allongeant le délai moyen de recouvrement de **$11{,}5\text{ jours}$ à $13{,}5\text{ jours}$** ($+2\text{ jours}$).

---

## PARTIE 3 — CORRIGÉ INTÉGRAL DES EXERCICES & DU QUIZ DE LA SESSION 3 (*Non-Current Assets*)

### I — Brief Exercises

#### Brief Exercise 9-10 — Goo-Yeong Limited (Disposal of Equipment)
- **Données** : Coût $= 144\,000\text{ \$}$ (acquis le 01/01/2016), valeur résiduelle $= 4\,000\text{ \$}$, durée $= 5\text{ ans}$. Base amortissable $= 144\,000 - 4\,000 = 140\,000\text{ \$}$.
- **Amortissement annuel linéaire** $= \dfrac{140\,000}{5} = \mathbf{28\,000\text{ \$/an}}$.
- **1. Mise à jour de l'amortissement en 2018 jusqu'au 30 septembre 2018 ($9\text{ mois}$)** :
  $$\text{Depreciation Expense (Jan 1 – Sept 30, 2018)} = 28\,000 \times \frac{9}{12} = \mathbf{21\,000\text{ \$}}$$
  *(Écriture : Dr. Depreciation Expense $21\,000\text{ \$}$ / Cr. Accumulated Depreciation $21\,000\text{ \$}$).*
- **2. Gain ou perte sur cession au 30 septembre 2018 (prix de vente $= 42\,000\text{ \$}$)** :
  - Amortissements cumulés au 30/09/2018 ($2\text{ ans et } 9\text{ mois} = 2{,}75\text{ ans}$) $= 28\,000\text{ (2016)} + 28\,000\text{ (2017)} + 21\,000\text{ (2018)} = \mathbf{77\,000\text{ \$}}$.
  - Valeur nette comptable (Carrying Amount / Book Value) $= 144\,000 - 77\,000 = \mathbf{67\,000\text{ \$}}$.
  - Résultat de cession $= \text{Prix de cession } (42\,000\text{ \$}) - \text{VNC } (67\,000\text{ \$}) = -\mathbf{25\,000\text{ \$}} \implies$ **Loss on disposal of $\$25,000$**.
  *(Écriture de sortie : Dr. Cash $42\,000$, Dr. Accumulated Depreciation $77\,000$, Dr. Loss on Disposal $25\,000$ / Cr. Equipment $144\,000$).*

---

#### Brief Exercise 9-14 — Classification (`PP&E`, `I` for Intangible, `NA` for Not Applicable)

| Item | Code | Justification |
|---|:---:|---|
| a) Accumulated amortization | **I** *(contra)* | Compte soustractif des immobilisations incorporelles (Intangible Assets) au bilan |
| b) Asset retirement cost for a factory | **PP&E** | Capitalisé dans le coût initial de l'usine selon IAS 16 / IAS 37 |
| c) Assets under finance lease ($>1$ year) | **PP&E** | Comptabilisé en actif non courant (ROU Asset / PP&E) selon IFRS 16 |
| d) Building | **PP&E** | Immobilisation corporelle |
| e) Franchise | **I** | Droit contractuel sans substance physique |
| f) Inventory | **NA** | Actif courant (IAS 2) |
| g) Common shares | **NA** | Capitaux propres (Shareholders' Equity) |
| h) Impairment loss | **NA** | Compte de charges au compte de résultat (Income Statement) |
| i) Land | **PP&E** | Immobilisation corporelle non amortissable |
| j) Land improvements | **PP&E** | Immobilisation corporelle amortissable |
| k) Leasehold improvements | **PP&E** | Agencements et installations sur biens loués = PP&E |
| l) License right | **I** | Immobilisation incorporelle |
| m) Operating lease ($<1$ year contract) | **NA** | Exemption court terme IFRS 16 ($\le 12\text{ mois}$) : loyers passés en charges, pas d'actif au bilan |
| n) Patent | **I** | Immobilisation incorporelle (durée finie) |
| o) Research costs | **NA** | Passés en charges (Income Statement) selon IAS 38 |
| p) Residual value on building | **NA** | Estimation utilisée dans le calcul d'amortissement, pas un compte de bilan distinct |
| q) Trademark | **I** | Immobilisation incorporelle |

---

#### Brief Exercise 9-15 — Saputo Inc. (Statement of Financial Position — Non-Current Assets, in €m)

```text
SAPUTO INC.
Statement of Financial Position (Partial) — As at March 31, 2015 (in millions of €)

Non-Current Assets:
  Property, Plant, and Equipment:
    Land ...................................................................................... €   66
    Buildings ............................................................ €   759
      Less: Accumulated depreciation – buildings .........................    (218)            541
    Furniture, machinery & equipment .....................................   2,339
      Less: Accumulated depreciation – furniture, machinery & equipment ..    (887)          1,452
    Total Property, Plant, and Equipment ...................................................... €2,059

  Intangible Assets and Goodwill:
    Finite-life intangible assets ........................................ €   246
      Less: Accumulated amortization – finite-life intangible assets .....     (57)            189
    Indefinite-life intangible assets .........................................................    318
    Total Intangible Assets ...................................................................    507
    Goodwill ..................................................................................  2,125

Total Non-Current Assets ...................................................................... €4,691
```

---

### II — Exercises on Non-Current Assets

#### Exercice 2.1 — Sword's Taxi Company ($20,000 cost, $5,000 salvage, 5 years, 100,000 miles)

- **Case A — Double-Declining-Balance (DDB) en 2015 (3e année) :**
  - Taux linéaire $= 1/5 = 20\% \implies \text{Taux DDB} = 2 \times 20\% = \mathbf{40\%}$ (appliqué à la VNC d'ouverture, sans déduire la valeur résiduelle au départ, mais avec plancher de VNC à $5\,000\text{ \$}$).
  - **2013 (An 1)** : Dotation $= 20\,000 \times 40\% = 8\,000\text{ \$} \rightarrow \text{VNC fin 2013} = 12\,000\text{ \$}$.
  - **2014 (An 2)** : Dotation $= 12\,000 \times 40\% = 4\,800\text{ \$} \rightarrow \text{VNC fin 2014} = 7\,200\text{ \$}$.
  - **2015 (An 3)** : Dotation théorique $= 7\,200 \times 40\% = 2\,880\text{ \$}$. Or $7\,200 - 2\,880 = 4\,320\text{ \$} < \text{Valeur résiduelle } (5\,000\text{ \$})$ !
    - ⚠️ **Plafonnement à la valeur résiduelle** : la dotation 2015 est plafonnée à $7\,200 - 5\,000 = \mathbf{2\,200\text{ \$}}$ (pour que la VNC fin 2015 s'arrête exactement à $5\,000\text{ \$}$). *(Note : si on calcule $40\%$ sans appliquer le plancher en 3e année, cela donne $2\,880\text{ \$}$ — indique les deux chiffres sur ta feuille : **$2\,200\text{ \$}$ avec plancher à la valeur résiduelle de $5\,000\text{ \$}$**, vs $2\,880\text{ \$}$ brut).*
  - **Écriture 2015** : **Dr. Depreciation Expense $2,200 / Cr. Accumulated Depreciation $2,200**.

- **Case B — Units-of-Production (UoP) : VNC fin 2015 et fin 2017 :**
  - Base amortissable $= 20\,000 - 5\,000 = 15\,000\text{ \$}$ sur $100\,000\text{ miles} \implies \text{Coût par mile} = \mathbf{0{,}15\text{ \$/mile}}$.
  - **Fin 2015** : miles cumulés $(2013\text{–}2015) = 22\,000 + 29\,000 + 23\,000 = 74\,000\text{ miles}$.
    - Amortissements cumulés fin 2015 $= 74\,000 \times 0{,}15\text{ \$} = 11\,100\text{ \$}$.
    - **Net Book Value fin 2015** $= 20\,000 - 11\,100 = \mathbf{8\,900\text{ \$}}$.
  - **Fin 2017** : miles cumulés $(2013\text{–}2017) = 74\,000 + 21\,000 + 25\,000 = 120\,000\text{ miles}$ (dépasse l'estimation initiale de $100\,000\text{ miles}$).
    - L'amortissement cumulé ne peut pas dépasser la base amortissable de $15\,000\text{ \$}$ (il s'arrête dès que $100\,000\text{ miles}$ sont atteints en 2017).
    - **Net Book Value fin 2017** $= 20\,000 - 15\,000 = \mathbf{5\,000\text{ \$}}$ (= valeur résiduelle).

- **Case C — Straight-Line fin 2016 (4e année) & Cession le 01/01/2017 pour $5\,700\text{ \$}$ :**
  - Dotation annuelle linéaire $= \dfrac{20\,000 - 5\,000}{5} = \mathbf{3\,000\text{ \$/an}}$.
  - **Accumulated Depreciation fin 2016 (après 4 ans)** $= 4 \times 3\,000\text{ \$} = \mathbf{12\,000\text{ \$}}$.
  - **Net Book Value au 01/01/2017** $= 20\,000 - 12\,000 = \mathbf{8\,000\text{ \$}}$.
  - **Cession pour $5\,700\text{ \$}$** : $5\,700 - 8\,000 = -\mathbf{2\,300\text{ \$}} \implies$ **Loss on disposal of $\$2,300$**.

---

#### Exercice 2.2 — Reitmans Limited (E9-11, en milliers d'€)

**1. Classification par état financier :**
- **Income Statement (Operating Expenses)** : Amortization expense ($3\,999$), Depreciation expense ($42\,410$), Impairment loss ($8\,276$), Reversal of impairment loss ($-775$, produit/réduction de charge opérationnelle).
- **Neither (Hors bilan / Notes annexes si engagements court terme)** : Operating leases ($376\,372$, engagements de loyers opérationnels mentionnés en annexe dans l'exercice historique pré-IFRS 16 / court terme).
- **Statement of Financial Position (Non-Current Assets)** : tous les autres postes ci-dessous.

**2. Section Non-Current Assets du bilan au 31 janvier 2015 (en k€) :**
- **Property, Plant, and Equipment (Net)** :
  - Land : **$5\,860$**
  - Buildings ($45\,633 - 19\,096$) : **$26\,537$**
  - Fixtures & equipment ($131\,073 - 68\,010$) : **$63\,063$**
  - Leasehold improvements ($140\,188 - 83\,299$) : **$56\,889$**
  - **Total PP&E (Net)** $= 5\,860 + 26\,537 + 63\,063 + 56\,889 = \mathbf{152\,349\text{ k€}}$
- **Intangible Assets (Net)** :
  - Software ($28\,261 - 8\,184$) $= 20\,077$ + Trademarks ($499$) $= \mathbf{20\,576\text{ k€}}$
- **Goodwill** : **$42\,426\text{ k€}$**
- **Total Non-Current Assets** $= 152\,349 + 20\,576 + 42\,426 = \mathbf{215\,351\text{ k€}}$.

---

#### Exercice 2.3 — Accounting for Natural Resources (Depletion)

- **2.3.1 Bantam Oil Company :**
  - $\text{Depletion per barrel} = \dfrac{625\,000\text{ \$} - 25\,000\text{ \$}}{150\,000\text{ barrels}} = \dfrac{600\,000}{150\,000} = \mathbf{4{,}00\text{ \$/barrel}}$.
  - **Depletion Expense 20X7** ($15\,000\text{ barrels}$) $= 15\,000 \times 4{,}00\text{ \$} = \mathbf{60\,000\text{ \$}}$.
- **2.3.2 Skyline Mine, Inc. :**
  - $\text{Depletion per ton} = \dfrac{12\,000\,000\text{ \$}}{2\,000\,000\text{ tons}} = \mathbf{6{,}00\text{ \$/ton}}$.
  - Extraction cumulée $20\text{X}6 + 20\text{X}7 = 610\,000 + 480\,000 = 1\,090\,000\text{ tons}$.
  - **Accumulated Depletion au 31/12/20X7** $= 1\,090\,000 \times 6{,}00\text{ \$} = \mathbf{6\,540\,000\text{ \$}}$.

---

#### Exercice 2.4 — Ajax Limited (E9-13 : ROA, Asset Turnover, Profit Margin & DuPont)

- **Actif moyen (Average Total Assets)** $= \dfrac{7\,200 + 6\,800}{2} = \mathbf{7\,000\text{ M€}}$.
- **a) Calcul des 3 ratios :**
  1. **Return on Assets (ROA)** $= \dfrac{\text{Net Income}}{\text{Average Total Assets}} = \dfrac{550}{7\,000} = \mathbf{7{,}86\%}$
  2. **Asset Turnover (ATO)** $= \dfrac{\text{Net Sales}}{\text{Average Total Assets}} = \dfrac{14\,000}{7\,000} = \mathbf{2{,}00\text{ times}}$
  3. **Profit Margin (PM)** $= \dfrac{\text{Net Income}}{\text{Net Sales}} = \dfrac{550}{14\,000} = \mathbf{3{,}93\%}$ ($3{,}9286\%$)
- **b) Preuve mathématique DuPont :**
  $$\text{Profit Margin} \times \text{Asset Turnover} = \frac{\text{Net Income}}{\text{Net Sales}} \times \frac{\text{Net Sales}}{\text{Average Total Assets}} = \frac{\text{Net Income}}{\text{Average Total Assets}} = \text{ROA}$$
  $$3{,}9286\% \times 2{,}00 = \mathbf{7{,}86\%} \quad \checkmark$$
- **c) Comparaison sectorielle :** Ajax surperforme nettement ses concurrents sur **les 3 dimensions** : sa marge nette est supérieure ($3{,}93\%$ vs $3{,}0\%$), la rotation de ses actifs est plus rapide ($2{,}0\times$ vs $1{,}5\times$), ce qui porte son **ROA à $7{,}86\%$ contre $4{,}5\%$ pour l'industrie**.

---

#### Exercice 9.9 — Bankers Group Inc. (Lease Financing — IFRS 16, 5 ans, $10,000/an à terme échu, taux 8 %)

**1. Cas 1 — Contrats court terme multiples / Operating Lease (exemption IFRS 16) :**
- Aucun actif ni dette de loyer au bilan.
- Chaque fin d'année (2020 à 2024) : **Dr. Lease (Rent) Expense $10,000 / Cr. Cash $10,000**.

**2. Cas 2 — Contrat de location de 5 ans sous IFRS 16 :**
- **Valeur actuelle (PV) à l'origine (01/01/2020)** :
  $$\text{PV} = \sum_{t=1}^{5} \frac{10\,000}{(1{,}08)^t} = 10\,000 \times \frac{1 - (1{,}08)^{-5}}{0{,}08} = 10\,000 \times 3{,}99271 = \mathbf{39\,927{,}10\text{ \$}}$$
- **Écriture initiale (01/01/2020)** :
  - **Dr. Right-of-Use (ROU) Asset** : `$39,927.10`
  - **Cr. Lease Liability** : `$39,927.10`
- **Amortissement annuel linéaire du ROU Asset (sur 5 ans)** : $\dfrac{39\,927{,}10}{5} = \mathbf{7\,985{,}42\text{ \$/an}}$.
- **Tableau d'amortissement de la dette de loyer (Lease Liability, taux effectif 8 %) :**

| Année | Dette début ($) | Paiement annuel ($) | Charge d'intérêts (8 %) ($) | Remboursement du principal ($) | Dette fin ($) | Amortissement ROU ($) | Charge totale P&L ($) |
|:---:|---:|---:|---:|---:|---:|---:|---:|
| **2020** | 39,927.10 | 10,000.00 | **3,194.17** | **6,805.83** | 33,121.27 | 7,985.42 | **11,179.59** |
| **2021** | 33,121.27 | 10,000.00 | **2,649.70** | **7,350.30** | 25,770.97 | 7,985.42 | **10,635.12** |
| **2022** | 25,770.97 | 10,000.00 | **2,061.68** | **7,938.32** | 17,832.65 | 7,985.42 | **10,047.10** |
| **2023** | 17,832.65 | 10,000.00 | **1,426.61** | **8,573.39** | 9,259.26 | 7,985.42 | **9,412.03** |
| **2024** | 9,259.26 | 10,000.00 | **740.74** | **9,259.26** | **0.00** | 7,985.42 | **8,726.16** |
| **Total** | — | **50,000.00** | **10,072.90** | **39,927.10** | — | **39,927.10** | **50,000.00** |

- **Écritures à chaque clôture annuelle $t$ (ex. au 31/12/2020)** :
  1. Paiement du loyer : **Dr. Interest Expense $3,194.17**, **Dr. Lease Liability $6,805.83** / **Cr. Cash $10,000.00**
  2. Amortissement du ROU : **Dr. Depreciation Expense — ROU Asset $7,985.42** / **Cr. Accumulated Depreciation — ROU Asset $7,985.42**

**3. Comparaison des deux méthodes (Contrast) :**
- Sur les 5 ans cumulés, la sortie de cash totale ($50\,000\text{ \$}$) et la charge totale au P&L ($50\,000\text{ \$}$) sont **identiques**.
- **Différences clés sous IFRS 16** : ① Augmentation de l'actif et de la dette financière au bilan dès $t=0$ ($+39\,927\text{ \$}$ $\implies$ hausse du Gearing), ② Charge totale au P&L **dégressive (front-loaded)** ($11\,180\text{ \$}$ en An 1 contre $8\,726\text{ \$}$ en An 5, au lieu de $10\,000\text{ \$}$ constants), ③ Amélioration de l'**EBITDA** ($+10\,000\text{ \$}$) et de l'**EBIT** ($+2\,015\text{ \$}$).

---

### III — Problem P9-9A (Intangible Assets & Goodwill)

| # | Item | (a) Intangible or Goodwill? | (b) Account Title (si Oui) | (c) Amortized? | (d) Traitement si NON (Compte / État financier / Section) |
|:---:|---|:---:|---|:---:|---|
| **1** | Goodwill recorded in the purchase of a business | **Oui** | **Goodwill** | **Non** *(test d'impairment annuel)* | — |
| **2** | Equipment under operating lease ($<1$ yr) | **Non** | — | — | **Lease / Rent Expense** $\rightarrow$ Income Statement (Operating Expenses) |
| **3** | Cost of purchasing a copyright | **Oui** | **Copyrights** (Intangible Assets) | **Oui** *(durée finie)* | — |
| **4** | Cost of purchasing a trademark | **Oui** | **Trademarks** (Intangible Assets) | **Non** *(si durée indéfinie ; Oui si finie)* | — |
| **5** | Research costs (chemical tests, new medication) | **Non** | — | — | **Research & Development Expense** $\rightarrow$ Income Statement (Operating Expenses) |
| **6** | Goodwill generated internally | **Non** | — | — | **Non comptabilisé** (*Not reported on any financial statement*, IAS 38) |
| **7** | Aircraft acquired using a finance lease ($>1$ yr) | **Non** | — | — | **Right-of-Use Asset / Aircraft (PP&E)** $\rightarrow$ Statement of Financial Position (Non-Current Assets, PP&E) |
| **8** | Cost of purchasing a patent | **Oui** | **Patents** (Intangible Assets) | **Oui** *(durée finie $\le 20\text{ ans}$)* | — |
| **9** | Legal costs to **unsuccessfully** defend a patent | **Non** | — | — | **Legal Expenses** (+ dépréciation du brevet si invalidé) $\rightarrow$ Income Statement (Operating Expenses) |
| **10** | Development costs for feasible sample product to be sold | **Oui** *(IFRS IAS 38)* | **Development Costs / Deferred Development Costs** (Intangible Assets) | **Oui** *(sur la durée de vente du produit)* | *(Note : sous US GAAP serait passé en R&D Expense)* |

---

### IV — Corrigé du MINI QUIZ (15 QCM — Pages 36–38 du Pack Session 3)

| Q# | Réponse | Justification rapide & Calcul |
|:---:|:---:|---|
| **1** | **b ($125,500)** | Coût du terrain $= \text{Prix d'achat } (120\,000) + \text{Démolition } (7\,000) - \text{Matériaux récupérés } (1\,500) = \mathbf{125\,500\text{ \$}}$. |
| **2** | **b** | Un camion détenu pour la revente par un concessionnaire auto est un **stock (Inventory, IAS 2)**, pas un PP&E. |
| **3** | **d (land)** | Le terrain (**Land**) a une durée d'utilité illimitée et ne perd pas son potentiel de service (non amortissable). |
| **4** | **a ($46,500)** | Coût capitalisable du camion $= \text{Prix } (45\,000) + \text{Peinture du logo } (1\,500) = \mathbf{46\,500\text{ \$}}$. *(La vignette de $175\text{ \$}$ et l'assurance annuelle de $1\,500\text{ \$}$ sont des charges périodiques).* |
| **5** | **b** | *Accumulated Depreciation* représente le cumul des dotations aux amortissements comptabilisées en charges **depuis l'acquisition de l'actif**. |
| **6** | **b** | La méthode *increasing-balance* n'est **pas** une méthode d'amortissement acceptable en IFRS/GAAP. |
| **7** | **d** | Principe de rattachement (*matching principle*) : le coût d'un actif amortissable est passé en charges **au fur et à mesure que l'actif procure des avantages économiques** (*as the asset benefits the company*). |
| **8** | **d** | $\text{Carrying amount (VNC)} = \text{Asset's cost} - \text{Accumulated depreciation}$ *(et pertes de valeur cumulées)*. |
| **9** | **d** | $\text{Cost} - \text{Residual value} =$ **Depreciable amount** (base amortissable). |
| **10** | **a** | La valeur résiduelle (*residual value*) est **l'estimation de la valeur de l'actif à la fin de sa durée d'utilité**. |
| **11** | **a ($3,400)** | Dotation annuelle linéaire $= \dfrac{20\,000 - 3\,000}{5} = \dfrac{17\,000}{5} = \mathbf{3\,400\text{ \$}}$. |
| **12** | **c ($2,150 and $3,225)** | Dotation annuelle pleine $= \dfrac{30\,000 - 4\,200}{8} = \mathbf{3\,225\text{ \$/an}}$. En 2018 (du 1er mai au 31 déc. $= 8\text{ mois}$) : $3\,225 \times \frac{8}{12} = \mathbf{2\,150\text{ \$}}$. En 2019 (année pleine) : **$3\,225\text{ \$}$**. |
| **13** | **c** | Le mode dégressif (*diminishing-balance*) applique un taux constant à une VNC décroissante, ce qui produit une **charge d'amortissement décroissante à chaque période**. |
| **14** | **d** | Selon IAS 16, la direction doit choisir la méthode qui **reflète le mieux le rythme de consommation des avantages économiques futurs de l'actif**. |
| **15** | **a** | Un changement de durée d'utilité estimée est un changement d'estimation comptable (IAS 8) traité **prospectivement** : la dotation est modifiée **pour l'exercice en cours et les exercices futurs** (pas de retraitement rétroactif). |
