# Major European Trading Loss Events — sources and methodology

**Slide:** `ubs-event-context-map.png`  
**Generator:** `build_ubs_event_context_map.py`  
**Map geometry:** Natural Earth 1:50m country outlines (`assets/natural-earth-50m-western-europe-context.geojson`, public domain). City positions follow the supplied brief.

## What the slide says

The map follows the supplied football-transfer reference: a light-grey Europe base, ten bank logos placed once at the specified cities, and spacious city labels. No proportional circles are used. Numeric loss callouts are limited to the three events requested—Barings, Kerviel and Adoboli/UBS—while the other seven banks are shown as logo-only context.

The examples are all major bank trading / positions-unwind loss events, but their causes and accounting bases are not identical: UBS, Société Générale and Barings involved unauthorized or concealed trading; JPMorgan's London Whale was a synthetic-credit portfolio loss; Credit Suisse's Archegos loss was a prime-brokerage counterparty exposure. The slide does not imply those causal mechanisms are equivalent.

## Event values and primary sources

1. **UBS, 2011 — approximately USD 2.3bn.** FINMA, *Investigation into the Events surrounding Trading Losses of USD 2.3 billion incurred by the Investment Banking Division of UBS AG in London*, summary report, 21 November 2012. FINMA identifies unauthorized trading on the London ETF desk, serious risk-management and control failures, and supervisory measures including capital restrictions and an acquisition ban for the Investment Bank. UBS described the business as ETF / Delta One; the map places UBS in Switzerland as its Zurich headquarters and notes the London desk in the footer.<br>
   https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/8news/medienmitteilungen/2012/11/20121121-ubs-summary-report.pdf?sc_lang=en&hash=D26DD4BBF243411F07C72BCA738FF40A  
   FINMA press summary: https://www.finma.ch/en/news/2012/11/mm-ubs-london-20121126
2. **Credit Suisse, 2021 — approximately USD 5.5bn.** Credit Suisse Group Special Committee, *Report on Archegos Capital Management*, filed as SEC Exhibit 99.2, 29 July 2021. The report describes the loss following Archegos's default and the resulting unwind. The map places the bank in Switzerland to show its Zurich headquarters, not the location of the underlying positions.<br>
   https://www.sec.gov/Archives/edgar/data/1159510/000137036821000064/a210729-ex992.htm
3. **JPMorgan, 2012 — at least USD 6.2bn.** U.S. Senate Permanent Subcommittee on Investigations, *JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses*, 15 March 2013. The losses arose from the Chief Investment Office's Synthetic Credit Portfolio, with trading in JPMorgan's London office.  
   https://www.hsgac.senate.gov/subcommittees/investigations/rep/senate-investigations-subcommittee-holds-hearing-and-releases-report-on-jpmorgan-chase-whale-trades/
4. **Société Générale, 2008 — EUR 4.9bn net loss.** Société Générale, *Kerviel case*, including its account of the loss and the January 2008 unwind. The bank explains the EUR 4.9bn net impact as the EUR 6.3bn unwind loss less EUR 1.4bn of concealed gains on unauthorized positions.  
   https://www.societegenerale.com/en/news/newsroom/kerviel-case
5. **Barings, 1995 — approximately USD 1.4bn equivalent.** The UK Board of Banking Supervision inquiry is summarized by the Reserve Bank of Australia. The inquiry records cumulative losses of GBP 827m by 27 February 1995; including close-out costs, total losses on the unauthorized trading were GBP 927m. USD 1.4bn is retained as the approximate equivalent requested for the slide, not as a precise converted accounting figure. Leeson's trading operation was in Singapore; the map places Barings in the UK to show its institutional home, not the trade location.<br>
   https://www.rba.gov.au/publications/bulletin/1995/nov/1.html  
   An accessible USD-equivalent summary: https://www.investopedia.com/ask/answers/08/nick-leeson-barings-bank.asp
## Identity marks

Ten bank logos appear once, directly on the map at the user-specified cities; Barings is an event text marker, not a second London bank logo. UBS is the repository's existing mark. Credit Suisse and Société Générale assets are sourced from Wikimedia Commons; BNP Paribas, Crédit Agricole CIB, Natixis, HSBC, Barclays, Lloyds and NatWest wordmarks are retained for identification. Brand marks remain their owners' trademarks.

- Credit Suisse logo: https://commons.wikimedia.org/wiki/File:Credit_Suisse_Logo.svg
- Société Générale logo: https://commons.wikimedia.org/wiki/File:Logo-SG-Soci%C3%A9t%C3%A9-G%C3%A9n%C3%A9rale.svg
- JPMorgan Chase wordmark: https://seekvectors.com/post/jpmorgan-chase-logo-vector
- Barings' historical crest context: https://content.time.com/time/specials/packages/article/0,28804,1937349_1937350_1937488,00.html
- BNP Paribas logo: https://www.pngplay.com/image/59723
- Crédit Agricole CIB logo: https://seeklogo.com/free-vector-logos/credit-agricole
- Natixis logo: https://seeklogo.com/free-vector-logos/natixis
- HSBC logo: https://www.pngitem.com/middle/oJTbwo_hsbc-bank-logo-png-transparent-png/
- Barclays logo: https://1000logos.net/barclays-logo/
- Lloyds Banking Group logo: https://companieslogo.com/lloyds-banking-group/logo/
- NatWest logo: https://www.vhv.rs/viewpic/TioTmix_natwest-bank-logo-transparent-background-image-natwest-bank/

## Map fills and annotations

- The base map is light grey and uses no filled country regions. City logo tiles use the requested brand colours: HSBC red in London, Barclays sky blue in Manchester, Lloyds green in Birmingham, NatWest purple in Edinburgh; Société Générale red in Paris, BNP green in Lille, Crédit Agricole green in Lyon, Natixis navy in Marseille; UBS red in Zurich and Credit Suisse blue in Geneva.
- Only the three benchmark events carry numeric callouts: Barings (1995, USD -1.4bn), Kerviel (2008, EUR -4.9bn), and Adoboli/UBS (2011, USD -2.3bn). The UBS logo has the largest red rectangular halo, following the requested hierarchy; the amount is not encoded by marker size.
- The Barings USD equivalent is approximate. The inquiry reports cumulative GBP 827m losses by 27 February 1995 and GBP 927m including close-out costs. The visible negative sign indicates a loss, not a separate conversion method.
- City placements follow the supplied brief. For factual context, Adoboli's unauthorized trading took place on UBS's London desk; Zurich is UBS's headquarters. Barings is shown as the London event marker, while Leeson's trading operation was in Singapore.
- No displayed loss is inflation-adjusted; the infographic compares nominal headline impacts across years.

## Executive takeaway

The requested conclusion is reproduced verbatim on the slide: “UBS's USD 2.3bn trading loss ranks among the most significant banking trading-loss events in Europe and illustrates how control failures can rapidly escalate into material financial and liquidity-management consequences.” This is framed as a lesson about control and consequence, not as a claim that UBS suffered a liquidity crisis.
