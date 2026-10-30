# Major European Trading Loss Events — sources and methodology

**Slide:** `ubs-event-context-map.png`  
**Generator:** `build_ubs_event_context_map.py`  
**Map geometry:** Natural Earth 1:50m country outlines (`assets/natural-earth-50m-western-europe-context.geojson`), metropolitan France regions (`assets/france-regions.geojson`, [gregoiredavid/france-geojson](https://github.com/gregoiredavid/france-geojson)), and the London region (`assets/uk-london-region.geojson`, UK-GeoJSON / ONS NUTS1, [martinjc/UK-GeoJSON](https://github.com/martinjc/UK-GeoJSON)).

## What the slide says

This is a selected context set, not a comprehensive league table. The UK, France and Switzerland remain grey except for small, schematic local banking-hub patches; no whole country is filled. The map has no pins or proportional circles. A compact Power BI-style panel places bank logos beside large loss values, while additional CIB / major-bank logos are shown as context only. No loss figure is assigned to a context bank unless a comparable benchmark case is included.

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

Event logos appear beside the reported loss values; peer-bank logos appear in a separate context group. The UBS mark is the repository's existing UBS asset. Credit Suisse and Société Générale marks are sourced from Wikimedia Commons, originally credited to their respective banks; JPMorgan Chase is a wordmark asset from SeekVectors. Barings Bank historically used a heraldic crest rather than a modern logo, so the slide uses a custom period-neutral text wordmark—not the contemporary Barings asset-management logo. Peer marks are used for identification only. Brand marks remain their owners' trademarks.

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

- The country base is neutral grey. French administrative regions are outlined; Île-de-France is red for Société Générale and Hauts-de-France is Crédit Agricole green. The remaining French regions stay grey.
- In the UK, only the London region is light blue for Barclays; the Barings London-hub marker is brown. Switzerland stays grey except for the UBS-red and Credit Suisse-teal Zurich hub areas. These highlights are regional/hub emphasis, not bank-owned territory.
- The right-hand table shows the five retained benchmark events and their large reported loss amounts. BNP Paribas, Crédit Agricole CIB, Natixis, HSBC, Barclays, Lloyds Bank and NatWest appear as peer logos only; no additional loss values are assigned to them in this comparison.
- There are no proportional circles or pin markers. Event values stay in their reported currencies: USD for UBS, Credit Suisse, JPMorgan and Barings; EUR for Société Générale. Barings’ USD 1.4bn is approximate; the official inquiry reports GBP 827m cumulative losses and GBP 927m including close-out costs.
- The map identifies institutional hubs, not necessarily precise trading locations: UBS and Credit Suisse are shown at their Zurich headquarters; Société Générale at Paris; JPMorgan's London Whale at London; Barings at its London headquarters. UBS's loss-making desk was in London, and Leeson traded in Singapore. The footer clarifies these distinctions.
- No event loss is inflation-adjusted; the slide compares nominal headline impacts across years, not present-value purchasing power.

## Executive takeaway

The requested conclusion is reproduced verbatim on the slide: “UBS's USD 2.3bn trading loss ranks among the most significant banking trading-loss events in Europe and illustrates how control failures can rapidly escalate into material financial and liquidity-management consequences.” This is framed as a lesson about control and consequence, not as a claim that UBS suffered a liquidity crisis.
