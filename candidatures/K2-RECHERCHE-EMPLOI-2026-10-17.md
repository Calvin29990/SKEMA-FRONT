# K2 SKEMA « International Students Job Search » + 3 nouveaux docs — exploitation pour la recherche de Calvin (17/10/2026)

> **Sources traitées dans ce fichier**
> 1. Page K2 *Career Toolkit → Job Search → International Students Job Search* (texte collé le 17/10/2026, page modifiée le 15/09/2026 sur K2).
> 2. `Finance (1) (2).pdf` — « Parcours types – SKEMA BS », Finance **CFM / Sustainable Finance & Fintech / AMAIS** (36 pages, Canva, déc. 2025).
> 3. `Finance (2) (1).pdf` — « Parcours types – SKEMA BS », Finance **Financial Markets & Investments (FMI)** (10 pages, 9 parcours uniques — les pages 6 et 10 sont le même parcours).
> 4. `SKEMA Professional Missions DATABASE 2021 to 2025_UPDATED 092025 (1).xlsx` — la base Excel des missions professionnelles SKEMA, exactement celle que la page K2 §4 recommande de télécharger.
>
> ⚠️ **Retrouvaille technique** : les 3 fichiers n'étaient **pas sur notre branche**. Tu les avais uploadés sur la branche `arena/789b026a-skema-front` (celle du plan master de Cléanne). Je les ai rapatriés à la racine de la branche de cette session, noms inchangés, comme sur ta capture. Travail ci-dessous appliqué à **ta recherche à toi (Calvin, M2 CFM, cible sales marchés/FX)** — pas au plan candidatures master de Cléanne.
>
> 🔐 **Sécurité** : le lien d'accès GoinGlobal collé contient un identifiant d'accès SKEMA (`accid=…`). Je ne l'ai **pas recopié dans le repo** (règle : pas de tokens). Retrouve-le sur la page K2 d'origine et ne le diffuse pas hors SKEMA.

---

## 0. TL;DR — ce que ces docs changent concrètement

1. **Convera Paris remonte en Priorité 1 bis.** La base prouve 2 missions SKEMA en 2024 chez **Convera Europe SA (Courbevoie, 92400)** : *Assistant Sales Forex Derivatives* et *Corporate Hedging Manager Assistant (Assistant FX Sales/Structuring Derivatives)*. C'est ton intitulé cible mot pour mot, avec précédent SKEMA. Le runbook du 26/09 mettait Convera en « veille » — la base dit l'inverse : c'est le seul broker FX corporate pur avec pipeline SKEMA démontré sur le desk hedging parisien.
2. **iBanFirst confirmé, mais l'axe est Paris *vente indirecte* + Bruxelles.** 13 missions (8 en 2023+), dont *Assistant Sales FX – Vente indirecte* (Paris 75116, 2024, profil CFM !), *FX Derivatives Sales Intern* (Paris 75116, 2024) et *FX Derivatives Sales* (21000 Dijon, 2023 — implantation régionale). 8 des 13 lignes sont en **Belgique** : garder aussi l'angle Bruxelles.
3. **Ebury et StoneX : zéro mission SKEMA dans la base (0/39 824).** Ça ne les disqualifie pas (les CDI juniors Ebury vus le 26/09 existent), mais ça veut dire **candidature à froid, aucun alumni à activer**. À effort égal, un employeur avec précédent SKEMA + alumni identifiable passe devant.
4. **Un track entier manquait au runbook : les brokers/intermédiaires de marché parisiens.** **Marex SA** (22 missions, 19 en 2023+ : assistant broker, futures & options, sales structurés, **Junior Broker en CDI en 2024**), **Aurel BGC** (28, dont *Junior Broker*), **TP ICAP Europe** (12 : broker inflation swaps, sales & structuring), **Tradition / TSAF / GFI** (*Assistant broker en swap de taux et swap de change*, 2024). Petit monde, recrutement junior récurrent, produits dérivés au quotidien : très compatible avec ton positionnement Hull/FX/dérivés et ton FR natif.
5. **Des spécialistes FX parisiens « à taille humaine » avec stagiaires SKEMA existent** : **Finomie / Mondial Change** (*Stage Corporate FX Sales* 2025 ; *Corporate Forex Sales* 2023 — c'est la même société, Finomie = raison sociale, Mondial Change = nom commercial, SARL parisienne de 1 à 5 salariés : valeur = réseau/référence FX PME, capacité CDI ≥ seuil visa à vérifier avant d'y investir du temps) et **Kamix** (*FX Sales*, Courbevoie, 2024).
6. **Le « sales marchés » au sens large est une autoroute SKEMA** : 300 missions « SALES » en Finance de marché depuis 2023 (SG 22, Natixis, BNP, Kepler Cheuvreux, Marex, CACIB, HSBC…), avec des conversions en CDI documentées : **Citi – Sales & Trading Program Analyst (CDI, Paris, 2025)**, **Kepler Cheuvreux – Junior Sales (CDI, 2025)**, **J.P. Morgan – CIB Analyst S&T (CDI, 2023)**. La base conforte ton Track B autant que ton Track A.
7. **Barclays validé par les données** : 18 missions, **17 depuis 2023** (Paris 75008 : sales trading equity, S&T structuring, cash equity sales). Tes 2 candidatures Barclays Paris « Under Consideration » (au 30/09) visent une maison qui prend des SKEMA chaque année sur ces desks.
8. **Lucidité visa** : sur 27 missions d'étudiants de nationalité gabonaise dans toute la base, **aucune en finance de marché front-office**. Les précédents « non-Français en sales à Paris » existent (ex. Fixed Income Sales chez Mediobanca Paris 2024 – Togolaise ; Cash Equity Sales Barclays 2023 – Marocaine ; **CDI Analyste risque de marché FX Derivatives chez Optima Advisory 2024 – Camerounaise**) : la preuve de concept visa existe donc, mais **tu serais pionnier côté Gabon** — d'où l'importance du fixe ≥ ~32 k€ (règle du repo) et des employeurs habitués aux profils internationaux.
9. 🚫 **Piège relevé dans la base** : *« VIE Corporate Sales – IRD and FX » @ CACIB (2025)*. Le VIE est réservé aux ressortissants France/EEE (18–28 ans) → **tu n'es pas éligible en nationalité gabonaise**. Ne poursuis CACIB que sur les formats stage/CDI, jamais en VIE.

