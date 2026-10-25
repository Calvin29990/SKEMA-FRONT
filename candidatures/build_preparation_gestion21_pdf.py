#!/usr/bin/env python3
"""Build the candidate-facing Gestion 21 preparation PDF from its Markdown source."""
from pathlib import Path
import html
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak,
    Table, LongTable, HRFlowable, KeepTogether,
)

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "PREPARATION-CANDIDAT-GESTION21-2027.md"
OUTPUT = ROOT / "PREPARATION-CANDIDAT-GESTION21-2027.pdf"

NAVY = colors.HexColor("#142B4A")
BLUE = colors.HexColor("#286A9B")
TEAL = colors.HexColor("#1B8A88")
INK = colors.HexColor("#273444")
MUTED = colors.HexColor("#64748B")
PALE = colors.HexColor("#EEF4F8")
PALE_BLUE = colors.HexColor("#E6F0F7")
GRID = colors.HexColor("#D7E0E8")
WHITE = colors.white

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
pdfmetrics.registerFont(TTFont("DejaVu", str(FONT_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", str(FONT_DIR / "DejaVuSans-Bold.ttf")))
# Some minimal containers ship only regular and bold DejaVu faces; use those
# for italic aliases so the PDF remains portable while preserving all glyphs.
pdfmetrics.registerFont(TTFont("DejaVu-Oblique", str(FONT_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DejaVu-BoldOblique", str(FONT_DIR / "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFontFamily("DejaVu", normal="DejaVu", bold="DejaVu-Bold", italic="DejaVu-Oblique", boldItalic="DejaVu-BoldOblique")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", fontName="DejaVu-Bold", fontSize=27, leading=32,
    textColor=NAVY, alignment=TA_LEFT, spaceAfter=8*mm, keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="CoverSubtitle", fontName="DejaVu", fontSize=16, leading=22,
    textColor=BLUE, spaceAfter=8*mm, keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="H1", fontName="DejaVu-Bold", fontSize=18, leading=22,
    textColor=NAVY, spaceBefore=0, spaceAfter=7*mm, keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="H2", fontName="DejaVu-Bold", fontSize=13, leading=17,
    textColor=BLUE, spaceBefore=5*mm, spaceAfter=2.5*mm, keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="H3", fontName="DejaVu-Bold", fontSize=10.5, leading=14,
    textColor=TEAL, spaceBefore=3.5*mm, spaceAfter=1.8*mm, keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="BodyG21", fontName="DejaVu", fontSize=8.7, leading=12.3,
    textColor=INK, spaceAfter=2.7*mm, alignment=TA_LEFT,
    allowWidows=0, allowOrphans=0,
))
styles.add(ParagraphStyle(
    name="BulletG21", parent=styles["BodyG21"], leftIndent=5*mm,
    firstLineIndent=-3.2*mm, bulletIndent=0, spaceAfter=1.5*mm,
))
styles.add(ParagraphStyle(
    name="QuoteG21", fontName="DejaVu-Oblique", fontSize=9, leading=13,
    textColor=NAVY, leftIndent=5*mm, rightIndent=4*mm,
    borderColor=TEAL, borderWidth=2, borderPadding=(2*mm, 3*mm, 2*mm, 3*mm),
    backColor=PALE, spaceBefore=2*mm, spaceAfter=4*mm,
))
styles.add(ParagraphStyle(
    name="TableHeadG21", fontName="DejaVu-Bold", fontSize=7.5, leading=9.3,
    textColor=WHITE, alignment=TA_LEFT,
))
styles.add(ParagraphStyle(
    name="TableCellG21", fontName="DejaVu", fontSize=7.1, leading=9.2,
    textColor=INK, alignment=TA_LEFT,
))
styles.add(ParagraphStyle(
    name="SmallG21", fontName="DejaVu", fontSize=7.7, leading=10.5,
    textColor=MUTED, spaceAfter=2*mm,
))


def inline_markup(text: str) -> str:
    """Convert the limited Markdown inline syntax used by the source to ReportLab XML."""
    stash = []

    def save(markup):
        token = f"ZXQPLACEHOLDER{len(stash)}QXZ"
        stash.append((token, markup))
        return token

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: save(f'<link href="{html.escape(m.group(2), quote=True)}" color="#286A9B"><u>{html.escape(m.group(1))}</u></link>'), text)
    text = re.sub(r"`([^`]+)`", lambda m: save(f'<font name="DejaVu-Bold" color="#142B4A">{html.escape(m.group(1))}</font>'), text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", text)
    for token, markup in stash:
        text = text.replace(token, markup)
    return text


def split_table_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def is_table_separator(line):
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells)


def table_widths(n, usable):
    ratios = {
        2: [0.30, 0.70],
        3: [0.19, 0.30, 0.51],
        4: [0.16, 0.25, 0.29, 0.30],
        5: [0.15, 0.20, 0.25, 0.20, 0.20],
        6: [0.15, 0.17, 0.17, 0.17, 0.17, 0.17],
    }.get(n)
    if ratios is None:
        ratios = [1 / n] * n
    return [usable * x for x in ratios]


def build_table(rows, usable):
    ncols = max(map(len, rows))
    rows = [row + [""] * (ncols - len(row)) for row in rows]
    converted = []
    for i, row in enumerate(rows):
        st = styles["TableHeadG21"] if i == 0 else styles["TableCellG21"]
        converted.append([Paragraph(inline_markup(cell), st) for cell in row])
    widths = table_widths(ncols, usable)
    cls = LongTable if len(rows) > 7 else Table
    t = cls(converted, colWidths=widths, repeatRows=1, hAlign="LEFT", splitByRow=1)
    t.setStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PALE]),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ])
    return t


