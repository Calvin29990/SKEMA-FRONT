#!/usr/bin/env python3
"""Convertit les mémos Markdown en PDF lisibles sur téléphone (A5, grosses polices).

Polices : DejaVu (couverture Unicode complète : → ● ■ ≤ € « »).
Pas de DejaVu-Oblique dans le sandbox → l'italique est rendu en gris foncé
(les notes « Piège : » ressortent quand même, c'est le but sur mobile).

Usage : python3 skema-training/scripts/md2pdf.py [fichier.md ...]
        (sans argument : convertit tout skema-training/memos/**/*.md)
"""
import glob
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A5
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (HRFlowable, Image, KeepTogether, PageBreak,
                                Paragraph, Preformatted, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

DJ = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("Dj", f"{DJ}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DjB", f"{DJ}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DjM", f"{DJ}/DejaVuSansMono.ttf"))
pdfmetrics.registerFont(TTFont("DjMB", f"{DJ}/DejaVuSansMono-Bold.ttf"))
pdfmetrics.registerFontFamily("Dj", normal="Dj", bold="DjB", italic="Dj", boldItalic="DjB")

PW, PH = A5
MARG = 12 * mm
AVAIL = PW - 2 * MARG

S = {
    "body": ParagraphStyle("body", fontName="Dj", fontSize=9.3, leading=12.6,
                           alignment=TA_LEFT, spaceAfter=4, textColor=colors.HexColor("#111827")),
    "h1": ParagraphStyle("h1", fontName="DjB", fontSize=15, leading=18, spaceBefore=2,
                         spaceAfter=7, textColor=colors.HexColor("#0b3d91")),
    "h2": ParagraphStyle("h2", fontName="DjB", fontSize=12.2, leading=15, spaceBefore=11,
                         spaceAfter=5, textColor=colors.HexColor("#0b3d91")),
    "h3": ParagraphStyle("h3", fontName="DjB", fontSize=10.6, leading=13.4, spaceBefore=9,
                         spaceAfter=4, textColor=colors.HexColor("#1f2937")),
    "h4": ParagraphStyle("h4", fontName="DjB", fontSize=9.8, leading=12.6, spaceBefore=7,
                         spaceAfter=3, textColor=colors.HexColor("#374151")),
    "quote": ParagraphStyle("quote", fontName="Dj", fontSize=8.9, leading=12, leftIndent=6,
                            spaceAfter=5, textColor=colors.HexColor("#1f3a5f"),
                            borderPadding=4, backColor=colors.HexColor("#eef3fb")),
    "li": ParagraphStyle("li", fontName="Dj", fontSize=9.3, leading=12.4, leftIndent=10,
                         bulletIndent=2, spaceAfter=2.5),
    "cell": ParagraphStyle("cell", fontName="Dj", fontSize=8.2, leading=10.4),
    "cellh": ParagraphStyle("cellh", fontName="DjB", fontSize=8.2, leading=10.4,
                            textColor=colors.white),
    "code": ParagraphStyle("code", fontName="DjM", fontSize=8.6, leading=11),
}