**Livrable compagnon** : [`K2-SHORTLIST-DB-SKEMA-2026-10-17.csv`](K2-SHORTLIST-DB-SKEMA-2026-10-17.csv) — 442 missions filtrées pour toi (Tier 1 FX : 37 · Tier 2 broker/sales-trading : 40 · Tier 3 sales marchés/structurés : 365), à ouvrir dans Excel (séparateur `;`).

---

## 1. Inventaire des 3 nouveaux docs

| Fichier | Ce que c'est | Contenu utile | Limite |
|---|---|---|---|
| `SKEMA Professional Missions DATABASE 2021 to 2025_UPDATED 092025 (1).xlsx` | Base K2 « former SKEMA students' professional missions » (§4 de la page K2) | **39 824 missions** (onglet 1), 2021→2025 (+68 début 2026) : intitulé, contrat, programme, nationalité, dates, entreprise, code postal, pays. Onglets 2–3 = alternances BBA/ESDHEM/PGE (1 573 l.) et MS (4 030 l.), moins utiles pour toi | **Aucun nom d'étudiant** : c'est une base *entreprises + intitulés + années*, pas un annuaire. Pour retrouver les personnes → LinkedIn/annuaire alumni (§9). Nationalité `UNKNOWN` dans **48,1 %** des lignes : l'absence de précédent étranger chez un employeur ne prouve rien |
| `Finance (1) (2).pdf` (9,2 Mo, 36 p.) | Parcours types CFM/SFF/AMAIS (ta majeure) | Chaînes L3 → césure(s) → fin d'études de 36 étudiants. Dominante : audit Big 4 / finance d'entreprise. Passerelles sales/marchés listées §7 | Parcours anonymisés, effet « vitrine » K2/orientation : utile pour les trajectoires crédibles, pas comme stats |
| `Finance (2) (1).pdf` (2,6 Mo, 10 p.) | Parcours types FMI | 9 parcours uniques, fins d'études : Natixis IB, **Citi Markets Graduate**, **JPM Market Sales Program**, Edmond de Rothschild CF, **Jefferies Equity Sales**, Julius Baer Collateral Trading, Goldman IB, Moody's Analytics, Mandarine Gestion | Idem. Note : pages 6 et 10 = même parcours dupliqué |

Chiffres de cadrage de la base (onglet 1) : Stage = 30 083 lignes (76 %) · CDI = 708 · Finance de marché = **2 827** (1 747 depuis 2023) · secteur Banque/Assurance/Finance = 5 428 · programmes contenant « Corporate Financial Management » = 1 134 (362 depuis 2023) · « Financial Markets » = 388 (128 depuis 2023).

**Top employeurs Finance de marché 2023+** (toutes fonctions) : Société Générale (69) · Natixis SA (45) · CACEIS Bank Luxembourg (32+) · Amundi (31) · BNP Paribas (30) · SG Private Banking (23) · Kepler Cheuvreux (19) · **Marex SA (17)** · HSBC Continental Europe (14) · CACIB (~24 sous 3 libellés) · CIC (12) · Rothschild (12) · Aurel BGC (9) · Oddo (8) · Lazard Frères Gestion (8) · JPM (7) · UBS · Barclays…

---

## 2. La page K2 en 8 axes → version Calvin (pas version générique « international student »)

La page K2 vise l'étudiant international **non-francophone**. Ton cas est différent : **francophone natif + titre de séjour gabonais à convertir**. Ta barrière n'est pas la langue, c'est le **statut + le seuil de salaire**. Traduction axe par axe :

