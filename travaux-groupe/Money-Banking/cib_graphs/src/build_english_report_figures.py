"""Create two portrait report-ready English figure pages.

The approved graphs remain untouched; each page places one graph above a clear
English explanation in a consistent report style.
"""
from __future__ import annotations

import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle, FancyBboxPatch

from build_cib_graphs import INK, MUTED, GRID, PAPER, GOLD, CACIB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
MAP = OUT / "01_europe_cib_activity_map.png"
BUBBLE = OUT / "four_brand_comparator" / "FOUR_BRANDS_EXECUTIVE_BUBBLE.png"
REPORT_DIR = OUT / "english_report_figures"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "text.color": INK,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})


def paragraph(fig, x, y, text, width=125, fontsize=8.1, line_spacing=1.20):
    wrapped = textwrap.fill(text, width=width)
    fig.text(x, y, wrapped, ha="left", va="top", fontsize=fontsize, color=INK,
             linespacing=line_spacing)
    return y - 0.040 - 0.0155 * (wrapped.count("\n") + 1)


def report_page(section, report_title, graph_path, intro, paragraphs, takeaway, source_note, output_name):
    fig = plt.figure(figsize=(8.5, 11.0), facecolor="white")
    # Thin page frame keeps the two images visually consistent with a formal report.
    fig.add_artist(Rectangle((0.018, 0.018), 0.964, 0.964, transform=fig.transFigure,
                             fill=False, edgecolor="#C9D1D8", linewidth=0.8))
    fig.text(0.11, 0.955, section, fontsize=8.0, color=GOLD, weight="bold", ha="left")
    fig.text(0.11, 0.928, report_title, fontsize=17.0, color=INK, weight="bold", ha="left")
    fig.text(0.11, 0.895, intro, fontsize=8.3, color=MUTED, ha="left", style="italic")

    # The source graph is kept intact: no logos, axes or values are redrawn.
    image_ax = fig.add_axes([0.055, 0.485, 0.89, 0.385])
    image_ax.imshow(plt.imread(graph_path), aspect="auto")
    image_ax.axis("off")

    fig.text(0.11, 0.455, "Explanation", fontsize=10.2, color=CACIB, weight="bold", ha="left")
    y = 0.423
    for item in paragraphs:
        y = paragraph(fig, 0.11, y, item)
    fig.add_artist(FancyBboxPatch((0.10, 0.095), 0.80, 0.105,
                                   transform=fig.transFigure,
                                   boxstyle="round,pad=0.008,rounding_size=0.012",
                                   facecolor="#F0F5F9", edgecolor="none", zorder=0))
    fig.text(0.125, 0.172, "Key takeaway", fontsize=7.1, color=GOLD, weight="bold", ha="left")
    fig.text(0.125, 0.145, textwrap.fill(takeaway, width=91), fontsize=8.6,
             color=INK, weight="bold", ha="left", va="top", linespacing=1.2)
    fig.text(0.11, 0.058, source_note, fontsize=6.2, color=MUTED, ha="left", va="bottom")
    page_number = "2" if section.startswith("1.2") else "1"
    fig.text(0.89, 0.035, page_number, fontsize=7.5, color=MUTED, ha="right")

    path = REPORT_DIR / output_name
    fig.savefig(path, dpi=210, bbox_inches="tight", pad_inches=0.08)
    return fig, path


def main():
    if not MAP.exists() or not BUBBLE.exists():
        raise FileNotFoundError("Approved source graph is missing")

    map_page, map_png = report_page(
        "1.1  EUROPEAN FOOTPRINT",
        "Figure 1. European CIB footprint and platform architecture",
        MAP,
        "European network and publicly documented activity hubs.",
        [
            "The map presents a selected public footprint of BNP Paribas CIB and Crédit Agricole CIB across Europe. Its purpose is to establish the geographic context before the comparative view: Paris acts as a central reference point, while London, Frankfurt, Milan, Madrid, Stockholm and Luxembourg illustrate selected regional locations documented in public business-line sources.",
            "The right-hand architecture distinguishes BNP Paribas CIB's Global Banking, Global Markets and Securities Services from CACIB's Financing Activities, Market Activities and Investment Banking. These are operating capabilities, not revenue categories or market-share scores.",
            "The map should therefore be read as a selected public network, not as an exhaustive legal-entity map. City markers, links and activity cards do not represent revenue, booked volume, exclusivity or legal booking location.",
        ],
        "Use the map to answer where the platforms operate; use the following bubble chart to discuss who they serve and how broad the public offer appears.",
        "Source: approved project map and public BNP Paribas CIB / CACIB business-line sources. Perimeter limitations are documented in cib_graphs/README.md.",
        "01_european_cib_footprint_report_en.png",
    )
    plt.close(map_page)

    bubble_page, bubble_png = report_page(
        "1.2  EXECUTIVE COMPARATOR",
        "Figure 2. Four franchises: client reach, offer breadth and operating weight",
        BUBBLE,
        "Comparative positioning based on publicly available information.",
        [
            "The chart compares four public franchise signals: BNP CIB France, CACIB France, CACEIS Luxembourg and BNP CIB Luxembourg. The horizontal reading moves from a specialist offer to a broad offer; the vertical bands move from a local signal to a group platform. This categorical design avoids false precision and is intended to be understandable in a few seconds.",
            "The client figure written next to each bubble is the publicly quantified reach when a source discloses it. Bubble area is an operating-weight signal based on public staff figures; it is not revenue, assets, market share or client value. The cards on the right identify the core product offer behind each point.",
            "BNP CIB Luxembourg is marked N/D because the local public page does not disclose a local client count. CACEIS is also qualified because the reported 240+ client perimeter extends beyond Luxembourg to Continental Europe and offshore platforms. These observations are therefore a positioning view, not a four-way league table.",
        ],
        "BNP CIB and CACIB represent broad group platforms; CACEIS is a specialised asset-servicing platform; BNP CIB Luxembourg is a focused local CIB offer.",
        "Source: approved project bubble chart. Underlying signals and source URLs: data/four_brand_bubble_metrics.csv.",
        "02_four_franchises_bubble_report_en.png",
    )
    plt.close(bubble_page)

    pdf_path = OUT / "CIB_FRANCE_LUXEMBOURG_REPORT_FIGURES_EN.pdf"
    with PdfPages(pdf_path) as pdf:
        for source in [map_png, bubble_png]:
            image = plt.imread(source)
            page = plt.figure(figsize=(8.5, 11.0), facecolor="white")
            ax = page.add_axes([0, 0, 1, 1])
            ax.imshow(image)
            ax.axis("off")
            pdf.savefig(page, bbox_inches="tight", pad_inches=0)
            plt.close(page)
    print(map_png)
    print(bubble_png)
    print(pdf_path)


if __name__ == "__main__":
    main()
