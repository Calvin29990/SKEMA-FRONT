"""Build two report-ready English figures from the approved map and bubble chart."""
from __future__ import annotations

from pathlib import Path
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch

from build_cib_graphs import INK, MUTED, GRID, PAPER, GOLD, CACIB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
REPORT_OUT = OUT / "report_en"
REPORT_OUT.mkdir(parents=True, exist_ok=True)
MAP = OUT / "01_europe_cib_activity_map.png"
BUBBLE = OUT / "four_brand_comparator" / "FOUR_BRANDS_EXECUTIVE_BUBBLE.png"
PDF = REPORT_OUT / "CIB_REPORT_FIGURES_EN.pdf"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "figure.facecolor": PAPER,
    "savefig.facecolor": PAPER,
})


def draw_report_page(graph_path, figure_label, page_no, intro, bullets, takeaway, sources, out_path):
    # A4 portrait, deliberately matching the report-style example supplied by the user.
    fig = plt.figure(figsize=(8.27, 11.69))
    fig.text(0.07, 0.965, "MONEY & BANKING · CIB BENCHMARK", fontsize=7.0, color=MUTED, weight="bold")
    fig.text(0.93, 0.965, f"{page_no}/2", fontsize=7.0, color=GOLD, weight="bold", ha="right")
    fig.text(0.07, 0.925, figure_label, fontsize=15.2, color=INK, weight="bold", va="top")
    fig.text(0.07, 0.892, "Report-ready figure · public sources · illustrative perimeter", fontsize=7.7, color=MUTED)

    graph_ax = fig.add_axes([0.07, 0.515, 0.86, 0.34])
    graph_ax.imshow(plt.imread(graph_path), aspect="auto")
    graph_ax.axis("off")
    for spine in graph_ax.spines.values():
        spine.set_visible(True)
        spine.set_color(GRID)
        spine.set_linewidth(0.7)

    # Explanation block below the visual.
    ax = fig.add_axes([0.07, 0.105, 0.86, 0.35])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.012,rounding_size=0.018",
                                facecolor="#F0F5F9", edgecolor="none"))
    ax.text(0.045, 0.91, "HOW TO READ THE FIGURE", fontsize=7.2, color=GOLD, weight="bold")
    y = 0.80
    intro_lines = textwrap.fill(intro, width=91)
    ax.text(0.045, y, intro_lines, fontsize=8.0, color=INK, va="top", linespacing=1.35)
    y -= 0.15 if len(intro_lines.splitlines()) <= 2 else 0.21
    for bullet in bullets:
        line = textwrap.fill("• " + bullet, width=91, subsequent_indent="  ")
        ax.text(0.045, y, line, fontsize=7.5, color=INK, va="top", linespacing=1.3)
        y -= 0.105 if len(line.splitlines()) == 1 else 0.15
    ax.add_patch(FancyBboxPatch((0.045, 0.07), 0.91, 0.16, boxstyle="round,pad=0.010,rounding_size=0.012",
                                facecolor="white", edgecolor=GRID, linewidth=0.7))
    ax.text(0.065, 0.19, "EXECUTIVE TAKEAWAY", fontsize=6.5, color=CACIB, weight="bold")
    ax.text(0.065, 0.145, textwrap.fill(takeaway, width=102), fontsize=8.1, color=INK, weight="bold", va="top")

    fig.text(0.07, 0.055, textwrap.fill("Sources and scope: " + sources, width=130), fontsize=5.9, color=MUTED, va="bottom")
    fig.savefig(out_path, dpi=220, bbox_inches="tight", pad_inches=0.06)
    return fig


def main():
    if not MAP.exists() or not BUBBLE.exists():
        raise FileNotFoundError("Approved source graph is missing")
    map_png = REPORT_OUT / "FIGURE_01_EUROPEAN_CIB_FOOTPRINT_EN.png"
    bubble_png = REPORT_OUT / "FIGURE_02_FOUR_FRANCHISES_BUBBLE_EN.png"

    pages = []
    pages.append(draw_report_page(
        MAP,
        "Figure 1. European CIB footprint and platform architecture",
        "1",
        "This figure introduces the geographic and business architecture of the comparison. It combines selected publicly documented hubs for BNP Paribas CIB and CACIB with the main activity engines shown in public business-line materials.",
        [
            "Dots and city labels represent selected public hub signals, not an exhaustive legal-entity footprint.",
            "The right-hand architecture separates financing, markets and securities services; it is a capability map rather than a revenue chart.",
            "Links and highlighted nodes are directional reading aids only: they do not represent transaction volumes, revenue or booking location.",
        ],
        "The European platform is connected, but Paris and Luxembourg must remain separate in the next comparison because the public sources do not evidence identical local perimeters.",
        "BNP Paribas CIB and CACIB public business-line pages; selected hub sources listed in data/europe_hubs_public.csv; the project README states the perimeter limits.",
        map_png,
    ))
    pages.append(draw_report_page(
        BUBBLE,
        "Figure 2. Four franchises: client reach, offer breadth and operating weight",
        "2",
        "This executive bubble chart focuses the comparison on four anchors: BNP CIB France, CACIB France, CACEIS Luxembourg and BNP CIB Luxembourg.",
        [
            "Left to right means a narrower or broader publicly named offer; this is a qualitative positioning axis, not a performance score.",
            "The vertical bands distinguish a local signal, public local reach and a group platform; the large labels retain the public client signal where it exists.",
            "Bubble size uses public staff signals as a visual proxy for operating weight; N/D means that the local client count is not publicly disclosed. Neither is revenue, assets, market share or client value."
        ],
        "BNP CIB and CACIB read as broad group platforms; CACEIS reads as specialised asset servicing; BNP CIB Luxembourg reads as a focused local CIB offer.",
        "BNP CIB at a glance and 2026 At a Glance; CACIB 2025 key figures; BNP Paribas Luxembourg CIB page; CACEIS Luxembourg Investor Services report. See data/four_brand_bubble_metrics.csv.",
        bubble_png,
    ))

    with PdfPages(PDF) as pdf:
        for fig in pages:
            pdf.savefig(fig, bbox_inches="tight", pad_inches=0.06)
            plt.close(fig)
    print(PDF)
    print(map_png)
    print(bubble_png)


if __name__ == "__main__":
    main()