| # | Axe K2 | Verdict pour toi | Action concrète (datée §10) |
|---|---|---|---|
| 1 | Comprendre le marché FR (France Travail, APEC, GoinGlobal) | ⚠️ Hiérarchiser : pour les desks, France Travail/APEC ne sont **pas** le canal (utile en appoint : trésorerie/credit PME, sales corporate régionaux). **GoinGlobal = le vrai outil** pour les guides pays Luxembourg/Allemagne/NL/Espagne si tu élargis. CDD/CDI : tu vises déjà le bon format | Alertes APEC/France Travail en mode passif uniquement ; GoinGlobal réservé aux dossiers Lux/DE/NL. Note : K2 écrit encore pole-emploi.fr → c'est **francetravail.fr** |
| 2 | Maîtriser le français | ✅ **Coché d'office** (FR natif). Ton équivalent de cet axe = **anglais de desk** (entretiens EN Barclays/Citi/JPM) + **différenciateur ES/PT** | Vends FR(natif)/EN/ES/PT comme couverture **EMEA + LatAm + Afrique francophone**, pas comme ligne « langues » décorative. Preuves base : Aurel BGC **Madrid** (Junior Broker CDI 2025), Banco BPI **Lisbonne** FX & Derivatives (2025), desks parisiens Iberia |
| 3 | Alumni & networking (SKEMA Alumni 60 000, LinkedIn, France Alumni) | 🔥 **C'est LE levier que les 3 docs rendent enfin actionnable** : la base donne entreprise + intitulé + année → l'annuaire alumni/LinkedIn donnent la personne. France Alumni = secondaire pour toi (réseau post-retour) | Protocole complet §9 : 20 demandes ciblées/sem. sur les Tier 1–2 de la shortlist CSV |
| 4 | Entreprises « international-friendly » (Tech/Finance/Luxe/Hospitality) + **base Excel des missions** | 🔥 Fait dans ce fichier (§3–6). Version Calvin : « international-friendly » = a déjà pris un **non-UE en front-office à Paris** ou fait des **CDI jeunes ≥ seuil**. Glassdoor/Indeed FR = vérification réputation/salaires avant entretien, pas canal principal | Utilise le CSV comme liste de ciblage ; Glassdoor pour préparer les questions « process/salaire » Ebury/iBanFirst/Convera |
| 5 | Élargir à l'Europe (EURES, StepStone DE, Moovijob Lux, NationaleVacaturebank NL, jobs.ac.uk) | ✅ Pertinent mais à classer par **preuve SKEMA** (§8). jobs.ac.uk = académique, quasi inadapté à la finance privée UK → eFinancialCareers UK à la place | Ordre d'élargissement : **Luxembourg → Belgique (Bruxelles iBanFirst) → Espagne (ES) → Pays-Bas (EN, OTC Flow) → UK (visa dédié) → Portugal (PT, plutôt ops)**. Allemagne : signal SKEMA faible (25 missions FM) |
| 6 | Job fairs & events (JobTeaser SKEMA, gethighered.com) | ✅ Canal chaud sous-utilisé dans tes fichiers actuels | Vérifier **JobTeaser → Événements** chaque lundi ; gethighered (EFMD) en appoint. Préparer la liste « stands à visiter » = entreprises Tier 1–2 |
| 7 | CV/lettre standards FR (CV 1–2 p., lettre adaptée, cours CV Career Toolkit) | ⚠️ Écart réel détecté : ton `documents/CV_Calvin_MINANG.pdf` affiche « Stages / Off-Cycle & Graduate 2026 » alors que le runbook du 26/09 assume une posture **CDI direct**. Un recruteur CDI qui lit « stage » en en-tête écarte. Portfolio PDF = images sans texte extractible → invisible pour les ATS | Produire **2 CV** (§10.3) : A « Corporate FX Sales — CDI » / B « Markets — Off-Cycle & Graduate » ; suivre le cours CV K2 (id 1267622) pour la version FR ; lettre type par track |
| 8 | Travailler dans ton pays d'origine pour des boîtes internationales | 🪂 Parachute réel mais mince côté Gabon (13 missions dans la base : BICIG, EY Gabon, Meridiam Central Africa…). Plus dense : Côte d'Ivoire (99, banques panafricaines) et **banques africaines à Paris** | À classer **Plan C** (§8) : Bank of Africa France, Attijariwafa Europe (Paris), parapluie UBA/Ecobank — et en faire un argument de niche « couverture Afrique francophone » pour les desks parisiens plutôt qu'un plan A |

---

## 3. Tier 1 — FX corporate / FX sales : les 37 preuves qui comptent (2023+, Europe)

Intitulés contenant FX/Forex/change au sens devise (hors « conduite du changement »). Détail ligne à ligne dans le CSV (TIER = `1-FX corporate/sales`).

