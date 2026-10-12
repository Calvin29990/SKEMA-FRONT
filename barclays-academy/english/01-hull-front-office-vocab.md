# 📈 VOCABULAIRE FRONT OFFICE — « Hull-Zero » (urgence n°1)

**Objectif** : zéro mot inconnu dans *Options, Futures and Other Derivatives* (Hull) et dans une conversation de desk. 15 termes/jour → Anki. IPA = prononciation UK approx.

## A. Marchés & instruments de base

| Terme | IPA | FR | Sens / usage |
|---|---|---|---|
| share / stock / equity | /ˈɛkwɪti/ | action | les 3 mots = action ; *equities* = la classe d'actifs actions |
| bond | /bɒnd/ | obligation | *government/corporate bond* |
| coupon | /ˈkuːpɒn/ | coupon | paiement d'intérêt périodique d'une obligation |
| principal / face value / par | /pɑː/ | nominal | montant remboursé à l'échéance ; *trading at par* = au pair |
| yield | /jiːld/ | rendement | *the 10-year gilt yield rose 5bp* |
| maturity | /məˈtʃʊərəti/ | échéance | *at maturity* |
| duration | /djʊəˈreɪʃn/ | duration | sensibilité aux taux (≠ durée !) |
| convexity | /kənˈvæksɪti/ | convexité | courbure prix/taux |
| gilt | /ɡɪlt/ | obligation d'État UK | UK Treasury bond — mot à connaître ABSOLUMENT à Londres |
| Treasury | /ˈtreʒəri/ | obligation US / Trésor | US Treasury + HM Treasury (le ministère !) — contexte décide |
| zero-coupon | /ˈzɪərəʊ kuːpɒn/ | zéro-coupon | aucun coupon, payé au pair à échéance |
| floating-rate note (FRN) | | oblig. à taux variable | coupon indexé (SOFR, SONIA) |
| SOFR / SONIA / €STR | | taux sans risque | les successeurs du LIBOR — citer-les proprement est un signal |
| interest-rate swap (IRS) | /swɒp/ | swap de taux | échange fixe vs variable ; *payer/receiver swap* |
| credit default swap (CDS) | | défaillance | assurance contre le défaut ; *CDS spread widened* |
| spread | /sprɛd/ | spread | écart ; *credit spread* / *bid-ask spread* |
| basis point (bp) | /ˈbeɪsɪs pɔɪnt/ | point de base | 1bp = 0,01 % — *twenty-five basis points* |
| repurchase agreement (repo) | /ˈriːpəʊ/ | pension livrée | vente avec rachat convenu ; *repo rate* |
| haircut | /ˈhɛəkʌt/ | décote | décote de garantie (repo, collatéral) — faux ami total ! |
| collateral | /kəˈlætərəl/ | garantie | *posted as collateral* |
| margin (initial/variation) | /ˈmɑːdʒɪn/ | marge | *margin call* = appel de marge |
| marked to market (MTM) | /mɑːkt/ | évalué au marché | revalorisation quotidienne ; *unrealized P&L* |
| settlement | /ˈsetlmənt/ | règlement | *T+1 settlement* (actions UK/US) |
| clearing house / CCP | /ˈklɪərɪŋ haʊs/ | chambre de compensation | *central counterparty* |
| dividend | /ˈdɪvɪdɛnd/ | dividende | *dividend yield* |
| earnings | /ˈɜːnɪŋz/ | résultats | *earnings season* ; EPS = earnings per share |
| market capitalisation | /ˌkæpɪtəlaɪˈzeɪʃn/ | capitalisation | *large-cap / mid-cap / small-cap* |
| P/E ratio | | PER | *trading at 18 times earnings* |
| book value | | valeur comptable | vs *market value* |
| free float | | flottant | part négociable |
| IPO | /ˌaɪ piː ˈəʊ/ | introduction en bourse | *to take a company public* |
| rights issue | | augmentation de capital | réservée aux actionnaires |
| buyback | /ˈbɪabæk/ | rachat d'actions | *share buyback programme* |
| underwriting | /ˈʌndəraɪtɪŋ/ | souscription/garantie | la banque garantit l'émission |
| syndication | /ˌsɪndɪˈkeɪʃn/ | syndication | *syndicated loan* |

## B. Dérivés & quant (le cœur du Hull)

