#!/usr/bin/env python3
"""
Profil LinkedIn de Cléanne MINANG — document PDF « à coller », section par section.

    python3 documents/linkedin-cleanne/build_linkedin_pdf.py

Sortie : documents/linkedin-cleanne/LINKEDIN-CLEANNE-EN.pdf
Polices : Lora + Source Sans 3 (SIL OFL), réutilisées depuis ../cv-cleanne/fonts.
Le contenu suit A-COLLER-LINKEDIN.md, qui reste la source de vérité.
"""

from __future__ import annotations

from pathlib import Path

from fpdf import FPDF

HERE = Path(__file__).resolve().parent
FONTS = HERE.parent / "cv-cleanne" / "fonts"
OUT = HERE / "LINKEDIN-CLEANNE-EN.pdf"

# ----------------------------------------------------------------------------
# Charte (identique au CV)
# ----------------------------------------------------------------------------
NAVY = (23, 50, 77)
INK = (28, 32, 38)
MUTED = (108, 118, 130)
RULE = (206, 213, 220)
BOX = (246, 248, 250)
WARN_BG = (255, 249, 236)
WARN_BAR = (198, 138, 24)
OK_BAR = (32, 122, 84)

SERIF = "Lora"
SANS = "Source Sans 3"

PW, PH = 210, 297
ML, MR = 18.0, 18.0
MT, MB = 16.0, 18.0
CW = PW - ML - MR

# ----------------------------------------------------------------------------
# Texte
# ----------------------------------------------------------------------------
NAME_LINE = "Cléanne MINANG — profil LinkedIn"
DOC_TITLE = "Texte à coller, section par section"
DOC_SUB = (
    "Profil en anglais · mots-clés conseil en stratégie, affaires publiques "
    "et organisations internationales · 29 octobre 2026"
)

INTRO = (
    "Chaque encadré gris se copie tel quel : sélectionner le texte à l'intérieur du cadre, "
    "copier, coller dans LinkedIn. Les champs (intitulé, entreprise, dates…) se saisissent à "
    "la main, ils sont donnés en clair dans les tableaux."
)
INTRO_POINTS = [
    "Suivre l'ordre de la dernière page : le profil se remplit de haut en bas.",
    "Ne recopier qu'une seule version de chaque bloc — les variantes sont des alternatives.",
    "Si le texte collé contient des retours à la ligne parasites, coller d'abord dans le bloc-notes.",
]

HEADLINES = [
    ("Version recommandée", "Economics & Management student at Université de Lille | "
     "McKinsey Skills for Success 2026 | Strategy, Public Affairs & International Affairs | "
     "MUNDUS – Model of the United Nations"),
    ("Variante courte, plus sobre", "Economics & Management student at Université de Lille | "
     "McKinsey Skills for Success 2026 | MUNDUS – Model of the United Nations"),
    ("Variante organisations internationales", "Economics & Management student at Université de "
     "Lille | McKinsey Skills for Success 2026 | Geopolitics, Public Policy & International "
     "Organizations"),
]
HEADLINE_NOTES = [
    "Champ « Titre » sous le nom. Le nom de l'université et McKinsey restent devant : ce sont "
    "les deux éléments qui arrêtent l'œil du recruteur.",
    "Ces mots (Strategy, Public Affairs, International Affairs, Geopolitics, Public Policy) sont "
    "ceux que les cabinets et organisations internationales filtrent dans la recherche LinkedIn.",
    "Pas d'emoji, pas de « Seeking opportunities » : la recherche d'un poste se dit dans la "
    "section À propos, une seule fois.",
]

ABOUT = """Economics & Management student at the University of Lille (France), after a year of selective preparatory classes in economics, mathematics and general culture (CPGE ECG).

I work at the intersection of analysis and communication: turning complex, fast-moving information into a clear recommendation.

WHERE I STAND TODAY

• McKinsey & Company — Skills for Success 2026. Selected for the firm's European programme for students and recent graduates. Four sessions on problem structuring, issue trees, hypothesis-driven analysis and executive communication, with a focus on risk and resilience.

• MUNDUS — Model of the United Nations, University of Lille. I write a weekly international analysis for the association's flagship format, "Le Monde en 7 actus": picking the story, verifying sources, writing and laying out the page. I also contribute to the association's decryptage formats and long-form articles, and take part in editorial planning and coordination across teams.

WHAT I BRING

• Problem structuring — breaking an ambiguous question into a clear, testable framework
• Research and synthesis — sourcing, cross-checking, and turning volume into a two-page brief
• Data analysis — Excel, statistics, and the discipline of checking a number before using it
• Written and spoken communication — in French (native) and English

WHAT I'M LOOKING FOR

A first professional experience in strategy consulting, public affairs or an international organisation — in France or abroad. I am particularly interested in teams working on geopolitics, risk and resilience, and public policy.

Feel free to reach out: minangcalvin0@gmail.com"""