| Employeur | Preuve(s) dans la base | Lecture pour toi |
|---|---|---|
| **Convera Europe SA** — Courbevoie | 2024 · *Assistant Sales Forex Derivatives* · *Corporate Hedging Manager Assistant (Assistant FX Sales/Structuring Derivatives)* | **N°1 ex æquo.** Desk hedging corporate, ex-Western Union BS. En direct web (17/10) : offres Paris plutôt seniors (Senior Client Relationship Manager) → voie = réseau alumni + spontanée junior/dealer, + surveiller Greenhouse Convera. Le poste Toronto « FX Sales/Structuring, French speaker preferred » est toujours affiché (option Canada du runbook, visa séparé) |
| **iBanFirst** — Paris 16e/Dijon + Bruxelles | 2024 · *Assistant Sales FX – Vente indirecte* (CFM) · *FX Derivatives Sales Intern* · 2023 · *FX Derivatives Sales* (Dijon) | **N°1 ex æquo.** Seul acteur avec une ligne *exactement* CFM+FX+Paris. Préparer le business case (process déjà documenté au runbook) |
| **HSBC Continental Europe** — Paris 16e | 2025 · *FX & Rates – Corporate Sales Assistant* · 2023 · *Assistant Sales Corporate FX, taux et métaux* · (+ *Stage Sales Junior – Derivatives Clearing* 2025) | Ton dossier HSBC « Origination & Structuration » est en attente de tests : ajoute le desk FX corporate comme cible 2027 |
| **MUFG Bank** — Paris 2e | 2024 · *FX Global Sales* · 2023 · *Global Market – FX Sales Assistant* | Banque japonaise, desk Paris qui prend des SKEMA en FX sales 2 ans de suite : ajout pur vs ton tracking actuel |
| **Commerzbank** — Paris 8e | 2024 · *Assistant Sales FX, IR & Commodities* | Idem, banque allemande à Paris, triple produit FX/taux/commo (tes sujets) |
| **LCL** — Villejuif | 2024 · *Assistant Sales FX, IRD and Structured Products* (+ précédent coverage par une Ivoirienne, 2024) | Salle des marchés LCL = réseau Crédit Agricole, moins visé que CACIB, moins de concurrence |
| **Crédit Agricole IDF** — Paris 12e | 2025 ×2 · *Assistant Sales FX & Rates Derivatives* | Attention : c'est la **caisse régionale IDF**, pas CACIB — clientèle PME/ETI IDF, très « corporate FX » dans l'esprit Ebury avec la solidité bancaire |
| **CACIB** — Montrouge | 2024 · *Flow Forex Sales Assistant – Financial Institutions* · 2023 · *Assistant sales – Short Term Markets & Repo* (Marocaine) · 🚫 2025 *VIE Corporate Sales IRD & FX* (non éligible pour toi) | À poursuivre en stage/off-cycle et CDI, jamais en VIE. Ton test AON CACIB du tracking reste le canal d'entrée |
| **Natixis / Natixis CIB** — Paris 13e | 2024 · *Assistant Sales Corporate FX* (apprentissage) · *Assistant Sales e-FX* | Natixis = 2e employeur FM des SKEMA ; e-FX valorise ton profil terminal/automatisation |
| **BRED** — Paris 12e | 2023 · *FX & IRD Sales Trader Assistant* (+ Assistant trader fixed income) | Banque Populaire, desk parisien — aussi l'employeur du seul précédent bancaire gabonais de la base (assistant middle-office, 2021) |
| **Caisse d'Épargne Bretagne-PDL** — Nantes | 2023 · *FX, IRD & Structured Products Sales Assistant* | Preuve que les caisses régionales BPCE ont des desks change/IRD entreprises (ton historique BPCE y parle). Variante hors-Paris |
| **Société Générale** — La Défense | 2025 · *Business Analyst – Trading Forex orchestration* · 2024 · *Assistance aux sales FX/e-FX* · 2023 · *Assistant Forex Sales IRD*, *Assistant FX Corporate Sales* | ⚠️ **Canal fermé pour toi en sales FX/EM jusqu'à ~août 2027** (blacklist test, voir tracking). Usage base = network/infos + types de postes « autres » autorisés, pas de re-candidature sales FX |
| **BNP Paribas** — Paris/Lux | 2023 · *Trader FX Sales* (BNPP IFS) · *Passive Currency Overlay Assistant* (Luxembourg) | Dépend de l'issue de ton processus BNP d'octobre (à mettre à jour dans le tracking) |
| **Finomie / Mondial Change** — Paris 12e/11e | 2025 · *Stage Corporate FX Sales* · 2023 · *Corporate Forex Sales* | Micro-broker change TPE/PME (1–5 salariés). Intérêt : référence FX PME + réseau, **pas** un plan CDI/visa crédible a priori. À contacter en mode « café métier », pas en priorité candidature |
| **Kamix** — Courbevoie | 2024 · *FX Sales* | Petit acteur FX, même usage réseau |
| **Valeo (corporate)** — Paris 17e | 2023 · *Stagiaire Front Office FX* | Rappel : les **trésoreries de grands groupes** ont des desks FX internes — piste « client-side » compatible CFM (couverture = ton produit) |
| **CACEIS Bank Luxembourg** | 2023/2024/2025 · *Forex Officer* (récurrent, ×3) | ⚠️ Intitulé trompeur : chez un dépositaire, c'est plutôt exécution/ops FX de fonds. Utile Luxembourg, mais **pas du sales** — ne pas confondre (voir §8) |
| **Optima Advisory** — La Défense | 2024 · ***Analyste risque de marché FX Derivatives — CDI — Camerounaise*** | La ligne la plus précieuse côté visa : un CDI FX obtenu par une ressortissante non-UE, en conseil/risk. À mettre dans tes preuves mentales en entretien (« le changement de statut sur ce type de poste se fait ») |
| **Banco BPI** — Lisbonne | 2025 · *FX and Derivatives Markets Intern* | Angle PT (§8) |

**Absent du Tier 1 alors qu'ils sont dans ton runbook** : **Ebury (0 mission)**, **StoneX (0)**, **Monex** (1 seule ligne, contrôle de gestion 2023 — rien côté desk), **CIC Marchés** (le CIC a 110 missions dont 64 récentes, mais les intitulés marchés sont DCM/allocation/coverage — je n'y ai pas trouvé de ligne « sales FX change entreprises » ; le « signal Bordeaux » de Naël reste donc non corroboré par la base).

---

## 4. Tier 2 — NOUVEAU TRACK : brokers / intermédiaires de marché (Paris d'abord)

40 missions 2023+ (CSV, TIER = `2-Broker / sales-trading`). C'est le chaînon manquant entre ton Track A (brokers FX corporate) et ton Track B (CIB) : vente/intermédiation de dérivés entre professionnels — téléphone, produit, pression commerciale, exactement ton pitch Finstart+BPCE+Hull.

