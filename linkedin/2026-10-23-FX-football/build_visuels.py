#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère les visuels LinkedIn du post « PSG-Barça / FX / clubs de foot ».
Sortie : assets/01-carte.png, assets/02-flux.png, assets/03-methode.png, assets/carrousel-FX-football.pdf

Volontairement agrégé : aucune commune, aucun nom d'entreprise, aucun montant par région.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon as MplPolygon, Rectangle
from matplotlib.backends.backend_pdf import PdfPages

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
os.makedirs(ASSETS, exist_ok=True)

# ---------------------------------------------------------------- palette
INK = "#0E1F17"
GREEN = "#12624A"
GREEN_L = "#3E9A72"
GREEN_LL = "#BFDCCB"
CREAM = "#F4F1E7"
PAPER = "#FCFBF7"
AMBER = "#C9821F"
GREY = "#66736D"

W, H = 10.8, 13.5
DPI = 100

plt.rcParams.update({"font.family": "DejaVu Sans", "pdf.fonttype": 42})


def new_page(bg=PAPER):
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    fig.patch.set_facecolor(bg)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_facecolor(bg)
    return fig, ax


def T(ax, x, y, s, size=12, color=INK, weight="normal", ha="left", va="baseline",
      style="normal", spacing=1.0, alpha=1.0):
    return ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va,
                   style=style, alpha=alpha, linespacing=spacing, transform=ax.transAxes)


def rule(ax, x0, x1, y, color=GREEN, lw=1.2, alpha=0.5):
    ax.plot([x0, x1], [y, y], color=color, lw=lw, alpha=alpha,
            transform=ax.transAxes, solid_capstyle="butt")


def box(ax, x, y, w, h, fc=CREAM, ec="none", lw=1.0, r=0.01, alpha=1.0, z=1):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw, alpha=alpha, zorder=z,
                                transform=ax.transAxes, clip_on=False))


def header(ax, left, right, dark=True):
    box(ax, 0, 0.947, 1, 0.053, fc=GREEN if dark else CREAM, r=0)
    T(ax, 0.045, 0.968, left, size=8.4, color=GREEN_LL if dark else GREY, weight="bold", va="center")
    T(ax, 0.955, 0.968, right, size=8.4, color=PAPER if dark else GREY, weight="bold",
      ha="right", va="center")


def footnote(ax, s, y=0.048):
    T(ax, 0.045, y, s, size=6.7, color=GREY, va="top", spacing=1.55)


# ---------------------------------------------------------------- géo
FEATS = json.load(open(os.path.join(ASSETS, "regions.geojson")))["features"]

CLASS = {"11": 4, "84": 3, "32": 3, "76": 3,
         "44": 2, "75": 2, "93": 2, "52": 2,
         "28": 1, "53": 1, "27": 1, "24": 1, "94": 0}
SHADES = {0: "#E6E2D3", 1: "#C9DBCC", 2: "#93BFA3", 3: "#47936F", 4: "#12624A"}
LEGEND = [("> 10 000", 4), ("3 000 – 4 000", 3), ("2 000 – 3 000", 2),
          ("1 000 – 2 000", 1), ("< 1 000", 0)]


