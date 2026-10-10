"""Build three candidate second-slide visuals for a five-minute CIB pitch.

Option 1 is quantitative performance, Option 2 is a Q1-to-Q2 double curve,
and Option 3 is an architecture flow. The flow uses equal-width links on
purpose: it explains the operating model and does not invent revenue weights.
"""
from __future__ import annotations

import csv
import shutil
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D
from matplotlib.backends.backend_pdf import PdfPages

from build_cib_graphs import (
    BNP, BNP_LIGHT, CACIB, CACIB_LIGHT, INK, MUTED, GRID, PAPER,
    build_dotplot,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "options"
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "text.color": INK,
    "figure.facecolor": PAPER,
    "savefig.facecolor": PAPER,
})


def footer(fig, text):
    fig.text(0.055, 0.025, text, fontsize=7.2, color=MUTED, ha="left", va="bottom")


def option_1_dotplot():
    # Reuse the validated director-ready dot plot and give it an option name.
    build_dotplot()
    source = ROOT / "output" / "03_q2_business_engine_dotplot.png"
    target = OUT / "OPTION_1_finance_committee_dotplot.png"
    shutil.copy2(source, target)
    return target


def option_2_double_curve():
    fig, axes = plt.subplots(1, 2, figsize=(15.4, 8.3), sharey=True,
                             gridspec_kw={"wspace": 0.08})
    with (ROOT / "data" / "q1_q2_2026_cib_metrics.csv").open(newline="", encoding="utf-8") as f:
        source_rows = list(csv.DictReader(f))

    def values(bank, metric):
        row = next(r for r in source_rows if r["bank"] == bank and r["metric"] == metric)
        return [float(row["q1_yoy_pct"]), float(row["q2_yoy_pct"])]

    panels = [
        (
            axes[0], "BNP PARIBAS CIB", BNP,
            [
                ("CIB total", values("BNP Paribas", "CIB total"), BNP, 3.8, True),
                ("Global Banking", values("BNP Paribas", "Global Banking"), BNP_LIGHT, 2.0, False),
                ("Global Markets", values("BNP Paribas", "Global Markets"), "#7FA8D2", 2.0, False),
                ("Securities Services", values("BNP Paribas", "Securities Services"), "#A7C5E2", 2.0, False),
            ],
        ),
        (
            axes[1], "CACIB / LARGE CUSTOMERS", CACIB,
            [
                ("CIB-related total", values("CACIB", "Corporate & Investment Banking"), CACIB, 3.8, True),
                ("Capital Markets & IB", values("CACIB", "Capital Markets & Investment Banking"), CACIB_LIGHT, 2.0, False),
                ("Financing activities", values("CACIB", "Financing activities"), "#8BD0C4", 2.0, False),
            ],
        ),
    ]
    for ax, title, color, series in panels:
        ax.axhline(0, color=INK, linewidth=1.1, zorder=1)
        for label, values, line_color, lw, total in series:
            ax.plot([0, 1], values, color=line_color, linewidth=lw, marker="o",
                    markersize=9 if total else 6, markeredgecolor="white", markeredgewidth=1.0,
                    solid_capstyle="round", zorder=3)
            ax.text(1.035, values[1], f"{values[1]:+.1f}%", va="center", ha="left",
                    color=line_color, fontsize=9.6, weight="bold" if total else "normal")
            ax.text(-0.035, values[0], f"{values[0]:+.1f}%", va="center", ha="right",
                    color=line_color, fontsize=8.4)
            # Label the line in the open middle of its trajectory.
            mid_y = (values[0] + values[1]) / 2
            ax.text(0.48, mid_y + (0.35 if total else 0), label, color=line_color,
                    fontsize=8.2, weight="bold" if total else "normal",
                    bbox=dict(boxstyle="round,pad=0.18", facecolor=PAPER, edgecolor="none", alpha=0.9))
        ax.set_xlim(-0.26, 1.37)
        ax.set_ylim(-12.0, 21.0)
        ax.set_xticks([0, 1], ["Q1 2026", "Q2 2026"])
        ax.grid(axis="y", color=GRID, linewidth=0.7, alpha=0.85)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color(GRID)
        ax.spines["bottom"].set_color(GRID)
        ax.tick_params(length=0, colors=MUTED)
        ax.set_title(title, loc="left", fontsize=12.5, color=color, weight="bold", pad=13)
    axes[0].set_ylabel("Revenue change vs same quarter prior year", labelpad=14)
    fig.suptitle("From Q1 headwinds to Q2 acceleration", x=0.055, y=0.965,
                 ha="left", fontsize=20, weight="bold", color=INK)
    fig.text(0.055, 0.925, "Double curve: the latest quarter changed the direction of the story", fontsize=9.5, color=MUTED)
    footer(fig, "BNP and CACIB reported categories are shown in separate panels; Q1 and Q2 are not treated as identical perimeters. BNP source: 1Q26 and 2Q26 results. CACIB source: Q1/H1 2026 results.")
    fig.subplots_adjust(left=0.075, right=0.93, bottom=0.09, top=0.86)
    path = OUT / "OPTION_2_q1_q2_double_curve.png"
    fig.savefig(path, dpi=240, bbox_inches="tight")
    plt.close(fig)
    return path


def node(ax, x, y, w, h, title, subtitle, color, title_size=9.5):
    ax.add_patch(FancyBboxPatch((x, y - h / 2), w, h,
                                boxstyle="round,pad=0.012,rounding_size=0.018",
                                facecolor="white", edgecolor=GRID, linewidth=0.8, zorder=3))
    ax.add_patch(FancyBboxPatch((x, y - h / 2), 0.012, h,
                                boxstyle="round,pad=0.002,rounding_size=0.008",
                                facecolor=color, edgecolor=color, zorder=4))
    ax.text(x + 0.026, y + 0.012, title, fontsize=title_size, weight="bold", color=color, zorder=5)
    if subtitle:
        ax.text(x + 0.026, y - 0.017, subtitle, fontsize=7.0, color=MUTED, zorder=5)


