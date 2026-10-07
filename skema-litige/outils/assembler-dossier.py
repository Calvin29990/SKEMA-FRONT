#!/usr/bin/env python3
"""assembler-dossier.py — construit les fichiers prêts à imprimer / à envoyer.

  pdf/DOSSIER-PARENTS-ANBG.pdf   UN SEUL fichier pour les parents : dossier déjà daté, nommé,
                                 complet, suivi des 7 annexes. Nothing to write.
  pdf/MAIL-CAMPUS-FRANCE.pdf     le courriel à copier-coller (2-3 pages, sans les annexes internes)
  pdf/pieces-mail/*.pdf + zip    les 7 pièces jointes, déjà renommées comme dans le courriel

Régénère aussi pdf/07-recours-gracieux-ANBG.pdf (extrait du dossier parents) pour la pièce jointe n° 7.

Usage : python3 skema-litige/outils/assembler-dossier.py
"""
import os
import re
import sys
import tempfile
import zipfile

import pymupdf as fitz

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, ".."))
SRC = os.path.join(BASE, "PARENTS-ANBG")
PIECES = os.path.join(BASE, "pieces")
OUT = os.path.join(SRC, "pdf")
MAILDIR = os.path.join(OUT, "pieces-mail")
sys.path.insert(0, HERE)
import md2pdf  # noqa: E402

FOOT = "MINANG Calvin — dossier ANBG 110584Z — sessions 2024-2025 et 2025-2026 — octobre 2026"
N_AN = 10  # dernière annexe

# annexe : (n°, fichier dans pieces/ ou None si page à imprimer par l'étudiant, légende, 1re page seule ?)
ANNEXES = [
    (4, None, "Captures d'écran de la plateforme eBourse : 25/09/2024 16:37 · 17/02/2025 11:06 · 17/02/2025 11:11 · 10/11/2025 15:47 · 23/07/2025 11:44. À imprimer depuis l'espace étudiant anbg.online, onglet Messages, en laissant visible l'horodatage de consultation", False),
    (5, "attestation-assiduite-09-12-2025.pdf", "Attestation de SKEMA Business School du 9 décembre 2025, signée Mme Sophie Gay, Directrice de l'Expérience Étudiant : inscription régulière pour 2025-2026 et présence régulière aux cours. Délivrée vingt-neuf jours après l'avis défavorable du 10/11/2025", False),
    (6, "attestation-PGE.pdf", "Attestation « Programme Grande École » du registraire de SKEMA Business School du 14 mai 2024 : césure Spring 24, césure Fall 24, M2 en 2025/2026. Établit que l'année sans relevé était une année de césure", False),
    (7, "bon-de-commande-M1.pdf", "Bon de commande Campus France n° 721622 du 6 mai 2024 — 16 000,00 €, dossier 110584Z, fournisseur 35025 SKEMA, ligne « pour le compte de l'ANBG — frais formation 2023 2024 »", False),
    (8, "convention-stage-bpce-2024.pdf", "Convention de stage SKEMA Business School / BPCE du 4 janvier 2024 : six mois en entreprise, du 8 janvier au 5 juillet 2024, autorisée et signée par l'établissement", False),
    (9, "mise-en-demeure.pdf", "Mise en demeure de SKEMA Business School du 7 octobre 2026, réf. 2026-SK.D-0002 : 14 840,00 € au titre de l'année 2025/2026, paiement sous dix jours — pièce justificative de l'urgence de la demande de documents", True),
    (10, "attestation-anbg-maintien-2021.pdf;attestation-anbg-attribution-2021-2022.pdf", "Deux décisions annuelles de la Commission Technique, catégorie C : attestation de maintien n° 100326-21-MAINTIEN (CPGE 2, Maroc, valable au 30/09/2021) puis attestation d'attribution n° 100057-22-ACCORD (année préparatoire IPESUP Paris, du 01/09/2021 au 31/08/2022), mention expresse « pour une durée : 1 année(s) »", False),
]


