# CIB executive graphics

Three Python-generated, director-ready visuals for the BNP Paribas / CACIB benchmark:

1. `output/01_europe_cib_footprint.png` — selected public European hubs, with Paris and Luxembourg highlighted;
2. `output/02_q2_momentum_slope.png` — Q2 2025 rebased to 100, showing Q2 2026 reported momentum;
3. `output/03_q2_business_engine_dotplot.png` — Q2 2026 year-on-year change by business engine;
4. `output/CIB_EXECUTIVE_GRAPHS.pdf` — the three figures in a presentation-ready PDF.

## Rebuild

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python src/build_cib_graphs.py
```

## Methodological guardrails

- The Q2 figures use the latest official publications available in the working brief: BNP Paribas 2Q26 results and Crédit Agricole CIB / Crédit Agricole S.A. Q2/H1 2026 reporting.
- The BNP and CACIB labels in the public reports are not perfectly identical. The charts show the reporting labels and state the limitation; they are not presented as a league table of group size.
- The map shows **selected disclosed hubs**, not an exhaustive group footprint. It uses official business-line or local-entity location pages and keeps the source URL in `data/europe_hubs_public.csv`.
- For Luxembourg, do not treat `Crédit Agricole CIB Finance Luxembourg S.A.` as the full CACIB Luxembourg commercial platform: its public financial report describes an issuing-vehicle activity. Confirm the exact local CACIB perimeter before using local financial KPIs.
- Likewise, do not substitute BGL BNP Paribas group figures for a BNP Paribas CIB Luxembourg-only figure. A local Luxembourg comparison should either use matched local business perimeters or explicitly present the entity/perimeter difference as the conclusion.

## Public source trail

- BNP Paribas: https://invest.bnpparibas/en/document/2q26-pr
- BNP Paribas Securities Services locations: https://securities.cib.bnpparibas/who-we-are/our-locations/
- CACIB Q2/H1 2026: https://www.ca-cib.com/en/news/financial-results-second-quarter-and-first-half-2026
- CACIB selected European business-line locations: https://www.ca-cib.com/en/expertise/solutions-support-your-financing-strategy/supporting-your-financing-needs/leveraged-0
- CACIB Finance Luxembourg public report: see the exact URL in `data/europe_hubs_public.csv`.
- Europe country geometry: `datasets/geo-countries` via GitHub, reduced to the countries shown in `data/europe_countries.geojson`.
