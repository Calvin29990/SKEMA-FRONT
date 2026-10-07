#!/usr/bin/env python3
"""dossier-unique.py — rendu « mémoire » d'un document unique et codé couleur, pour tous les acteurs.

  skema-litige/pdf/DOSSIER-UNIQUE-MINANG-2026.pdf
      page de garde (identité, préambule, plan paginé, contexte, code de lecture)
      + corps   (skema-litige/DOSSIER-UNIQUE-2026.md, sections teintées par destinataire)
      + annexes A à L, chacune ouverte par un feuillet de renvoi à la couleur de son lecteur
      + numérotation bas de page, polices embarquées, aucune consigne d'exécution.

Usage : python3 skema-litige/outils/dossier-unique.py
"""
import os
import re
import sys
import tempfile

import pymupdf as fitz

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, ".."))
PIECES = os.path.join(BASE, "pieces")
OUT = os.path.join(BASE, "pdf")
sys.path.insert(0, HERE)
import md2pdf  # noqa: E402
from md2pdf import ACCENTS, FONTS, F  # noqa: E402

BODY_MD = os.path.join(BASE, "DOSSIER-UNIQUE-2026.md")
RECOURS_MD = os.path.join(BASE, "PARENTS-ANBG", "RECOURS-GRACIEUX-ANBG.md")
FOOT = "Calvin B. MINANG — dossier 110584Z — ANBG / Campus France / SKEMA Business School"

W, H = fitz.paper_size("a4")
ML, MR, MT = 56.0, 56.0, 60.0

PRÉAMBULE = (
    "Le présent dossier est établi sur pièces, à l'appui de trois démarches conduites simultanément : "
    "la créance de scolarité portée par SKEMA Business School au titre de l'année 2025/2026, la facture "
    "n° 1281253 de cet établissement rejetée par le service financier de Campus France depuis le "
    "25 septembre 2025, et les trois décisions de la Commission Technique de l'Agence Nationale des "
    "Bourses du Gabon des 25 septembre 2024, 17 février 2025 et 10 novembre 2025. Son objet est de "
    "permettre à chaque destinataire de disposer, dans un document unique, de la totalité des éléments "
    "vérifiés, sans reprise ni reformulation. Les mentions entre guillemets reproduisent exactement le "
    "texte des documents cités ; chaque ligne des tableaux renvoie à une pièce annexée (A à L).")

CONTEXTE = (
    "Inscrit en Programme Grande École de SKEMA Business School le 1er septembre 2022, sous prise en "
    "charge de l'État gabonais exécutée par l'ANBG et Campus France, l'étudiant a vu ses droits supprimés "
    "le 25 septembre 2024 pour l'absence d'un relevé de notes portant sur une année de césure accomplie "
    "en entreprise, son recours clôturé le 17 février 2025 cinq minutes après la validation de la pièce "
    "demandée, et sa demande d'année 2025/2026 rejetée le 10 novembre 2025 par un motif référencé à un "
    "texte abrogé le 21 février 2025. La facture de l'établissement destinée à l'organisme payeur demeure "
    "en attente depuis le 25 septembre 2025 ; la créance de l'année 2025/2026, arrêtée à 14 840,00 €, "
    "est portée à la charge personnelle de l'étudiant par mise en demeure du 7 octobre 2026, alors que le "
    "cycle s'achève en décembre 2026 et que le titre de séjour expire le 30 janvier 2027.")

CODES = [
    ("commun", "Commun à tous les destinataires — §§ 1, 2, 6, 8, 9"),
    ("vert", "Lecture ANBG — § 4 : décisions, moyens, demandes"),
    ("bleu", "Lecture Campus France — § 5 : facture rejetée, bons de commande, demandes"),
    ("orange", "Lecture SKEMA Business School — § 3 : titre, assiette, exercice"),
    ("rouge", "Constats de discordance documentaire — § 7"),
]

IDENTITE = [
    ("Nom, prénoms", "MINANG Calvin Blanchard"),
    ("Né le / nationalité", "2 mai 2002, à Libreville (Gabon) — gabonaise"),
    ("Établissement", "SKEMA Business School — Programme Grande École"),
    ("Cycle", "MSc Corporate Financial Management, 2ᵉ année de Master"),
    ("N° étudiant", "0305476"),
    ("Référence du dossier", "110584Z"),
    ("Dossiers eBourse", "1LMK24 (2024-2025) · CA24B3 (2025-2026)"),
    ("Courriels", "calvin.minang@skema.edu · blanchardminang00@gmail.com"),
    ("Document", "Version 1.0 — établi le 8 octobre 2026, sur pièces"),
]

