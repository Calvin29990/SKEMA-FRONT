"""Individual one-pager (A4, single side), course format.
Top half = reasoning map: question, map of Brazil (IKEA-linked states), timeline, three arguments, thesis.
Bottom half = summary. Numbered sources in the footer.

NOTE: question and thesis are a DRAFT. The course requires the opinion to be the student's own.
All dated facts were checked against the sources listed in the footer (checked 27 Oct 2026).

Usage: python3 build_one_pager.py   (needs the Highcharts Brazil GeoJSON, see MAP_GEOJSON)
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
    "MAP_GEOJSON", "/tmp/mapdl/br-all.geo.json")  # @highcharts/map-collection, countries/br/br-all.geo.json
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
RED = HexColor("#B3261E")
M = 44
CW = W - 2 * M

# Brazilian states with an IKEA-linked fact (map keys from the Highcharts file)
HIGHLIGHT = {"br-rs": 1, "br-pa": 2, "br-es": 2, "br-pr": 3, "br-sc": 3}


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


def badge(c, x, y, n):
    c.setFillColor(BLUE)
    c.circle(x, y, 6.5, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("DVB", 7.5)
    c.drawCentredString(x, y - 2.6, str(n))


def draw_map_card(c, x, y_top, w, h):
    """Map of Brazil (states) with IKEA-linked states highlighted and numbered; callouts on the right."""
    rect(c, x, y_top - h, w, h, LIGHT, radius=6)
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(x + 10, y_top - 16, "IKEA's Brazilian footprint: supplier and forest projects")

    with open(MAP_GEOJSON, encoding="utf-8") as f:
        data = json.load(f)
    feats = data["features"]

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
    map_w, map_h = 296, h - 46
    sc = min(map_w / (xmax - xmin), map_h / (ymax - ymin))
    ox = x + 6
    oy = y_top - h + 24

    def P(px, py):
        return ox + (px - xmin) * sc, oy + (py - ymin) * sc

    centroids = {}
    for ft in feats:
        key = ft["properties"].get("hc-key")
        geom = ft["geometry"]
        polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
        hl = key in HIGHLIGHT
        if hl:
            c.setFillColor(YEL)
            c.setStrokeColor(BLUE)
            c.setLineWidth(0.9)
        else:
            c.setFillColor(MAPGREY)
            c.setStrokeColor(white)
            c.setLineWidth(0.4)
        cx_pts = []
        for poly in polys:
            path = c.beginPath()
            for ring in poly:
                for i, (px0, py0) in enumerate(ring):
                    px, py = P(px0, py0)
                    (path.moveTo if i == 0 else path.lineTo)(px, py)
                    cx_pts.append((px, py))
                path.close()
            c.drawPath(path, fill=1, stroke=1)
        if cx_pts:
            centroids[key] = (sum(p[0] for p in cx_pts) / len(cx_pts), sum(p[1] for p in cx_pts) / len(cx_pts))

    # numbered markers at the centroid of each highlighted state
    for key, n in HIGHLIGHT.items():
        if key in centroids:
            mx, my = centroids[key]
            badge(c, mx, my, n)
    c.setFillColor(GREY)
    c.setFont("DV", 6.2)
    c.drawString(x + 10, y_top - h + 12,
                 "Schematic, state-level positions only (not exact sites). Basemap: Highcharts map collection.")

    # callouts (right)
    rx = x + 314
    rw = w - 314 - 8
    items = [
        (1, "Nova Prata (RS): supplier Artemobili",
         "Fined in 2018 and 2022 for environmental offences. IKEA = 66% of the supplier's Brazilian orders in 2023 [1]"),
        (2, "Tapajós basin (PA) and Atlantic Forest hub (ES)",
         "WWF projects with IKEA; partnership renewed to 2030 [3]"),
        (3, "Paraná and Santa Catarina",
         "BTG Pactual project: about 4,000 ha, announced 6 Nov 2025 [4]"),
    ]
    ty = y_top - 26
    for n, head, body in items:
        rect(c, rx, ty - 52, rw, 52, white, radius=5)
        badge(c, rx + 11, ty - 12, n)
        hh = para(c, f"<b>{head}</b>", st("ch", 7.3, 9), rx + 22, ty - 5, rw - 28)
        para(c, body, st("cb", 6.8, 8.4), rx + 22, ty - 5 - hh - 3, rw - 28)
        ty -= 56


def draw_timeline(c, x, y_top, w, h):
    """Timeline of IKEA-linked events and the EU rules that apply to them."""
    rect(c, x, y_top - h, w, h, LIGHT, radius=6)
    events = [
        ("2018", "Supplier fined", 0),
        ("2022", "Second fine", 1),
        ("27 Feb 2024", "Disclose / ARTE investigation [1]", 0),
        ("12 Mar 2024", "IKEA: supplier not supplying now [2]", 1),
        ("24 Sep 2025", "WWF partnership renewed to 2030 [3]", 0),
        ("6 Nov 2025", "BTG Pactual, 4,000 ha [4]", 1),
        ("1 May 2026", "EU–Mercosur interim deal applied [6]", 0),
        ("30 Dec 2026", "EUDR applies to wood furniture (large firms) [5]", 1),
    ]
    line_y = y_top - 40
    x0, x1 = x + 24, x + w - 24
    c.setStrokeColor(BLUE)
    c.setLineWidth(1.2)
    c.line(x0, line_y, x1, line_y)
    step = (x1 - x0) / (len(events) - 1)
    for i, (date, label, pos) in enumerate(events):
        px = x0 + i * step
        c.setFillColor(YEL if i >= 6 else BLUE)
        c.circle(px, line_y, 3.2, stroke=0, fill=1)
        lw = 92
        lx = min(max(px - lw / 2, x + 4), x + w - lw - 4)
        if pos == 0:
            ly_top = line_y + 16
        else:
            ly_top = line_y - 8
        c.setFillColor(BLUE)
        c.setFont("DVB", 6.6)
        if pos == 0:
            c.drawCentredString(px, ly_top + 4, date)
            para(c, label, st("tl", 5.9, 6.9, color=INK), lx, ly_top, lw)
        else:
            c.drawCentredString(px, ly_top - 14, date)
            para(c, label, st("tl2", 5.9, 6.9, color=INK), lx, ly_top - 18, lw)


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

    q = ("<b>Question.</b> Should an ESG investor count IKEA's forest projects in Brazil as risk reduction, "
         "when its main Brazilian supplier has been fined for environmental offences?")
    hq = Paragraph(q, st("q", 9.6, 12.8)).wrap(CW - 20, 1000)[1]
    rect(c, M, y - hq - 12, CW, hq + 12, YEL, radius=6)
    para(c, q, st("q2", 9.6, 12.8), M + 10, y - 6, CW - 20)
    y = y - hq - 12 - 7

    map_h = 196
    draw_map_card(c, M, y, CW, map_h)
    y = y - map_h - 6

    tl_h = 84
    draw_timeline(c, M, y, CW, tl_h)
    y = y - tl_h - 6

    branches = [
        ("1 · Projects are elsewhere",
         "The forest projects sit in the Tapajós basin and the Atlantic Forest. The supplier sits in Rio Grande do Sul. "
         "No public source links the two.",
         "[1][3][4]; my inference on the link"),
        ("2 · Risk sits at the supplier",
         "IKEA says the supplier breached its code and no longer supplies it [2]. The EUDR tests supplier-level "
         "traceability for wood furniture from 30 Dec 2026 [5].",
         "[2][5]"),
        ("3 · What to price",
         "Supplier-level traceability and deforestation PAI data, not project headlines. Under SFDR, a project "
         "claim alone does not show lower risk.",
         "PAI and controversy framework of the course (my reading)"),
    ]
    gap = 7
    bw = (CW - 2 * gap) / 3
    bh = 96
    for i, (ttl, body, src) in enumerate(branches):
        x = M + i * (bw + gap)
        rect(c, x, y - bh, bw, bh, LIGHT, radius=6)
        rect(c, x, y - 4, bw, 4, BLUE, radius=2)
        ht_ = para(c, ttl, st("bt", 8.4, 10.6, font="DVB", color=BLUE), x + 8, y - 12, bw - 16)
        hb = para(c, body, st("bb", 7.3, 9.4), x + 8, y - 12 - ht_ - 4, bw - 16)
        para(c, src, st("bs", 6.2, 7.6, color=GREY), x + 8, y - 12 - ht_ - 4 - hb - 4, bw - 16)
    y = y - bh - 6

    thesis = ("<b>My thesis (draft).</b> No, not on current evidence. Forest projects elsewhere do not offset supplier risk. "
              "The risk must be priced where the wood is harvested and processed.")
    ht = Paragraph(thesis, st("th", 8.4, 11.4, color=white)).wrap(CW - 24, 1000)[1]
    rect(c, M, y - ht - 12, CW, ht + 12, BLUE, radius=6)
    para(c, thesis, st("th2", 8.4, 11.4, color=white), M + 12, y - 6, CW - 24)
    y_half = y - ht - 12

    c.setStrokeColor(GREY)
    c.setDash(3, 3)
    c.setLineWidth(0.6)
    sep_y = y_half - 8
    c.line(M, sep_y, W - M, sep_y)
    c.setDash()

    # ---------- BOTTOM HALF ----------
    y = sep_y - 11
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(M, y - 8, "SUMMARY")
    y -= 16

    summary = [
        "IKEA funds forest work in Brazil: WWF projects in the Tapajós basin and the Atlantic Forest [3], and a "
        "4,000-hectare project with BTG Pactual in Paraná and Santa Catarina [4]. Its main Brazilian supplier, Artemobili, "
        "in Nova Prata (Rio Grande do Sul), was fined in 2018 and 2022, and IKEA accounted for 66% of that supplier's orders in Brazil in 2023 [1]. "
        "IKEA told the NGO that the incidents breached its supplier code and that the supplier was not supplying it as of "
        "March 2024 [2].",

        "My view: the projects are a reputational buffer, not risk reduction. They sit in other places and do not change "
        "how the supplier's wood is audited. Supplier risk is what the EUDR will test for wood furniture from 30 December "
        "2026 [5], and this is where an investor should look. The EU–Mercosur interim deal, applied since 1 May 2026 [6], "
        "adds a second concern: more trade in commodities can move deforestation to other places, which is my inference, "
        "not a tested result.",

        "<b>What would change my mind:</b> independent evidence that IKEA's Brazilian wood is traced to the plot, and that "
        "its forest projects measurably reduce deforestation linked to its own supply.",
    ]
    s_body = st("sb", 8.3, 10.9)
    for txt in summary:
        hp = para(c, txt, s_body, M, y, CW)
        y -= hp + 4

    # ---------- SOURCES ----------
    src_lines = [
        "[1] Disclose, 'Au Brésil, le principal fournisseur d'Ikea accusé d'atteintes à l'environnement' (26 Feb 2024): disclose.ngo/fr/article/au-bresil-le-principal-fournisseur-dikea-accuse-datteintes-a-lenvironnement (fines 2018 and 2022; IKEA = 66% of supplier's orders; USD 34.4 m in 2023, customs data).",
        "[2] Business & Human Rights Resource Centre, 'IKEA's response on allegations of main manufacturer' (12 Mar 2024): business-humanrights.org/en/latest-news/ikeas-response-on-allegations-of-main-manufacturer-being-responsible-for-environmental-crimes/",
        "[3] IKEA Global: WWF projects in Colombia and Brazil (7 Dec 2023): ikea.com/global/en/newsroom/sustainability/wwf-ikea-forest-degradation-colombia-brazil-231207/ ; WWF–IKEA renewal to 2030 (24 Sep 2025): ikea.com/global/en/newsroom/sustainability/wwf-and-ikea-announce-the-next-phase-of-their-year-long-partnership-250924/",
        "[4] IKEA Global, forest investment in Brazil with BTG Pactual (6 Nov 2025): ikea.com/global/en/newsroom/corporate/inter-ikea-group-announces-forest-investment-in-brazil-251106/",
        "[5] European Commission, EUDR application dates (30 Dec 2026, large and medium operators): environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en ; wood furniture HS 9403 in Annex I (secondary source, check the Annex): saral.ro/en/blog/eudr-timber-furniture-deadline-2026/",
        "[6] Intereconomics, 'From Signature to Standstill' (21 Oct 2026): intereconomics.eu/contents/year/2026/number/3/article/from-signature-to-standstill-the-future-of-the-eu-mercosur-agreement.html",
        "Map basemap: Highcharts map collection 2.3.3 (npm, @highcharts/map-collection).",
    ]
    fy = y - 4
    c.setFillColor(BLUE)
    c.setFont("DVB", 6.8)
    c.drawString(M, fy - 6, "SOURCES")
    fy -= 11
    for ln in src_lines:
        fy -= para(c, ln, st("src", 5.4, 6.6, color=GREY), M, fy, CW) + 0.6

    c.save()
    print("written:", OUT, "| summary end y =", round(y, 1), "| sources end y =", round(fy, 1))


if __name__ == "__main__":
    build()
