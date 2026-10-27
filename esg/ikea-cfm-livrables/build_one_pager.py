"""One-pager individuel (A4, une page recto) - version 2 avec graphique et carte de France.

Haut de page : question, graphique (chiffres IKEA / Ingka), carte schématique de la France,
branches de raisonnement, thèse. Bas de page : synthèse.

ATTENTION : la question et la thèse sont un BROUILLON à remplacer par le point de vue
personnel de l'étudiant (exigence du cours : l'opinion doit être la sienne).
La carte est SCHÉMATIQUE : aucune donnée régionale vérifiée n'est affichée.

Usage : python3 build_one_pager.py   (nécessite le GeoJSON fr-all.geo.json, voir MAP_GEOJSON)
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
import math

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "One-page-Calvin-Minang.pdf")
MAP_GEOJSON = os.environ.get(
    "MAP_GEOJSON", "/tmp/mapdl/package/countries/fr/fr-all.geo.json")  # Highcharts map-collection (npm)
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
    """Barres : réduction des émissions vs 2016 (chiffres du profil Ingka ESG)."""
    rect(c, x, y_top - h, w, h, LIGHT, radius=6)
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(x + 10, y_top - 16, "Réduction des émissions vs 2016")
    rows = [
        ("IKEA France, opérations", 39, BLUE),
        ("Groupe, scopes 1 à 3", 30, BLUE),
        ("Objectif groupe 2030", 50, HexColor("#9DB9DC")),
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
    para(c, "Source : Ingka ESG Profile. Périmètres différents ; l'objectif 2030 n'est pas encore atteint.",
         st("gn", 6.8, 8.6, color=GREY), x + 10, y_top - h + 26, w - 20)


def draw_map(c, x, y_top, w, h):
    """Carte schématique des régions de France métropolitaine ; Île-de-France en évidence.
    Les coordonnées du GeoJSON Highcharts sont planes (projection), on les met à l'échelle directement."""
    rect(c, x, y_top - h, w, h, LIGHT, radius=6)
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(x + 10, y_top - 16, "Carte schématique de la France")
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
    # étiquette Île-de-France dans la marge droite de la carte, reliée par un trait
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
        para(c, "où se gère l'épargne", st("ml", 6.6, 8, color=white), lx + 5, ly + lh - 16, lw - 8)
    para(c, "Schéma : aucune donnée régionale vérifiée. Idée : la décision d'allocation se prend au centre, "
            "son effet se joue dans les régions.",
         st("mn", 6.6, 8.4, color=GREY), x + 10, y_top - h + 26, w - 20)


