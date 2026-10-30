# Why the UBS Event Matters — sources and methodology

**Slide:** `ubs-event-context-map.png`  
**Generator:** `build_ubs_event_context_map.py`  
**Map geometry:** `assets/natural-earth-50m-western-europe-context.geojson` (Natural Earth 1:50m, public domain).

## What the slide says

The UBS 2011 unauthorized-trading loss is highlighted in UBS red. The other four events are muted grey. This is a selected context set, not a comprehensive league table. UBS sits among the largest documented unauthorized-trading losses at a major European bank in this comparison, but it is not the largest event shown by dollar value.

The examples are all major bank trading / positions-unwind loss events, but their causes and accounting bases are not identical: UBS, Société Générale and Barings involved unauthorized or concealed trading; JPMorgan's London Whale was a synthetic-credit portfolio loss; Credit Suisse's Archegos loss was a prime-brokerage counterparty exposure. The slide does not imply those causal mechanisms are equivalent.

## Event values and primary sources

1. **UBS, 2011 — approximately USD 2.3bn.** FINMA, *Investigation into the Events surrounding Trading Losses of USD 2.3 billion incurred by the Investment Banking Division of UBS AG in London*, summary report, 21 November 2012. FINMA identifies unauthorized trading on the London ETF desk, serious risk-management and control failures, and supervisory measures including capital restrictions and an acquisition ban for the Investment Bank. UBS described the business as ETF / Delta One; the slide locates the institution at Zurich but labels the incident desk at London.  
   https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/8news/medienmitteilungen/2012/11/20121121-ubs-summary-report.pdf?sc_lang=en&hash=D26DD4BBF243411F07C72BCA738FF40A  
   FINMA press summary: https://www.finma.ch/en/news/2012/11/mm-ubs-london-20121126
2. **Credit Suisse, 2021 — approximately USD 5.5bn.** Credit Suisse Group Special Committee, *Report on Archegos Capital Management*, filed as SEC Exhibit 99.2, 29 July 2021. The report describes the loss following Archegos's default and the resulting unwind. The map's Zurich point is the institution's headquarters, not the location of the underlying positions.  
   https://www.sec.gov/Archives/edgar/data/1159510/000137036821000064/a210729-ex992.htm
3. **JPMorgan, 2012 — at least USD 6.2bn.** U.S. Senate Permanent Subcommittee on Investigations, *JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses*, 15 March 2013. The losses arose from the Chief Investment Office's Synthetic Credit Portfolio, with trading in JPMorgan's London office.  
   https://www.hsgac.senate.gov/subcommittees/investigations/rep/senate-investigations-subcommittee-holds-hearing-and-releases-report-on-jpmorgan-chase-whale-trades/
4. **Société Générale, 2008 — EUR 4.9bn net loss.** Société Générale, *Kerviel case*, including its account of the loss and the January 2008 unwind. The bank explains the EUR 4.9bn net impact as the EUR 6.3bn unwind loss less EUR 1.4bn of concealed gains on unauthorized positions.  
   https://www.societegenerale.com/en/news/newsroom/kerviel-case
5. **Barings, 1995 — approximately USD 1.4bn equivalent.** The UK Board of Banking Supervision inquiry is summarized by the Reserve Bank of Australia. The inquiry records cumulative losses of GBP 827m by 27 February 1995; including close-out costs, total losses on the unauthorized trading were GBP 927m. USD 1.4bn is retained as the approximate equivalent requested for the slide, not as a precise converted accounting figure. Leeson's trading operation was in Singapore; the map marks London as Barings' institutional home, not as the trade location.  
   https://www.rba.gov.au/publications/bulletin/1995/nov/1.html  
   An accessible USD-equivalent summary: https://www.investopedia.com/ask/answers/08/nick-leeson-barings-bank.asp
6. **FX rate used for the bubble scale.** ECB euro reference series, USD per EUR. EUR 4.9bn × 1.4663 on 24 January 2008 = approximately USD 7.18bn.  
   https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2008-01-24&endPeriod=2008-01-24&format=csvdata  
   The historic daily reference value is also reproduced here: https://www.poundsterlinglive.com/bank-of-england-spot/historical-spot-exchange-rates/eur/EUR-to-USD-2008

## Circle sizing and map geography

- Circle **area**, not radius, is proportional to the headline loss in approximate USD-equivalent terms. The rendered radius follows `sqrt(loss / maximum loss)`.
- USD losses use their published headline amounts. Société Générale's EUR 4.9bn is converted at the ECB reference rate for 24 January 2008 (USD 1.4663 per EUR), solely to size its circle; the right-side panel keeps the published EUR value.
- Barings is shown as approximately USD 1.4bn as requested; the primary inquiry's GBP 827m / GBP 927m figures remain the authoritative underlying record. Treat the USD value and resulting circle size as indicative.
- No event loss is inflation-adjusted. The map therefore compares nominal headline amounts across years, not present-value purchasing power.
- Map points indicate the requested institutional / financial hubs, not necessarily the precise location of the trading book: UBS incident desk—London; UBS and Credit Suisse institution—Zurich; Société Générale—Paris; JPMorgan London Whale—London; Barings HQ—London, while Leeson traded in Singapore.

## Treasury takeaway

“Delta One control failure: capital headroom, funding confidence and liquidity readiness” is framed as a **Treasury lens**, not as a claim that UBS suffered a liquidity crisis. FINMA's report supports the control-failure and capital-measure context; UBS's 2011 reporting describes a material loss and its capital impact. The concise takeaway highlights preparedness and resilience.