| Terme | IPA | FR | Sens / usage |
|---|---|---|---|
| derivative | /dɪˈrɪvətɪv/ | dérivé | valeur dérivée d'un sous-jacent |
| underlying | /ˈʌndəlaɪɪŋ/ | sous-jacent | *the underlying asset* |
| forward | /ˈfɔːwəd/ | forward | OTC, à date/s Prix libre ; ≠ *futures* (standardisé, chambre) |
| futures | /ˈfjuːtʃəz/ | future | contrat à terme standardisé |
| call / put | /kɔːl/ /pʊt/ | call / put | droit d'acheter / de vendre |
| strike (price) | /straɪk/ | prix d'exercice | *in the money / at the money / out of the money* |
| expiry / expiration | /ɪkˈspaɪəri/ | échéance | *at expiry* |
| premium | /ˈpriːmiəm/ | prime | prix de l'option |
| payoff | /ˈpeɪɒf/ | gain | *payoff diagram* |
| European / American / Bermudan | /bəˈmjuːdn/ | type d'exercice | exercice à échéance / en continu / aux dates fixées |
| put-call parity | /ˈpærɪti/ | parité call-put | relation d'absence d'arbitrage |
| no-arbitrage | | absence d'arbitrage | pilier de la valorisation |
| hedging / to hedge | /hɛdʒ/ | couverture / couvrir | **JAMAIS « hedge » prononcé « hédge-uh » — /hɛdʒ/** |
| speculation | /ˌspekjuˈleɪʃn/ | spéculation | prise de position directionnelle |
| arbitrage / arb | /ˈɑːbɪtrɑːʒ/ ou /ˈɑːbɪtrɪdʒ/ | arbitrage | le trader dit *arb* /ɑːb/ |
| implied volatility (IV) | /ɪmˈplaɪd/ | vol implicite | déduite du prix de marché |
| realised volatility | /ˈriːəlaɪzd/ | vol réalisée | historique |
| vol smile / skew | /skjuː/ | sourire / skew | forme de la surface de vol |
| volatility surface | /ˈsɜːfɪs/ | surface de vol | IV par strike/maturité |
| delta / gamma / theta / vega / rho | /ˈdɛltə/ /ˈɡæmə/ /ˈθiːtə/ /ˈviːɡə/ /ˈrəʊ/ | les Grecs | sensibilités ; **theta /θ/**, **vega pas un mot grec réel** |
| delta hedging | | couverture delta | neutraliser le delta |
| Black-Scholes(-Merton) | /blæk ˈʃəʊlz/ | Black-Scholes | **pron. « sholes » — PAS « skolès »** |
| binomial tree | /baɪˈnəʊmiəl/ | arbre binomial | modèle discret |
| Monte Carlo simulation | | simulation MC | *to run 10,000 paths* |
| risk-neutral valuation | | valorisation risque-neutre | monde Q vs monde P |
| Wiener process / Brownian motion | /ˈwiːnə/ /ˈbraʊniən/ | processus de Wiener | moteur stochastique |
| drift / diffusion | /drɪft/ /dɪˈfjuːʒn/ | tendance / diffusion | composantes du SDE |
| mean reversion | /ˈriːvɜːʃn/ | retour à la moyenne | taux, vol |
| stochastic | /stəˈkæstɪk/ | stochastique | *stochastic calculus* |
| martingale | /ˈmɑːtɪŋɡeɪl/ | martingale | espérance constante sous Q |
| Value at Risk (VaR) | /vɛə/ | VaR | *99% 10-day VaR* |
| expected shortfall (ES) | /ˈʃɔːtfɔːl/ | ES/CVaR | perte moyenne au-delà du quantile |
| stress test / backtest | | tests | *to stress-test the book* |
| exposure | /ɪkˈspəʊʒə/ | exposition | *net exposure to EM* |
| correlation | /ˌkɒrəˈleɪʃn/ | corrélation | *correlations spike in a crash* |

## C. Trading & microstructure

| Terme | IPA | FR | Sens / usage |
|---|---|---|---|
| bid / ask (offer) | /bɪd/ /ɑːsk/ | achat / vente | *the bid-ask spread tightened* |
| mid | /mɪd/ | milieu | (bid+ask)/2 |
| quote | /kwəʊt/ | cotation | *to quote a price* |
| liquidity | /lɪˈkwɪdɪti/ | liquidité | *deep/thin liquidity* |
| order book / depth | | carnet d'ordres | *level 2 depth* |
| slippage | /ˈslɪpɪdʒ/ | glissement | prix exécuté ≠ prix attendu |
| market maker | | teneur de marché | fournit la liquidité |
| flow | /fləʊ/ | flux | *client flow* — le nerf du S&T |
| agency vs principal | /ˈpreɪzɪpəl/ | pour compte / pour propre | *trading as principal* |
| long / short | /lɒŋ/ /ʃɔːt/ | position acheteuse / vendeuse | *to go long / to short* ; *short squeeze* |
| to cover (a short) | /ˈkʌvə/ | dénouer | *covering drives a squeeze* |
| P&L | /piː ænd ˈɛl/ | P&L | *today's P&L* |
| intraday | /ˌɪntrəˈdeɪ/ | intraday | dans la journée |
| open / close | | ouverture / clôture | *closing auction* |
| fixing | /ˈfɪksɪŋ/ | fixing | prix de référence (FX 4pm Londres) |
| on-the-run / off-the-run | | le plus récent / ancien | liquidité des Treasuries |
| block trade | /blɒk/ | bloc | grosse taille négociée hors marché |
| RFQ | /ˌɑːr ɛf ˈkjuː/ | demande de cotation | *request for quote* |
| execution algo / VWAP / TWAP | | algos d'exécution | *we traded via VWAP* |
| high-frequency trading (HFT) | | trading haute fréquence | |
| proprietary trading / prop desk | /prəˈpraɪətəri/ | pour compte propre | |
|front office / middle office / back office | | les bureaux | FO = revenue ; MO = risk/KYC ; BO = settlement |
| trader's morning: « overnight moves » | /ˌəʊvəˈnaɪt/ | mouvements de nuit | *Asia sold off overnight* |
| to sell off | | plonger (ventes) | *gilts sold off after the CPI print* |
| to rally / a rally | /ˈræli/ | rebondir / rallye | *equities rallied on dovish comments* |
| a plunge / to plunge | /plʌndʒ/ | plongeon | chute brutale |
| a bounce | /baʊns/ | rebond technique | |
| to pare losses / to pare gains | /peə/ | réduire pertes/gains | *stocks pared earlier losses* |

## D. Macro & banques centrales (le rituel quotidien)

| Terme | IPA | FR | Sens / usage |
|---|---|---|---|
| base rate / policy rate | /beɪs reɪt/ | taux directeur | la BoE : *Bank Rate* |
| to hike / to cut / to hold | /haɪk/ /kʌt/ /həʊld/ | monter / baisser / maintenir | *the MPC held rates at 4%* |
| dovish / hawkish | /ˈdʌvɪʃ/ /ˈhɔːkɪʃ/ | accommodant / restrictif | *a hawkish hold* |
| forward guidance | | indications prospectives | communication bc centrale |
| quantitative easing / tightening (QE/QT) | /ˈkwɒntɪtətɪv/ | QE / resserrement | achats / non-renouvellement d'actifs |
| MPC / FOMC / ECB Governing Council | | comités de politique monétaire | UK / US / zone euro |
| CPI (headline / core) | /ˌsiː piː ˈaɪ/ | IPC (global / sous-jacent) | *core CPI surprised to the upside* |
| inflation print | /prɪnt/ | publication d'inflation | *a hot print* = plus haut qu'attendu |
| consensus / to beat / to miss | /kənˈsɛnsəs/ | consensus / battre / manquer | *CPI missed expectations* |
| yield curve | | courbe des taux | *the curve inverted* |
| steepening / flattening | /ˈstiːpənɪŋ/ | pentification / aplatissement | *bull steepener / bear flattener* |
| inversion | /ɪnˈvɜːʃn/ | inversion | signal de récession débattu |
| fiscal deficit / surplus | /ˈdɪsɪt/ | déficit budgétaire | *the OBR forecasts* |
| gilt issuance | /ˈɪsjuːəns/ | émission de gilts | l'offre d'obligations UK |
| sovereign debt | /ˈsɒvrɪn/ | dette souveraine | **/ˈsɒvrɪn/, jamais « so-ver-reigne »** |
| GDP / growth | /ˌdʒiː diː ˈpiː/ | PIB / croissance | *GDP grew 0.2% quarter-on-quarter (q/q)* |
| PMI | | indice des acheteurs | >50 = expansion |
| wage growth | /weɪdʒ/ | croissance des salaires | *sticky wage growth* |
| recession / soft landing | /rɪˈseʃn/ | récession / atterrissage en douceur | *a soft-landing narrative* |
| stagflation | /stæɡˈfleɪʃn/ | stagflation | inflation + stagnation |
| pound sterling / the pound / sterling | /ˈstɜːlɪŋ/ | livre sterling | *sterling weakened against the dollar* |
| GBP/USD (cable) / EUR/GBP | /ˈkeɪbl/ | paires | *cable* = GBP/USD, argot du FX |
| pip | /pɪp/ | pip | 4e décimale FX |
| cross rate / NDF | | croisé / forward non livrable | marchés contraints |
| safe haven | /heɪvn/ | valeur refuge | *the yen as a safe haven* |
| risk-on / risk-off | | appétit / aversion au risque | *a risk-off session* |

