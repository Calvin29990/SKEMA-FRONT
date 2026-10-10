"""Create a two-page French executive brief from the approved graph pair."""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch

from build_cib_graphs import INK, MUTED, GRID, PAPER, GOLD, BNP, CACIB

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
PDF_PATH = OUT / "CIB_FRANCE_LUXEMBOURG_EXECUTIVE_BRIEF_FR.pdf"
MAP_PATH = OUT / "01_europe_cib_activity_map.png"
BUBBLE_PATH = OUT / "four_brand_comparator" / "FOUR_BRANDS_EXECUTIVE_BUBBLE.png"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "figure.facecolor": PAPER,
    "savefig.facecolor": PAPER,
})


def explainer(fig, label, title, bullets, takeaway, source_note):
    """Add the French explanation strip beneath a graph."""
    ax = fig.add_axes([0.06, 0.055, 0.88, 0.145])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.012,rounding_size=0.025",
                                facecolor="#F0F5F9", edgecolor="none"))
    ax.text(0.025, 0.80, label.upper(), fontsize=7.2, color=GOLD, weight="bold")
    ax.text(0.025, 0.58, title, fontsize=10.0, color=INK, weight="bold")
    bullet_text = "\n".join("• " + bullet for bullet in bullets)
    ax.text(0.025, 0.42, bullet_text, fontsize=7.1, color=INK, va="top", linespacing=1.35)
    ax.add_patch(FancyBboxPatch((0.62, 0.13), 0.35, 0.66, boxstyle="round,pad=0.012,rounding_size=0.018",
                                facecolor="white", edgecolor=GRID, linewidth=0.7))
    ax.text(0.645, 0.65, "À RETENIR", fontsize=6.7, color=CACIB, weight="bold")
    ax.text(0.645, 0.47, takeaway, fontsize=8.3, color=INK, weight="bold", va="top", linespacing=1.25)
    fig.text(0.06, 0.026, source_note, fontsize=6.2, color=MUTED, ha="left", va="bottom")


def page(fig, graph_path, graph_no, page_title, page_subtitle, label, explanation_title, bullets, takeaway, source_note):
    fig.text(0.06, 0.965, page_title, fontsize=20, color=INK, weight="bold", ha="left", va="top")
    fig.text(0.06, 0.928, page_subtitle, fontsize=9.2, color=MUTED, ha="left", va="top")
    fig.text(0.94, 0.955, f"{graph_no}/2", fontsize=8.5, color=GOLD, weight="bold", ha="right")
    image_ax = fig.add_axes([0.06, 0.245, 0.88, 0.665])
    image_ax.imshow(plt.imread(graph_path), aspect="auto")
    image_ax.axis("off")
    explainer(fig, label, explanation_title, bullets, takeaway, source_note)


def main():
    if not MAP_PATH.exists():
        raise FileNotFoundError(MAP_PATH)
    if not BUBBLE_PATH.exists():
        raise FileNotFoundError(BUBBLE_PATH)
    with PdfPages(PDF_PATH) as pdf:
        fig = plt.figure(figsize=(16, 11))
        page(
            fig,
            MAP_PATH,
            "1",
            "Brief exécutif France–Luxembourg — Graphique 1",
            "Carte d’ouverture : où se trouvent les plateformes CIB et comment lire leur empreinte européenne",
            "Graphique 1 · Carte européenne",
            "L’objectif de la carte",
            [
                "Les points identifient des hubs publiquement documentés pour BNP Paribas CIB et CACIB.",
                "Les activités à droite décrivent ce que les plateformes sont conçues à offrir : financement, marchés et services titres.",
                "Les villes et liaisons sont des repères de couverture, pas une mesure de revenus, de volumes ou de booking légal.",
            ],
            "Paris donne la lecture européenne ; Luxembourg est ensuite traité comme un périmètre local spécifique, et non comme une simple copie de la plateforme groupe.",
            "Sources : carte produite dans le projet à partir des pages publiques BNP Paribas CIB / CACIB. Les périmètres et limites sont détaillés dans cib_graphs/README.md.",
        )
        pdf.savefig(fig, bbox_inches="tight", pad_inches=0)
        plt.close(fig)

        fig = plt.figure(figsize=(16, 11))
        page(
            fig,
            BUBBLE_PATH,
            "2",
            "Brief exécutif France–Luxembourg — Graphique 2",
            "Bubble chart simplifié : qui est servi, quelle est la largeur de l’offre et quel est le poids opérationnel public",
            "Graphique 2 · Bubble chart exécutif",
            "La lecture en 20 secondes",
            [
                "De gauche à droite : offre spécialisée, offre mixte ou plateforme large.",
                "De bas en haut : signal local, portée locale publiquement quantifiée, plateforme groupe.",
                "La taille de la bulle correspond à un signal d’effectifs publics ; elle ne représente pas le revenu.",
                "N/D signifie que le nombre de clients locaux n’est pas publié : aucune estimation n’a été ajoutée.",
            ],
            "BNP CIB et CACIB portent les plateformes larges ; CACEIS est spécialisé dans l’asset servicing ; BNP CIB Luxembourg correspond à une offre CIB locale ciblée.",
            "Sources : BNP CIB at a glance / 2026 At a Glance ; CACIB 2025 key figures ; BNP Paribas Luxembourg CIB ; rapport CACEIS Investor Services Luxembourg. Voir four_brand_bubble_metrics.csv.",
        )
        pdf.savefig(fig, bbox_inches="tight", pad_inches=0)
        plt.close(fig)
    print(PDF_PATH)


if __name__ == "__main__":
    main()
