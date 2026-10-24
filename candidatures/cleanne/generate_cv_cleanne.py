#!/usr/bin/env python3
"""
Générateur de CV ATS-Friendly (PDF + DOCX) pour Cléanne MINANG.
Optimisé pour les filtres automatiques (Workday, SmartRecruiters, BrassRing, Taleo, Indeed, France Travail)
des enseignes Grande Distribution, Prêt-à-Porter, Restauration & Accueil autour de Lille Flandres / Euralille
(Carrefour, Primark, Uniqlo, H&M, Inditex/Zara, Monoprix, E.Leclerc, Intermarché, McDonald's, CRIT, etc.).
"""

from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
)

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


NAVY_HEX = "#17375E"
DARK_HEX = "#111111"
MUTED_HEX = "#333333"

NAVY_RL = HexColor(NAVY_HEX)
DARK_RL = HexColor(DARK_HEX)
MUTED_RL = HexColor(MUTED_HEX)

NAVY_RGB = RGBColor(0x17, 0x37, 0x5E)
DARK_RGB = RGBColor(0x11, 0x11, 0x11)
MUTED_RGB = RGBColor(0x33, 0x33, 0x33)


def get_cv_data(email: str) -> dict:
    return {
        "name": "CLÉANNE MINANG",
        "headline": "Employée / Vendeuse Polyvalente — Caisse, Mise en Rayon, Vente & Accueil Client",
        "subheadline": "Job Étudiant / CDI Temps Partiel (8h à 25h/sem.) — Disponibilité immédiate (dès 6h, soir, week-end & vacances)",
        "contact": f"+33 7 45 42 93 53  |  {email}  |  47 rue Vantroyen, 59800 Lille (7 min à pied Lille Flandres / Euralille)",
        "profile": (
            "Étudiante sérieuse, ponctuelle et dynamique en Licence Économie et Gestion à l'Université de Lille "
            "(issue de classe préparatoire ECG), résidant à proximité immédiate à pied des gares <b>Lille Flandres / "
            "Lille Europe et de Westfield Euralille</b>. Forte d'expériences concrètes en <b>accueil client à forte "
            "affluence</b> (Stade Bollaert-Delelis), en <b>coordination opérationnelle d'événements</b> et en "
            "<b>appui administratif</b>, j'allie sens du service client, esprit d'équipe sous cadence soutenue et "
            "aisance avec les chiffres. Opérationnelle immédiatement comme <b>employée commerciale, vendeuse polyvalente, "
            "hôtesse de caisse / d'accueil ou équipière polyvalente</b> en CDI étudiant ou temps partiel."
        ),
        "experiences": [
            {
                "title": "Stade Bollaert-Delelis (RC Lens) — Agent d'Accueil & Orientation Clientèle (Intérim)",
                "meta": "Agence d'intérim Caprisio, Lille  |  08/2026 – 10/2026 (2 vacations événementielles jour de match : août & octobre 2026)",
                "bullets": [
                    "<b>Accueil et gestion de flux à forte affluence :</b> réception, contrôle visuel et orientation de milliers de clients et spectateurs vers leurs tribunes, salons et accès dédiés lors de rencontres à plus de 35 000 personnes.",
                    "<b>Service et accompagnement client :</b> renseignement proactif, réponse rapide aux demandes pratiques, fluidification des files d'attente et maintien d'un accueil souriant et courtois sous pression.",
                    "<b>Fiabilité opérationnelle :</b> respect strict des consignes de sécurité, de présentation et de ponctualité ; mission renouvelée en octobre 2026 suite à la satisfaction de l'agence et du client en août 2026.",
                ],
            },
            {
                "title": "Association Audiovisuelle & Communication — Chargée d'Organisation, Accueil & Production",
                "meta": "Lille  |  2023 – 2025",
                "bullets": [
                    "<b>Organisation terrain et tenue des espaces :</b> préparation logistique des événements, installation, rangement et accueil physique des participants et intervenants.",
                    "<b>Coordination d'équipe en temps réel :</b> synchronisation opérationnelle entre les pôles techniques et communication sous délais serrés (gestion de régie live ATEM, suivi rigoureux des plannings).",
                    "<b>Polyvalence et réactivité :</b> résolution rapide des imprévus en direct, vérification du matériel et travail collaboratif en équipe pluridisciplinaire.",
                ],
            },
            {
                "title": "ABC Consulting — Assistante Polyvalente & Accueil Administratif (Bénévolat)",
                "meta": "Libreville, Gabon  |  2022",
                "bullets": [
                    "<b>Accueil physique et relation visiteurs :</b> réception, orientation des clients du cabinet et traitement des demandes courantes avec courtoisie et professionnalisme.",
                    "<b>Appui administratif et organisationnel :</b> classement, gestion documentaire, saisie bureautique (Pack Office) et soutien polyvalent à l'équipe selon les pics d'activité.",
                ],
            },
        ],
        "education": [
            {
                "title": "Université de Lille — Licence Économie et Gestion (Parcours Économie et Management des Entreprises)",
                "meta": "Lille  |  2024 – Présent (Statut étudiant actif 2026–2027)",
                "detail": "Compétences clés : gestion d'entreprise, suivi de stocks, analyse chiffrée, rigueur organisationnelle et outils bureautiques.",
            },
            {
                "title": "Lycée Gaston Berger — Classe Préparatoire ECG (Économique et Commerciale voie Générale)",
                "meta": "Lille  |  2023 – 2024",
                "detail": "Formation intensive : rapidité d'exécution, aisance en calcul mental, capacité de travail élevée, discipline et ponctualité.",
            },
            {
                "title": "Lycée Nelson Mandela — Baccalauréat Général Série ES (Économique et Social)",
                "meta": "Libreville  |  2022 – 2023 (Obtenu en 2023)",
                "detail": None,
            },
        ],
        "skills": [
            (
                "Vente, Magasin & Grande Distribution : ",
                "accueil et conseil client, mise en rayon, réassort, pliage, cintrage, rangement, facing, étiquetage, tenue de la surface de vente et des cabines d'essayage, réception et contrôle de livraisons, gestion de réserve/stocks, respect des normes d'hygiène et de sécurité.",
            ),
            (
                "Caisse, Relation Client & Chiffres : ",
                "forte aisance chiffrée et calcul mental (Prépa ECG / Licence Éco-Gestion), assimilation rapide des procédures d'encaissement (caisse classique & accompagnement caisses automatiques libre-service), retours/échanges, promotion carte de fidélité.",
            ),
            (
                "Savoir-être & Bureautique : ",
                "ponctualité irréprochable, sourire, écoute active, dynamisme, résistance au stress et à la station debout, travail d'équipe, maîtrise du Pack Office (Excel, Word, PowerPoint).",
            ),
            (
                "Disponibilités & Mobilité : ",
                "disponibilité immédiate en CDI étudiant / temps partiel (prise de poste matinale dès 6h00, après-midi, soirées, samedi, dimanche et temps plein vacances scolaires). Domicile à 7 min à pied de Lille Flandres, Lille Europe et Westfield Euralille.",
            ),
        ],
        "languages": (
            "<b>Français :</b> courant / bilingue  |  "
            "<b>Anglais :</b> niveau B1 (accueil et renseignement d'une clientèle internationale en gare / magasin)  |  "
            "<b>Espagnol :</b> niveau B1  |  "
            "<b>Italien :</b> notions"
        ),
        "interests": "Natation (pratique régulière, endurance), Chant, Réalisation audiovisuelle, Lecture & Culture.",
    }