## E. Investment banking (le programme Barclays GP !)

| Terme | IPA | FR | Sens / usage |
|---|---|---|---|
| M&A / merger / acquisition | /ˈmɜːdʒə/ | fusion-acquisition | *an all-cash acquisition* |
| takeover / to take over | /ˈteɪkəʊvə/ | prise de contrôle | *a hostile takeover* |
| bid / offer (M&A) | | offre | *a £4bn bid for the company* |
| due diligence | /ˌdjuː daɪˈdɪlɪdʒəns/ | audit préalable | *to run due diligence* |
| pitchbook | /ˈpɪtʃbʊk/ | pitchbook | présentation client |
| mandate | /ˈmændeɪt/ | mandat | *we won the sell-side mandate* |
| buy-side / sell-side | | acheteur / vendeur | lequel conseille qui |
| valuation | /ˌvæljuˈeɪʃn/ | valorisation | DCF, multiples, comps (comparables) |
| DCF (discounted cash flow) | /dɪsˈkaʊntɪd/ | DCF | *to discount the cash flows* |
| multiple | /ˈmʌltɪpl/ | multiple | *EV/EBITDA multiple* |
| capital structure | /ˈkæpɪtl/ | structure financière | dette vs capitaux propres |
| seniority / subordinated | /ˌsiːniˈɒrəti/ /səˈbɔːdɪneɪtɪd/ | séniorité / subordonné | rang de remboursement |
| covenant | /ˈkʌvənənt/ | covenant | clause de la dette |
| leveraged buyout (LBO) | /ˈliːvərɪdʒd/ | rachat avec effet de levier | **/ˈliːvərɪdʒ/, pas « lé-va-raj »** |
| leverage | /ˈliːvərɪdʒ/ | effet de levier | *highly leveraged* |
| leveraged finance / high yield | /haɪ jiːld/ | levier / haut rendement | HY = *junk bonds* (argot) |
| restructuring | /ˌriːˈstrʌktʃərɪŋ/ | restructuration | *debt restructuring* |
| default | /dɪˈfɔːlt/ | défaut | *to default on its debt* |
| distressed | /dɪˈstrest/ | en difficulté | *distressed debt* |
| bookbuilding / roadshow | /ˈrəʊdʃəʊ/ | construction du livre / tournée | étapes d'une IPO |
| ECM / DCM | | marchés actions / dette | les divisions de financement |
| advisor / adviser | /ədˈvaɪzə/ | conseiller | **le verbe advise /ədˈvaɪz/, le nom advice /ədˈvaɪs/** |

## F. Banque, rôles, conformité

| Terme | IPA | FR | Sens / usage |
|---|---|---|---|
| sales / trading / structuring / research (strats) | /ˈstræts/ | les 4 patte du S&T | *strats* = quants de desk |
| coverage banker | /ˈkʌvərɪdʒ/ | banquier coverage | relation client sectorielle |
| credit risk / market risk / operational risk | | risques | les 3 familles |
| compliance | /kəmˈplaɪəns/ | conformité | *compliance sign-off* |
| KYC / AML | | connaissance client / anti-blanchiment | onboarding |
| regulator / regulatory | /ˈreɡjʊlətəri/ | régulateur / réglementaire | FCA, PRA |
| ring-fencing | /rɪŋ ˈfɛnsɪŋ/ | cloisonnement | séparation détail/investissement UK |
| capital requirements | | exigences de capital | *CET1 ratio* |
| pay slip / payroll | /ˈpeɪrəʊl/ | fiche de paie / paie | utile pour ton bail à Londres ! |
| notice period | /ˈnəʊtɪs/ | préavis | *one month's notice* |
| graduate scheme / cohort | /ˈkəʊhɔːt/ | programme graduate / promotion | le vocabulaire exact du process |
| to be put forward for | | être proposé pour | *you'll be put forward for a final round* |
| to fast-track | /fɑːst træk/ | accélérer | *fast-tracked to assessment* |
| rolling basis | /ˈrəʊlɪŋ/ | au fil de l'eau | *applications reviewed on a rolling basis* |
| onboarding | /ˈɒnbɔːdɪŋ/ | intégration | pre-joining checks |
