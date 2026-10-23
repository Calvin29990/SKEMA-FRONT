#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuel LinkedIn v3 — palette de la carte source, badges de club sur la carte
(logo officiel si déposé dans assets/logos/<slug>.png, sinon monogramme aux
couleurs du club), partenaire FX et solde mercato été 2026.

Sortie : assets/07-post-carte-clubs.png
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
from matplotlib.patches import Polygon as MPoly, Rectangle, FancyBboxPatch, Circle, FancyArrow

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_map import CLUBS, REGIONS  # noqa: E402

ASSETS = os.path.join(HERE, "assets")
LOGOS = os.path.join(ASSETS, "logos")

# ---------------------------------------------------------------- palette carte source
PAPER = "#F7F2E4"
PANEL = "#EFE8D6"
PANEL2 = "#E5DCC4"
INK = "#12301F"
GREEN = "#1D6B4C"
AMBER = "#C8912F"
MUTED = "#6E7268"
LINE = "#D8CFB6"

CLUB_COLOR = {
    "Olympique Lyonnais": "#0072B2",
    "AS Monaco": "#D55E00",
    "Olympique de Marseille": "#3E9FD6",
    "Toulouse FC": "#6A4C93",
    "Stade de Reims": "#009E73",
    "Paris Saint-Germain": "#8C2F39",
    "LOSC Lille": "#E0A32E",
    "RC Lens": "#4F7942",
    "Stade Rennais FC": "#E8385A",
    "OGC Nice": "#17706B",
    "RC Strasbourg Alsace": "#8A6A3B",
    "Paris FC": "#2F4858",
}

SLUG = {
    "Olympique Lyonnais": "ol",
    "AS Monaco": "asm",
    "Olympique de Marseille": "om",
    "Toulouse FC": "tfc",
    "Stade de Reims": "sdr",
    "Paris Saint-Germain": "psg",
    "LOSC Lille": "losc",
    "RC Lens": "rcl",
    "Stade Rennais FC": "srfc",
    "OGC Nice": "ogcn",
    "RC Strasbourg Alsace": "rcsa",
    "Paris FC": "pfc",
}

MONO = {
    "Olympique Lyonnais": "OL",
    "AS Monaco": "ASM",
    "Olympique de Marseille": "OM",
    "Toulouse FC": "TFC",
    "Stade de Reims": "SDR",
    "Paris Saint-Germain": "PSG",
    "LOSC Lille": "LOSC",
    "RC Lens": "RCL",
    "Stade Rennais FC": "SRFC",
    "OGC Nice": "OGCN",
    "RC Strasbourg Alsace": "RCSA",
    "Paris FC": "PFC",
}

# solde mercato été 2026, M€ — Transfermarkt, via Sportune / 20 Minutes (02/09/2026)
SOLDE = {
    "Paris Saint-Germain": "+182,3",
    "LOSC Lille": "+120,4",
    "RC Strasbourg Alsace": "+101,5",
    "AS Monaco": "+56,0",
    "Olympique de Marseille": "+49,9",
    "RC Lens": "+46,7",
    "Olympique Lyonnais": "+44,0",
    "Stade Rennais FC": "+33,7",
    "Toulouse FC": "+25,5",
    "OGC Nice": "+14,9",
    "Paris FC": "-72,2",
    "Stade de Reims": "n.d.",
}

PROVIDER = {}
for _c in CLUBS:
    if _c["partners"]:
        names = list(dict.fromkeys(
            "Corpay" if p["fintech"].startswith("Corpay") else p["fintech"] for p in _c["partners"]))
        PROVIDER[_c["club"]] = " · ".join(names)

W, H, DPI = 10.8, 13.5, 100
plt.rcParams.update({"font.family": "DejaVu Sans", "pdf.fonttype": 42})

FEATS = json.load(open(os.path.join(ASSETS, "regions.geojson")))["features"]


def T(ax, x, y, s, size=12, color=INK, weight="normal", ha="left", va="baseline",
      family="DejaVu Sans", spacing=1.0, style="normal", alpha=1.0):
    return ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va,
                   family=family, linespacing=spacing, style=style, alpha=alpha,
                   transform=ax.transAxes)


