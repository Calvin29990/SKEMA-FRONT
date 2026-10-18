# CAPITAL STRUCTURE & DIVIDEND POLICY — Fiche Complète Session 2 + Corrigé des 4 Group Cases

> **Source :** `cours/S2_CapitalStructure/Session 2 - Capital_Structure_Policy.pdf` (41 slides) + notes de cours `CAPITAL STRUCTURE AND DIVIDEND POLICY 2409.docx`.
> **Cours :** **Mercredi 21/10/2026, 15:00–18:15 — Lille Amphi D 107** (Prof. Muhammad Farooq Ahmad).
> **Objectif de ce fichier :**
> 1. Synthétiser toutes les formules et exemples chiffrés de la Session 2 (*Make-or-Break Co.*, *Risk Shifting*, *Debt Overhang*, *Rest-&-Shirk Co.*, *Trade-off vs Pecking Order*).
> 2. Te donner les **corrigés complets et chiffrés des 4 études de cas de groupe** intégrées aux slides (**AeroNova**, **Helix Pharma**, **LumiTech**, **NovaRetail**) pour intervenir directement mercredi après-midi.

---

## PARTIE 1 — SYNTHÈSE DU COURS : FORMULES & EXEMPLES CHIFFRÉS (SLIDES 1–40)

### 1. Operating Leverage vs. Financial Leverage (Slides 3–6)
- **Operating Leverage (Levier opérationnel)** : causé par les **coûts fixes d'exploitation** (usines, flotte d'avions, magasins). Il amplifie une variation du chiffre d'affaires ($\Delta\text{Sales}$) en une variation plus que proportionnelle de l'**EBIT** :
  $$\text{EBIT} = \text{Sales} \times (1 - v) - \text{Fixed Operating Costs}$$
  *Exemple du cours (Slide 4)* : Normal Sales $= 1\,000$, EBIT $= 300$.
  - **Company A** (coûts variables $50\%$, coûts fixes $200$) : choc de ventes de $\pm 20\%$ ($\text{Sales} = 800\text{ ou } 1\,200$) $\implies \text{EBIT} = 200\text{ ou } 400$ (**$\pm 33\%$**).
  - **Company B** (coûts variables $20\%$, coûts fixes $500$) : choc de ventes de $\pm 20\%$ $\implies \text{EBIT} = 140\text{ ou } 460$ (**$\pm 53\%$**).
- **Financial Leverage (Levier financier)** : causé par les **charges financières fixes (intérêts $I$)**. Il amplifie la variation de l'EBIT en une variation encore plus forte du **résultat revenant aux actionnaires** ($\text{EBIT} - I$) :
  - *Suite Exemple Company B avec $I = 120\text{ €}$ (Slide 5)* : quand l'EBIT varie de $300 \rightarrow 140$ ($-53\%$), le revenu des actionnaires chute de $180 \rightarrow 20\text{ €}$ (**$-89\%$**) !
- **Règle fondamentale de structure du capital (Slide 6)** :
  $$\textbf{Higher Business / Operating Risk } \implies \textbf{ Lower Safe Financial Debt Capacity}$$

---

### 2. Modigliani-Miller Case III & Trade-Off Theory (Slides 2, 7–18)

$$\boxed{V_L = V_U + \text{PV(Tax Shield)} - \text{PV(Expected Financial Distress Costs)}}$$

