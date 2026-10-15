# -*- coding: utf-8 -*-
"""
PDF combiné pour Copilot : MOCK A (40 Q) + MOCK B (30 Q, format réel) + corrigés
+ MÉMO VISUEL (6 schémas vectoriels précis, dessinés par code — aucune image IA).
Usage : python3 build_mocks_ab.py
"""
import math
from build_docs import (LSEGPdf, render_pdf, MOCK_BLOCKS,
                        NAVY, PURPLE, PUR_BG, AMB_BG, GRN_BG, GRAY, LIGHT, GREEN, RED, ROW_BG, USABLE)

INK    = (40, 44, 52)
CARD   = (247, 248, 252)
EDGE   = (95, 100, 120)
BLUE   = (36, 84, 196)

# ---------------------------------------------------------------- helpers
def arrow(pdf, x1, y1, x2, y2, color=INK, lw=0.5, head=2.4):
    pdf.set_draw_color(*color); pdf.set_line_width(lw)
    pdf.line(x1, y1, x2, y2)
    ang = math.atan2(y2 - y1, x2 - x1)
    pts = [(x2, y2),
           (x2 - head * math.cos(ang - 0.45), y2 - head * math.sin(ang - 0.45)),
           (x2 - head * math.cos(ang + 0.45), y2 - head * math.sin(ang + 0.45))]
    pdf.set_fill_color(*color)
    pdf.polygon(pts, style="F")

def label(pdf, x, y, txt, size=7.2, bold=False, color=INK, align="L", w=60, lh=3.6):
    pdf.set_xy(x, y)
    pdf.set_font("DejaVu", "B" if bold else "", size)
    pdf.set_text_color(*color)
    pdf.multi_cell(w, lh, txt, align=align)

def card_box(pdf, x, y, w, h, fill=CARD, edge=EDGE, lw=0.3):
    pdf.set_fill_color(*fill); pdf.set_draw_color(*edge); pdf.set_line_width(lw)
    pdf.rect(x, y, w, h, style="DF", round_corners=True, corner_radius=1.6)

def chip(pdf, x, y, w, h, txt, fill, tcol=(255, 255, 255), size=7.4, bold=True):
    pdf.set_fill_color(*fill)
    pdf.rect(x, y, w, h, style="F", round_corners=True, corner_radius=1.6)
    pdf.set_xy(x, y)
    pdf.set_font("DejaVu", "B" if bold else "", size)
    pdf.set_text_color(*tcol)
    pdf.cell(w, h, txt, align="C")

# ---------------------------------------------------------------- figures
def _app_window(pdf, x, y, w, h, title, dot, symbol):
    card_box(pdf, x, y, w, h)
    pdf.set_fill_color(24, 44, 80)
    pdf.rect(x, y, w, 6, style="F", round_corners=True, corner_radius=1.6)
    pdf.set_fill_color(*dot)
    pdf.ellipse(x + 1.8, y + 1.5, 3, 3, style="F")
    pdf.set_xy(x + 6.5, y + 0.7)
    pdf.set_font("DejaVu", "B", 6.8); pdf.set_text_color(255, 255, 255)
    pdf.cell(w - 8, 4.6, title)
    pdf.set_xy(x, y + 12)
    pdf.set_font("DejaVu", "B", 8.6); pdf.set_text_color(*NAVY)
    pdf.cell(w, 5, symbol, align="C")

def fig_linkchannel(pdf):
    pdf._need(70)
    y = pdf.get_y() + 2
    label(pdf, 12, y, "Tu tapes un nouvel instrument dans UNE app liée…", 8.4, True, NAVY, w=USABLE)
    yw = y + 6
    _app_window(pdf, 14,  yw, 52, 26, "Monitor", RED, "ASML.PA")
    _app_window(pdf, 74,  yw, 52, 26, "Chart",   RED, "ASML.PA")
    _app_window(pdf, 134, yw, 52, 26, "Overview", RED, "ASML.PA")
    arrow(pdf, 66, yw + 13, 74, yw + 13); arrow(pdf, 126, yw + 13, 134, yw + 13)
    label(pdf, 12, yw + 29, "…les 3 apps « réglées » sur la MÊME couleur du Link Channel "
          "(cercle en haut à gauche) suivent automatiquement.", 7.6, False, GRAY, w=USABLE)
    pdf.set_xy(12, yw + 36)
    pdf.set_font("DejaVu", "", 7.6); pdf.set_text_color(*GREEN)
    pdf.multi_cell(USABLE, 4, "✓ VRAI (question officielle) : une NOUVELLE app groupée avec des apps déjà liées "
                   "devient automatiquement liée (elle prend la couleur du groupe).", markdown=True)
    pdf.set_y(yw + 50)
    pdf.set_draw_color(*PURPLE); pdf.set_line_width(0.3)
    pdf.line(12, pdf.get_y() - 3, 198, pdf.get_y() - 3)

