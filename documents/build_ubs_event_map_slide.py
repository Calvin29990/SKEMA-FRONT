from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
MAP = ASSETS / "ubs-event-map-approved.png"
UBS_LOGO_SOURCE = ASSETS / "ubs-logo.png"
UBS_LOGO = ASSETS / "ubs-logo-slide.png"
SKEMA_LOGO = ASSETS / "skema-logo.png"
PPTX_OUT = ROOT / "ubs-event-map-slide.pptx"
PNG_OUT = ROOT / "ubs-event-map-slide-preview.png"

# Palette sampled to echo the user's approved UBS / SKEMA risk-slide style.
BG = "F7F7F3"
NAVY = "18232B"
MUTED = "737B80"
TEAL = "00A985"
RED = "C82036"
GOLD = "D6A600"
PANEL = "101315"
PANEL_LINE = "30373B"
WHITE = "F7F8F6"
SOFT = "A9B0B2"

SLIDE_W, SLIDE_H = 13.333333, 7.5
MAP_ASPECT = 867 / 651


def rgb(value):
    return RGBColor.from_string(value)


def add_text(slide, text, x, y, w, h, size, color, bold=False,
             font="Arial", align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.MIDDLE,
             margin=0):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.margin_left = tf.margin_right = Inches(margin)
    tf.margin_top = tf.margin_bottom = Inches(margin)
    tf.vertical_anchor = valign
    p = tf.paragraphs[0]
    p.alignment = align
    p.space_before = Pt(0)
    p.space_after = Pt(0)
    run = p.add_run()
    run.text = text
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = rgb(color)
    return box


def rect(slide, x, y, w, h, fill, line=None, line_width=0.8):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                   Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb(fill)
    if line:
        shape.line.color.rgb = rgb(line)
        shape.line.width = Pt(line_width)
    else:
        shape.line.fill.background()
    return shape


def add_benchmark(slide, x, y, w, label, year, amount, color, institution=""):
    add_text(slide, label, x, y, 2.72, 0.23, 10, WHITE, True)
    add_text(slide, year, x + w - 0.62, y, 0.55, 0.23, 9, color, True,
             align=PP_ALIGN.RIGHT)
    add_text(slide, amount, x, y + 0.28, 2.58, 0.38, 18, color, True)
    if institution:
        add_text(slide, institution, x + 2.62, y + 0.34,
                 w - 2.62, 0.24, 8.5, SOFT, False, align=PP_ALIGN.RIGHT)


def prepare_logo():
    """Remove the source logo's white matte so it sits cleanly on the ivory header."""
    logo = Image.open(UBS_LOGO_SOURCE).convert("RGBA")
    pixels = logo.load()
    for y in range(logo.height):
        for x in range(logo.width):
            r, g, b, a = pixels[x, y]
            whiteness = min(r, g, b)
            if whiteness >= 248:
                pixels[x, y] = (r, g, b, 0)
            elif whiteness > 228 and max(r, g, b) - min(r, g, b) < 16:
                alpha = int(a * (248 - whiteness) / 20)
                pixels[x, y] = (r, g, b, alpha)
    logo.save(UBS_LOGO)


