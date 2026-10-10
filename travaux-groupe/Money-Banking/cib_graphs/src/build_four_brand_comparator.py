"""Build a four-brand France/Luxembourg comparator.

The chart keeps group-level and local-entity evidence in separate panels. It
must not be read as a league table between BNP CIB, CACIB and CACEIS.
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.collections import PatchCollection
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib.patches import FancyBboxPatch

from build_cib_graphs import (
    BNP, BNP_LIGHT, CACIB, CACIB_LIGHT, GOLD, GRID, INK, LAND, LAND_EDGE, MUTED, PAPER,
    europe_polygons,
)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
LOGOS = DATA / "logos"
OUT = ROOT / "output" / "four_brand_comparator"
OUT.mkdir(parents=True, exist_ok=True)

CACEIS = "#B4003A"
CACEIS_LIGHT = "#E6A0B5"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "text.color": INK,
    "figure.facecolor": PAPER,
    "savefig.facecolor": PAPER,
})


def load_signals():
    with (DATA / "four_brand_public_signals.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cropped_logo(filename):
    image = mpimg.imread(LOGOS / filename)
    if image.ndim == 2:
        image = np.dstack([image, image, image])
    # Crop white-background wordmarks (CACIB and CACEIS) so they do not look
    # like oversized white posters on the map. Keep BNP's black background.
    rgb = image[:, :, :3]
    if filename != "bnp-paribas.png":
        mask = np.any(rgb < 0.96, axis=2)
        ys, xs = np.where(mask)
        if len(xs):
            image = image[max(0, ys.min() - 8):ys.max() + 9,
                          max(0, xs.min() - 12):xs.max() + 13]
    return image


def add_logo(ax, filename, x, y, zoom=0.05, facecolor="white", edgecolor=GRID, frame=True, zorder=8):
    props = dict(boxstyle="round,pad=0.20", facecolor=facecolor, edgecolor=edgecolor, linewidth=0.7) if frame else None
    ab = AnnotationBbox(OffsetImage(cropped_logo(filename), zoom=zoom), (x, y),
                        frameon=frame, bboxprops=props, pad=0.18, zorder=zorder)
    ax.add_artist(ab)


def panel(ax, title, subtitle):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.015,rounding_size=0.025",
                                facecolor="white", edgecolor=GRID, linewidth=0.9, zorder=0))
    ax.text(0.04, 0.89, title, fontsize=10.2, weight="bold", color=INK, va="center")
    ax.text(0.04, 0.78, subtitle, fontsize=7.2, color=MUTED, va="center")


def bar(ax, y, value, maximum, color, label, value_label, logo_file, logo_face="white", logo_zoom=0.045):
    x0, x1 = 0.32, 0.95
    width = (x1 - x0) * value / maximum
    ax.add_patch(FancyBboxPatch((x0, y - 0.065), width, 0.13,
                                boxstyle="round,pad=0.004,rounding_size=0.018",
                                facecolor=color, edgecolor=color, linewidth=0, zorder=3))
    ax.text(0.045, y + 0.018, label, fontsize=8.0, weight="bold", color=INK, va="center")
    ax.text(x0 + width + 0.015, y, value_label, fontsize=9.1, weight="bold", color=color, va="center")
    # The logos are actual anchors, not decorative text labels.
    add_logo(ax, logo_file, 0.18, y, zoom=logo_zoom, facecolor=logo_face,
             edgecolor=logo_face if logo_face != "white" else GRID, frame=True, zorder=7)


def group_panel(fig, signals):
    ax = fig.add_axes([0.535, 0.535, 0.425, 0.29])
    panel(ax, "1  |  GROUP PLATFORM SCALE", "FY2025 published group signals · not France-only · same NBI unit")
    bnp_nbi = next(float(r["value"]) for r in signals if r["label"] == "BNP CIB France" and r["signal"] == "Net banking income")
    cacib_nbi = next(float(r["value"]) for r in signals if r["label"] == "CACIB France" and r["signal"] == "Net banking income")
    bar(ax, 0.54, bnp_nbi, 20, BNP, "BNP CIB", "€19.0bn NBI", "bnp-paribas.png", logo_face=BNP, logo_zoom=0.023)
    bar(ax, 0.27, cacib_nbi, 20, CACIB, "CACIB", "€8.664bn NBI", "cacib.png", logo_face="white", logo_zoom=0.047)
    for val in [0, 5, 10, 15, 20]:
        x = 0.32 + 0.63 * val / 20
        ax.plot([x, x], [0.13, 0.17], color=GRID, linewidth=0.7)
        ax.text(x, 0.08, str(val), ha="center", fontsize=6.8, color=MUTED)
    ax.text(0.32, 0.02, "Net banking income (€bn)", fontsize=6.7, color=MUTED)
    ax.text(0.68, 0.02, "reported perimeter ≠ France-only", fontsize=6.7, color=MUTED, style="italic")


def local_panel(fig, signals):
    ax = fig.add_axes([0.535, 0.235, 0.425, 0.245])
    panel(ax, "2  |  LUXEMBOURG LOCAL SIGNALS", "Different legal entities / reference years · deliberately not a league table")
    bnp_staff = next(float(r["value"]) for r in signals if r["label"] == "BNP CIB Luxembourg" and r["signal"] == "Employees")
    caceis_staff = next(float(r["value"]) for r in signals if r["label"] == "CACEIS Luxembourg" and r["signal"] == "Employees")
    bar(ax, 0.56, bnp_staff, 900, BNP, "BNP CIB", "72 staff · 2025", "bnp-paribas.png", logo_face=BNP, logo_zoom=0.023)
    bar(ax, 0.31, caceis_staff, 900, CACEIS, "CACEIS", "850 staff · 2023", "caceis.png", logo_face="white", logo_zoom=0.050)
    # Activity/client breadth is displayed as separate evidence chips, not
    # converted to a score or merged into the staff bars.
    ax.add_patch(FancyBboxPatch((0.04, 0.055), 0.42, 0.11, boxstyle="round,pad=0.008,rounding_size=0.015",
                                facecolor="#F0F5F9", edgecolor="none"))
    ax.text(0.06, 0.125, "BNP CIB LUX", fontsize=6.6, color=BNP, weight="bold")
    ax.text(0.06, 0.082, "5 named activity families", fontsize=8.0, color=INK, weight="bold")
    ax.add_patch(FancyBboxPatch((0.51, 0.055), 0.45, 0.11, boxstyle="round,pad=0.008,rounding_size=0.015",
                                facecolor="#FFF1F4", edgecolor="none"))
    ax.text(0.53, 0.125, "CACEIS IS BANK LUX", fontsize=6.6, color=CACEIS, weight="bold")
    ax.text(0.53, 0.082, "240+ clients*", fontsize=8.0, color=INK, weight="bold")
    ax.text(0.53, 0.012, "*reported perimeter includes Luxembourg, Continental Europe and offshore platforms", fontsize=5.8, color=MUTED)


def map_panel(fig):
    ax = fig.add_axes([0.045, 0.20, 0.43, 0.67])
    patches, names = europe_polygons()
    ax.add_collection(PatchCollection(patches, facecolor=LAND, edgecolor=LAND_EDGE, linewidth=0.45, zorder=1))
    ax.set_xlim(-2.4, 9.5)
    ax.set_ylim(47.2, 51.55)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.text(-1.95, 51.27, "FRANCE ↔ LUXEMBOURG", fontsize=10.2, weight="bold", color=INK)
    ax.text(-1.95, 50.98, "Four brand anchors · two evidence layers", fontsize=7.5, color=MUTED)

    paris = (2.3522, 48.8566)
    lux = (6.1319, 49.6116)
    ax.plot([paris[0], lux[0]], [paris[1], lux[1]], color=GOLD, linewidth=1.5, alpha=0.65, zorder=2)
    ax.text(4.05, 49.34, "same corridor · different scopes", fontsize=6.8, color=GOLD,
            rotation=6, ha="center", va="center", zorder=4,
            bbox=dict(boxstyle="round,pad=0.24", facecolor=PAPER, edgecolor="none", alpha=0.95))
    for point, color, label in [(paris, BNP, "PARIS"), (lux, GOLD, "LUXEMBOURG")]:
        ax.scatter(*point, s=360, facecolors="none", edgecolors=color, linewidths=2.2, zorder=5)
        ax.scatter(*point, s=34, color=color, edgecolor="white", linewidth=1.0, zorder=6)
        ax.text(point[0] + 0.15, point[1] - 0.29, label, fontsize=8.0, color=INK, weight="bold", zorder=7)

    # Four logo anchors, offset around the two cities to remain individually legible.
    anchors = [
        ("bnp-paribas.png", 1.15, 49.42, "BNP CIB · FRANCE", BNP, BNP, 0.021, (paris[0], paris[1] + 0.09)),
        ("cacib.png", 3.60, 48.27, "CACIB · FRANCE", CACIB, "white", 0.043, (paris[0], paris[1] - 0.09)),
        ("bnp-paribas.png", 5.00, 50.65, "BNP CIB · LUXEMBOURG", BNP, BNP, 0.021, (lux[0], lux[1] + 0.09)),
        ("caceis.png", 7.45, 48.93, "CACEIS · LUXEMBOURG", CACEIS, "white", 0.050, (lux[0], lux[1] - 0.09)),
    ]
    for filename, x, y, label, color, face, zoom, target in anchors:
        ax.plot([target[0], x], [target[1], y], color=color, linewidth=0.85, alpha=0.7, zorder=3)
        add_logo(ax, filename, x, y, zoom=zoom, facecolor=face,
                 edgecolor=color if face != "white" else GRID, frame=True, zorder=8)
        ax.text(x, y - 0.27, label, ha="center", va="top", fontsize=6.8, color=color, weight="bold", zorder=9)
    ax.text(-1.95, 47.48, "Map is positional: it does not represent booking location, revenue or legal-entity coverage.",
            fontsize=6.7, color=MUTED, style="italic")


def scope_key_panel(fig):
    ax = fig.add_axes([0.045, 0.075, 0.43, 0.175])
    panel(ax, "HOW TO READ THE COMPARISON", "The visual separates the only two defensible comparison layers")
    ax.add_patch(FancyBboxPatch((0.04, 0.18), 0.43, 0.38, boxstyle="round,pad=0.008,rounding_size=0.014",
                                facecolor="#F0F5F9", edgecolor="none"))
    ax.text(0.065, 0.46, "FRANCE / GROUP SCALE", fontsize=7.0, color=BNP, weight="bold")
    ax.text(0.065, 0.30, "BNP CIB and CACIB NBI signals", fontsize=8.2, color=INK, weight="bold")
    ax.text(0.065, 0.20, "same unit · group reporting · not France-only", fontsize=6.8, color=MUTED)
    ax.add_patch(FancyBboxPatch((0.52, 0.18), 0.44, 0.38, boxstyle="round,pad=0.008,rounding_size=0.014",
                                facecolor="#FFF1F4", edgecolor="none"))
    ax.text(0.545, 0.46, "LUXEMBOURG / LOCAL SIGNAL", fontsize=7.0, color=CACEIS, weight="bold")
    ax.text(0.545, 0.30, "BNP CIB and CACEIS local disclosures", fontsize=8.2, color=INK, weight="bold")
    ax.text(0.545, 0.20, "different entities · dates · business models", fontsize=6.8, color=MUTED)


def build():
    signals = load_signals()
    fig = plt.figure(figsize=(15.8, 8.8))
    fig.suptitle("France–Luxembourg CIB benchmark — four brands, two evidence layers",
                 x=0.045, y=0.965, ha="left", fontsize=20, weight="bold", color=INK)
    fig.text(0.045, 0.928,
             "A map locates the franchises; the panels show the public scale signal without mixing global BNP/CACIB data with local Luxembourg entities.",
             fontsize=9.3, color=MUTED)
    map_panel(fig)
    scope_key_panel(fig)
    group_panel(fig, signals)
    local_panel(fig, signals)

    # Executive reading strip.
    ax = fig.add_axes([0.535, 0.085, 0.425, 0.105])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.014,rounding_size=0.022",
                                facecolor="#F0F5F9", edgecolor="none"))
    ax.text(0.04, 0.68, "EXECUTIVE READING", fontsize=7.3, color=GOLD, weight="bold")
    ax.text(0.04, 0.37, "BNP CIB and CACIB carry the group-scale signal; Luxembourg reveals two distinct local business models.",
            fontsize=8.5, color=INK, weight="bold")
    ax.text(0.04, 0.13, "Use as a comparator, not as a four-way revenue ranking.", fontsize=7.0, color=MUTED)

    fig.text(0.045, 0.025,
             "Sources: BNP Paribas 2026 At a Glance; CACIB 2025 key figures; BNP Paribas Luxembourg CIB page; CACEIS Investor Services Bank Luxembourg CSR report. See data/four_brand_public_signals.csv.",
             fontsize=6.6, color=MUTED, ha="left", va="bottom")
    fig.subplots_adjust(left=0.02, right=0.985, bottom=0.045, top=0.89)
    png = OUT / "FOUR_BRANDS_ACTIVITY_COMPARATOR.png"
    fig.savefig(png, dpi=240, bbox_inches="tight")
    plt.close(fig)
    return png


def main():
    png = build()
    pdf = OUT / "FOUR_BRANDS_ACTIVITY_COMPARATOR.pdf"
    with PdfPages(pdf) as pages:
        image = plt.imread(png)
        page = plt.figure(figsize=(15.8, 8.8))
        ax = page.add_axes([0, 0, 1, 1])
        ax.imshow(image)
        ax.axis("off")
        pages.savefig(page, bbox_inches="tight", pad_inches=0)
        plt.close(page)
    print(png)
    print(pdf)


if __name__ == "__main__":
    main()
