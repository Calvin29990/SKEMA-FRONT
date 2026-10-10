"""Build director-ready BNP Paribas / CACIB executive graphics.

The figures deliberately show public reported scopes and disclose where those
scopes are not identical. No local Luxembourg financial figure is fabricated.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Polygon, FancyBboxPatch
from matplotlib.collections import PatchCollection
from matplotlib.colors import ListedColormap

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)

# Executive palette: BNP navy, Crédit Agricole/CACIB green, neutral ink.
BNP = "#0B2E59"
BNP_LIGHT = "#4B82B8"
CACIB = "#00857A"
CACIB_LIGHT = "#54B7A9"
INK = "#152536"
MUTED = "#5D6B78"
GRID = "#D9E1E8"
LAND = "#E8EEF2"
LAND_EDGE = "#C3CDD5"
PAPER = "#FBFCFD"
GOLD = "#D59B27"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 18,
        "axes.titleweight": "bold",
        "axes.labelcolor": INK,
        "text.color": INK,
        "axes.edgecolor": GRID,
        "axes.facecolor": PAPER,
        "figure.facecolor": PAPER,
        "savefig.facecolor": PAPER,
        "savefig.dpi": 220,
    }
)


def clean_axes(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0)


def footer(fig, text: str):
    fig.text(0.055, 0.025, text, fontsize=7.2, color=MUTED, ha="left", va="bottom")


def load_metrics():
    with (DATA / "q2_2026_cib_public_metrics.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_hubs():
    with (DATA / "europe_hubs_public.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def europe_polygons():
    with (DATA / "europe_countries.geojson").open(encoding="utf-8") as f:
        geo = json.load(f)
    patches = []
    names = []
    for feature in geo["features"]:
        geom = feature.get("geometry") or {}
        typ = geom.get("type")
        coords = geom.get("coordinates") or []
        if typ == "Polygon":
            parts = [coords]
        elif typ == "MultiPolygon":
            parts = coords
        else:
            continue
        for polygon in parts:
            if not polygon:
                continue
            # The first ring is the exterior. Country holes do not affect this
            # executive-scale map and are intentionally omitted.
            ring = polygon[0]
            if len(ring) >= 3:
                patches.append(Polygon(ring, closed=True))
                names.append(feature["properties"].get("name", ""))
    return patches, names


def build_map():
    fig, ax = plt.subplots(figsize=(14, 8.1))
    patches, names = europe_polygons()
    ax.add_collection(
        PatchCollection(
            patches,
            facecolor=LAND,
            edgecolor=LAND_EDGE,
            linewidth=0.45,
            zorder=1,
        )
    )
    ax.set_xlim(-11.5, 25.5)
    ax.set_ylim(36.0, 71.5)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    hubs = load_hubs()
    coords = {(r["city"], r["organization"]): (float(r["longitude"]), float(r["latitude"])) for r in hubs}
    # Draw the shared European network as understated arcs/links.
    for org, color in [("BNP Paribas", BNP), ("CACIB", CACIB)]:
        paris = coords.get(("Paris", org))
        if not paris:
            continue
        for (city, hub_org), point in coords.items():
            if hub_org != org or city == "Paris":
                continue
            ax.plot(
                [paris[0], point[0]],
                [paris[1], point[1]],
                color=color,
                alpha=0.14,
                linewidth=1.0,
                zorder=2,
            )

    # Highlight the two assignment comparison nodes.
    for city, ring_color, label in [
        ("Paris", BNP, ""),
        ("Luxembourg", GOLD, "LUXEMBOURG\nlocal node"),
    ]:
        point = coords.get((city, "BNP Paribas"))
        if point:
            ax.scatter(*point, s=440 if city == "Luxembourg" else 300, facecolors="none", edgecolors=ring_color,
                       linewidths=2.0, zorder=4)
            if label:
                dx, dy = (3.0, -2.1)
                ax.text(point[0] + dx, point[1] + dy, label, color=ring_color, fontsize=8.5,
                        weight="bold", ha="left", va="center", zorder=6,
                        bbox=dict(boxstyle="round,pad=0.28", facecolor=PAPER, edgecolor="none", alpha=0.94))

    # Offset overlapping markers so both banks remain visible.
    offsets = {"BNP Paribas": (-0.23, 0.14), "CACIB": (0.23, -0.14)}
    marker = {"BNP Paribas": "o", "CACIB": "D"}
    colors = {"BNP Paribas": BNP, "CACIB": CACIB}
    plotted_cities = set()
    for row in hubs:
        org = row["organization"]
        city = row["city"]
        x = float(row["longitude"]) + offsets[org][0]
        y = float(row["latitude"]) + offsets[org][1]
        ax.scatter(x, y, s=78, marker=marker[org], color=colors[org], edgecolor="white", linewidth=1.2, zorder=5)
        if city not in plotted_cities:
            # Keep labels clean: only label the core hubs used by the story.
            label_dx, label_dy = (0.42, 0.35)
            if city == "London": label_dx, label_dy = (-2.6, 0.55)
            if city == "Madrid": label_dx, label_dy = (-2.25, -0.8)
            if city == "Stockholm": label_dx, label_dy = (0.5, 0.55)
            if city == "Luxembourg": label_dx, label_dy = (0.42, 0.45)
            ax.text(float(row["longitude"]) + label_dx, float(row["latitude"]) + label_dy,
                    city, fontsize=8.8, color=INK, weight="bold", zorder=6)
            plotted_cities.add(city)

    # Two compact callouts make the map decision-useful rather than decorative.
    ax.add_patch(FancyBboxPatch((-10.8, 36.7), 9.5, 4.9, boxstyle="round,pad=0.35,rounding_size=0.18",
                                facecolor="white", edgecolor=GRID, linewidth=0.8, zorder=7))
    ax.text(-10.25, 41.0, "DIRECTOR TAKEAWAY", fontsize=8, color=CACIB, weight="bold", zorder=8)
    ax.text(-10.25, 39.25, "Paris is the shared anchor;\nLuxembourg is the local test case.",
            fontsize=10.5, color=INK, weight="bold", linespacing=1.45, zorder=8)

    ax.set_title("European CIB footprint — selected public hubs", loc="left", pad=15, color=INK)
    ax.text(-11.2, 70.7, "BNP Paribas and CACIB | presence shown by disclosed business-line / local-entity sources",
            fontsize=9.5, color=MUTED)
    legend = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=BNP, markeredgecolor="white", markersize=9,
               label="BNP Paribas (selected hubs)"),
        Line2D([0], [0], marker="D", color="none", markerfacecolor=CACIB, markeredgecolor="white", markersize=8,
               label="CACIB (selected hubs)"),
        Line2D([0], [0], marker="o", color=GOLD, markerfacecolor="none", markersize=10, label="Luxembourg comparison node"),
    ]
    ax.legend(handles=legend, loc="upper left", bbox_to_anchor=(0.01, 0.99), frameon=False, fontsize=8.8,
              handletextpad=0.6)
    footer(fig, "Sources: official BNP Paribas Securities Services locations; official CACIB business-line locations; CACIB Finance Luxembourg public report. Selected hubs ≠ exhaustive group footprint. See data/europe_hubs_public.csv.")
    fig.tight_layout(rect=(0, 0.055, 1, 0.96))
    path = OUT / "01_europe_cib_footprint.png"
    fig.savefig(path, dpi=240, bbox_inches="tight")
    return fig, path


def build_slope():
    fig, ax = plt.subplots(figsize=(12.5, 7.3))
    x0, x1 = 0, 1
    points = [
        ("BNP Paribas CIB", 112.7, BNP, "+12.7%"),
        ("CACIB — Corporate & Investment Banking*", 104.4, CACIB, "+4.4%"),
    ]
    for label, end, color, delta in points:
        ax.plot([x0, x1], [100, end], color=color, linewidth=3.2, solid_capstyle="round", zorder=3)
        ax.scatter([x0, x1], [100, end], s=[72, 150], color=["white", color], edgecolor=color,
                   linewidth=[2, 0.8], zorder=4)
        ax.text(x0 - 0.06, 100, "100", ha="right", va="center", fontsize=10, color=color, weight="bold")
        ax.text(x1 + 0.045, end, f"{end:.1f}  ({delta})", ha="left", va="center", fontsize=11, color=color, weight="bold")
        ax.text(0.34, 100 + (end - 100) * 0.52, label, color=color, fontsize=10, weight="bold",
                bbox=dict(boxstyle="round,pad=0.25", facecolor=PAPER, edgecolor="none", alpha=0.88))

    ax.axhline(100, color=GRID, linewidth=1.2, zorder=1)
    ax.set_xlim(-0.25, 1.34)
    ax.set_ylim(98, 115.3)
    ax.set_xticks([0, 1], ["Q2 2025", "Q2 2026"])
    ax.set_ylabel("Reported revenue index (Q2 2025 = 100)", labelpad=12)
    ax.grid(axis="y", color=GRID, linewidth=0.7, alpha=0.75)
    clean_axes(ax)
    ax.set_title("Q2 momentum — rebased to make the trend visible", loc="left", pad=16)
    ax.text(-0.24, 114.55, "The right question is momentum, not raw scale.", color=MUTED, fontsize=10)
    ax.text(0.98, 98.45, "↑ 4.4 pts", color=CACIB, ha="right", fontsize=8.5)
    ax.text(0.98, 99.12, "↑ 12.7 pts", color=BNP, ha="right", fontsize=8.5)
    footer(fig, "*Closest published comparison, not identical reporting perimeters: BNP CIB vs CACIB-related Corporate & Investment Banking. Q2 2025 = 100. Source: BNP Paribas 2Q26 results; CACIB Q2/H1 2026 results.")
    fig.tight_layout(rect=(0, 0.07, 1, 0.95))
    path = OUT / "02_q2_momentum_slope.png"
    fig.savefig(path, dpi=240, bbox_inches="tight")
    return fig, path


def build_dotplot():
    fig, ax = plt.subplots(figsize=(12.5, 8.1))
    rows = [
        ("BNP CIB — total", 12.7, BNP, True),
        ("Global Markets", 17.5, BNP_LIGHT, False),
        ("Securities Services", 17.5, BNP_LIGHT, False),
        ("Global Banking", 2.7, BNP_LIGHT, False),
        ("CACIB — CIB-related total*", 4.4, CACIB, True),
        ("Capital Markets & Investment Banking", 8.5, CACIB_LIGHT, False),
        ("Financing activities", 0.3, CACIB_LIGHT, False),
    ]
    ys = list(range(len(rows)))[::-1]
    for y, (label, value, color, total) in zip(ys, rows):
        ax.hlines(y, 0, value, color=color, linewidth=4.5 if total else 2.5, alpha=0.8, zorder=2)
        ax.scatter(value, y, s=155 if total else 95, color=color, edgecolor="white", linewidth=1.2, zorder=3)
        ax.text(value + 0.55, y, f"{value:+.1f}%", va="center", fontsize=10.5,
                color=color, weight="bold" if total else "normal")
    # group labels / separator
    ax.axhline(3.5, color=GRID, linewidth=1.2)
    ax.text(-5.5, 6.15, "BNP PARIBAS CIB", color=BNP, fontsize=9, weight="bold", va="center")
    ax.text(-5.5, 2.55, "CACIB / LARGE CUSTOMERS", color=CACIB, fontsize=9, weight="bold", va="center")
    ax.axvline(0, color=INK, linewidth=1.1)
    ax.set_xlim(-6.2, 21.0)
    ax.set_ylim(-0.65, 6.75)
    ax.set_yticks(ys, [r[0] for r in rows])
    ax.set_xlabel("Year-on-year revenue change, Q2 2026 vs Q2 2025", labelpad=11)
    ax.set_xticks([-5, 0, 5, 10, 15, 20])
    ax.grid(axis="x", color=GRID, linewidth=0.7, alpha=0.8)
    clean_axes(ax)
    ax.tick_params(axis="y", labelsize=9.4, pad=8)
    ax.set_title("Where the quarterly momentum comes from", loc="left", pad=16)
    ax.text(-6.15, 6.62, "Point estimates from official reporting — not a league table of group size.", color=MUTED, fontsize=10)
    footer(fig, "*CACIB figures use Crédit Agricole S.A. Large Customers / CIB-related published labels; BNP figures use BNP Paribas CIB labels. Source files and URLs are preserved in data/q2_2026_cib_public_metrics.csv.")
    fig.tight_layout(rect=(0, 0.07, 1, 0.95))
    path = OUT / "03_q2_business_engine_dotplot.png"
    fig.savefig(path, dpi=240, bbox_inches="tight")
    return fig, path


def build_luxembourg_matrix():
    """Show why the Luxembourg comparison needs a perimeter check first."""
    with (DATA / "luxembourg_perimeter.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    labels = [r["activity"] for r in rows]
    matrix = [[int(r["bnp_local"]), int(r["cacib_local"])] for r in rows]
    fig, ax = plt.subplots(figsize=(12.5, 8.3))
    cmap = ListedColormap(["#EEF2F5", BNP, GOLD])
    ax.imshow(matrix, cmap=cmap, vmin=0, vmax=2, aspect="auto")
    ax.set_xticks([0, 1], ["BNP Paribas Luxembourg\nCIB offer", "CACIB Finance Luxembourg S.A.\npublic issuer perimeter"])
    ax.set_yticks(range(len(labels)), labels)
    ax.tick_params(axis="x", labelsize=10, pad=12, length=0)
    ax.tick_params(axis="y", labelsize=9.8, pad=10, length=0)
    ax.set_xticks([x - 0.5 for x in range(1, 2)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, len(labels))], minor=True)
    ax.grid(which="minor", color="white", linewidth=2.2)
    ax.tick_params(which="minor", length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            symbol = "✓" if value == 1 else ("◆" if value == 2 else "—")
            color = "white" if value in (1, 2) else MUTED
            ax.text(j, i, symbol, ha="center", va="center", fontsize=17 if value else 15,
                    color=color, weight="bold")
    ax.set_title("Luxembourg: compare the perimeter before the performance", loc="left", pad=18)
    # The title carries the message; keep the area above the matrix uncluttered for slide use.
    legend = [
        Patch(facecolor=BNP, edgecolor="none", label="Explicitly disclosed in the local CIB offer"),
        Patch(facecolor=GOLD, edgecolor="none", label="Entity-specific activity: issuer / not full CIB platform"),
        Patch(facecolor="#EEF2F5", edgecolor="none", label="Not disclosed as an activity of this entity"),
    ]
    fig.legend(handles=legend, loc="lower center", bbox_to_anchor=(0.58, 0.095), frameon=False, fontsize=8.8,
               ncol=3, columnspacing=1.2, handlelength=1.2)
    footer(fig, "Sources: BNP Paribas Luxembourg CIB offer; public CACIB Finance Luxembourg documentation. Local financial reports exist, but the entity scopes are not equivalent. See data/luxembourg_perimeter.csv.")
    fig.subplots_adjust(left=0.31, right=0.98, bottom=0.22, top=0.80)
    path = OUT / "04_luxembourg_perimeter_heatmap.png"
    fig.savefig(path, dpi=240, bbox_inches="tight")
    return fig, path


def main():
    figures = []
    for builder in (build_map, build_slope, build_dotplot, build_luxembourg_matrix):
        fig, _ = builder()
        figures.append(fig)
    pdf_path = OUT / "CIB_EXECUTIVE_GRAPHS.pdf"
    with PdfPages(pdf_path) as pdf:
        for fig in figures:
            pdf.savefig(fig, bbox_inches="tight")
            plt.close(fig)
    print(f"Created {pdf_path}")
    for p in sorted(OUT.glob("*.png")):
        print(p)


if __name__ == "__main__":
    main()