def _wrap(font, text, size, width):
    out, cur = [], ""
    for w in text.split():
        if font.text_length((cur + " " + w).strip(), size) > width:
            out.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        out.append(cur)
    return out


def annex_page(num, legende, titre):
    doc = fitz.open()
    pg = doc.new_page(width=fitz.paper_size("a4")[0], height=fitz.paper_size("a4")[1])
    pg.insert_font(fontname="DJr", fontfile=md2pdf.FFILE["r"])
    pg.insert_font(fontname="DJb", fontfile=md2pdf.FFILE["b"])
    W = pg.rect.width
    pg.draw_rect(fitz.Rect(50, 60, W - 50, 108), color=None, fill=(0.11, 0.14, 0.20))
    pg.insert_text((60, 86), f"ANNEXE {num} SUR {N_AN}", fontname="DJb", fontsize=15, color=(1, 1, 1))
    pg.insert_text((60, 101), "MINANG Calvin — dossier 110584Z", fontname="DJr", fontsize=8.5, color=(0.80, 0.84, 0.90))
    y = 138
    pg.insert_font(fontname="DJb", fontfile=md2pdf.FFILE["b"])
    for ln in _wrap(fitz.Font(fontfile=md2pdf.FFILE["b"]), titre, 12.2, W - 100):
        pg.insert_text((50, y), ln, fontname="DJb", fontsize=12.2)
        y += 16.5
    y += 10
    for ln in _wrap(fitz.Font(fontfile=md2pdf.FFILE["r"]), legende, 10.2, W - 100):
        pg.insert_text((50, y), ln, fontname="DJr", fontsize=10.2, color=(0.18, 0.18, 0.18))
        y += 14.4
    if num == 4:
        pg.draw_rect(fitz.Rect(50, y + 22, W - 50, y + 122), color=(0.60, 0.60, 0.60), width=1.2, dashes="[3 3] 0 0")
        pg.insert_text((62, y + 50), "[ PIÈCES À IMPRIMER PAR L'ÉTUDIANT, PUIS À AGRAFER ICI ]", fontname="DJr", fontsize=10)
        pg.insert_text((62, y + 68), "Aucune de ces pages n'est à écrire par le porteur :", fontname="DJr", fontsize=10)
        pg.insert_text((62, y + 84), "si elles manquent, le dossier reste parfaitement recevable.", fontname="DJr", fontsize=10)
    pg.insert_text((50, pg.rect.height - 54), FOOT, fontname="DJr", fontsize=7.6, color=(0.42, 0.42, 0.42))
    return doc


def finalize(src_doc, path):
    """Pages scannées lourdes -> JPEG 150 dpi ; sous-embedding des polices ; enregistrement compact."""
    heavy = set()
    for i, pg in enumerate(src_doc):
        poids = 0
        for im in pg.get_images(full=True):
            try:
                poids += len(src_doc.extract_image(im[0])[1])
            except Exception:
                pass
        if poids > 250 * 1024:
            heavy.add(i)
    out = fitz.open()
    for i, pg in enumerate(src_doc):
        if i in heavy:
            img = pg.get_pixmap(dpi=150).tobytes("jpeg", jpg_quality=62)
            np = out.new_page(width=pg.rect.width, height=pg.rect.height)
            np.insert_image(np.rect, stream=img)
        else:
            out.insert_pdf(src_doc, from_page=i, to_page=i)
    try:
        out.subset_fonts()
    except Exception:
        pass
    out.save(path, deflate=True, garbage=4, clean=True)
    n, size = out.page_count, os.path.getsize(path)
    out.close()
    return n, size, len(heavy)


