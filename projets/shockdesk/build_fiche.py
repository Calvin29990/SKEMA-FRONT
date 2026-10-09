#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_fiche.py — Régénère projets/shockdesk/FICHE-PROJET-ShockDesk.pdf

Format alternatif au cours de 57 pages pour l'envoi BNP : 1 page « fiche projet »
droite au but, dans le même design que le CV (A4, Helvetica, #17375E).

Usage :  python3 build_fiche.py        (depuis projets/shockdesk/)
Dépendance : pip install reportlab
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth

NAVY = (0x17 / 255.0, 0x37 / 255.0, 0x5E / 255.0)
INK = (0x11 / 255.0, 0x11 / 255.0, 0x11 / 255.0)
GRAY = (0x3D / 255.0, 0x3D / 255.0, 0x3D / 255.0)

W, H = A4
ML, RIGHT = 48.5, 546.76
LEAD, BASE = 11.76, 1.116
REG, BLD = "Helvetica", "Helvetica-Bold"

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "FICHE-PROJET-ShockDesk.pdf")

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Fiche projet — ShockDesk")
c.setAuthor("Calvin MINANG")
c.setSubject("ShockDesk — poste de trading & stress-testing · Fiche projet")
c.setCreator("build_fiche.py (reportlab)")
t = 0.0


def wrap(segs, size, first_x, cont_x):
    words = []
    for text, font in segs:
        for w in text.split(" "):
            if w:
                words.append((w, font))
    lines, cur, cur_w, first = [], [], 0.0, True
    for w, font in words:
        ww = stringWidth(w, font, size)
        sp = stringWidth(" ", font, size)
        if cur and cur_w + sp + ww > RIGHT - (first_x if first else cont_x):
            lines.append(cur)
            cur, cur_w, first = [], 0.0, False
        if cur:
            cur_w += sp
        cur.append((w, font))
        cur_w += ww
    if cur:
        lines.append(cur)
    return lines


URLS = {
    "shockdesk.onrender.com": "https://shockdesk.onrender.com",
    "calvin.minang@skema.edu": "mailto:calvin.minang@skema.edu",
    "linkedin.com/in/calvin-minang": "https://linkedin.com/in/calvin-minang",
}


def line(segs, size=9.2, color=INK, first_x=None, cont_x=None, center=False):
    global t
    first_x = ML if first_x is None else first_x
    cont_x = ML if cont_x is None else cont_x
    for i, words in enumerate(wrap(segs, size, first_x, cont_x)):
        if center:
            total = sum(stringWidth(w, f, size) for w, f in words) + \
                stringWidth(" ", REG, size) * (len(words) - 1)
            x = (W - total) / 2.0
        else:
            x = first_x if i == 0 else cont_x
        c.setFillColorRGB(*color)
        for w, f in words:
            c.setFont(f, size)
            c.drawString(x, H - (t + size * BASE), w)
            ww = stringWidth(w, f, size)
            for key, url in URLS.items():
                if key in w:
                    c.linkURL(url, (x, H - (t + size), x + ww, H - t + size * 0.3),
                              relative=0, thickness=0)
                    break
            x += ww + stringWidth(" ", REG, size)
        t += LEAD


def section(title):
    global t
    t += 6.1
    c.setFillColorRGB(*NAVY)
    c.setFont(BLD, 10.4)
    c.drawString(ML, H - (t + 10.4 * BASE), title)
    rule_t = t + 15.2
    c.setStrokeColorRGB(*NAVY)
    c.setLineWidth(0.7)
    c.line(ML + 0.02, H - rule_t, RIGHT, H - rule_t)
    t += 16.5


def bullet(segs, size=9.2):
    global t
    c.setFillColorRGB(*GRAY)
    c.setFont(REG, 10.0)
    c.drawString(ML, H - (t + size * BASE), "•")
    line(segs, size=size, color=GRAY, first_x=58.0, cont_x=57.5)


# ------------------------------------------------------------------ header ----
t = 37.3
line([("SHOCKDESK", BLD)], size=18.0, color=NAVY, center=True)
t = 60.9
line([("Poste de trading & stress-testing — Fiche projet | Calvin MINANG", BLD)],
     size=9.8, color=INK, center=True)
t = 75.9
line([("Démo live : shockdesk.onrender.com | calvin.minang@skema.edu | +33 7 52 97 58 09", REG)],
     size=9.1, color=INK, center=True)

# --------------------------------------------------------------- en une ------
section("EN UNE PHRASE")
line([("Un poste de travail de desk complet, en Python : on publie une vue datée, on la dimensionne, on la "
       "backteste avec les coûts réels, on l'explique ligne par ligne, et on la corrige par révision — "
       "la discipline d'une salle de marché, de la publication du scénario au trade testé.", REG)])