def arrow(ax, x1, y1, x2, y2, color, rad=0.0, alpha=0.58):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), connectionstyle=f"arc3,rad={rad}",
                                 arrowstyle="-|>", mutation_scale=11, linewidth=2.0,
                                 color=color, alpha=alpha, zorder=2))


def option_3_architecture_flow():
    fig, ax = plt.subplots(figsize=(15.4, 8.3))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Column headers create the reading direction without a flat table.
    ax.text(0.055, 0.89, "EUROPEAN HUBS", fontsize=9, weight="bold", color=MUTED)
    ax.text(0.405, 0.89, "CIB ACTIVITIES", fontsize=9, weight="bold", color=MUTED)
    ax.text(0.77, 0.89, "CLIENT SOLUTIONS", fontsize=9, weight="bold", color=MUTED)

    # BNP lane.
    ax.text(0.055, 0.82, "BNP PARIBAS CIB", fontsize=10.5, weight="bold", color=BNP)
    node(ax, 0.055, 0.74, 0.25, 0.095, "Paris · London · Frankfurt", "France / UK / DACH", BNP)
    node(ax, 0.055, 0.60, 0.25, 0.095, "Milan · Madrid · Luxembourg", "Italy / Iberia / local node", BNP)
    node(ax, 0.405, 0.74, 0.245, 0.095, "Global Banking", "financing · advisory · cash", BNP)
    node(ax, 0.405, 0.60, 0.245, 0.095, "Global Markets", "rates · FX · equities", BNP_LIGHT)
    node(ax, 0.405, 0.46, 0.245, 0.095, "Securities Services", "custody · clearing · servicing", BNP)
    node(ax, 0.77, 0.70, 0.19, 0.095, "Corporates", "funding + risk solutions", BNP)
    node(ax, 0.77, 0.55, 0.19, 0.095, "Financial institutions", "markets + post-trade", BNP)
    node(ax, 0.77, 0.40, 0.19, 0.095, "Investors / issuers", "access + infrastructure", BNP)
    for y1, y2, color in [(0.74, 0.74, BNP), (0.74, 0.60, BNP_LIGHT), (0.60, 0.46, BNP)]:
        arrow(ax, 0.305, y1, 0.395, y2, color, rad=0.06 if y1 != y2 else 0.0)
    for y1, y2 in [(0.74, 0.70), (0.60, 0.55), (0.46, 0.40)]:
        arrow(ax, 0.655, y1, 0.76, y2, BNP, rad=-0.04)

    # CACIB lane.
    ax.text(0.055, 0.305, "CACIB", fontsize=10.5, weight="bold", color=CACIB)
    node(ax, 0.055, 0.225, 0.25, 0.095, "Paris · London · Frankfurt", "France / UK / DACH", CACIB)
    node(ax, 0.055, 0.085, 0.25, 0.095, "Milan · Madrid · Stockholm", "Italy / Iberia / Nordics", CACIB)
    node(ax, 0.405, 0.225, 0.245, 0.095, "Financing activities", "structured + transaction banking", CACIB)
    node(ax, 0.405, 0.085, 0.245, 0.095, "Market activities", "origination · structuring · trading", CACIB_LIGHT)
    node(ax, 0.77, 0.225, 0.19, 0.095, "Corporates", "financing + cash", CACIB)
    node(ax, 0.77, 0.085, 0.19, 0.095, "Financial institutions / public sector", "capital markets + advisory", CACIB)
    arrow(ax, 0.305, 0.225, 0.395, 0.225, CACIB)
    arrow(ax, 0.305, 0.225, 0.395, 0.085, CACIB_LIGHT, rad=0.06)
    arrow(ax, 0.655, 0.225, 0.76, 0.225, CACIB)
    arrow(ax, 0.655, 0.085, 0.76, 0.085, CACIB_LIGHT)

    fig.suptitle("From European hubs to client solutions", x=0.055, y=0.965,
                 ha="left", fontsize=20, weight="bold", color=INK)
    fig.text(0.055, 0.925, "A visual operating model — not a revenue-weighted Sankey", fontsize=9.5, color=MUTED)
    footer(fig, "Sources: BNP Paribas CIB at a glance / EMEA; CACIB 2025 activity report. Equal-width links are intentional: this slide explains architecture, not volumes or market share.")
    fig.subplots_adjust(left=0.02, right=0.985, bottom=0.07, top=0.88)
    path = OUT / "OPTION_3_hubs_to_client_solutions.png"
    fig.savefig(path, dpi=240, bbox_inches="tight")
    plt.close(fig)
    return path


def main():
    paths = [option_1_dotplot(), option_2_double_curve(), option_3_architecture_flow()]
    pdf_path = OUT / "SECOND_SLIDE_OPTIONS.pdf"
    with PdfPages(pdf_path) as pdf:
        for path in paths:
            image = plt.imread(path)
            page = plt.figure(figsize=(15.4, 8.3))
            page_ax = page.add_axes([0, 0, 1, 1])
            page_ax.imshow(image)
            page_ax.axis("off")
            pdf.savefig(page, bbox_inches="tight", pad_inches=0)
            plt.close(page)
    print("Created candidate second-slide visuals:")
    for path in paths:
        print(path)
    print(pdf_path)


if __name__ == "__main__":
    main()