def fig_newsaccess(pdf):
    pdf._need(72)
    y = pdf.get_y() + 2
    label(pdf, 12, y, "Les 2 SEULS accès officiels au News Monitor", 8.4, True, NAVY, w=USABLE)
    y1 = y + 7
    chip(pdf, 14, y1, 42, 8, "Search box", NAVY)
    chip(pdf, 70, y1, 62, 8, "« News » + Autosuggest", NAVY)
    chip(pdf, 146, y1, 42, 8, "News Component", GREEN)
    arrow(pdf, 56, y1 + 4, 70, y1 + 4, GREEN); arrow(pdf, 132, y1 + 4, 146, y1 + 4, GREEN)
    y2 = y1 + 15
    chip(pdf, 14, y2, 42, 8, "Menu", NAVY)
    chip(pdf, 70, y2, 62, 8, "News & Research", NAVY)
    arrow(pdf, 56, y2 + 4, 70, y2 + 4, GREEN); arrow(pdf, 132, y2 + 4, 146, y2 + 4, GREEN)
    chip(pdf, 146, y2, 42, 8, "News Monitor", GREEN)
    label(pdf, 12, y2 + 17, "Les 3 PIÈGES à cocher JAMAIS :", 8, True, RED)
    yt = y2 + 22
    for i, t in enumerate(["F2 ✗  (= Quote List)", "« Monitor » ✗", "Menu > Search Tools ✗"]):
        chip(pdf, 14 + i * 62, yt, 58, 7.5, t, (250, 233, 233), RED, 7.2, True)
    pdf.set_y(yt + 12)

def fig_briefcase(pdf):
    pdf._need(62)
    y = pdf.get_y() + 2
    label(pdf, 12, y, "My Briefcase — en haut à DROITE de la toolbar", 8.4, True, NAVY, w=USABLE)
    yb = y + 6
    card_box(pdf, 14, yb, 170, 12)
    for i, t in enumerate(["Search", "Workspaces", "Messenger", "Briefcase ★"]):
        x = 20 + i * 42
        pdf.set_xy(x, yb + 3)
        pdf.set_font("DejaVu", "B" if i == 3 else "", 7)
        pdf.set_text_color(*(PURPLE if i == 3 else GRAY))
        pdf.cell(36, 6, t, align="C")
    arrow(pdf, 152, yb + 14, 152, yb + 20, PURPLE)
    chip(pdf, 120, yb + 21, 64, 8, "100 documents MAX", (146, 100, 0))
    label(pdf, 14, yb + 21, "Collecte news + documents → lecture OFFLINE :", 7.6, False, GRAY, w=100)
    chip(pdf, 14, yb + 32, 46, 8, "Desktop", GREEN)
    chip(pdf, 68, yb + 32, 52, 8, "Mobile hors ligne", GREEN)
    pdf.set_y(yb + 44)