def build_pdf(output_path: Path, data: dict) -> None:
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=24,
        bottomMargin=22,
        title=f"CV {data['name']} - Employée Vendeuse Polyvalente Lille",
        author="Cléanne MINANG",
        subject="CV ATS Employée Polyvalente / Vendeuse / Hôtesse de Caisse & Accueil - Lille Flandres Euralille",
        keywords="Employée polyvalente, Vendeuse polyvalente, Hôtesse de caisse, Agent d'accueil, Job étudiant, CDI temps partiel, Lille Flandres, Euralille, Carrefour, Primark",
    )

    s_name = ParagraphStyle(
        "Name",
        fontName="Helvetica-Bold",
        fontSize=18.0,
        leading=20.0,
        textColor=NAVY_RL,
        alignment=TA_CENTER,
        spaceAfter=1.5,
    )
    s_headline = ParagraphStyle(
        "Headline",
        fontName="Helvetica-Bold",
        fontSize=9.8,
        leading=12.0,
        textColor=DARK_RL,
        alignment=TA_CENTER,
        spaceAfter=1.0,
    )
    s_subheadline = ParagraphStyle(
        "SubHeadline",
        fontName="Helvetica-Bold",
        fontSize=8.6,
        leading=11.0,
        textColor=NAVY_RL,
        alignment=TA_CENTER,
        spaceAfter=2.0,
    )
    s_contact = ParagraphStyle(
        "Contact",
        fontName="Helvetica",
        fontSize=8.6,
        leading=10.5,
        textColor=DARK_RL,
        alignment=TA_CENTER,
        spaceAfter=4.5,
    )
    s_section = ParagraphStyle(
        "Section",
        fontName="Helvetica-Bold",
        fontSize=9.8,
        leading=11.5,
        textColor=NAVY_RL,
        alignment=TA_LEFT,
        spaceBefore=5.0,
        spaceAfter=1.5,
    )
    s_body = ParagraphStyle(
        "Body",
        fontName="Helvetica",
        fontSize=8.75,
        leading=11.3,
        textColor=DARK_RL,
        alignment=TA_JUSTIFY,
        spaceAfter=2.0,
    )
    s_item_title = ParagraphStyle(
        "ItemTitle",
        fontName="Helvetica-Bold",
        fontSize=9.0,
        leading=11.2,
        textColor=DARK_RL,
        alignment=TA_LEFT,
        spaceBefore=2.8,
        spaceAfter=0.5,
    )
    s_item_meta = ParagraphStyle(
        "ItemMeta",
        fontName="Helvetica-Oblique",
        fontSize=8.35,
        leading=10.3,
        textColor=MUTED_RL,
        alignment=TA_LEFT,
        spaceAfter=1.5,
    )
    s_bullet = ParagraphStyle(
        "Bullet",
        fontName="Helvetica",
        fontSize=8.6,
        leading=11.0,
        textColor=DARK_RL,
        leftIndent=10,
        firstLineIndent=-7,
        alignment=TA_LEFT,
        spaceAfter=1.2,
    )

    def add_section_header(story, title: str):
        story.append(Paragraph(title, s_section))
        story.append(
            HRFlowable(
                width="100%",
                thickness=0.8,
                color=NAVY_RL,
                spaceBefore=0,
                spaceAfter=3.0,
            )
        )

    story = []

    # Header
    story.append(Paragraph(data["name"], s_name))
    story.append(Paragraph(data["headline"], s_headline))
    story.append(Paragraph(data["subheadline"], s_subheadline))
    story.append(Paragraph(data["contact"], s_contact))

    # Profil
    add_section_header(story, "PROFIL PROFESSIONNEL")
    story.append(Paragraph(data["profile"], s_body))

    # Expérience Professionnelle
    add_section_header(story, "EXPÉRIENCE PROFESSIONNELLE")
    for exp in data["experiences"]:
        story.append(Paragraph(exp["title"], s_item_title))
        story.append(Paragraph(exp["meta"], s_item_meta))
        for b in exp["bullets"]:
            story.append(Paragraph(f"• {b}", s_bullet))

    # Formation
    add_section_header(story, "FORMATION")
    for edu in data["education"]:
        story.append(Paragraph(edu["title"], s_item_title))
        story.append(Paragraph(edu["meta"], s_item_meta))
        if edu["detail"]:
            story.append(Paragraph(f"• {edu['detail']}", s_bullet))

    # Compétences
    add_section_header(story, "COMPÉTENCES CLÉS & DISPONIBILITÉS")
    for label, content in data["skills"]:
        story.append(Paragraph(f"• <b>{label}</b>{content}", s_bullet))

    # Langues & Centres d'intérêt
    add_section_header(story, "LANGUES & CENTRES D'INTÉRÊT")
    story.append(Paragraph(f"• {data['languages']}", s_bullet))
    story.append(Paragraph(f"• <b>Centres d'intérêt :</b> {data['interests']}", s_bullet))

    doc.build(story)