| Employeur | Preuves 2023+ | Note web au 17/10 |
|---|---|---|
| **Marex SA** — Paris 8e | Assistant broker (×3), cross-asset derivatives, futures & options, sales structurés, ***Junior Broker en CDI (2024)*** — 17 lignes FM 2023+ | Bureau parisien actif (Capital Markets + Marex Solutions, émetteur de structurés). Offres affichées Paris : plutôt VP (FX Institutional Sales Broker) → junior passe par stage/conversion + réseau. **Candidature spontanée junior + Talent Acquisition directe (Marex dit recruter en direct, sans agence)** |
| **Aurel BGC** — Paris 2e + Madrid | Assistant broker stagiaire (récurrent), equity derivatives, repo, *Junior Broker* ; **Madrid : Junior Broker CDI (2025)** + assistant broker repo | Le desk Madrid + ton ES = l'un des rares angles « langue » prouvés par la base |
| **TP ICAP Europe** — Paris 8e | 2025 · *Intern – Broker, Inflation Swaps* · *Sales & Structuring Intern* · activités de marchés | Leader mondial interdealer ; dérivés de taux = produit voisin direct du change |
| **GFI Group** — Paris 2e | 2024 · *Assistant broker en swap de taux et **swap de change*** (contrat local) | Le « swap de change » est littéralement ton produit corporate FX en version interbancaire |
| **Tradition (TSAF/Tradition SA)** — Paris 1er | *Sales/Trader Fixed Income Intern (2025)*, assistant broker equity derivatives, head of credit desk assistant | Groupe suisse, fort à Paris sur taux/crédit |
| **Kepler Cheuvreux** — Paris 16e (+ Suisse) | 64 missions au total ; *Assistant Sales Trader – Corporate Brokerage*, *Junior Sales **CDI 2025***, assistant sales structurés (Suisse) | Courtier actions européen n°1, prend des SKEMA en continu |
| **Plantureux & Associés, Magen Financial, Square Global** — Paris | Assistant derivatives broker (2024/2025), assistant broker (2025 ×2 + « fintech brokerage »), intermédiaire de marché (2025) | Petites structures parisiennes récurrentes : accès par réseau/spontanée, cycle court |
| **OTC Flow** — Amsterdam (+ ligne France) | ***Junior Sales Broker — CDI (2025)***, energy commodity sales trader | Sales-trading énergie/carbone en anglais à Amsterdam : ton angle « matières premières » (coton, commo) + EN. Hub NL de l'axe K2 §5, prouvé par la base (contrairement aux généralistes NL) |
| **Node Trading** — Paris 16e | *Physical Sugar Trader/Broker Assistant* (2024 ×2) | Négoce physique sucre — niche commodities cohérente avec tes lectures (cotton/softs) |

---

## 5. Tier 3 — Sales marchés / structurés : ce que 365 lignes racontent

- **Le gros du flux** : assistant sales produits structurés / cross-asset (SG, Natixis, BNP, CACIB, Marex, Leonteq, Marigny Capital, Feefty, Equitim, Eleva…), sales fixed income/rates (CACIB, ING, BBVA, Mediobanca), sales trading actions (Barclays, Exane, Kepler). La structuration « retail/CGP » (Marigny, Feefty, Marex Financial Products) recrute des profils commerce+produit comme le tien, avec des cycles plus courts que les CIB.
- **Conversions CDI jeunes documentées en FM (31 CDI seulement en 2023+ dans la base — elle est par construction « stages »)** : Citi S&T Program Analyst (2025), Kepler Junior Sales (2025), JPM CIB Analyst S&T (2023, Italienne), Marex Junior Broker (2024), Optima FX risk (2024, Camerounaise), Aurel BGC Madrid Junior Broker (2025), Kerius Finance Analyste junior (2023, CH), UBS Graduate Talent Program (2023, Norvégienne), CA-CIB Structureur (2024, profil CFM), BNP Paribas Luxembourg Structurer Front Office (2023). **Lecture** : le CDI direct existe mais reste l'exception dans les circuits écoles ; ton runbook a raison de le chercher chez les brokers/fintechs plutôt qu'en CIB.
- **Précédents nationalités non-FR en sales à Paris** (nationalité connue, FM, 2023+) : Togolaise → Fixed Income Sales, Mediobanca · Marocaine → Cash Equity Sales, Barclays ; Sales structurés SG (Tunisienne) ; Rates Sales CACIB (Tunisienne) ; Camerounaise → Global Markets Summer, JPM Londres ; Assistant Sales BNP (Portugal) ; Mauritanienne → Sales Support, KKR Paris. + hors FM strict : Ivoirienne → Analyste coverage institutionnels, LCL (2024 ×2). **Conclusion honnête** : les desks parisiens prennent des non-UE en stage sales chaque année ; l'échantillon « CDI + non-UE » est mince (Optima) — la conversion statut se jouera sur le fixe et la taille de l'employeur, d'où le tiering ci-dessus.

---

## 6. Ce que les « parcours types » Finance t'apprennent (les 2 PDF)

**FMI (9 parcours uniques)** — le modèle « fabrique à sales » : la césure 2 est presque toujours un *Assistant Sales* en salle (Citi, Raymond James, CACIB, SG structurés cross-asset) qui débouche sur un graduate market (Citi, JPM Market Sales, Jefferies Equity Sales). Tableau complet en annexe A.

**CFM/SFF/AMAIS (36 parcours)** — ta majeure part à ~⅔ vers audit/conseil/finance d'entreprise en fin d'études (Deloitte ×2, EY, PwC, Wavestone, Keyrus, Ailancy, Chanel/LVMH/Danone en finance corporate…). Les passerelles marchés **existent mais sont minoritaires et toujours construites un cran plus tôt** :