def fig_static_ts(pdf):
    pdf._need(66)
    y = pdf.get_y() + 2
    label(pdf, 12, y, "STATIC vs TIME SERIES — la photo ou le film ?", 8.4, True, NAVY, w=USABLE)
    yb = y + 6
    card_box(pdf, 14, yb, 86, 40, GRN_BG, GREEN)
    chip(pdf, 22, yb + 3, 70, 7, "STATIC REQUEST", GREEN)
    label(pdf, 22, yb + 13, "Photo à l'instant T (latest value)", 7.4, False, INK, w=72)
    label(pdf, 22, yb + 19, "Codes : VIRGULES « A,B,C »", 7.4, True, INK, w=72)
    label(pdf, 22, yb + 25, "ou code de liste (L#…, LN…)", 7.4, False, INK, w=72)
    label(pdf, 22, yb + 31, "Jamais le « + »  ✗", 7.4, True, RED, w=72)
    card_box(pdf, 108, yb, 86, 40, PUR_BG, PURPLE)
    chip(pdf, 116, yb + 3, 70, 7, "TIME SERIES REQUEST", PURPLE)
    label(pdf, 116, yb + 13, "Film : historique de valeurs", 7.4, False, INK, w=72)
    label(pdf, 116, yb + 19, "+ dates début/fin", 7.4, True, INK, w=72)
    label(pdf, 116, yb + 25, "+ fréquence (D/W/M/Q/Y)", 7.4, True, INK, w=72)
    label(pdf, 116, yb + 31, "Static = photo, TS = film", 7.4, False, GRAY, w=72)
    ty = yb + 47
    pdf.set_draw_color(*EDGE); pdf.set_line_width(0.6)
    pdf.set_fill_color(*BLUE)
    pdf.ellipse(52, ty - 1.7, 3.4, 3.4, style="F")
    label(pdf, 20, ty + 1.5, "1 seule valeur, datée (latest)", 6.6, False, GRAY, w=72)
    arrow(pdf, 116, ty, 188, ty)
    for dx in range(0, 5):
        pdf.set_fill_color(*BLUE); pdf.ellipse(122 + dx * 15, ty - 1.2, 2.4, 2.4, style="F")
    label(pdf, 116, ty + 1.5, "une suite de points datés", 6.6, False, GRAY)
    pdf.set_y(ty + 9)

def fig_excelmap(pdf):
    pdf._need(74)
    y = pdf.get_y() + 2
    label(pdf, 12, y, "Excel add-in — la carte des 3 vrais chemins + 1 faux", 8.4, True, NAVY, w=USABLE)
    yb = y + 6
    data = [("TEMPLATE LIBRARY", "Partager tes fichiers avec les AUTRES utilisateurs", GREEN),
            ("Menu LSEG > TEMPLATES", "Templates PRÉ-CONSTRUITS (pas depuis une cellule)", BLUE),
            ("MY FILES", "TES fichiers, accessibles de partout", PURPLE)]
    for i, (t, d, c) in enumerate(data):
        x = 14 + i * 62
        card_box(pdf, x, yb, 58, 24, CARD, c)
        chip(pdf, x + 4, yb + 3, 50, 6.5, t, c, size=6.4)
        label(pdf, x + 4, yb + 12, d, 6.6, False, INK, w=50, lh=3.2)
    card_box(pdf, 14, yb + 28, 178, 10, (250, 233, 233), RED)
    label(pdf, 20, yb + 30, "=TEMP()  ✗  N'EXISTE PAS — c'est l'énoncé FAUX de la question officielle "
          "(« which statement is false »)", 7.6, True, RED, w=168)
    label(pdf, 14, yb + 42, "Multi-séries en Static : VIRGULES ou code de liste — jamais « + »  ·  "
          "Embedded = mise à jour DYNAMIQUE", 7.4, True, (146, 100, 0), w=USABLE)
    pdf.set_y(yb + 50)

def fig_fkeys(pdf):
    pdf._need(48)
    y = pdf.get_y() + 2
    label(pdf, 12, y, "Les touches F — retenir 5 keycaps", 8.4, True, NAVY, w=USABLE)
    yb = y + 7
    keys = [("F2", "Quote List", "piège : PAS les news", True),
            ("F4", "Quote", "", False),
            ("F5", "Refresh", "", False),
            ("F6", "Max / Min", "", False),
            ("F9", "NEWS", "la touche des news", False)]
    for i, (k, lab, warn, trap) in enumerate(keys):
        x = 16 + i * 37
        pdf.set_fill_color(*(RED if trap else NAVY))
        pdf.set_draw_color(*EDGE); pdf.set_line_width(0.3)
        pdf.rect(x, yb, 15, 11, style="DF", round_corners=True, corner_radius=2)
        pdf.set_xy(x, yb)
        pdf.set_font("DejaVu", "B", 9.5); pdf.set_text_color(255, 255, 255)
        pdf.cell(15, 11, k, align="C")
        label(pdf, x - 6, yb + 12.5, lab, 6.8, True, NAVY, align="C", w=27)
        if warn:
            label(pdf, x - 6, yb + 16.5, warn, 6.2, False, RED, align="C", w=27)
        if lab == "NEWS":
            label(pdf, x - 6, yb + 16.5, "★ à retenir", 6.2, False, GREEN, align="C", w=27)
    pdf.set_y(yb + 25)

