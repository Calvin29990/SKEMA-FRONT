from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt
from PIL import Image

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUT = ROOT / "ubs-treasury-risk-presentation-10-slides.pptx"

MAP_SLIDE = ASSETS / "approved-map-slide.png"
THREE_PANEL_SLIDE = ASSETS / "approved-three-panel-slide.png"
DALTONS = ASSETS / "daltons-illustration.png"
UBS_LOGO = ASSETS / "ubs-logo-slide.png"
SKEMA_LOGO = ASSETS / "skema-logo.png"

SW, SH = 13.333333, 7.5
BG = "F7F7F3"
PANEL = "101315"
PANEL_2 = "191E21"
NAVY = "18232B"
WHITE = "F7F8F6"
MUTED = "737B80"
SOFT = "A9B0B2"
RED = "C82036"
TEAL = "00A985"
GOLD = "D6A600"
BLUE = "2E91C1"
GREEN = "42A878"
BORDER = "CFD3D0"


def C(hex_color):
    return RGBColor.from_string(hex_color)


def rect(slide, x, y, w, h, fill, line=None, width=0.8, shape=MSO_SHAPE.RECTANGLE):
    sh = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.fill.solid()
    sh.fill.fore_color.rgb = C(fill)
    if line:
        sh.line.color.rgb = C(line)
        sh.line.width = Pt(width)
    else:
        sh.line.fill.background()
    return sh


def line(slide, x1, y1, x2, y2, color=BORDER, width=1.0):
    sh = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                                    Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    sh.line.color.rgb = C(color)
    sh.line.width = Pt(width)
    return sh


def txt(slide, value, x, y, w, h, size=12, color=NAVY, bold=False,
        align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.MIDDLE, margin=0.02,
        font="Arial"):
    sh = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = sh.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(margin)
    tf.margin_top = tf.margin_bottom = Inches(margin)
    tf.vertical_anchor = valign
    p = tf.paragraphs[0]
    p.alignment = align
    p.space_before = Pt(0)
    p.space_after = Pt(0)
    r = p.add_run()
    r.text = value
    r.font.name = font
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = C(color)
    return sh


def add_img_fit(slide, path, x, y, w, h):
    """Place an image fully inside a box without cropping or distorting it."""
    with Image.open(path) as im:
        iw, ih = im.size
    aspect = iw / ih
    box_aspect = w / h
    if aspect > box_aspect:
        dw, dh = w, w / aspect
        dx, dy = x, y + (h - dh) / 2
    else:
        dh, dw = h, h * aspect
        dx, dy = x + (w - dw) / 2, y
    return slide.shapes.add_picture(str(path), Inches(dx), Inches(dy),
                                    width=Inches(dw), height=Inches(dh))


def add_header(slide, title, kicker, page, section):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = C(BG)
    slide.shapes.add_picture(str(UBS_LOGO), Inches(0.42), Inches(0.13),
                             width=Inches(1.38), height=Inches(0.49))
    txt(slide, title, 2.02, 0.15, 9.65, 0.31, 17, NAVY, True)
    txt(slide, kicker, 2.02, 0.47, 9.65, 0.20, 9.3, RED, True)
    txt(slide, section, 2.02, 0.71, 9.65, 0.16, 7.4, MUTED)
    slide.shapes.add_picture(str(SKEMA_LOGO), Inches(12.35), Inches(0.12),
                             width=Inches(0.52), height=Inches(0.55))
    rect(slide, 0.42, 0.97, 12.48, 0.012, BORDER)
    rect(slide, 0.42, 7.17, 12.48, 0.010, BORDER)
    txt(slide, f"UBS  ×  SKEMA   /   {page:02d}", 11.40, 7.22, 1.45, 0.12,
        6.4, MUTED, True, align=PP_ALIGN.RIGHT)


def panel_title(slide, x, y, w, title, accent=TEAL, sub=None):
    rect(slide, x, y, w, 0.055, accent)
    txt(slide, title, x + 0.18, y + 0.13, w - 0.36, 0.26, 11, WHITE, True)
    if sub:
        txt(slide, sub, x + 0.18, y + 0.43, w - 0.36, 0.20, 8, SOFT)


def add_fitted_user_slide(prs, image_path):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = C(BG)
    add_img_fit(slide, image_path, 0, 0, SW, SH)
    return slide