- BNP structurés (cés. 2) → **Assistant Sales Produits Structurés, Leonteq (Monaco)**
- BNP Paribas Dealing Services : Front Office Fixed Income (cés. 1) → Assistant Trader (cés. 2) → **SG DCM Liability Management**
- Marigny Capital *Assistant Sales – Structured Products* en césure 2 (après HSBC GRM)
- Oddo AM développement commercial → **Boussard & Gavaudan, suivi des opérations de marché**
- Keys Reim : analyse financière → asset management → **Sales – Business Developer** (le seul intitulé « business developer » de fin d'études CFM)
- HSBC credit → SGSS Sales Analyst → HSBC DPM → **SGCIB Impact Based Finance**

**Leçon pour ton positionnement** : tu n'as pas le parcours type (pas d'assistant sales en césure) — inutile de le déguiser. En revanche Finstart (prospection) + BPCE (reporting FX/taux Bloomberg) correspond point par point aux **intitulés réels de la base** : *Assistant Sales Forex Derivatives*, *Corporate FX Sales*, *Assistant Sales Corporate FX*. Ton histoire se raconte côté **FX corporate/brokers**, pas en imitant les FMI sur les structurés actions. Les PDF servent en entretien à montrer que tu connais la cartographie des sorties SKEMA (« je sais où les CFM partent ; je choisis délibérément la voie sales FX, minoritaire mais documentée »).

---

## 7. Révision du runbook CDI FX (croisement avec `CIBLE-CDI-FX-runbook-2026-09-26.md`)

| Cible runbook 26/09 | Verdict base K2 | Ajustement |
|---|---|---|
| Rocket4Sales (P0, via Naël) | Hors base (cabinet) — non contradictoire | Inchangé : canal chaud n°1. Ajoute à ton brief agent les maisons Tier 1–2 (ils chassent fintech/FX **et** brokers) |
| **Ebury Paris (P1)** | **0 mission SKEMA** | Reste P1 sur « CDI junior ouvert maintenant », mais **à froid** : lettre + Glassdoor, pas d'alumni à attendre |
| **iBanFirst (P2)** | 13 missions, CFM Sales FX Paris | **↑ P1** — précédent exact |
| **Convera (P2 « veille »)** | 2 missions 2024 exactement sur ton desk | **↑ P1** — spontanée + alumni des 2 stagiaires 2024 |
| StoneX (P3) | **0 mission** | Reste P3/veille, spontanée LatAm inchangée |
| Monex (P3) | 1 mission hors desk | ↓ veille LinkedIn seulement |
| CIC Marchés (P3) | CIC massif dans la base, **pas de ligne FX sales** trouvée | Garder via canal Naël/Bordeaux, ne pas y investir de spontanée générique |
| CACIB track B | Flow Forex + Sales salle des marchés 2025 | Confirmé, hors VIE |
| **— nouveau — Marex / Aurel BGC / TP ICAP / GFI / Tradition** | 60+ missions cumulées, CDI juniors prouvés | **Créer Track A2 « brokers parisiens »**, même priorité que les fintechs FX |
| **— nouveau — MUFG Paris, Commerzbank Paris, LCL Marchés, CA-IDF Marchés, BRED** | Lignes FX sales 2023–2025 | Track B « banques à desk FX Paris qui prennent des SKEMA » — souvent moins saturées que BNP/SG/Natixis |

---

## 8. Élargissement Europe & Plan C (axes K2 §5 et §8, triés par preuve)

1. **Luxembourg (Moovijob + sites carrières)** — 122 missions FM 2023+. Véritables portes front : **CA Indosuez Wealth Europe** (*Cross Asset Derivatives Sales – Advisory*, 2025), BNP Paribas Luxembourg (*Structurer Front Office*, CDI 2023), Edmond de Rothschild AM Europe (précédent Marocaine client service), Quintet (Graduate Program CDI). ⚠️ Le volume **CACEIS** (Forex/Collateral/Derivatives Officer) est du **middle/ops dépositaire** : tremplin Lux possible, mais étiquette-le comme tel dans ton tracking pour ne pas diluer le positionnement front. Aussi : Langham Hall Lux a pris une Gabonaise en fund accounting (2023) — preuve qu'un sponsor luxembourgeois pour profil gabonais existe déjà, hors front.
2. **Belgique / Bruxelles** — iBanFirst HQ (8 missions), Degroof Petercam, Candriam. FR + EN, coût d'entrée bas depuis Lille/Paris.
3. **Espagne (ton ES)** — Aurel BGC Madrid (CDI junior broker + stage repo), Kepler Madrid, Tradition Madrid, BBVA Paris en miroir. Petit volume, différenciateur fort.
4. **Pays-Bas / Amsterdam (EN)** — OTC Flow (CDI junior sales broker) ; sinon la base SKEMA y est quasi vide en FM (3 lignes) : à attaquer via GoinGlobal + NationaleVacaturebank/eFinancialCareers NL plutôt que via alumni.
5. **Royaume-Uni** — Barclays/JPM/Bloomberg (Sales & Analytics) existent dans la base, mais **visa UK autonome** (Skilled Worker/Graduate) : ne disperser que si un process précis avance. Ta ligne CV « mobilité Paris / Londres » suppose ce chantier visa — à assumer ou retirer.
6. **Portugal (ton PT)** — Banco BPI FX & Derivatives (2025) en front lisbonnin ; le reste (BNP/Natixis Porto) est surtout ops/IT. Angle : Brazil desks couverts depuis Lisbonne — à tester en entretien réseau, pas en candidatures masse.
7. **Monaco** — 63 missions FM : sales structurés/CGP et banque privée (Privatam, CMB, Edmond de Rothschild Monaco, Leonteq SAM via parcours CFM). Filière « structurés distribution » compatible avec un profil sales, permis de travail monégasque porté par l'employeur.
8. **Allemagne** — 25 missions FM (UniCredit/HypoVereinsbank surtout) : StepStone/EURES en veille passive seulement.
9. **Plan C — Afrique / banques africaines** : Gabon = 13 missions (BICIG, EY/EXCO Gabon, Meridiam Central Africa…). Côte d'Ivoire = 99 (SIB, UBA CI, Ecobank CI, Bridge Bank, KPMG CI). À Paris : **Bank of Africa France** (ligne 2023), **Attijariwafa Bank Europe** (le groupe a une ligne *FX & Commodities Derivatives Trader Assistant* au Maroc, 2024). Usage recommandé : **niche d'expertise** (« je couvre la clientèle Afrique centrale francophone ») vendue à un desk parisien/londonien EM, plutôt que retour immédiat — sauf si le statut FR se ferme.