FIGS = {"linkchannel": fig_linkchannel, "newsaccess": fig_newsaccess,
        "briefcase": fig_briefcase, "staticts": fig_static_ts,
        "excelmap": fig_excelmap, "fkeys": fig_fkeys}

# ---------------------------------------------------------------- render
def render2(path, title, tag, badge, stitle, meta, blocks):
    pdf = LSEGPdf(title, tag)
    pdf.cover(badge, title, stitle, meta)
    for b in blocks:
        kind = b[0]
        if kind == "fig":
            FIGS[b[1]](pdf)
        elif kind == "h1":
            pdf.h1(b[1])
        elif kind == "h2":
            pdf.h2(b[1])
        elif kind == "p":
            pdf.p(b[1])
        elif kind == "bullets":
            pdf.bullets(b[1])
        elif kind == "box":
            pdf.box(b[1], b[2], *b[3:])
        elif kind == "table":
            pdf.tbl(b[1], b[2], b[3] if len(b) > 3 else None)
        elif kind == "q":
            pdf.q(b[1], b[2], b[3])
        elif kind == "ans":
            pdf.ans(b[1], b[2], len(b) > 3 and b[3])
        elif kind == "pagebreak":
            pdf.pagebreak()
    pdf.output(path)
    print("PDF écrit :", path)

# ---------------------------------------------------------------- MOCK B (30 Q, format réel)
S1 = ["Which function key opens the Quote List?",
      ["F9", "F2", "F4", "F6"]]
S2 = ["You were viewing Air Liquide, then Shell. You now open a new Chart app. What does it display by default?",
      ["Air Liquide", "Shell", "The first index in your Monitor list", "It opens empty"]]
S3 = ["The Search box is powered by Autosuggest and can find:",
      ["Apps and instruments only", "People only", "Answers to your questions",
       "Apps, instruments, data AND answers"]]
S4 = ['Typing "NEWSD" in the Search box opens:',
      ["Top News", "News Monitor", "News Discovery", "My Briefcase"]]
S5 = ["How do you save your current workspace for later use or sharing?",
      ["Workspaces cannot be saved manually", "Right-click the workspace tab and choose Save",
       "Upload it to the Template Library", "Press F5"]]
S6 = ["Several apps share the same Link Channel colour. You type a new instrument code into one of them. What happens?",
      ["Only that app changes",
       "All the linked apps automatically display content for the new instrument",
       "The Link Channel colour resets to default", "A new workspace is created"]]
S7 = ["True or False: in News Monitor, you can exclude certain criteria (e.g. a specific source) from your results.",
      ["True", "False"]]
S8 = ["You want to reuse a complex news search tomorrow. What do you do?",
      ["Right-click > File > Favorites > Add to Favorites", "Upload it to the Template Library",
       "Save it in My Files", "Copy it into Excel"]]
S9 = ["The Timeline toggle in News Monitor displays stories:",
      ["In reverse chronological order or by the date/time criteria you have chosen",
       "Alphabetically by source", "Ranked by number of readers", "Only from the last 24 hours"]]
S10 = ["You want to read saved research during a flight with no internet. Which feature?",
       ["My Briefcase", "Template Library", "Aggregates", "Datastream Navigator"]]
S11 = ['Typing "TotalEnergies OV" opens:',
       ["TotalEnergies' quote line", "TotalEnergies' Company Overview",
        "TotalEnergies' news only", "A Screener pre-filtered on energy"]]
S12 = ["A company's peers list can be built from:",
       ["Analyst coverage overlap", "Business classification (TRBC / GICS)",
        "Competitors identified in the company's filings", "All of the above"]]
S13 = ['"Quick Search" in the Advanced Research Search app filters across:',
       ["Report type, Contributor and Industry", "Report type only",
        "Contributor only", "Language only"]]
