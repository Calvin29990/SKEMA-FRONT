/* ═══════════════════════════════════════════════════════════════
   banks.js — contenus d'entraînement (écrits pour l'entraînement,
   dans le style des épreuves, sans reproduire le contenu des tests
   réels) + textes d'introduction FR/EN conformes aux captures.
   Assessment Trainer — Calvin MINANG — usage personnel.
   ═══════════════════════════════════════════════════════════════ */
'use strict';

const BANK = (() => {

  /* ─────────── Palettes de symboles, par épreuve (captures) ─────────── */
  const SYM_DED = [                       /* déductif : carré rouge, rond vert, triangle bleu, croix bleu clair */
    { kind: 'square-full', color: '#e02b20' },
    { kind: 'disc',        color: '#7ab800' },
    { kind: 'tri-full',    color: '#145da0' },
    { kind: 'plus',        color: '#29abe2' }
  ];
  const SYM_IND = [                       /* inductif : rond violet, carré vert, triangle bleu, croix rouge */
    { kind: 'disc',        color: '#a12a9e' },
    { kind: 'square-full', color: '#5a9e32' },
    { kind: 'tri-full',    color: '#145da0' },
    { kind: 'plus',        color: '#c0272d' }
  ];
  const SYM_SW = [                        /* switch : triangle jaune, croix bleu clair, rond vert, carré rouge */
    { kind: 'tri-full',    color: '#fbb03b' },
    { kind: 'plus',        color: '#29abe2' },
    { kind: 'disc',        color: '#7ab800' },
    { kind: 'square-full', color: '#e02b20' }
  ];

  /* ─────────── VERBAL — 6 fiches de textes, 49 affirmations ─────────── */
  const verbalSheets = [
    { id: 'structure', name: 'GROUPE', html:
      '<b>Group structure.</b><p>Halden &amp; Roe plc is a United Kingdom consumer goods group headquartered in Leeds and listed on the London stock exchange. The group is organised into three divisions: Home Care, Personal Care and Foods. Each division operates through wholly owned subsidiaries in its main markets, while the holding company retains finance, legal and internal audit functions at group level.</p>' +
      '<p>Shareholdings. The group holds a 100% interest in eleven subsidiaries and a majority interest (between 51% and 90%) in four further companies, all of which are fully consolidated. Three associated companies, in which the group holds between 20% and 49%, are accounted for under the equity method. Minority interests are presented separately in the consolidated balance sheet.</p>' },
    { id: 'strategy', name: 'STRATÉGIE', html:
      '<b>Strategy.</b><p>The group concentrates on branded products in the middle and upper price segments. Growth is pursued both organically and through selective acquisitions of regional brands with a loyal customer base. Between the reporting years the group acquired two personal care brands in southern Europe and divested its low-margin private label activities in Foods.</p>' +
      '<p>Cost discipline. Shared services for procurement, logistics and IT were centralised in two service centres. The group states that restructuring reduced overheads by roughly one eighth over two years, while marketing investment was maintained at around nine per cent of revenue.</p>' },
    { id: 'principles', name: 'PRINCIPES', html:
      '<b>Principles.</b><p>Halden &amp; Roe commits to responsible sourcing: key raw materials must be traceable to certified suppliers by the end of the planning period. The group publishes an annual sustainability report reviewed by the audit committee.</p>' +
      '<p>People. The group operates a single grade structure across divisions and states that internal vacancies are advertised group-wide for at least two weeks before external recruitment begins. Training days per employee averaged 2.4 in the reporting year.</p>' },
    { id: 'products', name: 'PRODUITS', html:
      '<b>Products &amp; Services.</b><p>Home Care comprises cleaning preparations, laundry powders and air care, sold under four brands. Personal Care comprises hair colourants, skin care and oral care, sold under six brands, including the acquired colourant brand "Corline". Foods comprises breakfast cereals and cereal bars under three brands.</p>' +
      '<p>Service income. The group also licenses its formulations to two third-party manufacturers outside Europe; licence income is reported within the division that owns the formulation.</p>' },
    { id: 'locations', name: 'IMPLANTATIONS', html:
      '<b>Locations.</b><p>Production takes place at nine plants: four in the United Kingdom, two in continental Europe, two in North America and one in Australia. The two service centres are located in Manchester and Gdansk. The group sells in 34 countries but owns no production site in Asia or in South America.</p>' +
      '<p>Distribution. In the United Kingdom the group distributes through its own depot network; in all other markets it uses independent distributors, with the exception of North America where a joint venture handles logistics.</p>' },
    { id: 'board', name: 'DIRECTION', html:
      '<b>Executive Board.</b><p>The executive board comprises five members: the chief executive, the chief financial officer, and three divisional chief executives (Home Care, Personal Care, Foods). The chairman of the supervisory board is not a member of the executive board.</p>' +
      '<p>Committees. The audit committee has three members, all non-executive. The remuneration committee has four members, of whom one is a member of the executive board; this exception was approved by the supervisory board for a transitional period.</p>' }
  ];
  const verbal = [
    { sh: 'structure', s: 'The group holds a majority interest in more than ten companies that are fully consolidated.', a: 0, w: 'Eleven wholly owned plus four majority subsidiaries = fifteen fully consolidated companies.' },
    { sh: 'structure', s: 'Associated companies are fully consolidated in the group accounts.', a: 1, w: 'Associates (20–49%) are accounted for under the equity method, not fully consolidated.' },
    { sh: 'structure', s: 'The internal audit function is located at group level.', a: 0, w: 'The holding company retains finance, legal and internal audit.' },
    { sh: 'structure', s: 'Minority interests are included within group equity without separate presentation.', a: 1, w: 'The sheet states minority interests are presented separately.' },
    { sh: 'structure', s: 'The group employs more people in the UK than abroad.', a: 2, w: 'No headcount by country is given.' },
    { sh: 'structure', s: 'Halden & Roe is listed on a stock exchange outside the United Kingdom.', a: 1, w: 'It is listed on the London stock exchange.' },
    { sh: 'structure', s: 'Every subsidiary in which the group holds over 50% is fully consolidated.', a: 0, w: 'Majority interests (51–90%) are fully consolidated, as are wholly owned ones.' },
    { sh: 'structure', s: 'The group has exactly three associated companies.', a: 0, w: 'Three associated companies are stated.' },
    { sh: 'strategy', s: 'The group sold off its private label activities in Foods.', a: 0, w: 'The divestment of low-margin private label activities in Foods is stated.' },
    { sh: 'strategy', s: 'Overhead costs fell by about 12.5% over two years.', a: 0, w: 'A reduction of roughly one eighth equals about 12.5%.' },
    { sh: 'strategy', s: 'Marketing investment was cut to fund the restructuring.', a: 1, w: 'Marketing investment was maintained at around nine per cent of revenue.' },
    { sh: 'strategy', s: 'The two acquired personal care brands were profitable at acquisition.', a: 2, w: 'No profitability figure for the acquired brands is given.' },
    { sh: 'strategy', s: 'Growth relies exclusively on acquisitions.', a: 1, w: 'Growth is pursued organically and through selective acquisitions.' },
    { sh: 'strategy', s: 'Shared services were centralised in two centres.', a: 0, w: 'Procurement, logistics and IT were centralised in two service centres.' },
    { sh: 'strategy', s: 'The group targets only the luxury segment.', a: 1, w: 'It concentrates on the middle and upper price segments.' },
    { sh: 'strategy', s: 'The restructuring lasted exactly two years.', a: 2, w: 'The effect is measured over two years; the duration of the programme is not stated.' },
    { sh: 'principles', s: 'Key raw materials must be traceable to certified suppliers by the end of the planning period.', a: 0, w: 'Stated commitment.' },
    { sh: 'principles', s: 'The sustainability report is reviewed by the audit committee.', a: 0, w: 'Stated in the sheet.' },
    { sh: 'principles', s: 'External candidates are always considered before internal ones.', a: 1, w: 'Internal vacancies are advertised group-wide for at least two weeks first.' },
    { sh: 'principles', s: 'Employees received on average more than two training days in the reporting year.', a: 0, w: '2.4 days on average.' },
    { sh: 'principles', s: 'The grade structure differs between divisions.', a: 1, w: 'A single grade structure operates across divisions.' },
    { sh: 'principles', s: 'Suppliers are audited on site every year.', a: 2, w: 'Certification is required; on-site audit frequency is not stated.' },
    { sh: 'principles', s: 'The sustainability report is published every two years.', a: 2, w: 'It is annual; no two-year cycle is mentioned.' },
    { sh: 'principles', s: 'The audit committee reviews a report on sustainability.', a: 0, w: 'Same fact as the review of the annual sustainability report.' },
    { sh: 'products', s: 'The group sells more Personal Care brands than Home Care brands.', a: 0, w: 'Six personal care brands versus four home care brands.' },
    { sh: 'products', s: 'Licence income is reported in a separate division.', a: 1, w: 'Licence income is reported within the division owning the formulation.' },
    { sh: 'products', s: 'The colourant brand "Corline" was acquired rather than created internally.', a: 0, w: 'Described as the acquired colourant brand.' },
    { sh: 'products', s: 'Foods comprises exactly three brands.', a: 0, w: 'Breakfast cereals and cereal bars under three brands.' },
    { sh: 'products', s: 'Air care products generate more revenue than laundry powders.', a: 2, w: 'No revenue split within Home Care is given.' },
    { sh: 'products', s: 'The group licenses formulations to manufacturers located in Europe.', a: 1, w: 'Licensees are stated to be outside Europe.' },
    { sh: 'products', s: 'Oral care belongs to the Personal Care division.', a: 0, w: 'Listed under Personal Care.' },
    { sh: 'products', s: 'Cereal bars are sold under the same brands as breakfast cereals.', a: 2, w: 'Both are within Foods’ three brands, but brand-level overlap is not specified.' },
    { sh: 'locations', s: 'The group operates production sites on four continents.', a: 1, w: 'Sites lie in Europe (UK + continental), North America and Australia: three continents.' },
    { sh: 'locations', s: 'The group owns a production site in Asia.', a: 1, w: 'No production site in Asia or South America.' },
    { sh: 'locations', s: 'Distribution in the United Kingdom uses the group’s own depots.', a: 0, w: 'Stated.' },
    { sh: 'locations', s: 'Logistics in North America are handled by a joint venture.', a: 0, w: 'Stated exception.' },
    { sh: 'locations', s: 'The group sells in more than thirty countries.', a: 0, w: '34 countries.' },
    { sh: 'locations', s: 'Both service centres are located in the United Kingdom.', a: 1, w: 'Manchester (UK) and Gdansk (Poland, continental Europe).' },
    { sh: 'locations', s: 'The Australian plant exports to Asian markets.', a: 2, w: 'No export flows are described.' },
    { sh: 'locations', s: 'Independent distributors are used in every market outside the United Kingdom.', a: 1, w: 'North America is an exception (joint venture).' },
    { sh: 'locations', s: 'The group has nine production plants in total.', a: 0, w: '4+2+2+1 = 9.' },
    { sh: 'board', s: 'The executive board has five members.', a: 0, w: 'Stated.' },
    { sh: 'board', s: 'The chairman of the supervisory board sits on the executive board.', a: 1, w: 'Explicitly not a member.' },
    { sh: 'board', s: 'All members of the audit committee are non-executive.', a: 0, w: 'Stated.' },
    { sh: 'board', s: 'The remuneration committee is composed exclusively of non-executive members.', a: 1, w: 'One member is an executive board member (transitional exception).' },
    { sh: 'board', s: 'Each division has a chief executive on the executive board.', a: 0, w: 'Three divisional chief executives are members.' },
    { sh: 'board', s: 'The remuneration committee has more members than the audit committee.', a: 0, w: 'Four versus three.' },
    { sh: 'board', s: 'The transitional exception for the remuneration committee will end next year.', a: 2, w: 'No end date is given.' },
    { sh: 'board', s: 'The chief financial officer is a member of the executive board.', a: 0, w: 'Listed among the five members.' }
  ].map((x, i) => Object.assign({ id: 'V' + (i + 1) }, x));

  /* ─────────── LANGUES — anglais ─────────── */
  const enFluency = [
    { s: 'The board _____ the proposal after a lengthy discussion.', o: ['adopted', 'adapted', 'adjusted', 'admitted'], a: 0, w: 'To adopt a proposal = to approve it.' },
    { s: 'Sales have _____ steadily over the last four quarters.', o: ['risen', 'raised', 'aroused', 'lifted'], a: 0, w: 'Rise is intransitive; raise requires an object.' },
    { s: 'She is _____ charge of the client onboarding process.', o: ['in', 'on', 'at', 'for'], a: 0, w: 'Fixed phrase: in charge of.' },
    { s: 'The contract was signed _____ behalf of both parties.', o: ['on', 'in', 'by', 'at'], a: 0, w: 'Fixed phrase: on behalf of.' },
    { s: 'We regret to inform you that the delivery will be _____.', o: ['delayed', 'postponed off', 'detained', 'expired'], a: 0, w: 'A delivery is delayed.' },
    { s: 'His figures do not add _____; please check them again.', o: ['up', 'on', 'in', 'out'], a: 0, w: 'Add up = to be consistent.' },
    { s: 'The committee turned _____ the request for extra funding.', o: ['down', 'off', 'out', 'over'], a: 0, w: 'Turn down = to refuse.' },
    { s: 'Please _____ the attached documents to your application.', o: ['enclose', 'include up', 'attach with', 'insert to'], a: 0, w: 'Enclose/attach + object; only “enclose” fits the pattern.' },
    { s: 'The merger is _____ to be completed by June.', o: ['due', 'bound about', 'meant for', 'set out'], a: 0, w: 'Due to = scheduled.' },
    { s: 'Management takes _____ of every complaint received.', o: ['note', 'notice of', 'mark', 'count'], a: 0, w: 'Fixed phrase: take note of.' },
    { s: 'The new rules come _____ force next month.', o: ['into', 'in', 'to', 'under'], a: 0, w: 'Come into force.' },
    { s: 'He has little experience _____ negotiating with suppliers.', o: ['in', 'of', 'about', 'for'], a: 0, w: 'Experience in + -ing.' },
    { s: 'The report highlights a significant _____ in operating costs.', o: ['rise', 'raise', 'rising', 'risen'], a: 0, w: 'A noun is required: a rise.' },
    { s: 'Unless the invoice is paid _____ time, interest will apply.', o: ['on', 'in', 'at', 'by'], a: 0, w: 'On time = within the deadline.' }
  ];
  const enVocab = [
    { s: 'to postpone; to put off to a later date', o: ['defer', 'infer', 'confer', 'prefer'], a: 0, w: 'Defer = postpone.' },
    { s: 'careful attention to detail; thoroughness', o: ['meticulousness', 'haste', 'negligence', 'apathy'], a: 0, w: 'Meticulousness = thorough care.' },
    { s: 'to make a problem or a pain less severe', o: ['alleviate', 'aggravate', 'elevate', 'allocate'], a: 0, w: 'Alleviate = lessen.' },
    { s: 'abundant; more than sufficient in quantity', o: ['ample', 'scarce', 'meagre', 'finite'], a: 0, w: 'Ample = abundant.' },
    { s: 'to waver between two opinions or courses of action', o: ['vacillate', 'assert', 'commit', 'persist'], a: 0, w: 'Vacillate = waver.' },
    { s: 'clearly expressed; easy to understand', o: ['lucid', 'obscure', 'cryptic', 'muddled'], a: 0, w: 'Lucid = clear.' },
    { s: 'happening every year; recurring once a year', o: ['annual', 'biennial', 'perennial', 'manual'], a: 0, w: 'Annual = yearly.' },
    { s: 'to examine something carefully in order to assess it', o: ['scrutinise', 'ignore', 'discard', 'overlook'], a: 0, w: 'Scrutinise = examine closely.' },
    { s: 'unwilling to spend money; stingy', o: ['miserly', 'lavish', 'generous', 'open-handed'], a: 0, w: 'Miserly = stingy.' },
    { s: 'the quality of being honest and having strong morals', o: ['integrity', 'hostility', 'scarcity', 'opacity'], a: 0, w: 'Integrity.' },
    { s: 'to give permission for something to happen', o: ['authorise', 'forbid', 'refuse', 'withhold'], a: 0, w: 'Authorise = permit.' },
    { s: 'brief and concise, using few words', o: ['succinct', 'verbose', 'lengthy', 'rambling'], a: 0, w: 'Succinct = brief.' },
    { s: 'to rise again after a decline; to recover', o: ['rebound', 'relapse', 'recede', 'refract'], a: 0, w: 'Rebound = recover.' },
    { s: 'suitable or appropriate for a particular purpose', o: ['apt', 'inept', 'alien', 'adverse'], a: 0, w: 'Apt = suitable.' }
  ];
  const enSpell = [
    { o: ['necessary', 'neccessary'], a: 0 }, { o: ['occurrence', 'ocurrence'], a: 0 },
    { o: ['committee', 'comittee'], a: 0 },   { o: ['separate', 'seperate'], a: 0 },
    { o: ['maintenance', 'maintainance'], a: 0 }, { o: ['judgment', 'judgementt'], a: 0 },
    { o: ['acquaint', 'aquaint'], a: 0 },     { o: ['privilege', 'priviledge'], a: 0 },
    { o: ['threshold', 'threshhold'], a: 0 }, { o: ['conscientious', 'concientious'], a: 0 }
  ];

  /* ─────────── LANGUES — français ─────────── */
  const frFluency = [
    { s: 'On ne peut plus attendre : c’est _____ qu’il faut agir.', o: ['maintenant', 'demain', 'tôt', 'présent'], a: 0, w: '« Maintenant » marque l’urgence présente.' },
    { s: 'Le comité a _____ la demande de budget complémentaire.', o: ['rejeté', 'repoussé de', 'refusé à', 'écarté sur'], a: 0, w: 'Rejeter une demande.' },
    { s: 'Les ventes ont _____ de 8 % sur un an.', o: ['augmenté', 'amélioré', 'accru (s’)', 'haussé'], a: 0, w: 'Augmenter, verbe intransitif.' },
    { s: 'Ce dossier relève _____ la direction financière.', o: ['de', 'du', 'sous', 'par'], a: 0, w: 'Relever de.' },
    { s: 'Veuillez _____ les justificatifs à votre demande.', o: ['joindre', 'joindre avec', 'attacher à', 'ajouter avec'], a: 0, w: 'Joindre quelque chose à.' },
    { s: 'La réunion est reportée _____ une date ultérieure.', o: ['à', 'sur', 'en', 'pour de'], a: 0, w: 'Reporter à.' },
    { s: 'Il s’est abstenu _____ commenter les rumeurs.', o: ['de', 'à', 'pour', 'd’y'], a: 0, w: 'S’abstenir de.' },
    { s: 'Les résultats sont _____ cours de consolidation.', o: ['en', 'au', 'sous', 'par'], a: 0, w: 'En cours de.' },
    { s: 'Cette clause s’applique _____ effet immédiat.', o: ['avec', 'à', 'dès à', 'en'], a: 0, w: 'Avec effet immédiat.' },
    { s: 'Le rapport met en _____ plusieurs risques majeurs.', o: ['évidence', 'avant', 'garde', 'oeuvre'], a: 0, w: 'Mettre en évidence.' },
    { s: 'Nous donnons _____ à votre demande de délai.', o: ['suite', 'suite de', 'suit', 'suivi'], a: 0, w: 'Donner suite à.' },
    { s: 'Les équipes travaillent _____ étroite collaboration.', o: ['en', 'avec', 'sous', 'par'], a: 0, w: 'En étroite collaboration.' },
    { s: 'Ce dispositif vise à pallier _____ difficultés de trésorerie.', o: ['les', 'aux', 'des aux', 'à les'], a: 0, w: 'Pallier quelque chose (transitif direct).' },
    { s: 'La direction a tranché _____ faveur du projet pilote.', o: ['en', 'à', 'de', 'sous'], a: 0, w: 'Trancher en faveur de.' }
  ];
  const frVocab = [
    { s: 'qui survient chaque année ; annuel', o: ['récurrent', 'annuel', 'périodique', 'séculaire'], a: 1, w: 'Annuel = chaque année.' },
    { s: 'attention minutieuse aux détails', o: ['rigueur', 'hâte', 'négligence', 'désinvolture'], a: 0, w: 'Rigueur / minutie.' },
    { s: 'reporter à plus tard ; différer', o: ['ajourner', 'avancer', 'hâter', 'devancer'], a: 0, w: 'Ajourner = reporter.' },
    { s: 'qui manque d’ampleur ; insuffisant en quantité', o: ['exigu', 'ample', 'copieux', 'large'], a: 0, w: 'Exigu = trop petit.' },
    { s: ' examiner avec une attention minutieuse', o: ['scruter', 'ignorer', 'écarter', 'survoler'], a: 0, w: 'Scruter = examiner attentivement.' },
    { s: 'qui se dit avec peu de mots ; concis', o: ['succinct', 'verbeux', 'prolixe', 'fleuve'], a: 0, w: 'Succinct.' },
    { s: 'attachement aux principes moraux ; honnêteté', o: ['probité', 'hostilité', 'rareté', 'opacité'], a: 0, w: 'Probité = intégrité.' },
    { s: 'donner le pouvoir ou la permission de faire', o: ['habiliter', 'interdire', 'refuser', 'retenir'], a: 0, w: 'Habiliter = autoriser.' },
    { s: 'qui hésite entre deux partis ; flottant', o: ['vacillant', 'assuré', 'résolu', 'ferme'], a: 0, w: 'Vacillant.' },
    { s: 'rendre un mal ou une peine moins pénible', o: ['atténuer', 'aggraver', 'accroître', 'exacerber'], a: 0, w: 'Atténuer.' },
    { s: 'ensemble des règles qui régissent un domaine', o: ['cadre', 'hors-cadre', 'écart', 'marge'], a: 0, w: 'Cadre normatif.' },
    { s: 'qui se produit tous les deux ans', o: ['bisannuel', 'annuel', 'semestriel', 'bisextile'], a: 0, w: 'Bisannuel / biennal.' },
    { s: 'remonter après un déclin ; rebondir', o: ['reboundir', 'rechuter', 'reculer', 'régresser'], a: 0, w: 'Rebondir.' },
    { s: 'convenable ; approprié à l’usage', o: ['adéquat', 'inepte', 'étranger', 'contraire'], a: 0, w: 'Adéquat.' }
  ];
  const frSpell = [
    { o: ['développement', 'dévelopement'], a: 0 }, { o: ['occasion', 'occassion'], a: 0 },
    { o: ['apparemment', 'aparemment'], a: 0 },     { o: ['maintenance', 'maintainance'], a: 0 },
    { o: ['privilège', 'privilége'], a: 0 },        { o: ['consciencieux', 'concentieux'], a: 0 },
    { o: ['rythme', 'rhythme'], a: 0 },             { o: ['transmettre', 'transmetre'], a: 0 },
    { o: ['acquérir', 'acquérirre'], a: 0 },        { o: ['palette', 'pallette'], a: 0 }
  ];

  /* ─────────── LANGUES — réserves « jamais à court » ───────────
     Les banques ci-dessus couvrent le premier passage (items des captures).
     Les réserves suivantes prennent le relais : phrases supplémentaires
     écrites pour l'entraînement, paires mot/définition, et listes
     d'orthographe à partir desquelles le générateur fabrique des items
     supplémentaires (questions similaires) sans jamais s'épuiser. */

  const enFluencyExtra = [
    { s: 'The supplier failed to _____ with the agreed delivery schedule.', o: ['comply', 'apply', 'abide', 'conform'], a: 0, w: 'Comply with = respecter (abide by, conform to, apply to).' },
    { s: 'The analyst _____ down the figures before the meeting.', o: ['broke', 'cut', 'tore', 'split'], a: 0, w: 'Break down = décomposer.' },
    { s: 'The board decided to _____ the launch until the audit was complete.', o: ['defer', 'differ', 'infer', 'refer'], a: 0, w: 'Defer = reporter ; differ = être différent.' },
    { s: 'Management must _____ for the delay in the reporting process.', o: ['account', 'count', 'discount', 'recount'], a: 0, w: 'Account for = expliquer, répondre de.' },
    { s: 'The new system will _____ into effect on the first of March.', o: ['come', 'get', 'take', 'make'], a: 0, w: 'Come into effect = entrer en vigueur.' },
    { s: 'The team had to _____ with an unexpected rise in demand.', o: ['cope', 'deal', 'handle', 'manage'], a: 0, w: 'Cope with = faire face à.' },
    { s: 'The proposal was turned _____ because the budget was already committed.', o: ['down', 'off', 'out', 'up'], a: 0, w: 'Turn down = refuser.' },
    { s: 'Please _____ your expense claims before the end of the quarter.', o: ['submit', 'subsist', 'submerge', 'subscribe'], a: 0, w: 'Submit a claim = déposer une demande.' },
    { s: 'The manager was held _____ for the error in the report.', o: ['responsible', 'responsive', 'responsorial', 'responsibly'], a: 0, w: 'Held responsible for = tenu responsable de.' },
    { s: 'The two departments must work _____ close cooperation.', o: ['in', 'on', 'at', 'by'], a: 0, w: 'In close cooperation.' },
    { s: 'The figures are _____ line with the forecast.', o: ['in', 'on', 'at', 'by'], a: 0, w: 'In line with = conformément à.' },
    { s: 'The contract is _____ to renewal every three years.', o: ['subject', 'subjective', 'subjected', 'subjection'], a: 0, w: 'Be subject to = être soumis à.' },
    { s: 'Revenue rose _____ 4% in the second half.', o: ['by', 'of', 'from', 'to'], a: 0, w: 'Rise by + écart ; rise to + niveau atteint.' },
    { s: 'The audit committee will look _____ the matter at its next meeting.', o: ['into', 'after', 'for', 'up'], a: 0, w: 'Look into = examiner.' },
    { s: 'Please keep me _____ of any change in the schedule.', o: ['informed', 'informative', 'informing', 'information'], a: 0, w: 'Keep someone informed of.' },
    { s: 'The company had to _____ its losses on the project.', o: ['absorb', 'absolve', 'absorbed', 'absorbing'], a: 0, w: 'Absorb losses = absorber des pertes.' },
    { s: 'The report was _____ to the board last Friday.', o: ['submitted', 'subjected', 'subscribed', 'subsumed'], a: 0, w: 'Submit a report to.' },
    { s: 'We should aim to _____ the deadline rather than extend it.', o: ['meet', 'reach to', 'touch', 'attend'], a: 0, w: 'Meet a deadline.' },
    { s: 'The board must _____ by the end of the month.', o: ['decide', 'decide on', 'decision', 'decisive'], a: 0, w: 'Decide = verbe intransitif ici.' },
    { s: 'The figures were prepared _____ a tight deadline.', o: ['under', 'below', 'beneath', 'underneath'], a: 0, w: 'Under a deadline.' },
    { s: 'The supplier has agreed to _____ the order within ten days.', o: ['fulfil', 'full fill', 'fulfil with', 'fulfilment'], a: 0, w: 'Fulfil an order.' },
    { s: 'She has been _____ charge of the project since January.', o: ['in', 'on', 'at', 'with'], a: 0, w: 'In charge of.' },
    { s: 'The costs were _____ higher than expected.', o: ['considerably', 'considerate', 'consideration', 'considering'], a: 0, w: 'Adverbe de degré : considerably.' },
    { s: 'The teams will _____ the results at the end of the quarter.', o: ['review', 'revise up', 'revision', 'reviewing'], a: 0, w: 'Review = examiner.' }
  ];
  const enVocabExtra = [
    { s: 'to reduce costs or spending', o: ['retrench', 'entrench', 'entrance', 'trench'], a: 0, w: 'Retrench = réduire les dépenses.' },
    { s: 'a temporary decline in economic activity', o: ['downturn', 'downgrade', 'downfall', 'downpour'], a: 0, w: 'Downturn = ralentissement.' },
    { s: 'to describe something as smaller than it really is', o: ['understate', 'overstate', 'misstate', 'restate'], a: 0, w: 'Understate = minimiser.' },
    { s: 'goods sent out of a country', o: ['exports', 'imports', 'excise', 'exodus'], a: 0, w: 'Exports.' },
    { s: 'the amount by which spending exceeds income', o: ['deficit', 'debt', 'surplus', 'default'], a: 0, w: 'Deficit = déficit.' },
    { s: 'to officially forbid something', o: ['prohibit', 'permit', 'expedite', 'remit'], a: 0, w: 'Prohibit = interdire.' },
    { s: 'a person who owes money', o: ['debtor', 'creditor', 'broker', 'auditor'], a: 0, w: 'Debtor = débiteur.' },
    { s: 'able to be trusted to do what is expected', o: ['reliable', 'reliant', 'reluctant', 'relishing'], a: 0, w: 'Reliable = fiable.' },
    { s: 'a document stating an agreed price', o: ['quotation', 'quota', 'quorum', 'questionnaire'], a: 0, w: 'Quotation = devis.' },
    { s: 'to cancel a decision or an agreement', o: ['rescind', 'reside', 'resume', 'prescribe'], a: 0, w: 'Rescind = annuler.' },
    { s: 'exact and accurate', o: ['precise', 'obscure', 'vague', 'loose'], a: 0, w: 'Precise = précis.' },
    { s: 'to give up a claim or a right', o: ['waive', 'wave', 'waiver', 'weave'], a: 0, w: 'Waive = renoncer à.' },
    { s: 'quick to act; done without delay', o: ['prompt', 'prone', 'promote', 'prompting'], a: 0, w: 'Prompt = rapide, ponctuel.' },
    { s: 'the money a company owes to others', o: ['liabilities', 'assets', 'equity', 'revenues'], a: 0, w: 'Liabilities = passif.' },
    { s: 'an official inspection of accounts', o: ['audit', 'auction', 'edict', 'affidavit'], a: 0, w: 'Audit = audit.' },
    { s: 'a general increase in prices', o: ['inflation', 'deflation', 'inflection', 'infusion'], a: 0, w: 'Inflation.' },
    { s: 'to arrange a new payment plan for a debt', o: ['reschedule', 'reshape', 'resell', 'restock'], a: 0, w: 'Reschedule a debt.' },
    { s: 'modest; not extreme', o: ['moderate', 'immoderate', 'mediocre', 'mute'], a: 0, w: 'Moderate = modéré.' },
    { s: 'a sum paid regularly to a shareholder', o: ['dividend', 'deduction', 'deposit', 'discount'], a: 0, w: 'Dividend = dividende.' },
    { s: 'to reduce the size of a company by cutting staff', o: ['downsize', 'oversize', 'upskill', 'outsource'], a: 0, w: 'Downsize = réduire les effectifs.' },
    { s: 'a legally binding agreement between two parties', o: ['contract', 'contact', 'contrast', 'conduct'], a: 0, w: 'Contract = contrat.' },
    { s: 'to grow or increase quickly', o: ['expand', 'expend', 'expense', 'expunge'], a: 0, w: 'Expand = se développer.' },
    { s: 'the state of owing money', o: ['indebtedness', 'indifference', 'independence', 'indulgence'], a: 0, w: 'Indebtedness = endettement.' },
    { s: 'careful management of resources', o: ['thrift', 'theft', 'thrive', 'drift'], a: 0, w: 'Thrift = économie, parcimonie.' },
    { s: 'a written request for payment', o: ['invoice', 'invoyce', 'invoicing', 'invoke'], a: 0, w: 'Invoice = facture.' },
    { s: 'to delay an event to a later date', o: ['postpone', 'postulant', 'posturing', 'postdate'], a: 0, w: 'Postpone = reporter.' }
  ];
  const enSpellPairs = [
    ['necessary', 'neccessary'], ['occurrence', 'ocurrence'], ['committee', 'comittee'], ['separate', 'seperate'],
    ['maintenance', 'maintainance'], ['acquaintance', 'aquaintance'], ['privilege', 'priviledge'], ['threshold', 'threshhold'],
    ['conscientious', 'concientious'], ['accommodate', 'accomodate'], ['definitely', 'definately'], ['beginning', 'begining'],
    ['tomorrow', 'tommorow'], ['recommend', 'recomend'], ['schedule', 'shedule'], ['business', 'buisness'],
    ['receive', 'recieve'], ['believe', 'beleive'], ['colleague', 'collegue'], ['environment', 'enviroment'],
    ['government', 'goverment'], ['immediately', 'immediatly'], ['knowledge', 'knowlege'], ['management', 'managerment'],
    ['particularly', 'particulary'], ['performance', 'performence'], ['professional', 'proffessional'], ['pronunciation', 'pronounciation'],
    ['questionnaire', 'questionaire'], ['responsibility', 'responsability'], ['successful', 'succesful'], ['sufficient', 'suficient'],
    ['temperature', 'temperture'], ['unfortunately', 'unfortunatly'], ['vehicle', 'vehicule'], ['existence', 'existance'],
    ['hierarchy', 'hierachy'], ['liaison', 'liason'], ['millennium', 'millenium'], ['noticeable', 'noticable']
  ];

  const frFluencyExtra = [
    { s: 'Nous comptons _____ votre retour avant vendredi.', o: ['sur', 'de', 'à', 'pour'], a: 0, w: 'Compter sur.' },
    { s: 'Le dossier a été transmis _____ service comptable.', o: ['au', 'du', 'à le', 'vers'], a: 0, w: 'À + le = au.' },
    { s: 'Cette décision relève _____ la direction générale.', o: ['de', 'du', 'à', 'par'], a: 0, w: 'Relever de.' },
    { s: 'Les résultats sont _____ hausse depuis mars.', o: ['en', 'à', 'de', 'sur'], a: 0, w: 'En hausse.' },
    { s: 'Le rapport fait état _____ plusieurs risques.', o: ['de', 'des', 'à', 'sur'], a: 0, w: 'Faire état de.' },
    { s: 'Je vous prie de bien vouloir _____ votre accord.', o: ['confirmer', 'confirmation', 'confirmé', 'confirmant'], a: 0, w: 'Après « vouloir » : infinitif.' },
    { s: 'La direction a donné son accord pour _____ le projet.', o: ['lancer', 'lancement', 'lancé', 'lançant'], a: 0, w: 'Après « pour » : infinitif.' },
    { s: 'Le remboursement sera effectué _____ réception de la facture.', o: ['dès', 'depuis', 'pendant', 'durant'], a: 0, w: 'Dès réception.' },
    { s: 'Veuillez trouver ci-joint la facture _____ la prestation.', o: ['correspondant à', 'correspondant de', 'correspondante à', 'correspond à'], a: 0, w: 'Participe présent + à.' },
    { s: 'Il convient _____ vérifier ces montants avant la clôture.', o: ['de', 'à', 'pour', 'par'], a: 0, w: 'Il convient de + infinitif.' },
    { s: 'Le délai de paiement a été fixé _____ trente jours.', o: ['à', 'de', 'pour de', 'sur'], a: 0, w: 'Fixer à.' },
    { s: 'Nous restons _____ votre disposition pour tout complément.', o: ['à', 'de', 'en', 'sur'], a: 0, w: 'À votre disposition.' },
    { s: 'La note de service a été diffusée _____ l’ensemble des équipes.', o: ['à', 'au', 'de', 'vers'], a: 0, w: 'Diffuser à.' },
    { s: 'Le budget prévisionnel a été _____ à la baisse.', o: ['révisé', 'réviser', 'révision', 'révisant'], a: 0, w: 'Participe passé après « a été ».' },
    { s: 'Ces dépenses ne sont pas _____ au projet.', o: ['imputables', 'imputer', 'imputation', 'imputant'], a: 0, w: 'Imputable à.' },
    { s: 'Le fournisseur s’engage _____ livrer sous dix jours.', o: ['à', 'de', 'pour', 'par'], a: 0, w: 'S’engager à + infinitif.' },
    { s: 'La clause s’applique _____ compter du 1er janvier.', o: ['à', 'au', 'de', 'en'], a: 0, w: 'À compter de.' },
    { s: 'Les deux services doivent se concerter _____ définir le plan.', o: ['pour', 'de', 'par', 'sur'], a: 0, w: 'Se concerter pour + infinitif.' },
    { s: 'Le rapport doit être remis _____ la fin du mois.', o: ['avant', 'devant', 'avant de', 'auparavant'], a: 0, w: 'Avant + nom.' },
    { s: 'La direction a pris acte _____ la décision du comité.', o: ['de', 'des', 'à', 'sur'], a: 0, w: 'Prendre acte de.' },
    { s: 'Ces montants ont été corrigés _____ la suite de l’audit.', o: ['à', 'en', 'de', 'par'], a: 0, w: 'À la suite de.' },
    { s: 'Nous vous saurions gré _____ bien vouloir confirmer la date.', o: ['de', 'à', 'pour', 'par'], a: 0, w: 'Savoir gré de.' },
    { s: 'Le service commercial a été _____ de deux personnes.', o: ['renforcé', 'renforcer', 'renforcement', 'renforçant'], a: 0, w: 'Participe passé.' },
    { s: 'Les factures sont payables _____ réception.', o: ['à', 'sur', 'de', 'en'], a: 0, w: 'Payable à réception.' }
  ];
  const frVocabExtra = [
    { s: 'diminution progressive des prix', o: ['déflation', 'inflation', 'récession', 'expansion'], a: 0, w: 'Déflation.' },
    { s: 'somme d’argent due à un fournisseur', o: ['dette', 'créance', 'apport', 'versement'], a: 0, w: 'Dette (la créance est une somme à recevoir).' },
    { s: 'remise accordée sur un prix', o: ['rabais', 'majoration', 'prime', 'taxe'], a: 0, w: 'Rabais.' },
    { s: 'contrôle officiel des comptes', o: ['audit', 'audience', 'audition', 'édit'], a: 0, w: 'Audit.' },
    { s: 'qui ne peut pas être contesté', o: ['incontestable', 'contestable', 'incongru', 'inconstant'], a: 0, w: 'Incontestable.' },
    { s: 'prévision des recettes et des dépenses', o: ['budget', 'bilan', 'bordereau', 'barème'], a: 0, w: 'Budget.' },
    { s: 'part de bénéfice versée aux actionnaires', o: ['dividende', 'agio', 'apport', 'arrérage'], a: 0, w: 'Dividende.' },
    { s: 'situation d’une entreprise qui dépense plus qu’elle ne gagne', o: ['déficit', 'excédent', 'endettement', 'trésorerie'], a: 0, w: 'Déficit.' },
    { s: 'examen détaillé d’un dossier', o: ['analyse', 'analyste', 'analogue', 'analytique'], a: 0, w: 'Analyse.' },
    { s: 'mettre fin à un contrat', o: ['résilier', 'résoudre', 'résider', 'résumer'], a: 0, w: 'Résilier.' },
    { s: 'somme versée avant la livraison', o: ['acompte', 'remboursement', 'solde', 'ristourne'], a: 0, w: 'Acompte.' },
    { s: 'qui respecte les règles prévues', o: ['conforme', 'informe', 'énorme', 'difforme'], a: 0, w: 'Conforme.' },
    { s: 'manque de moyens ou de ressources', o: ['pénurie', 'pléthore', 'profusion', 'abondance'], a: 0, w: 'Pénurie.' },
    { s: 'réduire les dépenses', o: ['restreindre', 'étendre', 'prétendre', 'astreindre'], a: 0, w: 'Restreindre.' },
    { s: 'appréciation de la valeur d’un bien', o: ['estimation', 'destination', 'délimitation', 'prestation'], a: 0, w: 'Estimation.' },
    { s: 'personne chargée de vérifier les comptes', o: ['auditeur', 'éditeur', 'acquéreur', 'assureur'], a: 0, w: 'Auditeur.' },
    { s: 'résultat positif d’une opération', o: ['bénéfice', 'manque', 'pénurie', 'perte'], a: 0, w: 'Bénéfice.' },
    { s: 'document récapitulatif des opérations d’un exercice', o: ['bilan', 'bureau', 'barème', 'bordereau'], a: 0, w: 'Bilan.' },
    { s: 'augmentation du niveau général des prix', o: ['inflation', 'déflation', 'stagnation', 'dévaluation'], a: 0, w: 'Inflation.' },
    { s: 'action de céder un bien à un tiers', o: ['cession', 'session', 'concession', 'succession'], a: 0, w: 'Cession.' },
    { s: 'somme laissée en garantie', o: ['caution', 'captation', 'causerie', 'cassation'], a: 0, w: 'Caution.' },
    { s: 'qui produit un rendement satisfaisant', o: ['rentable', 'rondement', 'tenable', 'portable'], a: 0, w: 'Rentable.' },
    { s: 'écart entre le prévu et le réalisé', o: ['variation', 'variance', 'vacation', 'vénération'], a: 0, w: 'Variation / écart.' },
    { s: 'faire face à une échéance', o: ['honorer', 'honoraire', 'honorifique', 'honorariat'], a: 0, w: 'Honorer une échéance.' }
  ];
  const frSpellPairs = [
    ['développement', 'dévelopement'], ['occasion', 'occassion'], ['apparemment', 'aparemment'], ['maintenance', 'maintainance'],
    ['privilège', 'privilége'], ['consciencieux', 'concentieux'], ['rythme', 'rhythme'], ['transmettre', 'transmetre'],
    ['acquérir', 'acquérirre'], ['palette', 'pallette'], ['environnement', 'environement'], ['professionnel', 'profesionnel'],
    ['nécessaire', 'nécéssaire'], ['commettre', 'comettre'], ['indépendamment', 'indépendament'], ['accueil', 'acceuil'],
    ['adresse', 'addrèsse'], ['aggraver', 'agraver'], ['améliorer', 'amméliorer'], ['appeler', 'appeller'],
    ['argument', 'arguement'], ['attendre', 'atendre'], ['bibliothèque', 'bibliothéque'], ['catégorie', 'catégorrie'],
    ['collaboration', 'colaboration'], ['connaisseur', 'conaisseur'], ['décision', 'décission'], ['définition', 'définission'],
    ['difficulté', 'difficultée'], ['efficace', 'efficasse'], ['élément', 'élement'], ['entreprise', 'entrepise'],
    ['évidemment', 'évidament'], ['exception', 'exeption'], ['expérience', 'experiance'], ['gestion', 'guestion'],
    ['immédiatement', 'imédiatement'], ['intéressant', 'interressant'], ['malheureusement', 'malheuresement'], ['parallèle', 'paralelle'],
    ['satisfaction', 'satisfation'], ['sérieux', 'serrieux'], ['supplémentaire', 'suplementaire'], ['utiliser', 'utilisser']
  ];

  /* ─────────── Comportement professionnel — 48 blocs × 3 (FR / EN) ─────────── */
  const behaviour = [
    ["Je termine mes tâches sans qu’on me le demande deux fois.", "I complete my tasks without being asked twice."],
    ["J’aime que mes résultats soient comparés à ceux des autres.", "I like my results to be compared with other people’s."],
    ["Je garde mon calme quand tout s’accélère.", "I stay calm when everything speeds up."],

    ["Je préviens tôt quand je vois un risque de retard.", "I raise a flag early when I see a risk of delay."],
    ["Je cherche volontiers la compétition dans mon travail.", "I actively look for competition in my work."],
    ["Je respecte les délais même sous pression.", "I meet deadlines even under pressure."],

    ["Je relis mon travail avant de le rendre.", "I proofread my work before handing it in."],
    ["Je veux être meilleur que mes pairs.", "I want to be better than my peers."],
    ["Je digère vite les remarques critiques.", "I take critical feedback in my stride."],

    ["Je note mes priorités chaque matin.", "I write down my priorities every morning."],
    ["L’émulation d’équipe me stimule.", "Friendly rivalry within the team spurs me on."],
    ["Je préviens immédiatement si je ne peux pas tenir un engagement.", "I say immediately if I cannot keep a commitment."],

    ["Je pose des questions quand une consigne est floue.", "I ask questions when instructions are unclear."],
    ["Je compare souvent mes résultats à ceux du marché.", "I often compare my results with those of the market."],
    ["Je reste concentré malgré les interruptions.", "I stay focused despite interruptions."],

    ["Je découpe les gros chantiers en étapes.", "I break large pieces of work into steps."],
    ["Gagner un défi me motive.", "Winning a challenge motivates me."],
    ["Je signale les problèmes dès que je les constate.", "I report problems as soon as I notice them."],

    ["Je vérifie les chiffres avant de les transmettre.", "I check figures before passing them on."],
    ["Je prends plaisir à dépasser les objectifs fixés.", "I enjoy exceeding the targets set."],
    ["Je m’adapte quand le plan change.", "I adapt when the plan changes."],

    ["Je demande un retour sur la qualité de mon travail.", "I ask for feedback on the quality of my work."],
    ["La concurrence interne ne me gêne pas.", "Internal competition does not bother me."],
    ["Je tiens mes engagements même quand c’est inconfortable.", "I keep my commitments even when it is uncomfortable."],

    ["Je garde une trace écrite de mes décisions.", "I keep a written record of my decisions."],
    ["Je veux figurer parmi les meilleurs de mon équipe.", "I want to be among the best in my team."],
    ["Je hiérarchise quand tout arrive en même temps.", "I prioritise when everything arrives at once."],

    ["Je préviens les personnes impactées par mes retards.", "I warn the people affected by my delays."],
    ["Mesurer ma progression me motive.", "Measuring my progress motivates me."],
    ["Je vais au bout des tâches ingrates.", "I see thankless tasks through to the end."],

    ["Je clarifie le niveau de qualité attendu.", "I clarify the level of quality expected."],
    ["J’accepte d’être challengé sur mes idées.", "I accept being challenged on my ideas."],
    ["Je replanifie rapidement après un imprévu.", "I replan quickly after an unexpected event."],

    ["Je fais relire mon travail par un collègue quand c’est critique.", "I have a colleague review my work when it is critical."],
    ["Comparer mes méthodes à celles des autres m’intéresse.", "I am interested in comparing my methods with other people’s."],
    ["Je respecte les créneaux de travail des autres.", "I respect other people’s working hours."],

    ["Je signale quand une charge devient irréaliste.", "I speak up when a workload becomes unrealistic."],
    ["Le goût du défi fait partie de ma façon de travailler.", "A taste for challenge is part of the way I work."],
    ["Je maintiens mon niveau d’exigence en fin de journée.", "I maintain my standards at the end of the day."],

    ["Je prépare mes réunions à l’avance.", "I prepare my meetings in advance."],
    ["Dépasser un résultat précédent me satisfait.", "Beating a previous result satisfies me."],
    ["Je communique mes indisponibilités à l’avance.", "I communicate my unavailability in advance."],

    ["Je range mes dossiers pour les retrouver vite.", "I keep my files tidy so I can find them quickly."],
    ["Je sais défendre ma position face à un contradicteur.", "I can defend my position against someone who disagrees."],
    ["Je termine la journée sur une liste claire pour demain.", "I end the day with a clear list for tomorrow."],

    ["Je demande de l’aide avant d’être bloqué trop longtemps.", "I ask for help before being stuck for too long."],
    ["Les classements internes ne me découragent pas.", "Internal rankings do not discourage me."],
    ["Je préviens quand une dépendance externe menace.", "I give warning when an external dependency is at risk."],

    ["Je contrôle deux fois les informations sensibles.", "I double-check sensitive information."],
    ["L’idée de battre un record d’équipe me plaît.", "The idea of beating a team record appeals to me."],
    ["Je reste factuel quand on me critique.", "I stay factual when I am criticised."],

    ["Je mesure le temps réel que prennent mes tâches.", "I measure the real time my tasks take."],
    ["Je propose spontanément des améliorations de méthode.", "I spontaneously suggest better ways of working."],
    ["Je ne laisse pas un message urgent sans réponse.", "I do not leave an urgent message unanswered."],

    ["Je teste mes livrables dans les conditions réelles.", "I test my deliverables under real conditions."],
    ["Être évalué régulièrement me convient.", "Being assessed regularly suits me."],
    ["Je coupe mes notifications pour finir une tâche longue.", "I turn off my notifications to finish a long task."],

    ["Je documente ce que j’ai appris pour les suivants.", "I document what I have learnt for those who follow."],
    ["Le défi m’énergie plus qu’il ne me stresse.", "Challenge energises me rather than stressing me."],
    ["Je dis non quand je ne peux pas bien faire.", "I say no when I cannot do a good job."],

    ["Je reviens vers les gens à la date promise.", "I get back to people by the date promised."],
    ["Je cherche des référents meilleurs que moi pour progresser.", "I look for role models better than me in order to improve."],
    ["Je garde le même soin pour les tâches invisibles.", "I take the same care with invisible tasks."],

    ["Je fais un point d’avancement sans qu’on me le demande.", "I give a progress update without being asked."],
    ["Rivaliser avec moi-même me pousse à avancer.", "Competing with myself drives me forward."],
    ["Je préviens avant le délai, pas après.", "I give warning before the deadline, not after."],

    ["Je reformule les demandes pour éviter les malentendus.", "I rephrase requests to avoid misunderstandings."],
    ["J’ose postuler à des missions au-dessus de mon niveau.", "I dare to apply for assignments above my level."],
    ["Je repère vite ce qui est vraiment urgent.", "I quickly spot what is truly urgent."],

    ["Je laisse une trace des arbitrages pris.", "I keep a record of the trade-offs made."],
    ["Le dépassement d’objectif me motive plus que la prime.", "Exceeding a target motivates me more than the bonus."],
    ["Je reste joignable pendant mes absences planifiées.", "I stay reachable during planned absences."],

    ["Je vérifie la source d’une information avant de la reprendre.", "I check the source of information before reusing it."],
    ["J’apprécie les environnements où l’on se pousse mutuellement.", "I appreciate environments where people push each other."],
    ["Je respecte les temps de repos de mes collègues.", "I respect my colleagues’ rest times."],

    ["Je rends compte des difficultés avec des propositions.", "I report difficulties together with proposals."],
    ["Chaque progression chiffrée me satisfait.", "Every measurable step forward satisfies me."],
    ["Je boucle un sujet avant d’en ouvrir un autre.", "I close one topic before opening another."],

    ["Je demande le contexte avant d’exécuter.", "I ask for the context before carrying out a task."],
    ["Les challenges courts me réussissent.", "Short challenges suit me well."],
    ["Je signale un résultat anormal même s’il m’avantage.", "I report an unusual result even if it works in my favour."],

    ["Je planifie une marge pour les imprévus.", "I plan a margin for the unexpected."],
    ["Être challengé m’évite la routine.", "Being challenged keeps me out of a rut."],
    ["Je maintiens mes standards quand personne ne regarde.", "I keep my standards when no one is watching."],

    ["Je partage mes outils avec l’équipe.", "I share my tools with the team."],
    ["Je fixe des objectifs légèrement au-dessus du demandé.", "I set targets slightly above what is asked."],
    ["Je préviens dès que je change de priorité.", "I give warning as soon as I change priority."],

    ["Je relis les exigences avant de valider un livrable.", "I re-read the requirements before approving a deliverable."],
    ["Le score d’équipe compte autant que le mien.", "The team score matters as much as my own."],
    ["Je termine ce que j’ai commencé.", "I finish what I start."],

    ["Je sollicite un avis contraire au mien.", "I invite opinions that differ from mine."],
    ["Perdre un appel d’offre me pousse à analyser mes erreurs.", "Losing a tender makes me analyse my mistakes."],
    ["Je protège mon temps de travail profond.", "I protect my deep-work time."],

    ["Je note les retours reçus et ce que j’en fais.", "I note the feedback I receive and what I do with it."],
    ["La comparaison saine tire l’équipe vers le haut.", "Healthy comparison lifts the team."],
    ["Je reconnais mes erreurs sans attendre qu’on les pointe.", "I admit my mistakes without waiting to be challenged."],

    ["Je propose une date réaliste plutôt qu’une date plaisante.", "I propose a realistic date rather than a pleasant one."],
    ["Me confronter à plus fort m’enseigne quelque chose.", "Measuring myself against stronger people teaches me something."],
    ["Je garde une routine stable en période chargée.", "I keep a stable routine in busy periods."],

    ["Je vérifie que tout le monde a la même information.", "I check that everyone has the same information."],
    ["J’aime les objectifs tendus mais atteignables.", "I like demanding but achievable targets."],
    ["Je réponds dans les délais convenus, même pour dire non.", "I reply within the agreed deadlines, even to say no."],

    ["Je prépare un plan B pour les étapes critiques.", "I prepare a plan B for critical steps."],
    ["Sortir premier d’un exercice me fait plaisir.", "Coming first in an exercise makes me happy."],
    ["Je préviens mon manager avant l’escalade.", "I warn my manager before an escalation."],

    ["Je mesure l’effort avant de m’engager.", "I weigh up the effort before committing."],
    ["La compétition ne m’empêche pas d’aider les autres.", "Competition does not stop me from helping others."],
    ["Je laisse mon poste en ordre pour le suivant.", "I leave my workstation in order for the next person."],

    ["Je commence par la tâche la plus difficile de ma journée.", "I start with the hardest task of my day."],
    ["Un objectif collectif me motive autant qu’un objectif personnel.", "A collective goal motivates me as much as a personal one."],
    ["Je reste courtois même quand la pression monte.", "I stay courteous even when pressure rises."],

    ["Je bloque du temps dans mon agenda pour les sujets importants.", "I block time in my diary for important matters."],
    ["J’aime être quelqu’un sur qui l’équipe peut compter.", "I like being someone the team can rely on."],
    ["Je prends du recul avant de réagir à un e-mail irritant.", "I step back before reacting to an irritating e-mail."],

    ["Je vérifie que j’ai bien compris avant de commencer un travail long.", "I check that I have understood before starting a long piece of work."],
    ["Les défis techniques m’attirent plus que les tâches routinières.", "Technical challenges appeal to me more than routine tasks."],
    ["Je demande de l’aide avant la dernière minute.", "I ask for help before the last minute."],

    ["Je respecte les procédures même lorsque je les trouve perfectibles.", "I follow procedures even when I think they could be better."],
    ["J’aime travailler dans une équipe qui progresse vite.", "I like working in a team that moves fast."],
    ["Je garde mon sang-froid face à un client mécontent.", "I keep my composure with an unhappy client."],

    ["Je fais le point sur mes priorités quand tout change en même temps.", "I review my priorities when everything changes at once."],
    ["Me fixer un cap ambitieux me stimule.", "Setting an ambitious goal stimulates me."],
    ["Je m’excuse rapidement quand je fais une erreur.", "I apologise quickly when I make a mistake."],

    ["Je m’assure que mes livrables sont utilisables tels quels.", "I make sure my deliverables can be used as they are."],
    ["Les retours de mes pairs m’aident à progresser.", "Feedback from my peers helps me improve."],
    ["Je continue à travailler efficacement en fin de semaine.", "I keep working effectively at the end of the week."],

    ["Je vérifie mes hypothèses avant de prendre une décision.", "I check my assumptions before making a decision."],
    ["Je me réjouis des progrès de mes collègues.", "I take pleasure in my colleagues’ progress."],
    ["Je reste concentré lors des longues réunions.", "I stay focused in long meetings."],

    ["Je signale ce que je ne sais pas encore faire pour être formé.", "I say what I cannot do yet so that I can be trained."],
    ["Un environnement exigeant me tire vers le haut.", "A demanding environment pulls me up."],
    ["Je réponds présent quand l’équipe a besoin de renfort.", "I step in when the team needs support."],

    ["Je prépare les questions à poser avant un entretien.", "I prepare the questions to ask before an interview."],
    ["Je compare mon travail à mes résultats passés.", "I compare my work with my own past results."],
    ["Je conserve mon calme quand un projet prend du retard.", "I keep calm when a project falls behind."],

    ["Je mets à jour mes informations de suivi sans attendre.", "I update my tracking information without waiting to be asked."],
    ["L’idée de progresser chaque mois me motive.", "The idea of improving every month motivates me."],
    ["Je reste respectueux quand une décision ne me convient pas.", "I stay respectful when a decision does not suit me."],

    ["Je m’organise pour rendre avant l’échéance.", "I organise myself to deliver before the deadline."],
    ["J’aime être évalué sur des résultats concrets.", "I like being assessed on concrete results."],
    ["Je gère les imprévus sans perdre de vue l’essentiel.", "I handle the unexpected without losing sight of what matters."],

    ["Je vérifie le travail des autres quand on me le demande.", "I check other people’s work when asked to."],
    ["Je cherche à faire mieux que la fois précédente.", "I try to do better than the time before."],
    ["Je reste positif même dans les périodes difficiles.", "I stay positive even in difficult periods."],
  ];
  /* ─────────── Motivation & intérêts — 36 blocs × 3 (FR / EN) ─────────── */
  const motivation = [
    ["L’entreprise devrait former ses collaborateurs en continu.", "The company should provide ongoing training for its employees."],
    ["Les décisions importantes devraient être expliquées à tous.", "Important decisions should be explained to everyone."],
    ["La hiérarchie devrait rester légère et lisible.", "Hierarchy should stay light and clear."],

    ["Le télétravail devrait être possible quand la tâche le permet.", "Remote work should be possible when the task allows it."],
    ["Les erreurs devraient servir d’apprentissage collectif.", "Mistakes should serve as a collective learning opportunity."],
    ["Les promotions devraient reposer sur des critères connus.", "Promotions should be based on known criteria."],

    ["Chacun devrait connaître l’impact de son travail.", "Everyone should know the impact of their work."],
    ["Les réunions devraient avoir un ordre du jour clair.", "Meetings should have a clear agenda."],
    ["L’entreprise devrait encourager la mobilité interne.", "The company should encourage internal mobility."],

    ["Les salariés devraient pouvoir contester une décision sans risque.", "Employees should be able to challenge a decision without risk."],
    ["La rémunération devrait être comparable au marché.", "Pay should be comparable with the market."],
    ["Les équipes devraient être stables dans la durée.", "Teams should be stable over time."],

    ["L’innovation devrait faire partie du quotidien.", "Innovation should be part of everyday work."],
    ["Les outils de travail devraient être modernes et fiables.", "Work tools should be modern and reliable."],
    ["Le management devrait donner du sens avant des tâches.", "Management should give meaning before tasks."],

    ["Les feedbacks devraient être réguliers et directs.", "Feedback should be regular and direct."],
    ["L’entreprise devrait protéger les temps de repos.", "The company should protect rest times."],
    ["Les projets devraient laisser place à l’autonomie.", "Projects should leave room for autonomy."],

    ["La diversité des profils devrait être recherchée.", "Diversity of profiles should be actively sought."],
    ["Les succès devraient être célébrés collectivement.", "Successes should be celebrated collectively."],
    ["Les objectifs devraient être alignés sur la stratégie.", "Objectives should be aligned with the strategy."],

    ["Chacun devrait pouvoir dire non à une échéance irréaliste.", "Everyone should be able to say no to an unrealistic deadline."],
    ["L’entreprise devrait investir dans la communauté locale.", "The company should invest in the local community."],
    ["Les conflits constructifs devraient être permis.", "Constructive conflict should be allowed."],

    ["Le développement professionnel devrait être accompagné.", "Professional development should be supported."],
    ["Les informations essentielles devraient circuler vite.", "Essential information should circulate quickly."],
    ["La confiance devrait primer sur le contrôle.", "Trust should come before control."],

    ["Les horaires devraient s’adapter aux contraintes personnelles.", "Working hours should adapt to personal constraints."],
    ["La qualité devrait primer sur la vitesse.", "Quality should come before speed."],
    ["Les idées nouvelles devraient être testées rapidement.", "New ideas should be tested quickly."],

    ["L’entreprise devrait tenir ses promesses envers les nouveaux.", "The company should keep its promises to new joiners."],
    ["Les responsabilités devraient être réparties équitablement.", "Responsibilities should be shared fairly."],
    ["Le droit à la déconnexion devrait être respecté.", "The right to disconnect should be respected."],

    ["Chacun devrait voir comment progresse l’ensemble.", "Everyone should see how the whole is progressing."],
    ["L’exigence devrait s’appliquer à tous au même niveau.", "High standards should apply to everyone equally."],
    ["La mobilité interne devrait être aussi valorisée que le recrutement externe.", "Internal mobility should be valued as much as external recruitment."],

    ["Le sens du travail devrait être rappelé régulièrement.", "The meaning of the work should be restated regularly."],
    ["Les managers devraient être formés à l’écoute.", "Managers should be trained to listen."],
    ["L’entreprise devrait mesurer la satisfaction de ses équipes.", "The company should measure how satisfied its teams are."],

    ["Les décisions difficiles devraient être assumées par la direction.", "Difficult decisions should be owned by management."],
    ["Les responsabilités de chacun devraient être claires dès l’arrivée.", "Everyone’s responsibilities should be clear from day one."],
    ["Les efforts devraient être reconnus autant que les résultats.", "Effort should be recognised as much as results."],

    ["L’entreprise devrait laisser du temps pour apprendre.", "The company should leave time for learning."],
    ["Les collègues devraient pouvoir se donner un retour direct.", "Colleagues should be able to give each other direct feedback."],
    ["La sécurité de l’emploi compte pour moi.", "Job security matters to me."],

    ["Un salaire variable lié à la performance me motive.", "Pay linked to performance motivates me."],
    ["L’entreprise devrait soutenir les projets personnels utiles au travail.", "The company should support personal projects that are useful for work."],
    ["Les règles devraient être les mêmes pour tous.", "The rules should be the same for everyone."],

    ["L’entreprise devrait s’engager pour l’environnement.", "The company should be committed to the environment."],
    ["Les équipes devraient pouvoir choisir leurs méthodes de travail.", "Teams should be able to choose how they work."],
    ["Les objectifs devraient être révisables en cours d’année.", "Objectives should be open to revision during the year."],

    ["Le travail devrait laisser du temps pour la vie personnelle.", "Work should leave time for personal life."],
    ["Les erreurs devraient être traitées sans humiliation.", "Mistakes should be handled without humiliation."],
    ["Les carrières devraient être plus longues que les projets.", "Careers should last longer than projects."],

    ["L’entreprise devrait communiquer sur ses résultats.", "The company should communicate its results."],
    ["La charge de travail devrait être suivie de près.", "Workload should be monitored closely."],
    ["Les idées des juniors devraient être écoutées.", "Junior employees’ ideas should be heard."],

    ["Les responsabilités devraient évoluer avec les compétences.", "Responsibilities should grow with skills."],
    ["Un bon équilibre entre autonomie et cadre me convient.", "A good balance between autonomy and framework suits me."],
    ["L’entreprise devrait faciliter la mobilité géographique.", "The company should make geographic mobility easier."],

    ["Les réunions devraient être courtes et utiles.", "Meetings should be short and useful."],
    ["L’entreprise devrait investir dans la formation des managers.", "The company should invest in training its managers."],
    ["Les réussites collectives devraient primer sur les classements individuels.", "Collective success should come before individual rankings."],

    ["Je voudrais travailler dans un environnement international.", "I would like to work in an international environment."],
    ["L’entreprise devrait aider chacun à construire un projet professionnel.", "The company should help everyone build a career plan."],
    ["Les outils numériques devraient simplifier le travail, pas le compliquer.", "Digital tools should simplify work, not complicate it."],

    ["La qualité de la relation avec le manager compte pour moi.", "The quality of the relationship with my manager matters to me."],
    ["Les entreprises devraient être transparentes sur les salaires.", "Companies should be transparent about pay."],
    ["L’entreprise devrait laisser une vraie place à l’initiative.", "The company should give real room for initiative."],

    ["Un travail utile à la société me motive.", "Work that is useful to society motivates me."],
    ["Les temps de trajet longs devraient être évités.", "Long commutes should be avoided."],
    ["L’entreprise devrait reconnaître l’ancienneté sans bloquer les évolutions.", "The company should recognise seniority without blocking progression."],

    ["Les équipes devraient pouvoir décider de leurs horaires.", "Teams should be able to decide their own working hours."],
    ["Les clients devraient être au centre des décisions.", "Clients should be at the centre of decisions."],
    ["L’entreprise devrait aider les salariés à se reconvertir.", "The company should help employees retrain."],

    ["L’entreprise devrait prendre soin de la santé au travail.", "The company should take care of health at work."],
    ["Les projets devraient avoir des objectifs réalistes.", "Projects should have realistic objectives."],
    ["Les progrès devraient être fêtés simplement.", "Progress should be celebrated simply."],

    ["Un poste varié me motive plus qu’un poste stable.", "A varied role motivates me more than a stable one."],
    ["L’entreprise devrait favoriser le travail en équipe.", "The company should encourage teamwork."],
    ["Les décisions devraient être prises au plus près du terrain.", "Decisions should be taken as close to the front line as possible."],

    ["Les entreprises devraient partager la valeur créée.", "Companies should share the value they create."],
    ["L’entreprise devrait respecter les engagements pris avec les fournisseurs.", "The company should honour the commitments made to suppliers."],
    ["Chacun devrait pouvoir travailler depuis un autre lieu en cas de besoin.", "Everyone should be able to work from another location when needed."],

    ["Une culture du résultat me convient si elle reste humaine.", "A results-driven culture suits me if it stays humane."],
    ["Les formations devraient être accessibles pendant le temps de travail.", "Training should be available during working hours."],
    ["L’entreprise devrait mesurer l’impact social de ses décisions.", "The company should measure the social impact of its decisions."],

    ["L’entreprise devrait encourager la prise de parole des équipes.", "The company should encourage teams to speak up."],
    ["Les outils devraient être choisis par ceux qui les utilisent.", "Tools should be chosen by the people who use them."],
    ["La mobilité interne devrait être encouragée avant le recrutement externe.", "Internal mobility should be encouraged before external recruitment."],

    ["Je préfère les projets longs aux missions courtes.", "I prefer long projects to short assignments."],
    ["L’entreprise devrait aider chacun à mieux gérer son énergie.", "The company should help everyone manage their energy better."],
    ["Les succès d’équipe devraient compter dans l’évaluation.", "Team success should count in performance reviews."],

    ["L’entreprise devrait être exemplaire dans son secteur.", "The company should be a role model in its sector."],
    ["Les bonnes pratiques devraient circuler entre les équipes.", "Good practices should circulate between teams."],
    ["Les responsabilités familiales devraient être respectées.", "Family responsibilities should be respected."],

    ["Un mentor devrait être proposé aux nouveaux arrivants.", "A mentor should be offered to new joiners."],
    ["Les objectifs devraient tenir compte des moyens donnés.", "Objectives should take account of the resources provided."],
    ["L’entreprise devrait s’exprimer clairement en période de crise.", "The company should communicate clearly in a crisis."],

    ["Les équipes devraient pouvoir tester leurs idées rapidement.", "Teams should be able to test their ideas quickly."],
    ["L’évaluation devrait porter sur les compétences, pas sur les diplômes.", "Assessment should be based on skills, not diplomas."],
    ["L’entreprise devrait limiter les réorganisations fréquentes.", "The company should limit frequent reorganisations."],

    ["Le sens écologique des projets compte pour moi.", "The environmental purpose of projects matters to me."],
    ["Les salariés devraient être associés aux choix qui les concernent.", "Employees should be involved in the choices that affect them."],
    ["L’entreprise devrait offrir un cadre de travail agréable.", "The company should offer a pleasant working environment."],

    ["La progression des collègues me motive.", "My colleagues’ progress motivates me."],
    ["L’entreprise devrait veiller à la simplicité des procédures.", "The company should keep procedures simple."],
    ["Je souhaite travailler dans une entreprise qui reconnaît les efforts de chacun.", "I want to work for a company that recognises everyone’s effort."],
  ];

  /* ─────────── Raisonnement mécanique — 24 items, 3 options ─────────── */
  const mech = [
    { sc: 'gears2',   q: 'If gear A turns clockwise, which way does gear B turn?', o: ['anticlockwise', 'clockwise', 'it does not turn'], a: 0, w: 'Two meshing gears turn in opposite directions.' },
    { sc: 'gears3',   q: 'Gears A, B and C are in a row. If A turns clockwise, which way does C turn?', o: ['clockwise', 'anticlockwise', 'it does not turn'], a: 0, w: 'A→B reverses, B→C reverses again: same direction as A.' },
    { sc: 'gears4',   q: 'Four gears mesh in a line. If A turns anticlockwise, which way does D turn?', o: ['anticlockwise', 'clockwise', 'it does not turn'], a: 1, w: 'Each mesh reverses: A(anti) → B(cw) → C(anti) → D(cw).' },
    { sc: 'gears2size', q: 'Small gear A drives large gear B. Which one turns faster?', o: ['A', 'B', 'same speed'], a: 0, w: 'The smaller gear completes more turns per revolution of the larger one.' },
    { sc: 'belt',     q: 'Pulley A drives pulley B with an open belt. If A turns clockwise, B turns…', o: ['clockwise', 'anticlockwise', 'it stays still'], a: 0, w: 'An open (uncrossed) belt keeps the same direction.' },
    { sc: 'beltcross', q: 'Pulley A drives pulley B with a crossed belt. If A turns clockwise, B turns…', o: ['anticlockwise', 'clockwise', 'it stays still'], a: 0, w: 'A crossed belt reverses the direction.' },
    { sc: 'lever',    q: 'On a lever, the load is far from the pivot and the effort is close to it. The effort needed is…', o: ['greater than the load', 'smaller than the load', 'equal to the load'], a: 0, w: 'A short effort arm requires a greater effort.' },
    { sc: 'pulley1',  q: 'A single fixed pulley is used to lift a load. The force needed is…', o: ['equal to the weight', 'half the weight', 'double the weight'], a: 0, w: 'A fixed pulley only changes the direction of the force.' },
    { sc: 'pulley2',  q: 'A load hangs from a movable pulley held by two rope segments. The force needed is about…', o: ['half the weight', 'the full weight', 'double the weight'], a: 0, w: 'Two supporting segments share the load.' },
    { sc: 'pulley3',  q: 'Three parallel rope segments support the movable block. The force needed is about…', o: ['a third of the weight', 'half the weight', 'the full weight'], a: 0, w: 'The load is shared between three segments.' },
    { sc: 'spring',   q: 'A second identical weight is added to the spring. The spring stretches…', o: ['twice as much', 'the same amount', 'half as much'], a: 0, w: 'Extension is proportional to load (elastic range).' },
    { sc: 'axle',     q: 'Wheel G and pulley P are fixed on the same axle. If G makes one turn, P makes…', o: ['one turn', 'more than one turn', 'less than one turn'], a: 0, w: 'Same axle = same rotation.' },
    { sc: 'gears2',   q: 'Gear A is driven clockwise. What happens to the contact teeth of A and B?', o: ['they move in opposite directions at the contact point', 'they move in the same direction at the contact point', 'they do not move'], a: 1, w: 'At the mesh point the tooth surfaces travel together.' },
    { sc: 'gears3',   q: 'Which gears turn in the same direction as A?', o: ['C', 'B', 'both B and C'], a: 0, w: 'B reverses, C matches A.' },
    { sc: 'gears4',   q: 'Which gears turn in the same direction as B?', o: ['D', 'A', 'C'], a: 0, w: 'A(anti) B(cw) C(anti) D(cw): B and D match.' },
    { sc: 'gears2size', q: 'Large gear B makes one full turn. The small gear A makes…', o: ['more than one turn', 'exactly one turn', 'less than one turn'], a: 0, w: 'The smaller gear turns faster.' },
    { sc: 'belt',     q: 'The belt slips on pulley B. What is the likely effect on B’s speed?', o: ['B turns slower than expected', 'B turns faster than expected', 'no effect'], a: 0, w: 'Slippage loses transmission.' },
    { sc: 'beltcross', q: 'Why use a crossed belt here?', o: ['to reverse the driven pulley’s direction', 'to increase the driven pulley’s speed', 'to reduce friction'], a: 0, w: 'Crossing reverses direction.' },
    { sc: 'lever',    q: 'The effort moves further from the pivot. The effort needed to lift the same load…', o: ['decreases', 'increases', 'does not change'], a: 0, w: 'A longer effort arm gives more leverage.' },
    { sc: 'pulley1',  q: 'What is the main advantage of this fixed pulley?', o: ['it changes the direction of the pull', 'it halves the force', 'it doubles the speed'], a: 0, w: 'Direction change only.' },
    { sc: 'pulley2',  q: 'To lift the load 1 metre, the free end of the rope must be pulled about…', o: ['2 metres', '1 metre', '0.5 metre'], a: 0, w: 'Two segments: rope pulled = 2 × height.' },
    { sc: 'spring',   q: 'The spring is replaced by a stiffer one. For the same weight it stretches…', o: ['less', 'more', 'the same'], a: 0, w: 'Stiffer spring = smaller extension.' },
    { sc: 'axle',     q: 'Pulley P (small) drives a belt while fixed to wheel G. Compared with G’s rim, P’s rim moves…', o: ['slower', 'faster', 'at the same speed'], a: 0, w: 'Same rotation, smaller radius → lower rim speed.' },
    { sc: 'gears3',   q: 'Gear B is removed from the row. What happens?', o: ['C no longer turns', 'C turns like A', 'C turns faster'], a: 0, w: 'Without B the transmission from A to C is broken.' }
  ].map((x, i) => Object.assign({ id: 'M' + (i + 1) }, x));

  /* ─────────── Morgan Stanley — chatAssess (Aon) : 13 scénarios de chat ───────────
     Format documenté par les candidats (Wall Street Oasis : « responding to messages
     of colleagues in fake scenarios using a chat feature » ; mconsultingprep : « chat
     feature named chatAssess »). Contenu d'entraînement ORIGINAL rédigé pour cette
     plateforme : chaque scénario est un message reçu d'un collègue, le candidat répond
     dans la fenêtre de chat comme il le ferait en situation réelle. Paires [FR, EN]. */
  const msChat = [
    { from: 'Priya Nair — Analyst', in: [
      'Salut ! Je pars en réunion client dans 5 minutes. Tu peux envoyer la version actuelle du pitch au client tout de suite ? Il manque encore deux slides, mais il attend quelque chose avant midi.',
      'Hi! I’m heading into a client meeting in 5 minutes. Could you send the current version of the pitch to the client right away? Two slides are still unfinished, but the client expects something before noon.' ] },
    { from: 'Tom Keller — Associate', in: [
      'Hello, je monte un projet transversal et j’aurais besoin du dossier client Meridian. Tu peux me l’envoyer directement ? Inutile de passer par mon manager, ça ira plus vite.',
      'Hello, I’m setting up a cross-team project and I need the Meridian client file. Could you send it to me directly? No need to go through my manager, it will be faster.' ] },
    { from: 'Sofia Marino — Assistante d’équipe', in: [
      'Petit rappel : tu as deux réunions planifiées demain à 10h en même temps — le point hebdo de l’équipe et l’onboarding du nouveau stagiaire. Laquelle est-ce que je garde ?',
      'Quick reminder: you have two meetings scheduled for 10 a.m. tomorrow at the same time — the team weekly catch-up and the new intern’s onboarding. Which one should I keep?' ] },
    { from: 'David Chen — VP', in: [
      'Le modèle est sur le drive partagé. Peux-tu vérifier les chiffres clés avant 9h demain matin ? Si quelque chose te semble incohérent, signale-le-moi immédiatement plutôt que de corriger seul dans ton coin.',
      'The model is on the shared drive. Could you check the key figures before 9 a.m. tomorrow? If anything looks inconsistent to you, flag it to me immediately rather than fixing it on your own.' ] },
    { from: 'Léa Fontaine — Analyste', in: [
      'Petit service : je dois partir à 15h aujourd’hui mais mon relevé d’heures doit afficher 19h. Tu peux saisir les heures à ma place ? Je te revaudrai ça.',
      'Quick favour: I have to leave at 3 p.m. today but my timesheet needs to show 7 p.m. Could you log the hours for me? I’ll owe you one.' ] },
    { from: 'Marcus Webb — Compliance Officer', in: [
      'Pour l’audit du régulateur, il me faut la liste des transactions du compte 44-821. Je sais que ça demande normalement la validation du manager, mais le délai est très court — tu peux me l’envoyer directement ?',
      'For the regulator’s audit, I need the transaction list of account 44-821. I know it normally requires manager approval, but the deadline is very tight — could you send it to me directly?' ] },
    { from: 'Anna Petrova — Client Coverage', in: [
      'Le client Meridian demande notre grille tarifaire exacte sur le desk produits structurés avant 17h. Je n’ai pas les chiffres sous la main — tu peux lui donner une réponse rapide, même une estimation ?',
      'The Meridian client is asking for our exact fee structure on the structured products desk before 5 p.m. I don’t have the figures at hand — could you give them a quick answer, even an estimate?' ] },
    { from: 'Hugo Lambert — Stagiaire', in: [
      'Au secours : j’ai trois tâches « urgentes » de trois personnes différentes, toutes pour aujourd’hui — deux VP et un associate. Je ne peux matériellement pas tout faire. Qu’est-ce que je dois faire ?',
      'Help: I have three “urgent” tasks from three different people, all due today — two VPs and one associate. I physically cannot do all three. What should I do?' ] },
    { from: 'Rachel Adeyemi — RH', in: [
      'Pour préparer la revue de rémunération, tu pourrais me dire ce que gagne à peu près ton collègue de bureau ? Ça reste entre nous, c’est juste pour vérifier l’équité interne.',
      'To prepare the compensation review, could you tell me roughly what your desk neighbour earns? It stays between us, it is only to check internal fairness.' ] },
    { from: 'Karim Benali — Analyste', in: [
      'Hey, je viens de recevoir un e-mail du CEO qui demande d’acheter en urgence des cartes cadeaux et de cliquer sur un lien pour « valider ». Bizarre, non ? Je clique pour voir ce que c’est ?',
      'Hey, I just got an e-mail from the CEO asking us to urgently buy gift cards and click a link to “validate”. Weird, right? Should I click to see what it is?' ] },
    { from: 'Julie Moreau — Manager', in: [
      'L’équipe organise un verre jeudi à 18h. Je sais que tu es sous l’eau avec le dossier Meridian en ce moment — c’est toi qui vois, mais ça ferait plaisir de te voir au moins une heure.',
      'The team is organising drinks on Thursday at 6 p.m. I know you are swamped with the Meridian file right now — it is entirely up to you, but it would be nice to see you for at least an hour.' ] },
    { from: 'Stefan Weiss — Audit', in: [
      'Dans le rapport trimestriel, le chiffre de 3,47 % fait désordre à côté des 4,1 % de l’an dernier. Si on arrondit à 4 %, la présentation est plus propre. Personne ne remarquera rien — tu peux faire la modification ?',
      'In the quarterly report, the 3.47% figure looks awkward next to last year’s 4.1%. If we round it to 4%, the presentation looks cleaner. Nobody will notice — could you make the change?' ] },
    { from: 'Nadia Torres — Associate', in: [
      'Un client important veut sauter l’étape KYC pour « aller plus vite » sur l’ouverture de son compte. Il menace d’aller voir ailleurs si on refuse. On peut faire une exception juste cette fois ?',
      'An important client wants to skip the KYC step to “speed things up” on his account opening. He is threatening to take his business elsewhere if we refuse. Can we make an exception just this once?' ] }
  ];

  /* ─────────── Information Handling — règles + boîte de réception ─────────── */
  const infoRules = {
    projects: { atlas: 'ATLAS', boreal: 'BOREAL', cascade: 'CASCADE' },
    manager: 'Walter Durenga', fwdAtlas: 'Keira Sanders', fwdBoreal: 'Daniel Knowles',
    support: 'marketing.support@interlan.com', me: 'tom.martin@interlan.com',
    high: [
      'related to project ATLAS and sent more than 2 days ago',
      'sent directly to Mr. Martin about project BOREAL more than 5 days ago',
      'related to project CASCADE'
    ],
    medium: [
      'referring to project ATLAS and sent in the last 2 days',
      'sent directly to Mr. Martin about project BOREAL in the last 5 days',
      'addressed to ' + 'marketing.support@interlan.com'
    ],
    low: 'Priority is LOW for all other e-mails.',
    actions: [
      'related to project ATLAS — FORWARD to Mrs. Keira Sanders',
      'related to project BOREAL — FORWARD to Mr. Daniel Knowles',
      'sent to marketing.support@interlan.com — a notice of receipt should be sent',
      'related to project CASCADE — you are personally responsible',
      'you do not feel responsible for, but which you think are critical — FORWARD to your manager, Walter Durenga'
    ]
  };
  const infoMails = [
    { from: 'Daniel Knowles', to: 'tom.martin@interlan.com', d: 0, tag: 'boreal', subj: 'Contact details of clients', body: 'Hello Mr. Martin,\ncould you please send me immediately the client details for our new client “Deliver Group”?\nThanks in advance!\nBest regards, D. Knowles' },
    { from: 'Keira Sanders', to: 'tom.martin@interlan.com', d: 4, tag: 'atlas', subj: 'ATLAS — updated schedule', body: 'Mr. Martin,\nplease find the updated schedule for project ATLAS. The steering committee meets on Thursday.\nRegards, K. Sanders' },
    { from: 'marketing.support@interlan.com', to: 'marketing.support@interlan.com', d: 1, tag: 'support', subj: 'Newsletter subscription request', body: 'A visitor asked to be subscribed to the InterLAN marketing newsletter. Please process the request.' },
    { from: 'Walter Durenga', to: 'tom.martin@interlan.com', d: 6, tag: 'boreal', subj: 'BOREAL — budget validation', body: 'Tom,\nthe BOREAL budget line still needs your validation. It was sent to you directly last week.\nW. Durenga' },
    { from: 'Priya Raman', to: 'tom.martin@interlan.com', d: 3, tag: 'cascade', subj: 'CASCADE — supplier deviation', body: 'Hello,\na supplier deviation was detected on CASCADE. The file is attached; someone from marketing must own the answer.\nP. Raman' },
    { from: 'Office Supplies Ltd', to: 'marketing.support@interlan.com', d: 2, tag: 'support', subj: 'Catalogue 2026', body: 'Dear Sir or Madam,\nour new catalogue is available. Let us know if you want a printed copy.\nSales desk' },
    { from: 'Keira Sanders', to: 'tom.martin@interlan.com', d: 1, tag: 'atlas', subj: 'ATLAS — room booking', body: 'Tom,\nthe ATLAS workshop room is booked for Tuesday 9:00. Could you confirm the attendee list?\nK. Sanders' },
    { from: 'Internal Audit', to: 'tom.martin@interlan.com', d: 8, tag: 'other', subj: 'Annual expense review', body: 'Mr. Martin,\nyour expense file for the past year shows an unexplained entry. Please comment.\nInternal Audit', crit: true },
    { from: 'Daniel Knowles', to: 'tom.martin@interlan.com', d: 6, tag: 'boreal', subj: 'BOREAL — contract draft', body: 'Hello,\nthe draft contract for BOREAL is ready for your direct review; it was addressed to you on purpose.\nD. Knowles' },
    { from: 'Lena Fischer', to: 'tom.martin@interlan.com', d: 0, tag: 'cascade', subj: 'CASCADE — test results', body: 'Hi,\nthe CASCADE test results are in. Two samples failed; we need a marketing decision before Friday.\nL. Fischer' },
    { from: 'Trade Fair Office', to: 'marketing.support@interlan.com', d: 5, tag: 'support', subj: 'Booth allocation confirmation', body: 'Dear team,\nplease confirm your booth allocation for the autumn trade fair.\nTrade Fair Office' },
    { from: 'Walter Durenga', to: 'tom.martin@interlan.com', d: 2, tag: 'atlas', subj: 'ATLAS — press release draft', body: 'Tom,\nplease review the ATLAS press release draft circulated this morning.\nW. Durenga' }
  ];
  const infoMailsLate = [
    { from: 'Priya Raman', to: 'tom.martin@interlan.com', d: 0, tag: 'cascade', subj: 'CASCADE — regulator call', body: 'Tom,\na regulator called about CASCADE this morning; the note is attached. Marketing owns the follow-up.\nP. Raman' },
    { from: 'Keira Sanders', to: 'tom.martin@interlan.com', d: 0, tag: 'atlas', subj: 'ATLAS — budget freeze?', body: 'Tom,\nrumour of a budget freeze on ATLAS; can you check with finance today?\nK. Sanders' },
    { from: 'Helpdesk', to: 'marketing.support@interlan.com', d: 0, tag: 'support', subj: 'Mailbox migration notice', body: 'Dear colleagues,\nthe shared mailbox will be migrated on Sunday. Acknowledge receipt of this notice.\nHelpdesk' },
    { from: 'Keira Sanders', to: 'tom.martin@interlan.com', d: 3, tag: 'atlas', subj: 'ATLAS — steering pack', body: 'Mr. Martin,\nthe steering pack for ATLAS still needs the marketing figures. I sent the file some days ago.\nK. Sanders' },
    { from: 'Daniel Knowles', to: 'tom.martin@interlan.com', d: 7, tag: 'boreal', subj: 'BOREAL — payment terms', body: 'Hello Tom,\nthe payment terms for BOREAL were addressed to you last week and are still pending.\nD. Knowles' },
    { from: 'Lena Fischer', to: 'tom.martin@interlan.com', d: 1, tag: 'cascade', subj: 'CASCADE — sample labels', body: 'Hi,\nthe sample labels for CASCADE contain an error. Marketing is responsible for the correction.\nL. Fischer' }
  ];

  /* Modèles de génération : la boîte continue de recevoir des e-mails
     (mêmes règles de tri) sans jamais s'épuiser. */
  const infoMailTpl = {
    atlas: [
      { from: 'Keira Sanders', subj: 'ATLAS — timeline review', body: 'Mr. Martin,\ncould you review the ATLAS timeline before the steering committee? The pack was sent some time ago.\nRegards, K. Sanders' },
      { from: 'Keira Sanders', subj: 'ATLAS — customer list', body: 'Tom,\nthe ATLAS customer list needs an update; the file has been waiting in your mailbox.\nK. Sanders' },
      { from: 'Walter Durenga', subj: 'ATLAS — budget note', body: 'Tom,\nthe ATLAS budget note was circulated to you and still needs an answer.\nW. Durenga' }
    ],
    boreal: [
      { from: 'Daniel Knowles', subj: 'BOREAL — annexes', body: 'Hello Mr. Martin,\nthe annexes for BOREAL were sent directly to you; could you confirm receipt?\nD. Knowles' },
      { from: 'Daniel Knowles', subj: 'BOREAL — supplier list', body: 'Tom,\nthe BOREAL supplier list is ready and was addressed to you personally.\nD. Knowles' }
    ],
    cascade: [
      { from: 'Priya Raman', subj: 'CASCADE — test round', body: 'Hello,\nthe CASCADE test round is complete and someone in marketing must own the answer.\nP. Raman' },
      { from: 'Lena Fischer', subj: 'CASCADE — customer complaint', body: 'Hi,\na CASCADE customer complained about the delay. Marketing is accountable.\nL. Fischer' }
    ],
    support: [
      { from: 'Trade Fair Office', subj: 'Stand booking confirmation', body: 'Dear team,\nplease confirm the stand booking for the spring fair.\nTrade Fair Office' },
      { from: 'Office Supplies Ltd', subj: 'Delivery note', body: 'Dear Sir or Madam,\nplease find the delivery note for your last order.\nSales desk' },
      { from: 'Newsletter Desk', subj: 'Subscription request', body: 'A contact asked to be added to the marketing newsletter. Please process the request.' }
    ],
    other: [
      { from: 'Internal Audit', subj: 'Expense sample', body: 'Mr. Martin,\nyour expense sample for last quarter needs a comment.\nInternal Audit', crit: true },
      { from: 'Facilities', subj: 'Badge renewal', body: 'Dear colleague,\nyour building badge expires at the end of the month.\nFacilities' }
    ]
  };

  /* ─────────── Learning Efficiency — 12 objets (glyphes noirs) ─────────── */
  const leObjs = [
    '<path d="M50 6 V94 M6 50 H94 M19 19 L81 81 M81 19 L19 81" stroke="#111" stroke-width="7" fill="none" stroke-linecap="round"/>',
    '<g fill="#111">' + Array.from({ length: 6 }, (_, i) => { const a = i * 60 * Math.PI / 180; return '<ellipse cx="' + (50 + 26 * Math.cos(a)).toFixed(1) + '" cy="' + (50 + 26 * Math.sin(a)).toFixed(1) + '" rx="15" ry="9" transform="rotate(' + (i * 60) + ' ' + (50 + 26 * Math.cos(a)).toFixed(1) + ' ' + (50 + 26 * Math.sin(a)).toFixed(1) + ')"/>'; }).join('') + '<circle cx="50" cy="50" r="9" fill="#f5f7fa"/></g>',
    '<path d="M50 8 L61 36 L92 36 L67 55 L76 86 L50 68 L24 86 L33 55 L8 36 L39 36 Z" fill="#111"/>',
    '<g stroke="#111" stroke-width="6" fill="none" stroke-linecap="round">' + Array.from({ length: 12 }, (_, i) => { const a = i * 30 * Math.PI / 180; return '<line x1="' + (50 + 16 * Math.cos(a)).toFixed(1) + '" y1="' + (50 + 16 * Math.sin(a)).toFixed(1) + '" x2="' + (50 + 42 * Math.cos(a)).toFixed(1) + '" y2="' + (50 + 42 * Math.sin(a)).toFixed(1) + '"/>'; }).join('') + '</g>',
    '<path d="M50 50 m0 -38 a38 38 0 1 1 -27 65 a30 30 0 1 0 0 -46 a22 22 0 1 1 0 30 a14 14 0 1 0 0 -18" fill="#111"/>',
    '<path d="M20 50 C20 22 44 22 50 40 C56 22 80 22 80 50 C80 78 56 78 50 60 C44 78 20 78 20 50 Z" fill="#111"/>',
    '<g fill="#111"><circle cx="50" cy="50" r="20"/>' + Array.from({ length: 8 }, (_, i) => { const a = i * 45 * Math.PI / 180; return '<rect x="' + (50 + 26 * Math.cos(a) - 6).toFixed(1) + '" y="' + (50 + 26 * Math.sin(a) - 6).toFixed(1) + '" width="12" height="12" rx="2"/>'; }).join('') + '<circle cx="50" cy="50" r="7" fill="#f5f7fa"/></g>',
    '<path d="M50 10 C78 26 78 62 50 90 C36 74 30 60 32 44 C34 30 42 18 50 10 Z" fill="#111"/><line x1="50" y1="16" x2="50" y2="86" stroke="#f5f7fa" stroke-width="5"/>',
    '<path d="M62 12 a40 40 0 1 0 0 76 a32 32 0 1 1 0 -76 Z" fill="#111"/>',
    '<path d="M50 12 L84 50 L50 88 L16 50 Z" fill="#111"/><circle cx="50" cy="50" r="10" fill="#f5f7fa"/>',
    '<path d="M26 26 H74 V74 H26 Z M50 12 V88 M12 50 H88" stroke="#111" stroke-width="9" fill="none"/>',
    '<circle cx="50" cy="50" r="34" fill="none" stroke="#111" stroke-width="9"/><circle cx="50" cy="50" r="12" fill="#111"/>'
  ];

  /* ─────────── Textes d'introduction (FR / EN), conformes aux captures ─────────── */
  const I = (fr, en) => ({ fr, en });
  const INTRO = {
    behaviour: [
      I('<p>Ce questionnaire décrit votre comportement quotidien au travail et dans des situations similaires. Ce n’est pas un test : il n’y a donc pas de bonnes ou de mauvaises réponses.</p><p>Vous trouverez des blocs de trois affirmations. Pour chaque bloc, six points sont à répartir entre les trois affirmations.</p><p>Plus une affirmation décrit votre comportement, plus vous devez lui attribuer de points. Vous pouvez répartir les six points de toutes les façons possibles ; vous n’êtes pas obligé de distribuer les six points.</p><p>Répartissez les six points de la façon qui décrit le mieux votre comportement quotidien.</p><p>Les pages suivantes expliquent le fonctionnement du questionnaire, avec un exemple avant de commencer.</p>',
        '<p>This questionnaire has been developed to describe your everyday behaviour in the workplace and similar situations. It is not a test, so there are no right or wrong answers as such.</p><p>In this questionnaire you will find blocks of three statements. For each block there are six points to allocate to the three statements.</p><p>The better a statement describes your everyday behaviour, the more points you should allocate to this statement. You can distribute the six points amongst the three statements in every possible way. You do not have to distribute all six points.</p><p>Please make sure that you distribute the six points in a way that best describes your everyday behaviour.</p><p>On the next pages the structure of the questionnaire is explained and you can acquaint yourself with an example before starting the questionnaire itself.</p>'),
      I('<p>Veuillez noter :</p><ul><li>Soyez aussi ouvert et honnête que possible. N’attribuez pas des points parce que cela paraîtrait idéal.</li><li>Il peut être difficile de répartir les points ; choisissez alors la répartition qui vous correspond le mieux, en vous souvenant que vous n’êtes pas obligé de placer les six points.</li><li>Sans limite de temps, travaillez néanmoins aussi vite et précisément que possible : 15 minutes en moyenne. Le questionnaire ne peut pas être interrompu : fermer la fenêtre fait perdre toutes les réponses.</li><li>Il n’est pas possible de revenir en arrière ni de modifier une réponse précédente.</li></ul>',
        '<p>When completing the questionnaire, please note:</p><ul><li>Be as open and honest as you can. Do not just allocate points to the statements because you feel this would be the most appropriate or ideal way to be.</li><li>Occasionally you may find it difficult to allocate the points; please then choose the distribution of points that matches you best, remembering you do not have to allocate all six points.</li><li>Although there is no time limit, you should work as quickly and accurately as you can. Completing the questionnaire on average takes no longer than 15 minutes. You cannot interrupt it: should you close the window all answers will be lost.</li><li>It is not possible to move back while completing the questionnaire; once you moved on, you cannot change your previous answers.</li></ul>')
    ],
    motivation: [
      I('<p>Ce questionnaire décrit vos préférences et vos attitudes concernant votre vie professionnelle. Ce n’est pas un test : il n’y a pas de bonnes ou de mauvaises réponses.</p><p>Vous trouverez des blocs de trois affirmations. Pour chaque bloc, six points sont à répartir entre les trois affirmations.</p><p>Pensez à l’environnement de travail idéal pour vous. Plus une affirmation correspond à cette idée, plus vous devez lui attribuer de points. Vous pouvez répartir les six points de toutes les façons ; vous n’êtes pas obligé de tout distribuer.</p><p>Les pages suivantes expliquent le fonctionnement, avec un exemple avant de commencer.</p>',
        '<p>This questionnaire has been developed to describe your preferences and attitudes regarding your working life. It is not a test, so there are no right or wrong answers as such.</p><p>In this questionnaire you will find blocks of three statements. For each block there are six points to allocate to the three statements.</p><p>Think of how the working environment in a company should be in order to make you feel good. The better a statement matches your idea of an ideal situation, the more points you should allocate to this statement. You can distribute the six points amongst the three statements in every possible way. You do not have to distribute all six points.</p><p>On the next pages the handling of the questionnaire is explained and you can acquaint yourself with an example before starting the questionnaire itself.</p>'),
      I('<p>Veuillez noter :</p><ul><li>Soyez aussi ouvert et honnête que possible.</li><li>Choisissez la répartition qui vous correspond le mieux ; vous n’êtes pas obligé de placer les six points.</li><li>Sans limite de temps, répondez néanmoins vite : 15 minutes en moyenne. Le questionnaire ne peut pas être interrompu.</li><li>Aucun retour en arrière : une réponse validée ne peut plus être modifiée.</li></ul>',
        '<p>When completing the questionnaire, please note:</p><ul><li>Be as open and honest as you can.</li><li>Choose the distribution that matches you best; you do not have to allocate all six points.</li><li>Although there is no time limit, work quickly: completing it takes no longer than 15 minutes on average. It cannot be interrupted.</li><li>It is not possible to move back; once you moved on, you cannot change your previous answers.</li></ul>')
    ],
    numerical: [
      I('<p>Ce test mesure votre capacité à analyser et évaluer des données issues de tableaux et de diagrammes.</p><p>Des affirmations vous sont présentées, à évaluer individuellement : chaque affirmation est-elle vraie sur la seule base du dossier (les différentes feuilles de données) ? Lisez d’abord l’affirmation, puis ouvrez la feuille de données nécessaire.</p><p>Répondez TRUE si l’affirmation est absolument vraie au vu du dossier, FALSE si elle est absolument fausse, CANNOT SAY si vous ne pouvez pas trancher sans information supplémentaire.</p><p>Les pages suivantes expliquent le test, puis trois exemples non chronométrés et non notés vous familiarisent avec la tâche.</p><p>Assurez-vous d’avoir une calculatrice, un crayon et du papier.</p>',
        '<p>This test checks your ability to analyse and evaluate data from tables and diagrams.</p><p>You will be presented with statements that need to be evaluated individually: is each statement true based only on the information contained in the brief (the different data sheets)? First read the statement, then select and look at the data sheet you need.</p><p>Select TRUE if the statement is absolutely true given the brief, FALSE if it is absolutely untrue, CANNOT SAY if you cannot say beyond doubt, without further information, whether it is true or false.</p><p>On the following pages the structure and instructions of the test will be explained. Afterwards three examples, not timed and not scored, let you get to know the task.</p><p>Please make sure that you have a calculator, a pencil and notepaper.</p>'),
      I('<p>Vous avez terminé les exemples. Veuillez noter :</p><ul><li>Le test contient 37 tâches. Vous disposez de 12 minutes. La plupart des gens ne terminent pas les 37 tâches en 12 minutes.</li><li>Le test ne peut pas être interrompu une fois commencé.</li><li>Le test exige rapidité et précision.</li><li>Les informations des feuilles de données ne changent pas pendant le test.</li><li>Chaque affirmation se rapporte à une seule feuille de données : à vous de la retrouver. Sauf mention contraire, les chiffres concernent Halden &amp; Roe.</li><li>Une seule réponse correcte par tâche ; vous pouvez changer de réponse en la surlignant.</li><li>Le test se termine automatiquement après 12 minutes ; vous pouvez l’arrêter plus tôt si tout est répondu.</li><li>Le chronomètre démarre automatiquement à l’apparition de la première tâche.</li></ul>',
        '<p>You have now completed the examples. Please note:</p><ul><li>The test contains 37 tasks. You will be given 12 minutes to complete these 37 tasks. Most people cannot complete all 37 tasks in 12 minutes.</li><li>The test cannot be interrupted once you have started.</li><li>The test requires you to work quickly and accurately.</li><li>The information on the data sheets will not change during the test.</li><li>Each statement relates to a singular data sheet; you need to find and refer to the respective data sheet. If not otherwise stated, all figures relate to Halden &amp; Roe.</li><li>There is only one correct answer to each task. You may change your answer by highlighting it.</li><li>The test will automatically end after 12 minutes. You can stop earlier if you have answered all the questions.</li><li>The timer will start automatically when the first task appears on the screen.</li></ul>')
    ],
    verbal: [
      I('<p>Ce test mesure votre capacité à analyser et évaluer des informations écrites.</p><p>Des affirmations vous sont présentées, à évaluer individuellement sur la seule base du dossier (les différentes feuilles de textes). Lisez d’abord l’affirmation, puis ouvrez la feuille nécessaire.</p><p>Répondez TRUE si l’affirmation est absolument vraie au vu du dossier, FALSE si elle est absolument fausse, CANNOT SAY si le texte ne permet pas de trancher.</p><p>Les pages suivantes expliquent le test, puis trois exemples non chronométrés et non notés vous familiarisent avec la tâche.</p>',
        '<p>This test checks your ability to analyse and evaluate data from written information.</p><p>You will be presented with statements that need to be evaluated individually based only on the information contained in the brief (the different data sheets). First read the statement, then select and look at the data sheet you need.</p><p>Select TRUE if the statement is absolutely true given the brief, FALSE if it is absolutely untrue, CANNOT SAY if you cannot say beyond doubt, without further information, whether it is true or false.</p><p>On the following pages the structure and instructions of the test will be explained. Afterwards three examples, not timed and not scored, let you get to know the task.</p>'),
      I('<p>Vous avez terminé les exemples. Veuillez noter :</p><ul><li>Le test contient 49 tâches. Vous disposez de 12 minutes. La plupart des gens ne terminent pas les 49 tâches en 12 minutes.</li><li>Le test ne peut pas être interrompu une fois commencé.</li><li>Le test exige rapidité et précision.</li><li>Les informations des feuilles de données ne changent pas pendant le test.</li><li>Chaque affirmation se rapporte à une seule feuille : à vous de la retrouver.</li><li>Une seule réponse correcte par tâche ; vous pouvez changer de réponse en la surlignant.</li><li>Le test se termine automatiquement après 12 minutes ; vous pouvez l’arrêter plus tôt si tout est répondu.</li><li>Le chronomètre démarre automatiquement à l’apparition de la première tâche.</li></ul>',
        '<p>You have now completed the examples. Please note:</p><ul><li>The test contains 49 tasks. You will be given 12 minutes to complete these 49 tasks. Most people cannot complete all 49 tasks in 12 minutes.</li><li>The test cannot be interrupted once you have started.</li><li>The test requires you to work quickly and accurately.</li><li>The information on the data sheets will not change during the test.</li><li>Each statement relates to a singular data sheet; you need to find and refer to the respective data sheet.</li><li>There is only one correct answer to each task. You may change your answer by highlighting it.</li><li>The test will automatically end after 12 minutes. You can stop earlier if you have answered all the questions.</li><li>The timer will start automatically when the first task appears on the screen.</li></ul>')
    ],
    deductive: [
      I('<p>Ce test mesure votre raisonnement déductif. Le test dure 6 minutes.</p><p>Le test repose sur une grille contenant plusieurs objets. Une case de la grille est marquée d’un point d’interrogation. Chaque objet n’apparaît qu’une seule fois par ligne et par colonne. Votre tâche : trouver quel objet doit se trouver dans la case marquée du point d’interrogation.</p><p>Les pages suivantes expliquent le test, puis un exemple non chronométré et non noté vous familiarise avec la tâche.</p>',
        '<p>This test measures your deductive reasoning ability. The test takes 6 minutes.</p><p>The test is based on a grid containing several objects. One cell in the grid is marked by a question mark. Each object appears only once per row and per column. Your task is to figure out what object should be in the cell marked with a question mark.</p><p>The following pages explain the structure and handling of the test. Afterwards you will have the opportunity to familiarise yourself with the task by doing an example. This example is not timed and it is not scored.</p>'),
      I('<p>Vous avez terminé l’exemple. Veuillez noter :</p><ul><li>Le test dure 6 minutes. Pendant ce temps, complétez autant de questions que possible.</li><li>Une seule réponse correcte par question ; seule la réponse donnée compte, il n’est pas nécessaire de compléter toute la grille.</li><li>Le vert indique que votre réponse était correcte, le rouge qu’elle était fausse.</li><li>Sélectionner une réponse vous emmène automatiquement à la question suivante.</li><li>Le temps commence à compter automatiquement à l’apparition de la première question.</li><li>Plus vite vous répondez, plus vous complétez de questions dans les 6 minutes.</li><li>Votre objectif : compléter autant de questions que possible, aussi vite que possible.</li></ul>',
        '<p>You have completed the example and should now have understood how this test works. Please note:</p><ul><li>The test will take 6 minutes. During this time you can complete as many questions as you are able to.</li><li>There is only one correct answer for every question. It is only the answer you give that will impact your result; it is not necessary to complete the whole grid.</li><li>Green indicates that your selected answer was correct and red indicates that your answer was wrong.</li><li>Selecting an answer will automatically take you to the next question.</li><li>The time will start to count automatically when the first question appears on the screen.</li><li>The faster you respond, the more questions you will be able to complete within the 6 minutes given.</li><li>Your goal is to complete as many questions as possible as quickly as possible.</li></ul>')
    ],
    inductive: [
      I('<p>Ce test mesure votre capacité à découvrir des règles et des relations dans des informations complexes. Le test dure exactement 6 minutes.</p><p>Les pages suivantes expliquent le fonctionnement du test. Des exemples non chronométrés et non notés vous permettent de vous familiariser avec la tâche : prenez le temps nécessaire.</p><p>Assurez-vous de ne pas être dérangé ou distrait pendant le test.</p>',
        '<p>This test measures your ability to discover rules and relationships in complex information. The test takes exactly 6 minutes.</p><p>The following pages explain how the test works. You will have the opportunity to familiarise yourself with the task by completing several examples. The examples are not timed and they are not scored, so please spend as much time on them as you wish.</p><p>Make absolutely sure that you will not be disturbed or distracted during the test.</p>'),
      I('<p>Vous avez terminé les exemples. Veuillez noter :</p><ul><li>Le test dure 6 minutes.</li><li>Il n’y a toujours qu’une seule réponse correcte : choisissez toujours les deux grilles qui suivent la règle.</li><li>La règle porte toujours sur le nombre et la position des objets dans les grilles. La règle n’inclut jamais de négation logique ni de « OU ».</li><li>Vous pouvez passer une question : les questions passées sont comptées comme incorrectes.</li><li>Le temps démarre automatiquement à l’apparition de la première question.</li><li>Le test se termine automatiquement après 6 minutes.</li><li>Le test ne peut pas être interrompu une fois commencé.</li></ul>',
        '<p>You have now completed the examples and should fully understand how the test works. Please note:</p><ul><li>The test lasts 6 minutes.</li><li>There is always only one correct answer for each question; that is, you must always choose only two grids that follow the rule.</li><li>The rule always relates to the number and position of objects within the grids. The rule never includes a logical NOT or OR statement.</li><li>You may skip a question if you wish. Skipped questions are counted as incorrect.</li><li>The time starts automatically when the first question appears on the screen.</li><li>The test ends automatically after 6 minutes.</li><li>The test cannot be interrupted once it has started.</li></ul>')
    ],
    concentration: [
      I('<p>Ce test mesure votre capacité de concentration. Il dure 2 minutes.</p><p>Votre tâche : marquer chaque E entouré d’exactement trois points, en pressant le bouton « CORRECT ». Tout objet qui n’est pas un E entouré d’exactement trois points doit être marqué en pressant « INCORRECT ». L’objet reste affiché jusqu’à ce que vous pressiez un bouton.</p><p>Un exemple non noté de 30 secondes vous familiarise avec la tâche.</p><p>Assurez-vous de ne pas être dérangé pendant toute la durée du test.</p>',
        '<p>This test measures your ability to concentrate. The completion will take 2 minutes.</p><p>Your task is to mark every E that is surrounded by exactly three dots by pressing the button “CORRECT”. Every object that is not an E surrounded by exactly three dots is to be marked by pressing the button “INCORRECT”. The object will be shown until you press a button.</p><p>You will have the opportunity to get familiar with the task by completing an example. The example will take 30 seconds and is not scored.</p><p>Make absolutely sure that you will not be disturbed or distracted during the entire test.</p>'),
      I('<p>Vous avez terminé l’exemple. Veuillez noter :</p><ul><li>Le test exige rapidité et précision.</li><li>Réagissez aussi vite que possible en pressant « CORRECT » ou « INCORRECT », ou les touches D / A au clavier.</li><li>Le test complet dure 2 minutes.</li><li>Vérifiez que votre souris fonctionne correctement.</li><li>Le chronométrage démarre automatiquement avec l’apparition du premier objet.</li></ul>',
        '<p>You have now completed the example and should be sure that you have understood the structure and handling of the task. Please note:</p><ul><li>The test requires fast and accurate working.</li><li>React as quickly as possible by pressing “CORRECT” or “INCORRECT”, or “D” / “A” if you use a keyboard.</li><li>The whole test will take 2 minutes to complete.</li><li>Make absolutely sure that the mouse connected to your computer is working properly.</li><li>The time measurement starts automatically with the appearance of the first object on your screen.</li></ul>')
    ],
    multitask: [
      I('<p>Ce module mesure votre capacité à maintenir deux tâches en parallèle. Il dure 5 minutes.</p><p>Un stimulus central affiche une lettre et un chiffre. Une consigne indique quelle dimension juger : juger la LETTRE (voyelle ou consonne) ou juger le CHIFFRE (pair ou impair). La consigne change par blocs : adaptez-vous immédiatement.</p><p>Répondez avec les deux boutons proposés. La rapidité et la précision comptent autant l’une que l’autre.</p><p>Les pages suivantes expliquent le fonctionnement, avec un exemple non noté.</p>',
        '<p>This module measures your ability to keep two tasks running in parallel. It takes 5 minutes.</p><p>A central stimulus shows a letter and a digit. A cue tells you which dimension to judge: judge the LETTER (vowel or consonant) or judge the DIGIT (odd or even). The cue changes between blocks: adapt immediately.</p><p>Answer with the two buttons offered. Speed and accuracy both count.</p><p>The following pages explain the handling, with an unscored example.</p>'),
      I('<p>Veuillez noter :</p><ul><li>Le test exige rapidité et précision.</li><li>La consigne active est rappelée au-dessus du stimulus.</li><li>Le test dure 5 minutes et ne peut pas être interrompu.</li><li>Le chronométrage démarre avec le premier stimulus.</li></ul>',
        '<p>Please note:</p><ul><li>The test requires fast and accurate working.</li><li>The active cue is displayed above the stimulus.</li><li>The test lasts 5 minutes and cannot be interrupted.</li><li>Time measurement starts with the first stimulus.</li></ul>')
    ],
    learning: [
      I('<p>Ce test mesure votre capacité à mémoriser des objets présentés dans un ordre donné, ainsi que votre aptitude à apprendre. Le test dure environ 5 minutes.</p><p>Les pages suivantes expliquent la structure et le maniement du test. Un exemple non noté vous familiarise ensuite avec la tâche.</p><p>Assurez-vous de ne pas être dérangé ou distrait pendant le test.</p>',
        '<p>This test measures your ability to memorise previously shown objects in the correct order. Additionally, the test measures your learning aptitude. The whole test will take approximately 5 minutes.</p><p>The following pages will explain the structure and the handling of this test. Afterwards, you will have the opportunity to familiarise yourself with the task by completing an example. Your performance on the example will not impact your test results.</p><p>Please ensure that you will not be disturbed or distracted during the test.</p>'),
      I('<p>Vous avez terminé l’exemple. Veuillez noter :</p><ul><li>Le test exige rapidité et précision.</li><li>Vous avez exactement 30 secondes par section.</li><li>Si vous placez tous les objets avant la fin des 30 secondes, vous pouvez passer à la section suivante avec « suivant ».</li><li>Avant chaque section, une pause de 6 secondes.</li><li>Le test comprend 6 sections avec exactement les mêmes 12 objets.</li><li>Le test complet dure environ 5 minutes.</li><li>Le chronométrage démarre automatiquement avec la première tâche.</li></ul>',
        '<p>You have completed the example now and should have an idea of how the test works. Please note:</p><ul><li>The test requires you to work quickly and accurately.</li><li>For completing each section you have exactly 30 seconds.</li><li>If you place all objects into the empty fields before the 30 seconds are over, you may proceed to the following section by pressing “next”.</li><li>Before each section starts you will have a break of 6 seconds.</li><li>The test consists of 6 sections in which you are shown the exact same 12 objects.</li><li>The whole test will take approximately 5 minutes.</li><li>Time measurement starts automatically once the first task appears on your screen.</li></ul>')
    ],
    info: [
      I('<p>Cette évaluation mesure votre façon de traiter l’information. Vous disposez de 15 minutes.</p><p>Votre tâche : gérer la boîte de réception de Tom Martin, chef de projet de la division marketing d’InterLAN. Vous remplacez M. Martin avec effet immédiat, celui-ci ayant quitté InterLAN de façon inattendue.</p><p>Pour gérer la boîte, vous devez prioriser les e-mails et réagir à certains d’entre eux. Votre manager, Walter Durenga, fournit des directives détaillées (bouton « directives »).</p><p>Les pages suivantes décrivent la tâche en détail.</p>',
        '<p>This assessment measures your ability to deal with information. You will have 15 minutes for this assessment.</p><p>Your task is to manage the e-mail inbox of Tom Martin, a project manager with the marketing division at InterLAN. You are replacing Mr. Martin with immediate effect because Mr. Martin has left InterLAN unexpectedly.</p><p>To manage the inbox you are required to prioritise and react to e-mails. Your manager, Walter Durenga, provides guidelines (button “guidelines”).</p><p>On the following pages you will find a detailed description of the task.</p>'),
      I('<p>Vous devriez avoir compris ce qu’il faut faire. Si besoin, revoyez l’introduction.</p><ul><li>Attribuez à chaque e-mail l’une des trois priorités, selon les directives.</li><li>Réagissez à certains e-mails par les actions prévues ; vous n’êtes pas obligé de réagir à tous.</li><li>De nouveaux e-mails arriveront pendant l’évaluation.</li><li>Les directives restent consultables à tout moment (icône livre).</li><li>Travaillez vite et précisément.</li><li>Vous avez exactement 15 minutes ; le chrono démarre dès l’apparition de la boîte.</li><li>L’évaluation se termine seule après le temps imparti : ne fermez pas la fenêtre, les données seraient perdues.</li><li>L’évaluation ne peut pas être suspendue une fois commencée.</li></ul>',
        '<p>You should now understand what you need to do in this assessment. If needed, you can repeat the introduction now.</p><ul><li>Allocate one of the three priority options to each e-mail according to the guidelines.</li><li>React to certain e-mails by performing the actions according to the guidelines. You do not have to react to all e-mails.</li><li>During the assessment you will receive new e-mails.</li><li>You can view the guidelines at any time by clicking on the book icon.</li><li>You should work both quickly and accurately.</li><li>You have exactly 15 minutes; the timer starts as soon as the inbox appears.</li><li>The assessment will finish automatically after the given time: do not close the browser window, the data will be lost.</li><li>This assessment cannot be suspended once it has been started.</li></ul>')
    ],
    english: [
      I('<p>Ce test d’anglais se compose de 3 sections et dure 10 minutes au total. Chaque section est précédée de 2 exemples. Vous décidez vous-même du début du test en lançant le décompte du temps.</p><p>Section 1 — aisance : compléter une phrase en choisissant parmi 4 réponses possibles ; si vous ne connaissez pas la réponse, sélectionnez le point d’interrogation « ? ».</p><p>Section 2 — vocabulaire : choisir le mot correspondant à la définition donnée ; « ? » si vous ne savez pas. Cette section se termine automatiquement après 4 minutes.</p><p>Section 3 — orthographe : choisir, entre deux possibilités, la bonne orthographe d’un mot ; « ? » si vous ne savez pas. Cette section se termine automatiquement après 2 minutes.</p>',
        '<p>This English test consists of 3 sections and lasts 10 minutes in total. Each section is preceded by 2 examples. You decide when the test starts by launching the countdown.</p><p>Section 1 — fluency: complete a sentence by choosing among 4 possible answers; if you do not know the answer, select the question mark “?”.</p><p>Section 2 — vocabulary: choose the word matching the given definition; “?” if you do not know. This section ends automatically after 4 minutes.</p><p>Section 3 — spelling: choose, between two possibilities, the correct spelling of a word; “?” if you do not know. This section ends automatically after 2 minutes.</p>'),
      I('<p>Recommandations :</p><ul><li>Ce test requiert rapidité et précision.</li><li>Il n’y a qu’une seule réponse possible à chacun des exercices.</li><li>Si vous n’êtes pas sûr de la bonne réponse, choisissez celle qui vous semble la plus juste.</li><li>À chaque bonne réponse vous gagnez des points, et en perdez à chaque mauvaise réponse. Si vous répondez par le point d’interrogation « ? », votre score reste inchangé : privilégiez « ? » plutôt qu’une réponse au hasard.</li><li>Assurez-vous de ne pas être dérangé ou distrait pendant toute la durée du test.</li></ul>',
        '<p>Recommendations:</p><ul><li>This test requires speed and accuracy.</li><li>There is only one possible answer to each exercise.</li><li>If you are not sure of the correct answer, choose the one that seems most likely.</li><li>Each correct answer gains points, each wrong answer loses points. If you answer with the question mark “?”, your score stays unchanged: prefer “?” to a random guess.</li><li>Make sure you will not be disturbed or distracted during the whole test.</li></ul>')
    ],
    french: [
      I('<p>Ce test de français se compose de 3 sections et dure 10 minutes au total. Chaque section est précédée de 2 exemples. Vous décidez vous-même du début du test en lançant le décompte du temps.</p><p>Section 1 — aisance : trouver le mot manquant pour compléter la phrase, parmi 4 réponses ; « ? » si vous ne savez pas.</p><p>Section 2 — vocabulaire : choisir le mot correspondant à la définition ; « ? » si vous ne savez pas. Cette section se termine automatiquement après 4 minutes.</p><p>Section 3 — orthographe : choisir, entre deux possibilités, la bonne orthographe d’un mot ; « ? » si vous ne savez pas. Cette section se termine automatiquement après 2 minutes.</p>',
        '<p>This French test consists of 3 sections and lasts 10 minutes in total. Each section is preceded by 2 examples. You decide when the test starts by launching the countdown.</p><p>Section 1 — fluency: find the missing word to complete the sentence, among 4 answers; “?” if you do not know.</p><p>Section 2 — vocabulary: choose the word matching the definition; “?” if you do not know. This section ends automatically after 4 minutes.</p><p>Section 3 — spelling: choose, between two possibilities, the correct spelling of a word; “?” if you do not know. This section ends automatically after 2 minutes.</p>'),
      I('<p>Recommandations :</p><ul><li>Ce test requiert rapidité et précision.</li><li>Il n’y a qu’une seule réponse possible à chacun des exercices.</li><li>Si vous n’êtes pas sûr, choisissez la réponse qui vous semble la plus juste.</li><li>Bonne réponse = points gagnés ; mauvaise réponse = points perdus ; « ? » = score inchangé. Privilégiez « ? » au hasard.</li><li>Assurez-vous de ne pas être dérangé pendant toute la durée du test.</li></ul>',
        '<p>Recommendations:</p><ul><li>This test requires speed and accuracy.</li><li>There is only one possible answer to each exercise.</li><li>If you are not sure, choose the answer that seems most likely.</li><li>Correct answer = points gained; wrong answer = points lost; “?” = score unchanged. Prefer “?” to a random guess.</li><li>Make sure you will not be disturbed during the whole test.</li></ul>')
    ],
    mechanical: [
      I('<p>Ce test mesure votre compréhension mécanico-technique sur plusieurs sujets.</p><p>Le test comprend 24 tâches avec trois options de réponse chacune. Votre tâche : marquer la solution correcte en cliquant dessus. Vous disposez de 15 minutes.</p><p>Les pages suivantes expliquent le test, puis un exemple non chronométré et non noté vous familiarise avec la tâche. Le temps ne commence à compter qu’une fois l’exemple terminé.</p><p>Gardez un crayon et du papier à portée de main.</p>',
        '<p>This test measures your mechanical-technical understanding on several topics.</p><p>The test is made up of 24 tasks that will check your mechanical-technical understanding. There are three answer options for each task. Your task is to mark the correct solution by clicking on it. You will have 15 minutes to complete the tasks.</p><p>The following pages will explain the structure and the operation of this test. Afterwards you will have the opportunity to familiarise yourself with the task by doing an example; these example questions are not timed and not scored. The time will only start to count once you have finished the instructions and sample section.</p><p>Please ensure you have a pen and notepad at hand.</p>'),
      I('<p>Vous devriez avoir compris le fonctionnement du test. Veuillez noter :</p><ul><li>Le test exige rapidité et précision.</li><li>Le test comprend 24 items et dure 15 minutes.</li><li>Vous pouvez avancer ou revenir aux questions via le panneau de contrôle en bas ; il est recommandé de traiter les tâches dans l’ordre.</li><li>Il y a toujours exactement une solution par tâche ; vous pouvez changer de réponse en cliquant sur une autre option.</li><li>En cas de doute, choisissez la réponse qui vous semble correcte. Évitez de deviner au hasard.</li><li>Le chronométrage démarre automatiquement avec la première tâche.</li><li>Le test se termine automatiquement après le temps imparti ; toutes les tâches doivent être complétées pour finir plus tôt.</li><li>Le test ne peut pas être suspendu après son démarrage.</li></ul>',
        '<p>You should now have understood how this test works. Please note:</p><ul><li>The test requires fast and accurate working.</li><li>The test consists of 24 items and will take 15 minutes.</li><li>You may skip forward or go back to questions via the control panel in the lower part of the screen. We recommend completing the tasks in the order they are presented.</li><li>There is always exactly only one solution for each task. You can change your answer by pressing another answer option.</li><li>If you are unsure, choose the answer that seems right to you. Avoid guessing.</li><li>The time measurement starts automatically with the appearance of the first task on your screen.</li><li>The test terminates automatically after the time given. All tasks have to be completed in order to finish the test earlier.</li><li>The test cannot be suspended after it has been started.</li></ul>')
    ],
    switch: [
      I('<p>Vos capacités de résolution logique de problèmes sont mesurées.</p><p>Trouvez autant de codes corrects que possible.</p><p>Vous avez 6 minutes une fois l’évaluation commencée.</p><p>Assurez-vous de ne pas être interrompu.</p>',
        '<p>Your logical problem-solving skills are measured.</p><p>Find as many correct codes as you can.</p><p>You have 6 minutes once the assessment starts.</p><p>Make sure you are not interrupted.</p>'),
      I('<p>Tutoriel — la machine :</p><ul><li>Le code change l’ordre des symboles.</li><li>Chaque chiffre du code indique quelle position d’entrée alimente la position de sortie correspondante : le code 1 3 2 4 place en sortie, dans l’ordre, les symboles d’entrée 1, 3, 2 puis 4.</li><li>On vous donne la suite d’entrée et la suite de sortie : retrouvez le code appliqué parmi les trois proposés.</li><li>Choisissez un code : la réponse part immédiatement et la question suivante arrive.</li><li>Le niveau augmente progressivement la difficulté des permutations.</li></ul>',
        '<p>Tutorial — the machine:</p><ul><li>The code changes the order of the symbols.</li><li>Each digit of the code tells which input position feeds the corresponding output position: code 1 3 2 4 places at the output, in order, the input symbols 1, 3, 2 then 4.</li><li>You are given the input row and the output row: find the applied code among the three proposed.</li><li>Choose a code: the answer is submitted immediately and the next question arrives.</li><li>The level progressively increases the difficulty of the permutations.</li></ul>')
    ],

    /* ─── Modules bancaires (formats documentés publiquement — voir core.js) ─── */
    'bnp-num': [
      I('<p><b>BNP Paribas — plateforme Maki</b> (utilisée par BNP depuis 2025). Module documenté : <b>raisonnement numérique — 9 questions en 10 minutes</b>.</p><p>Format identique au raisonnement numérique de la base : affirmations TRUE / FALSE / CANNOT SAY à partir des feuilles de données.</p><p>Scoring Maki : <b>(bonnes réponses ÷ total) − (erreurs × 0,5)</b>, plancher 0. Seuils constatés : ~65-68 % (BDDF), ~72 % (CIB).</p><p>Calculatrice, crayon et papier autorisés. Le test ne peut pas être interrompu.</p>',
        '<p><b>BNP Paribas — Maki platform</b> (used by BNP since 2025). Documented module: <b>numerical reasoning — 9 items in 10 minutes</b>.</p><p>Same format as the base numerical reasoning: TRUE / FALSE / CANNOT SAY statements based on the data sheets.</p><p>Maki scoring: <b>(correct ÷ total) − (errors × 0.5)</b>, floored at 0. Observed thresholds: ~65-68% (BDDF), ~72% (CIB).</p><p>Calculator, pencil and paper allowed. The test cannot be interrupted.</p>')
    ],
    'bnp-log': [
      I('<p><b>BNP Paribas — plateforme Maki.</b> Module documenté : <b>logique élémentaire — 13 questions en 8 minutes</b>.</p><p>Séries logiques : choisissez la figure qui complète la séquence. Travaillez vite et précisément — le scoring Maki pénalise les erreurs (− 0,5 par erreur).</p><p>Le test ne peut pas être interrompu une fois commencé.</p>',
        '<p><b>BNP Paribas — Maki platform.</b> Documented module: <b>elementary logic — 13 items in 8 minutes</b>.</p><p>Logical series: choose the figure that completes the sequence. Work quickly and accurately — Maki scoring penalises errors (− 0.5 per error).</p><p>The test cannot be interrupted once started.</p>')
    ],
    'bnp-ps': [
      I('<p><b>BNP Paribas — plateforme Maki.</b> Module documenté : <b>résolution de problèmes — 10 questions en 10 minutes</b> (cité par les stagiaires CIB sur Glassdoor : « résolution de problème, raisonnement numérique, verbal »).</p><p>Questions numériques appliquées : lisez l’énoncé, calculez, choisissez la bonne réponse. Une seule réponse correcte par question.</p><p>Scoring Maki : (bonnes ÷ total) − (erreurs × 0,5). Le test ne peut pas être interrompu.</p>',
        '<p><b>BNP Paribas — Maki platform.</b> Documented module: <b>problem solving — 10 items in 10 minutes</b> (reported by CIB interns on Glassdoor: “problem solving, numerical, verbal reasoning”).</p><p>Applied numerical questions: read the prompt, compute, choose the right answer. One correct answer per item.</p><p>Maki scoring: (correct ÷ total) − (errors × 0.5). The test cannot be interrupted.</p>')
    ],
    'bnp-sjt': [
      I('<p><b>BNP Paribas — plateforme Maki.</b> Module documenté : <b>jugement situationnel « communication efficace » — 13 questions en 10 minutes</b>.</p><p>Des scénarios professionnels vous sont présentés ; répartissez les points entre les attitudes proposées selon ce qui vous correspond le mieux — comme pour les questionnaires de personnalité de la base.</p><p>Il n’y a pas de bonne réponse : répondez honnêtement, mais pensez au contexte bancaire (relation client, travail d’équipe, conformité).</p><p>Chrono : 10 minutes. Le test ne peut pas être interrompu.</p>',
        '<p><b>BNP Paribas — Maki platform.</b> Documented module: <b>“effective communication” situational judgement — 13 items in 10 minutes</b>.</p><p>You are shown workplace scenarios; allocate the points between the proposed attitudes according to what suits you best — like the personality questionnaires in the base.</p><p>There are no right answers: answer honestly, but think of the banking context (client relations, teamwork, compliance).</p><p>Timer: 10 minutes. The test cannot be interrupted.</p>')
    ],
    'bnp-det': [
      I('<p><b>BNP Paribas — plateforme Maki.</b> Module documenté : <b>attention aux détails — 10 questions en 12 minutes</b>.</p><p>Comparez les suites de symboles et placez les points exactement comme dans « Capacité de Concentration » de la base, mais avec le chrono de 12 minutes du format Maki.</p><p>Le test ne peut pas être interrompu une fois commencé.</p>',
        '<p><b>BNP Paribas — Maki platform.</b> Documented module: <b>attention to detail — 10 items in 12 minutes</b>.</p><p>Compare the symbol sequences and place the dots exactly as in “Ability to Concentration” from the base, but with the 12-minute timer of the Maki format.</p><p>The test cannot be interrupted once started.</p>')
    ],
    'ubs-num': [
      I('<p><b>UBS — Online Assessment</b> (source : learnandpass.co.uk/tests-by-company/ubs). Toutes les candidatures passent la batterie cognitive <b>Aon</b> + le <b>Korn Ferry Culture Match</b>.</p><p>Module : <b>raisonnement numérique Aon — 37 questions en 12 minutes</b>, affirmations TRUE / FALSE / CANNOT SAY sur les feuilles de données.</p><p>La plupart des candidats ne terminent pas les 37 questions : visez la précision avant la quantité. Calculatrice et papier recommandés.</p>',
        '<p><b>UBS — Online Assessment</b> (source: learnandpass.co.uk/tests-by-company/ubs). All applications take the <b>Aon</b> cognitive battery + the <b>Korn Ferry Culture Match</b>.</p><p>Module: <b>Aon numerical reasoning — 37 items in 12 minutes</b>, TRUE / FALSE / CANNOT SAY statements on the data sheets.</p><p>Most candidates cannot complete all 37 items: aim for accuracy before quantity. Calculator and paper recommended.</p>')
    ],
    'ubs-verb': [
      I('<p><b>UBS — Online Assessment.</b> Module documenté : <b>raisonnement logique/inductif — 18 questions en 6 minutes</b>, affirmations TRUE / FALSE / CANNOT SAY à partir d’informations écrites.</p><p>6 minutes pour 18 questions : moins de 20 secondes par question. Lisez l’affirmation, retrouvez la feuille, tranchez — ne restez jamais bloqué.</p><p>Le test ne peut pas être interrompu une fois commencé.</p>',
        '<p><b>UBS — Online Assessment.</b> Documented module: <b>logical/inductive reasoning — 18 items in 6 minutes</b>, TRUE / FALSE / CANNOT SAY statements based on written information.</p><p>6 minutes for 18 items: under 20 seconds per question. Read the statement, find the sheet, decide — never get stuck.</p><p>The test cannot be interrupted once started.</p>')
    ],
    'ubs-cult': [
      I('<p><b>UBS — Online Assessment.</b> Le <b>Korn Ferry Culture Match</b> fait partie de toutes les candidatures UBS (source : learnandpass.co.uk) : selon les retours de candidats (déc. 2024), il se compose de <b>18 questions basées sur des scénarios</b>.</p><p>Comme les questionnaires « Comportements » et « Motivations » de la base : blocs de trois affirmations, six points à répartir selon l’environnement de travail idéal pour vous.</p><p>Sans limite de temps, mais travaillez vite et honnêtement : ~15 minutes. Aucun retour en arrière possible.</p>',
        '<p><b>UBS — Online Assessment.</b> The <b>Korn Ferry Culture Match</b> is part of every UBS application (source: learnandpass.co.uk): according to candidate reports (Dec. 2024), it consists of <b>18 scenario-based questions</b>.</p><p>Like the “Behaviour” and “Motivation” questionnaires in the base: blocks of three statements, six points to allocate according to your ideal working environment.</p><p>No time limit, but work quickly and honestly: ~15 minutes. You cannot move back.</p>')
    ],
    'ms-num': [
      I('<p><b>Morgan Stanley — Online Assessment</b> (sources : forgeprep.io · careertestprep.com · preplounge.com). Selon le poste et la région : batterie <b>SHL</b> (IBD/S&amp;T notamment) ou <b>Aon/cut-e</b> (campus EMEA). Fenêtre de complétion : 5 à 7 jours ; cut-scores numériques parmi les plus élevés du secteur.</p><p>Module SHL : <b>numérique — 18 questions en 25 minutes</b>. Affirmations TRUE / FALSE / CANNOT SAY sur les feuilles de données.</p><p>Prévoyez calculatrice, crayon et papier. Le chrono démarre à la première question.</p>',
        '<p><b>Morgan Stanley — Online Assessment</b> (sources: forgeprep.io · careertestprep.com · preplounge.com). Depending on role and region: <b>SHL</b> battery (IBD/S&amp;T notably) or <b>Aon/cut-e</b> (EMEA campus). Completion window: 5 to 7 days; numerical cut-scores among the highest in the industry.</p><p>SHL module: <b>numerical — 18 items in 25 minutes</b>. TRUE / FALSE / CANNOT SAY statements on the data sheets.</p><p>Have a calculator, pencil and paper ready. The timer starts with the first question.</p>')
    ],
    'ms-verb': [
      I('<p><b>Morgan Stanley — Online Assessment.</b> Module SHL documenté : <b>verbal — 30 questions en 19 minutes</b>.</p><p>Affirmations TRUE / FALSE / CANNOT SAY à partir de passages écrits : répondez uniquement sur la base du texte, jamais sur vos connaissances.</p><p>~38 secondes par question. Le test ne peut pas être interrompu une fois commencé.</p>',
        '<p><b>Morgan Stanley — Online Assessment.</b> Documented SHL module: <b>verbal — 30 items in 19 minutes</b>.</p><p>TRUE / FALSE / CANNOT SAY statements based on written passages: answer only from the text, never from outside knowledge.</p><p>~38 seconds per question. The test cannot be interrupted once started.</p>')
    ],
    'ms-ind': [
      I('<p><b>Morgan Stanley — Online Assessment.</b> Module SHL documenté : <b>inductif — 24 questions en 25 minutes</b>.</p><p>Séries de figures : identifiez la règle (rotation, nombre, couleur, taille) et choisissez la figure suivante. Une seule réponse correcte.</p><p>~1 minute par question : si la règle ne saute pas aux yeux en 30 secondes, passez et revenez plus tard si le temps le permet.</p>',
        '<p><b>Morgan Stanley — Online Assessment.</b> Documented SHL module: <b>inductive — 24 items in 25 minutes</b>.</p><p>Figure series: identify the rule (rotation, count, colour, size) and pick the next figure. One correct answer.</p><p>~1 minute per question: if the rule is not obvious within 30 seconds, move on and come back later if time allows.</p>')
    ],
    'ms-sw': [
      I('<p><b>Morgan Stanley — Online Assessment.</b> Les candidats campus EMEA rapportent une batterie Aon incluant le <b>switchChallenge</b> (source : retours de candidats, gameassessmentprep.com).</p><p>Format identique au « switchChallenge » de la base : retrouvez le code de permutation appliqué par la machine. 6 minutes, niveau croissant.</p><p>Assurez-vous de ne pas être interrompu.</p>',
        '<p><b>Morgan Stanley — Online Assessment.</b> EMEA campus candidates report an Aon battery including the <b>switchChallenge</b> (source: candidate reports, gameassessmentprep.com).</p><p>Same format as the base “switchChallenge”: find the permutation code applied by the machine. 6 minutes, increasing difficulty.</p><p>Make sure you are not interrupted.</p>')
    ],
    'ms-sjt': [
      I('<p><b>Morgan Stanley — Online Assessment.</b> Les batteries campus EMEA incluent le <b>chatAssess d’Aon</b> : selon les candidats qui l’ont passé, « il faut répondre aux messages de collègues dans des scénarios fictifs en utilisant une interface de chat ».</p><p>Ce module reproduit ce format en mode messagerie : les scénarios arrivent comme des <b>messages reçus</b> et vous répondez comme vous le feriez dans un chat professionnel (quelques phrases suffisent).</p><p>13 scénarios, 10 minutes. Il n’y a pas de bonne réponse unique : demandez-vous ce que ferait un collègue fiable en contexte bancaire — qualité du travail, confidentialité, conformité, intégrité, priorisation, relation client.</p>',
        '<p><b>Morgan Stanley — Online Assessment.</b> EMEA campus batteries include <b>Aon’s chatAssess</b>: according to candidates who took it, “you have to respond to colleague messages in fake scenarios using a chat feature”.</p><p>This module reproduces that format in messenger mode: scenarios arrive as <b>incoming messages</b> and you reply exactly as you would in a professional chat (a few sentences are enough).</p><p>13 scenarios, 10 minutes. There is no single right answer: ask yourself what a reliable colleague would do in a banking context — quality of work, confidentiality, compliance, integrity, prioritisation, client care.</p>'),
      I('<p>Veuillez noter :</p><ul><li>Le chronomètre (10:00) démarre dès le premier message reçu.</li><li>Répondez à chaque message en tapant votre réponse puis « Envoyer » ; aucun retour en arrière possible.</li><li>Écrivez comme à un collègue : ton courtois, clair et professionnel.</li><li>À la fin, un dernier message vous oriente vers l’évaluation suivante du process.</li><li>Le test ne peut pas être interrompu une fois commencé.</li></ul>',
        '<p>Please note:</p><ul><li>The timer (10:00) starts as soon as the first message arrives.</li><li>Answer each message by typing your reply and pressing “Send”; you cannot move back.</li><li>Write as you would to a colleague: courteous, clear and professional tone.</li><li>At the end, a final message points you to the next assessment in the process.</li><li>The test cannot be interrupted once started.</li></ul>')
    ]
  };

  /* consignes courtes affichées pendant les items (FR / EN) */
  const STR = {
    fr: {
      chooseCorrect: 'Veuillez choisir la bonne réponse',
      dedNote: 'Chaque symbole apparaît une fois par ligne et par colonne.',
      indLeft: 'Ces deux grilles suivent une règle.',
      indRight: 'Lesquelles de ces quatre grilles suivent la même règle ?',
      indSel: 'Sélectionnez 2 grilles.',
      concQ: 'Cet objet est-il un E entouré d’exactement trois points ?',
      leShow: 'Mémorisez les objets dans l’ordre.',
      lePlace: 'Placez les objets dans l’ordre exact dans les champs correspondants.',
      leBreak: 'Pause — prochaine section dans',
      blkBeh: 'Avec quelle précision ces affirmations décrivent-elles votre comportement ?',
      blkMot: 'Quelle importance accordez-vous aux aspects suivants de votre environnement de travail ?',
      blkSjt: 'Répartissez les points selon les réactions qui vous correspondent le mieux dans la situation décrite.',
      blkSub: 'Attribuez les points en sélectionnant les cercles.',
      sheets: 'Feuilles de données', sheetsHint: 'Naviguez librement entre les feuilles : la question reste affichée.', sheetGo: 'Afficher cette feuille', finish: 'Terminer',
      exNoteOne: 'Exemple non noté et non chronométré — le chrono de {t} démarre après l’exemple.',
      exNoteMany: 'Exemples non notés et non chronométrés — le chrono de {t} démarre après le 3ᵉ exemple.',
      tf: ['true', 'false', 'cannot say'],
      unknown: '?',
      next: 'Suivant', intro: 'Introduction', guide: 'Directives', start: 'Commencer',
      langInstr: {
        flu: 'Trouvez le mot manquant pour compléter la phrase. Si vous ne connaissez pas la réponse, sélectionnez le point d’interrogation « ? ». Cliquez ensuite sur « suivant ».',
        voc: 'Choisissez le mot correspondant à la définition donnée. Sélectionnez le point d’interrogation « ? » si vous ne connaissez pas la réponse.',
        spe: 'Sélectionnez la bonne orthographe du mot. Si vous ne connaissez pas la réponse, choisissez le point d’interrogation « ? ».'
      },
      inbox: 'Boîte de réception', prio: 'Priorité', action: 'Action', noAction: '— aucune —',
      prioV: ['HIGH', 'MEDIUM', 'LOW'],
      actV: ['Transférer à Keira Sanders', 'Transférer à Daniel Knowles', 'Accuser réception', 'Responsable personnellement', 'Transférer à Walter Durenga'],
      chatOnline: 'en ligne', chatTyping: 'écrit…', chatPlaceholder: 'Écrivez votre réponse…', chatSend: 'Envoyer',
      chatNextLbl: 'Évaluation suivante', chatNextCta: 'Numerical Reasoning — appuyez pour commencer',
      chatEmpty: 'Écrivez une réponse avant d’envoyer.'
    },
    en: {
      chooseCorrect: 'Please choose the correct answer',
      dedNote: 'Each object appears only once per row and per column.',
      indLeft: 'These two grids follow a rule.',
      indRight: 'Which two of these grids follow the same rule?',
      indSel: 'Select 2 grids.',
      concQ: 'Is this object an E with three dots next to it?',
      leShow: 'Memorise the objects in the correct order.',
      lePlace: 'Please place the objects according to the correct order into the corresponding fields.',
      leBreak: 'Break — next section in',
      blkBeh: 'How accurately do these statements describe your behaviour?',
      blkMot: 'How important do you rate the following aspects for your work environment?',
      blkSjt: 'Allocate the points according to the reactions that suit you best in the situation described.',
      blkSub: 'Please allocate points by selecting the circles.',
      sheets: 'Data sheets', sheetsHint: 'Move freely between the sheets: the question stays on screen.', sheetGo: 'Show this sheet', finish: 'Finish',
      exNoteOne: 'Unscored, untimed example — the {t} test timer starts after the example.',
      exNoteMany: 'Unscored, untimed examples — the {t} test timer starts after the 3rd example.',
      tf: ['true', 'false', 'cannot say'],
      unknown: '?',
      next: 'Next', intro: 'Introduction', guide: 'Guidelines', start: 'Start',
      langInstr: {
        flu: 'Find the missing word to complete the sentence. If you do not know the answer, select the question mark "?". Then click "next".',
        voc: 'Choose the word corresponding to the given definition. Select the question mark "?" if you do not know the answer.',
        spe: 'Select the correct spelling of the word. If you do not know the answer, choose the question mark "?".'
      },
      inbox: 'Inbox', prio: 'Priority', action: 'Action', noAction: '— none —',
      prioV: ['HIGH', 'MEDIUM', 'LOW'],
      actV: ['Forward to Keira Sanders', 'Forward to Daniel Knowles', 'Notice of receipt', 'Personally responsible', 'Forward to Walter Durenga'],
      chatOnline: 'online', chatTyping: 'typing…', chatPlaceholder: 'Type your reply…', chatSend: 'Send',
      chatNextLbl: 'Next assessment', chatNextCta: 'Numerical Reasoning — tap to start',
      chatEmpty: 'Write a reply before sending.'
    }
  };

  return { SYM_DED, SYM_IND, SYM_SW, verbalSheets, verbal, enFluency, enVocab, enSpell, frFluency, frVocab, frSpell,
           behaviour, motivation, mech, msChat, infoRules, infoMails, infoMailsLate, infoMailTpl, leObjs, INTRO, STR,
           enFluencyExtra, enVocabExtra, enSpellPairs, frFluencyExtra, frVocabExtra, frSpellPairs };
})();

if (typeof window !== 'undefined') window.BANK = BANK; else globalThis.BANK = BANK;
