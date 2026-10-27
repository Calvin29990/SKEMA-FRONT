"""Individual one-pager (A4, single side) - English version.

Top half: reasoning map (question, emissions chart, schematic map of France,
three arguments, thesis). Bottom half: summary.

NOTE: the question and thesis are a DRAFT. The course requires the opinion to be the student's own.
The map is SCHEMATIC: no verified regional data is shown.

Usage: python3 build_one_pager.py   (needs the Highcharts GeoJSON, see MAP_GEOJSON)
"""
import json
import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "One-page-Calvin-Minang.pdf")
MAP_GEOJSON = os.environ.get(
    "MAP_GEOJSON", "/tmp/mapdl/package/countries/fr/fr-all.geo.json")  # @highcharts/map-collection (npm)
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DV", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DVB", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))

W, H = A4
BLUE = HexColor("#0058A3")
YEL = HexColor("#FFDA1A")
INK = HexColor("#1A1A1A")
GREY = HexColor("#5F6368")
LIGHT = HexColor("#F3F5F8")
MAPGREY = HexColor("#D9E2EF")
M = 44
CW = W - 2 * M
OVERSEAS = {"La Réunion", "Mayotte", "Guyane française", "Martinique", "Guadeloupe"}


def st(name, size, leading=None, font="DV", color=INK, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size,
                          leading=leading or size * 1.3, textColor=color, **kw)


def para(c, text, s, x, y_top, w):
    text = text.replace(" %", "&nbsp;%")
    p = Paragraph(text, s)
    _, h = p.wrap(w, 1000)
    p.drawOn(c, x, y_top - h)
    return h


def rect(c, x, y, w, h, fill, radius=0):
    c.setFillColor(fill)
    if radius:
        c.roundRect(x, y, w, h, radius, stroke=0, fill=1)
    else:
        c.rect(x, y, w, h, stroke=0, fill=1)


def draw_graph(c, x, y_top, w, h):
    """Bars: emissions reduction vs 2016 (figures from the Ingka ESG Profile)."""
    rect(c, x, y_top - h, w, h, LIGHT, radius=6)
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(x + 10, y_top - 16, "Emissions reduction vs 2016")
    rows = [
        ("IKEA France, operations", 39, BLUE),
        ("Group, scopes 1 to 3", 30, BLUE),
        ("Group 2030 target", 50, HexColor("#9DB9DC")),
    ]
    label_w = 96
    bar_x = x + 10 + label_w
    bar_max = w - label_w - 66
    y = y_top - 42
    for lbl, val, col in rows:
        para(c, lbl, st("gl", 7.6, 9.4), x + 10, y + 3, label_w - 6)
        rect(c, bar_x, y - 4, bar_max * val / 50, 13, col, radius=3)
        c.setFillColor(INK)
        c.setFont("DVB", 9)
        c.drawString(bar_x + bar_max * val / 50 + 5, y - 1, f"−{val} %")
        y -= 30
    para(c, "Source: Ingka ESG Profile. Different scopes; the 2030 target has not been reached yet.",
         st("gn", 6.8, 8.6, color=GREY), x + 10, y_top - h + 26, w - 20)