def main():
    for d in (OUT, MAILDIR):
        os.makedirs(d, exist_ok=True)
    tmp = os.path.join(tempfile.gettempdir(), "dossier_parents.pdf")
    md2pdf.render(open(os.path.join(SRC, "RECOURS-GRACIEUX-ANBG.md"), encoding="utf-8").read(), tmp, FOOT)

    full = fitz.open(tmp)
    # extrait autonome du recours signé (pièce jointe n° 7 du courriel Campus France)
    i_rec = next(i for i, p in enumerate(full) if "1. RECOURS GRACIEUX" in p.get_text())
    i_pro = next(i for i, p in enumerate(full) if "2. PROCURATION" in p.get_text())
    rec = fitz.open()
    rec.insert_pdf(full, from_page=i_rec, to_page=i_pro - 1)
    try:
        rec.subset_fonts()
    except Exception:
        pass
    rec.save(os.path.join(MAILDIR, "07-recours-gracieux-ANBG.pdf"), deflate=True, garbage=4, clean=True)
    n_rec = rec.page_count
    rec.close()

    parents = fitz.open()
    parents.insert_pdf(full)
    for num, fn, legende, one in ANNEXES:
        if fn is None:
            parents.insert_pdf(annex_page(num, legende, "Pièce à imprimer depuis la plateforme eBourse"))
            continue
        first = True
        for sub in fn.split(";"):
            src = fitz.open(os.path.join(PIECES, sub))
            if one:
                src.select([0])
            if first:
                titre = src[0].get_text().strip().split("\n")[0][:74] or "Pièce jointe au recours"
                parents.insert_pdf(annex_page(num, legende, titre))
                first = False
            parents.insert_pdf(src)
            src.close()
    n_p, s_p, _ = finalize(parents, os.path.join(OUT, "DOSSIER-PARENTS-ANBG.pdf"))
    parents.close()
    full.close()
    os.remove(tmp)

    mp = os.path.join(OUT, "MAIL-CAMPUS-FRANCE.pdf")
    tmp2 = os.path.join(tempfile.gettempdir(), "mail_raw.pdf")
    md2pdf.render(open(os.path.join(SRC, "MAIL-CAMPUS-FRANCE-BOUCLY-CC.md"), encoding="utf-8").read(), tmp2,
                  "MINANG Calvin — dossier 110584Z — courriel Campus France, copie SKEMA — 8 octobre 2026")
    _d = fitz.open(tmp2)
    finalize(_d, mp)
    _d.close()
    os.remove(tmp2)

    # pièces jointes du courriel, copiées sous les noms exacts cités dans le texte
    correspondances = {
        "01-filet-facture-rejetee-1281253.pdf": "contradiction-campus-france.pdf",
        "02-attestation-registraire-14-05-2024.pdf": "attestation-PGE.pdf",
        "03-attestation-assiduite-09-12-2025.pdf": "attestation-assiduite-09-12-2025.pdf",
        "04-convention-stage-BPCE-04-01-2024.pdf": "convention-stage-bpce-2024.pdf",
        "05-bon-de-commande-721622.pdf": "bon-de-commande-M1.pdf",
        "06-mise-en-demeure-2026-SK-D-0002.pdf": "mise-en-demeure.pdf",
    }
    for dst, srcf in correspondances.items():
        s = fitz.open(os.path.join(PIECES, srcf))
        if srcf == "mise-en-demeure.pdf":
            s.select([0])
        d2 = fitz.open()
        d2.insert_pdf(s)
        s.close()
        try:
            d2.subset_fonts()
        except Exception:
            pass
        d2.save(os.path.join(MAILDIR, dst), deflate=True, garbage=4, clean=True)
        d2.close()

    zp = os.path.join(OUT, "PIECES-MAIL-CAMPUS-FRANCE.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(os.listdir(MAILDIR)):
            z.write(os.path.join(MAILDIR, f), f)
        z.write(mp, "MAIL-CAMPUS-FRANCE-a-copier.pdf")

    print(f"DOSSIER-PARENTS-ANBG.pdf     {n_p:3d} pages  {s_p/1024:7.0f} Ko   (recours {n_rec} p. en pièce jointe 07)")
    print(f"MAIL-CAMPUS-FRANCE.pdf         {len(fitz.open(mp))} pages  {os.path.getsize(mp)/1024:7.0f} Ko")
    print(f"PIECES-MAIL-CAMPUS-FRANCE.zip  {os.path.getsize(zp)/1024:7.0f} Ko   {len(os.listdir(MAILDIR))} fichiers")


if __name__ == "__main__":
    main()
