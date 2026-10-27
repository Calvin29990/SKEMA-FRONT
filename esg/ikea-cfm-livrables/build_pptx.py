"""Group presentation 'Why would we invest in IKEA?' - 5 slides, timed for 3 minutes (English).

Canva-inspired style (coloured blocks, big figures); simplified IKEA logo drawn with native shapes.
Speaker notes contain the script, timing and the detailed points, so nothing from the longer version is lost.
All figures come from the Ingka ESG Profile and the IKEA one-pager (see notes on each slide).

Usage: python3 build_pptx.py
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "Group-IKEA-Why-invest-3min.pptx")

BLUE = RGBColor(0x00, 0x58, 0xA3)
YEL = RGBColor(0xFF, 0xDA, 0x1A)
INK = RGBColor(0x1A, 0x1A, 0x1A)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREY = RGBColor(0x5F, 0x63, 0x68)
LIGHT = RGBColor(0xF3, 0xF5, 0xF8)
GREEN = RGBColor(0x1E, 0x7B, 0x4A)
RED = RGBColor(0xB3, 0x26, 0x1E)
FONT = "Arial"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]


def box(slide, x, y, w, h, fill, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12):
    shp = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    shp.shadow.inherit = False
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        shp.adjustments[0] = radius
    return shp


def text(slide, x, y, w, h, runs, size=18, color=INK, bold=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, shape=None):
    """runs: a string, or a list of paragraphs (str, or (str, {options}))."""
    tb = shape if shape is not None else slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.08)
    tf.margin_top = tf.margin_bottom = Inches(0.04)
    paras = runs if isinstance(runs, list) else [runs]
    for i, p_item in enumerate(paras):
        opts = {}
        if isinstance(p_item, tuple):
            p_item, opts = p_item
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = opts.get("align", align)
        p.space_after = Pt(opts.get("space", 6))
        r = p.add_run()
        r.text = p_item
        f = r.font
        f.name = FONT
        f.size = Pt(opts.get("size", size))
        f.bold = opts.get("bold", bold)
        f.color.rgb = opts.get("color", color)
    return tb


def notes(slide, txt):
    slide.notes_slide.notes_text_frame.text = txt


def logo(slide, x, y, scale=1.0):
    """Simplified IKEA logo: blue rectangle + yellow oval + the word IKEA."""
    w, h = 2.4 * scale, 1.5 * scale
    box(slide, x, y, w, h, BLUE, shape=MSO_SHAPE.RECTANGLE)
    ov = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x + 0.12 * scale), Inches(y + 0.36 * scale),
                                Inches(w - 0.24 * scale), Inches(h - 0.72 * scale))
    ov.fill.solid()
    ov.fill.fore_color.rgb = YEL
    ov.line.fill.background()
    text(slide, x, y + 0.38 * scale, w, h - 0.76 * scale, "IKEA", size=int(30 * scale), color=BLUE,
         bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def header(slide, title, n):
    box(slide, 0, 0, 13.333, 0.12, BLUE, shape=MSO_SHAPE.RECTANGLE)
    text(slide, 0.6, 0.45, 11.8, 0.9, title, size=30, color=BLUE, bold=True)
    box(slide, 0.65, 1.35, 1.1, 0.08, YEL, shape=MSO_SHAPE.RECTANGLE)
    text(slide, 12.0, 6.95, 1.0, 0.35, f"{n} / 5", size=10, color=GREY, align=PP_ALIGN.RIGHT)


# ---------- 1. Cover (0:00 - 0:15) ----------
s = prs.slides.add_slide(BLANK)
box(s, 0, 0, 13.333, 7.5, BLUE, shape=MSO_SHAPE.RECTANGLE)
box(s, 0, 0, 0.18, 7.5, YEL, shape=MSO_SHAPE.RECTANGLE)
box(s, 0.9, 0.8, 2.9, 2.0, WHITE, radius=0.1)
logo(s, 1.15, 1.05, scale=1.0)
text(s, 0.9, 3.4, 11.5, 1.6, "Why would we invest in IKEA?", size=54, color=YEL, bold=True)
text(s, 0.9, 5.0, 11.5, 0.6, "An ESG reading of Ingka Group and IKEA France", size=22, color=WHITE)
text(s, 0.9, 6.1, 11.5, 0.8,
     ["MSc CFM · SKEMA · Sustainable Finance",
      "Calvin Minang · Jonathan Bouaffon · Liza Amouyal"], size=14, color=YEL)
notes(s, "[0:00 - 0:15] Cover.\n"
         "Script: \"Hello, we are... Our question: why would anyone invest in IKEA?\"\n\n"
         "Key point: Ingka Group is not listed. An investor would be exposed through debt or a private route, "
         "so the question is about risk, not equity returns.\n"
         "Source: Ingka ESG Profile (cover and group description).")

# ---------- 2. Answer (0:15 - 0:45) ----------
s = prs.slides.add_slide(BLANK)
header(s, "Our answer: a conditional yes", 2)
box(s, 0.65, 1.75, 5.1, 4.9, YEL, radius=0.08)
text(s, 0.95, 2.05, 4.6, 1.3, "Yes, under conditions.", size=36, color=BLUE, bold=True)
text(s, 0.95, 3.45, 4.6, 2.4,
     [("A risk-reduction case,", {"size": 22, "bold": True}),
      ("not an ESG premium.", {"size": 22, "bold": True}),
      ("We have no evidence that ESG lifts returns here.", {"size": 16})], color=INK)
kpis = [("−39%", "operational emissions in France\nsince 2016"),
        ("184%", "of IKEA France's electricity needs\ncovered by wind and solar output"),
        ("−30%", "group footprint, all scopes, since 2016\n(target: −50% by 2030)")]
for i, (num, lbl) in enumerate(kpis):
    y = 1.75 + i * 1.7
    box(s, 6.2, y, 6.5, 1.5, LIGHT, radius=0.1)
    box(s, 6.2, y, 0.12, 1.5, BLUE, shape=MSO_SHAPE.RECTANGLE)
    text(s, 6.6, y + 0.2, 2.6, 1.1, num, size=40, color=BLUE, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 9.2, y + 0.2, 3.4, 1.1, lbl, size=15, color=INK, anchor=MSO_ANCHOR.MIDDLE)
notes(s, "[0:15 - 0:45] Answer first.\n"
         "Script: \"Our answer is a conditional yes. It is a risk-reduction case, not an ESG premium.\"\n\n"
         "Figures (Ingka ESG Profile and IKEA one-pager):\n"
         "- Operational emissions in France down 39% since 2016.\n"
         "- Wind and solar output covers 184% of IKEA France's electricity needs.\n"
         "- Group footprint down about 30% since 2016 across scopes 1 to 3, while the business grew.\n"
         "- Target: minus 50% by 2030 (SBTi-aligned, replaces Climate Positive 2030); net zero by 2050.\n"
         "Caution: the France figures and the group figures are different scopes, and all data is company-reported "
         "and not tested by us.")

# ---------- 3. Environment, social, governance (0:45 - 1:35) ----------
s = prs.slides.add_slide(BLANK)
header(s, "Environment, social, governance: what holds and what is missing", 3)
text(s, 0.65, 1.7, 5.6, 0.5, "Where is the group's footprint?", size=16, color=BLUE, bold=True)
bars = [("Raw materials", 52, BLUE), ("Product use at home", 17, BLUE),
        ("Other items (residual)", 31, RGBColor(0xB8, 0xC4, 0xD6))]
for i, (lbl, val, col) in enumerate(bars):
    y = 2.35 + i * 0.85
    text(s, 0.65, y, 4.6, 0.35, lbl, size=13, color=INK)
    box(s, 0.65, y + 0.36, 4.3 * val / 52, 0.36, col, radius=0.06)
    text(s, 0.65 + 4.3 * val / 52 + 0.1, y + 0.33, 1.2, 0.42, f"{val}%", size=14, color=INK, bold=True)
text(s, 0.65, 5.0, 5.6, 1.2,
     "Raw materials and product use weigh more than operations: the supply chain matters most.",
     size=14, color=INK)
cols = [("What works", GREEN, ["Operations in France: −39% since 2016",
                              "Wind and solar: 184% of IKEA France's electricity needs",
                              "Fossil-free heating and 100% waste sorting by 2030",
                              "IWAY supplier code and supplier audits",
                              "200–400 local jobs per store",
                              "Gender equality index: 100/100 (4th year)"]),
        ("What is missing", RED, ["EU Taxonomy alignment not yet disclosed",
                                  "First TNFD results due in 2026",
                                  "SBTi targets may be questioned",
                                  "Supply chain outside France to verify",
                                  "Group not listed: ownership to confirm"])]
for i, (ttl, col, items) in enumerate(cols):
    x = 6.7 + i * 3.2
    box(s, x, 1.7, 3.0, 5.0, LIGHT, radius=0.08)
    box(s, x, 1.7, 3.0, 0.14, col, shape=MSO_SHAPE.RECTANGLE)
    text(s, x + 0.15, 1.95, 2.7, 0.5, ttl, size=17, color=col, bold=True)
    text(s, x + 0.15, 2.5, 2.75, 4.0, [(f"•  {it}", {"space": 10}) for it in items], size=13, color=INK)
notes(s, "[0:45 - 1:35] Environment, social, governance.\n"
         "Script: \"On environment, operations are falling, but most of the footprint sits in raw materials (52%) and "
         "product use (17%). On social, affordability and the IWAY code reduce risk. On governance, the duty of "
         "vigilance, CSRD and public reporting help. What is missing: the EU Taxonomy alignment, the first TNFD results "
         "due in 2026, and SBTi targets that may be questioned.\"\n\n"
         "Details to keep (Ingka ESG Profile):\n"
         "- 200–400 local jobs per store.\n"
         "- About EUR 200 million invested to cut prices on about 2,000 products.\n"
         "- 7% of employees with disabilities (legal requirement: 6%).\n"
         "- About 250 more refugees to be brought into work within 3 years.\n"
         "- IKEA Foundation: over EUR 2 billion funded for housing since 2009.\n"
         "- EUR 1.2 billion invested in France over 2023-26.\n"
         "- Fossil-free heating and 100% waste sorting by 2030; 10 urban micro-forests by 2030.\n"
         "- SFDR classifies funds, not companies, so the link to IKEA is indirect.")

# ---------- 4. Transmission to value (1:35 - 2:15) ----------
s = prs.slides.add_slide(BLANK)
header(s, "From ESG to value: three channels, one main effect", 4)
cards = [("1", "Cash flows", "Revenue and margins",
          ["Affordability widens the customer base", "Second-life and buy-back add margin",
           "Renewable energy hedges part of energy cost"], BLUE, WHITE),
         ("2", "Risk", "Discount rate (our main channel)",
          ["IWAY, audits and reporting", "Less regulatory and reputational risk",
           "Works through the rate, not revenue"], YEL, INK),
         ("3", "Investment", "Future resilience",
          ["Heat pumps, geothermal, renewables", "Spending today, protection tomorrow",
           "Hard to quantify without a published taxonomy"], BLUE, WHITE)]
for i, (num, ttl, sub, items, col, tcol) in enumerate(cards):
    x = 0.65 + i * 4.1
    box(s, x, 1.75, 3.85, 3.9, LIGHT, radius=0.08)
    box(s, x, 1.75, 3.85, 0.85, col, radius=0.08)
    text(s, x + 0.2, 1.85, 3.5, 0.65, f"{num}  {ttl}", size=20, color=tcol, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x + 0.2, 2.8, 3.5, 0.5, sub, size=14, color=BLUE, bold=True)
    text(s, x + 0.2, 3.4, 3.5, 2.2, [(f"•  {it}", {"space": 10}) for it in items], size=15, color=INK)
box(s, 0.65, 5.95, 12.0, 0.85, YEL, radius=0.12)
text(s, 0.9, 6.0, 11.5, 0.75,
     "Materiality: raw materials 52% and product use 17% of the footprint. The supply chain matters more than the 39% cut in France.",
     size=16, color=INK, anchor=MSO_ANCHOR.MIDDLE)
notes(s, "[1:35 - 2:15] Transmission channels.\n"
         "Script: \"ESG works through three channels: cash flows, risk and investment. The main one is risk. "
         "IWAY, audits and reporting reduce regulatory and reputational risk. That shows up in the discount rate, "
         "not in revenue.\"\n\n"
         "Details to keep:\n"
         "- Cash flows: affordability widens the customer base; second-life and buy-back add margin on existing products; "
         "wind and solar output covers part of the energy cost.\n"
         "- Investment: heat pumps, geothermal and renewables are spending today for resilience later; the effect is hard "
         "to quantify until the EU Taxonomy is published.\n"
         "- Our analysis, not company data: the channel logic. We have not valued anything.")

# ---------- 5. Decision rule and limits (2:15 - 2:50) ----------
s = prs.slides.add_slide(BLANK)
header(s, "Decision rule: yes while four conditions hold", 5)
conds = ["Green claims remain verifiable",
         "EU Taxonomy alignment is published in the next report",
         "First TNFD results support the nature roadmap",
         "The group stays on track for −50% by 2030 (scopes 1 to 3)"]
for i, txt in enumerate(conds):
    y = 1.75 + i * 0.95
    circ = box(s, 0.7, y, 0.7, 0.7, BLUE, shape=MSO_SHAPE.OVAL)
    text(s, 0.7, y, 0.7, 0.7, "abcd"[i], size=18, color=YEL, bold=True, align=PP_ALIGN.CENTER,
         anchor=MSO_ANCHOR.MIDDLE, shape=circ)
    text(s, 1.6, y + 0.05, 5.8, 0.65, txt, size=16, color=INK, anchor=MSO_ANCHOR.MIDDLE)
box(s, 7.7, 1.75, 5.0, 3.7, LIGHT, radius=0.08)
text(s, 7.95, 1.9, 4.6, 0.5, "Limits to keep in mind", size=17, color=BLUE, bold=True)
text(s, 7.95, 2.5, 4.6, 3.0,
     [(f"•  {it}", {"space": 9}) for it in [
         "No valuation, spread or return analysis",
         "One year of reporting; data is self-reported",
         "France figures are not the group scope",
         "Investment route (debt or private) to confirm",
         "Ingka ownership to verify (Stichting INGKA Foundation)"]], size=14, color=INK)
box(s, 0.65, 5.9, 12.0, 0.9, BLUE, radius=0.12)
text(s, 0.9, 5.95, 11.5, 0.8,
     [("Verdict: conditional yes, a risk-reduction case. We revise it if any condition fails.",
       {"color": WHITE, "size": 18, "bold": True})], anchor=MSO_ANCHOR.MIDDLE)
notes(s, "[2:15 - 2:50] Decision rule and limits.\n"
         "Script: \"Our decision rule: yes, while four conditions hold. We would revise if one fails. "
         "Our limits: no valuation or return analysis, one year of reporting, and self-reported data.\"\n\n"
         "Details to keep:\n"
         "- (a) Green claims are verifiable.\n"
         "- (b) EU Taxonomy alignment is published in the next report.\n"
         "- (c) First TNFD results support the nature roadmap.\n"
         "- (d) The group stays on the path to minus 50% by 2030 (scopes 1 to 3).\n"
         "- Ingka Group is not listed; its ownership (Stichting INGKA Foundation) must be verified.\n"
         "Closing line: \"Thank you. We are ready for your questions.\"\n"
         "Total: about 2 min 50 s. Rehearse once with a timer.")

prs.core_properties.title = "Why would we invest in IKEA? - group presentation (3 min)"
prs.core_properties.author = "Calvin Minang, Jonathan Bouaffon, Liza Amouyal"
prs.save(OUT)
print("written:", OUT)
