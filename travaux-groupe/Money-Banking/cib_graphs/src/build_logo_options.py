"""Marketing-finance visuals with client and bank logo anchors.

The case studies are public references, not claims of a complete client
portfolio. The graphics use logos as visual signposts and keep the transaction
source and perimeter visible in the footers.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge
from matplotlib.lines import Line2D
from matplotlib.backends.backend_pdf import PdfPages

from build_cib_graphs import BNP, BNP_LIGHT, CACIB, CACIB_LIGHT, INK, MUTED, GRID, PAPER

ROOT = Path(__file__).resolve().parents[1]
LOGOS = ROOT / "data" / "logos"
OUT = ROOT / "output" / "marketing_options"
OUT.mkdir(parents=True, exist_ok=True)

ORANGE = "#F4A81D"
RED = "#E04B4B"
PURPLE = "#6956A5"
DARK = "#172B4D"
LIGHT_BLUE = "#DDEAF5"
LIGHT_GREEN = "#DDF0EA"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "text.color": INK,
    "figure.facecolor": PAPER,
    "savefig.facecolor": PAPER,
})


SOURCE_LINE = (
    "Sources: [S1] https://securities.cib.bnpparibas/bnp-paribas-janus-henderson-core-banking-fund-servicing-europe-asia-pacific/ | "
    "[S2] https://securities.cib.bnpparibas/unicredit-mandate-custody-and-settlement-services/ | "
    "[S3] https://activity-report.ca-cib.com/market-activities/ | "
    "[S4] https://activity-report.ca-cib.com/loccitane-group-transaction/ | "
    "[H1] https://securities.cib.bnpparibas/who-we-are/our-locations/ | "
    "[H2] https://www.ca-cib.com/en/expertise/solutions-support-your-financing-strategy/supporting-your-financing-needs/leveraged-0"
)


def footer(fig, text):
    fig.text(0.045, 0.039, "PUBLIC EXAMPLES / ILLUSTRATIVE / NOT EXHAUSTIVE  •  " + text,
             fontsize=6.4, color=MUTED, ha="left", va="bottom")
    fig.text(0.045, 0.019, SOURCE_LINE, fontsize=4.9, color=MUTED, ha="left", va="bottom")


def trim_alpha(image):
    if image.ndim == 3 and image.shape[-1] == 4:
        alpha = image[:, :, 3]
        ys, xs = (alpha > 0.06).nonzero()
        if len(xs):
            image = image[max(0, ys.min() - 4):ys.max() + 5, max(0, xs.min() - 4):xs.max() + 5]
    return image


def logo(path):
    image = mpimg.imread(path)
    image = trim_alpha(image)
    # The CACIB image is a white-background square. Crop the white canvas so
    # the actual corporate mark has the same visual weight as the other logos.
    if Path(path).stem == "cacib" and image.ndim == 3:
        rgb = image[:, :, :3]
        mask = np.any(rgb < 0.96, axis=2)
        ys, xs = mask.nonzero()
        if len(xs):
            image = image[max(0, ys.min() - 8):ys.max() + 9, max(0, xs.min() - 8):xs.max() + 9]
    return image


def put_logo(ax, path, x, y, zoom=0.12, box_color="white", box_edge=GRID, box=(0.15, 0.10)):
    # A logo badge is more legible than dropping a raw logo onto the canvas.
    w, h = box
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0.008,rounding_size=0.018",
                                facecolor=box_color, edgecolor=box_edge, linewidth=0.9, zorder=4))
    image = logo(path)
    ab = AnnotationBbox(OffsetImage(image, zoom=zoom), (x, y), frameon=False, zorder=6)
    ax.add_artist(ab)


def bank_card(ax, x, y, w, h, bank, logo_path, color, subtitle):
    ax.add_patch(FancyBboxPatch((x, y - h / 2), w, h,
                                boxstyle="round,pad=0.012,rounding_size=0.02",
                                facecolor=color, edgecolor=color, linewidth=1.0, zorder=3))
    # Bank logos are predominantly light in the source assets; use a dark BNP
    # card and a white CACIB card for contrast.
    if bank == "BNP":
        put_logo(ax, logo_path, x + 0.095, y, zoom=0.038, box_color=color, box_edge=color, box=(0.145, 0.075))
        ax.text(x + 0.185, y + 0.012, "CIB PLATFORM", color="white", fontsize=9.6, weight="bold", zorder=7)
        ax.text(x + 0.185, y - 0.024, subtitle, color="#DCEBFA", fontsize=7.0, zorder=7)
    else:
        ax.add_patch(FancyBboxPatch((x, y - h / 2), w, h,
                                    boxstyle="round,pad=0.012,rounding_size=0.02",
                                    facecolor="white", edgecolor=color, linewidth=2.0, zorder=3))
        put_logo(ax, logo_path, x + 0.095, y, zoom=0.14, box_color="white", box_edge="white", box=(0.145, 0.075))
        ax.text(x + 0.185, y + 0.012, "CIB PLATFORM", color=color, fontsize=9.5, weight="bold", zorder=7)
        ax.text(x + 0.185, y - 0.024, subtitle, color=MUTED, fontsize=7.0, zorder=7)


def pill(ax, x, y, w, label, color, icon, text_color="white"):
    ax.add_patch(FancyBboxPatch((x, y - 0.027), w, 0.054,
                                boxstyle="round,pad=0.008,rounding_size=0.027",
                                facecolor=color, edgecolor=color, zorder=3))
    ax.add_patch(Circle((x + 0.027, y), 0.017, facecolor="white", edgecolor="none", zorder=4))
    ax.text(x + 0.027, y - 0.001, icon, ha="center", va="center", fontsize=7.0,
            color=color, weight="bold", zorder=5)
    ax.text(x + 0.053, y, label, va="center", fontsize=7.7, color=text_color, weight="bold", zorder=5)


def arrow(ax, start, end, color, rad=0.0, lw=2.0):
    ax.add_patch(FancyArrowPatch(start, end, connectionstyle=f"arc3,rad={rad}",
                                 arrowstyle="-|>", mutation_scale=12, linewidth=lw,
                                 color=color, alpha=0.78, zorder=2))


def client_card(ax, x, y, w, h, logo_path, name, detail, accent, image_box="white"):
    ax.add_patch(FancyBboxPatch((x, y - h / 2), w, h,
                                boxstyle="round,pad=0.012,rounding_size=0.018",
                                facecolor=image_box, edgecolor=accent, linewidth=1.4, zorder=3))
    logo_zoom = 0.060 if name == "Enel Finance" else (0.034 if name != "L'Occitane" else 0.045)
    put_logo(ax, logo_path, x + 0.105, y + 0.022, zoom=logo_zoom,
             box_color=image_box, box_edge=image_box, box=(0.17, 0.065))
    ax.text(x + 0.205, y + 0.028, name, fontsize=9.4, weight="bold", color=accent, zorder=6)
    ax.text(x + 0.205, y - 0.006, detail, fontsize=6.8, color=MUTED, zorder=6)


def option_1_deal_ecosystem():
    fig, ax = plt.subplots(figsize=(15.4, 8.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.suptitle("CIB in action — from platform to client outcome", x=0.045, y=0.965,
                 ha="left", fontsize=20, weight="bold", color=INK)
    fig.text(0.045, 0.925, "Selected public transactions turn the European footprint into a visible client franchise", fontsize=9.5, color=MUTED)

    # BNP lane
    ax.text(0.045, 0.835, "BNP PARIBAS CIB", color=BNP, fontsize=10.5, weight="bold")
    ax.text(0.045, 0.805, "SELECTED PUBLIC HUBS  ·  PARIS / LONDON / LUXEMBOURG", color=MUTED, fontsize=6.5, weight="bold")
    bank_card(ax, 0.04, 0.735, 0.23, 0.105, "BNP", LOGOS / "bnp-paribas.png", BNP, "multi-local platform")
    pill(ax, 0.34, 0.79, 0.22, "FUND SERVICING", BNP, "F")
    pill(ax, 0.34, 0.68, 0.22, "CUSTODY + SETTLEMENT", BNP_LIGHT, "C")
    client_card(ax, 0.70, 0.79, 0.255, 0.105, LOGOS / "janus-henderson.png", "Janus Henderson", "UK / FR / LUX / AU · fund servicing", BNP, "white")
    client_card(ax, 0.70, 0.68, 0.255, 0.105, LOGOS / "unicredit.png", "UniCredit", "IT / DE / LUX · custody + settlement", BNP, DARK)
    arrow(ax, (0.275, 0.755), (0.33, 0.79), BNP)
    arrow(ax, (0.275, 0.715), (0.33, 0.68), BNP_LIGHT)
    arrow(ax, (0.57, 0.79), (0.685, 0.79), BNP)
    arrow(ax, (0.57, 0.68), (0.685, 0.68), BNP_LIGHT)

    # CACIB lane
    ax.text(0.045, 0.485, "CACIB", color=CACIB, fontsize=10.5, weight="bold")
    ax.text(0.045, 0.455, "SELECTED PUBLIC HUBS  ·  PARIS / LONDON / MILAN", color=MUTED, fontsize=6.5, weight="bold")
    bank_card(ax, 0.04, 0.385, 0.23, 0.105, "CACIB", LOGOS / "cacib.png", CACIB, "capital markets + financing")
    pill(ax, 0.34, 0.44, 0.22, "BOND / DCM", CACIB, "B")
    pill(ax, 0.34, 0.33, 0.22, "FINANCING + ADVISORY", CACIB_LIGHT, "€")
    client_card(ax, 0.70, 0.44, 0.255, 0.105, LOGOS / "enel-green-power.png", "Enel Finance", "USD markets · USD 4.5bn bond", CACIB, "white")
    client_card(ax, 0.70, 0.33, 0.255, 0.105, LOGOS / "loccitane.png", "L'Occitane Group", "HK delisting · financing + quasi-equity", CACIB, "#FFF1C9")
    arrow(ax, (0.275, 0.405), (0.33, 0.44), CACIB)
    arrow(ax, (0.275, 0.365), (0.33, 0.33), CACIB_LIGHT)
    arrow(ax, (0.57, 0.44), (0.685, 0.44), CACIB)
    arrow(ax, (0.57, 0.33), (0.685, 0.33), CACIB_LIGHT)

    # Bottom message strip.
    ax.add_patch(FancyBboxPatch((0.04, 0.12), 0.91, 0.095,
                                boxstyle="round,pad=0.012,rounding_size=0.018",
                                facecolor="#F4F7FA", edgecolor=GRID, linewidth=0.8))
    ax.text(0.065, 0.176, "DIRECTOR TAKEAWAY", fontsize=8.5, color=ORANGE, weight="bold")
    ax.text(0.065, 0.142, "CIB is not a product list: it converts a regional platform into financing, market access and post-trade outcomes.",
            fontsize=10.2, color=INK, weight="bold")
    footer(fig, "BNP Paribas–Janus Henderson / UniCredit mandates; CACIB–Enel / L'Occitane transactions. Logos are visual anchors, not revenue evidence.")
    fig.subplots_adjust(left=0.02, right=0.985, bottom=0.07, top=0.88)
    path = OUT / "OPTION_1_deal_ecosystem_logos.png"
    fig.savefig(path, dpi=240, bbox_inches="tight")
    plt.close(fig)
    return path


def result_card(ax, x, y, w, h, bank, title, detail, color):
    ax.add_patch(FancyBboxPatch((x, y - h / 2), w, h,
                                boxstyle="round,pad=0.012,rounding_size=0.018",
                                facecolor="white", edgecolor=color, linewidth=1.3, zorder=3))
    ax.text(x + 0.025, y + h / 2 - 0.027, bank.upper() + "  /  PUBLIC RESULT", fontsize=6.3,
            color=color, weight="bold", zorder=6)
    ax.text(x + 0.025, y + 0.005, title, fontsize=8.2, color=INK, weight="bold", zorder=6)
    ax.text(x + 0.025, y - 0.029, detail, fontsize=6.6, color=MUTED, zorder=6)


def option_2_client_solution_journey():
    fig, ax = plt.subplots(figsize=(15.4, 8.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig.suptitle("Client need → CIB solution → public result", x=0.045, y=0.965,
                 ha="left", fontsize=20, weight="bold", color=INK)
    fig.text(0.045, 0.925, "A four-step journey: the logo starts the story, the product explains the economics, the case makes it verifiable", fontsize=9.5, color=MUTED)

    # Column headers create a clear narrative without turning the slide into a table.
    ax.text(0.055, 0.855, "CLIENT / NEED", fontsize=8.5, color=INK, weight="bold")
    ax.text(0.38, 0.855, "CIB SOLUTION", fontsize=8.5, color=ORANGE, weight="bold")
    ax.text(0.695, 0.855, "PUBLIC RESULT / SCOPE", fontsize=8.5, color=INK, weight="bold")
    ax.add_patch(FancyBboxPatch((0.34, 0.155), 0.01, 0.64, boxstyle="round,pad=0.001,rounding_size=0.003",
                                facecolor=GRID, edgecolor=GRID, linewidth=0, zorder=1))
    ax.add_patch(FancyBboxPatch((0.655, 0.155), 0.01, 0.64, boxstyle="round,pad=0.001,rounding_size=0.003",
                                facecolor=GRID, edgecolor=GRID, linewidth=0, zorder=1))

    rows = [
        (0.75, LOGOS / "janus-henderson.png", "Janus Henderson", "operating-model transformation", BNP, "FUND SERVICING", "FUND", "Mandate across selected UK, France, Luxembourg and Australia markets", "fund accounting, depositary, custody, cash and FX"),
        (0.60, LOGOS / "unicredit.png", "UniCredit", "back-office optimisation", BNP, "CUSTODY + SETTLEMENT", "CUSTODY", "Selected entities in Italy, Germany and Luxembourg", "local / global custody, clearing and settlement"),
        (0.45, LOGOS / "enel-green-power.png", "Enel Finance", "funding diversification", CACIB, "BOND / DCM", "BOND", "USD 4.5bn multi-tranche senior unsecured bond", "four maturities; joint bookrunner in Sep. 2025"),
        (0.30, LOGOS / "loccitane.png", "L'Occitane Group", "delisting + growth financing", CACIB, "FINANCING + ADVISORY", "€", "€1.36bn acquisition/refinancing facilities", "financial adviser for up to €1.6bn quasi-equity raise"),
    ]
    for y, logo_path, name, need, color, product, icon, result, detail in rows:
        image_box = DARK if name == "UniCredit" else ("#FFF1C9" if name == "L'Occitane Group" else "white")
        client_card(ax, 0.05, y, 0.255, 0.105, logo_path, name, need, color, image_box)
        pill(ax, 0.385, y, 0.235, product, color if color in (BNP, CACIB) else color, icon[0])
        result_card(ax, 0.695, y, 0.255, 0.105, "BNP Paribas" if color == BNP else "CACIB", result, detail, color)
        arrow(ax, (0.31, y), (0.375, y), color, lw=1.8)
        arrow(ax, (0.625, y), (0.685, y), color, lw=1.8)

    ax.add_patch(FancyBboxPatch((0.05, 0.115), 0.90, 0.075,
                                boxstyle="round,pad=0.012,rounding_size=0.018",
                                facecolor="#F4F7FA", edgecolor=GRID, linewidth=0.8))
    ax.text(0.075, 0.157, "EXECUTIVE MESSAGE", fontsize=8.2, color=ORANGE, weight="bold")
    ax.text(0.075, 0.132, "The commercial story is a chain: client problem → CIB capability → observable public mandate or transaction.",
            fontsize=9.8, color=INK, weight="bold")
    footer(fig, "One public case per row; mandate scope and transaction type are shown, not revenue, market share or total client coverage.")
    fig.subplots_adjust(left=0.02, right=0.985, bottom=0.07, top=0.88)
    path = OUT / "OPTION_2_client_solution_journey_logos.png"
    fig.savefig(path, dpi=240, bbox_inches="tight")
    plt.close(fig)
    return path


def option_3_risk_product_map():
    fig, ax = plt.subplots(figsize=(15.4, 8.5))
    ax.set_facecolor(PAPER)
    ax.set_xlim(-0.4, 10.8)
    ax.set_ylim(-0.5, 10.4)
    ax.set_xticks([0, 2.5, 5, 7.5, 10], ["Low", "", "Medium", "", "High"])
    ax.set_yticks([0, 2.5, 5, 7.5, 10], ["Low", "", "Medium", "", "High"])
    ax.set_xlabel("Balance-sheet / capital intensity", labelpad=10)
    ax.set_ylabel("Market + operational complexity", labelpad=10)
    ax.grid(color=GRID, linewidth=0.8, alpha=0.8)
    ax.axvline(5, color=GRID, linewidth=0.9)
    ax.axhline(5, color=GRID, linewidth=0.9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(length=0, colors=MUTED)
    fig.suptitle("CIB solutions carry different economic and risk signatures", x=0.045, y=0.965,
                 ha="left", fontsize=20, weight="bold", color=INK)
    fig.text(0.045, 0.925, "A marketing-finance map: the client logo makes the abstract risk channel tangible", fontsize=9.5, color=MUTED)

    # Quadrant captions.
    ax.text(0.35, 9.65, "MARKETS / CAPITAL MARKETS", fontsize=8.2, color=CACIB, weight="bold")
    ax.text(0.35, 0.45, "SERVICE / POST-TRADE", fontsize=8.2, color=BNP, weight="bold")
    ax.text(7.0, 9.65, "STRUCTURED FINANCE / ADVISORY", fontsize=8.2, color=CACIB, weight="bold")
    ax.text(7.0, 0.45, "FLOW BANKING", fontsize=8.2, color=BNP, weight="bold")

    # Product bubbles: position is a qualitative economic map, not a measured risk score.
    cases = [
        ("Enel Finance", "BOND", LOGOS / "enel-green-power.png", 4.2, 8.1, CACIB, "market access"),
        ("L'Occitane", "LOAN", LOGOS / "loccitane.png", 7.8, 8.0, CACIB, "acquisition finance"),
        ("Janus Henderson", "FUND", LOGOS / "janus-henderson.png", 2.1, 7.1, BNP, "fund servicing"),
        ("UniCredit", "CUSTODY", LOGOS / "unicredit.png", 1.7, 5.4, BNP, "settlement + custody"),
    ]
    for name, product, logo_path, x, y, color, descriptor in cases:
        ax.scatter(x, y, s=720, color="white", edgecolor=color, linewidth=3.0, zorder=4)
        image = logo(logo_path)
        bubble_zoom = 0.055 if name == "Enel Finance" else (0.030 if name != "L'Occitane" else 0.038)
        ab = AnnotationBbox(OffsetImage(image, zoom=bubble_zoom), (x, y + 0.18), frameon=False, zorder=6)
        ax.add_artist(ab)
        ax.text(x, y - 0.43, name, ha="center", fontsize=8.4, weight="bold", color=color, zorder=7)
        ax.text(x, y - 0.72, f"{product}  ·  {descriptor}", ha="center", fontsize=7.0, color=MUTED, zorder=7)

    # Center legend / reading rule.
    ax.add_patch(FancyBboxPatch((7.55, 1.20), 2.65, 2.55,
                                boxstyle="round,pad=0.02,rounding_size=0.15",
                                facecolor="#F4F7FA", edgecolor=GRID, linewidth=0.8, zorder=2))
    ax.text(7.78, 3.25, "Financing → balance sheet\nMarkets → risk capacity\nSecurities Services → operational excellence",
            fontsize=9.0, color=INK, weight="bold", linespacing=1.65)
    footer(fig, "Qualitative teaching map, not a regulatory risk rating or measured portfolio; examples span custody, servicing, bond and financing.")
    fig.subplots_adjust(left=0.08, right=0.96, bottom=0.09, top=0.88)
    path = OUT / "OPTION_3_risk_product_map_logos.png"
    fig.savefig(path, dpi=240, bbox_inches="tight")
    plt.close(fig)
    return path


def build_comparison_pdf(paths):
    pdf_path = OUT / "MARKETING_FINANCE_OPTIONS.pdf"
    with PdfPages(pdf_path) as pdf:
        for path in paths:
            image = mpimg.imread(path)
            height, width = image.shape[:2]
            fig = plt.figure(figsize=(15.4, 15.4 * height / width), facecolor=PAPER)
            ax = fig.add_axes([0, 0, 1, 1])
            ax.imshow(image)
            ax.axis("off")
            pdf.savefig(fig, dpi=180)
            plt.close(fig)
    return pdf_path


def main():
    paths = [option_1_deal_ecosystem(), option_2_client_solution_journey(), option_3_risk_product_map()]
    pdf_path = build_comparison_pdf(paths)
    print("Created marketing-finance logo visuals:")
    for path in paths:
        print(path)
    print(pdf_path)


if __name__ == "__main__":
    main()
