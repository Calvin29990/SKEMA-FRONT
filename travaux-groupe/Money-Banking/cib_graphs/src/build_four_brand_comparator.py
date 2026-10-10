"""Build the four-brand product/client comparator.

The Europe map already explains location. This slide explains what each of the
four selected platforms publicly says it delivers, and for which client
segments. Group-scale and local-entity signals remain visibly separated.
"""
from __future__ import annotations

import csv
from pathlib import Path
from textwrap import fill

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib.patches import FancyBboxPatch

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
INK_SOFT = "#334454"
EMPTY = "#F5F7F9"
GOLD = "#D59B27"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "text.color": INK,
    "figure.facecolor": PAPER,
    "savefig.facecolor": PAPER,
})

BRANDS = [
    {
        "id": "bnp_fr", "name": "BNP CIB", "scope": "FRANCE · GROUP PLATFORM",
        "signal": "€19.0bn NBI · FY2025*", "logo": "bnp-paribas.png", "color": BNP,
        "face": BNP, "zoom": 0.024,
        "clients": ["Corporates", "Financial institutions", "Institutional investors"],
    },
    {
        "id": "cacib_fr", "name": "CACIB", "scope": "FRANCE · GROUP PLATFORM",
        "signal": "€8.664bn NBI · FY2025†", "logo": "cacib.png", "color": CACIB,
        "face": "white", "zoom": 0.050,
        "clients": ["Corporates", "Financial institutions", "Public sector"],
    },
    {
        "id": "bnp_lu", "name": "BNP CIB", "scope": "LUXEMBOURG · LOCAL ENTITY",
        "signal": "72 staff · 5 named functions", "logo": "bnp-paribas.png", "color": BNP,
        "face": BNP, "zoom": 0.024,
        "clients": ["Corporate clients", "Institutional clients", "BGL BNP clients"],
    },
    {
        "id": "caceis_lu", "name": "CACEIS", "scope": "LUXEMBOURG · LOCAL ENTITY",
        "signal": "850 staff · 240+ clients‡", "logo": "caceis.png", "color": CACEIS,
        "face": "white", "zoom": 0.052,
        "clients": ["Asset managers", "Funds", "Banks & brokers", "Private capital"],
    },
]

PRODUCTS = [
    ("CAPITAL MARKETS / RISK", {
        "bnp_fr": "Global Markets · FX · rates · equities",
        "cacib_fr": "Origination · structuring · sales · trading",
        "bnp_lu": "Forex · brokerage · capital markets",
        "caceis_lu": "Treasury · market services · securities lending",
    }),
    ("FINANCING / ADVISORY", {
        "bnp_fr": "Global Banking · financing · cash management",
        "cacib_fr": "Syndicated · structured · project finance",
        "bnp_lu": "Global Markets-Credit · structured finance",
        "caceis_lu": "Finance solutions · issuer services",
    }),
    ("SECURITIES SERVICES", {
        "bnp_fr": "Custody · clearing · asset servicing",
        "cacib_fr": "Not separately shown in selected CIB scope",
        "bnp_lu": "Not separately shown in local CIB page",
        "caceis_lu": "Custody · clearing · depositary · trustee",
    }),
    ("ASSET / FUND SERVICES", {
        "bnp_fr": "Fund services · institutional servicing",
        "cacib_fr": "Not separately shown in selected CIB scope",
        "bnp_lu": "Not separately shown in local CIB page",
        "caceis_lu": "Fund admin · shareholder · private capital",
    }),
    ("SPECIALIST LOCAL OFFER", {
        "bnp_fr": "Risk management · trade finance",
        "cacib_fr": "Energy & infrastructure · sustainable finance",
        "bnp_lu": "Asset leasing · FI coverage · ALM",
        "caceis_lu": "Middle-office · post-trade support",
    }),
]