def build():
    c = canvas.Canvas(OUT, pagesize=A4)
    c.setTitle("One-page - Calvin Minang - E focus finance (brouillon)")
    c.setAuthor("Calvin Minang")

    rect(c, 0, H - 8, W, 8, BLUE)
    c.setFillColor(GREY)
    c.setFont("DV", 7.5)
    c.drawString(M, H - 24, "CFM · Sustainable Finance · One-pager individuel · Calvin Minang")
    c.drawRightString(W - M, H - 24, "Recto unique")

    # ---------- MOITIÉ HAUTE ----------
    y = H - 40
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(M, y - 8, "CARTE DU RAISONNEMENT")
    y -= 18

    q = ("<b>Question.</b> Les fonds Article 8 et 9 (SFDR) réduisent-ils réellement les émissions "
         "de l'économie réelle, ou déplacent-ils seulement le problème ?")
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
        ("1 · Transparence ≠ impact",
         "Le SFDR impose une stratégie déclarée et des indicateurs PAI. L'Article 8 « promeut », "
         "l'Article 9 vise un « objectif d'investissement durable ». Aucun ne fixe de baisse mesurée des émissions.",
         "Cours, Module 2 (SFDR, PAI, DNSH)"),
        ("2 · Coût du capital",
         "Exclure ou pondérer un émetteur renchérit son capital. L'effet réel passe par les flux primaires : "
         "un achat sur le marché secondaire ne finance aucun projet.",
         "Cours, Modules 1 et 3 (exclusion, additionnalité)"),
        ("3 · Preuve et greenwashing",
         "La taxonomie UE mesure une éligibilité, pas une baisse d'émissions. Une même étiquette peut couvrir "
         "des effets très différents.",
         "Cours, Module 2 (taxonomie, greenwashing)"),
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

    thesis = ("<b>Ma thèse.</b> Non, pas automatiquement. Le SFDR améliore la transparence, pas l'impact. "
              "L'effet environnemental dépend de l'engagement actionnarial et de l'additionnalité du financement.")
    ht = para(c, thesis, st("th", 8.9, 12.2, color=white), M + 12, y - 7, CW - 24)
    rect(c, M, y - ht - 14, CW, ht + 14, BLUE, radius=6)
    para(c, thesis, st("th2", 8.9, 12.2, color=white), M + 12, y - 7, CW - 24)
    y_half = y - ht - 14

    # Séparateur
    c.setStrokeColor(GREY)
    c.setDash(3, 3)
    c.setLineWidth(0.6)
    sep_y = y_half - 12
    c.line(M, sep_y, W - M, sep_y)
    c.setDash()

    # ---------- MOITIÉ BASSE ----------
    y = sep_y - 14
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(M, y - 8, "SYNTHÈSE")
    y -= 18

    summary = [
        "Un fonds classé Article 8 ou 9 ne prouve pas, à lui seul, qu'il réduit les émissions de l'économie réelle. "
        "Le SFDR est d'abord une obligation de transparence : stratégie déclarée, principales incidences négatives (PAI) "
        "et principe « do no significant harm » (DNSH). Cette transparence a une vraie valeur, car elle permet à "
        "l'épargnant de comparer. Mais elle décrit ce qu'un fonds déclare faire, pas ce que son capital produit.",

        "Mon point de vue est donc nuancé. Le levier environnemental passe moins par le label que par deux mécanismes. "
        "Le premier est l'engagement : vote en assemblée générale, dialogue, et escalade jusqu'à la cession. "
        "Le second est l'additionnalité : financer des projets qui n'auraient pas été financés sans ce capital. "
        "Un portefeuille bien noté peut détenir des actions déjà cotées, dont le prix change de main sans que le "
        "capital réel bouge. Dans ce cas, le fonds gagne en réputation sans réduire d'émissions.",

        "Je retiens donc que le SFDR est un outil nécessaire mais insuffisant. Pour qu'il tienne sa promesse, il "
        "faudrait relier les PAI à des trajectoires mesurées, publier des données vérifiables et distinguer le "
        "financement primaire du secondaire. Ma position peut être contestée sur un point : si les fonds Article 8/9 "
        "excluent finalement les émetteurs les plus émetteurs, la pression sur leur coût du capital peut suffire à "
        "changer leur comportement, même sans engagement actif. C'est le test que je proposerais aux données.",

        "<b>Ce qui me ferait changer d'avis :</b> si les PAI publiés montrent, sur plusieurs années, une baisse des "
        "émissions des portefeuilles Article 8/9 supérieure à celle des fonds classiques, vérifiable par une source publique.",
    ]
    s_body = st("sb", 9.4, 13.0)
    for txt in summary:
        hp = para(c, txt, s_body, M, y, CW)
        y -= hp + 6

    c.setFillColor(GREY)
    c.setFont("DV", 6.8)
    foot = ("Sources : cours Sabrine Aouida, Modules 1 à 3 ; Ingka ESG Profile (chiffres IKEA). "
            "Règlements à vérifier sur les textes officiels : SFDR (UE) 2019/2088 ; taxonomie (UE) 2020/852.")
    para(c, foot, st("ft", 6.8, 8.6, color=GREY), M, 40, CW)

    c.save()
    print("écrit :", OUT, "| bas de synthèse y =", round(y, 1), "| séparateur y =", round(sep_y, 1))


if __name__ == "__main__":
    build()
