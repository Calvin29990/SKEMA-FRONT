"""Génère la présentation allégée 'Why would we invest in IKEA?' (6 pages, 16:9).

Sources des chiffres : 'Ingka ESG Profile.pdf' et 'ikea_esg_one_pager.pdf' (Drive, dossier Documents importants).
Usage : python3 build_presentation.py
"""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "IKEA-Why-invest-presentation-6p.pdf")
LOGO = os.path.join(HERE, "assets", "ikea-logo.png")

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DV", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DVB", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))

W, H = 960, 540
BLUE = HexColor("#0058A3")
YEL = HexColor("#FFDA1A")
INK = HexColor("#1A1A1A")
GREY = HexColor("#5F6368")
LIGHT = HexColor("#F3F5F8")
RED = HexColor("#B3261E")
GREEN = HexColor("#1E7B4A")
TOTAL = 6


def style(name, size, leading=None, font="DV", color=INK, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size,
                          leading=leading or size * 1.3, textColor=color, **kw)


S_BODY = style("body", 14, 19)
S_SMALL = style("small", 11, 15)
S_BUL = style("bul", 13, 18, leftIndent=14, firstLineIndent=-14, spaceAfter=5)
S_BUL_SM = style("bulsm", 11.5, 15.5, leftIndent=12, firstLineIndent=-12, spaceAfter=4)
S_FOOT = style("foot", 9, 11, color=GREY)
S_TITLE = style("title", 26, 30, font="DVB", color=BLUE)
S_KPI = style("kpi", 40, 44, font="DVB", color=BLUE)
S_KPI_LBL = style("kpil", 12.5, 16)
S_H3 = style("h3", 16, 20, font="DVB", color=BLUE)
S_CARD = style("card", 13, 17.5, leftIndent=12, firstLineIndent=-12, spaceAfter=4)


def para(c, text, st, x, y_top, w):
    """Dessine un paragraphe dont le haut est en y_top ; renvoie sa hauteur."""
    text = text.replace(' %', '&nbsp;%')
    p = Paragraph(text, st)
    _, h = p.wrap(w, 2000)
    p.drawOn(c, x, y_top - h)
    return h


def bullets(c, items, st, x, y_top, w):
    y = y_top
    for it in items:
        h = para(c, "•&nbsp;&nbsp;" + it, st, x, y, w)
        y -= h + st.spaceAfter
    return y_top - y


def rect(c, x, y, w, h, fill, radius=0):
    c.setFillColor(fill)
    c.setStrokeColor(fill)
    if radius:
        c.roundRect(x, y, w, h, radius, stroke=0, fill=1)
    else:
        c.rect(x, y, w, h, stroke=0, fill=1)


def header(c, title, n, subtitle=None):
    rect(c, 0, H - 10, W, 10, BLUE)
    para(c, title, S_TITLE, 48, H - 34, W - 200)
    if subtitle:
        para(c, subtitle, style("sub", 14, 18, color=GREY), 48, H - 98, W - 120)
    rect(c, 48, H - 118 if subtitle else H - 92, 70, 5, YEL)
    c.setFillColor(GREY)
    c.setFont("DV", 9)
    c.drawRightString(W - 40, 22, f"{n} / {TOTAL}")


def footer(c, text):
    para(c, text, S_FOOT, 48, 42, W - 120)


def slide_cover(c):
    rect(c, 0, 0, W, H, BLUE)
    rect(c, 0, 0, 14, H, YEL)
    # carte blanche pour le logo (fond bleu du logo conservé)
    rect(c, 56, H - 230, 208, 170, white, radius=12)
    c.drawImage(LOGO, 60, H - 226, width=200, height=142.8, mask='auto')
    c.setFillColor(YEL)
    c.setFont("DVB", 50)
    c.drawString(60, 200, "Why would we invest")
    c.drawString(60, 146, "in IKEA?")
    c.setFillColor(white)
    c.setFont("DV", 19)
    c.drawString(60, 108, "Une lecture ESG d'Ingka Group et d'IKEA France")
    rect(c, 60, 88, 90, 4, YEL)
    c.setFont("DV", 12)
    c.drawString(60, 56, "MSc CFM · SKEMA · Sustainable Finance")
    c.drawString(60, 38, "Calvin Minang · Jonathan Bouaffon · Liza Amouyal")
    c.setFont("DV", 9)
    c.drawRightString(W - 40, 22, f"1 / {TOTAL}")


