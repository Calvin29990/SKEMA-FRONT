# UBS Treasury Committee deck — sources and claim notes

Prepared for the 8-slide executive presentation. Source IDs are referenced in slide footers. Scenario values are classroom assumptions, not historical UBS cash-flow data.

## Public event facts

1. **Société Générale, General Inspection, “Mission Green” summary (20 May 2008).** Reports the €4.9bn loss attributed to Jérôme Kerviel’s unauthorized positions.
   https://www.societegenerale.com/sites/default/files/12%20May%202008%20The%20report%20by%20the%20General%20Inspection%20of%20Societe%20Generale.pdf
2. **Reserve Bank of Australia, “The Barings Collapse” (November 1995).** Reports £827m of unreported losses by 27 February 1995; the closure of positions brought the total to approximately £927m.
   https://www.rba.gov.au/publications/bulletin/1995/nov/1.html
3. **Credit Suisse / SEC Form 6-K, Archegos review (29 July 2021), hosted by UBS.** Reports a Credit Suisse loss of approximately USD 5.5bn following Archegos’s default. This was a counterparty-default event, not an unauthorized employee-trading case.
   https://www.ubs.com/global/en/investor-relations/complementary-financial-information/disclosure-legal-entities/archive-credit-suisse/_jcr_content/mainpar/toplevelgrid_1145414446/col1/accordionbox/accordionsplit_794647952/table_1735174296.0683569823.file/dGFibGVUZXh0PS9jb250ZW50L2RhbS9hc3NldHMvY2MvaW52ZXN0b3ItcmVsYXRpb25zL2NvbXBsZW1lbnRhcnktZmluYW5jaWFsLWluZm9ybWF0aW9uL2FyY2hpdmUvMjAyMS8yMDIxMDcyOS02ay1tci1hcmNoZWdvc3JlcG9ydC5wZGY=/20210729-6k-mr-archegosreport.pdf
4. **FINMA, summary of investigation into UBS (21 November 2012).** Reports the UBS unauthorized-trading loss and key position/control failures; peak long futures positions were USD 12.1bn (8 August) and peak short positions USD 8.5bn (15 September), both gross notional—not P&L.
   https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/8news/medienmitteilungen/2012/11/20121121-ubs-summary-report.pdf?sc_lang=en&hash=D26DD4BBF243411F07C72BCA738FF40A
5. **FCA, Final Notice to UBS AG (25 November 2012).** Findings on control failures, fictitious/offsetting positions and the unauthorized trading loss.
   https://www.fca.org.uk/publication/final-notices/ubs-ag.pdf
6. **UBS Supplement No. 2 (11 October 2011).** Initial estimate of approximately USD 2bn, risk covered by 18 September and revised loss of USD 2.3bn on 4 October.
   https://keyinvest-it.ubs.com/filedb/deliver/xuuid/l00170bd9263aa8642128581708268d60e04/name/2.2_UBS_SNP_11Oct2011.pdf
7. **UBS Q3 2011 reporting archive.** Reports CHF 1.951bn accounting impact / USD 2.229bn equivalent (reporting presentation; not a cash-flow series).
   https://www.ubs.com/global/en/investor-relations/financial-information/quarterly-reporting/qr-archive/qr-archive11-15.html

## Presentation conventions and scenario assumptions

- Slide 1 uses approximate nominal event-date USD equivalents only to size bubbles: Barings £827m ≈ USD 1.3bn; Société Générale €4.9bn ≈ USD 7.2bn; Credit Suisse USD 5.5bn; UBS USD 2.3bn. These FX translations are approximate and are not inflation-adjusted.
- Barings bubble is based on the £827m unreported-loss figure, while the slide separately notes the approximately £927m total including closure costs.
- Slides 2 panels 1–2 use normalized illustrative profiles. The UBS panel contains cited public facts only, not a reconstructed historical series.
- Slides 5–6 use hypothetical cash paths and a hypothetical USD 250m T+2 facility. There is no verified public UBS daily cash-flow series or public minimum liquidity buffer for this incident.
- Slide 5 assumptions (USDm): opening cash 1,000; minimum buffer 700. Base path: 1,000, 990, 985, 990, 985, 987, 984, 1,004, 1,104, 1,054, 1,024. Incident teaching path: 1,000, 915, 805, 775, 765, 772, 724, 719, 859, 799, 774. Stress path: 1,000, 915, 805, 775, 765, 772, 724, 719, 759, 499, 474. Stress first breaches on 30 November at 499 (201 below buffer); minimum cash 474; maximum funding need 226. Stress shocks: settlement +50, October collateral return delayed −100, withdrawals −100, non-renewed funding −50. A hypothetical T+2 facility must be drawn by 25 November to receive cash by 29 November.
- Slide 6 hypothetical waterfall (USDm, 14–30 September): opening 1,000 + inflows 1,105 − operating/contractual payments 1,101 − incident settlements 270 − net collateral cash use 10 − operating costs 5 = closing 719; buffer 700; headroom 19. Loss, settlement and collateral are kept distinct to avoid double-counting.
- Slide 7 qualitative risk placements are management judgements for teaching, not externally validated regulatory scores.
