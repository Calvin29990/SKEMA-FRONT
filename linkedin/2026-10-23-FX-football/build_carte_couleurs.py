#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Carte plein cadre, v3 (finitions) :
- montants +12 % (premier élément lu)
- régions légèrement désaturées (opacité 93 %) pour faire ressortir les logos
- halo blanc très léger autour des logos
- bloc [Montant] / [Partenaire FX] toujours au même offset relatif au logo
- « aucun partenaire FX identifié »
- vert des partenaires plus visible mais sobre
- ligne de sources plus contrastée + note discrète en bas à droite
- PSG / Paris FC décollés

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
TXT = "#3D3D3D"
TXT_SOFT = "#666666"

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
REGION_ALPHA = 0.93          # les logos ressortent mieux

# tokens
NO_PARTNER = "aucun partenaire FX identifié"
C_AMOUNT = "#0E2A3A"
C_PARTNER = "#0B7A4B"        # vert plus visible, reste sobre
C_NO = "#6E6E6E"

# Offsets uniformes du bloc texte, relatifs au centre du logo
DX = 0.88                    # distance horizontale logo -> texte
DY_AMOUNT = 0.175            # montant au-dessus du centre
DY_PARTNER = -0.175          # partenaire sous le centre
F_AMOUNT = 14.6              # +12 % par rapport à 13.0
F_PARTNER = 8.5

METHOD = [
    "Soldes de transferts : mercato été 2026 (Transfermarkt, compilations presse spécialisée).",
    "Partenariats FX : informations publiquement documentées à la date de référence.",
    "Cette carte constitue une photographie à un instant donné.",
]

# slug, lon, lat (centre logo), montant, partenaire, sens du texte (+1 droite / -1 gauche)
CLUBS = [
    ("losc",  3.58, 50.70, "+120,4 M€",  NO_PARTNER, +1),
    ("rcl",   2.35, 50.18, "+43,2 M€",   NO_PARTNER, -1),
    ("psg",   2.15, 48.85, "+182,3 M€",  NO_PARTNER, -1),
    ("pfc",   3.62, 48.08, "−72,2 M€",  NO_PARTNER, +1),
    ("rcsa",  7.02, 48.90, "≈ +100 M€", NO_PARTNER, +1),
    ("srfc", -1.90, 48.20, "≈ +60 M€",  NO_PARTNER, +1),
    ("ol",    5.20, 45.90, "≈ +42 M€",  "Ebury (2025/26)", +1),
    ("tfc",   1.60, 43.90, "+37,0 M€",   "Corpay",    -1),
    ("om",    5.15, 43.55, "+49,9 M€",   "Ebury (2025/26)", -1),
    ("ogcn",  6.75, 44.30, "≈ +45 M€",  NO_PARTNER, +1),
    ("asm",   7.30, 43.40, "+56,0 M€",   NO_PARTNER, +1),
]

FEATS = json.load(open(os.path.join(ASSETS, "regions.geojson")))["features"]

W, H, DPI = 12.0, 12.0, 100
AZ = 1.0 / math.cos(math.radians(46.5))   # correction de latitude de la projection
plt.rcParams.update({"font.family": "DejaVu Sans"})


# ---------------------------------------------------------------- halo blanc derrière un logo
def halo_image(img, px=3):
    """Renvoie un calque blanc dont l'alpha est le masque du logo dilaté."""
    rgb = img[..., :3]
    alpha = img[..., 3] if img.shape[-1] == 4 else np.ones(rgb.shape[:2])
    m = (alpha > 0.05).astype(np.float32)
    for _ in range(px):
        m = np.maximum.reduce([
            m,
            np.roll(m, 1, 0), np.roll(m, -1, 0),
            np.roll(m, 1, 1), np.roll(m, -1, 1),
        ])
    out = np.ones((m.shape[0], m.shape[1], 4), dtype=np.float32)
    out[..., 3] = m * 0.85
    return out


def build():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    fig.patch.set_facecolor(BG)

    ax = fig.add_axes([0.0, 0.072, 1.0, 0.928])
    ax.set_facecolor(BG)
    ax.axis("off")

    # ---- régions
    for f in FEATS:
        code = f["properties"]["code"]
        fc = REGION_FILL.get(code, PALE)
        geom = f["geometry"]
        polys = [geom["coordinates"][0]] if geom["type"] == "Polygon" else [p[0] for p in geom["coordinates"]]
        for ring in polys:
            ax.add_patch(MPoly(ring, closed=True, fc=fc, ec="#FFFFFF", lw=2.6,
                               alpha=REGION_ALPHA, zorder=2))

    ax.set_xlim(-5.6, 10.9)
    ax.set_ylim(41.2, 51.4)
    ax.set_aspect(AZ, adjustable="box")

    # ---- clubs
    for slug, x, y, amount, partner, direction in CLUBS:
        p = os.path.join(LOGOS, slug + ".png")
        if os.path.exists(p):
            img = mpimg.imread(p)
            h, w = img.shape[0], img.shape[1]
            sz = 1.02
            ww = sz * w / max(w, h)
            hh = sz * h / max(w, h) / AZ   # corrige l'aspect des degres (lat corrigee)
            ext = (x - ww / 2, x + ww / 2, y - hh / 2, y + hh / 2)
            # contour blanc très léger
            ax.imshow(halo_image(img), extent=ext, zorder=5,
                      interpolation="bilinear", aspect="auto")
            ax.imshow(img, extent=ext, zorder=6,
                      interpolation="lanczos", aspect="auto")

        ha = "left" if direction > 0 else "right"
        tx = x + direction * DX
        halo = [pe.withStroke(linewidth=3.2, foreground="#FFFFFF")]

        ax.text(tx, y + DY_AMOUNT, amount, fontsize=F_AMOUNT, color=C_AMOUNT,
                fontweight="bold", ha=ha, va="center", zorder=8, path_effects=halo)

        covered = partner != NO_PARTNER
        ax.text(tx, y + DY_PARTNER, partner, fontsize=F_PARTNER,
                color=C_PARTNER if covered else C_NO,
                fontweight="bold" if covered else "normal",
                style="normal" if covered else "italic",
                ha=ha, va="center", zorder=8, path_effects=halo)

    # ---- pied de page : methodologie + date d'arret
    for i, line in enumerate(METHOD):
        fig.text(0.010, 0.010 + (len(METHOD) - 1 - i) * 0.0198, line,
                 fontsize=7.0, color="#4A4A4A", ha="left", va="center")
    fig.text(0.990, 0.010, "Arrêté au 1er septembre 2026",
             fontsize=7.6, color="#4A4A4A", ha="right", va="center",
             style="italic")

    out = os.path.join(ASSETS, "10-carte-clubs-couleurs.png")
    fig.savefig(out, dpi=DPI, facecolor=BG)
    print("ok", out)


if __name__ == "__main__":
    build()
