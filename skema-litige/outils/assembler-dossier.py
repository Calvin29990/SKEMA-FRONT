#!/usr/bin/env python3
"""assembler-dossier.py — construit les PDF prêts à imprimer / à envoyer du dossier ANBG.

Produit, dans skema-litige/PARENTS-ANBG/pdf/ :
  DOSSIER-A-REMETTRE-ANBG.pdf   volets 1 à 3 du recours + annexes, dans l'ordre de la chemise
  DOSSIER-FAMILLE-COMPLET.pdf   recours entier (mémo + note interne compris) + annexes
  MAIL-CAMPUS-FRANCE.pdf        courriel à adresser, juriste de SKEMA en copie

Usage : python3 skema-litige/outils/assembler-dossier.py
"""
import os
import re
import sys

import pymupdf as fitz

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, ".."))
SRC = os.path.join(BASE, "PARENTS-ANBG")
PIECES = os.path.join(BASE, "pieces")
OUT = os.path.join(SRC, "pdf")
sys.path.insert(0, HERE)
import md2pdf  # noqa: E402

FOOT = "MINANG Calvin — recours gracieux ANBG — dossier 110584Z — session 2025-2026"

# (fichier dans pieces/, légende de l'annexe)
ANNEXES = [
    ("__CAPTURES__", "Captures d'écran de la plateforme eBourse (4 notifications) — à imprimer depuis l'espace étudiant, horodatage de consultation visible"),
    ("attestation-assiduite-09-12-2025.pdf", "Attestation de SKEMA Business School du 9 décembre 2025 (Mme Sophie Gay) — assiduité certifiée 29 jours après l'avis défavorable"),
    ("attestation-PGE.pdf", "Attestation « Programme Grande École » du registraire du 14 mai 2024 — césures et calendrier du cycle"),
    ("bon-de-commande-M1.pdf", "Bon de commande Campus France n° 721622 du 6 mai 2024 — 16 000,00 €, « pour le compte de l'ANBG », frais formation 2023-2024"),
    ("convention-stage-bpce-2024.pdf", "Convention de stage SKEMA / BPCE du 4 janvier 2024 — six mois, du 8 janvier au 5 juillet 2024"),
    ("mise-en-demeure.pdf", "Mise en demeure SKEMA Business School du 7 octobre 2026, réf. 2026-SK.D-0002 — 14 840,00 €, 10 jours"),
]


def placeholder(ligne, legende):
    """Page « à insérer » pour une pièce que l'étudiant doit imprimer lui-même."""
    doc = fitz.open()
    pg = doc.new_page(width=fitz.paper_size("a4")[0], height=fitz.paper_size("a4")[1])
    pg.insert_font(fontname="DJr", fontfile=md2pdf.FFILE["r"])
    pg.insert_font(fontname="DJb", fontfile=md2pdf.FFILE["b"])
    font = fitz.Font(fontfile=md2pdf.FFILE["r"])
    pg.draw_rect(fitz.Rect(50, 54, pg.rect.width - 50, 96), color=None, fill=(0.11, 0.14, 0.20))
    pg.insert_text((59, 78), f"ANNEXE {ligne}", fontname="DJb", fontsize=15, color=(1, 1, 1))
    y = 130
    for ln in _wrap(font, legende, 11, pg.rect.width - 100):
        pg.insert_text((50, y), ln, fontname="DJr", fontsize=11)
        y += 16
    pg.draw_rect(fitz.Rect(50, y + 24, pg.rect.width - 50, y + 124), color=(0.6, 0.6, 0.6), width=1.2, dashes="[3 3] 0 0")
    pg.insert_text((62, y + 48), "[ PIÈCE À IMPRIMER PAR L'ÉTUDIANT — puis à agrafer ici ]", fontname="DJr", fontsize=10)
    pg.insert_text((50, pg.rect.height - 60), FOOT, fontname="DJr", fontsize=8, color=(0.42, 0.42, 0.42))
    return doc


def _wrap(font, text, size, width):
    out, cur = [], ""
    for w in text.split():
        if font.text_length(cur + " " + w, size) > width:
            out.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        out.append(cur)
    return out


