#!/usr/bin/env python3
"""
CV « vitrine » de Cléanne MINANG — génération PDF A4 (fpdf2).

    python3 documents/cv-cleanne/build_cv.py

Sortie : documents/cv-cleanne/CV_Cleanne_MINANG.pdf
Polices : Lora (titres) + Source Sans 3 (texte), SIL Open Font License
          (voir fonts/LICENSE-OFL.txt).

Tout le contenu éditable est dans la section CONTENU ci-dessous.
Densité : CV_SCALE (taille du texte) et CV_VSCALE (interlignage), en variables
d'environnement, pour tenir sur une page si le texte bouge.
"""

from __future__ import annotations

import os
from pathlib import Path

from fpdf import FPDF

HERE = Path(__file__).resolve().parent
FONTS = HERE / "fonts"
OUT = HERE / "CV_Cleanne_MINANG.pdf"

# ----------------------------------------------------------------------------
# Charte
# ----------------------------------------------------------------------------
NAVY = (23, 50, 77)        # #17324D — bleu encre
INK = (28, 32, 38)         # #1C2026 — corps de texte
MUTED = (108, 118, 130)    # #6C7682 — dates et mentions secondaires
SOFT = (150, 160, 170)     # séparateurs
SEP = "·"
RULE = (206, 213, 220)     # #CED5DC — filets
ACCENT = (23, 50, 77)

PW, PH = 210, 297
ML, MR = 17.0, 17.0
MT, MB = 14.0, 12.0
CW = PW - ML - MR

SERIF = "Lora"
SANS = "Source Sans 3"

S_NAME = 26.0
S_TAGLINE = 10.6
S_SUB = 9.4
S_CONTACT = 8.7
S_SECTION = 9.3
S_ROLE = 9.9
S_ORG = 9.3
S_META = 7.9
S_BODY = 9.15
S_BULLET = 8.95

SCALE = float(os.environ.get("CV_SCALE", "0.97"))
VSCALE = float(os.environ.get("CV_VSCALE", "0.92"))

NBSP = "\u00a0"


def ty(txt: str) -> str:
    """Typographie française : espaces insécables avant : ; ? ! % et dans les guillemets."""
    for ch in (":", ";", "?", "!", "%"):
        txt = txt.replace(f" {ch}", f"{NBSP}{ch}")
    txt = txt.replace("« ", f"«{NBSP}").replace(" »", f"{NBSP}»")
    txt = txt.replace(" — ", f"{NBSP}—{NBSP}")
    for n in ("500", "200", "100"):
        txt = txt.replace(f" {n}", f"{NBSP}{n}")
    return txt


# ----------------------------------------------------------------------------
# CONTENU — modifier ici
# ----------------------------------------------------------------------------
NAME = "Cléanne MINANG"
TAGLINE = "Économie & gestion · analyse, stratégie et affaires internationales"
SUBLINE = (
    "Licence à l'Université de Lille · McKinsey Skills for Success 2026 · "
    "MUNDUS, simulation des Nations unies de l'Université de Lille"
)
CONTACT = [
    "+33 7 45 42 93 53",
    "minangcalvin0@gmail.com",
    "Lille (59800)",
    "linkedin.com/in/cleanne-minang",
]

PROFIL = (
    "Étudiante en Licence Économie & Gestion à l'Université de Lille, après une classe "
    "préparatoire ECG (économie, mathématiques, culture générale). Sélectionnée en 2026 pour le "
    "programme Skills for Success de McKinsey & Company : résolution de problèmes, structuration "
    "d'analyse, gestion des risques et résilience. Rédaction hebdomadaire d'une analyse d'actualité "
    "internationale au sein de MUNDUS, simulation des Nations unies de l'Université de Lille. "
    "Orientation : conseil en stratégie, affaires publiques et organisations internationales."
)

