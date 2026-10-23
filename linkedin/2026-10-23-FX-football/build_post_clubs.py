#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuel LinkedIn — palette reprise de la carte d'origine (papier crème, vert profond,
ambre, aplats beiges) et UNE COULEUR PAR CLUB.

Sortie : assets/06-post-carte-clubs.png (1080 x 1350)
"""
import json
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import Polygon as MPoly, Rectangle, FancyBboxPatch, Circle

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_map import CLUBS, REGIONS  # noqa: E402

ASSETS = os.path.join(HERE, "assets")

# ---------------------------------------------------------------- palette reprise de la carte source
PAPER = "#F7F2E4"        # fond crème
PANEL = "#EFE8D6"        # aplat beige clair (zones "contingent")
PANEL2 = "#E5DCC4"       # aplat beige plus dense (Île-de-France)
INK = "#12301F"          # vert-noir du texte
GREEN = "#1D6B4C"        # vert profond (cœur)
AMBER = "#C8912F"        # ambre (contingent)
MUTED = "#6E7268"
LINE = "#D8CFB6"

# une couleur par club — 12 teintes distinctes, lisibles sur crème
CLUB_COLOR = {
    "Olympique Lyonnais": "#0072B2",     # bleu
    "AS Monaco": "#D55E00",              # vermillon
    "Olympique de Marseille": "#3E9FD6",  # bleu ciel
    "Toulouse FC": "#6A4C93",            # violet
    "Stade de Reims": "#009E73",         # vert jade
    "Paris Saint-Germain": "#8C2F39",    # bordeaux
    "LOSC Lille": "#E0A32E",             # or
    "RC Lens": "#4F7942",                # olive
    "Stade Rennais FC": "#E8385A",       # rouge Rennes
    "OGC Nice": "#17706B",               # teal
    "RC Strasbourg Alsace": "#8A6A3B",   # brun doré
    "FC Nantes": "#2F4858",              # ardoise
}

W, H, DPI = 10.8, 13.5, 100
plt.rcParams.update({"font.family": "DejaVu Sans", "pdf.fonttype": 42})
MONO = "DejaVu Sans Mono"

FEATS = json.load(open(os.path.join(ASSETS, "regions.geojson")))["features"]
CLASS = {code: cls for _, code, cls in REGIONS}


def T(ax, x, y, s, size=12, color=INK, weight="normal", ha="left", va="baseline",
      family="DejaVu Sans", spacing=1.0, style="normal", alpha=1.0):
    return ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va,
                   family=family, linespacing=spacing, style=style, alpha=alpha,
                   transform=ax.transAxes)


def draw_france(ax, rect):
    axm = ax.inset_axes(rect)
    axm.set_facecolor("none")
    axm.axis("off")

    for f in FEATS:
        code = f["properties"]["code"]
        geom = f["geometry"]
        # deux tons seulement : IDF plus dense, reste beige clair
        fc = PANEL2 if code == "11" else PANEL
        polys = [geom["coordinates"][0]] if geom["type"] == "Polygon" else [p[0] for p in geom["coordinates"]]
        for ring in polys:
            axm.add_patch(MPoly(ring, closed=True, fc=fc, ec="#FBF7EC", lw=1.5, zorder=2))

    axm.set_xlim(-5.35, 10.15)
    axm.set_ylim(41.2, 51.2)
    axm.set_aspect(1.0 / math.cos(math.radians(46.5)), adjustable="box")

    lab = {
        "Olympique Lyonnais": (-0.34, -0.34, "right", "OL"),
        "AS Monaco": (0.46, -0.30, "left", "ASM"),
        "Olympique de Marseille": (0.30, -0.46, "left", "OM"),
        "Toulouse FC": (0.34, -0.05, "left", "TFC"),
        "Stade de Reims": (0.34, 0.22, "left", "SDR"),
        "Paris Saint-Germain": (-0.32, -0.44, "right", "PSG"),
        "LOSC Lille": (0.34, 0.36, "left", "LOSC"),
        "RC Lens": (-0.34, -0.06, "right", "RCL"),
        "Stade Rennais FC": (-0.34, -0.10, "right", "SRFC"),
        "OGC Nice": (-0.38, 0.66, "right", "OGC NICE"),
        "RC Strasbourg Alsace": (0.36, 0.22, "left", "RCSA"),
        "FC Nantes": (-0.34, -0.32, "right", "FCN"),
    }

    for c in CLUBS:
        col = CLUB_COLOR[c["club"]]
        x, y = c["lon"], c["lat"]
        axm.add_patch(Circle((x, y), .58, fc=col, ec="none", alpha=.14, zorder=5))
        axm.add_patch(Circle((x, y), .30, fc=col, ec="#FBF7EC", lw=1.6, zorder=6))

        dx, dy, ha, short = lab.get(c["club"], (0.3, 0.2, "left", c["short"]))
        axm.text(x + dx, y + dy, short, fontsize=7.8, color=INK, ha=ha, va="center",
                 fontweight="bold", zorder=8,
                 path_effects=[pe.withStroke(linewidth=2.8, foreground="#FBF7EC")])
    return axm


def build():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # bandeau de tête, comme la carte source
    ax.add_patch(Rectangle((0, 0.958), 1, 0.042, fc=GREEN, ec="none"))
    T(ax, 0.045, 0.9725, "NOTE DE RECHERCHE  ·  ORBIS 20/10/2026  ·  MISE EN FORME PERSONNELLE",
      size=8.0, color="#BFDCCB", weight="bold", va="center", family=MONO)
    T(ax, 0.955, 0.9725, "C. MINANG  ·  1/1", size=8.0, color=PAPER,
      weight="bold", ha="right", va="center", family=MONO)

    # titre
    T(ax, 0.048, 0.918, "QUI PAIE EN DEVISE\nDANS LE FOOT FRANÇAIS", size=32, color=INK,
      weight="bold", va="top", spacing=1.05)
    T(ax, 0.048, 0.842,
      "12 clubs de Ligue 1. 5 ont annoncé un partenaire FX, 7 n'en ont aucun.\nUne couleur par club — le reste est agrégé.",
      size=11.0, color=MUTED, va="top", spacing=1.5)

    # carte
    draw_france(ax, [0.020, 0.338, 0.960, 0.470])

    # ---------------- légende : une ligne par club, deux groupes
    ax.plot([0.048, 0.955], [0.322, 0.322], color=GREEN, lw=1.0, alpha=.45,
            transform=ax.transAxes)
    T(ax, 0.048, 0.310, "COUVERTS  ·  5", size=8.4, color=GREEN, weight="bold", family=MONO)
    T(ax, 0.512, 0.310, "EXPOSÉS  ·  7", size=8.4, color=AMBER, weight="bold", family=MONO)
    T(ax, 0.955, 0.310, "PARTENAIRE FX ANNONCÉ", size=8.0, color=MUTED,
      ha="right", family=MONO, style="italic")

    covered = [c for c in CLUBS if c["partners"]]
    exposed = [c for c in CLUBS if not c["partners"]]
    covered.sort(key=lambda c: c["short"])
    exposed.sort(key=lambda c: c["short"])

    def row(c, cx, cy, show_partner=True):
        col = CLUB_COLOR[c["club"]]
        ax.add_patch(Circle((cx + 0.007, cy + 0.005), 0.0072, fc=col, ec="none",
                            transform=ax.transAxes, zorder=9))
        T(ax, cx + 0.023, cy, c["short"], size=8.8, color=INK, weight="bold",
          family=MONO, va="center")
        T(ax, cx + 0.070, cy, c["club"], size=8.8, color=INK, va="center")
        if not show_partner:
            return
        if c["partners"]:
            names = " · ".join(dict.fromkeys(
                "Corpay" if p["fintech"].startswith("Corpay") else p["fintech"] for p in c["partners"]))
            T(ax, cx + 0.300, cy, names, size=8.8, color=GREEN, weight="bold", va="center")

    y0 = 0.286
    for i, c in enumerate(covered):
        row(c, 0.048, y0 - i * 0.0335)
    for i, c in enumerate(exposed):
        row(c, 0.512, y0 - i * 0.0232, show_partner=False)

    # ---------------- bandeau chiffres
    stats = [
        ("1,7 Md£", "dépensés par la Premier League\nen joueurs de la zone euro"),
        ("22 M£", "de change caché sur un seul\nmercato (étude Glyde, 2026)"),
        ("7 / 12", "clubs sans partenaire FX\nannoncé à ce jour"),
    ]
    w = 0.288
    for i, (big, small) in enumerate(stats):
        x = 0.048 + i * (w + 0.0215)
        ax.add_patch(FancyBboxPatch((x, 0.052), w, 0.062,
                                    boxstyle="round,pad=0,rounding_size=0.006",
                                    fc=PANEL, ec=LINE, lw=1.0, transform=ax.transAxes))
        T(ax, x + 0.018, 0.092, big, size=17, color=GREEN if i < 2 else AMBER,
          weight="bold", va="center")
        T(ax, x + 0.018, 0.074, small, size=7.2, color=MUTED, va="top", spacing=1.4)

    # ---------------- pied
    T(ax, 0.048, 0.034,
      "Sources : communiqués des clubs et des fintechs (2021-2026) · Orbis 20/10/2026 · INSEE · The Fintech Times / Finance Magnates (étude Glyde).",
      size=6.6, color=MUTED)
    T(ax, 0.048, 0.021,
      "Entreprises agrégées : aucun nom, aucune commune, aucun montant individuel publié. Les clubs sont nommés uniquement sur annonce publique. Étude personnelle hors mission.",
      size=6.6, color=MUTED)

    out = os.path.join(ASSETS, "06-post-carte-clubs.png")
    fig.savefig(out, dpi=DPI, facecolor=PAPER)
    print("ok", out)
    return fig


if __name__ == "__main__":
    build()