def slide_answer(c):
    header(c, "Notre réponse : un oui conditionnel", 2)
    rect(c, 48, 100, 430, 300, YEL, radius=14)
    para(c, "Oui, sous conditions.", style("big", 30, 36, font="DVB", color=BLUE), 78, 372, 370)
    para(c, "Un cas de <b>réduction du risque</b>, pas une <b>prime ESG</b>.",
         style("b2", 19, 26), 78, 282, 370)
    para(c, "Nous n'avons aucune preuve que la performance ESG augmente le rendement ici : "
            "l'intérêt porte sur le coût du risque et du capital.",
         style("b3", 14, 19), 78, 216, 370)
    kpis = [
        ("−39 %", "émissions opérationnelles en France depuis 2016"),
        ("184 %", "des besoins électriques de la France couverts par éolien et solaire"),
        ("−30 %", "empreinte du groupe, tous scopes, depuis 2016, malgré la croissance"),
        ("−50 %", "objectif 2030 aligné SBTi (scopes 1 à 3), net zéro en 2050"),
    ]
    tw, th, gap = 205, 138, 14
    x0, y0 = 510, 400
    for i, (num, lbl) in enumerate(kpis):
        col, row = i % 2, i // 2
        x = x0 + col * (tw + gap)
        y = y0 - row * (th + gap)
        rect(c, x, y - th, tw, th, LIGHT, radius=12)
        rect(c, x, y - th, 6, th, BLUE)
        c.setFillColor(BLUE)
        c.setFont("DVB", 36)
        c.drawString(x + 22, y - 62, num)
        para(c, lbl, S_KPI_LBL, x + 22, y - 80, tw - 36)
    footer(c, "Sources : Ingka ESG Profile ; one-pager IKEA (Drive). Périmètres différents (France ≠ groupe) ; "
              "données auto-déclarées, non testées par nous.")


def slide_environment(c):
    header(c, "Environnement : la chaîne pèse plus", 3)
    # Graphique : répartition de l'empreinte
    para(c, "Répartition de l'empreinte du groupe", S_H3, 48, 390, 420)
    bars = [
        ("Matières premières", 52, BLUE),
        ("Usage à domicile", 17, BLUE),
        ("Autres postes (non détaillés)", 31, HexColor("#B8C4D6")),
    ]
    maxw = 330
    y = 362
    for label, val, col in bars:
        para(c, label, style("lab", 12.5, 15), 48, y, 300)
        rect(c, 48, y - 44, maxw * val / 52, 22, col, radius=4)
        c.setFillColor(INK)
        c.setFont("DVB", 13)
        c.drawString(48 + maxw * val / 52 + 8, y - 38, f"{val} %")
        y -= 60
    rect(c, 48, 100, 420, 90, LIGHT, radius=10)
    para(c, "<b>Lecture :</b> la baisse de 39 % en France porte sur nos opérations ; la matière et l'usage "
            "concentrent l'essentiel de l'empreinte, donc les choix d'achat comptent davantage.",
         style("note", 12.5, 16.5), 62, 180, 395)
    # Deux cartes
    cards = [
        ("Ce qui avance", GREEN, [
            "Opérations France : −39 % d'émissions depuis 2016",
            "Éolien et solaire : 184 % des besoins électriques",
            "Pompes à chaleur, géothermie, biomasse",
            "Chauffage sans fossile et 100 % de tri des déchets d'ici 2030",
        ]),
        ("Ce qui manque", RED, [
            "Taxonomie UE : alignement non publié",
            "Premiers résultats TNFD attendus en 2026",
            "Objectif SBTi : la transition est jugée discutable",
            "Fournisseurs : code IWAY et audits, à vérifier",
        ]),
    ]
    for i, (ttl, col, items) in enumerate(cards):
        x = 500 + i * 218
        rect(c, x, 130, 205, 330, LIGHT, radius=12)
        rect(c, x, 448, 205, 12, col, radius=4)
        para(c, ttl, style("ct", 16, 20, font="DVB", color=col), x + 16, 422, 180)
        bullets(c, items, S_CARD, x + 16, 392, 178)
    footer(c, "Sources : Ingka ESG Profile (volets Environnement, Risques, Objectifs) ; one-pager IKEA.")


def slide_social_gov(c):
    header(c, "Social & gouvernance : un risque mieux tenu", 4)
    kpis = [
        ("200–400", "emplois locaux par magasin"),
        ("≈ 200 M€", "investis pour baisser les prix de ~2 000 produits"),
        ("100 / 100", "indice égalité femmes-hommes, 4e année"),
        ("7 %", "d'emploi de personnes handicapées (légal : 6 %)"),
    ]
    for i, (num, lbl) in enumerate(kpis):
        x = 48 + i * 221
        rect(c, x, 330, 205, 120, BLUE, radius=12)
        c.setFillColor(YEL)
        c.setFont("DVB", 26)
        c.drawString(x + 16, 410, num)
        para(c, lbl, style("kl", 12, 15, color=white), x + 16, 396, 180)
    # Colonnes social / gouvernance
    para(c, "Social", S_H3, 48, 300, 420)
    bullets(c, [
        "Code IWAY : pas de travail des enfants, salaires équitables, audits fournisseurs",
        "Accessibilité : clients à revenus modestes, moins de risque réputationnel",
        "Fondation IKEA : plus de 2 Md€ depuis 2009 pour le logement des plus vulnérables",
        "Insertion : environ 250 réfugiés visés en 3 ans",
    ], S_BUL_SM, 48, 272, 420)
    para(c, "Gouvernance", S_H3, 500, 300, 420)
    bullets(c, [
        "Devoir de vigilance, CSRD et CS3D : le cadre réglementaire se durcit",
        "Reporting public annuel en France, publié et vérifiable",
        "Taxonomie UE non publiée : la part verte reste invérifiable",
        "SFDR classe des fonds, pas des entreprises : le lien est indirect",
    ], S_BUL_SM, 500, 272, 412)
    footer(c, "Sources : Ingka ESG Profile (volets Social, Gouvernance, Risques) ; one-pager IKEA.")