class CandidateDoc(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            str(filename), pagesize=A4,
            rightMargin=17*mm, leftMargin=17*mm,
            topMargin=19*mm, bottomMargin=17*mm,
            title="Gestion 21 — Dossier de préparation candidat",
            author="Dossier de préparation candidat",
            subject="Histoire, fonds, stratégie, concurrents, risques et questionnaire Excel",
        )
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="main", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="all", frames=frame, onPage=self.draw_page)])

    def draw_page(self, canvas, doc):
        canvas.saveState()
        w, h = A4
        if doc.page > 1:
            canvas.setStrokeColor(GRID)
            canvas.setLineWidth(0.6)
            canvas.line(17*mm, h - 13*mm, w - 17*mm, h - 13*mm)
            canvas.setFont("DejaVu-Bold", 7.2)
            canvas.setFillColor(NAVY)
            canvas.drawString(17*mm, h - 10.2*mm, "GESTION 21  /  PRÉPARATION CANDIDAT")
            canvas.setFont("DejaVu", 7.2)
            canvas.setFillColor(MUTED)
            canvas.drawRightString(w - 17*mm, h - 10.2*mm, "Sources consultées · 25 octobre 2026")
        canvas.setStrokeColor(GRID)
        canvas.setLineWidth(0.5)
        canvas.line(17*mm, 12*mm, w - 17*mm, 12*mm)
        canvas.setFont("DejaVu", 7)
        canvas.setFillColor(MUTED)
        canvas.drawString(17*mm, 8*mm, "Préparation personnelle · Vérifier les documents réglementaires en vigueur")
        canvas.drawRightString(w - 17*mm, 8*mm, f"{doc.page}")
        canvas.restoreState()


def markdown_to_story(source: str, usable_width: float):
    lines = source.splitlines()
    story = []
    i = 0
    seen_title = False
    seen_subtitle = False
    cover_finished = False
    paragraph = []

    def flush_paragraph():
        nonlocal paragraph
        if paragraph:
            text = " ".join(x.strip() for x in paragraph).strip()
            if text:
                story.append(Paragraph(inline_markup(text), styles["BodyG21"]))
            paragraph = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            i += 1
            continue

        if stripped == "---":
            flush_paragraph()
            if not cover_finished:
                # A zero-height break avoids a nearly empty spill page when the
                # cover text happens to end close to the frame boundary.
                story.append(PageBreak())
                cover_finished = True
            else:
                story.append(HRFlowable(width="100%", thickness=0.5, color=GRID, spaceBefore=2*mm, spaceAfter=3*mm))
            i += 1
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and is_table_separator(lines[i + 1]):
            flush_paragraph()
            rows = [split_table_row(stripped)]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_table_row(lines[i].strip()))
                i += 1
            story.append(build_table(rows, usable_width))
            story.append(Spacer(1, 3*mm))
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            text = inline_markup(stripped[2:].strip())
            story.append(Spacer(1, 22*mm))
            story.append(Paragraph(text, styles["CoverTitle"]))
            # Accent line under the title.
            story.append(HRFlowable(width="36%", thickness=3, color=TEAL, hAlign="LEFT", spaceBefore=1*mm, spaceAfter=8*mm))
            seen_title = True
            i += 1
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            text = inline_markup(stripped[3:].strip())
            if seen_title and not seen_subtitle:
                story.append(Paragraph(text, styles["CoverSubtitle"]))
                seen_subtitle = True
            else:
                story.append(Paragraph(text, styles["H1"]))
            i += 1
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            story.append(Paragraph(inline_markup(stripped[4:].strip()), styles["H2"]))
            i += 1
            continue

        if stripped.startswith("#### "):
            flush_paragraph()
            story.append(Paragraph(inline_markup(stripped[5:].strip()), styles["H3"]))
            i += 1
            continue

        if stripped.startswith("> "):
            flush_paragraph()
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(lines[i].strip()[1:].strip())
                i += 1
            story.append(Paragraph(inline_markup(" ".join(quote_lines)), styles["QuoteG21"]))
            continue

        bullet = re.match(r"^\s*[-*]\s+(.*)$", line)
        numbered = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if bullet or numbered:
            flush_paragraph()
            text = (bullet or numbered).group(1)
            prefix = "•" if bullet else "–"
            story.append(Paragraph(f"<font color='#1B8A88'><b>{prefix}</b></font>  {inline_markup(text)}", styles["BulletG21"]))
            i += 1
            continue

        if stripped.startswith("!["):
            flush_paragraph()
            alt = stripped[2:].split("]", 1)[0]
            story.append(Paragraph(f"<i>{html.escape(alt)}</i>", styles["SmallG21"]))
            i += 1
            continue

        paragraph.append(stripped)
        i += 1

    flush_paragraph()
    return story


def main():
    if not SOURCE.exists():
        raise SystemExit(f"Missing source: {SOURCE}")
    doc = CandidateDoc(OUTPUT)
    story = markdown_to_story(SOURCE.read_text(encoding="utf-8"), doc.width)
    doc.build(story)
    print(f"Created {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