def draw_map(c, x, y_top, w, h):
    """Schematic map of mainland France regions; Île-de-France highlighted.
    The Highcharts GeoJSON uses planar coordinates, so they are scaled directly."""
    rect(c, x, y_top - h, w, h, LIGHT, radius=6)
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(x + 10, y_top - 16, "Schematic map of France")
    with open(MAP_GEOJSON, encoding="utf-8") as f:
        data = json.load(f)
    feats = [ft for ft in data["features"]
             if ft["properties"].get("name") and ft["properties"]["name"] not in OVERSEAS]

    def pts_of(geom):
        out = []

        def walk(a):
            if isinstance(a[0], (int, float)):
                out.append(a)
            else:
                for b in a:
                    walk(b)
        walk(geom["coordinates"])
        return out

    allp = [q for ft in feats for q in pts_of(ft["geometry"])]
    xmin, xmax = min(q[0] for q in allp), max(q[0] for q in allp)
    ymin, ymax = min(q[1] for q in allp), max(q[1] for q in allp)
    area_w, area_h = 183, h - 40
    sc = min(area_w / (xmax - xmin), area_h / (ymax - ymin))
    ox = x + 6
    oy = y_top - h + 22

    def P(px, py):
        return ox + (px - xmin) * sc, oy + (py - ymin) * sc

    idf_pts = []
    for ft in feats:
        name = ft["properties"]["name"]
        is_idf = name == "Île-de-France"
        geom = ft["geometry"]
        polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
        if is_idf:
            c.setFillColor(YEL)
            c.setStrokeColor(BLUE)
            c.setLineWidth(0.9)
        else:
            c.setFillColor(MAPGREY)
            c.setStrokeColor(white)
            c.setLineWidth(0.5)
        for poly in polys:
            path = c.beginPath()
            for ring in poly:
                for i, (px0, py0) in enumerate(ring):
                    px, py = P(px0, py0)
                    (path.moveTo if i == 0 else path.lineTo)(px, py)
                    if is_idf:
                        idf_pts.append((px, py))
                path.close()
            c.drawPath(path, fill=1, stroke=1)
    # Île-de-France label in the right margin, linked by a line
    if idf_pts:
        cx = sum(p[0] for p in idf_pts) / len(idf_pts)
        cy = sum(p[1] for p in idf_pts) / len(idf_pts)
        lx, lw, lh = x + 194, w - 200, 44
        ly = cy - lh / 2
        c.setStrokeColor(BLUE)
        c.setLineWidth(0.7)
        c.line(cx + 3, cy, lx, cy)
        rect(c, lx, ly, lw, lh, BLUE, radius=4)
        c.setFillColor(white)
        c.setFont("DVB", 7.4)
        c.drawString(lx + 5, ly + lh - 12, "Île-de-France")
        para(c, "where allocation decisions sit", st("ml", 6.6, 8, color=white), lx + 5, ly + lh - 16, lw - 8)
    para(c, "Schematic only: no verified regional data. Idea: allocation decisions are taken at the centre; "
            "their effects play out in the regions.",
         st("mn", 6.6, 8.4, color=GREY), x + 10, y_top - h + 26, w - 20)


