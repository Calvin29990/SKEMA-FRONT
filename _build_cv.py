# -*- coding: utf-8 -*-
"""CV Calvin MINANG - version anglaise, mise en page propre (dates alignees a droite)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
                                Table, TableStyle, KeepTogether)
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

NAVY = colors.HexColor("#1B3A5C")
ACCENT = colors.HexColor("#2E5C8A")
RULE = colors.HexColor("#C8D2DC")
DARK = colors.HexColor("#222222")
MID = colors.HexColor("#4A4A4A")

# ---------------- CONTENT ----------------
NAME = "CALVIN MINANG"
HEADLINE = "GLOBAL MARKETS SALES  ·  FX, RATES & EQUITIES"
AVAILABILITY = "Available from mid-December 2026  ·  Paris, France"
CONTACT = "+33 7 52 97 58 09  ·  calvin.minang@skema.edu  ·  linkedin.com/in/calvin-minang"
CONTACT2 = "github.com/Calvin29990  ·  calvin-minibloomberg.netlify.app"

PROFILE = ("Final-year student on SKEMA Business School's Programme Grande Ecole (Master grade) and "
           "MSc Corporate Financial Management. Multi-asset reporting and market monitoring; B2B "
           "prospecting, partner CRM and business development. Target: Global Markets Sales Desk - "
           "FX Sales, Rates Sales, Cross-Asset Sales and equity derivatives.")

# (left, right, [detail lines], [bullets])
EDUCATION = [
    ("SKEMA Business School", "Jul 2022 - Dec 2026",
     ["Programme Grande Ecole (M2) - Dual degree: MSc Corporate Financial Management",
      "Campus Belo Horizonte, Brazil",
      "<i>Coursework:</i> FX &amp; Arbitrage · Fixed Income · Valuation &amp; Risk Management · Market Risk · Credit Risk · Financial Modelling"],
     []),
    ("Ipesup Paris", "2021 - 2022",
     ["Preparatory classes for French business schools (CPGE ECE) - intensive mathematics and economics"],
     []),
]

EXPERIENCE = [
    ("BPCE Assurances", "Jan - May 2024",
     "<b>Multi-Asset Reporting Analyst</b> (internship) · Paris",
     ["Daily production of multi-asset reporting for investment committees: FX pairs, equity indices, rates and credit spreads.",
      "Dashboards and Bloomberg BQL extractions on FX forwards and swaps; monitoring of the &euro;STR and SOFR rate curves.",
      "Excel/VBA automation and market materials on trends and volatility."],
     "Scale: &euro;103bn of life-insurance assets under management, direct business"),
    ("SKEMA Business School", "Oct - Dec 2025",
     "<b>CRM &amp; Partner Data Assistant</b> · Executive Education",
     ["Data cleaning, de-duplication and validation of the partner database.",
      "Updated 537 contact records and 102 company records across the Dubai and Belo Horizonte campuses."],
     None),
    ("FinStart.io", "Jun - Aug 2023",
     "<b>Sales</b> (internship) · Paris",
     ["B2B prospecting targeting independent consultants in finance, accounting, risk and compliance: approx. 100 emails per business day, 500 per week, with full response tracking.",
      "Sourcing and screening of profiles via APEC and LinkedIn; platform invitations."],
     None),
    ("SKEMA Job Service Paris", "Sep 2022 - Aug 2023",
     "<b>Board Member - HR &amp; Partnerships</b> (fixed-term contract)",
     ["B2B prospecting and partnership development for the student staffing offering: pitch, needs qualification, interviews and HR events with SKEMA, EY and Stade de France.",
      "Team results H1 2023: &euro;19,100 revenue, 125 students placed across 35 assignments, 5 partners including 4 new (EY, Roadbook, Auverprime, CDEFM)."],
     None),
]

PROJECTS = [
    ("CalvinX - Cross-Asset Market Terminal", "JavaScript",
     "Bloomberg-style dashboard covering FX, equity indices, rates, commodities and volatility, with regime detection and Excel export. Live demo: calvin-minibloomberg.netlify.app"),
    ("ShockLab - Portfolio Stress-Testing Engine", "Python · SQL · Machine Learning",
     "Replays real market analogues (Lehman, COVID, Soleimani) to quantify the P&amp;L impact on a multi-asset portfolio over the 20 days following each shock; SQL event database and interpretable ML."),
    ("Black-Scholes Option Pricer - Options &amp; Greeks", "Excel · VBA",
     "European option valuation with Delta, Gamma and Vega; used to locate the gamma peak of an option book during the Petrobras oil shock and validated against the March 2020 crash."),
]

SKILLS = [
    ("Sales Desk", "B2B prospecting · pitch delivery · needs qualification · response tracking · CRM"),
    ("Markets", "FX (forwards, swaps) · Rates · Fixed Income · equity derivatives · volatility · cross-asset monitoring · market risk (VaR)"),
    ("Tools", "Bloomberg Terminal (BQL) · Excel/VBA · Python (pandas, scikit-learn) · SQL (BigQuery) · R · JavaScript"),
    ("Certifications", "FRM candidate (GARP) · AMF certification in progress · Citi Markets Sales &amp; Trading (Forage) · QuantInsti (Python for Trading; Options Trading Strategies in Python)"),
]

LANGUAGES = "French (native)  ·  English (professional)  ·  Spanish (B2)  ·  Portuguese (basic)"

# ---------------- STYLES ----------------
S_NAME = ParagraphStyle('n', fontName='Helvetica-Bold', fontSize=18, leading=19, textColor=NAVY, spaceAfter=0)
S_HEAD = ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=9.6, leading=12, textColor=ACCENT, spaceAfter=1)
S_AVAIL = ParagraphStyle('a', fontName='Helvetica-Oblique', fontSize=8.8, leading=11, textColor=MID, spaceAfter=1)
S_CT = ParagraphStyle('c', fontName='Helvetica', fontSize=8.6, leading=11, textColor=DARK)
S_SEC = ParagraphStyle('sec', fontName='Helvetica-Bold', fontSize=9.4, leading=11.5, textColor=NAVY, spaceBefore=0, spaceAfter=0)
S_LEFT = ParagraphStyle('l', fontName='Helvetica-Bold', fontSize=9.0, leading=11, textColor=DARK)
S_RIGHT = ParagraphStyle('r', fontName='Helvetica-Bold', fontSize=8.4, leading=11, textColor=ACCENT, alignment=2)
S_DET = ParagraphStyle('d', fontName='Helvetica', fontSize=8.4, leading=10.6, textColor=DARK, spaceAfter=0.2)
S_BUL = ParagraphStyle('b', fontName='Helvetica', fontSize=8.4, leading=10.6, textColor=DARK, spaceAfter=0.6, leftIndent=8)
S_NOTE = ParagraphStyle('no', fontName='Helvetica-Oblique', fontSize=7.9, leading=10.1, textColor=MID, spaceAfter=0.8)
S_PROJ = ParagraphStyle('p', fontName='Helvetica', fontSize=8.4, leading=10.6, textColor=DARK, spaceAfter=0.8, alignment=TA_JUSTIFY)
S_PROF = ParagraphStyle('pf', fontName='Helvetica', fontSize=8.5, leading=10.9, textColor=DARK, alignment=TA_JUSTIFY)

def section(title):
    t = Table([[Paragraph(title.upper(), S_SEC)]], colWidths=[180*mm])
    t.setStyle(TableStyle([('LINEBELOW', (0,0), (-1,-1), 1, NAVY),
                           ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
                           ('TOPPADDING', (0,0), (-1,-1), 0),
                           ('LEFTPADDING', (0,0), (-1,-1), 0)]))
    return [Spacer(1, 5), t, Spacer(1, 3)]

def hdr_row(left, right):
    t = Table([[Paragraph(left, S_LEFT), Paragraph(right, S_RIGHT)]], colWidths=[127*mm, 53*mm])
    t.setStyle(TableStyle([('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),0),
                           ('TOPPADDING',(0,0),(-1,-1),1), ('BOTTOMPADDING',(0,0),(-1,-1),0.5),
                           ('VALIGN',(0,0),(-1,-1),'BOTTOM')]))
    return t

story = []
story.append(Paragraph(NAME, S_NAME))
story.append(Spacer(1, 1.5))
story.append(Paragraph(HEADLINE, S_HEAD))
story.append(Paragraph(AVAILABILITY, S_AVAIL))
story.append(Spacer(1, 3))
story.append(HRFlowable(width="100%", thickness=0.7, color=RULE, spaceAfter=3))
story.append(Paragraph(CONTACT, S_CT))
story.append(Paragraph(CONTACT2, S_CT))

# PROFILE
story += section("Profile")
story.append(Paragraph(PROFILE, S_PROF))

# EDUCATION
story += section("Education")
for name, dates, details, bullets in EDUCATION:
    story.append(KeepTogether([hdr_row(name, dates)] + [Paragraph(d, S_DET) for d in details]))

# EXPERIENCE
story += section("Professional Experience")
for company, dates, role, bullets, note in EXPERIENCE:
    block = [hdr_row(company, dates), Paragraph(role, S_DET)]
    if note:
        block.append(Paragraph(note, S_NOTE))
    for b in bullets:
        block.append(Paragraph(b, S_BUL, bulletText='\u2022'))
    story.append(KeepTogether(block))
    story.append(Spacer(1, 3))

# PROJECTS
story += section("Selected Projects")
for title, tech, desc in PROJECTS:
    story.append(KeepTogether([
        hdr_row(title, tech),
        Paragraph(desc, S_PROJ)]))
    story.append(Spacer(1, 2.5))

# SKILLS
story += section("Skills &amp; Certifications")
rows = [[Paragraph(f"<b>{k}</b>", S_DET), Paragraph(v, S_DET)] for k, v in SKILLS]
t = Table(rows, colWidths=[27*mm, 153*mm])
t.setStyle(TableStyle([('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),0),
                       ('TOPPADDING',(0,0),(-1,-1),1), ('BOTTOMPADDING',(0,0),(-1,-1),1.2),
                       ('VALIGN',(0,0),(-1,-1),'TOP')]))
story.append(t)

# LANGUAGES
story += section("Languages")
story.append(Paragraph(LANGUAGES, S_DET))

doc = SimpleDocTemplate("CV_Calvin_MINANG_EN.pdf", pagesize=A4,
    leftMargin=14*mm, rightMargin=14*mm, topMargin=10*mm, bottomMargin=8*mm,
    title="Calvin MINANG - Curriculum Vitae", author="Calvin MINANG",
    subject="Global Markets Sales")
doc.build(story)
print("OK -> CV_Calvin_MINANG_EN.pdf")
