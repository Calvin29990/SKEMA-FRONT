#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Carte seule, plein cadre, façon sortie Python / Excel :
- régions colorées selon la densité de sièges (palette de la carte source : verts + ambre)
- logos des clubs posés à même la carte, sans pastille ni contour
- aucun titre, aucune légende, aucun encadré
- une seule ligne de sources en bas

Sortie : assets/09-carte-plein-ecran.png (1080 x 1080)
"""
import json
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Polygon as MPoly

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_map import REGIONS  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
LOGOS = os.path.join(ASSETS, "logos")

BG = "#FFFFFF"
EDGE = "#FFFFFF"
TXT = "#5A5A5A"

# palette reprise de la carte d'origine : verts pour le cœur, ambre/beige pour le Grand Sud
DENS = {
    4: "#1D6B4C",
    3: "#3E8F65",
    2: "#7FB894",
    1: "#C5DCC7",
    0: "#E8EFD9",
}
# régions du Grand Sud traitées en ambre, comme sur la carte de départ
AMBRE = {"75", "76", "93"}
AMBRE_TONES = {4: "#C8912F", 3: "#D9A94F", 2: "#E7C588", 1: "#F0DCB4", 0: "#F6EBD3"}

# position de collage (lon, lat) du CENTRE du logo — posée à la main pour rester sur le territoire
CLUBS = [
    ("psg",  1.95, 49.02),
    ("pfc",  3.32, 48.42),
    ("losc", 3.55, 50.72),
    ("rcl",  2.45, 50.15),
    ("sdr",  4.55, 49.32),
    ("rcsa", 7.35, 48.95),
    ("srfc", -1.75, 48.25),
    ("ol",   5.20, 45.90),
    ("tfc",  1.75, 44.05),
    ("om",   5.05, 43.62),
    ("ogcn", 6.72, 44.18),
    ("asm",  7.25, 43.32),
]

FEATS = json.load(open(os.path.join(ASSETS, "regions.geojson")))["features"]
CLASS = {code: cls for _, code, cls in REGIONS}

W, H, DPI = 10.8, 10.8, 100
plt.rcParams.update({"font.family": "DejaVu Sans"})


def build():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    fig.patch.set_facecolor(BG)

    # la carte occupe tout, sauf une bande de 4 % en bas pour les sources
    ax = fig.add_axes([0.0, 0.055, 1.0, 0.945])
    ax.set_facecolor(BG)
    ax.axis("off")

    for f in FEATS:
        code = f["properties"]["code"]
        cls = CLASS.get(code, 0)
        fc = (AMBRE_TONES if code in AMBRE else DENS)[cls]
        geom = f["geometry"]
        polys = [geom["coordinates"][0]] if geom["type"] == "Polygon" else [p[0] for p in geom["coordinates"]]
        for ring in polys:
            ax.add_patch(MPoly(ring, closed=True, fc=fc, ec=EDGE, lw=2.2, zorder=2))

    ax.set_xlim(-5.25, 9.75)
    ax.set_ylim(41.55, 51.15)
    ax.set_aspect(1.0 / math.cos(math.radians(46.5)), adjustable="datalim")

    # logos posés à même la carte
    for slug, x, y in CLUBS:
        p = os.path.join(LOGOS, slug + ".png")
        if not os.path.exists(p):
            continue
        img = mpimg.imread(p)
        h, w = img.shape[0], img.shape[1]
        s = 0.86                      # hauteur du logo, en degrés de latitude
        ww = s * w / max(w, h)
        hh = s * h / max(w, h)
        ax.imshow(img, extent=(x - ww / 2, x + ww / 2, y - hh / 2, y + hh / 2),
                  zorder=6, interpolation="lanczos", aspect="auto")

    fig.text(0.012, 0.020,
             "Source : Orbis (Bureau van Dijk) 20/10/2026 · géolocalisation INSEE · sites des clubs et des fintechs",
             fontsize=6.6, color=TXT, ha="left", va="center")

    out = os.path.join(ASSETS, "09-carte-plein-ecran.png")
    fig.savefig(out, dpi=DPI, facecolor=BG)
    print("ok", out)
    return out


if __name__ == "__main__":
    build()