def strip_html(text: str) -> list[tuple[str, bool]]:
    """Convert simple <b>...</b> markup into (segment, is_bold) runs for python-docx."""
    parts = []
    rem = text
    while "<b>" in rem:
        before, rest = rem.split("<b>", 1)
        if before:
            parts.append((before, False))
        bold_txt, rem = rest.split("</b>", 1)
        parts.append((bold_txt, True))
    if rem:
        parts.append((rem, False))
    return parts


def add_bottom_border(paragraph, color_hex="17375E", size="6"):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), size)
    bottom.set(qn("w:space"), "2")
    bottom.set(qn("w:color"), color_hex)
    pBdr.append(bottom)
    pPr.append(pBdr)


def build_docx(output_path: Path, data: dict) -> None:
    doc = Document()

    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(0.95)
        section.bottom_margin = Cm(0.9)
        section.left_margin = Cm(1.25)
        section.right_margin = Cm(1.25)

    style_normal = doc.styles["Normal"]
    style_normal.font.name = "Calibri"
    style_normal.font.size = Pt(9.2)
    style_normal.font.color.rgb = DARK_RGB

    def add_Rich_p(text: str, size=9.0, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=1.5, italic=False, color=DARK_RGB):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.04
        for seg, is_b in strip_html(text):
            r = p.add_run(seg)
            r.font.name = "Calibri"
            r.font.size = Pt(size)
            r.bold = is_b
            r.italic = italic
            r.font.color.rgb = color
        return p

    def add_sec_title(title: str):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(4.5)
        p.paragraph_format.space_after = Pt(2.0)
        r = p.add_run(title)
        r.font.name = "Calibri"
        r.font.size = Pt(10.0)
        r.bold = True
        r.font.color.rgb = NAVY_RGB
        add_bottom_border(p)

    # Header
    add_Rich_p(f"<b>{data['name']}</b>", size=17.5, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0.5, color=NAVY_RGB)
    add_Rich_p(f"<b>{data['headline']}</b>", size=9.8, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0.5)
    add_Rich_p(f"<b>{data['subheadline']}</b>", size=8.7, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=1.5, color=NAVY_RGB)
    add_Rich_p(data["contact"], size=8.6, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=3)

    # Profil
    add_sec_title("PROFIL PROFESSIONNEL")
    add_Rich_p(data["profile"], size=8.9, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=1.5)

    # Expériences
    add_sec_title("EXPÉRIENCE PROFESSIONNELLE")
    for exp in data["experiences"]:
        add_Rich_p(f"<b>{exp['title']}</b>", size=9.1, space_before=2.0, space_after=0.3)
        add_Rich_p(exp["meta"], size=8.4, italic=True, space_after=1.0, color=MUTED_RGB)
        for b in exp["bullets"]:
            p = add_Rich_p(f"• {b}", size=8.75, space_after=0.9)
            p.paragraph_format.left_indent = Cm(0.35)
            p.paragraph_format.first_line_indent = Cm(-0.25)

    # Formation
    add_sec_title("FORMATION")
    for edu in data["education"]:
        add_Rich_p(f"<b>{edu['title']}</b>", size=9.1, space_before=1.8, space_after=0.3)
        add_Rich_p(edu["meta"], size=8.4, italic=True, space_after=0.8, color=MUTED_RGB)
        if edu["detail"]:
            p = add_Rich_p(f"• {edu['detail']}", size=8.75, space_after=0.9)
            p.paragraph_format.left_indent = Cm(0.35)
            p.paragraph_format.first_line_indent = Cm(-0.25)

    # Compétences
    add_sec_title("COMPÉTENCES CLÉS & DISPONIBILITÉS")
    for label, content in data["skills"]:
        p = add_Rich_p(f"• <b>{label}</b>{content}", size=8.75, space_after=1.0)
        p.paragraph_format.left_indent = Cm(0.35)
        p.paragraph_format.first_line_indent = Cm(-0.25)

    # Langues & Intérêts
    add_sec_title("LANGUES & CENTRES D'INTÉRÊT")
    p1 = add_Rich_p(f"• {data['languages']}", size=8.75, space_after=0.9)
    p1.paragraph_format.left_indent = Cm(0.35)
    p1.paragraph_format.first_line_indent = Cm(-0.25)
    p2 = add_Rich_p(f"• <b>Centres d'intérêt :</b> {data['interests']}", size=8.75, space_after=0)
    p2.paragraph_format.left_indent = Cm(0.35)
    p2.paragraph_format.first_line_indent = Cm(-0.25)

    doc.save(str(output_path))


def main():
    out_dir = Path(__file__).resolve().parent

    variants = [
        ("CV_Cleanne_MINANG_ATS_2026", "minangcalvin0@gmail.com"),
        ("CV_Cleanne_MINANG_ATS_EmailPerso", "minangclolina@gmail.com"),
    ]

    for stem, email in variants:
        data = get_cv_data(email)
        pdf_path = out_dir / f"{stem}.pdf"
        docx_path = out_dir / f"{stem}.docx"
        build_pdf(pdf_path, data)
        build_docx(docx_path, data)
        print(f"Generated: {pdf_path.name} & {docx_path.name} ({email})")


if __name__ == "__main__":
    main()
