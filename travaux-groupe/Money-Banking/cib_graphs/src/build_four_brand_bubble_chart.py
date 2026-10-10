"""Build an executive four-brand bubble chart.

The y-axis uses publicly quantified client reach when disclosed. BNP CIB
Luxembourg is intentionally shown in an N/D band because the public local
source does not publish a local client count. Bubble area is an employee
signal, not revenue.
"""
from __future__ import annotations

import csv
import textwrap
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib.patches import FancyBboxPatch, Circle
from matplotlib.lines import Line2D

from build_cib_graphs import BNP, CACIB, GRID, INK, MUTED, PAPER

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
LOGOS = DATA / "logos"
OUT = ROOT / "output" / "four_brand_comparator"
OUT.mkdir(parents=True, exist_ok=True)

CACEIS = "#B4003A"
CACEIS_LIGHT = "#F7E3E9"
BNP_LIGHT = "#DCE9F4"
CACIB_LIGHT = "#DDF1EE"
GOLD = "#D59B27"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "text.color": INK,
    "figure.facecolor": PAPER,
    "savefig.facecolor": PAPER,
})

COLORS = {
    "bnp_fr": BNP,
    "cacib_fr": CACIB,
    "caceis_lu": CACEIS,
    "bnp_lu": BNP,
}
LOGO_FACE = {
    "bnp_fr": BNP,
    "cacib_fr": "white",
    "caceis_lu": "white",
    "bnp_lu": BNP,
}
LOGO_ZOOM = {
    "bnp_fr": 0.038,
    "cacib_fr": 0.145,
    "caceis_lu": 0.072,
    "bnp_lu": 0.038,
}
LOGO_FILE = {
    "bnp_fr": "bnp-paribas.png",
    "cacib_fr": "cacib.png",
    "caceis_lu": "caceis.png",
    "bnp_lu": "bnp-paribas.png",
}