def build_pptx():
    prepare_logo()
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W)
    prs.slide_height = Inches(SLIDE_H)
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = rgb(BG)

    # Brand header mirrors the approved slide while keeping the event map central.
    slide.shapes.add_picture(str(UBS_LOGO), Inches(0.40), Inches(0.18),
                             width=Inches(1.53), height=Inches(0.54))
    add_text(slide, "UBS INVESTMENT BANK  |  2011", 2.18, 0.18,
             8.9, 0.31, 17.5, NAVY, True)
    add_text(slide, "EUROPEAN TRADING-LOSS BENCHMARKS", 2.18, 0.49,
             8.9, 0.22, 10.5, RED, True)
    add_text(slide, "Treasury Committee  /  incident overview",
             2.18, 0.75, 8.9, 0.18, 8.3, MUTED)
    slide.shapes.add_picture(str(SKEMA_LOGO), Inches(12.22), Inches(0.16),
                             width=Inches(0.59), height=Inches(0.59))
    rect(slide, 0.40, 0.99, 12.53, 0.012, "C9CDCA")

    add_text(slide, "EUROPEAN LOSS EVENTS  /  MAP & BENCHMARKS",
             0.43, 1.05, 6.1, 0.20, 7.7, MUTED, True)
    add_text(slide, "HISTORICAL CASES  ·  LOSS FIGURES AS LABELLED",
             7.60, 1.05, 5.25, 0.20, 7.7, MUTED, True,
             align=PP_ALIGN.RIGHT)

    # Two dark editorial panels echo the approved three-panel risk overview.
    panel_y, panel_h = 1.31, 5.43
    rect(slide, 0.42, panel_y, 7.20, panel_h, PANEL, PANEL_LINE, 0.8)
    rect(slide, 0.42, panel_y, 7.20, 0.045, TEAL)
    # Preserve the approved map's native 4:3-ish aspect ratio without cropping.
    map_h = 5.25
    map_w = map_h * MAP_ASPECT
    slide.shapes.add_picture(str(MAP), Inches(0.49), Inches(1.39),
                             width=Inches(map_w), height=Inches(map_h))

    panel_x, panel_w = 7.78, 5.15
    rect(slide, panel_x, panel_y, panel_w, panel_h, PANEL, PANEL_LINE, 0.8)
    rect(slide, panel_x, panel_y, panel_w, 0.045, RED)
    add_text(slide, "BENCHMARK LOSS EVENTS", 7.99, 1.56,
             4.75, 0.25, 11, WHITE, True)
    add_text(slide, "Selected European trading-loss cases",
             7.99, 1.86, 4.75, 0.20, 8.2, SOFT)
    rect(slide, 7.99, 2.15, 4.73, 0.008, PANEL_LINE)

    add_benchmark(slide, 8.01, 2.36, 4.68, "BARINGS", "1995",
                  "USD -1.4bn", GOLD)
    rect(slide, 7.99, 3.18, 4.73, 0.008, PANEL_LINE)
    add_benchmark(slide, 8.01, 3.38, 4.68, "KERVIEL", "2008",
                  "EUR -4.9bn", RED, "Société Générale")
    rect(slide, 7.99, 4.20, 4.73, 0.008, PANEL_LINE)
    add_benchmark(slide, 8.01, 4.40, 4.68, "ADOBOLI", "2011",
                  "USD -2.3bn", RED, "UBS")
    rect(slide, 7.99, 5.22, 4.73, 0.008, PANEL_LINE)

    add_text(slide, "LOCATION NOTE", 8.01, 5.43, 4.65, 0.20,
             8.2, GOLD, True)
    add_text(slide, "Adoboli's trading desk: London",
             8.01, 5.70, 4.65, 0.24, 10, WHITE, True)
    add_text(slide, "UBS Group headquarters: Zurich",
             8.01, 5.99, 4.65, 0.23, 9, SOFT)

    # A single bottom-line sentence, in the executive-summary position of the reference.
    rect(slide, 0.42, 6.88, 12.51, 0.012, "C9CDCA")
    add_text(slide, "EXECUTIVE SUMMARY", 0.44, 6.97, 1.58, 0.18,
             7.6, RED, True)
    add_text(slide,
             "The UBS case shows how control failures can escalate into material losses and liquidity pressure.",
             2.02, 6.95, 10.75, 0.23, 10.3, NAVY, True)
    add_text(slide, "UBS  ×  SKEMA", 11.92, 7.26, 0.95, 0.12,
             6.4, MUTED, True, align=PP_ALIGN.RIGHT)

    prs.core_properties.title = "UBS Investment Bank | European Trading-Loss Benchmarks"
    prs.core_properties.subject = "Approved European trading-loss map with benchmark cases"
    prs.core_properties.author = "SKEMA"
    prs.save(PPTX_OUT)


