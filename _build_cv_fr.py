# -*- coding: utf-8 -*-
"""CV Calvin MINANG - version FRANCAISE, mise en page propre (dates alignees a droite).
   Adaptee a l'offre BNP Paribas Wealth Management - Junior Analyst UHNW - Investment Solutions."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
                                Table, TableStyle, KeepTogether)

NAVY = colors.HexColor("#1B3A5C")
ACCENT = colors.HexColor("#2E5C8A")
RULE = colors.HexColor("#C8D2DC")
DARK = colors.HexColor("#222222")
MID = colors.HexColor("#4A4A4A")

# ---------------- CONTENU ----------------
NAME = "CALVIN MINANG"
HEADLINE = "MARCH&Eacute;S DE CAPITAUX &nbsp;&middot;&nbsp; SOLUTIONS D'INVESTISSEMENT &nbsp;&middot;&nbsp; CLIENTS UHNW"
AVAILABILITY = ("Stage de fin d'&eacute;tudes &mdash; disponible de <b>janvier &agrave; juin 2027</b> "
                "&nbsp;&middot;&nbsp; Paris, France")
CONTACT = "+33 7 52 97 58 09 &nbsp;&middot;&nbsp; calvin.minang@skema.edu &nbsp;&middot;&nbsp; linkedin.com/in/calvin-minang"
CONTACT2 = "github.com/Calvin29990 &nbsp;&middot;&nbsp; calvin-minibloomberg.netlify.app"

PROFILE = ("&Eacute;l&egrave;ve en derni&egrave;re ann&eacute;e du Programme Grande &Eacute;cole de SKEMA Business School "
           "(grade de Master) et du MSc Corporate Financial Management. Exp&eacute;rience en <b>reporting "
           "multi-actifs</b> et suivi de march&eacute;s (FX, taux, cr&eacute;dit, actions) au sein d'un "
           "gestionnaire de 103 Md&euro; d'encours, et en <b>d&eacute;veloppement commercial B2B</b>. Formation "
           "solide en obligations, risque de cr&eacute;dit, mod&eacute;lisation financi&egrave;re et financements "
           "&agrave; effet de levier. Cible : stage de fin d'&eacute;tudes en <b>solutions d'investissement</b>.")

FORMATION = [
    ("SKEMA Business School", "juil. 2022 &ndash; d&eacute;c. 2026",
     ["Programme Grande &Eacute;cole (M2) &mdash; Double dipl&ocirc;me : <b>MSc Corporate Financial Management</b>",
      "Campus Belo Horizonte, Br&eacute;sil",
      "<i>Enseignements :</i> Fixed Income &middot; Valorisation &amp; Risque &middot; Risque de march&eacute; (VaR) &middot; Risque de cr&eacute;dit &middot; Mod&eacute;lisation financi&egrave;re &middot; FX &amp; Arbitrage"]),
    ("Ipesup Paris", "2021 &ndash; 2022",
     ["Classes pr&eacute;paratoires ECE &mdash; math&eacute;matiques et &eacute;conomie (fili&egrave;re intensive)"],),
]

EXPERIENCE = [
    ("BPCE Assurances", "janv. &ndash; mai 2024",
     "<b>Analyste reporting multi-actifs</b> (stage) &middot; Paris",
     ["Production quotidienne de reportings multi-actifs destin&eacute;s aux comit&eacute;s d'investissement : paires FX, indices actions, taux et spreads de cr&eacute;dit.",
      "Tableaux de bord et extractions <b>Bloomberg BQL</b> sur forwards et swaps FX ; suivi des courbes de taux &euro;STR et SOFR.",
      "Automatisation Excel/VBA et supports de march&eacute; sur les tendances et la volatilit&eacute;."],
     "P&eacute;rim&egrave;tre : <b>103 Md&euro;</b> d'encours d'assurance vie g&eacute;r&eacute;s en direct"),
    ("SKEMA Business School", "oct. &ndash; d&eacute;c. 2025",
     "<b>Assistant CRM &amp; Donn&eacute;es Partenaires</b> &middot; Executive Education",
     ["Nettoyage, d&eacute;doublonnage et fiabilisation de la base de donn&eacute;es partenaires.",
      "Mise &agrave; jour de <b>537 fiches contacts</b> et <b>102 fiches entreprises</b> pour les campus de Duba&iuml; et de Belo Horizonte."],
     None),
    ("FinStart.io", "juin &ndash; ao&ucirc;t 2023",
     "<b>Sales</b> (stage) &middot; Paris",
     ["Prospection B2B ciblant des consultants ind&eacute;pendants en finance, comptabilit&eacute;, risque et compliance : environ <b>100 e-mails par jour ouvré</b>, 500 par semaine, avec suivi complet des r&eacute;ponses.",
      "Sourcing et qualification de profils via APEC et LinkedIn."],
     None),
    ("SKEMA Job Service Paris", "sept. 2022 &ndash; ao&ucirc;t 2023",
     "<b>Membre du bureau &mdash; RH &amp; Partenariats</b> (CDD)",
     ["Prospection B2B et d&eacute;veloppement de partenariats pour l'offre de missions &eacute;tudiantes : pitch, qualification du besoin, entretiens et &eacute;v&eacute;nements RH avec SKEMA, EY et le Stade de France.",
      "Bilan collectif S1 2023 : <b>19 100 &euro;</b> de chiffre d'affaires, <b>125 &eacute;tudiants</b> plac&eacute;s sur 35 missions, 5 partenaires dont 4 nouveaux (EY, Roadbook, Auverprime, CDEFM)."],
     None),
]

PROJECTS = [
    ("CalvinX &mdash; Terminal de march&eacute; cross-asset", "JavaScript",
     "Tableau de bord de type Bloomberg couvrant FX, indices actions, taux, mati&egrave;res premi&egrave;res et volatilit&eacute;, avec d&eacute;tection de r&eacute;gimes de march&eacute; et export Excel. D&eacute;mo : calvin-minibloomberg.netlify.app"),
    ("ShockLab &mdash; Moteur de stress-test de portefeuille", "Python &middot; SQL &middot; Machine Learning",
     "Rejoue des &eacute;pisodes de march&eacute; r&eacute;els (Lehman, COVID, Soleimani) pour quantifier l'impact d'un choc sur un portefeuille multi-actifs ; base &eacute;v&eacute;nementielle SQL."),
    ("Pricer Black-Scholes &mdash; Options &amp; Grecs", "Excel &middot; VBA",
     "Valorisation d'options europ&eacute;ennes avec Delta, Gamma et Vega ; utilis&eacute; pour localiser le pic de gamma d'un portefeuille lors du choc p&eacute;trolier Petrobras."),
]

SKILLS = [
    ("Produits &amp; client&egrave;le", "Reporting investisseurs &middot; supports de pr&eacute;sentation de produits &middot; suivi de mandats &middot; prospection B2B &middot; qualification du besoin &middot; CRM"),
    ("March&eacute;s", "FX (forwards, swaps) &middot; Taux &middot; Obligations &middot; D&eacute;riv&eacute;s actions &middot; Volatilit&eacute; &middot; Risque de march&eacute; (VaR) &middot; Risque de cr&eacute;dit &middot; Financements &agrave; effet de levier"),
    ("Outils", "Bloomberg Terminal (BQL) &middot; Excel/VBA &middot; Python (pandas, scikit-learn) &middot; SQL (BigQuery) &middot; R &middot; JavaScript"),
    ("Certifications", "Candidat FRM (GARP) &middot; Certification AMF en cours &middot; Citi Markets Sales &amp; Trading (Forage) &middot; QuantInsti (Python for Trading ; Options Trading Strategies in Python)"),
]

LANGUAGES = "Fran&ccedil;ais (natif) &nbsp;&middot;&nbsp; Anglais (professionnel) &nbsp;&middot;&nbsp; Espagnol (B2) &nbsp;&middot;&nbsp; Portugais (notions)"

# ---------------- STYLES ----------------
S_NAME = ParagraphStyle('n', fontName='Helvetica-Bold', fontSize=18, leading=19, textColor=NAVY, spaceAfter=0)
S_HEAD = ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=8.9, leading=11, textColor=ACCENT, spaceAfter=1)
S_AVAIL = ParagraphStyle('a', fontName='Helvetica-Oblique', fontSize=8.6, leading=10.6, textColor=MID, spaceAfter=1)
S_CT = ParagraphStyle('c', fontName='Helvetica', fontSize=8.6, leading=11, textColor=DARK)
S_SEC = ParagraphStyle('sec', fontName='Helvetica-Bold', fontSize=9.4, leading=11.5, textColor=NAVY, spaceBefore=0, spaceAfter=0)
S_LEFT = ParagraphStyle('l', fontName='Helvetica-Bold', fontSize=9.0, leading=11, textColor=DARK)
S_RIGHT = ParagraphStyle('r', fontName='Helvetica-Bold', fontSize=8.4, leading=11, textColor=ACCENT, alignment=2)
S_DET = ParagraphStyle('d', fontName='Helvetica', fontSize=8.25, leading=10.2, textColor=DARK, spaceAfter=0.2)
S_BUL = ParagraphStyle('b', fontName='Helvetica', fontSize=8.25, leading=10.2, textColor=DARK, spaceAfter=0.6, leftIndent=8)
S_NOTE = ParagraphStyle('no', fontName='Helvetica-Oblique', fontSize=7.9, leading=10.1, textColor=MID, spaceAfter=0.8)
S_PROJ = ParagraphStyle('p', fontName='Helvetica', fontSize=8.25, leading=10.2, textColor=DARK, spaceAfter=0.8, alignment=TA_JUSTIFY)
S_PROF = ParagraphStyle('pf', fontName='Helvetica', fontSize=8.35, leading=10.5, textColor=DARK, alignment=TA_JUSTIFY)

def section(title):
    t = Table([[Paragraph(title, S_SEC)]], colWidths=[180*mm])
    t.setStyle(TableStyle([('LINEBELOW', (0,0), (-1,-1), 1, NAVY),
                           ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
                           ('TOPPADDING', (0,0), (-1,-1), 0),
                           ('LEFTPADDING', (0,0), (-1,-1), 0)]))
    return [Spacer(1, 3.4), t, Spacer(1, 2.2)]

def hdr_row(left, right):
    t = Table([[Paragraph(left, S_LEFT), Paragraph(right, S_RIGHT)]], colWidths=[127*mm, 53*mm])
    t.setStyle(TableStyle([('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),0),
                           ('TOPPADDING',(0,0),(-1,-1),1), ('BOTTOMPADDING',(0,0),(-1,-1),0.5),
                           ('VALIGN',(0,0),(-1,-1),'BOTTOM')]))
    return t

story = []
story.append(Paragraph(NAME, S_NAME))
story.append(Spacer(1, 1.5))
story.append(Paragraph(HEADLINE, S_HEAD))
story.append(Paragraph(AVAILABILITY, S_AVAIL))
story.append(Spacer(1, 3))
story.append(HRFlowable(width="100%", thickness=0.7, color=RULE, spaceAfter=3))
story.append(Paragraph(CONTACT, S_CT))
story.append(Paragraph(CONTACT2, S_CT))

story += section("PROFIL")
story.append(Paragraph(PROFILE, S_PROF))

story += section("FORMATION")
for name, dates, details in FORMATION:
    story.append(KeepTogether([hdr_row(name, dates)] + [Paragraph(d, S_DET) for d in details]))

story += section("EXP&Eacute;RIENCE PROFESSIONNELLE")
for company, dates, role, bullets, note in EXPERIENCE:
    block = [hdr_row(company, dates), Paragraph(role, S_DET)]
    if note:
        block.append(Paragraph(note, S_NOTE))
    for b in bullets:
        block.append(Paragraph(b, S_BUL, bulletText='\u2022'))
    story.append(KeepTogether(block))
    story.append(Spacer(1, 2.2))

story += section("PROJETS S&Eacute;LECTIONN&Eacute;S")
for title, tech, desc in PROJECTS:
    story.append(KeepTogether([hdr_row(title, tech), Paragraph(desc, S_PROJ)]))
    story.append(Spacer(1, 1.8))

story += section("COMP&Eacute;TENCES &amp; CERTIFICATIONS")
rows = [[Paragraph(f"<b>{k}</b>", S_DET), Paragraph(v, S_DET)] for k, v in SKILLS]
t = Table(rows, colWidths=[30*mm, 150*mm])
t.setStyle(TableStyle([('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),0),
                       ('TOPPADDING',(0,0),(-1,-1),1), ('BOTTOMPADDING',(0,0),(-1,-1),1.2),
                       ('VALIGN',(0,0),(-1,-1),'TOP')]))
story.append(t)

story += section("LANGUES")
story.append(Paragraph(LANGUAGES, S_DET))

doc = SimpleDocTemplate("CV_Calvin_MINANG_FR_v2.pdf", pagesize=A4,
    leftMargin=14*mm, rightMargin=14*mm, topMargin=9*mm, bottomMargin=7*mm,
    title="Calvin MINANG - Curriculum Vitae", author="Calvin MINANG",
    subject="Solutions d'investissement - Marches de capitaux")
doc.build(story)
print("OK -> CV_Calvin_MINANG_FR_v2.pdf")