S14 = ["The Sustainable Finance landing page app (SUSFIN) includes:",
       ["Research and white papers, a What's New section, and a full list of sustainability-related apps and views",
        "Only ESG scores", "Only carbon emission prices", "Only regulatory news"]]
S15 = ["Which classification schema is NOT supported by the Aggregates app?",
       ["GICS", "TRBC", "SIC", "Both GICS and TRBC"]]
S16 = ["True or False: custom market-cap groups can be defined in the Aggregates app.",
       ["True", "False"]]
S17 = ["TRBC (LSEG Business Classifications) provides how many levels of industry granularity?",
       ["3", "5", "8", "10"]]
S18 = ["You want to see the same instrument as 1-day, 1-month and 1-year charts at once. Which feature?",
       ["Split mode, split by interval", "My Briefcase", "The Timeline toggle", "Template Library"]]
S19 = ["You type a new instrument in your Monitor and the chart updates instantly. Why?",
       ["Both apps are tuned to the same Link Channel colour", "The chart refreshes every 60 seconds",
        "My Briefcase syncs them", "It is a coincidence"]]
S20 = ["You need a reusable list of companies filtered by country, sector and market cap. Which app?",
       ["Aggregates", "Screener", "News Monitor", "Formula Builder"]]
S21 = ["In Excel, the Formula Builder can retrieve:",
       ["Real-time, fundamental AND historical data", "Real-time data only",
        "Fundamental data only", "Historical data only"]]
S22 = ["Which function does NOT exist in the Excel add-in?",
       ["=TR", "=RHistory", "=RSearch", "=TEMP"]]
S23 = ["Pre-built Excel templates are accessed by:",
       ["Clicking 'Templates' in the LSEG menu", "Typing =TEMPLATES() in a cell",
        "Opening My Briefcase", "The Datastream Navigator"]]
S24 = ["You want your COLLEAGUES (other users) to open your Excel file from their own Workspace. You upload it to:",
       ["My Files", "The Template Library", "My Briefcase", "The Request Table"]]
S25 = ["In a Static Request, to download data for several series you:",
       ["Type the codes separated by commas, or use a list code",
        "Type the codes separated by a plus sign",
        "Must search each series in Navigator — typing codes is impossible",
        "Must use a Time Series request instead"]]
S26 = ["With a list in a Static Request, how many datatypes can be returned for each series in the list?",
       ["Exactly 1", "Between 1 and 10", "Up to 50", "Unlimited"]]
S27 = ["What is the benefit of embedding a Datastream for Office (Excel) request?",
       ["The data can be dynamically updated going forward", "The request can never be changed",
        "It downloads more data than a manual request", "Only embedded requests support charts"]]
S28 = ['In the Excel Request Table, the request type "TSL" means:',
       ["Time series request for lists", "A static list request",
        "A chart request", "A template sheet"]]
S29 = ["Which TWO of the following are ways to add a chart or charts from the Library to a collection?",
       ["Single chart: open the flyout next to the chart, go to Collections, select Add to collection",
        "Multiple charts: tick the checkboxes next to the charts, then click the Add to collection icon on the toolbar",
        "Right-click a chart and select Add to collection",
        "Right-click a folder in the Library > Export > To collection"]]
S30 = ["Which of the following data is NOT available for Equities?",
       ["Attribution data types", "Asset4 ESG data",
        "WorldScope Company Accounts data", "I/B/E/S estimates"]]