---

## 9. Retrouver les humains derrière la base (protocole alumni)

La base ne contient aucun nom : chaque ligne utile se transforme en recherche **« SKEMA + entreprise + intitulé proche + année ±1 »**.

**Où chercher, dans l'ordre** : ① annuaire **SKEMA Alumni** (alumni.skema.edu — filtres entreprise/fonction/promo) ② LinkedIn (filtre École = SKEMA Business School, Entreprise actuelle ou passée = cible, mots-clés) ③ JobTeaser SKEMA (offres + événements où ces maisons exposent).

**Requêtes type à copier (1 entreprise = 1 recherche)** :

- LinkedIn, champ mots-clés : `"FX Sales" OR "Forex" OR "Corporate Hedging"` + École `SKEMA` + Lieu `Paris` ; variantes : `"Assistant Sales" "produits structurés"`, `"Junior Broker"`, `"Sales Trader"`, `"Derivatives" "Broker"`, `"e-FX"`.
- Google : `site:linkedin.com/in SKEMA Convera` · `site:linkedin.com/in SKEMA iBanFirst "FX"` · `site:linkedin.com/in SKEMA Marex broker` · `site:linkedin.com/in SKEMA "Aurel BGC"` · `site:linkedin.com/in SKEMA "TP ICAP"`.
- Cibles par ordre de valeur : stagiaires 2024 Convera (2) · stagiaire CFM 2024 iBanFirst Sales FX · Junior Broker Marex entré vers 2024 · assistantes FX sales HSBC/MUFG/LCL 2023–2025 · CDI Optima 2024 (question visa).

**Message type (court, factuel — ne jamais affirmer « c'est vous la ligne de la base » si tu n'es pas sûr)** :

> Bonjour [Prénom], je suis en dernière année à SKEMA (M2 MSc Corporate Financial Management, Lille) et je prépare une entrée en sales change/marchés (expériences : reporting FX multi-actifs chez BPCE, prospection B2B chez Finstart). En travaillant sur la base des missions SKEMA, j'ai vu que [Convera Paris] avait accueilli des stagiaires en *FX Sales/Structuring* en 2024. Auriez-vous 15 minutes pour me dire comment fonctionne le desk et ce qui compte pour y entrer en junior ? Merci d'avance, Calvin Minang

Version EN (desks anglos) : même structure, 4 phrases max, objet « SKEMA M2 CFM — 15 min on [firm]'s FX sales desk? ».

**Règles** : 1 relance à J+7 max · noter chaque contact dans le tracking (§10) · préparer 3 questions métier avant chaque call (produit, clientèle PME vs FI, licence/conformité MiFID du rôle) · remercier + proposer de renvoyer l'ascenseur (notes de marchés, terminal CalvinX).

---

## 10. Plan d'action

### 10.1 Semaine du 18→24/10 (mise en route K2)

