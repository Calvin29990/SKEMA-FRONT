"""Create polished Chapter 10 visuals: diagrams and a data-backed combo chart."""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ch10_front_office_illustrations" / "output"
OUT.mkdir(parents=True, exist_ok=True)

BG = "#F8F6F0"
NAVY = "#172B4D"
INK = "#243447"
MUTED = "#667085"
LINE = "#D8DEE8"
WHITE = "#FFFFFF"
BLUE = "#2F68A7"
TEAL = "#08A5A5"
MAGENTA = "#A83C6D"
GOLD = "#D6A33A"
CORAL = "#D96C61"
PALE_BLUE = "#EAF3F8"
PALE_TEAL = "#E8F5F3"
PALE_MAGENTA = "#F8EEF5"
PALE_GOLD = "#FBF4DD"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "figure.facecolor": BG,
    "savefig.facecolor": BG,
})


def setup(title: str, subtitle: str):
    fig = plt.figure(figsize=(16, 9), facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.text(0.55, 8.47, "CHAPTER 10  ·  THE BANKING BUSINESS", fontsize=9, color=TEAL, weight="bold")
    ax.text(15.45, 8.47, "FRONT OFFICE LENS", fontsize=8, color=MUTED, weight="bold", ha="right")
    ax.add_patch(Rectangle((0.55, 8.12), 0.55, 0.06, color=GOLD, linewidth=0))
    ax.text(1.28, 8.08, title, fontsize=24, color=NAVY, weight="bold", va="top")
    ax.text(1.30, 7.58, subtitle, fontsize=11, color=MUTED, va="top")
    return fig, ax


def card(ax, x, y, w, h, title, lines, fill=WHITE, accent=BLUE, title_size=13, body_size=9.2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.10",
                                facecolor=fill, edgecolor=LINE, linewidth=1.0))
    ax.add_patch(FancyBboxPatch((x, y), 0.10, h, boxstyle="round,pad=0.01,rounding_size=0.05",
                                facecolor=accent, edgecolor=accent, linewidth=0))
    ax.text(x + 0.28, y + h - 0.34, title, fontsize=title_size, color=NAVY, weight="bold", va="top")
    for i, line in enumerate(lines):
        ax.text(x + 0.28, y + h - 0.72 - i * 0.30, line, fontsize=body_size, color=INK, va="top")