SECTIONS = ["1. Synthèse du dossier", "2. Identification et références",
            "3. SKEMA Business School — titre, assiette et exercice de la créance",
            "4. ANBG — les trois décisions et leur motivation",
            "5. Campus France — facture n° 1281253 et bons de commande",
            "6. Chronologie documentée, 2019 → 2026",
            "7. Constats de discordance documentaire",
            "8. Situation de l'étudiant et échéances",
            "9. Index des pièces annexées"]

# annexe : (lettre, [(fichier, pages à garder)], titre, ce qu'elle établit, couleur du lecteur)
ANNEXES = [
    ("A", None, "Recours gracieux formé contre les décisions des 25/09/2024 et 10/11/2025",
     "Acte introductif, signé et daté, reproduisant les quatre moyens exposés au § 4.2 et les sept demandes du § 4.3.", "vert", "recours"),
    ("B", [("attestation-anbg-maintien-2021.pdf", None)], "Attestation de maintien de paiement de bourse n° 100326-21-MAINTIEN",
     "Décision annuelle de la Commission Technique du 01/02/2021, catégorie C : le régime appliqué est celui de décisions successives d'année en année.", "vert"),
    ("C", [("attestation-anbg-attribution-2021-2022.pdf", None)], "Attestation d'attribution de bourse n° 100057-22-ACCORD",
     "« Pour une durée : 1 année(s), du 01/09/2021 au 31/08/2022 » — mention expresse de l'annualité de l'attribution.", "vert"),
    ("D", [("contradiction-campus-france.pdf", None)], "Filet « TR: Facture rejetée SFO n° 1281253 », quatre messages",
     "Rejet du 25/09/2025 pour certificat de scolarité manquant ou non conforme, demandes de pièces des 06/10 et 29/10/2025, réponse du 06/11/2025.", "bleu"),
    ("E", None, "Notifications de la plateforme eBourse, horodatées",
     "Six notifications du 25/09/2024 16:37 au 10/11/2025 15:47, reproduites au § 4.1, avec l'horodatage de consultation de l'espace étudiant.", "vert", "à produire"),
    ("F", [("attestation-PGE.pdf", None), ("attestation-assiduite-09-12-2025.pdf", None)],
     "Attestation du registraire du 14/05/2024 et attestation d'assiduité du 09/12/2025",
     "Calendrier certifié par l'établissement (césures, M2 en 2025/2026) ; présence régulière aux cours attestée vingt-neuf jours après l'avis défavorable.", "vert"),
    ("G", [("bon-de-commande-M1.pdf", None)], "Bon de commande n° 721622 du 06/05/2024 — 16 000,00 €",
     "« POUR LE COMPTE DE L'ANBG FRAIS FORMATION 2023 2024 », fournisseur 35025, dossier 110584Z : le circuit de prise en charge a été exécuté jusqu'en 2023/2024.", "bleu"),
    ("H", [("convention-stage-bpce-2024.pdf", [0, 1, 2])], "Convention de stage SKEMA Business School / BPCE du 04/01/2024",
     "Stage de six mois du 8 janvier au 5 juillet 2024, autorisé et signé par l'établissement : l'année dont le relevé était exigé était une année en entreprise.", "vert"),
    ("I", [("mise-en-demeure.pdf", [0])], "Mise en demeure du 7 octobre 2026, réf. 2026-SK.D-0002",
     "14 840,00 € au titre de l'année académique 2025/2026, paiement sous dix jours, cessation définitive de scolarité envisagée.", "orange"),
    ("J", [("contrat-signé.pdf", None), ("dossier-campus-caution.pdf", None)],
     "Contrat d'inscription Fall 2022 et dossier d'inscription (acte de cautionnement)",
     "Prix du cycle 46 000,00 € pour une durée « pouvant atteindre soixante mois », article 4.4 sur l'allongement d'une année, garant « ETAT GABONAIS » enregistré à l'inscription, règle de facturation du 24/01/2023.", "orange"),
    ("K", None, "Procuration donnée au porteur du dossier",
     "Pouvoir de remettre le recours et de retirer les documents, sans pouvoir de transaction ni de reconnaissance de dette.", "vert", "acte"),
    ("L", None, "Accusé de remise du recours — deux exemplaires, à viser par le service",
     "Enregistrement de la remise : numéro, date, service et agent, cachet.", "vert", "acte"),
]