def build_preview():
    prepare_logo()
    scale = 120
    canvas = Image.new("RGB", (int(SLIDE_W * scale), int(SLIDE_H * scale)), f"#{BG}")
    draw = ImageDraw.Draw(canvas)
    regular_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

    def font(size, bold=False):
        return ImageFont.truetype(bold_path if bold else regular_path,
                                  int(size * scale / 72))

    def px(v):
        return int(v * scale)

    def text(s, x, y, size, color, bold=False, anchor=None):
        draw.text((px(x), px(y)), s, font=font(size, bold),
                  fill=f"#{color}", anchor=anchor)

    def rectangle(x, y, w, h, fill, outline=None, width=1):
        box = (px(x), px(y), px(x+w), px(y+h))
        draw.rectangle(box, fill=f"#{fill}",
                       outline=f"#{outline}" if outline else None, width=width)

    # Header logos and title.
    ubs = Image.open(UBS_LOGO).convert("RGBA")
    ubs = ubs.resize((px(1.53), px(0.54)), Image.Resampling.LANCZOS)
    canvas.paste(ubs, (px(0.40), px(0.18)), ubs)
    text("UBS INVESTMENT BANK  |  2011", 2.18, 0.22, 17.5, NAVY, True)
    text("EUROPEAN TRADING-LOSS BENCHMARKS", 2.18, 0.52, 10.5, RED, True)
    text("Treasury Committee  /  incident overview", 2.18, 0.77, 8.3, MUTED)
    skema = Image.open(SKEMA_LOGO).convert("RGBA")
    skema = skema.resize((px(0.59), px(0.59)), Image.Resampling.LANCZOS)
    canvas.paste(skema, (px(12.22), px(0.16)), skema)
    rectangle(0.40, 0.99, 12.53, 0.012, "C9CDCA")
    text("EUROPEAN LOSS EVENTS  /  MAP & BENCHMARKS", 0.43, 1.08,
         7.7, MUTED, True)
    text("HISTORICAL CASES  ·  LOSS FIGURES AS LABELLED", 12.85, 1.08,
         7.7, MUTED, True, anchor="ra")

    panel_y, panel_h = 1.31, 5.43
    rectangle(0.42, panel_y, 7.20, panel_h, PANEL, PANEL_LINE, 2)
    rectangle(0.42, panel_y, 7.20, 0.045, TEAL)
    map_h = 5.25
    map_w = map_h * MAP_ASPECT
    event_map = Image.open(MAP).convert("RGB")
    event_map = event_map.resize((px(map_w), px(map_h)), Image.Resampling.LANCZOS)
    canvas.paste(event_map, (px(0.49), px(1.39)))

    panel_x, panel_w = 7.78, 5.15
    rectangle(panel_x, panel_y, panel_w, panel_h, PANEL, PANEL_LINE, 2)
    rectangle(panel_x, panel_y, panel_w, 0.045, RED)
    text("BENCHMARK LOSS EVENTS", 7.99, 1.60, 11, WHITE, True)
    text("Selected European trading-loss cases", 7.99, 1.89, 8.2, SOFT)
    rectangle(7.99, 2.15, 4.73, 0.008, PANEL_LINE)

    cases = [
        (2.36, "BARINGS", "1995", "USD -1.4bn", GOLD, ""),
        (3.38, "KERVIEL", "2008", "EUR -4.9bn", RED, "Société Générale"),
        (4.40, "ADOBOLI", "2011", "USD -2.3bn", RED, "UBS"),
    ]
    for y, label, year, amount, color, org in cases:
        text(label, 8.01, y+0.03, 10, WHITE, True)
        text(year, 12.69, y+0.03, 9, color, True, anchor="ra")
        text(amount, 8.01, y+0.34, 18, color, True)
        if org:
            text(org, 10.62, y+0.40, 8.5, SOFT)
    for y in (3.18, 4.20, 5.22):
        rectangle(7.99, y, 4.73, 0.008, PANEL_LINE)

    text("LOCATION NOTE", 8.01, 5.47, 8.2, GOLD, True)
    text("Adoboli's trading desk: London", 8.01, 5.73, 10, WHITE, True)
    text("UBS Group headquarters: Zurich", 8.01, 6.02, 9, SOFT)

    rectangle(0.42, 6.88, 12.51, 0.012, "C9CDCA")
    text("EXECUTIVE SUMMARY", 0.44, 7.00, 7.6, RED, True)
    text("The UBS case shows how control failures can escalate into material losses and liquidity pressure.",
         2.02, 6.98, 10.3, NAVY, True)
    text("UBS  ×  SKEMA", 12.87, 7.28, 6.4, MUTED, True, anchor="ra")
    canvas.save(PNG_OUT, optimize=True)


if __name__ == "__main__":
    build_pptx()
    build_preview()
    print(PPTX_OUT)
    print(PNG_OUT)
