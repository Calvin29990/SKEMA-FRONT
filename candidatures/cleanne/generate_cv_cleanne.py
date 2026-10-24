#!/usr/bin/env python3
"""
Générateur de CV ATS-Friendly (PDF + DOCX) pour Cléanne MINANG — Édition Rose & Noir + Chiffres Clés.
Optimisé pour passer à 100 % les filtres automatiques (Workday, SmartRecruiters, BrassRing, Taleo, Indeed, France Travail)
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
    HRFlowable,
)

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


# Palette Rose Chic + Noir Intense (féminine, moderne, contraste élevé & 100 % ATS-safe)
ROSE_HEX = "#B8336A"        # Rose framboise / vieux rose soutenu (titres, nom, chiffres clés)
ROSE_LIGHT_BG = "#FDF2F6"   # Rose poudré très doux (bandeau chiffres clés linéaire)
ROSE_BORDER_HEX = "#E4AAC2" # Filet rose délicat
BLACK_HEX = "#111111"       # Noir profond (texte principal)
MUTED_HEX = "#3A3A3A"       # Gris anthracite (dates & lieux)

ROSE_RL = HexColor(ROSE_HEX)
ROSE_BG_RL = HexColor(ROSE_LIGHT_BG)
ROSE_BORDER_RL = HexColor(ROSE_BORDER_HEX)
BLACK_RL = HexColor(BLACK_HEX)
MUTED_RL = HexColor(MUTED_HEX)

ROSE_RGB = RGBColor(0xB8, 0x33, 0x6A)
BLACK_RGB = RGBColor(0x11, 0x11, 0x11)
MUTED_RGB = RGBColor(0x3A, 0x3A, 0x3A)


def get_cv_data(email: str) -> dict:
    return {
        "name": "CLÉANNE MINANG",
        "headline": "Employée / Vendeuse Polyvalente — Caisse, Mise en Rayon, Vente & Accueil Client",
        "subheadline": "Job Étudiant / CDI Temps Partiel (8h à 25h/sem.) — Disponibilité immédiate (dès 6h, soir, week-end & vacances)",
        "contact": f"+33 7 45 42 93 53  |  {email}  |  51 rue de Tournai, 59800 Lille (2 min à pied Gare Lille Flandres / Euralille)",
        "key_metrics_pdf": (
            f"<font color='{ROSE_HEX}'><b>CHIFFRES CLÉS :</b></font>  "
            f"<font color='{ROSE_HEX}'><b>3+ mois</b></font> d'accueil &amp; relation client  •  "
            f"<font color='{ROSE_HEX}'><b>2 ans</b></font> d'asso audiovisuelle  •  "
            f"<font color='{ROSE_HEX}'><b>Formation</b></font> de personnes  •  "
            f"<font color='{ROSE_HEX}'><b>2 min à pied</b></font> de Lille Flandres"
        ),
        "key_metrics_docx": [
            ("CHIFFRES CLÉS :  ", True, True),
            ("3+ mois", True, True),
            (" d'accueil & relation client  •  ", False, False),
            ("2 ans", True, True),
            (" d'asso audiovisuelle  •  ", False, False),
            ("Formation", True, True),
            (" de personnes  •  ", False, False),
            ("2 min à pied", True, True),
            (" de Lille Flandres", False, False),
        ],
        "profile": (
            "Étudiante sérieuse, ponctuelle et dynamique en Licence Économie et Gestion à l'Université de Lille "
            "(issue de classe préparatoire ECG), résidant au <b>51 rue de Tournai à 2 min à pied de la Gare Lille "
            "Flandres et de Westfield Euralille</b>. Forte de <b>plus de 3 mois d'expérience cumulée au contact direct "
            "des clients et visiteurs</b> (accueil événementiel grand flux au Stade Bollaert-Delelis, assistanat "
            "d'accueil chez ABC Consulting) et de <b>2 ans de gestion de projets et formation d'équipes</b> en "
            "association, j'allie sens du service client, rapidité d'exécution et aisance chiffrée. Opérationnelle "
            "immédiatement comme <b>employée commerciale, vendeuse polyvalente, hôtesse de caisse / d'accueil ou "
            "équipière polyvalente</b>."
        ),
        "experiences": [
            {
                "title": "Stade Bollaert-Delelis (RC Lens) — Agent d'Accueil & Orientation Clientèle (Intérim)",
                "meta": "Agence d'intérim Caprisio, Lille  |  08/2026 – 10/2026 (2 vacations événementielles jour de match : août & octobre 2026)",
                "bullets": [
                    "<b>Accueil et gestion de flux à forte affluence (+35 000 personnes) :</b> réception, contrôle visuel et orientation de milliers de clients et spectateurs vers leurs tribunes, salons et accès dédiés.",
                    "<b>Service et accompagnement client :</b> renseignement proactif, résolution rapide des demandes pratiques, fluidification des files d'attente et maintien d'un accueil souriant sous forte cadence.",
                    "<b>Fiabilité reconnue :</b> respect strict des consignes de sécurité, de présentation et de ponctualité ; mission renouvelée en octobre 2026 suite à la satisfaction client d'août 2026.",
                ],
            },
            {
                "title": "Association Audiovisuelle & Communication — Chargée de Production, Formation & Accueil (2 ans)",
                "meta": "Lille  |  2023 – 2025",
                "bullets": [
                    "<b>Formation et accompagnement de personnes :</b> intégration, formation pratique et transmission des procédures opérationnelles et techniques (régie live ATEM, organisation terrain) aux nouveaux membres.",
                    "<b>Organisation événementielle et accueil public :</b> préparation logistique des espaces, rangement, installation du matériel et accueil physique des participants et intervenants lors des événements.",
                    "<b>Coordination d'équipe sous délais serrés :</b> pilotage en temps réel entre les pôles techniques et communication, gestion du stress et résolution immédiate des imprévus.",
                ],
            },
            {
                "title": "ABC Consulting — Assistante Polyvalente & Relation Visiteurs / Clients (3 mois)",
                "meta": "Libreville  |  2022",
                "bullets": [
                    "<b>Accueil client et orientation (3 mois en cabinet) :</b> réception quotidienne des clients et visiteurs, traitement courtois des demandes d'information et tenue soignée de l'espace d'accueil.",
                    "<b>Appui administratif et organisationnel :</b> classement, vérification documentaire, saisie bureautique (Pack Office) et soutien polyvalent à l'équipe selon les pics d'activité.",
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
                "accueil et conseil client, mise en rayon, réassort, pliage, cintrage, rangement, facing, étiquetage, tenue de la surface de vente et des cabines d'essayage, réception de livraisons, gestion de réserve/stocks, normes d'hygiène et sécurité.",
            ),
            (
                "Caisse, Relation Client & Formation : ",
                "aisance chiffrée et calcul mental (Prépa ECG / Éco-Gestion), assimilation rapide des logiciels d'encaissement (caisse classique & caisses automatiques libre-service), retours/échanges, fidélité, capacité à former et épauler ses collègues.",
            ),
            (
                "Savoir-être & Bureautique : ",
                "ponctualité irréprochable, sourire, écoute active, dynamisme, endurance en station debout, esprit d'équipe, Pack Office (Excel, Word, PowerPoint).",
            ),
            (
                "Disponibilités & Mobilité : ",
                "disponibilité immédiate en CDI étudiant / temps partiel (dès 6h00 le matin, après-midi, soirées, samedi, dimanche et temps plein vacances scolaires). Domicile au 51 rue de Tournai (2 min à pied de Lille Flandres & Westfield Euralille).",
            ),
        ],
        "languages": (
            "<b>Français :</b> courant / bilingue  |  "
            "<b>Anglais :</b> niveau B1 (accueil et orientation d'une clientèle internationale en gare / magasin)  |  "
            "<b>Espagnol :</b> niveau B1  |  "
            "<b>Italien :</b> notions"
        ),
        "interests": "Natation (pratique régulière, endurance), Chant, Réalisation audiovisuelle, Lecture & Vie associative.",
    }


def build_pdf(output_path: Path, data: dict) -> None:
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=35,
        rightMargin=35,
        topMargin=22,
        bottomMargin=20,
        title=f"CV {data['name']} - Employée Vendeuse Polyvalente Lille",
        author="Cléanne MINANG",
        subject="CV ATS Employée Polyvalente / Vendeuse / Hôtesse de Caisse & Accueil - Lille Flandres Euralille",
        keywords="Employée polyvalente, Vendeuse polyvalente, Hôtesse de caisse, Agent d'accueil, Formation, Job étudiant, CDI temps partiel, Lille Flandres, Euralille, Carrefour, Primark",
    )

    s_name = ParagraphStyle(
        "Name",
        fontName="Helvetica-Bold",
        fontSize=18.5,
        leading=20.5,
        textColor=ROSE_RL,
        alignment=TA_CENTER,
        spaceAfter=1.5,
    )
    s_headline = ParagraphStyle(
        "Headline",
        fontName="Helvetica-Bold",
        fontSize=9.7,
        leading=11.8,
        textColor=BLACK_RL,
        alignment=TA_CENTER,
        spaceAfter=1.0,
    )
    s_subheadline = ParagraphStyle(
        "SubHeadline",
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=10.8,
        textColor=ROSE_RL,
        alignment=TA_CENTER,
        spaceAfter=2.0,
    )
    s_contact = ParagraphStyle(
        "Contact",
        fontName="Helvetica",
        fontSize=8.5,
        leading=10.5,
        textColor=BLACK_RL,
        alignment=TA_CENTER,
        spaceAfter=5.0,
    )
    # Bandeau Chiffres Clés 100 % mono-colonne (Paragraph standard -> lecture ATS linéaire parfaite)
    s_metrics = ParagraphStyle(
        "Metrics",
        fontName="Helvetica",
        fontSize=7.85,
        leading=10.2,
        textColor=BLACK_RL,
        alignment=TA_CENTER,
        backColor=ROSE_BG_RL,
        borderColor=ROSE_BORDER_RL,
        borderWidth=0.6,
        borderPadding=(3.5, 4, 3.5, 4),
        spaceBefore=1.0,
        spaceAfter=5.0,
    )
    s_section = ParagraphStyle(
        "Section",
        fontName="Helvetica-Bold",
        fontSize=9.6,
        leading=11.4,
        textColor=ROSE_RL,
        alignment=TA_LEFT,
        spaceBefore=4.5,
        spaceAfter=1.5,
    )
    s_body = ParagraphStyle(
        "Body",
        fontName="Helvetica",
        fontSize=8.6,
        leading=11.0,
        textColor=BLACK_RL,
        alignment=TA_JUSTIFY,
        spaceAfter=1.8,
    )
    s_item_title = ParagraphStyle(
        "ItemTitle",
        fontName="Helvetica-Bold",
        fontSize=8.95,
        leading=11.0,
        textColor=BLACK_RL,
        alignment=TA_LEFT,
        spaceBefore=2.5,
        spaceAfter=0.4,
    )
    s_item_meta = ParagraphStyle(
        "ItemMeta",
        fontName="Helvetica-Oblique",
        fontSize=8.25,
        leading=10.1,
        textColor=ROSE_RL,
        alignment=TA_LEFT,
        spaceAfter=1.3,
    )
    s_bullet = ParagraphStyle(
        "Bullet",
        fontName="Helvetica",
        fontSize=8.5,
        leading=10.8,
        textColor=BLACK_RL,
        leftIndent=10,
        firstLineIndent=-7,
        alignment=TA_LEFT,
        spaceAfter=1.1,
    )

    def add_section_header(story, title: str):
        story.append(Paragraph(title, s_section))
        story.append(
            HRFlowable(
                width="100%",
                thickness=0.85,
                color=ROSE_RL,
                spaceBefore=0,
                spaceAfter=2.8,
            )
        )

    bullet_dot = f"<font color='{ROSE_HEX}'><b>•</b></font>"

    story = []

    # Header
    story.append(Paragraph(data["name"], s_name))
    story.append(Paragraph(data["headline"], s_headline))
    story.append(Paragraph(data["subheadline"], s_subheadline))
    story.append(Paragraph(data["contact"], s_contact))
    story.append(Paragraph(data["key_metrics_pdf"], s_metrics))

    # Profil
    add_section_header(story, "PROFIL PROFESSIONNEL")
    story.append(Paragraph(data["profile"], s_body))

    # Expérience Professionnelle
    add_section_header(story, "EXPÉRIENCE PROFESSIONNELLE")
    for exp in data["experiences"]:
        story.append(Paragraph(exp["title"], s_item_title))
        story.append(Paragraph(exp["meta"], s_item_meta))
        for b in exp["bullets"]:
            story.append(Paragraph(f"{bullet_dot} {b}", s_bullet))

    # Formation
    add_section_header(story, "FORMATION")
    for edu in data["education"]:
        story.append(Paragraph(edu["title"], s_item_title))
        story.append(Paragraph(edu["meta"], s_item_meta))
        if edu["detail"]:
            story.append(Paragraph(f"{bullet_dot} {edu['detail']}", s_bullet))

    # Compétences
    add_section_header(story, "COMPÉTENCES CLÉS & DISPONIBILITÉS")
    for label, content in data["skills"]:
        story.append(Paragraph(f"{bullet_dot} <b>{label}</b>{content}", s_bullet))

    # Langues & Centres d'intérêt
    add_section_header(story, "LANGUES & CENTRES D'INTÉRÊT")
    story.append(Paragraph(f"{bullet_dot} {data['languages']}", s_bullet))
    story.append(Paragraph(f"{bullet_dot} <b>Centres d'intérêt :</b> {data['interests']}", s_bullet))

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


def add_bottom_border(paragraph, color_hex="B8336A", size="6"):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), size)
    bottom.set(qn("w:space"), "2")
    bottom.set(qn("w:color"), color_hex)
    pBdr.append(bottom)
    pPr.append(pBdr)


def style_metrics_box_docx(paragraph, bg_hex="FDF2F6", border_hex="E4AAC2"):
    pPr = paragraph._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), bg_hex)
    pPr.append(shd)

    pBdr = OxmlElement("w:pBdr")
    for side in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "3")
        el.set(qn("w:color"), border_hex)
        pBdr.append(el)
    pPr.append(pBdr)


def build_docx(output_path: Path, data: dict) -> None:
    doc = Document()

    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(0.85)
        section.bottom_margin = Cm(0.8)
        section.left_margin = Cm(1.2)
        section.right_margin = Cm(1.2)

    style_normal = doc.styles["Normal"]
    style_normal.font.name = "Calibri"
    style_normal.font.size = Pt(9.0)
    style_normal.font.color.rgb = BLACK_RGB

    def add_rich_p(text: str, size=8.9, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=1.3, italic=False, color=BLACK_RGB, rose_bullet=False):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.03
        if rose_bullet:
            rb = p.add_run("• ")
            rb.font.name = "Calibri"
            rb.font.size = Pt(size)
            rb.bold = True
            rb.font.color.rgb = ROSE_RGB
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
        p.paragraph_format.space_before = Pt(4.0)
        p.paragraph_format.space_after = Pt(1.8)
        r = p.add_run(title)
        r.font.name = "Calibri"
        r.font.size = Pt(9.8)
        r.bold = True
        r.font.color.rgb = ROSE_RGB
        add_bottom_border(p)

    # Header
    add_rich_p(f"<b>{data['name']}</b>", size=17.5, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0.5, color=ROSE_RGB)
    add_rich_p(f"<b>{data['headline']}</b>", size=9.6, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0.5)
    add_rich_p(f"<b>{data['subheadline']}</b>", size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=1.2, color=ROSE_RGB)
    add_rich_p(data["contact"], size=8.4, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2.5)

    # Bandeau Chiffres Clés
    pm = doc.add_paragraph()
    pm.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pm.paragraph_format.space_before = Pt(1.0)
    pm.paragraph_format.space_after = Pt(3.0)
    style_metrics_box_docx(pm)
    for seg_txt, is_b, is_rose in data["key_metrics_docx"]:
        r = pm.add_run(seg_txt)
        r.font.name = "Calibri"
        r.font.size = Pt(8.4)
        r.bold = is_b
        r.font.color.rgb = ROSE_RGB if is_rose else BLACK_RGB

    # Profil
    add_sec_title("PROFIL PROFESSIONNEL")
    add_rich_p(data["profile"], size=8.75, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=1.2)

    # Expériences
    add_sec_title("EXPÉRIENCE PROFESSIONNELLE")
    for exp in data["experiences"]:
        add_rich_p(f"<b>{exp['title']}</b>", size=9.0, space_before=1.8, space_after=0.2)
        add_rich_p(exp["meta"], size=8.25, italic=True, space_after=0.8, color=ROSE_RGB)
        for b in exp["bullets"]:
            p = add_rich_p(b, size=8.6, space_after=0.8, rose_bullet=True)
            p.paragraph_format.left_indent = Cm(0.35)
            p.paragraph_format.first_line_indent = Cm(-0.25)

    # Formation
    add_sec_title("FORMATION")
    for edu in data["education"]:
        add_rich_p(f"<b>{edu['title']}</b>", size=8.95, space_before=1.5, space_after=0.2)
        add_rich_p(edu["meta"], size=8.25, italic=True, space_after=0.7, color=ROSE_RGB)
        if edu["detail"]:
            p = add_rich_p(edu["detail"], size=8.6, space_after=0.8, rose_bullet=True)
            p.paragraph_format.left_indent = Cm(0.35)
            p.paragraph_format.first_line_indent = Cm(-0.25)

    # Compétences
    add_sec_title("COMPÉTENCES CLÉS & DISPONIBILITÉS")
    for label, content in data["skills"]:
        p = add_rich_p(f"<b>{label}</b>{content}", size=8.6, space_after=0.9, rose_bullet=True)
        p.paragraph_format.left_indent = Cm(0.35)
        p.paragraph_format.first_line_indent = Cm(-0.25)

    # Langues & Intérêts
    add_sec_title("LANGUES & CENTRES D'INTÉRÊT")
    p1 = add_rich_p(data["languages"], size=8.6, space_after=0.8, rose_bullet=True)
    p1.paragraph_format.left_indent = Cm(0.35)
    p1.paragraph_format.first_line_indent = Cm(-0.25)
    p2 = add_rich_p(f"<b>Centres d'intérêt :</b> {data['interests']}", size=8.6, space_after=0, rose_bullet=True)
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