EXPERIENCES = [
    {
        "role": "Skills for Success 2026",
        "org": "McKinsey & Company",
        "meta": "Programme de développement · 4 sessions · à distance",
        "date": "Oct. 2026",
        "bullets": [
            "Sélectionnée sur candidature pour un programme du cabinet destiné aux étudiants et "
            "jeunes diplômés en Europe : quatre sessions entre octobre et novembre 2026.",
            "Résolution de problèmes structurée : décomposition d'une problématique, construction "
            "d'arbres d'analyse et priorisation des hypothèses.",
            "Restitution d'une analyse et d'une recommandation en temps limité ; échanges avec des "
            "consultants du cabinet sur les métiers du conseil, la gestion des risques et la "
            "résilience.",
        ],
    },
    {
        "role": "Pôle presse et communication",
        "org": "MUNDUS — Model of the United Nations, Université de Lille",
        "meta": "Association · actualité internationale et décryptages",
        "date": "2026",
        "bullets": [
            "Rédaction hebdomadaire d'une analyse d'actualité internationale pour « Le Monde en "
            "7 actus » : choix du sujet, recherche et vérification des sources, rédaction, mise en "
            "page.",
            "Veille géopolitique et contribution aux formats éditoriaux de l'association : "
            "décryptages, « Carte sur table », articles de fond.",
            "Coordination éditoriale : découpage des sujets, calendrier de publication, répartition "
            "entre contributeurs et suivi des délais.",
        ],
    },
    {
        "role": "Agent d'accueil et d'orientation clientèle",
        "org": "Stade Bollaert-Delelis — RC Lens",
        "meta": "Intérim · jours de match",
        "date": "Avr. — Oct. 2026",
        "bullets": [
            "Accueil et orientation de plus de 3 500 spectateurs par jour de match : information, "
            "gestion des flux et traitement des demandes en temps réel.",
            "Application des consignes de sécurité et de présentation ; mission renouvelée en "
            "octobre 2026 au vu de la qualité du service rendu.",
        ],
    },
    {
        "role": "Chargée de production, formation et accueil",
        "org": "Association audiovisuelle et communication",
        "meta": "Bénévolat · production et coordination d'événements",
        "date": "2023 — 2025",
        "bullets": [
            "Coordination de productions audiovisuelles événementielles : régie live (écosystème "
            "ATEM) et liaison entre les pôles techniques et créatifs.",
            "Formation et intégration des nouveaux membres aux procédures et outils techniques.",
            "Organisation logistique d'événements : préparation des espaces, installation du "
            "matériel, accueil des participants et intervenants.",
        ],
    },
]

FORMATION = [
    {
        "role": "Licence Économie & Gestion",
        "org": "Université de Lille",
        "meta": "Parcours Économie et Management des Entreprises · en cours",
        "date": "2024 — en cours",
        "bullets": [
            "Économie, gestion d'entreprise, comptabilité, statistiques et analyse de données.",
        ],
    },
    {
        "role": "Classe préparatoire ECG — économie et commerce, voie générale",
        "org": "Lycée Gaston Berger, Lille",
        "meta": "Formation intensive et sélective",
        "date": "2023 — 2024",
        "bullets": [
            "Économie, mathématiques appliquées, culture générale et langues vivantes ; entraînement "
            "quotidien à l'analyse rapide et à l'expression écrite comme orale.",
            "Admise après un baccalauréat général série ES — Lycée Nelson Mandela, Libreville (2023).",
        ],
    },
]

COMPETENCES = [
    ("Analyse & stratégie",
     "structuration de problème, analyse et synthèse, analyse chiffrée, recherche documentaire, veille"),
    ("Gestion de projet",
     "planification, coordination d'équipes, suivi des délais, organisation d'événements"),
    ("Outils & data",
     "Excel, Word, PowerPoint, outils de mise en page et de publication"),
    ("Communication",
     "rédaction analytique, prise de parole, relation client, animation de réunions"),
]

LANGUES = (
    "Français — langue maternelle · Anglais — B1 (intermédiaire) · "
    "Espagnol — B1 (intermédiaire) · Italien — notions"
)
INTERETS = (
    "Géopolitique et actualité internationale · Débats et simulation des Nations unies (MUNDUS) · "
    "Course à pied et natation · Chant et vie associative"
)