def load_rows():
    with (DATA / "four_brand_bubble_metrics.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cropped_logo(filename):
    image = mpimg.imread(LOGOS / filename)
    if image.ndim == 2:
        image = np.dstack([image, image, image])
    if filename != "bnp-paribas.png":
        rgb = image[:, :, :3]
        mask = np.any(rgb < 0.96, axis=2)
        ys, xs = np.where(mask)
        if len(xs):
            image = image[max(0, ys.min() - 8):ys.max() + 9,
                          max(0, xs.min() - 12):xs.max() + 13]
    return image


def add_logo(ax, brand_id, x, y, frame=True, zorder=10):
    face = LOGO_FACE[brand_id]
    edge = face if face != "white" else GRID
    props = dict(boxstyle="round,pad=0.18", facecolor=face, edgecolor=edge, linewidth=0.7) if frame else None
    ab = AnnotationBbox(OffsetImage(cropped_logo(LOGO_FILE[brand_id]), zoom=LOGO_ZOOM[brand_id]),
                        (x, y), frameon=frame, bboxprops=props, pad=0.18, zorder=zorder)
    ax.add_artist(ab)


def add_info_card(ax, row, y):
    brand_id = row["brand_id"]
    color = COLORS[brand_id]
    face = {"bnp_fr": "#F3F7FB", "cacib_fr": "#EFFAF8", "caceis_lu": "#FFF2F5", "bnp_lu": "#F3F7FB"}[brand_id]
    metric = {
        "bnp_fr": ("19k+", "clients"),
        "cacib_fr": ("~3.6k", "clients"),
        "caceis_lu": ("240+", "clients*"),
        "bnp_lu": ("N/D", "clients"),
    }[brand_id]
    ax.add_patch(FancyBboxPatch((0.015, y - 0.105), 0.97, 0.19,
                                boxstyle="round,pad=0.009,rounding_size=0.018",
                                facecolor=face, edgecolor=GRID, linewidth=0.7, zorder=1))
    ax.add_patch(FancyBboxPatch((0.015, y - 0.105), 0.012, 0.19,
                                boxstyle="round,pad=0.002,rounding_size=0.006",
                                facecolor=color, edgecolor=color, linewidth=0, zorder=2))
    add_logo(ax, brand_id, 0.105, y + 0.035, frame=True, zorder=8)
    ax.text(0.235, y + 0.060, row["brand_label"].upper(), fontsize=8.5, color=color, weight="bold", va="center")
    ax.text(0.235, y + 0.030, row["territory"].upper() + " · " + row["offer_breadth_label"].upper(), fontsize=6.0, color=MUTED, weight="bold")
    ax.text(0.235, y - 0.008, metric[0], fontsize=13.0, color=color, weight="bold", va="center")
    ax.text(0.405, y - 0.008, metric[1], fontsize=6.8, color=INK, weight="bold", va="center")
    ax.text(0.235, y - 0.043, row["staff_display"], fontsize=6.8, color=MUTED, weight="bold")
    ax.text(0.53, y + 0.056, "PRODUCTS", fontsize=6.2, color=color, weight="bold", va="center")
    products = textwrap.fill(row["products"].replace(";", " ·"), width=27)
    ax.text(0.53, y + 0.026, products, fontsize=6.1, color=INK, va="top", linespacing=1.10)


def build():
    rows = load_rows()
    fig = plt.figure(figsize=(16.0, 8.8))
    fig.suptitle("Four franchises — client reach × offer breadth × operating weight",
                 x=0.04, y=0.965, ha="left", fontsize=20, weight="bold", color=INK)
    fig.text(0.04, 0.928,
             "Bubble chart for committee reading: vertical position = public client signal, horizontal position = qualitative offer breadth, bubble area = public staff signal.",
             fontsize=9.3, color=MUTED)

    ax = fig.add_axes([0.07, 0.19, 0.60, 0.66])
    ax.set_xlim(0.72, 3.34)
    ax.set_ylim(50, 30000)
    ax.set_yscale("log")
    ax.axhspan(50, 80, facecolor="#F3F5F7", zorder=0)
    ax.axhline(80, color=GRID, linewidth=0.8, linestyle="--", zorder=1)
    ax.text(0.76, 64, "N/D BAND — local client count not disclosed", fontsize=7.2, color=MUTED,
            va="center", style="italic", zorder=3)
    ax.set_xticks([1, 2, 3], ["SPECIALIST", "MIXED", "UNIVERSAL"])
    ax.set_xlabel("PUBLIC OFFER BREADTH  ·  qualitative, not a score", labelpad=12, fontsize=9.2, weight="bold")
    ax.set_ylabel("PUBLIC CLIENT REACH  ·  log scale", labelpad=12, fontsize=9.2, weight="bold")
    ax.set_yticks([100, 300, 1000, 3000, 10000, 30000])
    ax.set_yticklabels(["100", "300", "1k", "3k", "10k", "30k"])
    ax.grid(axis="y", color=GRID, linewidth=0.7, alpha=0.9)
    ax.grid(axis="x", color=GRID, linewidth=0.5, alpha=0.55)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0, labelsize=8.6)

    # Visual area is proportional to the public employee signal using a square-
    # root display scale so the smallest local platform remains visible.
    for row in rows:
        brand_id = row["brand_id"]
        x = float(row["offer_breadth_position"])
        staff = float(row["public_staff"])
        bubble_area = 20.0 * np.sqrt(staff)
        color = COLORS[brand_id]
        if row["public_clients"]:
            y = float(row["public_clients"])
            ax.scatter(x, y, s=bubble_area, color=color, alpha=0.88, edgecolor="white", linewidth=2.0, zorder=4)
            add_logo(ax, brand_id, x, y, frame=True, zorder=8)
            # Alternating callouts keep the labels out of each other on the log scale.
            if brand_id == "bnp_fr":
                text_xy = (x - 0.58, y * 1.38)
            elif brand_id == "cacib_fr":
                text_xy = (x - 0.48, y * 1.34)
            else:
                text_xy = (x + 0.13, y * 1.28)
            ax.annotate(row["brand_label"], xy=(x, y), xytext=text_xy,
                        fontsize=10.8, color=INK, weight="bold",
                        arrowprops=dict(arrowstyle="-", color=color, linewidth=1.0), zorder=9)
            ax.text(text_xy[0], text_xy[1] / 1.16,
                    f"{row['client_display']} · {row['staff_display']}", fontsize=8.0, color=color, weight="bold", zorder=9)
        else:
            # N/D is plotted only inside the explicitly labelled band: its y
            # coordinate is a visual slot, not an invented client count.
            y = 62
            ax.scatter(x, y, s=bubble_area, facecolors="white", edgecolor=color,
                       linewidth=2.0, zorder=5)
            add_logo(ax, brand_id, x, y, frame=True, zorder=8)
            ax.annotate(row["brand_label"], xy=(x, y), xytext=(x + 0.13, 96),
                        fontsize=10.8, color=INK, weight="bold",
                        arrowprops=dict(arrowstyle="-", color=color, linewidth=1.0), zorder=9)
            ax.text(x + 0.13, 83, "CLIENT COUNT N/D · 72 STAFF", fontsize=8.0, color=color, weight="bold", zorder=9)

    ax.text(0.78, 28000, "BUBBLE AREA ∝ PUBLIC STAFF SIGNAL", fontsize=7.4, color=GOLD, weight="bold")
    ax.text(0.78, 23800, "not revenue · not market share", fontsize=6.9, color=MUTED, style="italic")
    ax.legend(handles=[
        Line2D([0], [0], marker="o", color="none", markerfacecolor=BNP, markeredgecolor="white", markersize=8, label="BNP Paribas CIB"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=CACIB, markeredgecolor="white", markersize=8, label="CACIB"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=CACEIS, markeredgecolor="white", markersize=8, label="CACEIS"),
    ], loc="lower right", frameon=False, fontsize=7.3)

    info = fig.add_axes([0.71, 0.19, 0.25, 0.66])
    info.set_xlim(0, 1)
    info.set_ylim(0, 1)
    info.axis("off")
    info.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.012,rounding_size=0.022",
                                  facecolor="white", edgecolor=GRID, linewidth=0.9))
    info.text(0.04, 0.955, "FOUR READ-OUTS", fontsize=9.5, color=INK, weight="bold")
    info.text(0.04, 0.925, "The dot tells the story; the card tells what it sells.", fontsize=7.0, color=MUTED)
    row_by_id = {r["brand_id"]: r for r in rows}
    for brand_id, y in [("bnp_fr", 0.78), ("cacib_fr", 0.57), ("caceis_lu", 0.36), ("bnp_lu", 0.15)]:
        add_info_card(info, row_by_id[brand_id], y)

    bottom = fig.add_axes([0.07, 0.065, 0.89, 0.075])
    bottom.set_xlim(0, 1)
    bottom.set_ylim(0, 1)
    bottom.axis("off")
    bottom.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.012,rounding_size=0.020",
                                    facecolor="#F0F5F9", edgecolor="none"))
    bottom.text(0.025, 0.66, "EXECUTIVE READING", fontsize=7.1, color=GOLD, weight="bold")
    bottom.text(0.025, 0.34,
                "BNP CIB / CACIB = broad client platforms · CACEIS = mixed but specialised asset servicing · BNP CIB Lux = specialist local CIB.",
                fontsize=8.2, color=INK, weight="bold")
    bottom.text(0.72, 0.66, "DATA DISCIPLINE", fontsize=6.7, color=MUTED, weight="bold")
    bottom.text(0.72, 0.34, "N/D ≠ zero · CACEIS client perimeter is broader than Luxembourg.", fontsize=6.8, color=MUTED)

    fig.text(0.07, 0.025,
             "Sources: BNP CIB at a glance / 2026 At a Glance; CACIB 2025 key figures; BNP Paribas Luxembourg CIB page; CACEIS Luxembourg Investor Services report. See data/four_brand_bubble_metrics.csv.",
             fontsize=6.4, color=MUTED, ha="left", va="bottom")
    fig.subplots_adjust(left=0.02, right=0.985, bottom=0.045, top=0.89)
    png = OUT / "FOUR_BRANDS_EXECUTIVE_BUBBLE.png"
    fig.savefig(png, dpi=240, bbox_inches="tight")
    plt.close(fig)
    return png


def main():
    png = build()
    pdf = OUT / "FOUR_BRANDS_EXECUTIVE_BUBBLE.pdf"
    with PdfPages(pdf) as pages:
        image = plt.imread(png)
        page = plt.figure(figsize=(16.0, 8.8))
        ax = page.add_axes([0, 0, 1, 1])
        ax.imshow(image)
        ax.axis("off")
        pages.savefig(page, bbox_inches="tight", pad_inches=0)
        plt.close(page)
    print(png)
    print(pdf)


if __name__ == "__main__":
    main()