ABOUT_NOTES = [
    "La dernière ligne (What I'm looking for) se réécrit à chaque candidature. C'est la seule "
    "phrase du profil qui doit bouger.",
    "Le niveau d'anglais n'est pas chiffré ici, volontairement : il est en section compétences. "
    "Ne pas écrire « fluent ».",
]

MCK_FIELDS = [
    ("Intitulé", "Skills for Success 2026"),
    ("Type d'emploi", "Internship"),
    ("Entreprise", "McKinsey & Company"),
    ("Lieu", "Remote"),
    ("Date de début", "October 2026"),
    ("Date de fin", "laisser vide (programme en cours)"),
]
MCK_DESC = """Selected for McKinsey & Company's Skills for Success programme, run for students and recent graduates across Europe — four sessions in autumn 2026.

• Problem structuring: breaking an ambiguous business problem into a clear, testable issue tree
• Hypothesis-driven analysis: prioritising what matters, and knowing what would prove a thesis wrong
• Executive communication: turning an analysis into a recommendation that fits on one page
• Exposure to the consulting role, with a focus on risk and resilience"""
MCK_NOTE = (
    "L'intitulé est « Skills for Success 2026 », pas « Consultant ». Un recruteur McKinsey "
    "reconnaîtra le programme ; un titre inventé se fait démonter en entretien."
)

MUNDUS_FIELDS = [
    ("Intitulé", "Press & Communications Officer — à ajuster"),
    ("Type d'emploi", "Volunteering"),
    ("Entreprise", "MUNDUS – Model of the United Nations"),
    ("Lieu", "Lille, Hauts-de-France, France"),
    ("Date de début", "2026"),
]
MUNDUS_DESC = """MUNDUS is the University of Lille's Model of the United Nations: debates on international affairs, simulations and conferences.

• Write a weekly international analysis for "Le Monde en 7 actus", the association's flagship format: choosing the story, sourcing and cross-checking, writing and laying out the final page
• Geopolitical watch and contribution to the association's editorial formats — decryptages, "Carte sur table", long-form articles
• Editorial coordination: splitting topics between contributors, setting publication deadlines, tracking delivery across teams"""
MUNDUS_NOTE = (
    "« Press & Communications Officer » est une traduction assumée de « Pôle presse et "
    "communication ». Si MUNDUS donne un titre officiel, prendre le sien. Éviter « Head of "
    "Press », qui suppose une équipe à diriger."
)

FORMATION = [
    ("University of Lille",
     "Licence (Bachelor's) in Economics & Management — Economics and Business Management track",
     "2024 — present"),
    ("Lycée Gaston Berger, Lille",
     "CPGE ECG — Preparatory classes in Economics and Business (selective)",
     "2023 — 2024"),
]
FORMATION_NOTE = (
    "Ne pas ajouter le baccalauréat ni le lycée Nelson Mandela : au niveau Licence, cela "
    "n'apporte rien et allonge le profil sans le renforcer."
)

SKILLS = [
    ("1", "Strategy", "épinglée"),
    ("2", "Analysis", "épinglée"),
    ("3", "Microsoft Excel", "épinglée"),
    ("4", "Problem Solving", ""),
    ("5", "Research", ""),
    ("6", "Public Policy", ""),
    ("7", "Communication", ""),
    ("8", "Project Coordination", ""),
    ("9", "Data Analysis", ""),
    ("10", "International Relations", ""),
]
SKILLS_NOTE = (
    "Les trois premières sont épinglées et s'affichent en haut du profil. Ne pas dépasser dix : "
    "au-delà, LinkedIn affiche « +N skills » et l'ensemble se dilue."
)