def arrow(ax, x1, y1, x2, y2, color=GOLD, lw=2.0, text=None, text_y_offset=0.18):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=15,
                                 linewidth=lw, color=color, shrinkA=5, shrinkB=5))
    if text:
        ax.text((x1 + x2) / 2, (y1 + y2) / 2 + text_y_offset, text, fontsize=8.5,
                color=color, weight="bold", ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.18", facecolor=BG, edgecolor="none"))


def footer(ax, text):
    ax.plot([0.55, 15.45], [0.54, 0.54], color=LINE, linewidth=0.8)
    ax.text(0.58, 0.28, text, fontsize=7.2, color=MUTED, va="bottom")


def save(fig, name):
    path = OUT / name
    fig.savefig(path, dpi=180, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    print(path)


def illustration_1():
    fig, ax = setup(
        "01  ·  From a subprime mortgage to structured credit",
        "A borrower becomes part of a risk-transformation chain — the asset is not simply made to disappear.",
    )
    y, h, w = 4.02, 2.05, 2.52
    xs = [0.58, 3.55, 6.52, 9.49, 12.46]
    card(ax, xs[0], y, w, h, "BORROWER", ["Subprime profile", "higher PD · weaker file", "illustrative mortgage"], PALE_MAGENTA, MAGENTA)
    card(ax, xs[1], y, w, h, "BANK / ORIGINATOR", ["underwrites loans", "may service cash flows", "originates credit"], PALE_BLUE, BLUE)
    card(ax, xs[2], y, w, h, "POOL + SPV", ["loan pool", "true sale or synthetic", "issues notes"], PALE_TEAL, TEAL)
    card(ax, xs[3], y, w, h, "TRANCHES", ["senior · mezzanine", "equity / residual", "different priorities"], PALE_GOLD, GOLD)
    card(ax, xs[4], y, w, h, "INVESTORS", ["cash-flow exposure", "yield · spread · risk", "different mandates"], WHITE, NAVY)
    for i in range(4):
        arrow(ax, xs[i] + w + 0.10, y + h / 2, xs[i + 1] - 0.08, y + h / 2, GOLD)

    ax.text(0.62, 3.38, "Illustrative structured-credit example", fontsize=10, color=GOLD, weight="bold")
    ax.text(0.62, 3.07, "100 mortgages  =  €100m pool", fontsize=18, color=NAVY, weight="bold")
    # tranche stack
    stack_x, stack_y, stack_w = 5.20, 1.36, 5.55
    segments = [("Equity  €5m", 0.15, PALE_MAGENTA, MAGENTA), ("Mezzanine  €15m", 0.23, PALE_TEAL, TEAL), ("Senior  €80m", 0.62, PALE_BLUE, BLUE)]
    current = stack_y
    for label, portion, fill, color in segments:
        height = portion * 1.62
        ax.add_patch(Rectangle((stack_x, current), stack_w, height, facecolor=fill, edgecolor=WHITE, linewidth=2))
        ax.text(stack_x + 0.18, current + height / 2, label, fontsize=11, color=NAVY, weight="bold", va="center")
        current += height
    ax.text(stack_x, 3.00, "Notes issued by the SPV", fontsize=9, color=MUTED)
    ax.text(11.28, 2.83, "Cash-flow priority", fontsize=10, color=BLUE, weight="bold")
    arrow(ax, 11.50, 2.45, 11.50, 1.70, BLUE, text="senior first")
    ax.text(12.10, 2.06, "Loss priority", fontsize=10, color=MAGENTA, weight="bold")
    arrow(ax, 12.33, 1.68, 12.33, 0.92, MAGENTA, text="equity first", text_y_offset=-0.16)
    ax.add_patch(FancyBboxPatch((0.62, 1.36), 3.95, 1.62, boxstyle="round,pad=0.02,rounding_size=0.10",
                                facecolor=WHITE, edgecolor=LINE, linewidth=1))
    ax.text(0.90, 2.62, "WHAT ‘SUBPRIME’ MEANS", fontsize=9, color=MAGENTA, weight="bold")
    ax.text(0.90, 2.28, "A higher-risk credit profile —\nnot one universal legal category.", fontsize=9.3, color=INK, weight="bold", linespacing=1.1)
    ax.text(0.90, 1.79, "May involve weaker history, higher LTV,\nlimited documentation or a higher PD.", fontsize=8.4, color=MUTED, linespacing=1.1)
    ax.text(0.90, 1.43, "PD = probability of default  ·  LTV = loan-to-value", fontsize=7.6, color=MUTED)
    footer(ax, "Illustrative example only. Mechanism: assigned textbook, Chapter 10; FCIC; Basel Committee securitisation framework.")
    save(fig, "01_subprime_to_structured_credit.png")


def illustration_2():
    fig, ax = setup(
        "02  ·  Waterfall: who gets paid, who absorbs the loss?",
        "The same structure allocates cash flows and losses in opposite directions.",
    )
    # Two waterfall panels
    ax.add_patch(FancyBboxPatch((0.62, 4.00), 6.35, 2.40, boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor=WHITE, edgecolor=LINE, linewidth=1))
    ax.text(0.95, 6.02, "CASH-FLOW WATERFALL", fontsize=10, color=BLUE, weight="bold")
    ax.text(0.95, 5.70, "Borrower collections are distributed by payment priority.", fontsize=9, color=MUTED)
    for i, (label, fill, color, y) in enumerate([
        ("1  Senior", PALE_BLUE, BLUE, 5.02), ("2  Mezzanine", PALE_TEAL, TEAL, 4.55), ("3  Equity / residual", PALE_MAGENTA, MAGENTA, 4.08)
    ]):
        ax.add_patch(FancyBboxPatch((1.00, y), 4.65, 0.34, boxstyle="round,pad=0.01,rounding_size=0.06", facecolor=fill, edgecolor=fill))
        ax.text(1.22, y + 0.17, label, fontsize=10, color=NAVY, weight="bold", va="center")
        ax.text(5.25, y + 0.17, "paid first" if i == 0 else ("paid second" if i == 1 else "paid last"), fontsize=8.5, color=color, ha="right", va="center")
    arrow(ax, 0.96, 4.88, 1.00, 4.88, GOLD, lw=2, text="collections", text_y_offset=0.28)

    ax.add_patch(FancyBboxPatch((7.35, 4.00), 7.98, 2.40, boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor=WHITE, edgecolor=LINE, linewidth=1))
    ax.text(7.68, 6.02, "LOSS WATERFALL", fontsize=10, color=MAGENTA, weight="bold")
    ax.text(7.68, 5.70, "Credit losses hit the protection layers in reverse order.", fontsize=9, color=MUTED)
    for i, (label, fill, color, y) in enumerate([
        ("1  Equity absorbs first", PALE_MAGENTA, MAGENTA, 5.02), ("2  Mezzanine absorbs next", PALE_TEAL, TEAL, 4.55), ("3  Senior is touched last", PALE_BLUE, BLUE, 4.08)
    ]):
        ax.add_patch(FancyBboxPatch((7.72, y), 6.20, 0.34, boxstyle="round,pad=0.01,rounding_size=0.06", facecolor=fill, edgecolor=fill))
        ax.text(7.94, y + 0.17, label, fontsize=10, color=NAVY, weight="bold", va="center")
        ax.text(13.65, y + 0.17, "first" if i == 0 else ("second" if i == 1 else "last"), fontsize=8.5, color=color, ha="right", va="center")
    arrow(ax, 7.67, 4.88, 7.72, 4.88, CORAL, lw=2, text="losses", text_y_offset=0.28)

    ax.text(0.65, 3.35, "Illustrative €100m pool", fontsize=10, color=GOLD, weight="bold")
    ax.text(0.65, 2.98, "€80m senior  ·  €15m mezzanine  ·  €5m equity", fontsize=15, color=NAVY, weight="bold")
    scenarios = [
        ("€4m loss", "equity absorbs it", PALE_TEAL, TEAL),
        ("€7m loss", "equity is exhausted; mezzanine starts", PALE_MAGENTA, MAGENTA),
        ("€22m loss", "senior protection is breached", "#FDECEA", CORAL),
    ]
    x = 0.65
    for loss, result, fill, color in scenarios:
        ax.add_patch(FancyBboxPatch((x, 1.30), 4.55, 1.12, boxstyle="round,pad=0.02,rounding_size=0.09", facecolor=fill, edgecolor=fill))
        ax.text(x + 0.22, 2.10, loss, fontsize=12, color=color, weight="bold")
        ax.text(x + 0.22, 1.73, result, fontsize=9, color=INK)
        x += 4.85
    footer(ax, "Illustrative example only. Payment and loss priorities depend on the legal waterfall of the transaction.")
    save(fig, "02_cashflow_and_loss_waterfalls.png")


def illustration_3():
    fig, ax = setup(
        "03  ·  CDS: transferring credit risk without necessarily selling the asset",
        "A Credit Default Swap is a bilateral derivative: premium in normal times, contingent payment after a credit event.",
    )
    # Buyer/seller panels
    card(ax, 0.65, 4.05, 3.15, 2.05, "PROTECTION BUYER", ["Investor / bank", "owns or references €10m RMBS", "wants to hedge credit risk"], PALE_BLUE, BLUE, body_size=8.8)
    card(ax, 12.20, 4.05, 3.15, 2.05, "PROTECTION SELLER", ["Dealer / insurer", "receives premium", "takes contingent exposure"], PALE_MAGENTA, MAGENTA, body_size=8.8)
    # central contract rail
    ax.plot([3.85, 12.13], [5.02, 5.02], color=LINE, linewidth=2)
    arrow(ax, 4.02, 5.45, 11.95, 5.45, TEAL, lw=2.6, text="premium / CDS spread: 250 bps per year")
    ax.text(7.95, 5.11, "€250,000 annual premium on €10m notional", fontsize=10, color=TEAL, weight="bold", ha="center")
    arrow(ax, 11.95, 4.57, 4.02, 4.57, MAGENTA, lw=2.6, text="protection payment after a defined credit event", text_y_offset=-0.22)
    ax.text(7.95, 4.22, "Illustrative recovery = 40%  →  LGD = 60%  →  €6m payment", fontsize=10, color=MAGENTA, weight="bold", ha="center")

    # Definition / no default cards
    ax.add_patch(FancyBboxPatch((0.65, 1.16), 6.85, 2.25, boxstyle="round,pad=0.02,rounding_size=0.10", facecolor=WHITE, edgecolor=LINE, linewidth=1))
    ax.text(0.98, 3.06, "CDS CONTRACT LOGIC", fontsize=9.5, color=NAVY, weight="bold")
    ax.text(0.98, 2.68, "If no credit event occurs", fontsize=11, color=TEAL, weight="bold")
    ax.text(0.98, 2.35, "The buyer pays the premium; the seller makes no protection payment.", fontsize=9.2, color=INK)
    ax.text(0.98, 1.92, "If a defined credit event occurs", fontsize=11, color=MAGENTA, weight="bold")
    ax.text(0.98, 1.59, "The contract settles according to the reference obligation, not simply according to market fear.", fontsize=9.2, color=INK)

    ax.add_patch(FancyBboxPatch((7.78, 1.16), 7.55, 2.25, boxstyle="round,pad=0.02,rounding_size=0.10", facecolor="#FDF4E7", edgecolor="#F3D9A7", linewidth=1))
    ax.text(8.10, 3.06, "WHAT THE TRADER MONITORS", fontsize=9.5, color=GOLD, weight="bold")
    tags = ["notional", "spread", "recovery", "counterparty", "collateral", "liquidity"]
    for i, tag in enumerate(tags):
        xx = 8.10 + (i % 3) * 2.15
        yy = 2.55 - (i // 3) * 0.52
        ax.add_patch(FancyBboxPatch((xx, yy), 1.82, 0.30, boxstyle="round,pad=0.01,rounding_size=0.06", facecolor=WHITE, edgecolor="#F3D9A7", linewidth=0.8))
        ax.text(xx + 0.91, yy + 0.15, tag, fontsize=8.5, color=INK, ha="center", va="center")
    ax.text(8.10, 1.55, "A CDS is a credit derivative — not automatically an insurance policy.", fontsize=9.1, color=CORAL, weight="bold")
    footer(ax, "Illustrative example only. A CDS contract has defined documentation, credit events, settlement terms and collateral obligations.")
    save(fig, "03_cds_cashflows_and_protection.png")


def illustration_4():
    fig, ax = setup(
        "04  ·  From structured credit to systemic stress and regulation",
        "The crisis was a chain of incentives, leverage, opacity and liquidity — not securitisation alone.",
    )
    labels = [
        ("Weak\nunderwriting", PALE_MAGENTA, MAGENTA),
        ("RMBS / CDO\ncomplexity", PALE_GOLD, GOLD),
        ("Leverage +\noff-balance sheet", PALE_BLUE, BLUE),
        ("Defaults +\ndowngrades", "#FDECEA", CORAL),
        ("Margin calls +\nfire sales", PALE_MAGENTA, MAGENTA),
        ("Liquidity stress +\ncontagion", NAVY, WHITE),
    ]
    x = 0.62
    for i, (label, fill, color) in enumerate(labels):
        ax.add_patch(FancyBboxPatch((x, 4.46), 2.12, 1.20, boxstyle="round,pad=0.02,rounding_size=0.10", facecolor=fill, edgecolor=fill))
        ax.text(x + 1.06, 5.06, label, fontsize=11.5, color=color if fill != NAVY else WHITE, weight="bold", ha="center", va="center")
        if i < len(labels) - 1:
            arrow(ax, x + 2.22, 5.06, x + 2.75, 5.06, CORAL, lw=1.9)
        x += 2.62

    ax.text(0.65, 3.85, "REGULATORY AFTERSHOCK", fontsize=10, color=TEAL, weight="bold")
    timeline = [
        ("Basel I\n1988", "credit-risk\ncapital", BLUE),
        ("Basel II\n2004", "three pillars\n+ risk sensitivity", TEAL),
        ("Basel III\npost-2008", "CET1 · buffers\nLCR · NSFR · leverage", MAGENTA),
        ("Basel IV*", "revised RWA\n+ output floor", GOLD),
    ]
    x = 0.65
    for i, (label, body, color) in enumerate(timeline):
        ax.add_patch(FancyBboxPatch((x, 1.56), 3.22, 1.50, boxstyle="round,pad=0.02,rounding_size=0.10", facecolor=WHITE, edgecolor=LINE, linewidth=1))
        ax.text(x + 0.22, 2.72, label, fontsize=11, color=color, weight="bold")
        ax.text(x + 0.22, 2.28, body, fontsize=9.7, color=INK, linespacing=1.2)
        if i < 3:
            arrow(ax, x + 3.29, 2.31, x + 3.62, 2.31, GOLD, lw=1.5)
        x += 3.60
    ax.text(0.68, 1.10, "*Basel IV is a market nickname for the final Basel III reforms, not an official standalone accord.", fontsize=8.6, color=MUTED)
    footer(ax, "Sources: FCIC; Federal Reserve History; Basel Committee. Basel labels and dates require the exact course/source edition to be cited in the final deck.")
    save(fig, "04_crisis_to_basel_timeline.png")


def illustration_5():
    """Create a simple volume-plus-share chart in the style of the user's reference."""
    fig, ax = setup(
        "05  ·  Growth of subprime mortgage lending",
        "Bars show annual originations; the line shows subprime originations as a share of all mortgage originations.",
    )

    # Same-source, directly reported figures from Table 1 of the NY Fed staff report.
    # The percentage series is calculated from that table's origination columns so the
    # denominator is explicit rather than mixing incompatible market definitions.
    years = [2001, 2002, 2003, 2004, 2005, 2006]
    volume = [190, 231, 335, 540, 625, 600]  # USD billions
    total_originations = [2113, 2773, 3765, 2600, 2755, 2520]
    share = [100 * value / total for value, total in zip(volume, total_originations)]

    chart = fig.add_axes([0.095, 0.18, 0.665, 0.60], facecolor=WHITE)
    share_axis = chart.twinx()
    chart.set_axisbelow(True)
    chart.grid(axis="y", color=LINE, linewidth=0.8)
    chart.grid(axis="x", color="#EEF1F5", linewidth=0.7)

    bars = chart.bar(years, volume, width=0.68, color="#E24A00", edgecolor="#B63B00",
                     linewidth=0.5, label="Subprime originations ($bn)", zorder=3)
    line, = share_axis.plot(years, share, color="#8B1E1E", linewidth=2.8,
                            marker="o", markersize=5.5, markerfacecolor=WHITE,
                            markeredgewidth=1.8, label="Share of all mortgage originations",
                            zorder=5)

    chart.set_xlim(2000.45, 2006.55)
    chart.set_ylim(0, 700)
    share_axis.set_ylim(0, 30)
    chart.set_xticks(years)
    chart.set_xticklabels([str(year) for year in years], fontsize=9, color=INK)
    chart.set_yticks([0, 100, 200, 300, 400, 500, 600, 700])
    share_axis.set_yticks([0, 5, 10, 15, 20, 25, 30])
    chart.set_ylabel("Annual subprime originations ($bn)", fontsize=9.5, color=INK, labelpad=8)
    share_axis.set_ylabel("Share of all mortgage originations (%)", fontsize=9.5, color="#8B1E1E", labelpad=10)
    chart.tick_params(axis="y", labelsize=8.5, colors=INK)
    share_axis.tick_params(axis="y", labelsize=8.5, colors="#8B1E1E")
    chart.tick_params(axis="x", length=0, pad=6)
    share_axis.tick_params(axis="x", length=0)
    for spine in ["top", "right"]:
        chart.spines[spine].set_visible(False)
    chart.spines["left"].set_color(LINE)
    chart.spines["bottom"].set_color(LINE)
    share_axis.spines["top"].set_visible(False)
    share_axis.spines["left"].set_visible(False)
    share_axis.spines["right"].set_color("#8B1E1E")

    chart.text(2006, volume[-1] + 28, "$600bn", fontsize=9, color="#B63B00",
               weight="bold", ha="center")
    share_axis.text(2006.08, share[-1] + 1.5, f"{share[-1]:.1f}%", fontsize=9,
                    color="#8B1E1E", weight="bold", ha="left")
    chart.axvspan(2003.5, 2006.5, color=PALE_GOLD, alpha=0.42, zorder=0)
    chart.text(2005.0, 655, "Acceleration", fontsize=8.5, color=GOLD,
               weight="bold", ha="center", va="top")

    handles = [bars, line]
    labels = ["Subprime originations ($bn)", "Share of all mortgage originations (%)"]
    chart.legend(handles, labels, loc="upper left", bbox_to_anchor=(0.01, 0.99),
                 frameon=False, fontsize=8.3, handlelength=2.4)

    # One short reading panel replaces the previous block diagrams with an explicit
    # market message: scale increases, but a chart is not a causal proof by itself.
    ax.add_patch(FancyBboxPatch((12.55, 1.42), 2.55, 4.62,
                                boxstyle="round,pad=0.02,rounding_size=0.10",
                                facecolor=WHITE, edgecolor=LINE, linewidth=1))
    ax.text(12.82, 5.67, "WHAT THIS SHOWS", fontsize=9.5, color=TEAL, weight="bold")
    ax.text(12.82, 5.22, "1", fontsize=15, color=GOLD, weight="bold")
    ax.text(13.17, 5.28, "Volume rises", fontsize=10.2, color=NAVY, weight="bold")
    ax.text(13.17, 4.91, "$190bn → $625bn\nfrom 2001 to 2005", fontsize=8.6, color=INK, linespacing=1.25)
    ax.text(12.82, 4.35, "2", fontsize=15, color=GOLD, weight="bold")
    ax.text(13.17, 4.41, "Market share expands", fontsize=10.2, color=NAVY, weight="bold")
    ax.text(13.17, 4.04, "about 9% → 23.8%\nin this table's definition", fontsize=8.6, color=INK, linespacing=1.25)
    ax.text(12.82, 3.48, "3", fontsize=15, color=GOLD, weight="bold")
    ax.text(13.17, 3.54, "Not a causal proof", fontsize=10.2, color=NAVY, weight="bold")
    ax.text(13.17, 3.17, "Growth shows scale and\nfunding demand — not by itself\nwhy losses later occurred.", fontsize=8.6, color=INK, linespacing=1.25)
    ax.text(12.82, 2.26, "DEFINITION", fontsize=8.5, color=MUTED, weight="bold")
    ax.text(12.82, 1.88, "Share = subprime originations\n÷ total originations in Table 1", fontsize=8.1, color=MUTED, linespacing=1.25)

    footer(ax, "Source: Ashcraft & Schuermann, Federal Reserve Bank of New York Staff Report 318 (2008), Table 1; Inside Mortgage Finance. Share calculated from the same table.")
    save(fig, "05_subprime_growth_combo_chart.png")


def main():
    illustration_1()
    illustration_2()
    illustration_3()
    illustration_4()
    illustration_5()


if __name__ == "__main__":
    main()