ANS_B = [
    ("Q1 → B", "**F2 = Quote List** (piège classique : F9 = news, F4 = Quote, F6 = Max/Min). [M1]"),
    ("Q2 → B", "Instrument actif = **le dernier consulté** → Shell (pas Air Liquide, pas vide). [M1]"),
    ("Q3 → D", "Autosuggest trouve apps, **instruments/données et réponses (Answers)**. [M1]"),
    ("Q4 → C", "**NEWSD = News Discovery** (TOPNEWS = Top News, NEWS = News Monitor). [M1/M2]"),
    ("Q5 → B", "**Clic droit sur l'onglet workspace > Save** (sauvegarde/partage). [M1]"),
    ("Q6 → B", "Même couleur Link Channel = **toutes les apps liées suivent le nouvel instrument**. [M1]"),
    ("Q7 → A", "**VRAI** — les filtres avancés News Monitor permettent des **exclusions**. [M2]"),
    ("Q8 → A", "News filter réutilisable = **clic droit > File > Favorites > Add to Favorites**. [M2]"),
    ("Q9 → A", "Timeline = **chronologique inverse OU critères date/heure choisis**. [M2]"),
    ("Q10 → A", "**My Briefcase** = lecture offline (dont mobile, même hors connexion). [M2]"),
    ("Q11 → B", "« Nom + OV » = **Company Overview**. [M4]"),
    ("Q12 → D", "**All of the above** (couverture analystes + classification + filings). [M4]"),
    ("Q13 → A", "Quick Search = **Report Type + Contributor + Industry** → all of these. [M4]"),
    ("Q14 → A", "SUSFIN = **white papers + What's New + liste d'apps durables** → all of these. [M5]"),
    ("Q15 → C", "Aggregates = **GICS ET TRBC** ; **SIC non supporté**. [M5]"),
    ("Q16 → A", "**VRAI** — groupes custom dont tranches de market cap (pool candidats). [M5]"),
    ("Q17 → B", "TRBC = **5 niveaux** de granularité (250 000+ sociétés, 130 pays). [M5]"),
    ("Q18 → A", "**Split mode par intervalle** (1J/1M/1A simultanés). [M3]"),
    ("Q19 → A", "**Link Channel** — même couleur = instrument partagé. [M3]"),
    ("Q20 → B", "**Screener** = filtres (place, secteur, cap) + listes réutilisables. [M4]"),
    ("Q21 → A", "Formula Builder = **real-time + fundamental + historical** → all of the above. [M6]"),
    ("Q22 → D", "**=TEMP n'existe pas** (question officielle reformulée). [M6]"),
    ("Q23 → A", "Templates pré-construits = **menu LSEG > Templates** (pas depuis une cellule). [M6]"),
    ("Q24 → B", "**Template Library** = partage avec les AUTRES utilisateurs (My Files = perso). [M6]"),
    ("Q25 → A", "**Virgules ou code de liste** — jamais « + ». [M6]"),
    ("Q26 → B", "Liste en static = **1 à 10 datatypes** par série. [M6]"),
    ("Q27 → A", "Embedded = **mise à jour dynamique** des données. [M6]"),
    ("Q28 → A", "Types Request Table : TS, S, **TSL** (time series pour listes), L, CH. [M6]"),
    ("Q29 → A et B", "« Which TWO » : **flyout** (une chart) + **cases à cocher + icône toolbar** (plusieurs). [M6]"),
    ("Q30 → A", "**Attribution data types** : non disponibles pour les équities. [M6]"),
]

MOCK_B_BLOCKS = [("h1", "MOCK EXAM B — 30 QUESTIONS (FORMAT EXACT DE L'EXAMEN RÉEL)"),
    ("p", "60 minutes chrono, sans notes, comme le vrai. Une seule bonne réponse SAUF « Which TWO » (2 cases). "
          "Seuil réel : **24/30** — ton objectif : **30/30**. Corrigé détaillé juste après (ne pas regarder avant)."),
    ("h2", "Section A — Workspace & News [M1-M2]")]
MOCK_B_BLOCKS += [("q", i + 1, S[0], S[1]) for i, S in enumerate(
    [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10])]
MOCK_B_BLOCKS += [("h2", "Section B — Company, Industry & Charts [M3-M5]")]
MOCK_B_BLOCKS += [("q", i + 11, S[0], S[1]) for i, S in enumerate(
    [S11, S12, S13, S14, S15, S16, S17, S18, S19, S20])]
MOCK_B_BLOCKS += [("h2", "Section C — Excel, Datastream & API [M6]")]
MOCK_B_BLOCKS += [("q", i + 21, S[0], S[1]) for i, S in enumerate(
    [S21, S22, S23, S24, S25, S26, S27, S28, S29, S30])]
