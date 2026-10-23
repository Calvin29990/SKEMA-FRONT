#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuel unique LinkedIn : « Le change caché du foot français ».
Code couleur risK desk : vert = couvert (partenaire FX annoncé), rouge = exposé.
Sortie : assets/05-post-carte-FX.png  (1080 x 1350)
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
from build_map import CLUBS, REGIONS, CLASS_LABEL  # noqa: E402

ASSETS = os.path.join(HERE, "assets")

# ---------------------------------------------------------------- palette « desk »
BG = "#0A1310"          # presque noir, vert froid
PANEL = "#101C17"
GRID = "#1B2B24"
WHITE = "#F1F5F2"
MUTED = "#8CA096"
GREEN = "#00D68F"       # couvert
RED = "#FF4D5E"         # exposé
# densité : rampe bleu-gris neutre (ne concurrence pas le vert/rouge)
DENS = {0: "#18262E", 1: "#22363F", 2: "#2E4A57", 3: "#3E6475", 4: "#4E8093"}

W, H, DPI = 10.8, 13.5, 100
plt.rcParams.update({"font.family": "DejaVu Sans", "pdf.fonttype": 42})
MONO = "DejaVu Sans Mono"

FEATS = json.load(open(os.path.join(ASSETS, "regions.geojson")))["features"]
CLASS = {c: k for _, c, k in REGIONS}
NAMES = {c: n for n, c, _ in REGIONS}