# ---------------------------------------------------------------- badges
def logo_path(club):
    p = os.path.join(LOGOS, SLUG[club] + ".png")
    return p if os.path.exists(p) else None


def badge(axm, x, y, club, r=0.32):
    """Badge circulaire : logo si dispo, sinon monogramme aux couleurs du club."""
    col = CLUB_COLOR[club]
    axm.add_patch(Circle((x, y), r * 1.45, fc=col, ec="none", alpha=.13, zorder=5))
    axm.add_patch(Circle((x, y), r, fc="#FDFBF4", ec=col, lw=2.0, zorder=6))

    lg = logo_path(club)
    if lg:
        img = mpimg.imread(lg)
        h, w = img.shape[0], img.shape[1]
        s = r * 1.34
        axm.imshow(img, extent=(x - s * w / max(w, h) / 2, x + s * w / max(w, h) / 2,
                                y - s * h / max(w, h) / 2, y + s * h / max(w, h) / 2),
                   zorder=7, interpolation="lanczos")
    else:
        axm.text(x, y, MONO[club], fontsize=5.8 if len(MONO[club]) > 3 else 6.6, color=col, ha="center", va="center",
                 fontweight="bold", zorder=7, family="DejaVu Sans")


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
            axm.add_patch(MPoly(ring, closed=True, fc=fc, ec="#FBF7EC", lw=1.5, zorder=2))

    axm.set_xlim(-5.35, 10.15)
    axm.set_ylim(41.2, 51.2)
    axm.set_aspect(1.0 / math.cos(math.radians(46.5)), adjustable="box")

    # nudge d'affichage uniquement (les coordonnées réelles restent dans les données)
    NUDGE = {
        "RC Lens": (-0.30, -0.26),
        "LOSC Lille": (0.26, 0.30),
        "OGC Nice": (-0.34, -0.20),
        "AS Monaco": (0.46, 0.16),
        "Paris FC": (1.55, -0.05),
        "Paris Saint-Germain": (-0.40, -0.18),
    }

    for c in CLUBS:
        dx, dy = NUDGE.get(c["club"], (0.0, 0.0))
        x, y = c["lon"] + dx, c["lat"] + dy
        badge(axm, x, y, c["club"], r=.32)
    return axm