LANGUAGES = [
    ("French", "Native or bilingual proficiency"),
    ("English", "Limited working proficiency — tant que le niveau est B1"),
    ("Spanish", "Limited working proficiency"),
    ("Italian", "Elementary proficiency"),
]
LANGUAGES_NOTE = (
    "Ne passer à « Professional working proficiency » qu'avec un certificat B2 en main. Un "
    "recruteur qui teste en entretien le verra en trente secondes."
)

URL_CURRENT = "linkedin.com/in/cléanne-minang-95772a2b0"
URL_TARGET = "linkedin.com/in/cleanne-minang"
URL_FALLBACKS = [
    "linkedin.com/in/cleanne-minang-lille",
    "linkedin.com/in/cleanne-minang1",
    "linkedin.com/in/cleanne-minang-econ",
]
URL_TEXT = (
    "L'adresse actuelle contient un accent et huit caractères aléatoires : l'accent se casse dès "
    "qu'on la colle dans un email ou un formulaire, et les caractères font « profil non fini ». "
    "À changer dans Réglages > Visibilité > Modifier l'URL publique."
)
URL_WARNING = (
    "Le CV papier indique déjà linkedin.com/in/cleanne-minang. Si une autre adresse est retenue, "
    "prévenir pour régénérer le CV : sinon le lien du CV mène à une page 404."
)

NOT_ADDED = [
    "Le stade Bollaert-Delelis (accueil, jours de match) et la production audiovisuelle "
    "associative : ils restent sur le CV papier, où ils prouvent la tenue d'un poste.",
    "Le baccalauréat et le lycée : inutiles au niveau Licence.",
    "Toute certification non obtenue. Le certificat d'anglais du dossier appartient à Calvin, "
    "pas à Cléanne : ne pas le reprendre.",
]
NOT_ADDED_WHY = (
    "Pourquoi : sur un profil qui démarre, deux entrées fortes font plus de bruit que six entrées moyennes. "
    "Un recruteur de cabinet lit les quatre premières secondes : s'il voit « Agent d'accueil » en "
    "deuxième position, il classe le profil en job étudiant et ne lit pas la suite. Ces deux "
    "expériences reviendront dans 6 à 12 mois."
)

STEPS = [
    "Réglages > Visibilité > Modifier l'URL publique (voir section 8).",
    "Photo : portrait, cadrage buste, fond neutre. Bannière sobre, sans texte.",
    "Titre du profil — section 1.",
    "À propos — section 2.",
    "Expérience McKinsey, puis MUNDUS — sections 3 et 4.",
    "Formation — section 5.",
    "Compétences puis langues — sections 6 et 7.",
    "Open to work en mode « recruteurs uniquement ». Postes : Internship, Apprenticeship. "
    "Secteurs : Business Consulting and Services, International Affairs, Public Policy Offices.",
    "Ouvrir le profil en navigation privée et le relire à voix haute : ce qui sonne faux s'entend.",
]

CHECKLIST = [
    "URL LinkedIn modifiée et identique à celle du CV",
    "Photo et bannière en place",
    "Titre du profil collé (une seule version)",
    "À propos collé, paragraphes recollés",
    "McKinsey en première expérience",
    "MUNDUS en deuxième expérience",
    "Formation : deux entrées seulement",
    "Dix compétences, dans l'ordre indiqué",
    "Langues : anglais en Limited working proficiency",
    "Open to work en mode recruteurs uniquement",
    "Profil relu en navigation privée",
]

DELIVERY = (
    "Le CV s'envoie en pièce jointe, jamais en .docx. Une version en ligne existe "
    "(documents/cv-cleanne/CV_Cleanne_MINANG.pdf), mais le dépôt GitHub qui l'héberge est public "
    "et contient des pièces personnelles et juridiques : ne pas le mettre dans le champ « Site "
    "web » du profil tant qu'un dépôt dédié au CV n'est pas créé."
)


