#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Carte plein cadre, v2 :
- chaque région prend la couleur du club qui y joue (Paris bleu foncé, Marseille bleu ciel…)
- à côté de chaque logo : le montant (solde mercato 2026, en M€) et le partenaire FX
- ni titre, ni légende, ni encadré

Sortie : assets/10-carte-clubs-couleurs.png (1200 x 1200)
"""
import json
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patheffects as pe
from matplotlib.patches import Polygon as MPoly
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
LOGOS = os.path.join(ASSETS, "logos")

BG = "#FFFFFF"
TXT = "#4E4E4E"

# ---------------------------------------------------------------- couleur du territoire = couleur du club
REGION_FILL = {
    "11": "#0B1E4A",   # Paris — bleu nuit (PSG)
    "32": "#B01B33",   # Hauts-de-France — rouge LOSC
    "44": "#0E7FC0",   # Grand Est — bleu Strasbourg
    "53": "#BE2F3C",   # Bretagne — rouge Rennes
    "84": "#123A8B",   # Auvergne-Rhône-Alpes — bleu OL
    "76": "#5C4B9B",   # Occitanie — violet Toulouse
    "93": "#35A7DE",   # PACA — bleu ciel Marseille
}
PALE = "#EFF2E7"

# slug, lon, lat (centre logo), montant, partenaire, (x, y, ha) du bloc texte
CLUBS = [
    ("losc", 3.40, 50.62, "+120,4 M€", "aucun partenaire",   4.30, 50.80, "left"),
    ("rcl",  2.35, 50.18, "+46,7 M€",  "aucun partenaire",   1.30, 50.05, "right"),
    ("psg",  2.15, 48.85, "+182,3 M€", "aucun partenaire",   0.95, 48.86, "right"),
    ("pfc",  3.30, 48.42, "-72,2 M€",  "aucun partenaire",   4.30, 47.85, "left"),
    ("sdr",  4.70, 49.42, "n.d.",      "Ebury",              4.95, 49.88, "left"),
    ("rcsa", 7.20, 48.90, "+101,5 M€", "aucun partenaire",   7.00, 47.70, "left"),
    ("srfc", -1.90, 48.20, "+33,7 M€", "aucun partenaire",  -2.45, 47.75, "right"),
    ("ol",   5.20, 45.90, "+44,0 M€",  "Ebury",              6.60, 46.45, "left"),
    ("tfc",  1.60, 43.90, "+25,5 M€",  "Corpay",             2.75, 44.05, "left"),
    ("om",   5.15, 43.55, "+49,9 M€",  "Ebury",              4.45, 43.10, "right"),
    ("ogcn", 6.75, 44.30, "+14,9 M€",  "aucun partenaire",   7.55, 44.55, "left"),
    ("asm",  7.45, 43.40, "+56,0 M€",  "Ebury · Sokin",      8.30, 43.75, "left"),
]

FEATS = json.load(open(os.path.join(ASSETS, "regions.geojson")))["features"]

W, H, DPI = 12.0, 12.0, 100
plt.rcParams.update({"font.family": "DejaVu Sans"})


def build():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    fig.patch.set_facecolor(BG)

    ax = fig.add_axes([0.0, 0.045, 1.0, 0.955])
    ax.set_facecolor(BG)
    ax.axis("off")

    for f in FEATS:
        code = f["properties"]["code"]
        fc = REGION_FILL.get(code, PALE)
        geom = f["geometry"]
        polys = [geom["coordinates"][0]] if geom["type"] == "Polygon" else [p[0] for p in geom["coordinates"]]
        for ring in polys:
            ax.add_patch(MPoly(ring, closed=True, fc=fc, ec="#FFFFFF", lw=2.6, zorder=2))

    ax.set_xlim(-5.6, 10.2)
    ax.set_ylim(41.2, 51.4)
    ax.set_aspect(1.0 / math.cos(math.radians(46.5)), adjustable="box")

    for slug, x, y, amount, partner, tx, ty, ha in CLUBS:
        p = os.path.join(LOGOS, slug + ".png")
        if os.path.exists(p):
            img = mpimg.imread(p)
            h, w = img.shape[0], img.shape[1]
            sz = 0.92
            ww, hh = sz * w / max(w, h), sz * h / max(w, h)
            ax.imshow(img, extent=(x - ww / 2, x + ww / 2, y - hh / 2, y + hh / 2),
                      zorder=6, interpolation="lanczos", aspect="auto")

        covered = "aucun" not in partner
        halo = [pe.withStroke(linewidth=3.0, foreground="#FFFFFF")]

        ax.text(tx, ty + 0.16, amount, fontsize=13.0, color="#0E2A3A", fontweight="bold",
                ha=ha, va="center", zorder=8, path_effects=halo)
        ax.text(tx, ty - 0.16, partner, fontsize=8.8,
                color="#12624A" if covered else "#7C7C7C",
                fontweight="bold" if covered else "normal",
                style="normal" if covered else "italic",
                ha=ha, va="center", zorder=8, path_effects=halo)

    fig.text(0.010, 0.017,
             "Source : Orbis (Bureau van Dijk) 20/10/2026 · INSEE · sites des clubs et des fintechs · "
             "montants = solde mercato été 2026 (Transfermarkt, 02/09/2026)",
             fontsize=6.6, color=TXT, ha="left", va="center")

    out = os.path.join(ASSETS, "10-carte-clubs-couleurs.png")
    fig.savefig(out, dpi=DPI, facecolor=BG)
    print("ok", out)


if __name__ == "__main__":
    build()