def slide_transmission(c):
    header(c, "De l'ESG à la valeur : trois canaux", 5)
    cols = [
        ("1  Flux de trésorerie", "Revenus et marges", [
            "L'accessibilité élargit la clientèle",
            "Seconde vie et rachat ajoutent de la marge",
            "L'énergie renouvelable couvre une part du coût énergétique",
        ], BLUE),
        ("2  Risque", "Taux d'actualisation", [
            "IWAY, audits et reporting réduisent les risques réglementaires et de réputation",
            "L'effet passe par le taux, pas par le chiffre d'affaires",
            "C'est l'effet principal retenu",
        ], YEL),
        ("3  Investissements", "Résilience future", [
            "Pompes à chaleur, géothermie, renouvelables",
            "Dépenses aujourd'hui, protection demain",
            "Effet difficile à chiffrer sans taxonomie publiée",
        ], BLUE),
    ]
    for i, (ttl, sub, items, col) in enumerate(cols):
        x = 48 + i * 298
        rect(c, x, 170, 280, 280, LIGHT, radius=12)
        rect(c, x, 418, 280, 32, col, radius=12)
        tcol = INK if col == YEL else white
        c.setFillColor(tcol)
        c.setFont("DVB", 14)
        c.drawString(x + 14, 428, ttl)
        para(c, sub, style("sb", 13, 16, font="DVB", color=BLUE), x + 16, 398, 250)
        bullets(c, items, style("cb", 13, 17.5, leftIndent=12, firstLineIndent=-12, spaceAfter=6),
                x + 16, 370, 250)
    rect(c, 48, 88, W - 96, 60, YEL, radius=10)
    para(c, "<b>Matérialité :</b> matières premières 52 % et usage 17 % de l'empreinte. "
            "La chaîne d'approvisionnement pèse donc plus que la baisse de 39 % en France.",
         style("mat", 14, 18, color=INK), 66, 136, W - 130)
    footer(c, "Sources : Ingka ESG Profile (empreinte, risques) ; one-pager IKEA (raisonnement et limites).")


def slide_decision(c):
    header(c, "Règle de décision : quatre conditions", 6)
    conds = [
        ("a", "Les allégations vertes restent vérifiables"),
        ("b", "L'alignement à la taxonomie est publié dans le prochain rapport"),
        ("c", "Les premiers résultats TNFD soutiennent la feuille de route nature"),
        ("d", "Le groupe reste sur la trajectoire −50 % d'ici 2030 (scopes 1 à 3)"),
    ]
    y = 380
    for letter, txt in conds:
        c.setFillColor(BLUE)
        c.circle(78, y - 14, 17, stroke=0, fill=1)
        c.setFillColor(YEL)
        c.setFont("DVB", 15)
        c.drawCentredString(78, y - 20, letter)
        para(c, txt, style("cond", 15.5, 20), 108, y - 2, 380)
        y -= 66
    rect(c, 530, 150, 382, 300, LIGHT, radius=12)
    para(c, "Limites à garder en tête", S_H3, 548, 420, 350)
    bullets(c, [
        "Aucune valorisation, aucune analyse de spread, aucun rendement",
        "Groupe non coté : détention à vérifier (Stichting INGKA Foundation)",
        "Une seule année de reporting, données auto-déclarées",
        "Chiffres France et groupe : périmètres différents",
        "Voie d'investissement (dette ou privé) à confirmer",
    ], style("lim", 13, 17, leftIndent=12, firstLineIndent=-12, spaceAfter=6), 548, 392, 350)
    rect(c, 48, 60, W - 96, 58, BLUE, radius=10)
    para(c, "<font color='#FFDA1A'><b>Verdict :</b></font> <font color='#FFFFFF'>oui conditionnel, "
            "un cas de réduction du risque, révisé si une des quatre conditions tombe.</font>",
         style("verd", 15, 20), 70, 96, W - 140)
    footer(c, "Sources : one-pager IKEA (règle de décision, limites) ; Ingka ESG Profile (objectifs, Taxonomie, TNFD).")


def build():
    c = canvas.Canvas(OUT, pagesize=(W, H))
    c.setTitle("Why would we invest in IKEA? - présentation 6 pages")
    c.setAuthor("Calvin Minang, Jonathan Bouaffon, Liza Amouyal")
    for fn in (slide_cover, slide_answer, slide_environment, slide_social_gov,
               slide_transmission, slide_decision):
        fn(c)
        c.showPage()
    c.save()
    print("écrit :", OUT)


if __name__ == "__main__":
    build()
