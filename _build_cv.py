# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

NAVY = colors.HexColor("#1F3864")
GREY = colors.HexColor("#BFBFBF")

NAME = "CALVIN MINANG"
TITLE = "GLOBAL MARKETS SALES  |  FX, RATES & EQUITIES"
SUB = "Available from mid-December 2026"
CONTACT = "+33 7 52 97 58 09  |  calvin.minang@skema.edu  |  Paris, France"
LINKS = "linkedin.com/in/calvin-minang  |  github.com/Calvin29990  |  calvin-minibloomberg.netlify.app"

SECTIONS = [
 ("PROFILE", [
   "Final-year student in SKEMA Business School's Programme Grande Ecole (Master grade) and MSc Corporate Financial Management. Multi-asset reporting and market monitoring; B2B prospecting, partner CRM and business development. Target: Global Markets Sales Desk - FX Sales, Rates Sales, Cross-Asset Sales and equity derivatives."]),
 ("EDUCATION", [
   "SKEMA Business School | Jul 2022 - Dec 2026",
   "Programme Grande Ecole (M2) - Dual degree: MSc Corporate Financial Management",
   "Campus Belo Horizonte, Brazil. Coursework: FX & Arbitrage - Fixed Income - Valuation & Risk Management - Market Risk - Credit Risk - Financial Modelling",
   "Ipesup Paris - Preparatory classes for French business schools (CPGE ECE) | 2021 - 2022",
   "Intensive mathematics and economics"]),
 ("EXPERIENCE", [
   "BPCE Assurances - Multi-Asset Reporting Analyst (internship) | Jan - May 2024",
   "Scale: EUR 103bn of life-insurance assets under management, direct business",
   "- Daily production of multi-asset reporting for investment committees: FX pairs, equity indices, rates and credit spreads.",
   "- Dashboards and Bloomberg BQL extractions on FX forwards and swaps; monitoring of EURSTR and SOFR rate curves.",
   "- Excel/VBA automation and market materials on trends and volatility.",
   "",
   "SKEMA Business School - CRM & Partner Data Assistant | Oct - Dec 2025",
   "Executive Education / Marketing & Communication",
   "- Data cleaning, de-duplication and validation of the partner database.",
   "- Updated 537 contact records and 102 company records across the Dubai and Belo Horizonte campuses.",
   "",
   "FinStart.io - Sales (internship) | Jun - Aug 2023",
   "- B2B prospecting targeting independent consultants in finance, accounting, risk and compliance: approx. 100 emails per business day, 500 per week, with response tracking.",
   "- Sourcing and screening of profiles via APEC and LinkedIn; platform invitations.",
   "",
   "SKEMA Job Service Paris - Board Member, HR & Partnerships | Sep 2022 - Aug 2023",
   "Fixed-term contract",
   "- B2B prospecting and partnership development for the student staffing offering: pitch, needs qualification, interviews and HR events with SKEMA, EY and Stade de France.",
   "- Team results H1 2023: EUR 19,100 revenue, 125 students placed across 35 assignments, 5 partners including 4 new - EY, Roadbook, Auverprime and CDEFM."]),
 ("SELECTED PROJECTS", [
   "CalvinX - Cross-Asset Market Terminal (JavaScript)",
   "- Bloomberg-style dashboard covering FX, equity indices, rates, commodities and volatility. Demo: calvin-minibloomberg.netlify.app",
   "",
   "ShockLab - Portfolio Stress-Testing Engine (Python / SQL / Machine Learning)",
   "- Quantifies the impact of geopolitical and macroeconomic scenarios on a multi-asset portfolio using real market analogues; SQL event database and interpretable ML.",
   "",
   "Black-Scholes Option Pricer - Options & Greeks (Excel / VBA)",
   "- European option valuation with Delta, Gamma and Vega sensitivities; located the gamma peak of an option book during an oil shock (Petrobras case), validated on the March 2020 crash."]),
 ("SKILLS & CERTIFICATIONS", [
   "Sales Desk: B2B prospecting, pitch delivery, needs qualification, response tracking, CRM.",
   "Markets: FX (forwards, swaps), Rates, Fixed Income, equity derivatives, volatility, cross-asset monitoring, market risk (VaR).",
   "Tools: Bloomberg Terminal (BQL), Excel/VBA, Python (pandas, scikit-learn), SQL (BigQuery), R, JavaScript.",
   "Certifications: FRM candidate (GARP); AMF certification in progress; Citi Markets Sales & Trading (Forage); QuantInsti (Python for Trading; Options Trading Strategies in Python)."]),
 ("LANGUAGES", [
   "French (native)  |  English (professional)  |  Spanish (B2)  |  Portuguese (basic)"]),
]

s_name = ParagraphStyle('n', fontName='Helvetica-Bold', fontSize=17, leading=20, textColor=NAVY, spaceAfter=1)
s_tit = ParagraphStyle('t', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=colors.HexColor("#333333"), spaceAfter=2)
s_sub = ParagraphStyle('s', fontName='Helvetica-Oblique', fontSize=9, leading=12, textColor=colors.HexColor("#555555"))
s_ct = ParagraphStyle('c', fontName='Helvetica', fontSize=8.7, leading=11.5, textColor=colors.HexColor("#333333"))
s_sec = ParagraphStyle('sec', fontName='Helvetica-Bold', fontSize=9.6, leading=12, textColor=NAVY, spaceBefore=6, spaceAfter=2)
s_bul = ParagraphStyle('b', fontName='Helvetica', fontSize=8.6, leading=11.2, spaceAfter=0.6)
s_job = ParagraphStyle('j', fontName='Helvetica-Bold', fontSize=8.9, leading=11.4, spaceBefore=3, spaceAfter=0.5)

doc = SimpleDocTemplate("CV_Calvin_MINANG_EN.pdf", pagesize=A4,
        leftMargin=15*mm, rightMargin=15*mm, topMargin=12*mm, bottomMargin=11*mm,
        title="Calvin MINANG - CV", author="Calvin MINANG")
F = []
F.append(Paragraph(NAME, s_name))
F.append(Paragraph(TITLE, s_tit))
F.append(Paragraph(SUB, s_sub))
F.append(Spacer(1, 2))
F.append(Paragraph(CONTACT, s_ct))
F.append(Paragraph(LINKS, s_ct))
F.append(Spacer(1, 3))
F.append(HRFlowable(width="100%", thickness=1, color=NAVY, spaceAfter=2))

for title, lines in SECTIONS:
    F.append(Paragraph(title, s_sec))
    F.append(HRFlowable(width="100%", thickness=0.5, color=GREY, spaceAfter=2))
    for ln in lines:
        if not ln.strip():
            F.append(Spacer(1, 2))
            continue
        if ln.startswith("- "):
            F.append(Paragraph(ln[2:], s_bul, bulletText='\u2022'))
        elif title == "EXPERIENCE" and " | " in ln:
            F.append(Paragraph(ln, s_job))
        elif title == "EDUCATION" and (ln.startswith("SKEMA Business") or ln.startswith("Ipesup")):
            F.append(Paragraph(ln, s_job))
        elif title == "SELECTED PROJECTS" and not ln.startswith("-"):
            F.append(Paragraph(ln, s_job))
        else:
            F.append(Paragraph(ln, s_bul))
doc.build(F)
print("OK -> CV_Calvin_MINANG_EN.pdf")
