#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuel « comité de direction » — carte + logos officiels.
Titre court, un chiffre qui saute aux yeux, carte à gauche, tableau à droite.
Sortie : assets/08-post-carte-comex.png
"""
import json
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patheffects as pe
from matplotlib.patches import Polygon as MPoly, Rectangle, FancyBboxPatch, Circle

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_map import CLUBS, REGIONS  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
LOGOS = os.path.join(ASSETS, "logos")

PAPER = "#F7F2E4"
PANEL = "#EFE8D6"
PANEL2 = "#E5DCC4"
INK = "#12301F"
GREEN = "#1D6B4C"
AMBER = "#C8912F"
MUTED = "#6E7268"
LINE = "#D8CFB6"
RED = "#B24A3C"

CLUB_COLOR = {
    "Olympique Lyonnais": "#0072B2", "AS Monaco": "#D55E00",
    "Olympique de Marseille": "#3E9FD6", "Toulouse FC": "#6A4C93",
    "Stade de Reims": "#009E73", "Paris Saint-Germain": "#8C2F39",
    "LOSC Lille": "#E0A32E", "RC Lens": "#4F7942",
    "Stade Rennais FC": "#E8385A", "OGC Nice": "#17706B",
    "RC Strasbourg Alsace": "#8A6A3B", "Paris FC": "#2F4858",
}
SLUG = {
    "Olympique Lyonnais": "ol", "AS Monaco": "asm", "Olympique de Marseille": "om",
    "Toulouse FC": "tfc", "Stade de Reims": "sdr", "Paris Saint-Germain": "psg",
    "LOSC Lille": "losc", "RC Lens": "rcl", "Stade Rennais FC": "srfc",
    "OGC Nice": "ogcn", "RC Strasbourg Alsace": "rcsa", "Paris FC": "pfc",
}
SOLDE = {
    "Paris Saint-Germain": "+182,3", "LOSC Lille": "+120,4", "RC Strasbourg Alsace": "+101,5",
    "AS Monaco": "+56,0", "Olympique de Marseille": "+49,9", "RC Lens": "+46,7",
    "Olympique Lyonnais": "+44,0", "Stade Rennais FC": "+33,7", "Toulouse FC": "+25,5",
    "OGC Nice": "+14,9", "Paris FC": "-72,2", "Stade de Reims": "n.d.",
}
PROVIDER = {}
for _c in CLUBS:
    if _c["partners"]:
        PROVIDER[_c["club"]] = " · ".join(dict.fromkeys(
            "Corpay" if p["fintech"].startswith("Corpay") else p["fintech"] for p in _c["partners"]))

W, H, DPI = 10.8, 13.5, 100
plt.rcParams.update({"font.family": "DejaVu Sans", "pdf.fonttype": 42})

FEATS = json.load(open(os.path.join(ASSETS, "regions.geojson")))["features"]


def T(ax, x, y, s, size=12, color=INK, weight="normal", ha="left", va="baseline",
      spacing=1.0, style="normal", alpha=1.0):
    return ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va,
                   linespacing=spacing, style=style, alpha=alpha, transform=ax.transAxes)


def put_logo(ax, x, y, size, club, circle=False, lw=1.6):
    """Colle le logo (carré de côté `size`, en fraction d'axes) centré en (x,y)."""
    lg = os.path.join(LOGOS, SLUG[club] + ".png")
    if not os.path.exists(lg):
        return False
    img = mpimg.imread(lg)
    h, w = img.shape[0], img.shape[1]
    s = size
    ww, hh = s * w / max(w, h), s * h / max(w, h)
    if circle:
        ax.add_patch(Circle((x, y), size * 0.78, fc="#FDFBF4",
                            ec=CLUB_COLOR[club], lw=lw, transform=ax.transAxes, zorder=6))
    ax.imshow(img, extent=(x - ww / 2, x + ww / 2, y - hh / 2, y + hh / 2),
              transform=ax.transAxes, zorder=7, aspect="auto", interpolation="lanczos")
    return True


def draw_france(ax, rect):
    axm = ax.inset_axes(rect)
    axm.set_facecolor("none")
    axm.axis("off")
    for f in FEATS:
        code = f["properties"]["code"]
        geom = f["geometry"]
        fc = PANEL2 if code == "11" else PANEL
        polys = [geom["coordinates"][0]] if geom["type"] == "Polygon" else [p[0] for p in geom["coordinates"]]
        for ring in polys:
            axm.add_patch(MPoly(ring, closed=True, fc=fc, ec="#FBF7EC", lw=1.6, zorder=2))
    axm.set_xlim(-5.35, 10.15)
    axm.set_ylim(41.2, 51.2)
    axm.set_aspect(1.0 / math.cos(math.radians(46.5)), adjustable="box")

    NUDGE = {
        "RC Lens": (-0.42, -0.30), "LOSC Lille": (0.34, 0.38),
        "OGC Nice": (-0.46, -0.26), "AS Monaco": (0.66, 0.22),
        "Paris FC": (0.95, -0.05), "Paris Saint-Germain": (-0.30, -0.34),
        "Stade de Reims": (0.40, 0.28), "Olympique de Marseille": (0.10, -0.30),
    }
    r = 0.44
    for c in CLUBS:
        dx, dy = NUDGE.get(c["club"], (0.0, 0.0))
        x, y = c["lon"] + dx, c["lat"] + dy
        col = CLUB_COLOR[c["club"]]
        axm.add_patch(Circle((x, y), r * 1.35, fc=col, ec="none", alpha=.13, zorder=5))
        axm.add_patch(Circle((x, y), r, fc="#FDFBF4", ec=col, lw=2.0, zorder=6))
        lg = os.path.join(LOGOS, SLUG[c["club"]] + ".png")
        if os.path.exists(lg):
            img = mpimg.imread(lg)
            hh, ww = img.shape[0], img.shape[1]
            s = r * 1.28
            axm.imshow(img,
                       extent=(x - s * ww / max(ww, hh) / 2, x + s * ww / max(ww, hh) / 2,
                               y - s * hh / max(ww, hh) / 2, y + s * hh / max(ww, hh) / 2),
                       zorder=7, interpolation="lanczos", aspect="auto")
    return axm


def build():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # bandeau
    ax.add_patch(Rectangle((0, 0.966), 1, 0.034, fc=GREEN, ec="none"))
    T(ax, 0.038, 0.9775, "NOTE DE RECHERCHE  ·  ORBIS 20/10/2026", size=7.4,
      color="#BFDCCB", weight="bold", va="center")
    T(ax, 0.962, 0.9775, "C. MINANG", size=7.4, color=PAPER, weight="bold",
      ha="right", va="center")

    # titre
    T(ax, 0.038, 0.938, "LE CHANGE CACHÉ\nDU FOOT FRANÇAIS", size=30, color=INK,
      weight="bold", va="top", spacing=1.04)

    # le chiffre qui saute aux yeux
    T(ax, 0.038, 0.838, "14", size=46, color=RED, weight="bold", va="top")
    T(ax, 0.146, 0.826,
      "clubs de Ligue 1 sur 18 n'ont annoncé\naucun partenaire FX",
      size=10.4, color=INK, weight="bold", va="top", spacing=1.45)

    # carte — moitié gauche
    draw_france(ax, [0.005, 0.240, 0.600, 0.520])

    # mini légende « qui couvre qui » sous la carte
    T(ax, 0.040, 0.212, "QUI COUVRE QUI", size=7.4, color=GREEN, weight="bold")
    ax.plot([0.040, 0.560], [0.204, 0.204], color=GREEN, lw=1.0, alpha=.4, transform=ax.transAxes)
    prov = [("Ebury", "4 clubs", "OL · ASM · OM · Reims"),
            ("Corpay", "1 club", "Toulouse"),
            ("Sokin", "1 club", "AS Monaco (2021-24)")]
    yy = 0.190
    for name, cnt, clubs in prov:
        T(ax, 0.040, yy, name, size=9.2, color=INK, weight="bold", va="center")
        T(ax, 0.140, yy, cnt, size=8.4, color=GREEN, weight="bold", va="center")
        T(ax, 0.196, yy, clubs, size=8.4, color=MUTED, va="center")
        yy -= 0.0180


    # ---------------- panneau droit : le tableau
    px0, px1 = 0.600, 0.966
    ax.plot([px0, px1], [0.782, 0.782], color=GREEN, lw=1.2, alpha=.55, transform=ax.transAxes)
    T(ax, px0, 0.792, "18 CLUBS DE LIGUE 1  ·  PARTENAIRE FX  ·  SOLDE MERCATO", size=7.0,
      color=GREEN, weight="bold")

    def key(c):
        v = SOLDE[c["club"]]
        return float(v.replace("+", "").replace(",", ".")) if v[0] in "+-" else 0.0

    covered = sorted([c for c in CLUBS if c["partners"]], key=key, reverse=True)
    exposed = sorted([c for c in CLUBS if not c["partners"]], key=key, reverse=True)
    ordered = covered + exposed

    y = 0.756
    step = 0.0372
    for i, c in enumerate(ordered):
        if i == len(covered):
            ax.plot([px0, px1], [y + step * 0.58, y + step * 0.58], color=LINE, lw=1.0,
                    transform=ax.transAxes)
        is_cov = bool(c["partners"])
        put_logo(ax, px0 + 0.017, y - 0.004, 0.026, c["club"])

        T(ax, px0 + 0.040, y + 0.004, c["club"] + ("  (L2)" if c["league"] == "Ligue 2" else ""),
          size=8.6, color=INK, weight="bold", va="center")

        if is_cov:
            T(ax, px0 + 0.040, y - 0.011, PROVIDER[c["club"]], size=7.8, color=GREEN,
              weight="bold", va="center")
        else:
            T(ax, px0 + 0.040, y - 0.011, "aucun partenaire annoncé", size=7.8,
              color="#A79878", style="italic", va="center")

        solde = SOLDE[c["club"]] + ("" if SOLDE[c["club"]] == "n.d." else " M€")
        T(ax, px1, y + 0.004, solde, size=8.6, color=INK, weight="bold", ha="right", va="center")
        T(ax, px1, y - 0.011, "couvert" if is_cov else "exposé", size=7.2,
          color=GREEN if is_cov else RED, weight="bold", ha="right", va="center")
        y -= step

    # ---------------- bandeau chiffres
    stats = [
        ("1,33 Md€", "de ventes de joueurs en Ligue 1 cet été — un record"),
        ("4 / 18", "clubs avec un partenaire FX annoncé"),
        ("22 M£", "de change caché sur les seuls transferts européens (2026)"),
    ]
    w = 0.296
    for i, (big, small) in enumerate(stats):
        x = 0.035 + i * (w + 0.0185)
        ax.add_patch(FancyBboxPatch((x, 0.058), w, 0.062,
                                    boxstyle="round,pad=0,rounding_size=0.006",
                                    fc=PANEL, ec=LINE, lw=1.0, transform=ax.transAxes))
        T(ax, x + 0.016, 0.100, big, size=14, color=GREEN, weight="bold", va="center")
        T(ax, x + 0.016, 0.084, small, size=6.6, color=MUTED, va="top", spacing=1.4)

    T(ax, 0.038, 0.036,
      "Soldes mercato : Transfermarkt au 02/09/2026 (via Sportune / 20 Minutes). Partenaires FX : communiqués des clubs et des fintechs, 2021-2026.",
      size=6.2, color=MUTED)
    T(ax, 0.038, 0.023,
      "Entreprises agrégées : aucun nom, aucun montant individuel publié. Étude personnelle hors mission, aucune donnée client.",
      size=6.2, color=MUTED)

    out = os.path.join(ASSETS, "08-post-carte-comex.png")
    fig.savefig(out, dpi=DPI, facecolor=PAPER)
    print("ok", out)
    return fig


if __name__ == "__main__":
    build()