# ----------------------------------------------------------------------------
# Moteur
# ----------------------------------------------------------------------------
class Doc(FPDF):
    def __init__(self) -> None:
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(False)
        self.set_margins(ML, MT, MR)
        self.set_compression(True)
        self.add_font(SERIF, "", str(FONTS / "Lora_400Regular.ttf"))
        self.add_font(SERIF, "B", str(FONTS / "Lora_600SemiBold.ttf"))
        self.add_font(SANS, "", str(FONTS / "SourceSans3_400Regular.ttf"))
        self.add_font(SANS, "I", str(FONTS / "SourceSans3_400Regular_Italic.ttf"))
        self.add_font(SANS, "B", str(FONTS / "SourceSans3_600SemiBold.ttf"))
        self.y = MT
        self.page_no = 0

    # -- primitives ----------------------------------------------------------
    def new_page(self) -> None:
        if self.page_no:
            self._footer()
        self.add_page()
        self.page_no += 1
        self.y = MT
        self.set_text_color(*INK)

    def _footer(self) -> None:
        self.set_draw_color(*RULE)
        self.set_line_width(0.3)
        self.line(ML, PH - MB + 4, PW - MR, PH - MB + 4)
        self.set_font(SANS, "", 7.4)
        self.set_text_color(*MUTED)
        self.set_xy(ML, PH - MB + 6)
        self.cell(0, 0, NAME_LINE)
        p = f"{self.page_no}"
        self.set_xy(ML, PH - MB + 6)
        self.cell(CW, 0, p, align="R")

    def need(self, h: float) -> None:
        if self.y + h > PH - MB:
            self.new_page()

    def lines(self, txt: str, w: float, size: float, font: str = SANS, style: str = "") -> list[str]:
        self.set_font(font, style, size)
        return self.multi_cell(w, 4, txt, dry_run=True, output="LINES", align="L")

    def para(self, txt: str, size: float = 9.2, lh: float = 4.5, color=INK,
             font: str = SANS, style: str = "", x: float = ML, w: float = CW) -> None:
        self.set_font(font, style, size)
        self.set_text_color(*color)
        h = len(self.lines(txt, w, size, font, style)) * lh
        self.need(h)
        self.set_xy(x, self.y)
        self.multi_cell(w, lh, txt, align="L")
        self.y = self.get_y()

    def space(self, mm: float) -> None:
        self.y += mm

    def rule(self) -> None:
        self.set_draw_color(*RULE)
        self.set_line_width(0.35)
        self.line(ML, self.y, PW - MR, self.y)


def section_head(pdf: Doc, num: str, title: str, limit: str = "") -> None:
    h = 12.5
    pdf.need(h + 26)
    pdf.space(1.5)
    y = pdf.y
    pdf.set_fill_color(*NAVY)
    pdf.rect(ML, y + 0.35, 2.4, 2.4, style="F")

    pdf.set_font(SANS, "B", 8.4)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(ML + 5.0, y)
    pdf.cell(0, 0, f"SECTION {num}")

    pdf.set_font(SERIF, "B", 12.6)
    pdf.set_text_color(*NAVY)
    pdf.set_xy(ML + 5.0, y + 4.3)
    pdf.cell(0, 0, title)

    if limit:
        pdf.set_font(SANS, "", 7.8)
        pdf.set_text_color(*MUTED)
        pdf.set_xy(ML, y + 4.8)
        pdf.cell(CW, 0, limit, align="R")

    pdf.y = y + 11.5