# ------------------------------------------------------- ce que ça fait ------
section("CE QUE LE POSTE FAIT")
bullet([("Prévisions", BLD), (" — une vue publiée est un objet daté : signe, amplitude, pic, stop et date d'arrêt "
        "fixés ex-ante ; révisions numérotées et auditables ; scorecard ex-post qui affiche les misses avec "
        "les réussites (sens mesuré net du drift, pondéré par le bêta de la ligne).", REG)])
bullet([("Backtest", BLD), (" — moteur avec slippage (5 bps) et commissions facturés, attribution du P&L par "
        "ligne, comparaison alpha/bêta au benchmark, turnover et coût moyen rapportés au résultat.", REG)])
bullet([("Options", BLD), (" — pricer Black-Scholes, surface de volatilité (skew, terme), Greeks, catalogue de "
        "structures : butterfly, iron condor, strangles — prime nette, points morts, pertes et gains max.", REG)])
bullet([("Interface", BLD), (" — recherche, code, backtest, anticipation, options : la même grammaire d'URL pour "
        "l'interface, l'API HTTP et la ligne de commande.", REG)])

# ----------------------------------------------------------- cas pratique ----
section("CAS PRATIQUE — BOOK CHOC PÉTROLIER « SHOCKLAB »")
line([("Scénario géopolitique Brent (type détroit d'Ormuz) joué sur l'univers global-macro (Brent, S&P 500, "
       "TLT, or, dollar, crédit HY). Fenêtre 01/07/2026 → 29/08/2026 · 42 barres yfinance (données réelles) · "
       "21 trades · 60,6 M$ échangés · capital de départ 25,5 M$. Entrée à la publication du scénario, "
       "sortie au stop calendaire fixé ex-ante — et chaque ligne du P&L est expliquée par l'attribution.", REG)])

# ------------------------------------------------------- objet de desk ------
section("POURQUOI C'EST UN OBJET DE DESK")
bullet([("Un backtest sans attribution ne se commente pas : un P&L positif porté par une seule ligne est un pari, "
         "pas une stratégie — et on le dit avant que le hasard s'en mêle.", REG)])
bullet([("On publie avant de savoir : la révision corrige, elle ne réécrit pas l'historique.", REG)])
bullet([("On mesure net du marché : le sens d'une vue se lit déduit du benchmark, pondéré par le bêta.", REG)])

# ------------------------------------------------- produits structurés -----
section("POUR UN DESK PRODUITS STRUCTURÉS")
bullet([("Le catalogue de structures traduit directement une prévision en payoff : amplitude attendue vs mouvement "
         "payé par l'IV, choix butterfly / iron condor / strangle, prime et points morts calculés — le même "
         "raisonnement que sur un desk de vendue d'options.", REG)])
bullet([("Le book ShockLab et ses chargements factoriels (SPX, OIL, RATES, GOLD, USD, CREDIT) montrent la lecture "
         "de corrélations d'un livre multi-actifs avant de lancer un backtest.", REG)])

# ---------------------------------------------------------------- accès -----
section("ACCÈS & SUIVI")
bullet([("Démo live de 15 minutes possible (shockdesk.onrender.com) : le book choc pétrolier rejoué en direct, "
         "de la prévision publiée à l'attribution du P&L.", REG)])
bullet([("Fonctionnalités démontrées en direct : publication du scénario, backtest avec coûts, "
         "attribution du P&L ligne par ligne, passage prévision → structure.", REG)])
bullet([("Je joins volontiers le support de formation « ShockDesk — Cours pratique des concepts de "
         "desk » (57 pages, 19 modules, 10 ateliers) pour aller plus loin.", REG)])

# ------------------------------------------------------------- footer ------
# bandeau navy en bas de page (identité visuelle du portfolio)
band_top = 762.0
c.setFillColorRGB(*NAVY)
c.rect(0, H - band_top - 44.0, W, 44.0, stroke=0, fill=1)
c.setFillColorRGB(1, 1, 1)
c.setFont(BLD, 9.2)
c.drawString(ML, H - band_top - 15.0, "Calvin MINANG — Stage Front Office (Vente / Structuration), janv. 2027")
c.setFont(REG, 8.6)
c.drawString(ML, H - band_top - 28.5,
             "calvin.minang@skema.edu · +33 7 52 97 58 09 · linkedin.com/in/calvin-minang")
c.setFont(BLD, 8.6)
c.drawRightString(RIGHT, H - band_top - 15.0, "Démo 15 min : shockdesk.onrender.com")
c.setFont(REG, 8.6)
c.drawRightString(RIGHT, H - band_top - 28.5, "Support de formation (57 p.) joint si utile")

print("bas de la dernière ligne : %.1f pt (limite utile ~ 801.9)" % t)
c.showPage()
c.save()
print("Fiche générée :", OUT)