- [ ] **GoinGlobal** : ouvrir le compte via le lien K2 (page d'origine, ne pas enregistrer le lien `accid` dans le repo) ; télécharger les guides Luxembourg et Espagne ; rien d'autre pour l'instant.
- [ ] **JobTeaser SKEMA** : créer 3 alertes offres (`FX`, `Sales – finance de marché`, `Broker / intermédiaire de marché`) + consulter l'onglet **Événements** ; viser en priorité les événements où figurent des maisons Tier 1–2.
- [ ] **SKEMA Alumni** : vérifier l'accès annuaire ; lancer les 5 requêtes §9 (Convera, iBanFirst, Marex, HSBC FX, MUFG) ; **10 demandes LinkedIn envoyées** avec le message type.
- [ ] Filtrer le CSV : TIER 1 → onglet de travail « 37 lignes FX » ; cocher les 10 entreprises à attaquer en spontanée en novembre.
- [ ] Poser les alertes passives K2 §1–§5 : **APEC** (« chargé d'affaires entreprises / trésorerie / change »), **France Travail** (mêmes mots, IDF), **Moovijob** (Luxembourg : FX, sales, dealing), **EURES** (FX sales, broker), **eFinancialCareers FR** (déjà fait — ajouter Marex/Aurel/TP ICAP/Tradition en entreprises suivies).

### 10.2 Semaine du 25→31/10 (première vague de candidatures « avec précédent »)

- [ ] Spontanées ciblées (CV A) : **Convera Europe (Courbevoie)**, **Marex Paris (Talent Acquisition directe)**, **Aurel BGC Paris**, **TP ICAP Europe** ; (CV B si format stage/off-cycle) : **HSBC FX & Rates Corporate Sales**, **MUFG Paris Markets**, **LCL Marchés**, **CA-IDF salle des marchés**.
- [ ] **iBanFirst** : candidature dès apparition d'une offre junior/BD (WTTJ) + message à l'alumni CFM 2024 ; version Bruxelles en parallèle.
- [ ] Relances réseau J+7 ; viser **2 calls alumni réalisés** fin octobre.
- [ ] Mettre à jour `TRACKING-CANDIDATURES-2026-2027.md` : statuts réels post-tests d'octobre (BNP, AON, HSBC…) — la version du 30/09 est périmée et toutes les priorités ci-dessus doivent s'y brancher.

### 10.3 Deux CV à produire (audit éclair vs standard K2 §7)

Ton CV actuel (1 page) est propre dans la forme mais **raconte une recherche de stage 2026 en risk**. À décliner :

| | CV A « Corporate FX Sales — CDI » | CV B « Markets — Off-Cycle / Graduate » |
|---|---|---|
| En-tête | Business Developer FX / Corporate FX Sales — CDI, disponibilité fin de scolarité | Sales & Trading / Market Risk — off-cycle & graduate 2027 |
| 1ʳᵉ expérience mise en avant | Finstart (vente/prospection) puis BPCE (produit FX) | BPCE (marchés) puis projets (terminal, pricer) |
| Preuves | prospection, appels, base clients, produits de couverture PME (spot/forward/swap), ES/PT | BQL, VaR, grecques, automatisation, FRM candidate |
| Emplois | Ebury, Convera, iBanFirst, brokers Tier 2 | Barclays, Citi, HSBC, CACIB, Marex Solutions |

Compléments : suivre le **cours CV du Career Toolkit** (K2, id 1267622) pour la version FR ; lettre d'1 page max par track reprenant le pitch légitimité du runbook ; générer une version **texte du portfolio** (l'actuelle est en images, illisible par les ATS).

### 10.4 Routine hebdo (à partir de novembre, 2 h/sem.)

Lundi : JobTeaser événements + offres Tier 1–2 (20 min) → Mercredi : 10 contacts alumni (45 min) → Vendredi : candidatures/relances + mise à jour tracking (45 min) → 1 veille GoinGlobal/Glassdoor avant chaque entretien. Règle visa inchangée : **ne signer que ≥ ~32 k€ fixe** (changement de statut direct) et avancer les deux mondes ensemble (CDI ↔ titre qui expire le 30/01/2027) — les mondes SKEMA/compta du dossier archive restent prioritaires en parallèle.

---

## Annexe A — Parcours types FMI (9 uniques) et passerelles CFM

**FMI — fin d'études :** Natixis *Investment Banking Analyst* · Citi *Markets Graduate Analyst (Markets & Securities Services)* · JPM *Market Sales Program* · Edmond de Rothschild CF *Analyste M&A* · Jefferies *Equity Sales Intern* · Bank Julius Baer *Collateral Trading & Management Intern* · Goldman Sachs *Investment Banking Seasonal* · Moody's Analytics *Development Representative* · Mandarine Gestion *Analyste Actions*.
Étapes sales intermédiaires typiques : Assistant Sales Citi / Front Office Assistant Sales Raymond James Euro Equities · Assistant Sales CACIB · Assistance Sales Produits Structurés Cross-Asset SG (après Exane BNP Paribas research/advisory) · Analyste Coverage HSBC → Syndication SG · Produits/dérivés La Française → Oddo AM.

**CFM/SFF/AMAIS — fins d'études sales/marchés (sur 36)** : Leonteq Securities (Assistant Sales Produits Structurés, Monaco) · SG La Défense (DCM Liability Management) · Keys Reim (Sales – Business Developer) · Boussard & Gavaudan (suivi opérations de marché) · SGCIB (Impact Based Finance). Le reste : audit/conseil (Deloitte ×2, EY ×2, PwC, Wavestone, Keyrus, Ailancy, Renault, FINETIC), PE/VC/M&A/RE (Ardian RE debt, UI Investissement, Alantra, Windcliff, Foxstone, Edmond de Rothschild REIM), finance corporate (Chanel, Dior/LVMH, Danone, Vinci), banque réseau/corporate (BNP chargé d'affaires entrepreneurs, La Banque Postale financements structurés, HSBC analyse crédit).

## Annexe B — Fichiers, liens K2, méthode

- Fichiers importés à la racine : `Finance (1) (2).pdf` · `Finance (2) (1).pdf` · `SKEMA Professional Missions DATABASE 2021 to 2025_UPDATED 092025 (1).xlsx` (depuis la branche `arena/789b026a-skema-front`).
- Shortlist générée : `candidatures/K2-SHORTLIST-DB-SKEMA-2026-10-17.csv` (442 lignes ; filtres : Tier 1 = intitulé FX strict Europe 2023+ ; Tier 2 = broker/sales-trader en Finance de marché 2023+ ; Tier 3 = sales/structurés/dérivés FM 2023+ ; géographies FR/Lux/BE/NL/DE/IE/UK/CH/Monaco/ES/PT).
- Liens K2 cités (authentification SKEMA requise) : base missions `k2.skema.edu/mod/resource/view.php?id=1267628` · cours CV `k2.skema.edu/mod/url/view.php?id=1267622` · GoinGlobal : accès direct depuis la page K2 (lien à identifiant, non reproduit ici).
- Limites de l'analyse : intitulés libres (orthographe variable, ex. 3 libellés pour CACIB) ; entreprises parfois vides (31 lignes FM) ; nationalités inconnues à 48 % ; dates = début de mission ; la base reflète les stages déclarés à SKEMA, pas l'emploi des diplômés à 2–3 ans. Aucune offre « live » n'est affirmée sans vérification du 17/10 (Convera/Marex : voir notes §3–4) ; le reste est de la veille à refaire au moment de candidater.
- Croisements repo : `candidatures/CIBLE-CDI-FX-runbook-2026-09-26.md` (addendum du 17/10 ajouté) · `candidatures/TRACKING-CANDIDATURES-2026-2027.md` (addendum du 17/10 ajouté) · statuts au 30/09 à rafraîchir par Calvin.

*MAJ 17/10/2026 — exploitation K2 + base missions SKEMA 2021-2025 (39 824 lignes lues) + 2 PDF parcours types Finance (46 pages).*
