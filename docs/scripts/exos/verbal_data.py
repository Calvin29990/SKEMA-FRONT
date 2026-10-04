"""10 textes × 6 affirmations = 60 items de raisonnement verbal (Vrai / Faux / On ne peut pas dire).

Chaque affirmation porte son piège : c'est lui qu'il faut mémoriser.
"""

PASSAGES = [
    ("Nordex Logistics",
     "Nordex Logistics was founded in Rotterdam in 1998 and employs 1,400 people. In 2024 the company "
     "reported revenue of €310 million, 6% higher than in 2023. It operates twelve warehouses in the "
     "Benelux region and has run a fleet of 220 electric trucks since 2023. Anke Vermeer has been Chief "
     "Executive since 2021. The board kept the dividend at the same level as the previous year.",
     [
         ("Nordex operates warehouses outside the Benelux region.", "F",
          "le texte ne mentionne que douze entrepôts **dans** le Benelux → contraire direct."),
         ("Revenue increased by €18 million in 2024.", "CS",
          "on connaît le CA 2024 et la hausse de 6 %, mais **pas le montant 2023 en euros** → pas de chiffre affirmé."),
         ("Anke Vermeer has led the company since 2021.", "T",
          "reformulation exacte de « Chief Executive since 2021 »."),
         ("The entire fleet is electric.", "T",
          "« a fleet of 220 electric trucks » = toute la flotte est électrique."),
         ("The dividend was increased in 2024.", "F",
          "« kept the dividend at the same level » = inchangé → faux."),
         ("Nordex has always had its head office in Rotterdam.", "CS",
          "fondée à Rotterdam ≠ siège **toujours** à Rotterdam : l'info manque."),
     ]),
    ("Halvard Bank stress test",
     "In March 2025 the European Banking Authority published the results of its stress test covering "
     "seventy banks. Halvard Bank's common equity tier 1 ratio fell from 14.2% to 11.8% under the "
     "adverse scenario, remaining above the 8% regulatory minimum. Three of the seventy banks fell below "
     "the minimum. The Authority does not publish a ranking of the banks and the results are not used to "
     "set individual capital requirements.",
     [
         ("Halvard Bank remained above the regulatory minimum in the adverse scenario.", "T",
          "11,8 % > 8 % : c'est écrit (« remaining above »)."),
         ("Halvard Bank was among the three weakest banks tested.", "CS",
          "aucun **classement** n'est publié : on ne peut pas le situer."),
         ("The stress test covered more than sixty banks.", "T",
          "soixante-dix > soixante : inférence directe sur un nombre écrit."),
         ("The results are used to set capital requirements for each bank.", "F",
          "le texte dit explicitement le contraire (« are not used to set »)."),
         ("Halvard Bank's ratio fell by 2.4 percentage points.", "T",
          "14,2 − 11,8 = 2,4 : calcul direct sur deux chiffres **donnés** (autorisé)."),
         ("The European Banking Authority publishes the results every year.", "CS",
          "une seule publication (mars 2025) est mentionnée : la fréquence n'est pas indiquée."),
     ]),
    ("Mirel pharmaceuticals",
     "Mirel Pharmaceuticals announced that its arthritis treatment, currently in phase III trials, will "
     "not reach the market before 2028. Research spending rose to 19% of revenue in 2024, the highest "
     "level in the company's history. Two rival firms have abandoned similar programmes. Mirel employs "
     "6,200 people, of whom 1,100 work in research.",
     [
         ("The arthritis treatment is already on sale.", "F",
          "il n'arrivera pas avant 2028 → faux."),
         ("Research spending as a share of revenue has never been higher at Mirel.", "T",
          "« the highest level in the company's history » = reformulation."),
         ("About one employee in six works in research.", "CS",
          "1 100 / 6 200 ≈ 1 sur 5,6 : le texte donne les chiffres mais **pas la proportion**, et « environ un sur six » est une estimation non affirmée."),
         ("Two competitors stopped comparable research programmes.", "T",
          "reformulation de « abandoned similar programmes »."),
         ("Mirel's revenue increased in 2024.", "CS",
          "on connaît le **pourcentage** (19 %), pas l'évolution du chiffre d'affaires."),
         ("The treatment will be launched in 2028.", "CS",
          "« not before 2028 » ≠ « en 2028 » : la date exacte n'est pas donnée."),
     ]),
    ("Verano energy contracts",
     "Verano Energy has signed fifteen-year supply contracts with four industrial customers in Spain and "
     "Portugal. The contracts cover 40% of Verano's planned output from its new solar parks, which are "
     "scheduled to start operating in 2027. The remaining output has not been sold. Verano's share price "
     "rose 7% on the day of the announcement.",
     [
         ("All of Verano's planned output has been sold.", "F",
          "40 % seulement : « the remaining output has not been sold »."),
         ("The contracts run for fifteen years.", "T",
          "chiffre écrit."),
         ("The solar parks began operating in 2027.", "CS",
          "ils sont **prévus** pour 2027 ; rien ne dit qu'ils ont démarré."),
         ("Verano's customers are all Spanish.", "F",
          "quatre clients **en Espagne et au Portugal** → pas tous espagnols."),
         ("The share price rose on the announcement day.", "T",
          "+7 % le jour de l'annonce."),
         ("The 7% rise was caused by the announcement.", "CS",
          "corrélation de date ≠ **causalité** affirmée : classique « On ne peut pas dire »."),
     ]),
    ("Briq retail restructuring",
     "Retailer Briq will close thirty-one of its 240 stores by the end of 2026 and convert twelve sites "
     "into collection points. The company expects the plan to save €45 million a year once completed. "
     "Restructuring charges of €60 million will be booked in 2025. Briq will not reduce staff numbers "
     "below 8,000.",
     [
         ("More than ten per cent of Briq's stores will close.", "F",
          "31 / 240 ≈ 12,9 % : c'est **plus** de 10 % → l'affirmation est fausse."),
         ("Twelve sites will become collection points.", "T",
          "chiffre écrit."),
         ("The savings of €45 million were achieved in 2025.", "CS",
          "les économies sont **attendues** une fois le plan achevé ; aucune réalisation en 2025 n'est indiquée."),
         ("Restructuring charges will be recognised in 2025.", "T",
          "« will be booked in 2025 »."),
         ("Briq will keep at least 8,000 employees.", "T",
          "« will not reduce staff numbers below 8,000 »."),
         ("Briq's turnover will fall after the closures.", "CS",
          "aucun chiffre de chiffre d'affaires n'est donné : effet inconnu."),
     ]),
    ("Caldwell fund performance",
     "The Caldwell Global Fund returned 9.4% in 2024, against 6.1% for its benchmark index. Over five "
     "years the fund returned an average of 5.8% a year, below the benchmark's 6.9%. The fund charges an "
     "annual fee of 1.2% and does not pay a performance fee. Assets under management reached €2.1 billion "
     "at the end of 2024.",
     [
         ("The fund beat its benchmark in 2024.", "T",
          "9,4 % > 6,1 %."),
         ("The fund beat its benchmark over five years.", "F",
          "5,8 % < 6,9 % : surperformé sur un an, **sous**-performé sur cinq ans."),
         ("The fund charges a performance fee.", "F",
          "« does not pay a performance fee »."),
         ("The annual fee is more than one per cent.", "T",
          "1,2 % > 1 % : comparaison directe sur un chiffre écrit."),
         ("Assets under management grew during 2024.", "CS",
          "seul le niveau de fin 2024 est donné : pas de comparaison avec le début d'année."),
         ("The fund's five-year return was positive.", "T",
          "5,8 % par an en moyenne = positif."),
     ]),
    ("Sarnia shipping regulation",
     "From 1 January 2026 ships calling at Sarnian ports must report their emissions. The rule applies to "
     "vessels above 5,000 gross tonnes and excludes fishing vessels. Operators that fail to report face "
     "fines of up to €250,000 per voyage. The Sarnian Maritime Authority will publish the data annually "
     "but will not name individual operators without their consent.",
     [
         ("All vessels calling at Sarnian ports must report emissions.", "F",
          "seulement **au-dessus de 5 000 tonneaux** et hors bateaux de pêche."),
         ("Fishing vessels are excluded from the rule.", "T",
          "écrit explicitement."),
         ("The maximum fine is €250,000 per voyage.", "T",
          "« up to €250,000 per voyage »."),
         ("Every operator's data will be made public each year.", "F",
          "publication **sans nommer** les opérateurs sans leur accord."),
         ("The rule came into force before 2026.", "F",
          "entrée en vigueur au 1er janvier 2026."),
         ("Fines have already been issued under this rule.", "CS",
          "rien sur d'éventuelles sanctions déjà prononcées."),
     ]),
    ("Ostren manufacturing automation",
     "Ostren has automated two of its seven production lines, raising output per hour by 12% on those "
     "lines. Total factory output rose 3% in 2024. The company spent €18 million on the project, funded "
     "from cash reserves rather than borrowing. Ostren plans to automate a third line in 2026 if the "
     "current investment pays back within four years.",
     [
         ("Most of Ostren's production lines are automated.", "F",
          "2 lignes sur 7 = minorité."),
         ("Output per hour rose 12% across the whole factory.", "F",
          "+12 % **sur les deux lignes** seulement ; +3 % au total."),
         ("The project was financed by debt.", "F",
          "« from cash reserves rather than borrowing »."),
         ("A third line will definitely be automated in 2026.", "CS",
          "c'est **conditionnel** (« if the investment pays back ») : rien n'est certain."),
         ("Total output increased in 2024.", "T",
          "+3 % : chiffre écrit."),
         ("The €18 million investment has already paid back.", "CS",
          "le remboursement est une **condition future**, aucun résultat n'est indiqué."),
     ]),
    ("Pellam insurance claims",
     "Pellam Mutual received 41,000 claims in 2024, 4% fewer than in 2023. Average settlement time fell "
     "from nineteen days to sixteen. The company paid out €612 million in total, of which €180 million "
     "related to weather damage. Pellam does not disclose the number of claims it rejected.",
     [
         ("The number of claims fell in 2024.", "T",
          "−4 % par rapport à 2023."),
         ("Claims were settled faster in 2024 than in 2023.", "T",
          "19 → 16 jours."),
         ("Weather damage accounted for about a third of the amount paid.", "T",
          "180 / 612 ≈ 29,4 % : calcul direct sur deux chiffres **donnés** (≈ un tiers)."),
         ("Pellam rejected fewer claims in 2024 than in 2023.", "CS",
          "les rejets ne sont **pas divulgués**."),
         ("The total paid out exceeded €600 million.", "T",
          "612 > 600."),
         ("Most claims were related to weather damage.", "F",
          "180 M€ sur 612 M€ = minorité (et c'est un montant, pas un nombre de dossiers)."),
     ]),
    ("Trevane public takeover",
     "Trevane Holdings launched a cash offer of €42 per share for Kessel Media, valuing the company at "
     "€1.3 billion. Kessel's board recommends that shareholders reject the offer, calling it too low. "
     "Trevane holds 12% of Kessel's shares and needs more than 50% for the offer to succeed. The offer "
     "closes on 30 November unless extended.",
     [
         ("Kessel's board supports the offer.", "F",
          "elle recommande de **rejeter** l'offre."),
         ("Trevane already owns more than half of Kessel.", "F",
          "12 % seulement."),
         ("The offer values Kessel at €1.3 billion.", "T",
          "chiffre écrit."),
         ("The offer is made in shares rather than cash.", "F",
          "« a cash offer »."),
         ("The offer will definitely close on 30 November.", "CS",
          "« unless extended » : une prolongation est possible."),
         ("Trevane's offer is €42 for each Kessel share.", "T",
          "reformulation exacte."),
     ]),
]
