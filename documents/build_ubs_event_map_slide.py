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

BG = "F7F7F3"
NAVY = "18232B"
MUTED = "737B80"
RED = "C82036"
TEAL = "00A985"
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
                pixels[x, y] = (r, g, b, int(a * (248 - whiteness) / 20))
    logo.save(UBS_LOGO)


def build_pptx():
    prepare_logo()
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W)
    prs.slide_height = Inches(SLIDE_H)
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = rgb(BG)

    # Brand header follows the approved UBS / SKEMA slide style.
    slide.shapes.add_picture(str(UBS_LOGO), Inches(0.40), Inches(0.18),
                             width=Inches(1.53), height=Inches(0.54))
    add_text(slide, "MAJOR EUROPEAN TRADING LOSS EVENTS", 2.18, 0.18,
             8.9, 0.31, 17.5, NAVY, True)
    add_text(slide, "SELECTED BENCHMARKS RELEVANT TO UBS 2011",
             2.18, 0.49, 8.9, 0.22, 10.5, RED, True)
    add_text(slide, "Treasury Committee  /  incident overview",
             2.18, 0.75, 8.9, 0.18, 8.3, MUTED)
    slide.shapes.add_picture(str(SKEMA_LOGO), Inches(12.22), Inches(0.16),
                             width=Inches(0.59), height=Inches(0.59))
    rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                  Inches(0.40), Inches(0.99),
                                  Inches(12.53), Inches(0.012))
    rule.fill.solid()
    rule.fill.fore_color.rgb = rgb("C9CDCA")
    rule.line.fill.background()

    # Only the validated map: its Barings, Kerviel and Adoboli benchmarks stay intact.
    map_h = 5.72
    map_w = map_h * MAP_ASPECT
    slide.shapes.add_picture(str(MAP), Inches((SLIDE_W-map_w)/2), Inches(1.08),
                             width=Inches(map_w), height=Inches(map_h))

    # One concise executive-summary line at the bottom, as requested.
    rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                  Inches(0.42), Inches(6.91),
                                  Inches(12.51), Inches(0.012))
    rule.fill.solid()
    rule.fill.fore_color.rgb = rgb("C9CDCA")
    rule.line.fill.background()
    add_text(slide, "EXECUTIVE SUMMARY", 0.44, 6.99, 1.58, 0.18,
             7.6, RED, True)
    add_text(slide,
             "The UBS case shows how control failures can escalate into material losses and liquidity pressure.",
             2.02, 6.97, 10.75, 0.23, 10.3, NAVY, True)
    add_text(slide, "UBS  ×  SKEMA", 11.92, 7.27, 0.95, 0.12,
             6.4, MUTED, True, align=PP_ALIGN.RIGHT)

    prs.core_properties.title = "Major European Trading Loss Events"
    prs.core_properties.subject = "Approved event map with executive-summary line"
    prs.core_properties.author = "SKEMA"
    prs.save(PPTX_OUT)


def build_preview():
    prepare_logo()
    scale = 120
    canvas = Image.new("RGB", (int(SLIDE_W*scale), int(SLIDE_H*scale)), f"#{BG}")
    draw = ImageDraw.Draw(canvas)
    regular_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

    def font(size, bold=False):
        return ImageFont.truetype(bold_path if bold else regular_path,
                                  int(size*scale/72))

    def px(value):
        return int(value*scale)

    def text(value, x, y, size, color, bold=False, anchor=None):
        draw.text((px(x), px(y)), value, font=font(size, bold),
                  fill=f"#{color}", anchor=anchor)

    ubs = Image.open(UBS_LOGO).convert("RGBA")
    ubs = ubs.resize((px(1.53), px(0.54)), Image.Resampling.LANCZOS)
    canvas.paste(ubs, (px(0.40), px(0.18)), ubs)
    text("MAJOR EUROPEAN TRADING LOSS EVENTS", 2.18, 0.22,
         17.5, NAVY, True)
    text("SELECTED BENCHMARKS RELEVANT TO UBS 2011", 2.18, 0.52,
         10.5, RED, True)
    text("Treasury Committee  /  incident overview", 2.18, 0.77,
         8.3, MUTED)
    skema = Image.open(SKEMA_LOGO).convert("RGBA")
    skema = skema.resize((px(0.59), px(0.59)), Image.Resampling.LANCZOS)
    canvas.paste(skema, (px(12.22), px(0.16)), skema)
    draw.rectangle((px(0.40), px(0.99), px(12.93), px(1.002)), fill="#C9CDCA")

    map_h = 5.72
    map_w = map_h * MAP_ASPECT
    event_map = Image.open(MAP).convert("RGB")
    event_map = event_map.resize((px(map_w), px(map_h)), Image.Resampling.LANCZOS)
    canvas.paste(event_map, (px((SLIDE_W-map_w)/2), px(1.08)))

    draw.rectangle((px(0.42), px(6.91), px(12.93), px(6.922)), fill="#C9CDCA")
    text("EXECUTIVE SUMMARY", 0.44, 7.02, 7.6, RED, True)
    text("The UBS case shows how control failures can escalate into material losses and liquidity pressure.",
         2.02, 7.00, 10.3, NAVY, True)
    text("UBS  ×  SKEMA", 12.87, 7.29, 6.4, MUTED, True, anchor="ra")
    canvas.save(PNG_OUT, optimize=True)


if __name__ == "__main__":
    build_pptx()
    build_preview()
    print(PPTX_OUT)
    print(PNG_OUT)