def load_public_rows():
    with (DATA / "four_brand_product_client.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cropped_logo(filename):
    image = mpimg.imread(LOGOS / filename)
    if image.ndim == 2:
        image = np.dstack([image, image, image])
    # White-background wordmarks are cropped to their content. BNP's black
    # background is intentional and gives the wordmark contrast on a navy card.
    if filename != "bnp-paribas.png":
        rgb = image[:, :, :3]
        mask = np.any(rgb < 0.96, axis=2)
        ys, xs = np.where(mask)
        if len(xs):
            image = image[max(0, ys.min() - 8):ys.max() + 9,
                          max(0, xs.min() - 12):xs.max() + 13]
    return image


def add_logo(ax, filename, x, y, zoom, facecolor="white", edgecolor=GRID, frame=True, zorder=8):
    props = dict(boxstyle="round,pad=0.20", facecolor=facecolor, edgecolor=edgecolor, linewidth=0.7) if frame else None
    ax.add_artist(AnnotationBbox(OffsetImage(cropped_logo(filename), zoom=zoom), (x, y),
                                 frameon=frame, bboxprops=props, pad=0.18, zorder=zorder))


def round_box(ax, xy, width, height, facecolor="white", edgecolor=GRID, linewidth=0.8, radius=0.018, zorder=1):
    patch = FancyBboxPatch(xy, width, height, boxstyle=f"round,pad=0.009,rounding_size={radius}",
                           facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth, zorder=zorder)
    ax.add_patch(patch)
    return patch


def brand_header(ax, brand, x, width):
    color = brand["color"]
    round_box(ax, (x, 0.02), width, 0.96, facecolor="white", edgecolor=GRID, linewidth=0.9, zorder=1)
    ax.add_patch(FancyBboxPatch((x, 0.02), 0.012, 0.96, boxstyle="round,pad=0.002,rounding_size=0.008",
                                facecolor=color, edgecolor=color, linewidth=0, zorder=2))
    # Bank logo + scope.
    add_logo(ax, brand["logo"], x + width * 0.18, 0.82, zoom=brand["zoom"],
             facecolor=brand["face"], edgecolor=brand["face"] if brand["face"] != "white" else GRID,
             frame=True, zorder=8)
    ax.text(x + width * 0.38, 0.86, brand["name"], fontsize=9.6, weight="bold", color=color, va="center")
    ax.text(x + width * 0.38, 0.76, brand["scope"], fontsize=6.2, color=MUTED, va="center")
    round_box(ax, (x + 0.035, 0.59), width - 0.07, 0.105, facecolor=color, edgecolor=color, linewidth=0, radius=0.012, zorder=3)
    ax.text(x + 0.055, 0.642, "PUBLIC SCALE SIGNAL", fontsize=5.9, color="white", weight="bold", va="center")
    ax.text(x + 0.055, 0.605, brand["signal"], fontsize=7.8, color="white", weight="bold", va="center")
    ax.text(x + 0.035, 0.46, "CLIENT COVERAGE", fontsize=6.0, color=color, weight="bold", va="center")
    ax.text(x + 0.035, 0.35, fill(" · ".join(brand["clients"]), width=29), fontsize=6.5, color=INK_SOFT, va="top")


def pill(ax, x, y, width, text, color, face, fontsize=6.8):
    round_box(ax, (x, y), width, 0.042, facecolor=face, edgecolor="none", linewidth=0, radius=0.015, zorder=5)
    ax.text(x + 0.012, y + 0.021, text, fontsize=fontsize, color=color, va="center", weight="bold", zorder=6)


def matrix_panel(fig, public_rows):
    ax = fig.add_axes([0.04, 0.145, 0.92, 0.49])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    round_box(ax, (0, 0), 1, 1, facecolor="white", edgecolor=GRID, linewidth=0.9, radius=0.024, zorder=0)
    ax.text(0.022, 0.95, "PUBLICLY NAMED PRODUCT ARCHITECTURE", fontsize=10.4, weight="bold", color=INK)
    ax.text(0.022, 0.895, "Filled cells show an activity or service publicly named for the selected platform; they do not represent revenue share.",
            fontsize=7.2, color=MUTED)

    left = 0.205
    gap = 0.012
    col_w = 0.185
    row_top = 0.68
    row_h = 0.10
    row_gap = 0.012
    # Header strips align the product matrix to the four actual logo anchors.
    for i, brand in enumerate(BRANDS):
        x = left + i * (col_w + gap)
        ax.add_patch(FancyBboxPatch((x, 0.80), col_w, 0.055, boxstyle="round,pad=0.005,rounding_size=0.011",
                                    facecolor=brand["color"], edgecolor="none", zorder=2))
        ax.text(x + col_w / 2, 0.827, "FRANCE" if i < 2 else "LUXEMBOURG", ha="center", va="center",
                fontsize=7.0, color="white", weight="bold")

    for r, (row_label, values) in enumerate(PRODUCTS):
        y = row_top - r * (row_h + row_gap)
        ax.text(0.022, y + row_h / 2, row_label, fontsize=6.9, color=INK, weight="bold", va="center")
        ax.plot([0.022, 0.18], [y - 0.004, y - 0.004], color=GRID, linewidth=0.65)
        for i, brand in enumerate(BRANDS):
            x = left + i * (col_w + gap)
            value = values[brand["id"]]
            is_empty = value.startswith("Not separately")
            face = EMPTY if is_empty else ([BNP_LIGHT, CACIB_LIGHT, BNP_LIGHT, CACEIS_LIGHT][i])
            edge = "none" if is_empty else [BNP, CACIB, BNP, CACEIS][i]
            round_box(ax, (x, y), col_w, row_h, facecolor=face, edgecolor=edge, linewidth=0.8,
                      radius=0.014, zorder=1)
            # Short accent marker is used instead of a faux quantitative scale.
            if not is_empty:
                ax.add_patch(FancyBboxPatch((x, y), 0.009, row_h, boxstyle="round,pad=0.001,rounding_size=0.004",
                                            facecolor=edge, edgecolor=edge, linewidth=0, zorder=3))
            text = fill(value, width=27 if not is_empty else 29)
            ax.text(x + 0.019, y + row_h / 2, text, fontsize=6.8 if not is_empty else 6.1,
                    color=INK_SOFT if not is_empty else MUTED, va="center", zorder=4,
                    style="normal" if not is_empty else "italic")

    # Client universe band is part of the same visual logic, not a separate legend.
    ax.text(0.022, 0.085, "CLIENT SEGMENTS NAMED IN THE PUBLIC OFFER", fontsize=7.1, color=GOLD, weight="bold")
    for i, brand in enumerate(BRANDS):
        x = left + i * (col_w + gap)
        ax.plot([x, x + col_w], [0.12, 0.12], color=GRID, linewidth=0.65)
        round_box(ax, (x + 0.008, 0.028), col_w - 0.016, 0.075,
                  facecolor=[BNP_LIGHT, CACIB_LIGHT, BNP_LIGHT, CACEIS_LIGHT][i],
                  edgecolor="none", linewidth=0, radius=0.012, zorder=2)
        ax.text(x + 0.020, 0.087, fill(" · ".join(brand["clients"]), width=27),
                fontsize=5.9, color=brand["color"], va="top", weight="bold", zorder=4)

    # Vertical separators turn it into a portfolio architecture rather than a raw table.
    for i in range(1, 4):
        x = left + i * (col_w + gap) - gap / 2
        ax.plot([x, x], [0.16, 0.89], color=GRID, linewidth=0.65, alpha=0.9)
    return ax


def footer_panel(fig):
    ax = fig.add_axes([0.04, 0.055, 0.92, 0.065])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    round_box(ax, (0, 0), 1, 1, facecolor="#F0F5F9", edgecolor="none", linewidth=0, radius=0.018, zorder=0)
    ax.text(0.022, 0.67, "EXECUTIVE READING", fontsize=7.3, color=GOLD, weight="bold")
    ax.text(0.022, 0.34,
            "BNP CIB / CACIB = broad platforms · BNP CIB Lux = focused CIB · CACEIS Lux = post-trade / asset servicing.",
            fontsize=7.6, color=INK, weight="bold")
    ax.text(0.70, 0.67, "PUBLICLY NAMED ≠ EXHAUSTIVE", fontsize=6.5, color=MUTED, weight="bold")
    ax.text(0.70, 0.34, "No cell = revenue or market-share measure.", fontsize=6.8, color=MUTED)


def build():
    public_rows = load_public_rows()
    fig = plt.figure(figsize=(15.8, 8.8))
    fig.suptitle("Four CIB franchises — product architecture and client coverage",
                 x=0.04, y=0.965, ha="left", fontsize=20, weight="bold", color=INK)
    fig.text(0.04, 0.928,
             "The Europe map already explains where the platforms are; this slide explains what each one delivers and to which client universe.",
             fontsize=9.3, color=MUTED)

    header_ax = fig.add_axes([0.04, 0.695, 0.92, 0.205])
    header_ax.set_xlim(0, 1)
    header_ax.set_ylim(0, 1)
    header_ax.axis("off")
    left = 0.0
    gap = 0.014
    col_w = (1 - 3 * gap) / 4
    for i, brand in enumerate(BRANDS):
        brand_header(header_ax, brand, left + i * (col_w + gap), col_w)

    matrix_panel(fig, public_rows)
    footer_panel(fig)
    fig.text(0.04, 0.025,
             "Sources: BNP CIB / EMEA public offer; CACIB 2025 activity report and URD; BNP Paribas Luxembourg CIB pages; CACEIS 2025 brochure and Luxembourg Investor Services report. See data/four_brand_product_client.csv.  ‡ CACEIS client scope includes Luxembourg, Continental Europe and offshore platforms.",
             fontsize=6.4, color=MUTED, ha="left", va="bottom")
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.04, top=0.89)
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
