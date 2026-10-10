"""Build an editable six-slide Canva-style deck for the Credit Bureaus bonus."""
from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "bonus_credit_scoring" / "assets"
OUT = ROOT / "bonus_credit_scoring" / "output"
OUT.mkdir(parents=True, exist_ok=True)
PPTX = OUT / "BONUS-2-CREDIT-BUREAUS-TEAM-5.pptx"

# Palette inspired by modern Canva finance templates, with brand accents.
BG = "F8F6F0"
NAVY = "172B4D"
INK = "1F2937"
MUTED = "667085"
LINE = "D8DEE8"
PANEL = "FFFFFF"
SOFT_BLUE = "EAF3F8"
SOFT_TEAL = "E8F5F3"
SOFT_MAGENTA = "F8EEF5"
EQUIFAX = "9B1C3F"
EXPERIAN = "2F68A7"
TRANSUNION = "08A5BE"
GOLD = "D6A33A"
CORAL = "D96C61"
WHITE = "FFFFFF"

TEAM = "Team 5  ·  Chapter 10 — The Banking Business"
MEMBERS = "Jules Metayer  ·  Manal Ouahmed  ·  Matteo Patussi  ·  Meng Qi  ·  Juan Romeromejia  ·  Calvin Minang"

SOURCES = {
    "Equifax — About Equifax": "https://www.equifax.com/about-equifax/",
    "Equifax — Credit reports and services": "https://www.equifax.com/personal/credit-report-services/",
    "Experian plc — About us": "https://www.experianplc.com/about-us/",
    "Experian — Consumer information": "https://www.experian.com/consumer-information/",
    "Experian — What is a credit score?": "https://www.experian.com/blogs/ask-experian/what-is-a-credit-score/",
    "TransUnion — About us": "https://www.transunion.com/about-us",
    "TransUnion — Information for Good": "https://newsroom.transunion.com/transunion-announces-its-new-brand-platform--information-for-good/",
    "FICO — Scores across bureaus": "https://www.myfico.com/credit-education/faq/scores/do-i-need-to-know-my-scores-for-all-bureaus",
    "CFPB — Credit reports and scores": "https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/",
}


def rgb(hex_value: str) -> RGBColor:
    hex_value = hex_value.lstrip("#")
    return RGBColor(int(hex_value[0:2], 16), int(hex_value[2:4], 16), int(hex_value[4:6], 16))


def set_fill(shape, color: str, transparency: int = 0):
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb(color)
    shape.fill.transparency = transparency
    shape.line.fill.background()


def add_shape(slide, kind, x, y, w, h, fill=WHITE, line=None, radius=True):
    shape = slide.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    set_fill(shape, fill)
    if line:
        shape.line.color.rgb = rgb(line)
        shape.line.width = Pt(0.8)
    else:
        shape.line.fill.background()
    return shape


def add_text(slide, text, x, y, w, h, size=14, color=INK, bold=False, italic=False,
             align=PP_ALIGN.LEFT, font="Aptos", valign=MSO_ANCHOR.TOP, margin=0.04,
             all_caps=False):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = Inches(margin)
    tf.margin_right = Inches(margin)
    tf.margin_top = Inches(margin)
    tf.margin_bottom = Inches(margin)
    tf.vertical_anchor = valign
    p = tf.paragraphs[0]
    p.alignment = align
    p.space_after = Pt(0)
    run = p.add_run()
    run.text = text.upper() if all_caps else text
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = rgb(color)
    return shape


def add_multiline(slide, lines, x, y, w, h, size=11, color=INK, bullet=False,
                  line_gap=1.1, margin=0.05):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = Inches(margin)
    tf.margin_right = Inches(margin)
    tf.margin_top = Inches(margin)
    tf.margin_bottom = Inches(margin)
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = ("• " if bullet else "") + line
        p.font.name = "Aptos"
        p.font.size = Pt(size)
        p.font.color.rgb = rgb(color)
        p.space_after = Pt(5)
        p.line_spacing = line_gap
    return shape


def add_logo(slide, filename, x, y, w, h=None):
    path = ASSETS / filename
    if h is None:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y), width=Inches(w))
    else:
        slide.shapes.add_picture(str(path), Inches(x), Inches(y), width=Inches(w), height=Inches(h))


def add_header(slide, section, number, title, subtitle=None):
    add_text(slide, "BONUS  ·  CREDIT BUREAUS", 0.55, 0.28, 4.0, 0.22, size=8.5,
             color=TRANSUNION, bold=True, all_caps=True)
    add_text(slide, f"{number:02d}", 12.15, 0.27, 0.55, 0.28, size=9,
             color=MUTED, bold=True, align=PP_ALIGN.RIGHT)
    add_shape(slide, MSO_SHAPE.RECTANGLE, 0.55, 0.62, 0.46, 0.055, fill=GOLD)
    add_text(slide, section.upper(), 1.12, 0.54, 3.0, 0.22, size=8.2,
             color=MUTED, bold=True, all_caps=True)
    add_text(slide, title, 0.55, 0.90, 11.9, 0.62, size=25, color=NAVY, bold=True)
    if subtitle:
        add_text(slide, subtitle, 0.58, 1.54, 11.4, 0.35, size=11, color=MUTED, italic=True)


