"""Build a simplified executive bubble chart for an M1 audience.

The chart uses a categorical vertical reading instead of a logarithmic axis:
that makes the message understandable in a few seconds while retaining the
public client signals as large labels. Bubble area is an employee signal, not
revenue.
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
from matplotlib.patches import FancyBboxPatch
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

COLORS = {"bnp_fr": BNP, "cacib_fr": CACIB, "caceis_lu": CACEIS, "bnp_lu": BNP}
FACES = {"bnp_fr": BNP_LIGHT, "cacib_fr": CACIB_LIGHT, "caceis_lu": CACEIS_LIGHT, "bnp_lu": BNP_LIGHT}
LOGO_FACE = {"bnp_fr": BNP, "cacib_fr": "white", "caceis_lu": "white", "bnp_lu": BNP}
LOGO_FILE = {"bnp_fr": "bnp-paribas.png", "cacib_fr": "cacib.png", "caceis_lu": "caceis.png", "bnp_lu": "bnp-paribas.png"}

# The bubble plot is intentionally categorical for a first-year audience.
# The number shown beside each bubble remains the public signal behind it.
PLOT_POSITION = {
    "bnp_fr": (2.84, 3.08),       # broad group platform / highest public reach
    "cacib_fr": (3.08, 2.72),    # broad group platform / quantified reach
    "caceis_lu": (2.02, 2.03),   # specialised domain / local quantified signal
    "bnp_lu": (1.05, 1.00),      # specialist local platform / client count N/D
}
PLOT_LOGO_ZOOM = {"bnp_fr": 0.038, "cacib_fr": 0.145, "caceis_lu": 0.072, "bnp_lu": 0.038}
CARD_LOGO_ZOOM = {"bnp_fr": 0.030, "cacib_fr": 0.105, "caceis_lu": 0.062, "bnp_lu": 0.030}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "text.color": INK,
    "figure.facecolor": PAPER,
    "savefig.facecolor": PAPER,
})


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


def add_logo(ax, brand_id, x, y, zoom, frame=True, zorder=10):
    face = LOGO_FACE[brand_id]
    edge = face if face != "white" else GRID
    props = dict(boxstyle="round,pad=0.18", facecolor=face, edgecolor=edge, linewidth=0.7) if frame else None
    ax.add_artist(AnnotationBbox(OffsetImage(cropped_logo(LOGO_FILE[brand_id]), zoom=zoom),
                                 (x, y), frameon=frame, bboxprops=props, pad=0.18, zorder=zorder))


def brand_metric(row):
    return {
        "bnp_fr": ("19k+", "clients", "42k staff"),
        "cacib_fr": ("~3.6k", "clients", "10.8k staff"),
        "caceis_lu": ("240+", "clients*", "850 staff"),
        "bnp_lu": ("N/D", "clients", "72 staff"),
    }[row["brand_id"]]


def short_products(row):
    return {
        "bnp_fr": "Markets · financing · securities services",
        "cacib_fr": "Markets · financing · investment banking",
        "caceis_lu": "Custody · funds · depositary",
        "bnp_lu": "Forex · credit · leasing · FI coverage",
    }[row["brand_id"]]


def add_simple_card(ax, row, y):
    brand_id = row["brand_id"]
    color = COLORS[brand_id]
    metric, unit, staff = brand_metric(row)
    ax.add_patch(FancyBboxPatch((0.02, y - 0.085), 0.96, 0.155,
                                boxstyle="round,pad=0.008,rounding_size=0.018",
                                facecolor=FACES[brand_id], edgecolor=GRID, linewidth=0.7, zorder=1))
    ax.add_patch(FancyBboxPatch((0.02, y - 0.085), 0.012, 0.155,
                                boxstyle="round,pad=0.002,rounding_size=0.006",
                                facecolor=color, edgecolor=color, linewidth=0, zorder=2))
    add_logo(ax, brand_id, 0.105, y + 0.022, CARD_LOGO_ZOOM[brand_id], frame=True, zorder=8)
    ax.text(0.23, y + 0.046, row["brand_label"].upper(), fontsize=8.5, color=color, weight="bold")
    ax.text(0.23, y + 0.020, row["territory"].upper(), fontsize=6.0, color=MUTED, weight="bold")
    ax.text(0.23, y - 0.026, metric, fontsize=13.0, color=color, weight="bold", va="center")
    ax.text(0.43, y - 0.026, unit, fontsize=6.6, color=INK, weight="bold", va="center")
    ax.text(0.23, y - 0.057, staff, fontsize=6.8, color=MUTED, weight="bold")
    ax.text(0.54, y + 0.030, "CORE OFFER", fontsize=6.1, color=color, weight="bold")
    ax.text(0.54, y - 0.005, textwrap.fill(short_products(row), width=28), fontsize=6.7,
            color=INK, va="top", linespacing=1.08)


def build():
    rows = load_rows()
    fig = plt.figure(figsize=(16.0, 8.8))
    fig.suptitle("Four franchises — who they serve and what they offer",
                 x=0.04, y=0.965, ha="left", fontsize=21, weight="bold", color=INK)
    fig.text(0.04, 0.928,
             "Read the chart in 20 seconds: left → right = offer breadth · up = public reach · bubble size = operating weight.",
             fontsize=10.0, color=MUTED)

    # Main bubble chart.
    ax = fig.add_axes([0.07, 0.22, 0.60, 0.62])
    ax.set_xlim(0.65, 3.38)
    ax.set_ylim(0.55, 3.48)
    ax.set_xticks([1, 2, 3], ["SPECIALIST", "MIXED", "BROAD OFFER"])
    ax.set_yticks([1, 2, 3], ["LOCAL SIGNAL", "PUBLIC LOCAL REACH", "GROUP PLATFORM"])
    ax.set_xlabel("WIDTH OF PUBLIC OFFER", labelpad=12, fontsize=9.5, weight="bold")
    ax.set_ylabel("CLIENT REACH", labelpad=12, fontsize=9.5, weight="bold")
    ax.grid(axis="both", color=GRID, linewidth=0.8, alpha=0.9)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0, labelsize=9.2)

    # Horizontal reading bands make the chart understandable without a log scale.
    ax.axhspan(0.55, 1.45, facecolor="#F4F6F8", zorder=0)
    ax.axhspan(1.45, 2.45, facecolor="#FBFCFD", zorder=0)
    ax.axhspan(2.45, 3.48, facecolor="#F2F8FC", zorder=0)
    ax.text(0.70, 3.34, "BUBBLE AREA = PUBLIC STAFF SIGNAL", fontsize=7.4, color=GOLD, weight="bold")
    ax.text(0.70, 3.22, "not revenue · not market share", fontsize=7.0, color=MUTED, style="italic")

    for row in rows:
        brand_id = row["brand_id"]
        x, y = PLOT_POSITION[brand_id]
        staff = float(row["public_staff"])
        bubble_area = 24.0 * np.sqrt(staff)
        color = COLORS[brand_id]
        ax.scatter(x, y, s=bubble_area, color=color, alpha=0.90, edgecolor="white", linewidth=2.2, zorder=5)
        add_logo(ax, brand_id, x, y, PLOT_LOGO_ZOOM[brand_id], frame=True, zorder=8)
        metric, unit, staff_display = brand_metric(row)
        if brand_id == "bnp_fr":
            label_xy = (2.05, 3.34)
        elif brand_id == "cacib_fr":
            label_xy = (2.30, 2.52)
        elif brand_id == "caceis_lu":
            label_xy = (2.14, 2.34)
        else:
            label_xy = (1.22, 1.30)
        ax.annotate(row["brand_label"], xy=(x, y), xytext=label_xy, fontsize=11.0,
                    color=INK, weight="bold", arrowprops=dict(arrowstyle="-", color=color, linewidth=1.0), zorder=9)
        ax.text(label_xy[0], label_xy[1] - 0.14, f"{metric} {unit} · {staff_display}", fontsize=8.4,
                color=color, weight="bold", zorder=9)
        if brand_id == "bnp_lu":
            ax.text(label_xy[0], label_xy[1] - 0.27, "client count not publicly disclosed", fontsize=7.1,
                    color=MUTED, style="italic", zorder=9)
        if brand_id == "caceis_lu":
            ax.text(label_xy[0], label_xy[1] - 0.27, "*perimeter includes Luxembourg + wider platforms", fontsize=6.7,
                    color=MUTED, style="italic", zorder=9)

    ax.legend(handles=[
        Line2D([0], [0], marker="o", color="none", markerfacecolor=BNP, markeredgecolor="white", markersize=9, label="BNP Paribas CIB"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=CACIB, markeredgecolor="white", markersize=9, label="CACIB"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=CACEIS, markeredgecolor="white", markersize=9, label="CACEIS"),
    ], loc="lower right", frameon=False, fontsize=8.0)

    # Right-side read-out: one big number and one simple product sentence.
    info = fig.add_axes([0.71, 0.22, 0.25, 0.62])
    info.set_xlim(0, 1)
    info.set_ylim(0, 1)
    info.axis("off")
    info.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.012,rounding_size=0.022",
                                  facecolor="white", edgecolor=GRID, linewidth=0.9))
    info.text(0.04, 0.955, "FOUR SIMPLE READ-OUTS", fontsize=10.0, color=INK, weight="bold")
    info.text(0.04, 0.925, "The number = reach · the size = staff · the line = core offer", fontsize=7.2, color=MUTED)
    row_by_id = {r["brand_id"]: r for r in rows}
    for brand_id, y in [("bnp_fr", 0.78), ("cacib_fr", 0.57), ("caceis_lu", 0.36), ("bnp_lu", 0.15)]:
        add_simple_card(info, row_by_id[brand_id], y)

    bottom = fig.add_axes([0.07, 0.065, 0.89, 0.09])
    bottom.set_xlim(0, 1)
    bottom.set_ylim(0, 1)
    bottom.axis("off")
    bottom.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.012,rounding_size=0.020",
                                    facecolor="#F0F5F9", edgecolor="none"))
    bottom.text(0.025, 0.68, "ONE-SENTENCE TAKEAWAY", fontsize=7.2, color=GOLD, weight="bold")
    bottom.text(0.025, 0.36,
                "BNP CIB and CACIB serve broad group platforms; CACEIS specialises in asset servicing; BNP CIB Luxembourg is a focused local CIB offer.",
                fontsize=8.5, color=INK, weight="bold")
    bottom.text(0.72, 0.68, "IMPORTANT", fontsize=6.8, color=MUTED, weight="bold")
    bottom.text(0.72, 0.36, "N/D is not zero · scopes are not a four-way revenue ranking.", fontsize=7.0, color=MUTED)

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