def rings(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"][0]]
    return [poly[0] for poly in geom["coordinates"]]


def draw_map(ax, rect, label_font=8.0):
    axm = ax.inset_axes(rect)
    axm.set_aspect("equal")
    axm.axis("off")
    for f in FEATS:
        col = SHADES[CLASS.get(f["properties"]["code"], 0)]
        for ring in rings(f["geometry"]):
            axm.add_patch(MplPolygon(ring, closed=True, fc=col, ec=PAPER, lw=1.8, zorder=2))
    axm.set_xlim(-5.5, 9.9)
    axm.set_ylim(41.1, 51.3)

    for name, (x, y), dark in [("Île-de-France", (3.0, 48.55), True),
                               ("Occitanie", (1.5, 43.6), False),
                               ("Auvergne-\nRhône-Alpes", (4.5, 45.1), False),
                               ("Nouvelle-Aquitaine", (-0.3, 45.3), False),
                               ("Hauts-de-France", (2.6, 50.2), False)]:
        axm.text(x, y, name, fontsize=label_font, color=PAPER if dark else INK,
                 ha="center", va="center", zorder=5, linespacing=1.3,
                 fontweight="bold" if dark else "normal")
    return axm


# ---------------------------------------------------------------- 1. carte
def page_carte():
    fig, ax = new_page()
    header(ax, "NOTE DE RECHERCHE  ·  ORBIS 20/10/2026  ·  MISE EN FORME PERSONNELLE",
           "CALVIN MINANG  ·  1/3")

    T(ax, 0.045, 0.928, "OÙ VIT LE RISQUE\nDE CHANGE FRANÇAIS",
      size=31, color=INK, weight="bold", va="top", spacing=1.05)
    T(ax, 0.045, 0.855,
      "64 646 sociétés françaises ≥ 5 M€ de CA. Une carte, cinq classes, zéro nom.",
      size=10.8, color=GREY, va="top")

    draw_map(ax, [0.04, 0.300, 0.92, 0.545], label_font=7.8)

    # légende horizontale
    lx, ly = 0.055, 0.278
    for lab, c in LEGEND:
        ax.add_patch(Rectangle((lx, ly), 0.021, 0.0105, fc=SHADES[c], ec="none",
                               transform=ax.transAxes, zorder=6))
        T(ax, lx + 0.030, ly + 0.0052, lab, size=8.0, color=INK, va="center")
        lx += 0.135
    T(ax, 0.055, 0.259, "sièges d'entreprises mesurés par région — ordre de grandeur, aucune valeur exacte publiée",
      size=7.2, color=GREY, va="top", style="italic")

    stats = [("45 837", "sociétés géolocalisées\nsur les 64 646 du périmètre"),
             ("32,9 %", "des sièges concentrés\nen Île-de-France"),
             ("68,1 %", "du CA national\nconcentré en Île-de-France")]
    wgl = 0.288
    for i, (big, small) in enumerate(stats):
        x = 0.045 + i * (wgl + 0.023)
        box(ax, x, 0.152, wgl, 0.096, fc=CREAM)
        T(ax, x + 0.020, 0.238, big, size=19, color=GREEN, weight="bold", va="top")
        T(ax, x + 0.020, 0.198, small, size=8.0, color=INK, va="top", spacing=1.4)

    box(ax, 0.045, 0.075, 0.91, 0.062, fc=GREEN)
    T(ax, 0.066, 0.122, "CE QUE LA CARTE NE DIT PAS", size=8.2, color=GREEN_LL, weight="bold")
    T(ax, 0.066, 0.094,
      "Le segment qui m'a le plus surpris n'est ni une banque ni une industrie : c'est le sport professionnel.",
      size=10.2, color=PAPER, weight="bold")

    footnote(ax, "Périmètre : comptes ≥ 5 M€ de CA, France entière + outre-mer · agrégation par région : aucune commune, aucun nom d'entreprise, aucun montant individuel.\n"
                 "Sources : Orbis (Bureau van Dijk) 20/10/2026 · géolocalisation INSEE · retraitements et classification personnels. Étude personnelle hors mission, aucune donnée client.")
    return fig


# ---------------------------------------------------------------- 2. flux
def page_flux():
    fig, ax = new_page()
    header(ax, "PSG 4 – 2 BARÇA  ·  MARDI 20 OCTOBRE", "2/3")

    T(ax, 0.045, 0.928, "UN CLUB DE FOOT EST\nUNE PME MULTIDEVISES",
      size=26, color=INK, weight="bold", va="top", spacing=1.08)
    T(ax, 0.045, 0.845,
      "Il encaisse dans une devise, paie dans une autre, et signe aujourd'hui\nce qu'il paiera dans trois ans. Cinq flux, cinq expositions.",
      size=10.2, color=GREY, va="top", spacing=1.6)

    rows = [
        ("01", "INDEMNITÉS DE TRANSFERT",
         "Les clubs de Premier League ont dépensé plus de 1,7 Md£ en joueurs\nvenus de clubs de la zone euro sur un seul mercato.",
         "EUR → GBP"),
        ("02", "PAIEMENTS ÉCHELONNÉS",
         "Les transferts se règlent en 3 à 5 échéances. L'exposition au change\ncourt bien après la signature : besoin de couverture, pas de spot.",
         "forward 12–48 m"),
        ("03", "SALAIRES & STAFF ÉTRANGERS",
         "Joueurs, entraîneurs, staff médical : des salaires versés en devise,\nchaque mois, sur des corridors multiples.",
         "BRL · ARS · CHF · JPY"),
        ("04", "DROITS TV & SPONSORS",
         "Diffusion et sponsoring arrivent en devise, à date connue :\nle cash-flow est prévisible, donc couvrable.",
         "USD · GBP · QAR"),
        ("05", "MERCHANDISING & TOURNÉES",
         "Pré-saison, boutiques, licences : des encaissements dans 10 à 20 devises,\nsouvent petits, souvent oubliés dans le budget FX.",
         "20+ devises"),
    ]
    y = 0.713
    for num, title, body, tag in rows:
        box(ax, 0.045, y, 0.91, 0.093, fc=CREAM)
        T(ax, 0.062, y + 0.070, num, size=13, color=AMBER, weight="bold", va="top")
        T(ax, 0.062, y + 0.030, tag, size=7.2, color=GREY, va="top", style="italic")
        T(ax, 0.205, y + 0.070, title, size=9.4, color=GREEN, weight="bold", va="top")
        T(ax, 0.205, y + 0.046, body, size=8.4, color=INK, va="top", spacing=1.55)
        y -= 0.116

    box(ax, 0.045, 0.122, 0.91, 0.098, fc=GREEN)
    T(ax, 0.066, 0.198, "LE VRAI SUJET", size=8.2, color=GREEN_LL, weight="bold")
    T(ax, 0.066, 0.172,
      "Un club a la complexité financière d'une multinationale et la trésorerie d'une PME.",
      size=10.6, color=PAPER, weight="bold")
    T(ax, 0.066, 0.145,
      "Ce n'est pas un client « exotique » : c'est le cœur de cible d'une fintech FX.",
      size=10.6, color=GREEN_LL, weight="bold")

    footnote(ax, "Sources : FIFA TMS / marché des transferts internationaux · dépenses des clubs de Premier League vers la zone euro, données reprises par The Fintech Times\n"
                 "et Finance Magnates (étude Glyde, 2026) · Ebury / FC Business sur les échéanciers de 3 à 5 ans et le financement de transfert. Chiffres publics, non retraités.")
    return fig


# ---------------------------------------------------------------- 3. méthode
def page_methode():
    fig, ax = new_page()
    header(ax, "MÉTHODE & SOURCES", "3/3")

    T(ax, 0.045, 0.928, "CE QUE JE MONTRE,\nCE QUE JE GARDE",
      size=26, color=INK, weight="bold", va="top", spacing=1.08)
    T(ax, 0.045, 0.845,
      "Le sujet n'est pas la carte. C'est la question qu'elle permet de poser à un commercial FX :\nqui, dans mon portefeuille, paie déjà en devise sans que personne ne l'ait benchmarké ?",
      size=10.2, color=GREY, va="top", spacing=1.6)

    cols = [("PUBLIC", GREEN, ["Le nombre de sociétés du périmètre",
                                "La répartition par région, en classes",
                                "Les ratios nationaux (IDF, poids du CA)",
                                "Une intuition de segment : le sport pro"]),
            ("GARDÉ", AMBER, ["Les communes et les noms d'entreprises",
                               "Les montants société par société",
                               "Le croisement flux récurrents / épisodiques",
                               "La liste nominative des cibles"])]
    x = 0.045
    for title, col, items in cols:
        box(ax, x, 0.455, 0.435, 0.305, fc=CREAM)
        T(ax, x + 0.022, 0.735, title, size=9.2, color=col, weight="bold", va="top")
        rule(ax, x + 0.022, x + 0.413, 0.720, color=col, lw=1.4, alpha=0.9)
        yy = 0.690
        for it in items:
            T(ax, x + 0.022, yy, "—", size=8.4, color=col, weight="bold", va="top")
            T(ax, x + 0.046, yy, it, size=8.3, color=INK, va="top")
            yy -= 0.055
        x += 0.46

    T(ax, 0.045, 0.430, "SOURCES UTILISÉES", size=8.4, color=GREEN, weight="bold")
    rule(ax, 0.045, 0.955, 0.420, color=GREEN, lw=1.0, alpha=0.4)

    src = [("Orbis — Bureau van Dijk", "comptes annuels, périmètre ≥ 5 M€ de CA, extraction du 20/10/2026"),
           ("INSEE", "géolocalisation des sièges à la commune, millésime 2026"),
           ("FIFA — TMS / Clearing House", "transferts internationaux, échéanciers, contribution de solidarité"),
           ("The Fintech Times · Finance Magnates", "coût caché du change sur les paiements de transfert des clubs"),
           ("FC Business · Ebury", "échéanciers 3–5 ans et financement de transfert")]
    yy = 0.392
    for a, b in src:
        T(ax, 0.045, yy, a, size=8.4, color=INK, weight="bold", va="top")
        T(ax, 0.345, yy, b, size=8.4, color=GREY, va="top")
        yy -= 0.032

    box(ax, 0.045, 0.090, 0.91, 0.128, fc=INK)
    T(ax, 0.066, 0.196, "LE POINT QUE JE VOUDRAIS DÉFENDRE EN ENTRETIEN", size=8.2,
      color=GREEN_LL, weight="bold")
    T(ax, 0.066, 0.176,
      "Le FX n'est pas une classe d'actifs qu'on aime par goût de la volatilité. C'est une industrie\n"
      "qui vit d'un problème très concret : quelqu'un, quelque part, doit payer en devise,\n"
      "et personne ne lui a dit combien ça lui coûte.",
      size=9.4, color=PAPER, va="top", spacing=1.8)

    footnote(ax, "Étude personnelle réalisée hors mission, sur données publiques et licences académiques. Aucune donnée client, aucune donnée confidentielle.\n"
                 "La carte détaillée et les jeux de données ne sont pas diffusés.")
    return fig


# ---------------------------------------------------------------- build
if __name__ == "__main__":
    pages = [(page_carte, "01-carte.png"), (page_flux, "02-flux.png"), (page_methode, "03-methode.png")]
    figs = []
    for fn, name in pages:
        f = fn()
        f.savefig(os.path.join(ASSETS, name), dpi=DPI, facecolor=f.get_facecolor())
        figs.append(f)
        print("ok", name)
    with PdfPages(os.path.join(ASSETS, "carrousel-FX-football.pdf")) as pdf:
        for f in figs:
            pdf.savefig(f, facecolor=f.get_facecolor())
    print("ok carrousel-FX-football.pdf")