def para(pg, text, y, size=9.8, lead=13.4, x=ML, width=W - ML - MR, color=(0.08, 0.08, 0.10), justify=True, fname="DJr"):
    font = FONTS["r"]
    """Paragraphe justifié (rendu maison, métriques exactes)."""
    ls = _lines(pg, text, size, width, font)
    sw = font.text_length(" ", size)
    for n, line in enumerate(ls):
        if justify and len(line) > 1 and n < len(ls) - 1:
            natural = sum(font.text_length(t, size) for t, _ in line) + sw * (len(line) - 1)
            gap = sw + (width - natural) / (len(line) - 1)
        else:
            gap = sw
        cx = x
        for t, st in line:
            pg.insert_text((cx, y + size * 0.80), t, fontname=fname, fontsize=size, color=color)
            cx += font.text_length(t, size) + gap
        y += lead
    return y


def _lines(pg, text, size, width, f):
    words = [(w, "r") for w in text.split()]
    lines, cur, cw = [], [], 0.0
    for w, st in words:
        ww = f.text_length(w, size)
        if cur and cw + ww > width:
            lines.append(cur)
            cur, cw = [(w, st)], ww
        else:
            cur.append((w, st))
            cw += ww + f.text_length(" ", size)
    if cur:
        lines.append(cur)
    return lines


def cover(doc, plans):
    pg = doc.new_page(width=W, height=H)
    pg.insert_font(fontname="DJr", fontfile=FFILE["r"])
    pg.insert_font(fontname="DJb", fontfile=FFILE["b"])
    pg.insert_font(fontname="DJi", fontfile=FFILE["i"])
    # bandeau
    pg.draw_rect(fitz.Rect(0, 0, W, 132), color=None, fill=(0.09, 0.12, 0.19))
    pg.draw_rect(fitz.Rect(0, 132, W, 136), color=None, fill=ACCENTS["vert"][0])
    pg.draw_rect(fitz.Rect(0, 136, W, 140), color=None, fill=ACCENTS["bleu"][0])
    pg.draw_rect(fitz.Rect(0, 140, W, 144), color=None, fill=ACCENTS["orange"][0])
    pg.insert_text((ML, 52), "DOSSIER DE SITUATION", fontname="DJb", fontsize=20, color=(1, 1, 1))
    pg.insert_text((ML, 84), "Prise en charge de bourse d'État et facturation scolaire", fontname="DJr", fontsize=12.4, color=(0.86, 0.89, 0.95))
    pg.insert_text((ML, 96), "ANBG · Campus France · SKEMA Business School — 2019-2026", fontname="DJr", fontsize=10.4, color=(0.70, 0.76, 0.86))
    pg.insert_text((ML, 119), "MINANG Calvin Blanchard", fontname="DJb", fontsize=13, color=(1, 1, 1))
    pg.insert_text((W - MR - FONTS["b"].text_length("Version 1.0 — 8 octobre 2026", 8.6), 119), "Version 1.0 — 8 octobre 2026", fontname="DJb", fontsize=8.6, color=(0.78, 0.83, 0.92))

    y = 170
    # identité
    _title(pg, "Identité et références", y)
    y += 21
    for k, v in IDENTITE:
        pg.insert_text((ML, y), k.upper(), fontname="DJb", fontsize=7.4, color=(0.34, 0.38, 0.46))
        pg.insert_text((ML + 150, y - 0.4), v, fontname="DJr", fontsize=9.5)
        pg.draw_line(fitz.Point(ML, y + 4.5), fitz.Point(W - MR, y + 4.5), width=0.28, color=(0.80, 0.82, 0.86))
        y += 13.2
    y += 8
    _title(pg, "Préambule", y)
    y += 20
    y = para(pg, PRÉAMBULE, y, 9.4, 12.6)
    y += 6
    _title(pg, "Contexte", y)
    y += 20
    y = para(pg, CONTEXTE, y, 9.4, 12.6)
    y += 10
    # plan
    _title(pg, "Plan du dossier", y)
    y += 19
    for s in plans:
        pg.insert_text((ML + 2, y), s, fontname="DJr", fontsize=9.6)
        dots = "." * max(2, int((W - MR - 96 - FONTS["r"].text_length(s, 9.6)) / 4.2))
        pg.insert_text((ML + 2 + FONTS["r"].text_length(s, 9.6) + 4, y - 1.2), dots, fontname="DJr", fontsize=7.5, color=(0.62, 0.64, 0.70))
        pg.insert_text((W - MR - 30, y), f"p. {plans[s]}", fontname="DJb", fontsize=9.0, color=(0.34, 0.38, 0.46))
        y += 12.8
    y += 8
    _title(pg, "Code de lecture", y)
    y += 18
    for key, lab in CODES:
        c = ACCENTS[key][0]
        pg.draw_rect(fitz.Rect(ML, y - 7.4, ML + 15, y + 1.6), color=None, fill=c)
        pg.insert_text((ML + 24, y), lab, fontname="DJr", fontsize=9.2)
        y += 13.2
    y += 4
    pg.insert_text((ML, y), "Un bandeau de couleur, dans la marge, signale la section destinée à chaque lecteur ; les carrés en tête de page", fontname="DJi", fontsize=8.4, color=(0.36, 0.38, 0.44))
    pg.insert_text((ML, y + 11), "rappellent les couleurs présentes sur la page. Les pièces A à L suivent le § 9, sans intercalaire d'exécution.", fontname="DJi", fontsize=8.4, color=(0.36, 0.38, 0.44))
    return pg


