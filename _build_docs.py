# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, HRFlowable, PageBreak
from PIL import Image as PILImage

NAVY = colors.HexColor("#1F3864")
GREY = colors.HexColor("#BFBFBF")

# ============ COVER LETTER PDF ============
s_n = ParagraphStyle('n', fontName='Helvetica-Bold', fontSize=15, leading=18, textColor=NAVY, spaceAfter=2)
s_ct = ParagraphStyle('ct', fontName='Helvetica', fontSize=8.8, leading=11, textColor=colors.HexColor("#333333"))
s_to = ParagraphStyle('to', fontName='Helvetica', fontSize=9.2, leading=12.4, textColor=colors.HexColor("#333333"))
s_p = ParagraphStyle('p', fontName='Helvetica', fontSize=9.4, leading=13.4, spaceAfter=7, alignment=4)
s_sig = ParagraphStyle('sg', fontName='Helvetica-Bold', fontSize=9.4, leading=13, spaceBefore=6)

def build_cover():
    doc = SimpleDocTemplate("Cover_Letter_Barclays_STS_2027_Calvin_MINANG.pdf", pagesize=A4,
        leftMargin=20*mm, rightMargin=20*mm, topMargin=16*mm, bottomMargin=15*mm,
        title="Cover Letter - Calvin MINANG - Barclays", author="Calvin MINANG")
    F = []
    F.append(Paragraph("CALVIN MINANG", s_n))
    F.append(Paragraph("Paris, France &nbsp;·&nbsp; +33 7 52 97 58 09 &nbsp;·&nbsp; calvin.minang@skema.edu", s_ct))
    F.append(Paragraph("linkedin.com/in/calvin-minang &nbsp;·&nbsp; github.com/Calvin29990", s_ct))
    F.append(Spacer(1, 10))
    F.append(HRFlowable(width="100%", thickness=0.8, color=NAVY, spaceAfter=10))
    F.append(Paragraph("<b>Barclays Europe — Early Careers</b>", s_to))
    F.append(Paragraph("Sales, Trading and Structuring Off Cycle Internship Programme 2027", s_to))
    F.append(Paragraph("52 avenue Hoche, 75008 Paris", s_to))
    F.append(Spacer(1, 12))
    F.append(Paragraph("Dear Hiring Team,", s_to))
    F.append(Spacer(1, 7))
    F.append(Paragraph("I am applying for the <b>Sales, Trading and Structuring Off Cycle Internship Programme 2027</b> in Paris. I am a final-year student on SKEMA Business School's Programme Grande Ecole (Master grade) and MSc Corporate Financial Management, available from mid-December 2026.", s_p))
    F.append(Paragraph("Two things set my application apart, and I would rather state them plainly than bury them.", s_p))
    F.append(Paragraph("<b>The first is that I have actually sold.</b> At FinStart.io I ran B2B prospecting for a finance-focused platform — roughly 100 emails a day, 500 a week, with every response tracked. At SKEMA Job Service Paris I built partnerships for our student staffing business: our team closed EUR 19,100 of revenue, placed 125 students across 35 assignments and signed five partners, including EY. I understand that sales is a discipline before it is a product — qualifying a need, resisting the temptation to pitch too early, and following up without wearing the client down. Most candidates for a sales position have never sold anything.", s_p))
    F.append(Paragraph("<b>The second is that I build my own tools to understand markets.</b> I built CalvinX, a Bloomberg-style cross-asset dashboard covering FX, equity indices, rates, commodities and volatility. I built ShockLab, a portfolio stress-testing engine in Python and SQL that replays real market analogues — Lehman, COVID, the Soleimani strike — to quantify the P&amp;L impact on a multi-asset book. I also built a Black-Scholes pricer with Delta, Gamma and Vega, which I used to locate the gamma peak of an option book during the Petrobras oil shock and to validate the short-gamma mechanism against the March 2020 crash. None of this was coursework.", s_p))
    F.append(Paragraph("Professionally, I spent five months at BPCE Assurances producing daily multi-asset reporting for investment committees — FX pairs, equity indices, rate curves and credit spreads — and running Bloomberg BQL extractions on FX forwards and swaps, with monitoring of the EURSTR and SOFR curves. That role taught me where the numbers that reach a trading floor actually come from.", s_p))
    F.append(Paragraph("I am a FRM candidate (GARP), currently completing the AMF certification, and I hold the Citi Markets Sales &amp; Trading certificate. I am bilingual in French and English, with Spanish at B2.", s_p))
    F.append(Paragraph("Mr Olivier Moser, Sales Manager at Barclays Private Bank, kindly responded to my application and directed me to your programme, authorising me to mention his name. My enclosed CV and project portfolio provide further detail.", s_p))
    F.append(Paragraph("I am available from mid-December 2026, which matches the programme's start date, and I would welcome the opportunity to discuss how my background fits your desk.", s_p))
    F.append(Spacer(1, 4))
    F.append(Paragraph("Yours sincerely,", s_to))
    F.append(Paragraph("Calvin MINANG", s_sig))
    F.append(Spacer(1, 6))
    F.append(Paragraph("<i>Enclosures: Curriculum Vitae · Project Portfolio</i>", s_ct))
    doc.build(F)
    print("OK -> Cover_Letter_Barclays_STS_2027_Calvin_MINANG.pdf")

# ============ PORTFOLIO PDF ============
def rl_image(path, max_w, max_h):
    im = PILImage.open(path)
    w, h = im.size
    ratio = min(max_w / w, max_h / h)
    return RLImage(path, width=w*ratio, height=h*ratio)