def copy_box(pdf: Doc, text: str, label: str = "", size: float = 9.0) -> None:
    """Encadré gris copiable. Se coupe proprement d'une page à l'autre si nécessaire."""
    pad_x, pad_y = 4.6, 3.4
    lh = 4.35
    inner_w = CW - pad_x - 3.0
    lines = pdf.lines(text, inner_w, size)

    remaining = list(lines)
    first = True
    while remaining:
        head = 4.6 if (label and first) else 0.0
        avail = PH - MB - pdf.y - pad_y * 2 - head
        fit = int(avail // lh)
        if fit < 3:
            pdf.new_page()
            continue

        chunk = remaining[:fit]
        remaining = remaining[fit:]
        h = len(chunk) * lh + pad_y * 2 + head

        y0 = pdf.y
        pdf.set_fill_color(*BOX)
        pdf.rect(ML, y0, CW, h, style="F")
        pdf.set_fill_color(*NAVY)
        pdf.rect(ML, y0, 1.5, h, style="F")

        if head:
            pdf.set_font(SANS, "B", 7.5)
            pdf.set_text_color(*MUTED)
            pdf.set_xy(ML + pad_x, y0 + pad_y - 0.4)
            pdf.cell(0, 0, label)
            pdf.set_font(SANS, "", 7.5)
            pdf.set_xy(ML + pad_x, y0 + pad_y - 0.4)
            pdf.cell(inner_w, 0, f"{len(text)} caractères", align="R")

        pdf.set_font(SANS, "", size)
        pdf.set_text_color(*INK)
        ty = y0 + pad_y + head
        for ln in chunk:
            pdf.set_xy(ML + pad_x, ty)
            pdf.cell(0, lh, ln)
            ty += lh

        pdf.y = y0 + h
        first = False
        if remaining:
            pdf.new_page()

    pdf.y += 3.6


def field_table(pdf: Doc, rows: list[tuple[str, str]]) -> None:
    lw = 33.0
    lh = 4.9
    vw = CW - lw - 2.0
    for k, v in rows:
        ls = pdf.lines(v, vw, 9.0)
        h = len(ls) * lh
        pdf.need(h + 1.5)
        y0 = pdf.y
        pdf.set_font(SANS, "B", 8.6)
        pdf.set_text_color(*NAVY)
        pdf.set_xy(ML, y0 + 0.3)
        pdf.cell(lw, 0, k)
        pdf.set_font(SANS, "", 9.0)
        pdf.set_text_color(*INK)
        pdf.set_xy(ML + lw, y0)
        pdf.multi_cell(vw, lh, v, align="L")
        pdf.y = y0 + h + 1.1
    pdf.space(2.2)


def numbered_table(pdf: Doc, rows: list[tuple[str, str, str]]) -> None:
    nw, sw = 9.0, 44.0
    lh = 4.8
    for num, name, tag in rows:
        pdf.set_font(SANS, "", 8.9)
        pdf.set_text_color(*MUTED)
        pdf.set_xy(ML, pdf.y)
        pdf.cell(nw, lh, num)
        pdf.set_font(SANS, "B", 9.0)
        pdf.set_text_color(*INK)
        pdf.set_xy(ML + nw, pdf.y)
        pdf.cell(sw, lh, name)
        if tag:
            pdf.set_font(SANS, "I", 7.9)
            pdf.set_text_color(*MUTED)
            pdf.set_xy(ML + nw + sw, pdf.y)
            pdf.cell(0, lh, tag)
        pdf.y += lh
    pdf.space(2.6)


def bullets(pdf: Doc, items: list[str], size: float = 8.7, color=INK) -> None:
    for it in items:
        ls = pdf.lines(it, CW - 4.4, size)
        h = len(ls) * 4.3
        pdf.need(h)
        y0 = pdf.y
        pdf.set_fill_color(*NAVY)
        pdf.rect(ML + 0.6, y0 + 1.65, 1.4, 1.4, style="F")
        pdf.set_font(SANS, "", size)
        pdf.set_text_color(*color)
        pdf.set_xy(ML + 4.4, y0)
        pdf.multi_cell(CW - 4.4, 4.3, it, align="L")
        pdf.y = pdf.get_y() + 1.0
    pdf.space(1.4)


def callout(pdf: Doc, title: str, body: str, bar=WARN_BAR, bg=WARN_BG) -> None:
    pad = 4.2
    inner = CW - pad - 3.4
    ls = pdf.lines(body, inner, 8.5)
    h = len(ls) * 4.25 + pad * 2 + 5.0
    pdf.need(h + 3)
    y0 = pdf.y
    pdf.set_fill_color(*bg)
    pdf.rect(ML, y0, CW, h, style="F")
    pdf.set_fill_color(*bar)
    pdf.rect(ML, y0, 1.5, h, style="F")

    pdf.set_font(SANS, "B", 7.9)
    pdf.set_text_color(*bar)
    pdf.set_xy(ML + pad, y0 + pad - 0.6)
    pdf.cell(0, 3, title)

    pdf.set_font(SANS, "", 8.5)
    pdf.set_text_color(*INK)
    pdf.set_xy(ML + pad, y0 + pad + 4.2)
    pdf.multi_cell(inner, 4.25, body, align="L")
    pdf.y = y0 + h + 3.8


def checklist(pdf: Doc, items: list[str]) -> None:
    lh = 5.4
    for it in items:
        pdf.need(lh)
        y0 = pdf.y
        pdf.set_draw_color(*NAVY)
        pdf.set_line_width(0.3)
        pdf.rect(ML + 0.4, y0 + 1.1, 2.6, 2.6)
        pdf.set_font(SANS, "", 8.9)
        pdf.set_text_color(*INK)
        pdf.set_xy(ML + 5.6, y0 + 1.2)
        pdf.cell(0, 0, it)
        pdf.y += lh


# ----------------------------------------------------------------------------
# Composition
# ----------------------------------------------------------------------------
def build() -> Path:
    pdf = Doc()
    pdf.new_page()

    # ---- couverture / mode d'emploi ---------------------------------------
    pdf.set_font(SANS, "B", 7.6)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(ML, pdf.y)
    pdf.cell(0, 0, "PROFIL LINKEDIN  ·  CLÉANNE MINANG")
    pdf.y += 7.5

    pdf.set_font(SERIF, "B", 21)
    pdf.set_text_color(*NAVY)
    pdf.set_xy(ML, pdf.y)
    pdf.cell(0, 0, DOC_TITLE)
    pdf.y += 8.6

    pdf.set_font(SANS, "", 9.0)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(ML, pdf.y)
    pdf.multi_cell(CW, 4.6, DOC_SUB, align="L")
    pdf.y = pdf.get_y() + 5.2

    pdf.rule()
    pdf.y += 6.0

    pdf.para(INTRO, size=9.3, lh=4.7)
    pdf.space(2.4)
    bullets(pdf, INTRO_POINTS, size=8.7)
    pdf.space(3.0)

    # ---- 1. titre ----------------------------------------------------------
    section_head(pdf, "1", "Titre du profil (headline)", "220 caractères max")
    for label, txt in HEADLINES:
        copy_box(pdf, txt, label)
    pdf.space(0.6)
    bullets(pdf, HEADLINE_NOTES)
    pdf.space(2.0)

    # ---- 2. à propos -------------------------------------------------------
    section_head(pdf, "2", "À propos (About)", "2 600 caractères max")
    pdf.para(
        "À coller dans « Ajouter une section » > « À propos ». Le bloc ci-dessous fait "
        f"{len(ABOUT)} caractères.",
        size=8.8, lh=4.4, color=MUTED,
    )
    pdf.space(1.6)
    copy_box(pdf, ABOUT, "Bloc À propos — intégralité")
    pdf.space(0.4)
    bullets(pdf, ABOUT_NOTES)
    pdf.space(2.0)

    # ---- 3. McKinsey -------------------------------------------------------
    section_head(pdf, "3", "Expérience 1 — McKinsey & Company")
    field_table(pdf, MCK_FIELDS)
    copy_box(pdf, MCK_DESC, "Description du poste")
    callout(pdf, "ATTENTION — INTITULÉ EXACT", MCK_NOTE)
    pdf.space(1.6)

    # ---- 4. MUNDUS ---------------------------------------------------------
    section_head(pdf, "4", "Expérience 2 — MUNDUS, Model of the United Nations")
    field_table(pdf, MUNDUS_FIELDS)
    copy_box(pdf, MUNDUS_DESC, "Description du poste")
    callout(pdf, "INTITULÉ À AJUSTER", MUNDUS_NOTE)
    pdf.space(1.6)

    # ---- 5. formation ------------------------------------------------------
    section_head(pdf, "5", "Formation")
    for i, (school, degree, dates) in enumerate(FORMATION, start=1):
        dl = pdf.lines(degree, CW - 6.0, 9.0)
        pdf.need(6.0 + len(dl) * 4.5 + 3.6)
        y0 = pdf.y
        pdf.set_font(SANS, "B", 9.4)
        pdf.set_text_color(*INK)
        pdf.set_xy(ML, y0)
        pdf.cell(0, 0, f"{i}.  {school}")
        pdf.set_font(SANS, "", 8.5)
        pdf.set_text_color(*MUTED)
        pdf.set_xy(ML, y0)
        pdf.cell(CW, 0, dates, align="R")

        pdf.set_font(SANS, "", 9.0)
        pdf.set_text_color(*INK)
        pdf.set_xy(ML + 6.0, y0 + 5.0)
        pdf.multi_cell(CW - 6.0, 4.5, degree, align="L")
        pdf.y = pdf.get_y() + 3.4
    pdf.space(0.6)
    bullets(pdf, [FORMATION_NOTE])
    pdf.space(1.8)

    # ---- 6. compétences ----------------------------------------------------
    section_head(pdf, "6", "Compétences (skills)", "10 maximum")
    numbered_table(pdf, SKILLS)
    bullets(pdf, [SKILLS_NOTE])
    pdf.space(1.8)

    # ---- 7. langues --------------------------------------------------------
    section_head(pdf, "7", "Langues")
    field_table(pdf, LANGUAGES)
    callout(pdf, "NIVEAU D'ANGLAIS", LANGUAGES_NOTE)
    pdf.space(1.6)

    # ---- 8. URL ------------------------------------------------------------
    section_head(pdf, "8", "URL du profil — à modifier")
    pdf.para("Adresse actuelle :", size=8.5, lh=4.3, color=MUTED)
    pdf.space(1.2)
    copy_box(pdf, URL_CURRENT, "à remplacer")
    pdf.para(URL_TEXT, size=9.0, lh=4.5)
    pdf.space(3.0)
    pdf.para("Adresse à viser :", size=8.5, lh=4.3, color=MUTED)
    pdf.space(1.2)
    copy_box(pdf, URL_TARGET, "objectif")
    pdf.para(
        "Si LinkedIn répond que l'adresse est déjà prise, par ordre de préférence :",
        size=8.9, lh=4.4,
    )
    pdf.space(1.6)
    for u in URL_FALLBACKS:
        copy_box(pdf, u, "", size=9.0)
    callout(pdf, "COHÉRENCE CV / LINKEDIN", URL_WARNING)
    pdf.space(1.6)

    # ---- 9. ce qu'on n'ajoute pas ------------------------------------------
    section_head(pdf, "9", "Ce qu'on n'ajoute pas, et pourquoi")
    bullets(pdf, NOT_ADDED)
    pdf.space(1.4)
    pdf.para(NOT_ADDED_WHY, size=8.9, lh=4.5)
    pdf.space(3.0)

    # ---- 10. ordre de saisie ------------------------------------------------
    section_head(pdf, "10", "Ordre de saisie — 30 minutes")
    for i, s in enumerate(STEPS, start=1):
        ls = pdf.lines(s, CW - 8.0, 8.9)
        h = len(ls) * 4.5
        pdf.need(h + 1.4)
        y0 = pdf.y
        pdf.set_font(SANS, "B", 8.9)
        pdf.set_text_color(*NAVY)
        pdf.set_xy(ML, y0)
        pdf.cell(7.0, 0, f"{i}.")
        pdf.set_font(SANS, "", 8.9)
        pdf.set_text_color(*INK)
        pdf.set_xy(ML + 7.0, y0)
        pdf.multi_cell(CW - 7.0, 4.5, s, align="L")
        pdf.y = pdf.get_y() + 1.4
    pdf.space(2.4)

    # ---- 11. checklist ------------------------------------------------------
    section_head(pdf, "11", "Vérification avant de communiquer le profil")
    checklist(pdf, CHECKLIST)
    pdf.space(3.0)

    # ---- 12. diffusion ------------------------------------------------------
    section_head(pdf, "12", "Diffusion du CV")
    callout(pdf, "PIÈCE JOINTE, PAS DE LIEN", DELIVERY, bar=OK_BAR, bg=(240, 247, 243))

    pdf._footer()

    pdf.set_title("Profil LinkedIn — Cléanne MINANG (texte à coller)")
    pdf.set_author("Cléanne MINANG")
    pdf.set_subject("LinkedIn — profil en anglais, section par section")
    pdf.set_keywords("LinkedIn, profil, conseil, stratégie, affaires publiques")
    pdf.output(str(OUT))
    return OUT


if __name__ == "__main__":
    path = build()
    import pymupdf

    doc = pymupdf.open(str(path))
    chars = sum(len(p.get_text()) for p in doc)
    imgs = sum(len(p.get_images()) for p in doc)
    print(f"PDF écrit : {path}")
    print(f"pages={doc.page_count}  images={imgs}  caractères extractibles={chars}")