def _title(pg, txt, y):
    pg.draw_rect(fitz.Rect(ML - 8, y - 12, ML - 3.5, y + 3.5), color=None, fill=(0.09, 0.12, 0.19))
    pg.insert_text((ML, y), txt.upper(), fontname="DJb", fontsize=9.6, color=(0.09, 0.12, 0.19))
    pg.draw_line(fitz.Point(ML, y + 5.5), fitz.Point(W - MR, y + 5.5), width=0.6, color=(0.55, 0.58, 0.65))


def label(pg, lettre, titre, objet, key, sous_titre):
    c = ACCENTS[key][0]
    pg.draw_rect(fitz.Rect(0, 0, W, 92), color=None, fill=c)
    pg.insert_text((ML, 40), f"ANNEXE {lettre}", fontname="DJb", fontsize=19, color=(1, 1, 1))
    pg.insert_text((ML, 62), sous_titre, fontname="DJr", fontsize=10, color=(0.88, 0.90, 0.95))
    y = 122
    for line in _lines(pg, titre, 12.6, W - ML - MR, FONTS["b"]):
        pg.insert_text((ML, y), " ".join(t for t, _ in line), fontname="DJb", fontsize=12.6)
        y += 16.5
    y += 12
    y = para(pg, objet, y, 10.0, 13.8)
    pg.draw_rect(fitz.Rect(ML, y + 16, W - MR, y + 52), color=(0.72, 0.72, 0.74), width=0.6, fill=(0.965, 0.965, 0.975))
    pg.insert_text((ML + 12, y + 34), f"Pièce {lettre} du dossier · {ACCENTS[key][1]} · 12 pièces au total (A à L)", fontname="DJr", fontsize=9.2, color=(0.36, 0.38, 0.44))
    pg.insert_text((ML + 12, y + 46), f"{FOOT}", fontname="DJr", fontsize=8.0, color=(0.48, 0.50, 0.56))
    return pg


FFILE = md2pdf.FFILE
MAIN_TITLES = {
    "3. SKEMA": "orange", "4. ANBG": "vert", "5. Campus France": "bleu", "7. Constats": "rouge",
}