def T(ax, x, y, s, size=12, color=WHITE, weight="normal", ha="left", va="baseline",
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
        cls = CLASS.get(code, 0)
        geom = f["geometry"]
        polys = [geom["coordinates"][0]] if geom["type"] == "Polygon" else [p[0] for p in geom["coordinates"]]
        for ring in polys:
            axm.add_patch(MPoly(ring, closed=True, fc=DENS[cls], ec=BG, lw=1.4, zorder=2))

    axm.set_xlim(-5.35, 10.15)
    axm.set_ylim(41.2, 51.2)
    axm.set_aspect(1.0 / math.cos(math.radians(46.5)), adjustable="box")

    # clubs
    lab = {
        "Olympique Lyonnais": (-0.34, -0.34, "right", "OL"),
        "AS Monaco": (0.46, -0.30, "left", "ASM"),
        "Olympique de Marseille": (0.30, -0.46, "left", "OM"),
        "Toulouse FC": (0.34, -0.05, "left", "TFC"),
        "Stade de Reims": (0.34, 0.22, "left", "SDR"),
        "Paris Saint-Germain": (-0.32, -0.42, "right", "PSG"),
        "LOSC Lille": (0.34, 0.34, "left", "LOSC"),
        "RC Lens": (-0.34, -0.05, "right", "RCL"),
        "Stade Rennais FC": (-0.34, -0.08, "right", "SRFC"),
        "OGC Nice": (-0.34, 0.52, "right", "OGC NICE"),
        "RC Strasbourg Alsace": (0.36, 0.20, "left", "RCSA"),
        "FC Nantes": (-0.34, -0.30, "right", "FCN"),
    }
    for c in CLUBS:
        cov = len(c["partners"]) > 0
        col = GREEN if cov else RED
        x, y = c["lon"], c["lat"]
        # halo
        axm.add_patch(Circle((x, y), .40, fc=col, ec="none", alpha=.14, zorder=5))
        axm.add_patch(Circle((x, y), .21, fc=col, ec="#06100C" if cov else WHITE,
                             lw=1.4, zorder=6))
        if cov:
            axm.add_patch(Circle((x, y), .085, fc="#06100C", ec="none", zorder=7))

        dx, dy, ha, short = lab.get(c["club"], (0.3, 0.2, "left", c["short"]))
        axm.text(x + dx, y + dy, short, fontsize=7.6, color=WHITE, ha=ha, va="center",
                 fontweight="bold", zorder=8, family=MONO,
                 path_effects=[pe.withStroke(linewidth=2.6, foreground=BG)])
    return axm


def build():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # cadre fin
    ax.add_patch(Rectangle((0.018, 0.012), 0.964, 0.976, fc="none", ec="#22352C", lw=1.0))

    # bandeau haut
    ax.add_patch(Rectangle((0.018, 0.930), 0.964, 0.0035, fc=GREEN, ec="none"))
    T(ax, 0.045, 0.948, "RISK DESK  ·  FRANCE  ·  FX", size=8.4, color=GREEN,
      weight="bold", family=MONO, va="center")
    T(ax, 0.955, 0.948, "23.10.2026", size=8.4, color=MUTED, family=MONO,
      ha="right", va="center")

    # titre
    T(ax, 0.045, 0.900, "LE CHANGE CACHÉ", size=41, color=WHITE, weight="bold",
      va="top", spacing=1.02)
    T(ax, 0.045, 0.838, "DU FOOT FRANÇAIS", size=41, color=WHITE, weight="bold",
      va="top", spacing=1.02)

    # sous-titre
    T(ax, 0.048, 0.778,
      "12 clubs de Ligue 1 passés au crible.\n5 ont un partenaire FX annoncé. 7 n'en ont aucun.",
      size=12.5, color=MUTED, va="top", spacing=1.55)

    # carte
    draw_france(ax, [0.015, 0.240, 0.970, 0.492])

    # légende
    ly = 0.246
    ax.add_patch(Circle((0.058, ly + 0.006), 0.0075, fc=GREEN, ec="none",
                        transform=ax.transAxes, zorder=9))
    ax.add_patch(Circle((0.058, ly + 0.006), 0.0032, fc=BG, ec="none",
                        transform=ax.transAxes, zorder=10))
    T(ax, 0.076, ly, "COUVERT", size=9.2, color=GREEN, weight="bold", family=MONO, va="center")
    T(ax, 0.155, ly, "partenaire FX annoncé publiquement", size=8.6, color=MUTED, va="center")

    ax.add_patch(Circle((0.058, ly - 0.026), 0.0075, fc=RED, ec=WHITE, lw=1.2,
                        transform=ax.transAxes, zorder=9))
    T(ax, 0.076, ly - 0.026, "EXPOSÉ", size=9.2, color=RED, weight="bold", family=MONO, va="center")
    T(ax, 0.155, ly - 0.026, "aucune annonce publique trouvée", size=8.6, color=MUTED, va="center")

    T(ax, 0.955, ly - 0.001, "FOND : densité de sièges\npar région (Orbis, agrégé)",
      size=7.2, color="#63796E", ha="right", va="center", spacing=1.5)

    # bandeau de chiffres
    stats = [
        ("1,7 Md£", "dépensés par la Premier League\nen joueurs de la zone euro"),
        ("22 M£", "de change caché sur un\nseul mercato (étude 2026)"),
        ("7 / 12", "clubs français sans\npartenaire FX annoncé"),
    ]
    w = 0.288
    for i, (big, small) in enumerate(stats):
        x = 0.045 + i * (w + 0.022)
        ax.add_patch(FancyBboxPatch((x, 0.098), w, 0.098,
                                    boxstyle="round,pad=0,rounding_size=0.008",
                                    fc=PANEL, ec="#22352C", lw=1.0,
                                    transform=ax.transAxes))
        T(ax, x + 0.020, 0.164, big, size=24, color=GREEN if i < 2 else RED,
          weight="bold", family=MONO, va="top")
        T(ax, x + 0.020, 0.128, small, size=7.6, color=MUTED, va="top", spacing=1.5)

    # pied
    T(ax, 0.045, 0.068,
      "Ebury chez l'OL, Monaco, Marseille et Reims · Corpay chez Toulouse · Sokin chez Monaco",
      size=8.6, color=WHITE, weight="bold")
    T(ax, 0.045, 0.048,
      "Sources : communiqués des clubs et des fintechs (2021-2026) · Orbis 20/10/2026 · INSEE · étude Glyde / The Fintech Times (2026).",
      size=6.6, color="#63796E")
    T(ax, 0.045, 0.032,
      "Étude personnelle hors mission. Entreprises agrégées : aucun nom, aucune commune, aucun montant individuel publié. Les clubs sont nommés uniquement sur annonce publique.",
      size=6.6, color="#63796E")
    T(ax, 0.955, 0.032, "C. MINANG", size=7.2, color=MUTED, ha="right", family=MONO)

    out = os.path.join(ASSETS, "05-post-carte-FX.png")
    fig.savefig(out, dpi=DPI, facecolor=BG)
    print("ok", out)
    return fig


if __name__ == "__main__":
    build()
