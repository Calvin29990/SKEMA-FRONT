# Marketing-finance options — slide 2 after the Europe CIB map

Generated with `src/build_logo_options.py`. The three visuals are deliberately different from the rejected dot plot, double curve and hub-to-activity diagram: they use client wordmarks as **visual anchors**, product badges as the CIB architecture and public transactions as the finance message.

## Individual visuals

1. [Option A — European deal ecosystem](OPTION_1_deal_ecosystem_logos.png)
   A flow from BNP Paribas CIB / CACIB to CIB products and selected public client cases. Best for explaining the European platform in under one minute.
2. [Option B — Client-to-solution journey](OPTION_2_client_solution_journey_logos.png)
   A true flow architecture: client logo and need on the left, CIB product in the middle, public mandate or transaction outcome on the right. Best when the committee needs a one-minute, verifiable story.
3. [Option C — CIB franchise universe / risk-product map](OPTION_3_risk_product_map_logos.png)
   A bubble/portfolio composition separating balance-sheet intensity from market and operational complexity. Best for a finance committee discussion, provided the qualitative nature is explained orally.

[Comparison PDF — all three pages](MARKETING_FINANCE_OPTIONS.pdf)

## Recommendation

Use **Option A** as the leading candidate after the approved Europe map. The reading path is immediate — **platform → product → public client outcome** — and the split BNP Paribas / CACIB lanes create a clear bridge to the following Luxembourg focus without claiming that every city or client is represented. Keep Option B as the more marketing-led backup. Use Option C only if the oral presentation explicitly says that the axes are qualitative and illustrative, not measured risk or revenue data.

## Perimeter and source discipline

- `PUBLIC EXAMPLES / ILLUSTRATIVE / NOT EXHAUSTIVE` is printed on every figure.
- Logos do **not** prove revenue, market share, booking location, legal-entity coverage or an exhaustive client portfolio.
- Flow direction and bubble position are explanatory only; no arrow width, logo size or coordinate is a transaction amount or revenue measure.
- The public references shown are four different business stories: fund servicing, custody/settlement, a bond issuance and acquisition/refinancing financing. They should not be compared as like-for-like revenues.
- The figures use the public pages below as the deal/mandate evidence. The files in `data/logos/` are presentation assets copied from the provenance listed in `LOGO-SOURCES.md`; they are not evidence of a commercial relationship by themselves.

### Transaction / mandate sources printed on the figures

Option A also uses the selected hub examples in the repository's `data/europe_hubs_public.csv`:

- **[H1] BNP Paribas Securities Services locations**: <https://securities.cib.bnpparibas/who-we-are/our-locations/>
- **[H2] CACIB Leveraged Finance Europe locations**: <https://www.ca-cib.com/en/expertise/solutions-support-your-financing-strategy/supporting-your-financing-needs/leveraged-0>

These are selected public business-line location examples, not a complete footprint or a line-by-line booking map.

- **[S1] Janus Henderson — BNP Paribas Securities Services**, core banking and fund-servicing partner across selected European and Asia-Pacific markets:
  <https://securities.cib.bnpparibas/bnp-paribas-janus-henderson-core-banking-fund-servicing-europe-asia-pacific/>
- **[S2] UniCredit — BNP Paribas Securities Services**, custody and settlement mandate for selected entities in Italy, Germany and Luxembourg:
  <https://securities.cib.bnpparibas/unicredit-mandate-custody-and-settlement-services/>
- **[S3] Enel Finance International N.V. — CACIB**, joint bookrunner on the September 2025 USD 4.5bn multi-tranche senior unsecured bond issuance:
  <https://activity-report.ca-cib.com/market-activities/>
- **[S4] L’OCCITANE Group — CACIB**, financial adviser for a quasi-equity raise of up to €1.6bn and sole underwriter/bookrunner for €1.36bn of acquisition and refinancing facilities:
  <https://activity-report.ca-cib.com/loccitane-group-transaction/>

## Reproduce

From the repository root:

```bash
PYTHONPATH=travaux-groupe/Money-Banking/cib_graphs/src \
  /tmp/skema-graphs-venv/bin/python \
  travaux-groupe/Money-Banking/cib_graphs/src/build_logo_options.py
```

The script regenerates the three PNGs and `MARKETING_FINANCE_OPTIONS.pdf` from the selected local logo assets.