def build_portfolio():
    s_n = ParagraphStyle('n', fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=NAVY, spaceAfter=4)
    s_t = ParagraphStyle('t', fontName='Helvetica-Bold', fontSize=11.5, leading=15, textColor=colors.HexColor("#333333"), spaceAfter=3)
    s_c = ParagraphStyle('c', fontName='Helvetica', fontSize=9, leading=12, textColor=colors.HexColor("#333333"))
    s_h = ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=12.5, leading=15, textColor=NAVY, spaceBefore=4, spaceAfter=4)
    s_b = ParagraphStyle('b', fontName='Helvetica', fontSize=9.2, leading=12.8, spaceAfter=4, alignment=4)
    s_cap = ParagraphStyle('cap', fontName='Helvetica-Oblique', fontSize=8.2, leading=10.6, textColor=colors.HexColor("#666666"), spaceBefore=3)

    doc = SimpleDocTemplate("Portfolio_Calvin_MINANG_EN.pdf", pagesize=A4,
        leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=14*mm,
        title="Calvin MINANG - Project Portfolio", author="Calvin MINANG")
    F = []
    # Cover
    F.append(Spacer(1, 55))
    F.append(Paragraph("CALVIN MINANG", s_n))
    F.append(Paragraph("PROJECT PORTFOLIO — GLOBAL MARKETS", s_t))
    F.append(HRFlowable(width="100%", thickness=1, color=NAVY, spaceBefore=6, spaceAfter=8))
    F.append(Paragraph("Three self-directed market projects: a cross-asset market terminal, a portfolio stress-testing engine and an option pricer with Greeks.", s_c))
    F.append(Spacer(1, 8))
    F.append(Paragraph("calvin.minang@skema.edu &nbsp;·&nbsp; +33 7 52 97 58 09", s_c))
    F.append(Paragraph("github.com/Calvin29990 &nbsp;·&nbsp; calvin-minibloomberg.netlify.app", s_c))
    F.append(PageBreak())

    # Project 1
    F.append(Paragraph("1 · CalvinX — Cross-Asset Market Terminal", s_h))
    F.append(Paragraph("JavaScript · Client-side · Public demo", ParagraphStyle('m', fontName='Helvetica-Oblique', fontSize=8.6, leading=11, textColor=colors.HexColor("#666666"), spaceAfter=5)))
    F.append(rl_image("portfolio-assets/calvinx.jpg", 174*mm, 105*mm))
    F.append(Paragraph("Live market monitor: instrument search with KPI panel (last price, daily change, volume, day range), candlestick chart with SMA-20/SMA-50 overlays, and a sector/keyword-filtered news feed.", s_b))
    F.append(Paragraph("Built as a single-page app: data fetching, client-side indicators, regime detection (risk-on / risk-off) and Excel export. No framework — plain JavaScript, purpose-built to understand what a desk screen actually displays.", s_b))
    F.append(Paragraph("Demo: calvin-minibloomberg.netlify.app &nbsp;|&nbsp; github.com/Calvin29990/calvinx-market-terminal", s_cap))
    F.append(PageBreak())

    # Project 2
    F.append(Paragraph("2 · ShockLab — Portfolio Stress-Testing Engine", s_h))
    F.append(Paragraph("Python · SQL · Machine Learning", ParagraphStyle('m2', fontName='Helvetica-Oblique', fontSize=8.6, leading=11, textColor=colors.HexColor("#666666"), spaceAfter=5)))
    F.append(Paragraph("Scenario replay: historical analogues applied to a multi-asset book", s_b))
    F.append(Paragraph("The engine replays real market analogues — Lehman 2008, COVID 2020, the Soleimani strike, the 2016 US election — to quantify the P&amp;L impact on a diversified portfolio over the 20 days following each shock.", s_b))
    F.append(rl_image("portfolio-assets/shocklab_trajectory.jpg", 150*mm, 82*mm))
    F.append(Paragraph("S&amp;P 500 trajectory (base 100) across four historical shocks — from fade to cascade.", s_cap))
    F.append(Spacer(1, 5))
    F.append(Paragraph("Scenario output: Iran–US / Strait of Hormuz", s_b))
    F.append(rl_image("portfolio-assets/shocklab_scenario.jpg", 150*mm, 82*mm))
    F.append(Paragraph("Estimated P&amp;L by asset class (USD m): long Brent and commodities, long Treasuries and gold, short S&amp;P 500 and short EUR/USD — the classic geopolitical risk-off trade.", s_cap))
    F.append(PageBreak())

    # Project 3
    F.append(Paragraph("3 · Black-Scholes Option Pricer — Options & Greeks", s_h))
    F.append(Paragraph("Excel · VBA · Applied case study", ParagraphStyle('m3', fontName='Helvetica-Oblique', fontSize=8.6, leading=11, textColor=colors.HexColor("#666666"), spaceAfter=5)))
    F.append(rl_image("portfolio-assets/bs_pricer.jpg", 150*mm, 112*mm))
    F.append(Paragraph("Put pricing and sensitivities under a stress scenario (Petrobras, March 2020 crash).", s_cap))
    F.append(Spacer(1, 6))
    F.append(Paragraph("The pricer computes price, Delta, Gamma and Vega for European options. I used it to study the <b>gamma peak</b> of an option book during the Petrobras oil shock, and to validate the short-gamma mechanism against the March 2020 crash.", s_b))
    F.append(Paragraph("The result is visible in the table: as spot falls from 13 to 5.5 and implied volatility rises from 40% to 90%, put Delta moves from −0.435 to −0.951 while Gamma collapses from 0.151 to 0.041. A desk short this put must buy roughly 0.5 additional delta per contract to stay hedged — forced hedging that amplifies the decline. That is short gamma in practice, and it is why the crash accelerates.", s_b))
    doc.build(F)
    print("OK -> Portfolio_Calvin_MINANG_EN.pdf")

build_cover()
build_portfolio()