def inline(t):
    """Markdown inline -> balises reportlab (l'italique devient du gris foncé)."""
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"`([^`]+)`", r'<font face="DjM" color="#7a1f1f">\1</font>', t)
    t = re.sub(r"\[\[([^\]]+)\]\]", r'<font color="#0a7a2f"><b>\1</b></font>', t)  # réponses en vert
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r'<font color="#41546b">\1</font>', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"<b>\1</b>", t)   # liens -> titre en gras
    return t


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def build(md_path, pdf_path, title):
    lines = open(md_path, encoding="utf-8").read().split("\n")
    flow, i, n = [], 0, len(lines)
    while i < n:
        ln = lines[i]
        s = ln.strip()

        if s.startswith("```"):                                     # bloc de code
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            tbl = Table([[Preformatted("\n".join(buf), S["code"])]], colWidths=[AVAIL])
            tbl.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f4f6f8")),
                                     ("LEFTPADDING", (0, 0), (-1, -1), 6),
                                     ("TOPPADDING", (0, 0), (-1, -1), 4),
                                     ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
            flow += [tbl, Spacer(1, 4)]
            continue

        if s.startswith("!["):                                      # image
            m = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", s)
            if m:
                p = os.path.normpath(os.path.join(os.path.dirname(md_path), m.group(2)))
                if os.path.exists(p):
                    from PIL import Image as PILImage
                    w, h = PILImage.open(p).size
                    rw = min(AVAIL, w * 0.42)
                    flow += [Image(p, width=rw, height=rw * h / w), Spacer(1, 5)]
            i += 1
            continue

        if s.startswith("|") and i + 1 < n and set(lines[i + 1].strip()) <= set("|-: "):
            hdr = cells(s)
            rows = [hdr]
            i += 2
            while i < n and lines[i].strip().startswith("|"):
                rows.append(cells(lines[i]))
                i += 1
            ncol = max(len(r) for r in rows)
            rows = [r + [""] * (ncol - len(r)) for r in rows]
            widths = [AVAIL / ncol] * ncol
            body = [[Paragraph(inline(c), S["cellh"] if ri == 0 else S["cell"])
                     for c in r] for ri, r in enumerate(rows)]
            tbl = Table(body, colWidths=widths, repeatRows=1, hAlign="LEFT")
            tbl.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0b3d91")),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#b9c4d4")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1),
                 [colors.white, colors.HexColor("#f3f6fb")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 2.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
            ]))
            flow += [Spacer(1, 3), tbl, Spacer(1, 5)]
            continue

        if s.startswith("####"):
            flow.append(Paragraph(inline(s.lstrip("#").strip()), S["h4"]))
        elif s.startswith("###"):
            flow.append(Paragraph(inline(s.lstrip("#").strip()), S["h3"]))
        elif s.startswith("##"):
            flow.append(Paragraph(inline(s.lstrip("#").strip()), S["h2"]))
        elif s.startswith("# "):
            if flow:
                flow.append(PageBreak())
            flow.append(Paragraph(inline(s[2:].strip()), S["h1"]))
        elif s in ("---", "***", "___"):
            flow.append(HRFlowable(width="100%", thickness=0.6,
                                   color=colors.HexColor("#c7d2e0"), spaceBefore=4, spaceAfter=5))
        elif s.startswith(">"):                                     # bloc cité (regroupé)
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            flow.append(Paragraph(inline(" ".join(x for x in buf if x)), S["quote"]))
            continue
        elif re.match(r"^[-*+]\s+", s):
            flow.append(Paragraph(inline(re.sub(r"^[-*+]\s+", "", s)), S["li"],
                                  bulletText="•"))
        elif re.match(r"^\d+[.)]\s+", s):
            num = re.match(r"^(\d+)[.)]\s+", s).group(1)
            flow.append(Paragraph(inline(re.sub(r"^\d+[.)]\s+", "", s)), S["li"],
                                  bulletText=f"{num}."))
        elif s == "":
            flow.append(Spacer(1, 2.5))
        else:
            buf = [s]
            i += 1
            while i < n:
                t = lines[i].strip()
                if (t == "" or t.startswith(("#", "|", ">", "```", "![", "---"))
                        or re.match(r"^[-*+]\s+", t) or re.match(r"^\d+[.)]\s+", t)):
                    break
                buf.append(t)
                i += 1
            flow.append(Paragraph(inline(" ".join(buf)), S["body"]))
            continue
        i += 1

    def deco(cv, doc):
        cv.saveState()
        cv.setFont("Dj", 7)
        cv.setFillColor(colors.HexColor("#6b7280"))
        cv.drawString(MARG, 7 * mm, title[:52])
        cv.drawRightString(PW - MARG, 7 * mm, f"p. {doc.page}")
        cv.setStrokeColor(colors.HexColor("#dbe2ec"))
        cv.line(MARG, 9 * mm, PW - MARG, 9 * mm)
        cv.restoreState()

    doc = SimpleDocTemplate(pdf_path, pagesize=A5,
                            leftMargin=MARG, rightMargin=MARG,
                            topMargin=MARG, bottomMargin=15 * mm,
                            title=title, author="SKEMA-FRONT")
    doc.build([f for f in flow if f is not None], onFirstPage=deco, onLaterPages=deco)
    return pdf_path


def main():
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "memos")
    outdir = os.path.join(root, "pdf")
    os.makedirs(outdir, exist_ok=True)
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(root, "**", "*.md"), recursive=True))
    made = []
    for f in files:
        rel = os.path.relpath(f, root)
        base = os.path.splitext(os.path.basename(f))[0]
        title = base
        pdf = os.path.join(outdir, base + ".pdf")
        build(f, pdf, title)
        made.append(pdf)
        print(f"{rel:42s} -> pdf/{base}.pdf  ({os.path.getsize(pdf)//1024} Ko)")
    print(f"\n{len(made)} PDF dans {os.path.abspath(outdir)}")


if __name__ == "__main__":
    main()