def add_footer(slide, source_text, number):
    add_shape(slide, MSO_SHAPE.RECTANGLE, 0.55, 7.05, 12.2, 0.012, fill=LINE)
    add_text(slide, source_text, 0.58, 7.10, 11.1, 0.18, size=6.5, color=MUTED)
    add_text(slide, f"{number} / 06", 12.1, 7.08, 0.62, 0.18, size=7.0,
             color=MUTED, align=PP_ALIGN.RIGHT)


def add_card(slide, x, y, w, h, fill=WHITE, line=LINE, radius=True):
    return add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
                     x, y, w, h, fill=fill, line=line)


def add_logo_card(slide, x, y, w, h, logo, accent, fill):
    add_card(slide, x, y, w, h, fill=fill, line=fill)
    add_shape(slide, MSO_SHAPE.RECTANGLE, x, y, 0.08, h, fill=accent)
    add_logo(slide, logo, x + 0.26, y + 0.18, 1.45)


def slide_base(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = rgb(BG)
    return slide


def build_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    # Remove the default first slide if present.
    while prs.slides:
        r_id = prs.slides._sldIdLst[0].rId
        prs.part.drop_rel(r_id)
        del prs.slides._sldIdLst[0]

    # Slide 1 — cover
    slide = slide_base(prs)
    add_text(slide, "MONEY, BANKING AND FINANCIAL MARKETS", 0.65, 0.42, 5.5, 0.25,
             size=9, color=TRANSUNION, bold=True, all_caps=True)
    add_text(slide, "BONUS  ·  CREDIT BUREAUS", 0.65, 0.78, 4.0, 0.25,
             size=9, color=MUTED, bold=True, all_caps=True)
    add_text(slide, "Credit information\nand scoring", 0.65, 1.30, 6.0, 1.35,
             size=31, color=NAVY, bold=True)
    add_text(slide, "Equifax  ·  Experian  ·  TransUnion", 0.70, 2.86, 5.5, 0.35,
             size=14, color=INK, bold=True)
    add_text(slide, "How data supports lending — and why a score is never the whole decision.",
             0.70, 3.34, 5.8, 0.55, size=12, color=MUTED)
    add_card(slide, 7.12, 1.12, 5.55, 3.60, fill=PANEL, line=LINE)
    add_text(slide, "THREE SIGNALS  ·  ONE DECISION CONTEXT", 7.52, 1.45, 4.55, 0.3,
             size=8.5, color=MUTED, bold=True, all_caps=True)
    add_logo_card(slide, 7.52, 1.95, 4.74, 0.72, "equifax_logo.png", EQUIFAX, "FDF5F7")
    add_logo_card(slide, 7.52, 2.82, 4.74, 0.72, "experian_logo.png", EXPERIAN, "F2F7FB")
    add_logo_card(slide, 7.52, 3.69, 4.74, 0.72, "transunion_logo.png", TRANSUNION, "ECFBFC")
    add_text(slide, "Team 5  ·  Chapter 10 — The Banking Business", 0.70, 5.86, 6.2, 0.25,
             size=10, color=NAVY, bold=True)
    add_text(slide, MEMBERS, 0.70, 6.22, 11.8, 0.38, size=8.4, color=MUTED)
    add_text(slide, "Professor Dhafer Saidane  ·  Due 15 October 2026", 0.70, 6.63, 6.5, 0.24,
             size=8, color=MUTED)
    add_footer(slide, "Sources: CFPB; FICO; official company pages listed on slide 6. Accessed 10 October 2026.", 1)

    # Slide 2 — definitions
    slide = slide_base(prs)
    add_header(slide, "Start with the distinction", 2, "A report is not a score — and a score is not a decision",
               "The basic vocabulary behind modern credit information.")
    cards = [
        (0.65, "01", "Credit bureau", "Collects, organises and supplies credit-related information.", SOFT_BLUE, EXPERIAN),
        (4.52, "02", "Credit report", "A record of reported information about a consumer or business.", SOFT_TEAL, TRANSUNION),
        (8.39, "03", "Credit score", "An output produced by a scoring model using selected information.", SOFT_MAGENTA, EQUIFAX),
    ]
    for x, no, title, body, fill, accent in cards:
        add_card(slide, x, 2.25, 3.55, 2.25, fill=fill, line=fill)
        add_text(slide, no, x + 0.28, 2.53, 0.45, 0.3, size=11, color=accent, bold=True)
        add_text(slide, title, x + 0.28, 2.97, 2.9, 0.35, size=17, color=NAVY, bold=True)
        add_text(slide, body, x + 0.28, 3.58, 2.95, 0.65, size=11, color=INK)
    add_card(slide, 0.65, 5.05, 11.96, 0.95, fill=NAVY, line=NAVY)
    add_text(slide, "KEY CONTROL POINT", 0.95, 5.28, 1.75, 0.25, size=8, color=GOLD, bold=True, all_caps=True)
    add_text(slide, "A credit score supports a lending decision; the lender remains responsible for the final decision.",
             2.75, 5.22, 9.35, 0.42, size=15, color=WHITE, bold=True)
    add_footer(slide, "Sources: Consumer Financial Protection Bureau — Credit reports and scores; FICO — Scores across credit bureaus.", 2)

    # Slide 3 — decision journey
    slide = slide_base(prs)
    add_header(slide, "Decision journey", 3, "From reported information to a bank decision",
               "A conceptual process — not a proprietary process attributed to one company.")
    steps = [
        ("01", "Application", "A consumer or business applies for credit."),
        ("02", "Reporting", "Lenders and data furnishers report information."),
        ("03", "Credit file", "The bureau organises a report or data product."),
        ("04", "Scoring", "A model produces a score or risk indicator."),
        ("05", "Underwriting", "The lender adds affordability, collateral and policy."),
        ("06", "Outcome", "Approval, rejection, pricing, limit or monitoring."),
    ]
    x_positions = [0.62, 2.73, 4.84, 6.95, 9.06, 11.17]
    for i, (no, title, body) in enumerate(steps):
        x = x_positions[i]
        add_card(slide, x, 2.45, 1.62, 2.15, fill=PANEL, line=LINE)
        add_shape(slide, MSO_SHAPE.OVAL, x + 0.48, 2.68, 0.66, 0.66, fill=TRANSUNION if i in (2, 3) else NAVY)
        add_text(slide, no, x + 0.48, 2.86, 0.66, 0.22, size=9, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, title, x + 0.14, 3.57, 1.34, 0.28, size=11, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
        add_text(slide, body, x + 0.14, 3.98, 1.34, 0.50, size=8.4, color=MUTED, align=PP_ALIGN.CENTER)
        if i < len(steps) - 1:
            add_shape(slide, MSO_SHAPE.CHEVRON, x + 1.72, 3.30, 0.32, 0.42, fill=GOLD)
    add_card(slide, 2.08, 5.35, 9.15, 0.72, fill=SOFT_TEAL, line=SOFT_TEAL)
    add_text(slide, "A score is one input among data, policy, affordability, regulation and human or automated review.",
             2.34, 5.55, 8.62, 0.25, size=12, color=NAVY, bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, "Sources: Consumer Financial Protection Bureau; FICO. The six-step sequence is an educational synthesis of those sources.", 3)

    # Slide 4 — comparison
    slide = slide_base(prs)
    add_header(slide, "Three companies", 4, "Three public emphases — not one universal score provider",
               "Mission statements are positioning; products, models and coverage must be verified separately.")
    columns = [
        (0.60, "equifax_logo.png", EQUIFAX, "Founded 1899", "Financial wellbeing\n+ data-driven decisions", ["Credit information", "Decision support", "Identity and fraud"], "FDF5F7"),
        (4.48, "experian_logo.png", EXPERIAN, "Current group established 1996", "Financial inclusion\n+ consumer information", ["Credit information", "Decision analytics", "Fraud and identity"], "F2F7FB"),
        (8.36, "transunion_logo.png", TRANSUNION, "Founded 1968", "Information for Good\n+ trust", ["Credit information", "Risk decisioning", "Fraud and identity"], "ECFBFC"),
    ]
    for x, logo, accent, history, positioning, services, fill in columns:
        add_card(slide, x, 2.25, 3.55, 3.85, fill=fill, line=fill)
        add_logo(slide, logo, x + 0.30, 2.55, 1.58)
        add_text(slide, history, x + 0.30, 3.25, 2.85, 0.20, size=8.2, color=accent, bold=True)
        add_shape(slide, MSO_SHAPE.RECTANGLE, x + 0.30, 3.55, 2.92, 0.012, fill=accent)
        add_text(slide, "PUBLIC POSITIONING", x + 0.30, 3.76, 2.8, 0.22, size=7.3, color=MUTED, bold=True, all_caps=True)
        add_text(slide, positioning, x + 0.30, 4.04, 2.84, 0.62, size=13, color=NAVY, bold=True)
        add_text(slide, "SERVICES TO VERIFY", x + 0.30, 4.80, 2.8, 0.22, size=7.3, color=MUTED, bold=True, all_caps=True)
        add_multiline(slide, services, x + 0.30, 5.08, 2.82, 0.7, size=9.6, color=INK, bullet=True, line_gap=1.0)
    add_footer(slide, "History: official company information pages listed on slide 6. Positioning is paraphrased and is not a performance ranking.", 4)

    # Slide 5 — limits
    slide = slide_base(prs)
    add_header(slide, "Critical lens", 5, "What the comparison must not over-interpret",
               "Rigorous finance means stating the limits of the data and the model.")
    add_card(slide, 0.65, 2.15, 5.72, 3.95, fill=PANEL, line=LINE)
    add_text(slide, "WHAT DIFFERS", 1.00, 2.53, 2.2, 0.24, size=8.5, color=TRANSUNION, bold=True, all_caps=True)
    add_multiline(slide, [
        "Scoring models and score ranges",
        "Data coverage and reporting timing",
        "Products, customers and geography",
        "Lender policy and underwriting rules",
    ], 1.00, 2.98, 4.75, 1.75, size=13, color=INK, bullet=True, line_gap=1.15)
    add_card(slide, 6.92, 2.15, 5.72, 3.95, fill=SOFT_MAGENTA, line=SOFT_MAGENTA)
    add_text(slide, "WHY IT MATTERS", 7.27, 2.53, 2.2, 0.24, size=8.5, color=EQUIFAX, bold=True, all_caps=True)
    add_multiline(slide, [
        "Incomplete, outdated or incorrect data",
        "Privacy, transparency and fairness",
        "Potential bias in automated decisions",
        "A score is not a full affordability assessment",
    ], 7.27, 2.98, 4.75, 1.75, size=13, color=INK, bullet=True, line_gap=1.15)
    add_card(slide, 1.68, 6.25, 9.98, 0.40, fill=NAVY, line=NAVY)
    add_text(slide, "No universal score · no automatic ranking · no final decision without the lender", 1.90, 6.36, 9.55, 0.16,
             size=9.8, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_footer(slide, "Sources: Consumer Financial Protection Bureau; FICO; official company pages. No score model or market ranking is inferred here.", 5)

    # Slide 6 — conclusion/sources
    slide = slide_base(prs)
    add_header(slide, "Close with the lesson", 6, "Information improves decisions — but it is not the decision",
               "A concise conclusion for the optional credit-bureaus exercise.")
    add_card(slide, 0.65, 2.10, 7.05, 2.25, fill=NAVY, line=NAVY)
    add_text(slide, "CONCLUSION", 1.02, 2.47, 1.55, 0.24, size=8.2, color=GOLD, bold=True, all_caps=True)
    conclusion = ("Equifax, Experian and TransUnion use information and analytics to support credit and risk decisions, "
                  "but they are not identical score providers. Their data, models, products and geographic perimeters differ. "
                  "The final credit decision remains the responsibility of the lender.")
    add_text(slide, conclusion, 1.02, 2.93, 6.22, 0.95, size=16, color=WHITE, bold=True)
    add_card(slide, 8.05, 2.10, 4.58, 2.25, fill=SOFT_TEAL, line=SOFT_TEAL)
    add_text(slide, "MAIN LESSON", 8.40, 2.47, 1.55, 0.24, size=8.2, color=TRANSUNION, bold=True, all_caps=True)
    add_text(slide, "A credit score is an input to risk assessment — not a complete measure of a borrower’s financial situation.",
             8.40, 2.94, 3.82, 0.78, size=14, color=NAVY, bold=True)
    add_text(slide, "VERIFIED SOURCES", 0.70, 4.70, 2.0, 0.22, size=8.2, color=MUTED, bold=True, all_caps=True)
    source_lines = [
        "Equifax: https://www.equifax.com/about-equifax/ | https://investor.equifax.com/company-information",
        "Equifax services: https://www.equifax.com/personal/credit-report-services/",
        "Experian: https://www.experianplc.com/about-us/ | https://www.experian.com/corporate/principal-businesses",
        "Experian consumer information: https://www.experian.com/consumer-information/",
        "Experian score explainer: https://www.experian.com/blogs/ask-experian/what-is-a-credit-score/",
        "TransUnion: https://www.transunion.com/about-us",
        "TransUnion Information for Good: https://newsroom.transunion.com/transunion-announces-its-new-brand-platform--information-for-good/",
        "FICO: https://www.myfico.com/credit-education/faq/scores/do-i-need-to-know-my-scores-for-all-bureaus",
        "CFPB: https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/",
    ]
    add_multiline(slide, source_lines, 0.70, 4.96, 11.85, 1.55, size=6.1, color=MUTED, bullet=False, line_gap=0.88)
    add_footer(slide, "Accessed 10 October 2026. Official sources only; historical dates and unsupported statistics intentionally omitted.", 6)

    prs.save(PPTX)
    print(PPTX)


if __name__ == "__main__":
    build_deck()
