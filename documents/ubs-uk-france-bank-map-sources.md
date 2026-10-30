# UK & France banking results map — source and methodology notes

**Deliverable:** `ubs-uk-france-bank-map.png`  
**Generator:** `build_ubs_uk_france_bank_map.py`  
**Period:** full-year 2011, except for the separately identified UBS trading incident.

## What the slide compares—and what it does not

The green / charcoal values are each issuer's **published full-year consolidated group net income or loss**, shown in its original reporting currency and rounded to three decimal places in billions. Labels for the attributable/group-share line vary somewhat across issuers; the amounts are reproduced from the issuer's own results announcement or annual report. They are context, not a perfectly harmonized accounting comparison.

The red UBS value is a **one-off unauthorized-trading loss of approximately USD 2.3bn** associated with the London ETF desk. It is not UBS's full-year consolidated result, and it is not the same metric as the peers' annual group net income. The slide deliberately separates the incident from the peer results. No currency conversion, common scale, or proportional marker sizing is used.

The displayed bank locations are approximate major hubs: London for UBS's ETF desk, HSBC, Barclays and Lloyds; Edinburgh for RBS; Paris for the French groups. They do not imply that the full-year group result was generated in that city. The map outline is derived from Natural Earth 1:50m Admin 0 country boundaries; UK and metropolitan France are highlighted, with neighboring land muted for context. The selected boundary geometries are stored in `assets/natural-earth-50m-uk-france-context.geojson`. Natural Earth data are public domain; dataset information: https://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-admin-0-countries/. Markers are equal-sized and encode only positive/negative category, not value magnitude.

## Values and primary sources

1. **UBS incident loss — −USD 2.3bn.** FINMA, *Report on the UBS trading losses*, summary report (21 November 2012). The report describes unauthorized transactions on the ETF desk of UBS's London branch and the resulting loss of approximately USD 2.3bn.  
   https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/8news/medienmitteilungen/2012/11/20121121-ubs-summary-report.pdf?sc_lang=en&hash=D26DD4BBF243411F07C72BCA738FF40A
2. **HSBC — +USD 16.797bn.** HSBC, *Annual Report and Accounts 2011*, profit attributable to shareholders of the parent company.  
   https://www.hsbc.com/-/files/hsbc/investors/investing-in-hsbc/all-reporting/group/2011/hsbc2011arn.pdf
3. **Barclays — +GBP 3.007bn.** Barclays, *Full Year 2011 Results Announcement*, profit attributable to equity holders of the parent company.  
   https://home.barclays/content/dam/home-barclays/documents/investor-relations/ResultAnnouncements/2011FYResults/Barclays-PLC-Full-Year-2011-Results-Announcement.pdf
4. **Lloyds Banking Group — −GBP 2.787bn.** Lloyds, *2011 Results*, loss attributable to shareholders.  
   https://www.lloydsbankinggroup.com/assets/pdfs/investors/financial-performance/lloyds-banking-group-plc/archive/2011/full-year/2011-lbg-results.pdf
5. **RBS — −GBP 1.997bn.** RBS, *Annual Report 2011*, loss attributable to ordinary and B shareholders.  
   https://www.investors.rbs.com/~/media/Files/R/RBS-IR-V2/annual-reports/annual-report-2011.pdf
6. **BNP Paribas — +EUR 6.050bn.** BNP Paribas, *Annual Report 2011*, net income attributable to equity holders.  
   https://invest.bnpparibas/en/document/financial-statements-annual-audited-2
7. **Société Générale — +EUR 2.385bn.** Société Générale, *2011 Results*, Group net income.  
   https://www.societegenerale.com/sites/default/files/documents/cp-q411.pdf
8. **Crédit Agricole Group — +EUR 0.812bn.** Crédit Agricole Group, *2011 Results*, Group share of net income. This is the **Group** result, not Crédit Agricole S.A. on its own (which reported a loss).  
   https://www.credit-agricole.com/en/pdfPreview/103052
9. **Natixis — +EUR 1.562bn.** Natixis, *2011 and fourth-quarter 2011 results*, Group share of net income.  
   https://pressroom-en.natixis.com/news/2011-and-fourth-quarter-2011-results-12ff-8e037.html

## Display and rounding

- The figures are billions, retaining each company's published currency (USD, GBP or EUR); CHF is not shown on this map.
- Values are rounded to the nearest 0.001bn where source amounts are published in millions.
- The minus sign denotes a reported group loss, except the red UBS item, which specifically denotes the separate trading incident loss.
- Positive results use green; negative annual results use charcoal; UBS's incident is red.
- The approved reference image at `assets/approved-fx-map-slide.png` is preserved separately and has not been altered or used as the map artwork.