def annex_doc():
    bundle = fitz.open()
    for i, (fn, legende) in enumerate(ANNEXES, start=4):
        if fn == "__CAPTURES__":
            src = placeholder(f"{i} SUR {len(ANNEXES)}", legende)
            bundle.insert_pdf(src)
            src.close()
            continue
        src = fitz.open(os.path.join(PIECES, fn))
        if i == 9:  # mise en demeure : 1re page seulement (la 2e est blanche)
            src.select([0])
        cover = placeholder(f"{i} SUR {len(ANNEXES)}", legende)
        bundle.insert_pdf(cover)
        bundle.insert_pdf(src)
        src.close()
        cover.close()
    return bundle


def finalize(doc, path, seuKo=250):
    """Dossiers de remise : pages scannées lourdes -> JPEG 150 dpi, sous-embedding des polices.

    Les pages générées (recours, procuration, récépissé) restent vectorielles et nettes à l'impression.
    """
    heavy = set()
    for i, pg in enumerate(doc):
        poids = 0
        for im in pg.get_images(full=True):
            try:
                poids += len(doc.extract_image(im[0])[1])
            except Exception:
                pass
        if poids > seuKo * 1024:
            heavy.add(i)
    out = fitz.open()
    for i, pg in enumerate(doc):
        if i in heavy:
            pix = pg.get_pixmap(dpi=150)
            img = pix.tobytes("jpeg", jpg_quality=62)
            np = out.new_page(width=pg.rect.width, height=pg.rect.height)
            np.insert_image(np.rect, stream=img)
        else:
            out.insert_pdf(doc, from_page=i, to_page=i)
    try:
        out.subset_fonts()
    except Exception:
        pass
    out.save(path, deflate=True, garbage=4, clean=True)
    n, o = out.page_count, os.path.getsize(path)
    out.close()
    return n, o, len(heavy)


def main():
    os.makedirs(OUT, exist_ok=True)
    md = os.path.join(SRC, "RECOURS-GRACIEUX-ANBG.md")
    import tempfile
    tmp = os.path.join(tempfile.gettempdir(), "_recours_tmp.pdf")
    md2pdf.render(open(md, encoding="utf-8").read(), tmp, FOOT)
    full = fitz.open(tmp)
    start_memo = next((i for i, p in enumerate(full) if "MÉMO POUR LES PARENTS" in p.get_text()), len(full))
    end_memo = next((i for i, p in enumerate(full) if "NOTE INTERNE FAMILIALE" in p.get_text()), len(full))

    for name, ranges in [
        ("DOSSIER-A-REMETTRE-ANBG.pdf", [(0, start_memo)]),
        ("DOSSIER-FAMILLE-COMPLET.pdf", [(0, len(full))]),
    ]:
        out = fitz.open()
        for a, b in ranges:
            if b > a:
                out.insert_pdf(full, from_page=a, to_page=b - 1)
        an = annex_doc()
        out.insert_pdf(an)
        an.close()
        path = os.path.join(OUT, name)
        n, size, lourdes = finalize(out, path)
        out.close()
        print(f"{name:34s} {n:3d} pages   {size // 1024:5d} Ko   ({lourdes} page(s) scannée(s) recompressée(s))")

    mp = os.path.join(OUT, "MAIL-CAMPUS-FRANCE.pdf")
    md2pdf.render(open(os.path.join(SRC, "MAIL-CAMPUS-FRANCE-BOUCLY-CC.md"), encoding="utf-8").read(), mp,
                  "MINANG Calvin — dossier 110584Z — courriel Campus France, copie SKEMA — 07/10/2026")
    d = fitz.open(mp)
    try:
        d.subset_fonts()
    except Exception:
        pass
    tmp2 = mp + ".tmp"
    d.save(tmp2, deflate=True, garbage=4, clean=True)
    d.close()
    os.replace(tmp2, mp)
    print(f"{'MAIL-CAMPUS-FRANCE.pdf':34s} 3 pages   {os.path.getsize(mp) // 1024:5d} Ko")
    os.remove(tmp)
    print("annexes:", ", ".join(re.sub(r"\.pdf$", "", f) for f, _ in ANNEXES))


if __name__ == "__main__":
    main()