def build():
    c = canvas.Canvas(OUT, pagesize=A4)
    c.setTitle("One-page - Calvin Minang - E focus finance (draft)")
    c.setAuthor("Calvin Minang")

    rect(c, 0, H - 8, W, 8, BLUE)
    c.setFillColor(GREY)
    c.setFont("DV", 7.5)
    c.drawString(M, H - 24, "CFM · Sustainable Finance · Individual one-pager · Calvin Minang")
    c.drawRightString(W - M, H - 24, "Single side")

    # ---------- TOP HALF ----------
    y = H - 40
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(M, y - 8, "REASONING MAP")
    y -= 18

    q = ("<b>Question.</b> Do Article 8 and Article 9 funds (SFDR) actually reduce emissions in the real economy, "
         "or do they only shift the problem?")
    hq = para(c, q, st("q", 10, 13.5), M + 10, y - 7, CW - 20)
    rect(c, M, y - hq - 14, CW, hq + 14, YEL, radius=6)
    para(c, q, st("q2", 10, 13.5), M + 10, y - 7, CW - 20)
    y = y - hq - 14 - 8

    row_h = 182
    gw = 232
    draw_graph(c, M, y, gw, row_h)
    draw_map(c, M + gw + 10, y, CW - gw - 10, row_h)
    y = y - row_h - 8

    branches = [
        ("1 · Transparency ≠ impact",
         "SFDR requires a declared strategy and PAI indicators. Article 8 'promotes' environmental or social "
         "characteristics; Article 9 targets a 'sustainable investment objective'. Neither sets a measured emissions cut.",
         "Course, Module 2 (SFDR, PAI, DNSH)"),
        ("2 · Cost of capital",
         "Excluding or down-weighting an issuer raises its cost of capital. The real effect runs through primary "
         "flows: a secondary-market purchase finances no project.",
         "Course, Modules 1 and 3 (exclusion, additionality)"),
        ("3 · Greenwashing risk",
         "The EU taxonomy measures eligibility, not an emissions cut. The same label can cover very different effects.",
         "Course, Module 2 (taxonomy, greenwashing)"),
    ]
    gap = 8
    bw = (CW - 2 * gap) / 3
    bh = 112
    for i, (ttl, body, src) in enumerate(branches):
        x = M + i * (bw + gap)
        rect(c, x, y - bh, bw, bh, LIGHT, radius=6)
        rect(c, x, y - 4, bw, 4, BLUE, radius=2)
        para(c, ttl, st("bt", 8.8, 11, font="DVB", color=BLUE), x + 8, y - 13, bw - 16)
        hb = para(c, body, st("bb", 7.6, 10), x + 8, y - 28, bw - 16)
        para(c, src, st("bs", 6.6, 8, color=GREY), x + 8, y - 30 - hb, bw - 16)
    y = y - bh - 6

    thesis = ("<b>My thesis.</b> No, not automatically. SFDR improves transparency, not impact. "
              "The environmental effect depends on shareholder engagement and on the additionality of the financing.")
    ht = para(c, thesis, st("th", 8.9, 12.2, color=white), M + 12, y - 7, CW - 24)
    rect(c, M, y - ht - 14, CW, ht + 14, BLUE, radius=6)
    para(c, thesis, st("th2", 8.9, 12.2, color=white), M + 12, y - 7, CW - 24)
    y_half = y - ht - 14

    c.setStrokeColor(GREY)
    c.setDash(3, 3)
    c.setLineWidth(0.6)
    sep_y = y_half - 12
    c.line(M, sep_y, W - M, sep_y)
    c.setDash()

    # ---------- BOTTOM HALF ----------
    y = sep_y - 14
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(M, y - 8, "SUMMARY")
    y -= 18

    summary = [
        "A fund classified as Article 8 or 9 does not, on its own, prove that it reduces real-economy emissions. "
        "SFDR is first and foremost a transparency obligation: a declared strategy, principal adverse impact (PAI) "
        "indicators and the 'do no significant harm' (DNSH) principle. This transparency has real value because it "
        "lets savers compare funds. But it describes what a fund says it does, not what its capital actually achieves.",

        "My view is therefore nuanced. The environmental lever works less through the label than through two "
        "mechanisms. The first is engagement: voting at shareholder meetings, dialogue, and escalation up to divestment. "
        "The second is additionality: financing projects that would not have been financed without this capital. "
        "A well-rated portfolio can hold listed shares whose price changes hands without any change in real capital. "
        "In that case the fund gains reputation without cutting emissions.",

        "I conclude that SFDR is a necessary but insufficient tool. To deliver on its promise, PAI indicators would need "
        "to be linked to measured trajectories, verifiable data would need to be published, and primary financing would "
        "need to be distinguished from secondary trading. My position could be challenged on one point: if Article 8/9 "
        "funds end up excluding the largest emitters, pressure on their cost of capital could be enough to change their "
        "behaviour even without active engagement. That is the test I would run on the data.",

        "<b>What would change my mind:</b> if published PAI data show, over several years, that Article 8/9 portfolios "
        "cut emissions faster than conventional funds, verifiable from public sources.",
    ]
    s_body = st("sb", 9.4, 13.0)
    for txt in summary:
        hp = para(c, txt, s_body, M, y, CW)
        y -= hp + 6

    foot = ("Sources: course by Sabrine Aouida, Modules 1 to 3; Ingka ESG Profile (IKEA figures). "
            "Check regulations against official texts: SFDR (EU) 2019/2088; EU Taxonomy (EU) 2020/852.")
    para(c, foot, st("ft", 6.8, 8.6, color=GREY), M, 40, CW)

    c.save()
    print("written:", OUT, "| end of summary y =", round(y, 1), "| separator y =", round(sep_y, 1))


if __name__ == "__main__":
    build()