def build():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.add_patch(Rectangle((0, 0.962), 1, 0.038, fc=GREEN, ec="none"))
    T(ax, 0.045, 0.9745, "NOTE DE RECHERCHE  ·  ORBIS 20/10/2026  ·  MISE EN FORME PERSONNELLE",
      size=7.6, color="#BFDCCB", weight="bold", va="center")
    T(ax, 0.955, 0.9745, "C. MINANG  ·  1/1", size=7.6, color=PAPER,
      weight="bold", ha="right", va="center")

    T(ax, 0.048, 0.926, "QUI PAIE EN DEVISE\nDANS LE FOOT FRANÇAIS", size=31, color=INK,
      weight="bold", va="top", spacing=1.05)
    T(ax, 0.048, 0.860,
      "12 clubs passés au crible : 5 ont annoncé un partenaire FX, 7 n'en ont aucun.\n"
      "Solde mercato été 2026 en regard — c'est le volume exposé au change.",
      size=10.2, color=MUTED, va="top", spacing=1.55)

    draw_france(ax, [0.020, 0.392, 0.960, 0.398])

    # ---------------- tableau
    top = 0.356
    ax.plot([0.048, 0.955], [top + 0.014, top + 0.014], color=GREEN, lw=1.0, alpha=.5,
            transform=ax.transAxes)
    T(ax, 0.050, top, "CLUB", size=7.6, color=GREEN, weight="bold")
    T(ax, 0.300, top, "PARTENAIRE FX", size=7.6, color=GREEN, weight="bold")
    T(ax, 0.640, top, "SOLDE MERCATO 2026", size=7.6, color=GREEN, weight="bold")
    T(ax, 0.955, top, "STATUT", size=7.6, color=GREEN, weight="bold", ha="right")

    covered = sorted([c for c in CLUBS if c["partners"]], key=lambda c: -float(SOLDE[c["club"]].replace("+", "").replace(",", ".")) if SOLDE[c["club"]][0] in "+-" else 0)
    exposed = sorted([c for c in CLUBS if not c["partners"]],
                     key=lambda c: float(SOLDE[c["club"]].replace("+", "").replace(",", ".")) if SOLDE[c["club"]][0] in "+-" else 0,
                     reverse=True)
    ordered = covered + exposed

    y = top - 0.028
    step = 0.0190
    for i, c in enumerate(ordered):
        col = CLUB_COLOR[c["club"]]
        is_cov = bool(c["partners"])
        if i == len(covered):
            # séparateur entre couverts et exposés
            ax.plot([0.048, 0.955], [y + step * 0.55, y + step * 0.55], color=LINE, lw=0.9,
                    transform=ax.transAxes)

        ax.add_patch(Circle((0.056, y + 0.004), 0.0062, fc=col, ec="none",
                            transform=ax.transAxes, zorder=9))
        T(ax, 0.070, y, MONO[c["club"]], size=8.0, color=INK, weight="bold", va="center")
        name = c["club"] + ("  (L2)" if c["league"] == "Ligue 2" else "")
        T(ax, 0.118, y, name, size=8.0, color=INK, va="center")

        if is_cov:
            T(ax, 0.300, y, PROVIDER[c["club"]], size=8.0, color=GREEN, weight="bold", va="center")
            T(ax, 0.640, y, SOLDE[c["club"]] + ("" if SOLDE[c["club"]] == "n.d." else " M€"), size=8.0, color=INK, va="center")
            T(ax, 0.955, y, "couvert", size=7.8, color=GREEN, weight="bold", va="center", ha="right")
        else:
            T(ax, 0.300, y, "aucun", size=8.0, color="#A79878", style="italic", va="center")
            T(ax, 0.640, y, SOLDE[c["club"]] + ("" if SOLDE[c["club"]] == "n.d." else " M€"), size=8.0, color=INK, va="center")
            T(ax, 0.955, y, "exposé", size=7.8, color=AMBER, weight="bold", va="center", ha="right")
        y -= step

    # ---------------- bandeau
    stats = [
        ("+1,33 Md€", "de ventes de joueurs en Ligue 1\ncet été (Transfermarkt)"),
        ("4 / 18", "clubs de Ligue 1 avec un\npartenaire FX annoncé"),
        ("22 M£", "de change caché sur les seuls\ntransferts européens (2026)"),
    ]
    w = 0.288
    for i, (big, small) in enumerate(stats):
        x = 0.048 + i * (w + 0.0215)
        ax.add_patch(FancyBboxPatch((x, 0.046), w, 0.056,
                                    boxstyle="round,pad=0,rounding_size=0.006",
                                    fc=PANEL, ec=LINE, lw=1.0, transform=ax.transAxes))
        T(ax, x + 0.018, 0.082, big, size=15, color=GREEN, weight="bold", va="center")
        T(ax, x + 0.018, 0.068, small, size=6.8, color=MUTED, va="top", spacing=1.4)

    T(ax, 0.048, 0.030,
      "Soldes mercato : Transfermarkt, relevés au 02/09/2026 (via Sportune / 20 Minutes). Partenaires FX : communiqués des clubs et des fintechs, 2021-2026.",
      size=6.4, color=MUTED)
    T(ax, 0.048, 0.018,
      "Entreprises agrégées : aucun nom, aucune commune, aucun montant individuel publié. Étude personnelle hors mission, aucune donnée client.",
      size=6.4, color=MUTED)

    out = os.path.join(ASSETS, "07-post-carte-clubs.png")
    fig.savefig(out, dpi=DPI, facecolor=PAPER)
    print("ok", out)
    return fig


if __name__ == "__main__":
    os.makedirs(LOGOS, exist_ok=True)
    build()
