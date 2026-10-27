"""Individual one-pager (A4, single side), course format:
top half = reasoning map (question, large schematic map of France with key figures, three arguments, thesis);
bottom half = summary. Sources are numbered and listed in the footer.

NOTE: the question and thesis are a DRAFT. The course requires the opinion to be the student's own.
Figures are dated (as of 27 Oct 2026) and were checked against the sources listed in the footer.

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


def draw_map_card(c, x, y_top, w, h):
    """Large schematic map of mainland France (left) + three key figures and a spread mini-chart (right)."""
    rect(c, x, y_top - h, w, h, LIGHT, radius=6)
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(x + 10, y_top - 16, "France at a glance, as of 27 Oct 2026")

    # ---- map (left) ----
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
    map_w = 252
    map_h = h - 52
    sc = min(map_w / (xmax - xmin), map_h / (ymax - ymin))
    ox = x + 8
    oy = y_top - h + 26

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
            c.setLineWidth(1.0)
        else:
            c.setFillColor(MAPGREY)
            c.setStrokeColor(white)
            c.setLineWidth(0.6)
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
    if idf_pts:
        cx = sum(p[0] for p in idf_pts) / len(idf_pts)
        cy = sum(p[1] for p in idf_pts) / len(idf_pts)
        c.setFillColor(BLUE)
        c.circle(cx, cy, 2.2, stroke=0, fill=1)
        c.setFillColor(BLUE)
        c.setFont("DVB", 6.8)
        c.drawString(cx - 22, cy - 12, "Paris")
    para(c, "Schematic only. Île-de-France (yellow): where allocation decisions are taken; their effects play out in the regions.",
         st("mn", 6.4, 8.0, color=GREY), x + 10, y_top - h + 22, map_w)

    # ---- key figures (right) ----
    rx = x + 268
    rw = w - 268 - 10
    tiles = [
        ("Aa3 · outlook negative", "Moody's rating on France, affirmed 23 Oct 2026 [1]"),
        ("≈ 155 bp", "OAT–Bund 10-year spread on 26 Oct 2026 [2]"),
        ("1 May 2026", "EU–Mercosur interim trade deal applied provisionally [3]"),
    ]
    ty = y_top - 28
    for big, small in tiles:
        rect(c, rx, ty - 46, rw, 46, white, radius=5)
        rect(c, rx, ty - 46, 4, 46, BLUE)
        c.setFillColor(BLUE)
        c.setFont("DVB", 11.5)
        c.drawString(rx + 11, ty - 19, big)
        para(c, small, st("tl", 7.0, 8.8), rx + 11, ty - 25, rw - 18)
        ty -= 52

    # mini chart: OAT–Bund spread history (sources [2])
    c.setFillColor(BLUE)
    c.setFont("DVB", 7.6)
    c.drawString(rx, ty - 8, "OAT–Bund 10-year spread (bp) [2]")
    bars = [("Mid-Sep", 96), ("22 Oct", 175), ("26 Oct", 156)]
    by = ty - 20
    bmax = rw - 82
    for lbl, val in bars:
        c.setFillColor(GREY)
        c.setFont("DV", 6.8)
        c.drawString(rx, by + 1, lbl)
        rect(c, rx + 48, by, bmax * val / 180, 9, BLUE if lbl != "22 Oct" else YEL, radius=2)
        c.setFillColor(INK)
        c.setFont("DVB", 6.8)
        c.drawString(rx + 48 + bmax * val / 180 + 4, by + 1, f"{val}")
        by -= 13


def build():
    c = canvas.Canvas(OUT, pagesize=A4)
    c.setTitle("One-page - Calvin Minang - E focus finance (draft)")
    c.setAuthor("Calvin Minang")

    rect(c, 0, H - 8, W, 8, BLUE)
    c.setFillColor(GREY)
    c.setFont("DV", 7.5)
    c.drawString(M, H - 24, "CFM · Sustainable Finance · Individual one-pager · Calvin Minang")
    c.drawRightString(W - M, H - 24, "Single side")

    # ---------- TOP HALF: reasoning map ----------
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

    map_h = 236
    draw_map_card(c, M, y, CW, map_h)
    y = y - map_h - 8

    branches = [
        ("1 · Transparency ≠ impact",
         "SFDR sets disclosure rules, not emissions targets. Article 8 'promotes' environmental or social "
         "characteristics; Article 9 targets a 'sustainable investment objective'.",
         "Course, Module 2 (SFDR, PAI, DNSH)"),
        ("2 · Cost of capital",
         "French sovereign risk moved from about 96 bp to about 175 bp in five weeks [2]. Prices react fast, "
         "but only additional capital changes real projects.",
         "[2]; course, Module 3 (additionality)"),
        ("3 · Displacement",
         "EU–Mercosur has applied provisionally since 1 May 2026; France voted against in the Council [3]. "
         "Emissions may move abroad: my inference, not yet tested.",
         "[3] (inference is mine)"),
    ]
    gap = 8
    bw = (CW - 2 * gap) / 3
    bh = 100
    for i, (ttl, body, src) in enumerate(branches):
        x = M + i * (bw + gap)
        rect(c, x, y - bh, bw, bh, LIGHT, radius=6)
        rect(c, x, y - 4, bw, 4, BLUE, radius=2)
        para(c, ttl, st("bt", 8.8, 11, font="DVB", color=BLUE), x + 8, y - 13, bw - 16)
        hb = para(c, body, st("bb", 7.5, 9.8), x + 8, y - 28, bw - 16)
        para(c, src, st("bs", 6.4, 7.8, color=GREY), x + 8, y - 30 - hb, bw - 16)
    y = y - bh - 6

    thesis = ("<b>My thesis.</b> No, not automatically. SFDR improves transparency, not impact. The effect on emissions "
              "depends on additionality, shareholder engagement, and whether trade policy moves emissions elsewhere.")
    ht = para(c, thesis, st("th", 8.6, 11.8, color=white), M + 12, y - 7, CW - 24)
    rect(c, M, y - ht - 14, CW, ht + 14, BLUE, radius=6)
    para(c, thesis, st("th2", 8.6, 11.8, color=white), M + 12, y - 7, CW - 24)
    y_half = y - ht - 14

    c.setStrokeColor(GREY)
    c.setDash(3, 3)
    c.setLineWidth(0.6)
    sep_y = y_half - 10
    c.line(M, sep_y, W - M, sep_y)
    c.setDash()

    # ---------- BOTTOM HALF: summary ----------
    y = sep_y - 12
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(M, y - 8, "SUMMARY")
    y -= 17

    summary = [
        "A fund classified as Article 8 or 9 does not, on its own, prove that it reduces real-economy emissions. "
        "SFDR is first a transparency obligation: a declared strategy, principal adverse impact (PAI) indicators and the "
        "'do no significant harm' (DNSH) principle. This helps savers compare funds, but it describes what a fund says "
        "it does, not what its capital changes.",

        "The strongest case for a real effect runs through the cost of capital. The OAT–Bund spread rose from about "
        "96 bp in mid-September to about 175 bp on 22 October [2], and Moody's kept France at Aa3 with a negative outlook [1]. "
        "A premium of this size changes what borrowers pay. But it only helps the climate if the money is additional: buying "
        "listed shares moves a price, not a project.",

        "The second argument is displacement, which is the heart of the question. The EU–Mercosur interim agreement has "
        "applied provisionally since 1 May 2026 [3]. My inference, which I have not tested: if cheaper imports replace "
        "domestic production, part of the emissions moves abroad, so a portfolio can look greener while the problem is "
        "only relocated.",

        "<b>My view:</b> SFDR is a necessary but insufficient tool. It makes claims comparable, but an effect on emissions "
        "needs additional capital, engagement and PAI data tied to measured trajectories. <b>What would change my mind:</b> "
        "if published PAI data show, over several years, that Article 8/9 portfolios cut emissions faster than conventional "
        "funds, after allowing for displacement through trade.",
    ]
    s_body = st("sb", 8.7, 11.7)
    for txt in summary:
        hp = para(c, txt, s_body, M, y, CW)
        y -= hp + 4

    # ---------- SOURCES (footer) ----------
    src_lines = [
        "[1] Moody's affirms France at Aa3, negative outlook (23 Oct 2026): cnbc.com/2026/10/23/moodys-holds-steady-on-frances-credit-rating-as-country-grapples-with-turmoil-and-higher-yields.html",
        "[2] OAT–Bund spread: ideal-investisseur.fr/en/markets/oat-bund-spread.html (156.4 bp, 26 Oct 2026); fxstreet.com/analysis/france-tests-the-euros-nerve-what-the-oat-spread-is-telling-fx-traders-202610270406 (about 96 bp mid-Sep; 174.6 bp close 22 Oct). Sources differ by a few bp.",
        "[3] Intereconomics, 'From Signature to Standstill' (21 Oct 2026): intereconomics.eu/contents/year/2026/number/3/article/from-signature-to-standstill-the-future-of-the-eu-mercosur-agreement.html ; Council vote, 9 Jan 2026: intereconomics.eu/contents/year/2026/number/3/article/eu-mercosur-trade-agreement-from-negotiations-to-application.html",
        "Course: Sabrine Aouida, 'Skema Module 1 Sustainable Finance and impact investing', Modules 1 to 3. Check SFDR (EU) 2019/2088 against the official text.",
    ]
    fy = y - 6
    c.setFillColor(BLUE)
    c.setFont("DVB", 7)
    c.drawString(M, fy - 7, "SOURCES")
    fy -= 12
    for ln in src_lines:
        fy -= para(c, ln, st("src", 5.9, 7.2, color=GREY), M, fy, CW) + 1

    c.save()
    print("written:", OUT, "| summary end y =", round(y, 1), "| sources end y =", round(fy, 1))


if __name__ == "__main__":
    build()