- **De quoi se composent les coûts de détresse financière (Slides 7–10) ?**
  1. **Direct costs** ($\approx 3\text{–}5\%$ de la valeur de l'actif) : frais d'avocats, banques conseils en restructuration, frais de justice/tribunal, experts.
  2. **Indirect costs** (souvent bien plus élevés : $10\text{–}20\%+$) : perte de clients (garanties, SAV long terme, confiance), durcissement/coupure du crédit fournisseur, départ des ingénieurs/commerciaux clés, ventes forcées d'actifs au rabais (*fire-sale discounts*).
  3. **Lost flexibility** : covenants restrictifs, sous-investissement, distraction du management.
- **Formule du coût espéré de détresse (Slide 9)** :
  $$\text{Expected Distress Cost} = \mathbb{P}(\text{Distress}) \times \text{Economic Loss Given Distress}$$
  *(Un levier plus élevé augmente à la fois la probabilité de défaut ET la sévérité des pertes indirectes).*

- **Exemple chiffré de référence : Make-or-Break Co. (Slides 13–16)**
  - **Données** : Cash-flow opérationnel avant impôt $= 2\,000\text{ \$}$ (Boom, prob. $50\%$) ou $100\text{ \$}$ (Bust, prob. $50\%$). Taux d'IS $\tau = 35\%$, coût du capital non endetté $r_U = 10\%$. Dette perpétuelle $D = 1\,200\text{ \$}$ à $10\% \implies \text{Intérêt promis } I = 120\text{ \$}$. Coût de détresse en cas de défaut (Bust) $= 50\text{ \$ direct} + 50\text{ \$ indirect} = 100\text{ \$}$.
  - **Étape 1 — Valeur non endettée ($V_U$)** :
    $$\mathbb{E}[\text{FCF}_U] = [0{,}5 \times 2\,000 + 0{,}5 \times 100] \times (1 - 0{,}35) = 1\,050 \times 0{,}65 = 682{,}5\text{ \$} \implies \mathbf{V_U = \frac{682{,}5}{0{,}10} = 6\,825\text{ \$}}$$
  - **Étape 2 — PV du bouclier fiscal ($\text{PV(Tax Shield)}$)** *(attention : en Bust, l'EBIT n'est que de $100\text{ \$}$, donc l'intérêt déductible est plafonné à $100\text{ \$}$ !)* :
    $$\mathbb{E}[\text{Tax Shield}] = 0{,}35 \times [0{,}5 \times 120 + 0{,}5 \times 100] = 0{,}35 \times 110 = 38{,}5\text{ \$/an} \implies \mathbf{\text{PV(TS)} = \frac{38{,}5}{0{,}10} = 385\text{ \$}}$$
    *(Sans coûts de détresse : $V_L = 6\,825 + 385 = 7\,210\text{ \$}$).*
  - **Étape 3 — PV des coûts de détresse ($\text{PV(Distress)}$)** :
    $$\mathbb{E}[\text{Distress Cost}] = 0{,}5 \times 0 + 0{,}5 \times 100 = 50\text{ \$/an} \implies \mathbf{\text{PV(Distress)} = \frac{50}{0{,}10} = 500\text{ \$}}$$
  - **Verdict Trade-off** :
    $$\mathbf{V_L = 6\,825 + 385 - 500 = 6\,710\text{ \$} < V_U (6\,825\text{ \$})}$$
    $\implies$ À ce niveau de dette ($1\,200\text{ \$}$), l'endettement **détruit $-115\text{ \$}$ de valeur** car la PV des coûts de détresse ($500\text{ \$}$) dépasse la PV du bouclier fiscal ($385\text{ \$}$).

---

### 3. Coûts et Bénéfices d'Agence de la Dette (Slides 21–33)

$$\boxed{V_L = V_U + \text{PV(Tax Shield)} - \text{PV(Distress Costs)} - \text{PV(Agency Costs of Debt)} + \text{PV(Agency Benefits of Debt)}}$$

| Mécanisme d'agence | Définition & Logique économique | Exemple chiffré des slides |
|---|---|---|
| **Agency Cost 1 : Risk Shifting / Asset Substitution** *(Overinvestment, Slides 22–24)* | Quand l'entreprise est très endettée, la responsabilité limitée donne aux actionnaires un payoff convexe (comme un **Call** sur les actifs de la firme de strike $D$). Ils préfèrent un projet **très risqué à NPV plus faible** car ils captent tout l'upside en cas de succès et transfèrent la perte aux créanciers en cas d'échec. | Dette due $= 500\text{ \$}$.<br>• **Projet 1 (Sûr)** : $50\%$ de $1\,200$ / $50\%$ de $500 \implies \mathbb{E}[\text{Total}] = \mathbf{850\text{ \$}}$ ($\text{Debt} = 500$, $\text{Equity} = \mathbf{350\text{ \$}}$).<br>• **Projet 2 (Risqué)** : $25\%$ de $2\,100$ / $75\%$ de $100 \implies \mathbb{E}[\text{Total}] = \mathbf{600\text{ \$}}$ ($\text{Debt} = 200$, $\text{Equity} = 0{,}25 \times 1\,600 = \mathbf{400\text{ \$}}$).<br>$\implies$ Les actionnaires choisissent le Projet 2 ($400 > 350$) qui détruit $250\text{ \$}$ de valeur totale ! |
| **Agency Cost 2 : Debt Overhang** *(Underinvestment, Myers 1977, Slides 25–27)* | En situation de détresse (la dette existante $D$ dépasse la valeur des actifs), les actionnaires **refusent de financer par fonds propres un projet à NPV strictement positif**, car la valeur créée sert d'abord à renflouer les créanciers existants (*wealth transfer to bondholders*). | Sans projet : Actif $= 50\,000\text{ \$}$, Dette reçoit $50\,000\text{ \$}$, Equity $= 0\text{ \$}$.<br>Nouveau projet : coûte $10\,000\text{ \$}$ aujourd'hui, porte la valeur de la firme à $90\,000\text{ \$}$ en espérance ($\text{NPV} = +30\,000\text{ \$}$), mais la dette faciale est $\ge 100\,000\text{ \$}$.<br>$\implies$ Les créanciers captent $100\%$ des $+40\,000\text{ \$}$ ; les actionnaires paient $10\,000\text{ \$}$ pour recevoir $0\text{ \$}$ $\implies$ **projet rejeté** ! |
| **Agency Benefit : Free Cash Flow Discipline** *(Jensen 1986, Slides 29–32)* | La dette oblige le management à verser le cash excédentaire (service de la dette), réduisant le gaspillage (*empire building*, *shirking*) et concentrant la part d'equity du dirigeant-actionnaire. | **Rest-&-Shirk Co.** : Valeur initiale $1\,000\text{ \$}$, projet coûte $3\,000\text{ \$}$ ($r=10\%$). High effort $\rightarrow 5\,000\text{ \$}$ ; Low effort $\rightarrow 4\,000\text{ \$} + 500\text{ \$}$ de bénéfice privé.<br>• **Financé par Equity** (dirigeant dilué à $25\%$) : High effort $= 1\,500\text{ \$}$ vs Low effort $= 1\,250 + 500 = \mathbf{1\,750\text{ \$}} \implies$ choisit *Low effort*.<br>• **Financé par Dette** ($3\,300\text{ \$}$ à rembourser, dirigeant garde $100\%$) : High effort $= 6\,000 - 3\,300 = \mathbf{2\,700\text{ \$}}$ vs Low effort $= 1\,700 + 500 = 2\,200\text{ \$} \implies$ choisit **High effort** ! |

---

### 4. Asymétrie d'Information, Signaling & Pecking Order Theory (Slides 35–40)
- **Signaling par la dette (Ross 1977)** : émettre de la dette est un signal crédible de bonne santé (*good firm*) car une entreprise fragile (*bad firm*) ne peut pas imiter ce choix sans risquer le défaut de paiement et la perte du poste des dirigeants.
- **Adverse Selection sur les émissions d'actions (Myers & Majluf 1984)** : les dirigeants émettent des actions surtout quand ils savent qu'elles sont surévaluées ; le marché applique donc une décote immédiate à toute annonce d'augmentation de capital.
- **Hiérarchie du Pecking Order** :
  $$\textbf{1. Internal Funds (Cash / Autofinancement)} \;\longrightarrow\; \textbf{2. Safe Debt} \;\longrightarrow\; \textbf{3. Hybrid / Convertible} \;\longrightarrow\; \textbf{4. External Equity (en dernier recours)}$$

---

## PARTIE 2 — CORRIGÉ INTÉGRAL DES 4 ÉTUDES DE CAS EN CLASSE (SLIDES 19, 28, 39, 41)

---

### CASE 1 — AeroNova : Debt-Funded Share Repurchase? (Slides 19–20)

#### 1. Diagnostic chiffré avant vs après l'opération proposée (+€1.0bn de dette pour rachat d'actions)
- **Situation actuelle** :
  - $\text{CA} = 3{,}2\text{ Md€}$, $\text{EBIT} = 320\text{ M€}$ (marge EBIT $= 10\%$).
  - $\text{Dette brute} = 900\text{ M€}$, $\text{Cash} = 250\text{ M€} \implies \text{Dette nette} = 650\text{ M€}$.
  - $\text{Intérêts} = 45\text{ M€}$ (coût moyen de la dette $= 45/900 = \mathbf{5{,}0\%}$).
  - **Ratios actuels (sains)** : $\text{Debt / EBIT} = 900 / 320 = \mathbf{2{,}81\times}$ ($\text{Net Debt / EBIT} = 2{,}03\times$) ; **Interest Coverage ($\text{EBIT / Interest}$)** $= 320 / 45 = \mathbf{7{,}11\times}$.
- **Situation post-transaction si on emprunte $+1{,}0\text{ Md€}$ (en supposant un taux d'intérêt $\ge 5{,}5\%\text{–}6{,}0\%$ vu la hausse du levier, soit $+55\text{ à } +60\text{ M€}$ d'intérêts annuels)** :
  - **Nouvelle dette brute** $= 1\,900\text{ M€}$ ($\text{Dette nette} = 1\,650\text{ M€}$).
  - **Nouveaux intérêts** $\approx 45 + 55 = \mathbf{100\text{ M€}}$ (ou $95\text{ M€}$ à $5\%$).
  - **Nouveaux ratios** : $\text{Debt / EBIT}$ bondit à $1\,900 / 320 = \mathbf{5{,}94\times}$ ($\text{Net Debt / EBIT} = 5{,}16\times$) ; **Interest Coverage chute de $7{,}11\times$ à $\approx \mathbf{3{,}20\times}$** — avant même tout retard du programme aéronautique !

#### 2. Décision recommandée : **REJECT the €1.0bn debt-funded buyback** *(ou au grand maximum approuver un rachat très limité de 150–200 M€ conditionné à la levée de l'incertitude sur le programme avion)*

#### 3. Les 3 arguments structurés selon la grille du prof (Benefit / Distress / Flexibility / Evidence) :
1. **Tax Benefit limité et fragile en cas de choc d'EBIT (Critère 1 : Benefit)** :
   - Sur le papier, $1{,}0\text{ Md€}$ de dette à $5\text{–}6\%$ génère $50\text{–}60\text{ M€}$ d'intérêts, soit un bouclier fiscal théorique de $25\% \times 55 = \mathbf{13{,}75\text{ M€/an}}$.
   - **Mais** l'annonce d'un retard majeur sur un programme avion alors que **60 % du CA dépend de 4 clients** peut faire chuter l'EBIT (fort levier opérationnel dans l'aéronautique). Si l'EBIT baisse fortement (ou si la règle fiscale de plafonnement à $30\%$ de l'EBITDA s'applique), AeroNova ne pourra même plus utiliser pleinement son bouclier fiscal.
2. **Explosion des coûts espérés de détresse financière — directs et surtout indirects (Critère 2 : Distress)** :
   - **Probabilité de détresse élevée** : concentration client extrême ($60\%$ sur 4 avionneurs) + retard programme + échéance de **$600\text{ M€}$ de dette à refinancer d'ici 3 ans**.
   - **Perte en cas de détresse (Loss Given Distress) très forte** : **30 % des actifs sont des machines spécialisées** (faible valeur de revente / forte décote *fire-sale*), et les grands donneurs d'ordres aéronautiques (Airbus/Boeing/Safran) exigent une **fiabilité de livraison à long terme**. Si AeroNova passe à $\approx 6\times\text{EBIT}$ de dette, ses 4 grands clients risquent de réallouer leurs commandes à un concurrent plus solide (*indirect distress cost* destructeur).
3. **Perte critique de flexibilité financière (Critère 3 : Flexibility)** :
   - Le rachat d'actions fait sortir $1{,}0\text{ Md€}$ au profit des actionnaires sans créer aucun actif opérationnel, alors que l'entreprise doit absorber le BFR du programme retardé et refinancer $600\text{ M€}$ à court/moyen terme.
4. **Preuves / données additionnelles à exiger avant toute décision (Critère 4 : Evidence)** :
   - Stress-test de l'EBIT et du Free Cash Flow en cas de retard de 12 à 24 mois du programme aéronautique ; détail de l'échéancier de la dette (maturity wall des $600\text{ M€}$) et des covenants bancaires (plafond Net Debt/EBITDA) ; contrats fermes (*take-or-pay* ou pénalités) avec les 4 grands clients.

---

### CASE 2 — Helix Pharma : Safe Project S vs. Risky Project R (Slide 28)

#### 1. Rappel des données
- Dette à rembourser dans 1 an : **$D = 400\text{ M€}$**.
- Valeur des actifs existants dans 1 an : **$250\text{ M€}$**.
- Coût d'investissement aujourd'hui : **$I_0 = 100\text{ M€}$** (dans un seul des deux projets mutuellement exclusifs).

#### 2. Tableau complet des payoffs dans 1 an (Valeur totale de la firme = Actifs existants $250\text{ M€} + \text{Payoff du projet}$)

| Scénario | État du monde (Probabilité) | Payoff Projet | Valeur Totale Firme ($V_1 = 250 + \text{Projet}$) | Payoff Créanciers $\min(400, V_1)$ | Payoff Actionnaires $\max(0, V_1 - 400)$ |
|---|---:|---:|---:|---:|---:|
| **Sans projet** | $100\%$ | $0\text{ M€}$ | $250\text{ M€}$ | $250\text{ M€}$ | $0\text{ M€}$ |
| **Project S (Safe)** | Succès ($80\%$) | $300\text{ M€}$ | $550\text{ M€}$ | $400\text{ M€}$ | $150\text{ M€}$ |
| | Échec ($20\%$) | $150\text{ M€}$ | $400\text{ M€}$ | $400\text{ M€}$ | $0\text{ M€}$ |
| **$\implies$ Espérance Project S** | **Espérance** | **$270\text{ M€}$** *(NPV $+170\text{ M€}$)* | **$520\text{ M€}$** | **$400\text{ M€}$** *(0 défaut)* | **$120\text{ M€}$** |
| **Project R (Risky)** | Succès ($30\%$) | $700\text{ M€}$ | $950\text{ M€}$ | $400\text{ M€}$ | $550\text{ M€}$ |
| | Échec ($70\%$) | $0\text{ M€}$ | $250\text{ M€}$ | $250\text{ M€}$ | $0\text{ M€}$ |
| **$\implies$ Espérance Project R** | **Espérance** | **$210\text{ M€}$** *(NPV $+110\text{ M€}$)* | **$460\text{ M€}$** | **$295\text{ M€}$** | **$165\text{ M€}$** |

#### 3. Réponses aux 3 questions du prof
1. **Quel projet maximise la valeur totale de l'entreprise ?**
   - C'est **Project S (Safe)** : son payoff espéré est de **$270\text{ M€}$** (contre $210\text{ M€}$ pour R), portant la valeur totale espérée de la firme à **$520\text{ M€}$ contre $460\text{ M€}$** pour R (soit **$+60\text{ M€}$ de valeur supplémentaire** et une NPV de $+170\text{ M€}$ contre $+110\text{ M€}$). De plus, avec le Projet S, la dette de $400\text{ M€}$ devient **100 % sans risque** (remboursée intégralement même dans l'état défavorable : $250 + 150 = 400\text{ M€}$).
