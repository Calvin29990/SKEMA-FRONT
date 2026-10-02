/* ═══════════════════════════════════════════════════════════════
   banks.js — Banques d'items FIXES (réplique de forme)
   Contenu : Verbal reasoning (EN) · Déductif · Comportement pro ·
             Motivation · Raisonnement mécanique
   ⚠ Toutes les banques de ce fichier sont "limitées" : contenu
     stable, identique à chaque session, aucune régénération.
   ═══════════════════════════════════════════════════════════════ */
'use strict';

const BANK = (() => {

  /* ══════════════════ 1. VERBAL REASONING (anglais) ══════════════════
     Format cut-e/SHL : un passage, 3 affirmations, Vrai / Faux / Impossible à dire.
     Règle stricte : on ne répond QUE sur la base du passage.
     « True »  = l'affirmation découle du texte.
     « False » = l'affirmation contredit le texte.
     « Cannot say » = le texte ne permet pas de trancher (info absente). */
  const T = 'true', F = 'false', CS = 'cannot say';

  const verbal = [
    {
      id: 'V01', theme: 'Corporate banking',
      passage: 'Meridian Bank reported that its corporate lending division grew its loan book by 9% in 2025, driven mainly by mid-sized manufacturers in northern Europe. The bank stated that demand for long-term credit facilities remained steady, but that many clients were increasingly requesting sustainability-linked covenants. Meridian expects the division to grow more slowly in 2026 because several large facilities will mature in the first half of the year.',
      q: [
        { s: 'Meridian Bank lends to mid-sized manufacturers.', a: T, w: 'Le texte précise que la croissance du portefeuille est portée principalement par les fabricants de taille moyenne.' },
        { s: 'Meridian Bank is the largest corporate lender in Europe.', a: CS, w: 'Aucune comparaison avec d’autres banques n’est faite.' },
        { s: 'Meridian Bank expects its corporate lending division to shrink in 2026.', a: F, w: 'Le texte annonce une croissance plus lente, pas une contraction.' }
      ]
    },
    {
      id: 'V02', theme: 'Market structure',
      passage: 'The share of European equity trading executed on exchanges declined last year, while trading on multilateral trading facilities and systematic internalisers increased. Regulators noted that this shift has made consolidated market data harder to assemble and more expensive. Market participants have argued that the fragmentation improves execution speed, although they acknowledge that the total cost of trading has not fallen for all investor categories.',
      q: [
        { s: 'Trading on multilateral trading facilities increased last year.', a: T, w: 'Stated explicitly.' },
        { s: 'Fragmentation has reduced the total cost of trading for all investors.', a: F, w: 'Le texte dit explicitement que le coût total n’a pas baissé pour toutes les catégories.' },
        { s: 'Regulators consider fragmented trading to be harmful overall.', a: CS, w: 'Ils constatent une difficulté technique sur les données ; aucun jugement global n’est donné.' }
      ]
    },
    {
      id: 'V03', theme: 'Central banks',
      passage: 'The central bank left its policy rate unchanged for the third consecutive meeting, citing persistent service-sector inflation. Two members of the committee voted for an increase. The governor stated that future decisions would depend on wage data and on the pace of disinflation, and declined to give any indication about the timing of a first cut.',
      q: [
        { s: 'The decision to hold rates was unanimous.', a: F, w: 'Deux membres ont voté pour une hausse.' },
        { s: 'The governor indicated when the first rate cut might occur.', a: F, w: 'Il a refusé de donner toute indication de calendrier.' },
        { s: 'Wage data will influence future decisions.', a: T, w: 'Le gouverneur le dit explicitement.' }
      ]
    },
    {
      id: 'V04', theme: 'Private equity',
      passage: 'A private equity fund closed its fifth vehicle at €4.1 billion, exceeding its €3.5 billion target. The fund focuses on healthcare and software businesses in Western Europe. Its previous fund delivered a gross multiple of 2.3x. The fund manager said that exit conditions had improved, but that entry valuations remained demanding, particularly for software assets.',
      q: [
        { s: 'The fund exceeded its fundraising target.', a: T, w: '4,1 Md€ > 3,5 Md€.' },
        { s: 'The previous fund returned a net multiple of 2.3x.', a: CS, w: 'Le multiple de 2,3x est indiqué comme BRUT ; le net n’est pas donné.' },
        { s: 'The fund invests mainly in industrial businesses.', a: F, w: 'Le texte parle de santé et de logiciels.' }
      ]
    },
    {
      id: 'V05', theme: 'FX',
      passage: 'The euro weakened against the dollar after the release of weaker-than-expected industrial production figures. Analysts attributed part of the move to position unwinding ahead of the year-end. Options market pricing suggested that investors were paying more for protection against further euro weakness, although realised volatility remained below its five-year average.',
      q: [
        { s: 'Industrial production figures were weaker than expected.', a: T, w: 'Stated explicitly.' },
        { s: 'Realised volatility was above its five-year average.', a: F, w: 'Le texte dit « below ».' },
        { s: 'The euro weakened against all major currencies.', a: CS, w: 'Seul le dollar est mentionné.' }
      ]
    },
    {
      id: 'V06', theme: 'ESG regulation',
      passage: 'The new disclosure standard requires asset managers to report the proportion of portfolio companies with validated emissions targets. Smaller managers have complained about the administrative burden, and the regulator has granted a two-year transition period for firms managing less than €5 billion. The standard applies to equity and corporate bond portfolios alike.',
      q: [
        { s: 'Smaller managers will have more time to comply.', a: T, w: 'Période transitoire de deux ans sous 5 Md€.' },
        { s: 'The standard applies only to equity portfolios.', a: F, w: 'Elle couvre aussi les obligations d’entreprise.' },
        { s: 'The regulator expects the administrative burden to raise fund fees.', a: CS, w: 'Aucune mention des frais.' }
      ]
    },
    {
      id: 'V07', theme: 'Fixed income',
      passage: 'The issuer priced a ten-year bond at a spread of 135 basis points over the reference rate, 15 basis points tighter than initial guidance. The order book reached €6 billion, allowing the issuer to increase the deal size from €750 million to €1 billion. The bonds were allocated predominantly to asset managers, with banks receiving a smaller share than in the previous transaction.',
      q: [
        { s: 'The final spread was tighter than the initial guidance.', a: T, w: '135 bp contre 150 bp de guidance initiale.' },
        { s: 'The order book was oversubscribed.', a: T, w: '6 Md€ de demandes pour 1 Md€ émis.' },
        { s: 'Banks received a larger allocation than in the previous transaction.', a: F, w: 'Le texte indique une part plus faible.' }
      ]
    },
    {
      id: 'V08', theme: 'Technology & trading',
      passage: 'A trading venue announced that it would reduce its latency by migrating to a new data centre. The migration will occur over a weekend to limit disruption, and members will be required to certify their connectivity before the change. The venue said that fees would remain unchanged for at least twelve months.',
      q: [
        { s: 'Members must certify connectivity before the migration.', a: T, w: 'Stated explicitly.' },
        { s: 'The migration will take place during a trading day.', a: F, w: 'Elle aura lieu un week-end.' },
        { s: 'The venue will attract more members after the migration.', a: CS, w: 'Aucune projection sur le nombre de membres.' }
      ]
    },
    {
      id: 'V09', theme: 'Equity research',
      passage: 'The analyst upgraded the stock to buy, arguing that the company’s free cash flow would cover its dividend even under a moderate demand slowdown. The target price was raised by 12%. The analyst noted that the balance sheet remains leveraged relative to peers, and that a further deterioration in demand would require a reassessment of the recommendation.',
      q: [
        { s: 'The analyst believes free cash flow covers the dividend in a moderate slowdown.', a: T, w: 'Argument central de la note.' },
        { s: 'The company has lower leverage than its peers.', a: F, w: 'Le texte dit l’inverse.' },
        { s: 'The target price increase was based on a higher valuation multiple.', a: CS, w: 'La méthode n’est pas donnée.' }
      ]
    },
    {
      id: 'V10', theme: 'Corporate finance',
      passage: 'The board approved a share buyback of up to 4% of share capital over eighteen months. Management stated that the programme would be executed only if the share price remained below the board’s estimate of intrinsic value. The company also confirmed that its dividend policy was unchanged, targeting a payout ratio between 40% and 50% of net income.',
      q: [
        { s: 'The buyback has a maximum size of 4% of share capital.', a: T, w: 'Stated explicitly ("up to 4%").' },
        { s: 'The company will pay out at least 50% of net income as dividends.', a: F, w: 'La fourchette va de 40% à 50%.' },
        { s: 'The board believes the shares are currently undervalued.', a: CS, w: 'La condition porte sur l’exécution future, pas sur l’avis actuel.' }
      ]
    },
    {
      id: 'V11', theme: 'Operations',
      passage: 'The settlement team reduced its failed trades by a third after introducing automated matching. The head of operations said the reduction had freed capacity for client onboarding, a process that had previously been delayed by manual reconciliation. She added that further automation would require investment in data quality rather than in new software.',
      q: [
        { s: 'Automated matching contributed to fewer failed trades.', a: T, w: 'Réduction d’un tiers après l’introduction de l’appariement automatisé.' },
        { s: 'Client onboarding had previously been delayed by manual reconciliation.', a: T, w: 'Explicitement indiqué.' },
        { s: 'The team plans to buy new software next year.', a: CS, w: 'Le texte dit que l’investissement nécessaire porterait sur la qualité des données, pas sur un plan d’achat.' }
      ]
    },
    {
      id: 'V12', theme: 'Risk management',
      passage: 'The bank reported a fall in its value-at-risk measure, which it attributed to lower market volatility rather than to a change in portfolio composition. The risk committee nonetheless asked for a stress test incorporating a sharp widening of credit spreads. The bank stated that its capital ratio remained above its target range.',
      q: [
        { s: 'The fall in value-at-risk was caused by changes in the portfolio.', a: F, w: 'Le texte attribue la baisse à la volatilité.' },
        { s: 'The capital ratio was above the target range.', a: T, w: 'Stated explicitly.' },
        { s: 'The stress test will show that the bank would pass.', a: CS, w: 'Aucun résultat n’est donné.' }
      ]
    }
  ];

  /* ══════════════════ 2. DÉDUCTIF — séries de figures ══════════════════
     Format cut-e "deductive reasoning" (matrices) : on applique les règles
     d'une grille logique 3x3 pour trouver la figure manquante.          */
  const DED = [
    { id: 'D01', size: 3, rule: 'Chaque ligne contient trois formes différentes ; chaque colonne contient trois couleurs différentes.',
      grid: [['circle', 'square', 'triangle'], ['square', 'triangle', 'circle'], ['triangle', 'circle', '??']],
      colors: [['grn', 'amb', 'red'], ['amb', 'red', 'grn'], ['red', 'grn', '??']],
      opts: [{ shape: 'square', color: 'grn' }, { shape: 'circle', color: 'red' }, { shape: 'triangle', color: 'blu' }], ans: 0 },
    { id: 'D02', size: 3, rule: 'La forme tourne d’un cran vers la droite à chaque case ; la couleur alterne par ligne.',
      grid: [['dot', 'square', 'tri'], ['square', 'tri', 'dot'], ['tri', 'dot', '??']],
      colors: [['blu', 'pur', 'teal'], ['pur', 'teal', 'blu'], ['teal', 'blu', '??']],
      opts: [{ shape: 'square', color: 'pur' }, { shape: 'tri', color: 'blu' }, { shape: 'dot', color: 'red' }], ans: 0 },
    { id: 'D03', size: 3, rule: 'Le nombre de points augmente de 1 par colonne ; la teinte reste identique dans chaque ligne.',
      grid: [['d1', 'd2', 'd3'], ['d2', 'd3', 'd1'], ['d3', 'd1', '??']],
      colors: [['amb', 'amb', 'amb'], ['grn', 'grn', 'grn'], ['red', 'red', 'red']],
      opts: [{ shape: 'd2', color: 'red' }, { shape: 'd1', color: 'red' }, { shape: 'd3', color: 'grn' }], ans: 0 },
    { id: 'D04', size: 3, rule: 'La rotation d’un quart de tour est appliquée à chaque déplacement horizontal ; la forme est identique sur toute la diagonale.',
      grid: [['arr-r', 'arr-d', 'arr-l'], ['arr-d', 'arr-l', 'arr-r'], ['arr-l', 'arr-r', '??']],
      colors: [['grn', 'grn', 'grn'], ['grn', 'grn', 'grn'], ['grn', 'grn', 'grn']],
      opts: [{ shape: 'arr-d', color: 'grn' }, { shape: 'arr-u', color: 'grn' }, { shape: 'arr-l', color: 'grn' }], ans: 0 },
    { id: 'D05', size: 3, rule: 'Deux attributs varient indépendamment : le remplissage (plein/vide) et le contour (simple/double). Chaque combinaison apparaît une fois par ligne.',
      grid: [['full', 'empty', 'full2'], ['empty', 'full2', 'full'], ['full2', 'full', '??']],
      colors: [['pur', 'pur', 'pur'], ['blu', 'blu', 'blu'], ['teal', 'teal', 'teal']],
      opts: [{ shape: 'empty', color: 'teal' }, { shape: 'full', color: 'teal' }, { shape: 'full2', color: 'pur' }], ans: 0 },
    { id: 'D06', size: 2, rule: 'La figure du bas est la figure du haut privée de son attribut le plus à droite ; le sens de lecture est conservé.',
      grid: [['gp', 'gm'], ['gh', '??']],
      colors: [['amb', 'amb'], ['amb', 'amb']],
      opts: [{ shape: 'gm', color: 'amb' }, { shape: 'gp', color: 'amb' }, { shape: 'gh', color: 'red' }], ans: 0 },
    { id: 'D07', size: 3, rule: 'Le symbole se déplace dans le sens des aiguilles d’une montre autour de la grille ; la forme change à chaque ligne en respectant l’ordre cercle → carré → triangle.',
      grid: [['c-tl', 's-t', 't-tr'], ['t-r', 'c-br', 's-b'], ['s-bl', 't-l', '??']],
      colors: [['grn', 'grn', 'grn'], ['grn', 'grn', 'grn'], ['grn', 'grn', 'grn']],
      opts: [{ shape: 'c-br', color: 'grn' }, { shape: 's-br', color: 'grn' }, { shape: 't-br', color: 'grn' }], ans: 0 },
    { id: 'D08', size: 3, rule: 'Chaque colonne respecte : la couleur de fond décroît d’un cran vers la droite (vert > ambre > rouge) et le trait s’épaissit.',
      grid: [['thin', 'mid', 'thick'], ['mid', 'thick', 'thin'], ['thick', 'thin', '??']],
      colors: [['grn', 'amb', 'red'], ['amb', 'red', 'grn'], ['red', 'grn', '??']],
      opts: [{ shape: 'mid', color: 'amb' }, { shape: 'thin', color: 'amb' }, { shape: 'thick', color: 'red' }], ans: 0 },
    { id: 'D09', size: 3, rule: 'La moitié pleine tourne d’un quart de tour vers la gauche à chaque colonne ; le contour reste identique.',
      grid: [['ht', 'hl', 'hb'], ['hl', 'hb', 'ht'], ['hb', 'ht', '??']],
      colors: [['blu', 'blu', 'blu'], ['blu', 'blu', 'blu'], ['blu', 'blu', 'blu']],
      opts: [{ shape: 'hl', color: 'blu' }, { shape: 'ht', color: 'blu' }, { shape: 'hb', color: 'blu' }], ans: 0 },
    { id: 'D10', size: 3, rule: 'Règle "XOR" : une case contient l’élément présent dans exactement une des deux cases de la ligne précédente (jamais dans les deux).',
      grid: [['a', 'b', 'ab'], ['b', 'ab', 'a'], ['ab', 'a', '??']],
      colors: [['pur', 'pur', 'pur'], ['pur', 'pur', 'pur'], ['pur', 'pur', 'pur']],
      opts: [{ shape: 'b', color: 'pur' }, { shape: 'ab', color: 'pur' }, { shape: 'a', color: 'pur' }], ans: 0 },
    { id: 'D11', size: 3, rule: 'La figure applique une symétrie horizontale puis verticale en alternance, en partant du coin supérieur gauche.',
      grid: [['fl', 'fr', 'fl'], ['fr', 'fl', 'fr'], ['fl', 'fr', '??']],
      colors: [['teal', 'teal', 'teal'], ['teal', 'teal', 'teal'], ['teal', 'teal', 'teal']],
      opts: [{ shape: 'fl', color: 'teal' }, { shape: 'fr', color: 'teal' }, { shape: 'f2', color: 'teal' }], ans: 0 },
    { id: 'D12', size: 2, rule: 'La progression est hexagonale : chaque case hérite du contour de la case supérieure et du remplissage de la case de gauche.',
      grid: [['h1', 'h2'], ['h3', '??']],
      colors: [['amb', 'amb'], ['amb', 'amb']],
      opts: [{ shape: 'h4', color: 'amb' }, { shape: 'h1', color: 'amb' }, { shape: 'h2', color: 'amb' }], ans: 0 }
  ];

  /* ══════════════════ 3. COMPORTEMENT PRO (work behaviour) ══════════════════
     Format cut-e "scales" : affirmation + fréquence. Aucune bonne réponse —
     l'objectif est la cohérence (c'est ce que l'école appelle l'aspect
     "inconfortable" : pas de solution unique, il faut se positionner vite). */
  const WB_SCALE = ['Presque jamais', 'Parfois', 'Souvent', 'Presque toujours'];
  const workBehaviour = [
    'Je tiens mes engagements même lorsque le délai devient très serré.',
    'Je remets en question une méthode de travail qui produit des erreurs répétées.',
    'Je demande un retour précis plutôt qu’un avis général.',
    'Je continue une tâche fastidieuse jusqu’à ce qu’elle soit terminée.',
    'Je préfère décider avec une information incomplète que d’attendre.',
    'Je signale une erreur que j’ai commise avant que quelqu’un d’autre ne la découvre.',
    'Je m’adapte quand les priorités changent au milieu de la semaine.',
    'Je critique une idée sans viser la personne qui l’a proposée.',
    'Je prends en charge une tâche qui n’entre pas strictement dans mon périmètre.',
    'Je maintiens le même niveau de qualité sur une longue série de tâches répétitives.',
    'Je cherche à comprendre la finalité d’une demande avant de l’exécuter.',
    'Je préfère être évalué sur des résultats mesurables.',
    'Je reste efficace lorsque plusieurs personnes me sollicitent en même temps.',
    'Je suis à l’aise lorsque je dois présenter un travail à des personnes plus expérimentées.',
    'Je reconnais rapidement lorsqu’une piste est mauvaise et j’en change.',
    'Je relis systématiquement un livrable avant de l’envoyer.',
    'Je m’organise pour ne pas dépendre de la dernière minute.',
    'Je préfère une consigne écrite à une consigne orale.',
    'Je reste calme lorsqu’un interlocuteur conteste mon travail.',
    'J’apprends d’un retour négatif plutôt que de le contester.',
    'Je demande de l’aide quand je bloque depuis plus de trente minutes.',
    'Je tiens compte des contraintes des autres équipes dans mes délais.',
    'Je vérifie mes chiffres par une seconde méthode de calcul.',
    'Je préfère travailler sur un sujet nouveau plutôt que sur un sujet déjà maîtrisé.',
    'Je respecte un processus établi même si je le trouve perfectible.',
    'Je propose un changement après avoir prouvé qu’il fonctionne.',
    'Je m’engage sur un objectif ambitieux même sans garantie de réussite.',
    'Je priorise ce qui a le plus d’impact plutôt que ce qui est le plus urgent.',
    'Je m’impose une méthode de suivi pour ne rien oublier.',
    'Je m’assure que mon travail peut être repris par quelqu’un d’autre.',
    'Je préfère un environnement compétitif à un environnement très collaboratif.',
    'Je reste concentré lorsque mon téléphone reçoit des notifications.',
    'Je sais dire non à une demande incompatible avec mes délais.',
    'Je prépare mes arguments avant une discussion difficile.',
    'J’accepte un retour critique en public si cela fait gagner du temps.',
    'Je m’intéresse aux détails qui n’ont d’importance qu’en cas de contrôle.'
  ];

  /* ══════════════════ 4. MOTIVATION & INTÉRÊTS ══════════════════ */
  const MOT_SCALE = ['Pas du tout', 'Un peu', 'Assez', 'Beaucoup'];
  const motivation = [
    'Travailler sur des marchés financiers réactifs au quart d’heure.',
    'Construire une expertise reconnue dans une seule classe d’actifs.',
    'Côtoyer des clients de grande taille et négocier avec eux.',
    'Produire un travail dont le résultat se mesure chaque jour.',
    'Évoluer dans un environnement où le classement est explicite.',
    'Passer une partie de ma carrière à l’étranger.',
    'Résoudre des problèmes quantitatifs complexes.',
    'Avoir une rémunération fortement liée à la performance.',
    'Rédiger des analyses écrites longues et argumentées.',
    'Diriger une équipe dans un délai court.',
    'Apprendre un métier technique auprès d’un senior exigeant.',
    'Travailler sous pression avec des délais non négociables.',
    'Prendre des décisions risquées avec un impact financier direct.',
    'Approfondir la réglementation et les normes comptables.',
    'Développer des outils informatiques pour automatiser des tâches répétitives.',
    'Exercer un métier où l’erreur se paie immédiatement.',
    'Passer des certifications professionnelles pendant mon temps libre.',
    'M’exprimer en anglais la majorité de ma journée de travail.',
    'Avoir une visibilité directe sur les décisions de la direction.',
    'Travailler dans une entreprise de petite taille à forte croissance.',
    'Mener de front un travail et un projet académique exigeant.',
    'Être évalué sur ma capacité à convaincre plutôt que sur mon analyse.',
    'Faire du chiffre un usage quotidien, sans calculatrice.',
    'Assumer une responsabilité commerciale (objectifs de revenus).',
    'Passer plusieurs années dans la même entreprise.',
    'Faire des présentations régulières devant des décideurs.',
    'Me spécialiser dans la gestion des risques plutôt que dans la vente.',
    'Travailler sur des opérations longues, en équipe projet.',
    'Avoir un manager qui corrige mon travail en détail.',
    'Rejoindre une structure où la formation se fait sur le terrain.'
  ];

  /* ══════════════════ 5. RAISONNEMENT MÉCANIQUE ══════════════════
     Format cut-e "mechanical": engrenages, leviers, axes, ressorts, poulies.
     Chaque item possède un dessin (scene) rendu en SVG paramétrique. */
  const mech = [
    { id: 'M01', scene: 'gears2', q: 'La roue A tourne dans le sens des aiguilles d’une montre. Dans quel sens tourne la roue B ?',
      opts: ['aiguilles d’une montre', 'sens inverse', 'elle ne tourne pas'], ans: 1,
      why: 'Deux roues en contact direct tournent en sens opposés.' },
    { id: 'M02', scene: 'gears3', q: 'La roue A tourne dans le sens inverse des aiguilles d’une montre. La roue C tourne…',
      opts: ['comme A (sens inverse)', 'sens des aiguilles', 'sens alterné'], ans: 0,
      why: 'Avec un nombre impair de roues en série, la dernière tourne dans le même sens que la première.' },
    { id: 'M03', scene: 'gears4', q: 'Quatre roues en chaîne : A, B, C, D. Si A tourne dans le sens des aiguilles, D tourne…',
      opts: ['sens des aiguilles', 'sens inverse', 'impossible à déterminer'], ans: 1,
      why: 'Avec un nombre pair de roues, la dernière tourne en sens opposé à la première.' },
    { id: 'M04', scene: 'belt', q: 'Une courroie droite relie deux poulies. Si la poulie A tourne dans le sens inverse des aiguilles d’une montre, la poulie B tourne…',
      opts: ['dans le même sens que A', 'en sens opposé à A', 'elle est immobile'], ans: 0,
      why: 'Une courroie droite (non croisée) transmet le mouvement dans le MÊME sens aux deux poulies.' },
    { id: 'M05', scene: 'beltcross', q: 'Une courroie croisée relie deux poulies. Les deux poulies tournent…',
      opts: ['dans le même sens', 'en sens opposés', 'par intermittence'], ans: 1,
      why: 'Le croisement fait croiser les brins : les deux poulies tournent en sens OPPOSÉS.' },
    { id: 'M06', scene: 'lever', q: 'Un levier avec la charge à 20 cm du pivot et la force appliquée à 80 cm. Quel effort minimal faut-il pour soulever une charge de 100 kg (levier sans frottement) ?',
      opts: ['25 kg', '50 kg', '400 kg', '80 kg'], ans: 0,
      why: 'F × 80 = 100 × 20 → F = 25 kg.' },
    { id: 'M07', scene: 'lever', q: 'Charge de 60 kg à 30 cm du pivot. Force appliquée à 60 cm. Effort nécessaire ?',
      opts: ['30 kg', '60 kg', '15 kg', '120 kg'], ans: 0,
      why: 'F × 60 = 60 × 30 → F = 30 kg.' },
    { id: 'M08', scene: 'pulley1', q: 'Une poulie fixe simple. Pour soulever une charge de 80 kg, l’effort théorique à fournir est…',
      opts: ['80 kg', '40 kg', '160 kg', '0 kg'], ans: 0,
      why: 'Une poulie fixe ne réduit pas l’effort : elle change seulement la direction.' },
    { id: 'M09', scene: 'pulley2', q: 'Un palan à deux brins mobiles. Effort théorique pour une charge de 80 kg ?',
      opts: ['20 kg', '40 kg', '80 kg', '160 kg'], ans: 1,
      why: 'Deux brins porteurs divisent l’effort par 2 : 40 kg.' },
    { id: 'M10', scene: 'pulley3', q: 'Un palan à trois brins porteurs. Charge de 90 kg. Effort théorique ?',
      opts: ['45 kg', '30 kg', '90 kg', '15 kg'], ans: 1,
      why: 'Effort = charge / nombre de brins = 90 / 3 = 30 kg.' },
    { id: 'M11', scene: 'spring', q: 'Un ressort s’allonge de 4 cm sous 8 kg. Que vaut son allongement sous 12 kg (loi de Hooke) ?',
      opts: ['6 cm', '8 cm', '3 cm', '12 cm'], ans: 0,
      why: 'Allongement proportionnel : 4 × (12/8) = 6 cm.' },
    { id: 'M12', scene: 'axle', q: 'Une roue de 40 cm de diamètre est montée sur le même axe qu’une roue de 10 cm. La grande roue fait 1 tour. Combien de tours fait la petite ?',
      opts: ['1 tour', '2 tours', '4 tours', '0,25 tour'], ans: 0, why: 'Même axe : les deux roues font exactement le même nombre de tours.' },
    { id: 'M13', scene: 'gears2size', q: 'Deux roues dentées en contact : la petite a 10 dents, la grande 30 dents. Si la petite fait 3 tours, la grande fait…',
      opts: ['1 tour', '3 tours', '9 tours', '0,33 tour'], ans: 0,
      why: '10 × 3 = 30 × n → n = 1 tour.' },
    { id: 'M14', scene: 'gears2size', q: 'Rapport 10 dents / 40 dents. La grande fait 2 tours, la petite fait…',
      opts: ['8 tours', '2 tours', '4 tours', '0,5 tour'], ans: 0,
      why: '40 × 2 = 10 × n → n = 8 tours.' },
    { id: 'M15', scene: 'gears4', q: 'Sur une chaîne de 4 roues de même diamètre, si la roue 1 fait 12 tours, la roue 4 fait…',
      opts: ['12 tours', '3 tours', '48 tours', '6 tours'], ans: 0,
      why: 'Roues en contact : la vitesse est transmise à l’identique (seul le sens change).' },
    { id: 'M16', scene: 'lever', q: 'Charge de 150 kg à 10 cm du pivot, force à 150 cm. Effort nécessaire ?',
      opts: ['10 kg', '15 kg', '100 kg', '1,5 kg'], ans: 0,
      why: 'F × 150 = 150 × 10 → F = 10 kg.' },
    { id: 'M17', scene: 'spring', q: 'Un ressort de raideur k = 20 kg/cm. Allongement sous 100 kg ?',
      opts: ['5 cm', '20 cm', '2 cm', '50 cm'], ans: 0,
      why: 'x = F / k = 100 / 20 = 5 cm.' },
    { id: 'M18', scene: 'pulley2', q: 'Palan à deux brins, charge 120 kg. Effort théorique ?',
      opts: ['60 kg', '120 kg', '240 kg', '30 kg'], ans: 0,
      why: '120 / 2 = 60 kg.' },
    { id: 'M19', scene: 'gears3', q: 'Trois roues en chaîne. La roue A tourne dans le sens des aiguilles d’une montre. La roue C…',
      opts: ['sens des aiguilles', 'sens inverse', 'elle est bloquée'], ans: 0,
      why: 'Nombre impair de roues → même sens que A.' },
    { id: 'M20', scene: 'axle', q: 'Deux roues sur le même axe : grand diamètre 60 cm, petit 20 cm. Une marque sur la grande fait 1 tour ; la marque sur la petite fait…',
      opts: ['1 tour', '3 tours', '1/3 de tour', '9 tours'], ans: 0,
      why: 'Même axe → même vitesse angulaire.' },
    { id: 'M21', scene: 'beltcross', q: 'Courroie croisée : la poulie A tourne dans le sens des aiguilles d’une montre. La poulie B tourne…',
      opts: ['dans le sens des aiguilles', 'dans le sens inverse', 'alternativement dans les deux sens'], ans: 1,
      why: 'Courroie croisée → sens opposés. A horaire ⇒ B antihoraire.' },
    { id: 'M22', scene: 'gears2size', q: 'Engrenage 12 dents / 36 dents. La roue de 12 dents fait 6 tours. La roue de 36 dents fait…',
      opts: ['2 tours', '3 tours', '18 tours', '0,5 tour'], ans: 0,
      why: '12 × 6 = 36 × n → n = 2 tours.' },
    { id: 'M23', scene: 'lever', q: 'Charge 90 kg à 40 cm du pivot, force à 120 cm. Effort nécessaire ?',
      opts: ['30 kg', '45 kg', '60 kg', '270 kg'], ans: 0,
      why: 'F × 120 = 90 × 40 → F = 30 kg.' },
    { id: 'M24', scene: 'pulley3', q: 'Palan à 3 brins, effet de levier optimal. Pour soulever 300 kg, l’effort théorique minimal est…',
      opts: ['150 kg', '100 kg', '300 kg', '75 kg'], ans: 1,
      why: '300 / 3 = 100 kg.' }
  ];

  /* ══════════════════ 6. TRAITEMENT DE L'INFORMATION (Shannon) ══════════════════
     Format cut-e "information handling" / Shannon : minimiser le coût
     d'acquisition d'une information sûre dans une chaîne logique.       */
  const info = [
    { id: 'I01', q: 'Un coffre contient deux sommes : soit 20 000 € (p = 0,8), soit 0 € (p = 0,2). Combien payez-vous au maximum pour connaître le contenu du coffre ?',
      opts: ['16 000 €', '20 000 €', '13 300 €', '4 000 €'], ans: 0,
      why: 'Valeur de l’information parfaite = 0,8 × 20 000 = 16 000 €.' },
    { id: 'I02', q: 'Un projet rapporte 12 000 € avec une probabilité de 0,25, sinon 0 €. Une information fiable coûte 3 500 €. Que faites-vous ?',
      opts: ['J’achète l’information', 'Je n’achète pas l’information', 'Indifférent, coût = espérance'], ans: 1,
      why: 'Valeur de l’information = 0,25 × 12 000 = 3 000 € < 3 500 € : refus. Piège classique.' },
    { id: 'I03', q: 'Bénéfice espéré sans information : 6 000 €. Avec information parfaite : 9 000 €. La valeur de l’information est…',
      opts: ['3 000 €', '9 000 €', '6 000 €', '15 000 €'], ans: 0,
      why: 'VI = espérance avec information − espérance sans = 9 000 − 6 000 = 3 000 €.' },
    { id: 'I04', q: 'On vous propose une loterie : 10 000 € avec p = 0,4 ; 0 € sinon. Prix de participation : 3 000 €. Que faites-vous ?',
      opts: ['Je participe', 'Je refuse', 'Indifférent'], ans: 0,
      why: 'Espérance = 4 000 € > 3 000 € : participer est rentable.' },
    { id: 'I05', q: 'Trois sources donnent des informations indépendantes dont la fiabilité est 1/2 chacune. Fiabilité de la majorité des trois ?',
      opts: ['1/2', '3/4', '1/8', '2/3'], ans: 0,
      why: 'Probabilité de majorité exacte sur 3 pièces équilibrées = 1/2 (toutes combinaisons de parité).' },
    { id: 'I06', q: 'Combien de questions binaires faut-il au minimum pour identifier une carte parmi 52 (sans réponse préalable) ?',
      opts: ['6', '5', '52', '9'], ans: 0,
      why: 'log₂(52) ≈ 5,7 → 6 questions (borne supérieure entière).' },
    { id: 'I07', q: 'Un test coûte 8 000 € et révèle une information qui augmente le gain espéré de 5 000 €. Décision ?',
      opts: ['Acheter le test', 'Ne pas acheter', 'Acheter seulement si le gain dépasse 10 000 €'], ans: 1,
      why: 'Coût > valeur de l’information : refus.' },
    { id: 'I08', q: 'Espérance sans info : 1 500 €. Info parfaite : 4 000 € avec certitude. Prix maximal acceptable ?',
      opts: ['2 500 €', '4 000 €', '1 500 €', '5 500 €'], ans: 0,
      why: 'VI = 4 000 − 1 500 = 2 500 €.' },
    { id: 'I09', q: 'Deux options : (A) 5 000 € sûrs ; (B) 12 000 € avec p = 0,5. Laquelle choisit un décideur neutre au risque ?',
      opts: ['A', 'B', 'Indifférent'], ans: 1,
      why: 'Espérance B = 6 000 € > 5 000 €.' },
    { id: 'I10', q: 'Un rapport acheté 2 000 € a une probabilité 0,3 de faire gagner 10 000 € et 0,7 de ne rien changer. Décision rationnelle ?',
      opts: ['Acheter', 'Ne pas acheter', 'Acheter si le rapport est certifié'], ans: 0,
      why: 'Espérance du gain = 3 000 € > 2 000 €.' },
    { id: 'I11', q: 'Quatre urnes, une seule contient un jeton. On peut poser des questions binaires. Nombre minimal de questions ?',
      opts: ['4', '2', '3', '1'], ans: 1,
      why: 'log₂(4) = 2 questions suffisent.' },
    { id: 'I12', q: 'Une source est fiable à 90%. Deux sources indépendantes donnent le même signal. Probabilité que le signal soit correct (règle de la majorité exacte) ?',
      opts: ['0,90', '0,99', '0,81', '0,95'], ans: 1,
      why: 'Les deux sources concordent : P = 0,9² / (0,9² + 0,1²) = 0,81/0,82 ≈ 0,988 → 0,99.' },
    { id: 'I13', q: 'Coût d’une information : 1 000 €. Elle permet d’éviter une perte de 6 000 € dans 20% des cas. Faut-il l’acheter ?',
      opts: ['Oui', 'Non', 'Oui seulement si la perte survient'], ans: 0,
      why: 'Gain espéré = 0,2 × 6 000 = 1 200 € > 1 000 € : oui, de justesse.' },
    { id: 'I14', q: 'On peut payer 500 € pour savoir laquelle de 8 hypothèses est vraie ; chaque hypothèse a le même gain espéré de 600 € mais une seule est correcte. Décision ?',
      opts: ['Payer', 'Ne pas payer', 'Payer si la probabilité dépasse 50%'], ans: 1,
      why: 'Probabilité 1/8, gain espéré 75 € < 500 €.' },
    { id: 'I15', q: 'Probabilité de succès d’un projet : 0,2. Gain en cas de succès : 50 000 €. Valeur du projet ?',
      opts: ['10 000 €', '50 000 €', '2 500 €', '40 000 €'], ans: 0,
      why: '0,2 × 50 000 = 10 000 €.' },
    { id: 'I16', q: 'Un test parfait coûte X et transforme une espérance de 7 000 € en 11 000 €. X maximal acceptable ?',
      opts: ['4 000 €', '11 000 €', '7 000 €', '18 000 €'], ans: 0,
      why: 'X ≤ VI = 4 000 €.' },
    { id: 'I17', q: 'Interrogé, un expert se trompe 1 fois sur 5. Deux experts indépendants donnent des réponses différentes. Lequel croire ?',
      opts: ['Le premier', 'Le second', 'Les deux hypothèses sont équiprobables'], ans: 2,
      why: 'Les deux experts étant symétriques et indépendants, aucune règle ne permet de trancher : les deux hypothèses restent équiprobables.' },
    { id: 'I18', q: 'Une information permet de choisir entre deux projets (espérances 4 000 € et 9 000 €, équiprobables). Valeur de l’information ?',
      opts: ['2 500 €', '6 500 €', '5 000 €', '9 000 €'], ans: 0,
      why: 'Avec info : 9 000 € ; sans info : 6 500 € (espérance). VI = 2 500 €.' }
  ];

  return { verbal, DED, workBehaviour, WB_SCALE, motivation, MOT_SCALE, mech, info };
})();
