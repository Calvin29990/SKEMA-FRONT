# Major European Trading Loss Events — sources and methodology

**Slide:** `ubs-event-context-map.png`
**Generator:** `build_ubs_event_context_map.py`
**Map geometry:** Natural Earth 1:50m Western Europe country outlines (`assets/natural-earth-50m-western-europe-context.geojson`, public domain).

## Slide copy

- **Title:** `MAJOR EUROPEAN TRADING LOSS EVENTS`
- **Subtitle:** `Selected benchmark trading-loss events relevant to the UBS 2011 case`
- **Conclusion:** `UBS's USD 2.3bn trading loss ranks among the most significant banking trading-loss events in Europe and illustrates how control failures can rapidly escalate into material financial and liquidity-management consequences.`

## Event values and factual context

1. **Adoboli / UBS, 2011 — USD -2.3bn.** FINMA's investigation describes losses of USD 2.3 billion in UBS Investment Banking in London and serious failures in risk management and controls. The trading desk was in London; Zurich is the UBS group headquarters. The map places the UBS logo at Zurich as requested and states the distinction in the footnote; the Adoboli event callout is visually associated with the UBS marker, not intended to relocate the trading desk to Zurich.
   FINMA, *Investigation into the Events surrounding Trading Losses of USD 2.3 billion incurred by the Investment Banking Division of UBS AG in London*, summary report, 21 November 2012: https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/8news/medienmitteilungen/2012/11/20121121-ubs-summary-report.pdf?sc_lang=en&hash=D26DD4BBF243411F07C72BCA738FF40A
   FINMA press summary: https://www.finma.ch/en/news/2012/11/mm-ubs-london-20121126
2. **Kerviel / Société Générale, 2008 — EUR -4.9bn.** Société Générale describes the EUR 4.9bn net impact of the January 2008 unwind, after offsetting EUR 1.4bn in concealed gains against EUR 6.3bn in losses on unauthorized positions. The slide displays the requested net-loss figure.
   Société Générale, *Kerviel case*: https://www.societegenerale.com/en/news/newsroom/kerviel-case
3. **Barings, 1995 — USD -1.4bn equivalent (approximate).** The UK Board of Banking Supervision inquiry, summarized by the Reserve Bank of Australia, records cumulative losses of GBP 827m by 27 February 1995 and GBP 927m including close-out costs. The slide retains USD 1.4bn as the requested approximate equivalent, not as a precise converted accounting figure. Barings is represented at its London institutional home; Nick Leeson's unauthorized trading operation was in Singapore.
   Reserve Bank of Australia, *The Barings collapse*: https://www.rba.gov.au/publications/bulletin/1995/nov/1.html
   Accessible USD-equivalent summary: https://www.investopedia.com/ask/answers/08/nick-leeson-barings-bank.asp

The minus signs on the slide explicitly indicate losses. The amounts are nominal headline impacts from different years and are not inflation-adjusted; causes and accounting bases are not identical.

## Bank identities and map treatment

The infographic shows the 12 requested logo-and-city pairings, once each:

| City | Bank | City-label colour |
|---|---|---|
| London | HSBC | `#DB0011` |
| Manchester | Barclays | `#00AEEF` |
| Birmingham | Lloyds | `#00843D` |
| Edinburgh | NatWest | `#5E2750` |
| Lille | BNP Paribas | `#00965E` |
| Paris | Société Générale | `#E30613` (red) |
| Lyon | Crédit Agricole | `#006B54` |
| Marseille | Natixis | `#6F2DA8` (violet, as requested) |
| Zurich | UBS | `#111111` (black) |
| Geneva | Credit Suisse | `#005EB8` |
| Basel | Julius Baer | `#B89D4F` |
| Lugano | Pictet | `#006A52` |

The European land base is light grey with understated borders. Bank wordmarks float directly on the map without circular markers, halos or white logo cards; each city name appears underneath its logo in the associated colour. Natixis is slightly enlarged as a visual example, and **MARSEILLE** is highlighted in violet. The three event highlights remain in the requested hierarchy: largest red UBS/Adoboli callout, second red Kerviel callout, and third gold Barings callout.

## Logo asset references

Logo image files used by the generator are in `assets/`. Logos are trademarks of their respective owners; the listed pages are asset references, not endorsements.

- HSBC: https://www.pngitem.com/middle/oJTbwo_hsbc-bank-logo-png-transparent-png/
- Barclays: https://1000logos.net/barclays-logo/
- Lloyds Banking Group: https://companieslogo.com/lloyds-banking-group/logo/
- NatWest: https://www.vhv.rs/viewpic/TioTmix_natwest-bank-logo-transparent-background-image-natwest-bank/
- BNP Paribas: https://www.pngplay.com/image/59723
- Société Générale: https://commons.wikimedia.org/wiki/File:Logo-SG-Soci%C3%A9t%C3%A9-G%C3%A9n%C3%A9rale.svg
- Crédit Agricole CIB: https://seeklogo.com/free-vector-logos/credit-agricole
- Natixis: https://seeklogo.com/free-vector-logos/natixis
- UBS: existing repository asset, `assets/ubs-logo.png`
- Credit Suisse: https://commons.wikimedia.org/wiki/File:Credit_Suisse_Logo.svg
- Julius Baer: https://freebiesupply.com/logos/julius-baer-logo/
- Pictet: https://www.abps.ch/en/members/banque-pictet-cie-sa/

## Rebuild and conclusion

From the repository root, run `python documents/build_ubs_event_context_map.py` after installing Pillow. The generated slide retains the conclusion quoted above. It frames the UBS case as a lesson about control failures and consequences, not as a claim that UBS suffered a liquidity crisis.