2. **Quel projet les actionnaires préfèrent-ils ?**
   - Les actionnaires préfèrent **Project R (Risky)** !
   - En effet, l'espérance de gain des actionnaires est de **$0{,}30 \times (950 - 400) + 0{,}70 \times 0 = \mathbf{165\text{ M€}}$** avec le Projet R, contre seulement **$0{,}80 \times (550 - 400) + 0{,}20 \times 0 = \mathbf{120\text{ M€}}$** avec le Projet S (soit **$+45\text{ M€}$ de mieux pour les actionnaires** avec R !).
   - *(Bonus : si les actionnaires doivent sortir les $100\text{ M€}$ de leur poche aujourd'hui, le Projet S ne leur rapporte que $120 - 100 = +20\text{ M€}$ nets car $150\text{ M€}$ de la valeur créée sert à relever le recouvrement des créanciers de $250\text{ M€}$ à $400\text{ M€}$ — effet **Debt Overhang** — tandis que le Projet R leur rapporte $165 - 100 = +65\text{ M€}$ nets).*
3. **Quel conflit d'agence cela révèle-t-il ?**
   - Cela illustre le conflit d'**Asset Substitution / Risk Shifting (Overinvestment dans le risque)** entre actionnaires et créanciers : en choisissant R plutôt que S, les actionnaires détruisent **$60\text{ M€}$** de valeur totale de l'entreprise mais s'enrichissent de **$+45\text{ M€}$** en expropriant les créanciers de **$-105\text{ M€}$** ($295\text{ M€}$ au lieu de $400\text{ M€}$).

---

### CASE 3 — LumiTech : Cash, Debt or Equity? (Slide 39)

#### 1. Analyse des données du cas
- **Opportunité** : Investissement $I_0 = 300\text{ M€}$, $\text{NPV} = +90\text{ M€} > 0 \implies$ le projet est fortement créateur de valeur et doit être réalisé.
- **Trésorerie** : Cash actuel $= 220\text{ M€}$, buffer opérationnel minimum requis $= 100\text{ M€} \implies$ **Cash excédentaire mobilisable immédiatement $= 220 - 100 = \mathbf{120\text{ M€}}$**.
- **Asymétrie d'information majeure** : le cours de bourse actuel est de **$38\text{ €}$**, alors que le management sait que la vraie valeur intrinsèque est de **$50\text{ €}$** (sous-évaluation de **$-24\%$**, soit $12\text{ €}$ par action) en raison d'une annonce produit majeure dans 6 mois qui ne peut pas encore être divulguée.

#### 2. Plan de financement recommandé (Combinaison optimale : Cash excédentaire + Dette à 5 ans)
$$\boxed{\text{Plan optimal } (300\text{ M€}) = \mathbf{120\text{ M€ d'autofinancement (Cash excédentaire)}} + \mathbf{180\text{ M€ de Dette à 5 ans à } 5{,}5\%} + \mathbf{0\text{ M€ d'Equity}}}$$

#### 3. Justification par la Pecking Order Theory ET la Flexibilité Financière
1. **Pourquoi $0\text{ M€}$ d'émission d'actions (Pecking Order / Adverse Selection)** :
   - Émettre $300\text{ M€}$ d'actions à $38\text{ €}$ alors qu'elles valent $50\text{ €}$ obligerait à émettre $300 / 38 = 7{,}89\text{ M}$ d'actions (au lieu de $6{,}00\text{ M}$ à la juste valeur), transférant **$7{,}89\text{ M} \times (50 - 38) \approx 94{,}7\text{ M€}$ de valeur** des actionnaires actuels vers les nouveaux entrants (soit **plus que la totalité de la NPV de $+90\text{ M€}$ du projet !**). De plus, l'annonce d'une augmentation de capital enverrait un signal négatif au marché.
2. **Pourquoi utiliser $120\text{ M€}$ de Cash (et pas les $220\text{ M€}$ totaux)** :
   - Selon le *Pecking Order*, les fonds internes ($120\text{ M€}$ disponibles au-dessus du buffer) sont la source n°1 car ils ne souffrent d'aucune asymétrie d'information ni coût de transaction.
   - Mais la **flexibilité financière** interdit de descendre sous le buffer opérationnel de $100\text{ M€}$ (notamment pendant les 6 mois précédant le lancement du nouveau produit).
3. **Pourquoi compléter par $180\text{ M€}$ de Dette à 5 ans à $5{,}5\%$** :
   - L'endettement actuel est modeste et l'EBIT est positif et stable : LumiTech a une capacité d'endettement intacte (faible coût de détresse + intérêts de $180 \times 5{,}5\% = 9{,}9\text{ M€/an}$ fiscalement déductibles).
   - La dette est peu sensible à l'asymétrie d'information sur l'upside du nouveau produit ; et une fois l'annonce produit faite dans 6 mois (quand l'action remontera vers $50\text{ €}$) et les cash-flows générés, LumiTech pourra désendetter ou refinancer à d'excellentes conditions.

---

### CASE 4 — In-Class Mini Case : Should NovaRetail Add Debt? (€800m Share Buyback — Slide 41)

#### 1. Diagnostic chiffré : Avant vs. Après l'émission de $+800\text{ M€}$ de dette pour rachat d'actions
- **Avant l'opération** :
  - $\text{CA} = 8{,}0\text{ Md€}$, $\text{EBIT} = 640\text{ M€}$ (marge EBIT $= 8{,}0\%$, demande stable, réseau de magasins tangibles).
  - $\text{Dette brute} = 1\,200\text{ M€}$, $\text{Cash} = 400\text{ M€} \implies \text{Dette nette} = 800\text{ M€}$.
  - $\text{Intérêts} = 60\text{ M€}$ (coût de la dette $= 60 / 1\,200 = \mathbf{5{,}0\%}$).
  - $\text{Debt / EBIT} = 1\,200 / 640 = \mathbf{1{,}875\times}$ ($\approx 1{,}9\times$) ; $\text{Net Debt / EBIT} = \mathbf{1{,}25\times}$ ; **Interest Coverage** $= 640 / 60 = \mathbf{10{,}67\times}$.
- **Après l'opération ($+800\text{ M€}$ de dette à $\approx 5{,}0\text{–}5{,}5\%$, soit $+40\text{ à } +44\text{ M€}$ d'intérêts)** :
  - **Nouvelle dette brute** $= \mathbf{2\,000\text{ M€}}$ ($\text{Dette nette} = 1\,600\text{ M€}$).
  - **Nouveaux intérêts** $\approx \mathbf{100\text{ à } 104\text{ M€}}$.
  - **Nouveau $\text{Debt / EBIT}$** $= 2\,000 / 640 = \mathbf{3{,}125\times}$ ($\text{Net Debt / EBIT} = \mathbf{2{,}50\times}$).
  - **Nouvel Interest Coverage** $= 640 / 100 = \mathbf{6{,}40\times}$ (reste très confortable, $> 6\times$ !).

#### 2. Recommandation : **APPROVE / INCREASE DEBT (oui au principe d'augmenter le levier, idéalement de 500 à 800 M€ après vérification des baux IFRS 16)**

#### 3. Les arguments clés (Contrast parfait avec AeroNova !)
1. **Fort bénéfice fiscal utilisable + Discipline d'agence (Tax Shield & Agency Benefits)** :
   - Contrairement à une biotech ou à un équipementier cyclique, NovaRetail génère un **EBIT élevé et régulier de $640\text{ M€}$** (couverture des intérêts post-opération de $6{,}4\times$). Le bouclier fiscal additionnel ($\tau = 25\% \times 40\text{ M€} = \mathbf{10\text{ M€/an}}$ de cash fiscal économisé, soit une PV de $200\text{ M€}$ en perpétuité à $5\%$) sera **intégralement utilisé**.
   - Comme la croissance est modérée (*moderate growth*) et le Free Cash Flow abondant, augmenter la dette réduit le risque d'agence de gaspillage du FCF (*Jensen's Free Cash Flow discipline*).
2. **Coûts espérés de détresse faibles (Low Expected Distress Costs)** :
   - **Faible risque opérationnel** : demande alimentaire/retail stable, faible volatilité des cash-flows.
   - **Actifs tangibles à forte valeur de garantie** : un réseau de magasins physiques (*tangible store network*) offre un collatéral réel qui réduit la perte en cas de défaut (*Loss Given Distress*), et les clients d'un distributeur ne demandent pas de garanties SAV à 10 ans (contrairement à AeroNova).
3. **Les 3 informations complémentaires à vérifier avant de signer (Extra Data Needed)** :
   - **Dettes de loyers (IFRS 16 Lease Liabilities) et DPO fournisseurs** : dans le retail, une grande partie de l'endettement réel est dans les baux des magasins et le crédit fournisseur. Il faut vérifier que les $1{,}2\text{ Md€}$ de dette incluent bien les baux IFRS 16 et que le crédit fournisseur ne comporte aucun arriéré.
   - **Notation de crédit cible (Investment Grade BBB/BBB+)** et **covenants bancaires**.
   - **Besoins de CapEx de transition digitale / e-commerce** pour s'assurer que le service de la dette ne bride pas la modernisation du réseau.