# ----------------------------------------------------------------------------
# Moteur de rendu
# ----------------------------------------------------------------------------
class CV(FPDF):
    def __init__(self) -> None:
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(False)
        self.set_margins(ML, MT, MR)
        self.set_compression(True)
        f = FONTS
        self.add_font(SERIF, "", str(f / "Lora_400Regular.ttf"))
        self.add_font(SERIF, "B", str(f / "Lora_600SemiBold.ttf"))
        self.add_font(SANS, "", str(f / "SourceSans3_400Regular.ttf"))
        self.add_font(SANS, "I", str(f / "SourceSans3_400Regular_Italic.ttf"))
        self.add_font(SANS, "B", str(f / "SourceSans3_600SemiBold.ttf"))


def fs(size: float) -> float:
    return size * SCALE


def sh(mm: float) -> float:
    return mm * SCALE * VSCALE


def width_of(pdf: FPDF, txt: str, font: str, style: str, size: float, tracking: float = 0.0) -> float:
    pdf.set_font(font, style, fs(size))
    pdf.set_char_spacing(tracking)
    val = pdf.get_string_width(ty(txt))
    pdf.set_char_spacing(0)
    return val


def text(pdf: FPDF, x, y, txt, font, style, size, color, tracking=0.0, align="L", width=0.0):
    """Écrit une ligne de texte. align='R' aligne à droite de [x, x+width]."""
    pdf.set_font(font, style, fs(size))
    pdf.set_char_spacing(tracking)
    pdf.set_text_color(*color)
    s = ty(txt)
    if align == "R" and width:
        x = x + width - pdf.get_string_width(s) - tracking * max(len(s) - 1, 0)
    pdf.set_xy(x, y)
    pdf.cell(0, 0, s)
    pdf.set_char_spacing(0)


def section(pdf: CV, y: float, title: str) -> float:
    """Titre de section : carré d'accent + libellé capitales + filet jusqu'à la marge."""
    pdf.set_fill_color(*ACCENT)
    pdf.rect(ML, y + 0.6, 2.0, 2.0, style="F")

    tx = ML + 4.8
    label = title.upper()
    text(pdf, tx, y, label, SERIF, "B", S_SECTION, NAVY, tracking=0.75)
    tw = width_of(pdf, label, SERIF, "B", S_SECTION, 0.75)
    x1 = tx + tw + 4.2
    pdf.set_draw_color(*RULE)
    pdf.set_line_width(0.35)
    if PW - MR > x1 + 2:
        pdf.line(x1, y + 1.5, PW - MR, y + 1.5)
    return y + sh(5.4)


def entry(pdf: CV, y: float, item: dict) -> float:
    text(pdf, ML, y, item["role"], SANS, "B", S_ROLE, INK)
    text(pdf, ML, y + 0.1, item["date"], SANS, "", S_META, MUTED, align="R", width=CW)
    y += sh(4.5)

    org = item["org"]
    org_w = width_of(pdf, org, SANS, "B", S_ORG - 0.3)
    text(pdf, ML, y, org, SANS, "B", S_ORG - 0.3, NAVY)
    if item.get("meta"):
        text(pdf, ML + org_w + 2.6, y + 0.05, item["meta"], SANS, "I", S_META + 0.35, MUTED)
    y += sh(4.4)

    for b in item.get("bullets", []):
        y = bullet(pdf, y, b)
    return y + sh(2.1)


def bullet(pdf: CV, y: float, txt: str) -> float:
    indent = 4.2
    pdf.set_draw_color(*NAVY)
    pdf.set_line_width(0.45)
    pdf.line(ML + 0.4, y + 1.45, ML + 2.6, y + 1.45)

    pdf.set_font(SANS, "", fs(S_BULLET))
    pdf.set_text_color(*INK)
    pdf.set_xy(ML + indent, y)
    pdf.multi_cell(CW - indent, sh(3.95), ty(txt), align="J")
    return pdf.get_y() + sh(1.05)