def make_deck():
    prs = Presentation()
    prs.slide_width = Inches(SW)
    prs.slide_height = Inches(SH)
    blank = prs.slide_layouts[6]

    # 1 — Cover + compact introduction
    s = prs.slides.add_slide(blank)
    add_header(s, "UBS 2011 ROGUE TRADING SCANDAL",
               "FROM OPERATIONAL FAILURE TO TREASURY DECISIONS",
               1, "CORPORATE TREASURY MANAGEMENT  ·  14 SEP–14 DEC 2011")
    txt(s, "CENTRAL QUESTION", 0.60, 1.30, 5.95, 0.24, 9, TEAL, True)
    rect(s, 0.58, 1.62, 5.98, 1.23, PANEL, PANEL)
    txt(s, "How should Treasury protect due payments after concealed trading losses are discovered?",
        0.82, 1.82, 5.50, 0.78, 16, WHITE, True)
    # User-requested humorous Dalton illustration replaces the trader portrait.
    rect(s, 6.88, 1.30, 5.98, 3.36, "FFFFFF", BORDER, 0.8)
    add_img_fit(s, DALTONS, 6.98, 1.40, 5.78, 3.05)
    txt(s, "ILLUSTRATIVE CARTOON", 10.14, 4.42, 2.48, 0.17,
        7, MUTED, True, align=PP_ALIGN.RIGHT)
    # Three-month horizon
    txt(s, "DECISION WINDOW", 0.62, 3.08, 2.2, 0.20, 8.5, MUTED, True)
    line(s, 0.78, 3.64, 5.94, 3.64, TEAL, 3)
    for x, date, label in [(0.85, "14 SEP", "Discovery"), (5.85, "14 DEC", "Treasury horizon")]:
        rect(s, x - 0.08, 3.55, 0.18, 0.18, TEAL, shape=MSO_SHAPE.OVAL)
        txt(s, date, x - 0.35, 3.82, 1.12, 0.22, 9, NAVY, True)
        txt(s, label, x - 0.35, 4.06, 1.72, 0.22, 8, MUTED)
    # Method: short and legible
    txt(s, "EVIDENCE RULE", 0.62, 4.66, 2.1, 0.20, 8.5, MUTED, True)
    evidence = [
        (0.60, 1.66, "PUBLISHED", "Incident facts", RED),
        (2.58, 1.66, "DERIVED", "Accounting bridge", TEAL),
        (4.56, 1.99, "ASSUMED", "Cash scenarios", GOLD),
    ]
    for x, w, title, sub, accent in evidence:
        rect(s, x, 4.95, w, 0.73, WHITE, BORDER)
        rect(s, x, 4.95, 0.055, 0.73, accent)
        txt(s, title, x + 0.16, 5.05, w - 0.23, 0.20, 8, NAVY, True)
        txt(s, sub, x + 0.16, 5.31, w - 0.23, 0.19, 7.2, MUTED)
    # Treasury decision sequence
    txt(s, "TREASURY RESPONSE", 6.97, 5.03, 5.66, 0.22, 8.5, MUTED, True)
    steps = [(7.04, "VERIFY", "Positions"), (8.92, "PROTECT", "Headroom"), (10.80, "STAGE", "Funding")]
    for idx, (x, title, sub) in enumerate(steps):
        rect(s, x, 5.38, 1.62, 0.85, PANEL, PANEL)
        rect(s, x, 5.38, 1.62, 0.045, [TEAL, GOLD, RED][idx])
        txt(s, title, x + 0.11, 5.55, 1.40, 0.22, 9, WHITE, True, align=PP_ALIGN.CENTER)
        txt(s, sub, x + 0.11, 5.85, 1.40, 0.20, 8, SOFT, align=PP_ALIGN.CENTER)
        if idx < 2:
            rect(s, x + 1.68, 5.70, 0.16, 0.16, [GOLD, RED][idx], shape=MSO_SHAPE.CHEVRON)
    txt(s, "Research lens: maturity-based liquidity headroom, not a corporate working-capital proxy.",
        0.62, 6.47, 11.85, 0.25, 9.2, NAVY, True)

    # 2 — Company, cash cycle and incident timeline
    s = prs.slides.add_slide(blank)
    add_header(s, "UBS CASH CYCLE MEETS HIDDEN TRADING RISK",
               "PART I  ·  COMPANY & INCIDENT", 2,
               "UBS INVESTMENT BANK  /  LONDON ETF DESK")
    txt(s, "A BANK MUST HAVE CASH IN THE RIGHT ENTITY, CURRENCY AND PLACE — WHEN DUE",
        0.58, 1.19, 12.1, 0.25, 9.3, MUTED, True)
    # Cash cycle as a row of simple boxes
    flow = [
        (0.62, "CUSTOMERS", "Deposits · fees"),
        (3.10, "UBS TREASURY", "Accessible liquidity"),
        (5.58, "MARKETS", "Futures · CCPs"),
        (8.06, "SETTLEMENT", "Cash · collateral"),
        (10.54, "PAYMENTS", "Withdrawals · debt"),
    ]
    for i, (x, top, bottom) in enumerate(flow):
        rect(s, x, 1.67, 2.16, 0.92, PANEL, PANEL)
        rect(s, x, 1.67, 2.16, 0.05, [TEAL, BLUE, GOLD, RED, TEAL][i])
        txt(s, top, x + 0.12, 1.87, 1.92, 0.20, 9.2, WHITE, True, align=PP_ALIGN.CENTER)
        txt(s, bottom, x + 0.12, 2.16, 1.92, 0.20, 8, SOFT, align=PP_ALIGN.CENTER)
        if i < len(flow) - 1:
            rect(s, x + 2.22, 2.03, 0.20, 0.16, TEAL, shape=MSO_SHAPE.CHEVRON)
    # Concealment mechanism
    txt(s, "CONCEALMENT MECHANISM", 0.60, 2.92, 3.1, 0.22, 8.7, RED, True)
    mechanism = [
        (0.62, "REAL POSITIONS", "Long / short index futures", BLUE),
        (4.65, "FALSE OFFSETS", "Fictitious internal entries", GOLD),
        (8.68, "RISK VIEW", "Exposure appeared covered", RED),
    ]
    for i, (x, title, body, color) in enumerate(mechanism):
        rect(s, x, 3.27, 3.35, 0.83, WHITE, BORDER)
        rect(s, x, 3.27, 0.06, 0.83, color)
        txt(s, title, x + 0.18, 3.40, 2.98, 0.20, 9.2, NAVY, True)
        txt(s, body, x + 0.18, 3.68, 2.98, 0.22, 8, MUTED)
        if i < 2:
            rect(s, x + 3.54, 3.59, 0.32, 0.18, color, shape=MSO_SHAPE.CHEVRON)
    # Timeline
    txt(s, "FOUR DATES THAT CHANGED THE TREASURY VIEW", 0.60, 4.42, 5.7, 0.22, 8.7, MUTED, True)
    timeline = [
        (0.66, "14 SEP", "Positions discovered", RED),
        (3.78, "15 SEP", "Initial estimate ~USD 2.0bn", GOLD),
        (6.90, "18 SEP", "Risk described as covered", BLUE),
        (10.02, "04 OCT", "Revised loss USD 2.3bn", RED),
    ]
    line(s, 0.94, 5.04, 11.98, 5.04, BORDER, 2)
    for x, date, text_, accent in timeline:
        rect(s, x, 4.94, 0.20, 0.20, accent, shape=MSO_SHAPE.OVAL)
        txt(s, date, x - 0.15, 5.24, 1.25, 0.22, 9, NAVY, True)
        txt(s, text_, x - 0.15, 5.52, 2.65, 0.42, 8, MUTED)
    txt(s, "Adoboli was a trader on UBS Investment Bank’s London ETF Desk. Sources: FINMA §§11–18; FSA §§23–25; UBS disclosures.",
        0.62, 6.38, 11.9, 0.27, 7.3, MUTED)

    # 3 — User-approved three-panel slide, embedded pixel-for-pixel.
    add_fitted_user_slide(prs, THREE_PANEL_SLIDE)

    # 4 — How trading exposures translate into cash
    s = prs.slides.add_slide(blank)
    add_header(s, "A TRADING LOSS IS NOT A DAY-ONE CASH REQUIREMENT",
               "PART II  ·  TRANSMISSION INTO CASH", 4,
               "SEPARATE PERMANENT LOSS FROM TIMING-DRIVEN LIQUIDITY")
    # Top process ribbon
    stages = [
        (0.62, "MARKET LOSS", "Realised / booked", RED),
        (3.78, "SETTLEMENT", "Cash due by value date", GOLD),
        (6.94, "COLLATERAL", "Call or return timing", BLUE),
        (10.10, "HEADROOM", "Cash available when due", TEAL),
    ]
    for i, (x, title, sub, accent) in enumerate(stages):
        rect(s, x, 1.55, 2.55, 1.10, PANEL, PANEL)
        rect(s, x, 1.55, 2.55, 0.05, accent)
        txt(s, title, x + 0.15, 1.80, 2.25, 0.23, 10, WHITE, True, align=PP_ALIGN.CENTER)
        txt(s, sub, x + 0.15, 2.16, 2.25, 0.20, 8, SOFT, align=PP_ALIGN.CENTER)
        if i < 3:
            rect(s, x + 2.65, 1.97, 0.33, 0.18, accent, shape=MSO_SHAPE.CHEVRON)
    # Three liquidity channels
    channels = [
        (0.62, RED, "PERMANENT", "Trading loss; remediation expense", "P&L / capital impact"),
        (4.66, BLUE, "TEMPORARY", "Settlement cash; recoverable collateral", "Timing / liquidity impact"),
        (8.70, GOLD, "CONTINGENT", "Withdrawals; tighter terms; rollover", "Stress-only until evidenced"),
    ]
    for x, accent, title, desc, note in channels:
        rect(s, x, 3.25, 3.75, 1.60, WHITE, BORDER)
        rect(s, x, 3.25, 3.75, 0.055, accent)
        txt(s, title, x + 0.18, 3.48, 3.35, 0.23, 10, accent, True)
        txt(s, desc, x + 0.18, 3.82, 3.35, 0.44, 10.2, NAVY, True)
        txt(s, note, x + 0.18, 4.39, 3.35, 0.20, 8, MUTED)
    # Formula + ongoing obligations
    rect(s, 0.62, 5.18, 12.0, 0.74, PANEL, PANEL)
    txt(s, "CASH FORECAST", 0.82, 5.38, 1.55, 0.22, 8.5, TEAL, True)
    txt(s, "Opening accessible cash  +  dated receipts  −  payments  +  confirmed funding",
        2.42, 5.34, 9.85, 0.28, 13, WHITE, True, align=PP_ALIGN.CENTER)
    txt(s, "OBLIGATIONS CONTINUE", 0.64, 6.19, 2.25, 0.20, 8.5, MUTED, True)
    for i, label in enumerate(["Settlements", "Withdrawals", "Debt maturities", "Payroll & suppliers"]):
        x = 2.72 + i * 2.48
        rect(s, x, 6.12, 2.20, 0.43, "E9ECE8", None)
        txt(s, label, x + 0.08, 6.21, 2.04, 0.19, 8.4, NAVY, True, align=PP_ALIGN.CENTER)
    txt(s, "Do not equate the published USD 2.3bn loss with same-day cash need. Potential channels are not asserted historical cash movements.",
        0.64, 6.71, 11.95, 0.20, 7.1, MUTED)

    # 5 — Quantitative model / cash bridge
    s = prs.slides.add_slide(blank)
    add_header(s, "CASH BRIDGE: BASE CASE HOLDS ABOVE THE BUFFER",
               "PART III  ·  QUANTITATIVE ANALYSIS", 5,
               "CLASSROOM MODEL OUTPUTS · USD MILLIONS · NOT HISTORICAL UBS CASH")
    txt(s, "LOW POINT BY SCENARIO", 0.68, 1.31, 4.2, 0.22, 9, MUTED, True)
    # Plot background
    chart_x, chart_y, chart_w, chart_h = 0.82, 1.72, 7.62, 4.46
    rect(s, chart_x, chart_y, chart_w, chart_h, WHITE, BORDER)
    # y-axis 500..1100
    y0, y1 = chart_y + chart_h - 0.65, chart_y + 0.45
    val_min, val_max = 500, 1100
    def cy(v): return y0 - (v - val_min) / (val_max - val_min) * (y0 - y1)
    for v in (500, 600, 700, 800, 900, 1000, 1100):
        yy = cy(v)
        line(s, chart_x + 0.64, yy, chart_x + chart_w - 0.24, yy,
             RED if v == 700 else "E3E7E3", 1.2 if v == 700 else 0.55)
        txt(s, str(v), chart_x + 0.08, yy - 0.09, 0.45, 0.18, 7.2,
            RED if v == 700 else MUTED, v == 700, align=PP_ALIGN.RIGHT)
    txt(s, "$700m BUFFER", chart_x + 5.90, cy(700) - 0.25, 1.25, 0.18, 7.2, RED, True,
        align=PP_ALIGN.RIGHT)
    # Three bars
    bars = [
        (2.14, 984, "NO INCIDENT", TEAL, "min"),
        (4.36, 765, "INCIDENT BASE", BLUE, "min"),
        (6.58, 549, "COMBINED STRESS", RED, "30 Nov"),
    ]
    for x, value, label, accent, when in bars:
        top = cy(value)
        rect(s, x, top, 1.12, y0 - top, accent)
        txt(s, f"${value}m", x - 0.13, top - 0.35, 1.40, 0.24, 11, accent, True,
            align=PP_ALIGN.CENTER)
        txt(s, label, x - 0.55, y0 + 0.11, 2.20, 0.20, 7.7, NAVY, True,
            align=PP_ALIGN.CENTER)
        txt(s, when, x - 0.22, y0 + 0.34, 1.60, 0.18, 7, MUTED,
            align=PP_ALIGN.CENTER)
    # Key model facts side panel
    rect(s, 8.78, 1.72, 4.10, 4.46, PANEL, PANEL)
    panel_title(s, 8.78, 1.72, 4.10, "MODEL ASSUMPTIONS", TEAL,
                "Replace with Treasury ledger and approved buffer")
    metrics = [("$1,000m", "assumed opening cash"), ("$700m", "assumed minimum buffer"),
               ("$765m", "incident-base minimum · $0 gap")]
    for i, (big, small) in enumerate(metrics):
        yy = 2.48 + i * 0.87
        txt(s, big, 9.00, yy, 1.55, 0.33, 17, [TEAL, GOLD, BLUE][i], True)
        txt(s, small, 10.62, yy + 0.04, 2.00, 0.24, 8.3, WHITE)
        if i < 2:
            line(s, 9.00, yy + 0.60, 12.62, yy + 0.60, "343B3E", 0.7)
    txt(s, "No incident low point: $984m.\nCombined stress: buffer breached on 30 Nov.",
        9.00, 5.17, 3.65, 0.62, 9.1, WHITE, True)
    txt(s, "Every cash input is a labelled classroom assumption. Public USD 2.3bn loss is not deducted again from opening cash.",
        0.72, 6.54, 12.0, 0.28, 7.5, MUTED)

    # 6 — Stress waterfall and funding timing
    s = prs.slides.add_slide(blank)
    add_header(s, "STRESS FIRST BREACH: 30 NOVEMBER · FUND BEFORE IT",
               "PART III  ·  STRESS & FUNDING TIMING", 6,
               "SENSITIVITY OUTPUTS ARE ASSUMPTION-DRIVEN")
    txt(s, "COMBINED STRESS SHOCKS", 0.62, 1.28, 4.2, 0.22, 9, MUTED, True)
    # Waterfall from incident-base November cash to 30 Nov stress cash.
    x0, y_top, base_y = 0.82, 1.92, 5.58
    vmin, vmax = 450, 950
    def wy(v): return base_y - (v-vmin)/(vmax-vmin)*(base_y-y_top)
    for v in (500, 600, 700, 800, 900):
        yy = wy(v)
        line(s, 0.98, yy, 8.58, yy, RED if v == 700 else "E3E7E3", 1.15 if v == 700 else 0.55)
        txt(s, str(v), 0.60, yy - 0.08, 0.30, 0.16, 7, RED if v == 700 else MUTED,
            v == 700, align=PP_ALIGN.RIGHT)
    txt(s, "$700m buffer", 7.12, wy(700)-0.23, 1.35, 0.18, 7.1, RED, True,
        align=PP_ALIGN.RIGHT)
    steps = [
        (1.15, 849, 849, "BASE", "$849m", TEAL),
        (2.55, 849, 799, "SETTLEMENT", "−$50m", GOLD),
        (3.95, 799, 699, "COLLATERAL", "−$100m", BLUE),
        (5.35, 699, 599, "WITHDRAWALS", "−$100m", RED),
        (6.75, 599, 549, "ROLLOVER", "−$50m", GOLD),
    ]
    for i, (x, before, after, label, amount, color) in enumerate(steps):
        top_v = max(before, after)
        bottom_v = min(before, after)
        rect(s, x, wy(top_v), 0.72, wy(bottom_v)-wy(top_v) if after != before else base_y-wy(before), color)
        if after == before:
            rect(s, x, wy(before), 0.72, base_y-wy(before), color)
        txt(s, amount, x - 0.18, wy(top_v)-0.28, 1.10, 0.19, 8.5, color, True,
            align=PP_ALIGN.CENTER)
        txt(s, label, x - 0.28, base_y + 0.15, 1.28, 0.33, 7.2, NAVY, True,
            align=PP_ALIGN.CENTER)
        if i < len(steps)-1:
            line(s, x+0.73, wy(after), steps[i+1][0], wy(after), MUTED, 0.8)
    # Result and T+2 timeline
    rect(s, 8.90, 1.53, 3.98, 2.28, PANEL, PANEL)
    panel_title(s, 8.90, 1.53, 3.98, "LIQUIDITY RESULT", RED)
    txt(s, "$549m", 9.14, 2.30, 1.65, 0.45, 22, RED, True)
    txt(s, "30 Nov · $151m below buffer", 10.73, 2.36, 1.95, 0.28, 8.5, WHITE, True)
    txt(s, "$524m at 14 Dec  ·  $176m peak funding need",
        9.14, 3.05, 3.48, 0.34, 9.3, WHITE, True)
    rect(s, 8.90, 4.02, 3.98, 2.16, WHITE, BORDER)
    txt(s, "ASSUMED T+2 FUNDING PLAN", 9.14, 4.24, 3.50, 0.22, 9.4, NAVY, True)
    line(s, 9.40, 5.10, 12.38, 5.10, TEAL, 2.4)
    for x, date, label in [(9.48, "25 NOV", "Trigger"), (10.84, "29 NOV", "Arrives"), (12.14, "30 NOV", "Breach")]:
        rect(s, x, 5.01, 0.18, 0.18, [GOLD, TEAL, RED][2 if label=="Breach" else 0 if label=="Trigger" else 1], shape=MSO_SHAPE.OVAL)
        txt(s, date, x - 0.34, 5.30, 0.90, 0.18, 7.7, NAVY, True, align=PP_ALIGN.CENTER)
        txt(s, label, x - 0.34, 5.56, 0.90, 0.18, 7.2, MUTED, align=PP_ALIGN.CENTER)
    txt(s, "Assumed $200m committed line; availability and T+2 timing must be verified. Stress inputs: settlement −50, collateral delay −100, withdrawals −100, non-renewal −50 (USDm).",
        0.64, 6.54, 12.0, 0.31, 7.3, MUTED)

    # 7 — User-approved map slide, pixel-for-pixel.
    add_fitted_user_slide(prs, MAP_SLIDE)

    # 8 — Risk assessment and 3x3 matrix
    s = prs.slides.add_slide(blank)
    add_header(s, "PRIORITISE RESIDUAL EXPOSURE AFTER CONTAINMENT",
               "PART IV  ·  RISK ASSESSMENT", 8,
               "ANALYST SCORES FOR THE 14 SEP–14 DEC HORIZON")
    txt(s, "LIKELIHOOD", 0.70, 1.33, 1.3, 0.20, 8, MUTED, True)
    # 3x3 matrix; vertical axis from unlikely to likely, horizontal impact low to high.
    mx, my, cell = 1.15, 1.83, 1.26
    fills = [["DCECE4", "F5EDC8", "F0D5D7"],
             ["E6EED5", "F0E2B2", "E8C6C8"],
             ["F1E8D0", "E8CFB3", "E2B7BB"]]
    for row in range(3):
        for col in range(3):
            rect(s, mx + col*cell, my + row*cell, cell-0.04, cell-0.04,
                 fills[row][col], WHITE, 1.1)
            txt(s, f"{(row+1)*(col+1)}", mx + col*cell + 0.06,
                my + row*cell + 0.04, 0.22, 0.18, 7, MUTED)
    for i, lab in enumerate(["UNLIKELY", "POSSIBLE", "LIKELY"]):
        txt(s, lab, 0.32, my + i*cell + 0.42, 0.76, 0.22, 7.2, NAVY, True,
            align=PP_ALIGN.RIGHT)
    for col, lab in enumerate(["LOW", "MED", "HIGH"]):
        txt(s, lab, mx + col*cell, my + 3*cell + 0.04, cell-0.04, 0.20,
            7.3, NAVY, True, align=PP_ALIGN.CENTER)
    txt(s, "IMPACT", mx + 0.72, my + 3*cell + 0.34, 2.15, 0.22, 8, MUTED, True,
        align=PP_ALIGN.CENTER)
    # Put top-priority markers in the medium/high cell; color-coded distinct dots.
    cx, cy = mx + 2*cell + 0.50, my + cell + 0.50
    for idx, (dx, dy, label, color) in enumerate([(-0.22, -0.16, "P1", RED), (0.18, -0.16, "P2", BLUE), (-0.02, 0.18, "P3", GOLD)]):
        rect(s, cx+dx-0.15, cy+dy-0.13, 0.30, 0.26, color, shape=MSO_SHAPE.OVAL)
        txt(s, label, cx+dx-0.14, cy+dy-0.08, 0.28, 0.16, 6.1, WHITE, True,
            align=PP_ALIGN.CENTER)
    # Priority list and score explanation
    rect(s, 5.45, 1.56, 7.42, 4.65, PANEL, PANEL)
    panel_title(s, 5.45, 1.56, 7.42, "TOP RESIDUAL RISKS", RED,
                "Likelihood × impact = score · proposed analyst ratings")
    risk_rows = [
        (2.42, "P1", "OPERATIONAL", "Unreconciled breaks may hide open positions", "2 × 3 = 6", RED),
        (3.26, "P2", "LIQUIDITY", "Settlement / collateral peak versus buffer", "2 × 3 = 6", BLUE),
        (4.10, "P3", "FUNDING", "Maturity inside horizon may not roll", "2 × 3 = 6", GOLD),
    ]
    for y, p, title, desc, score, accent in risk_rows:
        rect(s, 5.70, y, 0.55, 0.55, accent, shape=MSO_SHAPE.OVAL)
        txt(s, p, 5.70, y+0.11, 0.55, 0.22, 8.5, WHITE, True, align=PP_ALIGN.CENTER)
        txt(s, title, 6.43, y-0.01, 2.20, 0.22, 9, WHITE, True)
        txt(s, desc, 6.43, y+0.24, 4.50, 0.25, 8.1, SOFT)
        txt(s, score, 11.30, y+0.08, 1.26, 0.28, 10, accent, True, align=PP_ALIGN.RIGHT)
        if y < 4.1: line(s, 5.70, y+0.70, 12.60, y+0.70, "343B3E", 0.7)
    txt(s, "OTHER WATCHLIST", 5.72, 5.15, 1.60, 0.20, 7.6, TEAL, True)
    txt(s, "Market  ·  counterparty  ·  legal / regulatory  ·  reputational", 7.38, 5.14,
        5.10, 0.22, 8.2, WHITE)
    txt(s, "Scores are assumptions, not UBS / regulator ratings. Re-score after close-out; define impact using approved internal buffer.",
        0.60, 6.59, 12.0, 0.25, 7.2, MUTED)

    # 9 — CFO action plan
    s = prs.slides.add_slide(blank)
    add_header(s, "THREE CFO ACTIONS LINK CONTROL, CASH AND EXECUTION",
               "PART V  ·  CFO RECOMMENDATIONS", 9,
               "OWNERS · DEADLINES · BENEFITS · CONSTRAINTS · FALLBACKS")
    actions = [
        (0.62, TEAL, "01", "PROTECT LIQUIDITY", "GROUP TREASURER", "24h initial view · daily to 14 Dec",
         "13-week cash forecast; confirm accessible facilities before any modeled breach.",
         "Benefit: verified headroom", "Constraint: eligibility · lead time · cost"),
        (4.66, RED, "02", "CONTAIN EXPOSURE", "IB COO + MARKET RISK", "Immediate · daily until reconciled",
         "Independently reconcile positions and settle / collateral breaks; close exposure under control.",
         "Benefit: uncertainty reduced", "Fallback: conservative overlay"),
        (8.70, GOLD, "03", "REBUILD CONTROLS", "CRO + IB COO · IA VALIDATES", "Interim now · programme by 14 Dec",
         "Dual verification, exception escalation and ownership of trade breaks.",
         "Benefit: recurrence risk down", "Constraint: systems · staffing"),
    ]
    for x, accent, num, title, owner, deadline, action, benefit, constraint in actions:
        rect(s, x, 1.55, 3.75, 4.83, PANEL, PANEL)
        rect(s, x, 1.55, 3.75, 0.055, accent)
        rect(s, x+0.20, 1.82, 0.54, 0.54, accent, shape=MSO_SHAPE.OVAL)
        txt(s, num, x+0.20, 1.96, 0.54, 0.20, 10, WHITE, True, align=PP_ALIGN.CENTER)
        txt(s, title, x+0.20, 2.55, 3.35, 0.48, 12, WHITE, True)
        txt(s, owner, x+0.20, 3.18, 3.35, 0.20, 8, accent, True)
        txt(s, deadline, x+0.20, 3.46, 3.35, 0.36, 8.2, SOFT)
        # Vertical action mark / execution path
        line(s, x+0.27, 4.02, x+0.27, 5.30, accent, 2.2)
        rect(s, x+0.18, 4.05, 0.18, 0.18, accent, shape=MSO_SHAPE.OVAL)
        txt(s, action, x+0.52, 3.98, 2.98, 0.83, 9.2, WHITE, True, valign=MSO_ANCHOR.TOP)
        line(s, x+0.20, 5.00, x+3.54, 5.00, "343B3E", 0.7)
        txt(s, benefit, x+0.20, 5.16, 3.35, 0.26, 8.2, TEAL, True)
        txt(s, constraint, x+0.20, 5.55, 3.35, 0.44, 7.8, SOFT)
    txt(s, "FUNDING FALLBACK: separately verify availability, eligible collateral and arrival time; do not count an unconfirmed facility as cash.",
        0.64, 6.62, 12.0, 0.24, 7.5, NAVY, True)

    # 10 — Conclusion / Treasury decision
    s = prs.slides.add_slide(blank)
    add_header(s, "PROTECT PAYMENT CAPACITY — ACT ON VERIFIED EVIDENCE",
               "CONCLUSION  ·  THE TREASURY DECISION", 10,
               "A TIMING-LED LIQUIDITY PLAN, NOT A CLAIM ABOUT UBS’S ACTUAL CASH GAP")
    txt(s, "RECONCILE", 0.90, 1.55, 3.08, 0.30, 10, TEAL, True, align=PP_ALIGN.CENTER)
    txt(s, "FORECAST", 5.13, 1.55, 3.08, 0.30, 10, BLUE, True, align=PP_ALIGN.CENTER)
    txt(s, "STAGE FUNDING", 9.35, 1.55, 3.08, 0.30, 10, RED, True, align=PP_ALIGN.CENTER)
    decision_nodes = [
        (0.72, TEAL, "01", "Verify positions", "Independent trade and collateral reconciliation"),
        (4.93, BLUE, "02", "Map dated cash", "By entity · currency · value date · buffer"),
        (9.14, RED, "03", "Fund before breach", "Confirm source, conditions and T+2 arrival"),
    ]
    for x, accent, num, title, sub in decision_nodes:
        rect(s, x, 2.05, 3.44, 1.73, PANEL, PANEL)
        rect(s, x, 2.05, 3.44, 0.055, accent)
        rect(s, x+0.20, 2.34, 0.55, 0.55, accent, shape=MSO_SHAPE.OVAL)
        txt(s, num, x+0.20, 2.49, 0.55, 0.20, 10, WHITE, True, align=PP_ALIGN.CENTER)
        txt(s, title, x+0.88, 2.34, 2.32, 0.30, 11, WHITE, True)
        txt(s, sub, x+0.22, 3.05, 3.00, 0.46, 8.3, SOFT, align=PP_ALIGN.CENTER)
    for x in (4.30, 8.52):
        rect(s, x, 2.78, 0.34, 0.20, GOLD, shape=MSO_SHAPE.CHEVRON)
    # Single bottom-line answer
    rect(s, 0.72, 4.22, 11.90, 1.06, WHITE, BORDER)
    rect(s, 0.72, 4.22, 0.06, 1.06, RED)
    txt(s, "TREASURY DECISION", 0.98, 4.42, 1.80, 0.22, 8, RED, True)
    txt(s, "Preserve headroom and activate funding only when verified forecasts show a buffer breach before the funding source can arrive.",
        2.83, 4.36, 9.36, 0.54, 12, NAVY, True)
    # Monitor strip
    for i, (label, value, accent) in enumerate([
        ("HEADROOM", "Cash vs approved buffer", TEAL),
        ("OPEN ITEMS", "Unmatched trades / collateral", GOLD),
        ("FUNDING", "Confirmed source arrival", RED),
    ]):
        x = 0.72 + i*4.02
        rect(s, x, 5.72, 3.78, 0.72, PANEL, PANEL)
        rect(s, x, 5.72, 0.055, 0.72, accent)
        txt(s, label, x+0.17, 5.84, 3.42, 0.18, 8, accent, True)
        txt(s, value, x+0.17, 6.10, 3.42, 0.20, 8.2, WHITE)
    txt(s, "Public information confirms the loss and control failures, not UBS’s actual daily accessible cash or peak funding need. Load internal Treasury records before quantifying a real gap.",
        0.74, 6.65, 11.9, 0.28, 7.3, MUTED)

    prs.core_properties.title = "UBS 2011 Rogue Trading Scandal — Treasury Risk Briefing"
    prs.core_properties.subject = "Ten-slide visual briefing following the agreed plan"
    prs.core_properties.author = "Corporate Treasury Management Team"
    prs.save(OUT)
    return OUT


if __name__ == "__main__":
    print(make_deck())