def main():
    os.makedirs(OUT, exist_ok=True)
    tmp = os.path.join(tempfile.gettempdir(), "corps.pdf")
    md2pdf.render(open(BODY_MD, encoding="utf-8").read(), tmp, "")
    corps = fitz.open(tmp)

    # pagination du plan : première page de chaque titre de section
    plans = {}
    for s in SECTIONS:
        cle = s[:9]
        for i, p in enumerate(corps):
            if cle in p.get_text().replace("\n", " ").replace("  ", " "):
                plans[s] = i + 2  # +1 index -> n°, +1 page de garde
                break
        plans.setdefault(s, "—")

    # annexe A : le recours signé, et K / L : procuration et accusé de remise, rendus depuis leur source
    rtmp = os.path.join(tempfile.gettempdir(), "recours.pdf")
    md2pdf.render(open(RECOURS_MD, encoding="utf-8").read(), rtmp, "")
    recours = fitz.open(rtmp)
    idx = {k: next((i for i, p in enumerate(recours) if k in p.get_text()), 0) for k in
           ("1. RECOURS GRACIEUX", "2. PROCURATION", "3. ACCUSÉ DE REMISE", "4. CHEMISE")}
    for k, v in idx.items():
        if v == 0 and not any(k[:6] in p.get_text() for p in recours):
            print(f"  ! section introuvable dans le recours : {k}")

    doc = fitz.open()
    cover(doc, plans)
    doc.insert_pdf(corps)

    def slice_of(a, b):
        out = fitz.open()
        out.insert_pdf(recours, from_page=a, to_page=(b - 1) if b is not None else recours.page_count - 1)
        return out

    for lettre, fichiers, titre, objet, key, *rest in ANNEXES:
        tag = rest[0] if rest else None
        src = None
        if tag == "recours":
            src = slice_of(idx["1. RECOURS GRACIEUX"], idx["2. PROCURATION"])
        elif tag == "acte" and lettre == "K":
            src = slice_of(idx["2. PROCURATION"], idx["3. ACCUSÉ DE REMISE"])
        elif tag == "acte" and lettre == "L":
            src = slice_of(idx["3. ACCUSÉ DE REMISE"], idx["4. CHEMISE"])
        lab = fitz.open()
        lp = lab.new_page(width=W, height=H)
        lp.insert_font(fontname="DJr", fontfile=FFILE["r"])
        lp.insert_font(fontname="DJb", fontfile=FFILE["b"])
        lp.insert_font(fontname="DJi", fontfile=FFILE["i"])
        label(lp, lettre, titre, objet, key, ACCENTS[key][1])
        doc.insert_pdf(lab)
        lab.close()
        if src is not None:
            doc.insert_pdf(src)
            src.close()
            continue
        if fichiers is None:
            continue
        for fn, keep in fichiers:
            path = os.path.join(PIECES, fn)
            if not os.path.exists(path):
                alt = os.path.join(PIECES, fn.replace("contrat-signé.pdf", "2733904447-Contrat-Signe.pdf"))
                path = alt if os.path.exists(alt) else None
                if path is None:
                    print(f"  ! pièce manquante pour l'annexe {lettre} : {fn}")
                    continue
            a = fitz.open(path)
            if keep:
                a.select([i for i in keep if i < a.page_count])
            doc.insert_pdf(a)
            a.close()
    recours.close()
    corps.close()
    os.remove(tmp)
    os.remove(rtmp)

    # numérotation bas de page (hors page de garde)
    for i in range(1, doc.page_count):
        p = doc[i]
        p.insert_font(fontname="DJr", fontfile=FFILE["r"])
        p.draw_line(fitz.Point(ML, H - 38), fitz.Point(W - MR, H - 38), width=0.35, color=(0.74, 0.75, 0.80))
        p.insert_text((W - MR - 42, H - 25), f"{i + 1}", fontname="DJr", fontsize=8.4, color=(0.30, 0.32, 0.38))
        p.insert_text((ML, H - 25), "Dossier de situation — v1.0 — 8 octobre 2026", fontname="DJr", fontsize=7.4, color=(0.48, 0.50, 0.56))

    try:
        doc.subset_fonts()
    except Exception:
        pass
    dest = os.path.join(OUT, "DOSSIER-UNIQUE-MINANG-2026.pdf")
    doc.save(dest, deflate=True, garbage=4, clean=True)
    print(f"DOSSIER-UNIQUE-MINANG-2026.pdf — {doc.page_count} pages, {os.path.getsize(dest)/1024:.0f} Ko")
    print("plan paginé :", ", ".join(f"{k.split('.')[0]}→p{v}" for k, v in plans.items()))
    doc.close()


if __name__ == "__main__":
    main()