MOCK_B_BLOCKS += [("h2", "CORRIGÉ MOCK B — réponse + justification + module à relire")]
MOCK_B_BLOCKS += [("ans", lab, txt) for lab, txt in ANS_B]
MOCK_B_BLOCKS += [("box", "Barème Mock B (comparé au format réel)",
     "**30/30** : objectif atteint → réserve ton créneau.  **≥ 28** : excellent (le vrai seuil est 24/30).  "
     "**24-27** : au-dessus du seuil, consolide les modules [Mx] des erreurs.  "
     "**< 24** : ne réserve pas — reprends la fiche puis refais le Mock B à 48 h.")]

# ---------------------------------------------------------------- blocs globaux
PROMPTS = ("**Mode examen** : « Sert-moi les 30 questions du MOCK B une par une, sans montrer le corrigé. "
           "J'écris la lettre, tu passes à la suivante. À la fin : note /30, tableau des erreurs + modules à revoir. »\n"
           "**Mode drill** : « Interroge-moi en désordre sur les questions ★ du MOCK A ; corrige chaque réponse immédiatement. »\n"
           "**Mode flash** : « Génère 20 nouvelles questions du même style que le MOCK B, avec corrigé séparé. »\n"
           "**Mode explication** : « Pour chaque question ratée, reformule la règle produit en une phrase + un moyen mnémotechnique. »")

BLOCKS = [
    ("box", "MODE D'EMPLOI — avec Copilot / ChatGPT / Claude",
     "Donne ce PDF (ou le fichier MOCK-EXAMS-ET-CORRIGES.md du repo) à ton assistant et colle un des prompts :\n" + PROMPTS),
    ("h1", "MOCK EXAM A — 40 QUESTIONS (SIMULATION ÉTENDUE)"),
    ("p", "45 minutes conseillées, sans notes. Une seule bonne réponse SAUF mention « Which TWO ». "
          "★ = question issue des sample questions officielles LSEG ou du pool réel de candidats. Corrigé juste après."),
]
BLOCKS += [b for b in MOCK_BLOCKS if b[0] not in ("box",)]  # 40 questions + corrigé A + bilan
BLOCKS += [("pagebreak",)] + MOCK_B_BLOCKS
BLOCKS += [
    ("pagebreak",),
    ("h1", "MÉMO VISUEL — 6 SCHÉMAS POUR ANCER L'IMAGE MENTALE"),
    ("p", "Dessins exacts (générés par code, pas d'IA) : chaque schéma couvre les questions correspondantes du mock. "
          "Si tu sais re-dessiner ces 6 images de tête, tu as tes 30/30."),
    ("fig", "linkchannel"),
    ("fig", "newsaccess"),
    ("fig", "briefcase"),
    ("fig", "staticts"),
    ("fig", "excelmap"),
    ("fig", "fkeys"),
    ("h2", "Fiabilité des réponses"),
    ("box", "D'où viennent les corrigés ?",
     "• **Sources officielles** : « Certification sample questions — LSEG Workspace » (PDF officiel maj 11/24), modules du "
     "LSEG Learning Centre, guides rapides Eikon/Workspace (Thomson Reuters/Refinitiv), manuel Datastream for Office, QRC de formation Refinitiv.\n"
     "• Toutes les réponses des deux mocks en découlent directement.\n"
     "• **Seules exceptions (pool candidats, non officiel)** : « Story layout » (News Monitor) et « custom market-cap groups » "
     "(Aggregates) — marquées ⚠ dans la fiche de révision ; dans ce mock, Q16 du Mock B est concernée (raisonnement fourni)."),
]

if __name__ == "__main__":
    import os
    out = os.path.dirname(os.path.abspath(__file__))
    render2(os.path.join(out, "MOCKS-AB-Certification-LSEG-Workspace.pdf"),
            "Mock Exams A + B — Certification LSEG Workspace",
            "Mocks A+B + corrigés — Certification LSEG Workspace",
            "MOCKS A + B · 70 QUESTIONS · CORRIGÉS · MÉMO VISUEL",
            "Mock A (40 Q) + Mock B format réel (30 Q) — corrigés justifiés — schémas pour Copilot",
            "Fichier de travail pour Copilot/ChatGPT/Claude : questions exactes, corrigés sourcés, 6 schémas visuels. "
            "Format réel : 30 Q · 60 min · ≥ 80 % · 2 tentatives.",
            BLOCKS)
