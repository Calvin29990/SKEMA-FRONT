"""Export the approved CIB graphs as clean, graph-only English assets.

The explanatory text is kept separately for the Drive/report document. These
PNG files deliberately contain only the enlarged graph: no wrapper title,
source footer or takeaway box.
"""
from __future__ import annotations

import shutil
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
MAP = OUT / "01_europe_cib_activity_map.png"
BUBBLE = OUT / "four_brand_comparator" / "FOUR_BRANDS_EXECUTIVE_BUBBLE.png"
REPORT_DIR = OUT / "english_report_figures"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

MAP_OUT = REPORT_DIR / "01_european_cib_footprint_report_en.png"
BUBBLE_OUT = REPORT_DIR / "02_four_franchises_bubble_report_en.png"
PDF_OUT = OUT / "CIB_FRANCE_LUXEMBOURG_REPORT_FIGURES_EN.pdf"


def copy_graph(source: Path, destination: Path) -> Path:
    """Copy a graph-only source without adding any report furniture."""
    shutil.copy2(source, destination)
    return destination


def make_pdf_page(pdf: PdfPages, source: Path) -> None:
    image = plt.imread(source)
    height, width = image.shape[:2]
    # Keep the page ratio close to the source image so the graph is not
    # rescaled into a portrait wrapper or surrounded by unnecessary whitespace.
    page = plt.figure(figsize=(width / 240.0, height / 240.0), facecolor="white")
    ax = page.add_axes([0, 0, 1, 1])
    ax.imshow(image, aspect="auto")
    ax.axis("off")
    pdf.savefig(page, bbox_inches="tight", pad_inches=0)
    plt.close(page)


def main() -> None:
    if not MAP.exists() or not BUBBLE.exists():
        raise FileNotFoundError("Clean source graph is missing")

    map_png = copy_graph(MAP, MAP_OUT)
    bubble_png = copy_graph(BUBBLE, BUBBLE_OUT)
    with PdfPages(PDF_OUT) as pdf:
        make_pdf_page(pdf, map_png)
        make_pdf_page(pdf, bubble_png)

    print(map_png)
    print(bubble_png)
    print(PDF_OUT)


if __name__ == "__main__":
    main()