def labeled_row(pdf: CV, y: float, label: str, value: str) -> float:
    label_w = 30.0
    text(pdf, ML, y, label, SANS, "B", S_BODY - 0.2, NAVY)
    pdf.set_font(SANS, "", fs(S_BODY - 0.2))
    pdf.set_text_color(*INK)
    pdf.set_xy(ML + label_w, y)
    pdf.multi_cell(CW - label_w, sh(3.95), ty(value), align="L")
    return pdf.get_y() + sh(1.4)


def paragraph(pdf: CV, y: float, value: str) -> float:
    pdf.set_font(SANS, "", fs(S_BODY - 0.2))
    pdf.set_text_color(*INK)
    pdf.set_xy(ML, y)
    pdf.multi_cell(CW, sh(3.95), ty(value), align="J")
    return pdf.get_y() + sh(1.2)


# ----------------------------------------------------------------------------
# Composition
# ----------------------------------------------------------------------------
def build() -> Path:
    pdf = CV()
    pdf.add_page()

    # ---- en-tête -----------------------------------------------------------
    y = MT
    text(pdf, ML, y, NAME.upper(), SERIF, "B", S_NAME, NAVY, tracking=0.9)
    y += sh(9.6)

    text(pdf, ML, y, TAGLINE, SANS, "B", S_TAGLINE, INK)
    y += sh(5.4)

    text(pdf, ML, y, SUBLINE, SANS, "", S_SUB, MUTED)
    y += sh(5.8)

    text(pdf, ML, y, f" {SEP} ".join(CONTACT), SANS, "", S_CONTACT, MUTED)
    y += sh(5.4)

    pdf.set_draw_color(*NAVY)
    pdf.set_line_width(0.6)
    pdf.line(ML, y, PW - MR, y)
    y += sh(6.9)

    # ---- profil ------------------------------------------------------------
    y = section(pdf, y, "Profil")
    pdf.set_font(SANS, "", fs(S_BODY))
    pdf.set_text_color(*INK)
    pdf.set_xy(ML, y)
    pdf.multi_cell(CW, sh(4.15), ty(PROFIL), align="J")
    y = pdf.get_y() + sh(4.8)

    # ---- expériences -------------------------------------------------------
    y = section(pdf, y, "Expériences & engagements")
    for item in EXPERIENCES:
        y = entry(pdf, y, item)
    y += sh(2.4)

    # ---- formation ---------------------------------------------------------
    y = section(pdf, y, "Formation")
    for item in FORMATION:
        y = entry(pdf, y, item)
    y += sh(2.4)

    # ---- compétences -------------------------------------------------------
    y = section(pdf, y, "Compétences")
    for label, value in COMPETENCES:
        y = labeled_row(pdf, y, label, value)
    y += sh(2.6)

    # ---- langues -----------------------------------------------------------
    y = section(pdf, y, "Langues")
    y = paragraph(pdf, y, LANGUES)
    y += sh(2.4)

    # ---- centres d'intérêt -------------------------------------------------
    y = section(pdf, y, "Centres d'intérêt")
    y = paragraph(pdf, y, INTERETS)

    pdf.set_y(y)
    pdf.set_title("CV — Cléanne MINANG")
    pdf.set_author("Cléanne MINANG")
    pdf.set_subject("CV — Licence Économie & Gestion, Université de Lille")
    pdf.set_keywords("CV, économie, gestion, analyse, communication, Lille")
    pdf.set_creator("Cléanne MINANG")
    pdf.output(str(OUT))
    return OUT


if __name__ == "__main__":
    path = build()
    print(f"PDF écrit : {path}")

    import pymupdf

    doc = pymupdf.open(str(path))
    page = doc[0]
    bottom = max(b[3] for b in page.get_text("blocks")) / 72 * 25.4
    chars = len(page.get_text())
    print(f"pages={doc.page_count}  bas du texte={bottom:.1f} mm  "
          f"(limite {PH - MB:.0f} mm)  caractères extraits={chars}")
