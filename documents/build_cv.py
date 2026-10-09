#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_cv.py — Régénère les CV de Calvin (documents/)

Design : celui du CV « forme bleue » (Resume_Calvin_MINANG.pdf) — STRICTEMENT
conservé : Helvetica, titre #1B3A5C, accents #2E5C8A, dates alignées à droite,
filets navy sous les titres de section.

Sorties :
  1. CV_Calvin_MINANG_ShockDesk.pdf — BNP CIB : uniquement ShockDesk
  2. CV_Calvin_MINANG.pdf           — Général : 3 projets (CACEIS & autres)

Règles de contenu (09/10/2026) :
  - PAS de « candidat FRM » : statut CFA uniquement (membre ICAN du CFA Institute,
    CFA Level I prévu pendant le stage, sinon 2027).
  - Dépôt GitHub ShockDesk PRIVÉ : jamais de lien github.com/.../shockdesk —
    uniquement la démo live (shockdesk.onrender.com) et les fonctionnalités.
  - Liens cliquables (tél., e-mail, LinkedIn, GitHub profil, démo).
  - Curseur de ligne unique : aucune superposition possible.

Usage :  python3 build_cv.py       (depuis documents/)
Dépendance : pip install reportlab
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth

# ---------------------------------------------------------------- design ----
NAVY = (0x1B / 255.0, 0x3A / 255.0, 0x5C / 255.0)   # #1B3A5C titres + filets
BLUE = (0x2E / 255.0, 0x5C / 255.0, 0x8A / 255.0)   # #2E5C8A sous-titre + dates
INK = (0x22 / 255.0, 0x22 / 255.0, 0x22 / 255.0)    # #222222 corps
GRAY = (0x4A / 255.0, 0x4A / 255.0, 0x4A / 255.0)   # #4A4A4A italiques
LIGHT = (0xC8 / 255.0, 0xD2 / 255.0, 0xDC / 255.0)  # #C8D2DC filet contact

W, H = A4
X0 = 42.5          # titres de section / noms d'entrée
X = 45.7           # texte courant
XB = 55.2          # texte après puce
XBC = 53.7         # retour à la ligne après puce
RIGHT = 552.8      # bord droit (dates, tags)

REG, BLD, OBL = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"
KBASE = 1.075      # baseline = top + KBASE * size (calibré pymupdf)

HERE = os.path.dirname(os.path.abspath(__file__))

# liens
TEL = "tel:+33752975809"
MAIL = "mailto:calvin.minang@skema.edu"
LI = "https://linkedin.com/in/calvin-minang"
GH = "https://github.com/Calvin29990"
DEMO = "https://shockdesk.onrender.com"
DEMOX = "https://calvin-minibloomberg.netlify.app"


class Doc:
    """Page A4 — TOUT passe par un curseur unique `t` (top de la prochaine
    ligne libre). Aucune fonction ne redessine à une position déjà consommée."""

    def __init__(self, out, subject):
        self.c = canvas.Canvas(out, pagesize=A4)
        self.c.setTitle("CV — Calvin MINANG")
        self.c.setAuthor("Calvin MINANG")
        self.c.setSubject(subject)
        self.c.setCreator("build_cv.py (reportlab)")
        self.t = 0.0

    # ---- bas niveau ----
    def _draw(self, x, top, segs, size, color):
        self.c.setFillColorRGB(*color)
        for text, font, url in segs:
            self.c.setFont(font, size)
            self.c.drawString(x, H - (top + KBASE * size), text)
            w = stringWidth(text, font, size)
            if url:
                self.c.linkURL(url, (x, H - (top + size), x + w, H - top + size * 0.3),
                               relative=0, thickness=0)
            x += w

    def _wrap(self, segs, size, first_x, cont_x):
        words = []
        for text, font, url in segs:
            for w in text.split(" "):
                if w:
                    words.append((w, font, url))
        lines, cur, cur_w, first = [], [], 0.0, True
        for w, font, url in words:
            ww = stringWidth(w, font, size)
            sp = stringWidth(" ", REG, size)
            limit = RIGHT - (first_x if first else cont_x)
            if cur and cur_w + sp + ww > limit:
                lines.append(cur)
                cur, cur_w, first = [], 0.0, False
            if cur:
                cur_w += sp
            cur.append((w, font, url))
            cur_w += ww
        if cur:
            lines.append(cur)
        return lines

    # ---- blocs (sémantique curseur : renvoient la prochaine ligne libre) ----
    def para(self, segs, size, color=INK, first_x=None, cont_x=None, lead=None):
        first_x = X if first_x is None else first_x
        cont_x = X if cont_x is None else cont_x
        lead = lead if lead else size * 1.33
        t = self.t
        for i, words in enumerate(self._wrap(segs, size, first_x, cont_x)):
            x = first_x if i == 0 else cont_x
            self.c.setFillColorRGB(*color)
            for w, f, url in words:
                self.c.setFont(f, size)
                self.c.drawString(x, H - (t + KBASE * size), w)
                ww = stringWidth(w, f, size)
                if url:
                    self.c.linkURL(url, (x, H - (t + size), x + ww, H - t + size * 0.3),
                                   relative=0, thickness=0)
                x += ww + stringWidth(" ", REG, size)
            t += lead
        self.t = t
        return self.t

    def line_of(self, segs, size=8.4, color=INK, align_right_to=None):
        """Une ligne non wrappée (dates, tags) — ne touche PAS au curseur."""
        if align_right_to is not None:
            total = sum(stringWidth(t, f, size) for t, f, _ in segs)
            x = align_right_to - total
        else:
            x = X
        self._draw(x, self.t, segs, size, color)

    def section(self, title, gap=5.0):
        self.t += gap
        self._draw(X0, self.t, [(title, BLD, None)], 9.4, NAVY)
        self.c.setStrokeColorRGB(*NAVY)
        self.c.setLineWidth(1.0)
        self.c.line(X0 + 0.5, H - (self.t + 13.9), RIGHT, H - (self.t + 13.9))
        self.t += 17.0
        return self.t

    def entry(self, name, date):
        self._draw(X0, self.t, [(name, BLD, None)], 9.0, INK)
        if date:
            self.line_of([(date, BLD, None)], 8.4, BLUE, align_right_to=RIGHT)
        self.t += 11.5
        return self.t

    def context(self, text):
        self.para([(text, OBL, None)], 7.9, color=GRAY, lead=10.6)
        return self.t

    def bullet(self, segs, size=8.4):
        self._draw(X, self.t - 1.7, [("•", REG, None)], 10.0, INK)
        self.para(segs, size, color=INK, first_x=XB, cont_x=XBC, lead=11.2)
        return self.t

    def bullets(self, items):
        for it in items:
            self.bullet(it)

    def save(self, bottom):
        print("  curseur final : %.1f pt (limite ~ 800)" % bottom)
        self.c.showPage()
        self.c.save()
        print("  →", self.c._filename)


# ============================================================== contenu ======
HDR1 = [("+33 7 52 97 58 09", REG, TEL), (" · ", REG, None),
        ("calvin.minang@skema.edu", REG, MAIL), (" · ", REG, None),
        ("linkedin.com/in/calvin-minang", REG, LI)]

CERTIFS = ("CFA Institute (membre ICAN) — CFA Level I en stage, sinon 2027 · Bloomberg Market "
           "Concepts (BMC, 2026) · AMF en cours · Citi Markets Sales & Trading (Forage) · "
           "QuantInsti (Python for Trading ; Options ; ML for Trading)")


def header(d, hdr2_segs):
    d._draw(X, 33.1, [("CALVIN MINANG", BLD, None)], 18.0, NAVY)
    d._draw(X, 54.2, [("GLOBAL MARKETS SALES | FX, RATES & EQUITIES", BLD, None)], 9.6, BLUE)
    d._draw(X, 67.2, [("Disponible à partir de mi-décembre 2026 · Paris, France", OBL, None)], 8.8, GRAY)
    d.c.setStrokeColorRGB(*LIGHT)
    d.c.setLineWidth(0.7)
    d.c.line(X, H - 84.5, 549.6, H - 84.5)
    d._draw(X, 86.9, HDR1, 8.6, INK)
    d._draw(X, 97.9, hdr2_segs, 8.6, INK)
    d.t = 97.9 + 11.0   # curseur = ligne libre après le contact


def formation(d):
    d.section("FORMATION")
    d.entry("SKEMA Business School", "07/2022 – 12/2026")
    d.para([("Programme Grande École (M2 CFM) — Double diplôme : MSc Corporate Financial "
             "Management", REG, None)], 8.4, lead=10.8)
    d.para([("Campus Belo Horizonte, Brésil — Cours : FX & arbitrage · Fixed Income · "
             "Valuation & Risk Management · Market Risk", REG, None)], 8.4, lead=10.8)
    d.bullet([("Mentions :", BLD, None),
              (" International Finance 14/20 · Sustainable and Climate Risk 17/20 · "
               "Risk Mgmt & Investment Mgmt (F1 117) 14/20 · Advanced Financial "
               "Analysis (S2 220) 14/20", REG, None)])
    d.t += 3.0
    d.entry("Ipesup — Classe préparatoire aux grandes écoles de commerce (CPGE)", "08/2021 – 08/2022")
    d.bullet([("Concours BCE :", BLD, None),
              (" dissertation culture générale 17/20 · mathématiques 2 16/20 · "
               "dissertation ESH 2022 18/20 · épreuve d'entretien SKEMA 19/20", REG, None)])


def experience(d):
    d.section("EXPÉRIENCE PROFESSIONNELLE", gap=6.5)

    d.entry("BPCE Assurances — Analyste Reporting Multi-Actifs (stage)", "01/2024 – 05/2024")
    d.context("Périmètre : 103 Md€ d'actifs d'assurance-vie en gestion directe "
              "(données groupe, fin 2024)")
    d.bullets([
        [("Production quotidienne de reportings multi-actifs pour les comités "
          "d'investissement : paires de change, indices actions, taux et spreads "
          "de crédit.", REG, None)],
        [("Construction d'extractions Bloomberg BQL sur les forwards et swaps ; suivi "
          "des courbes de taux €STR et SOFR.", REG, None)],
        [("Automatisation Excel/VBA et supports de marché sur les tendances et la "
          "volatilité.", REG, None)],
    ])

    d.t += 3.0
    d.entry("SKEMA Business School — Assistant CRM & données partenaires", "10/2025 – 12/2025")
    d.context("Direction Executive Education / Marketing & Communication — lien avec "
              "la direction générale du campus.")
    d.bullets([
        [("Nettoyage, dé-doublonnage et validation de la base de données partenaires.", REG, None)],
        [("Mise à jour de 537 fiches contacts et 102 fiches entreprises pour les campus "
          "de Dubaï et Belo Horizonte.", REG, None)],
    ])

    d.t += 3.0
    d.entry("FinStart.io — Sales (stage)", "06/2023 – 08/2023")
    d.bullets([
        [("Prospection B2B auprès de consultants indépendants en finance, "
          "comptabilité, risque et conformité : environ 100 e-mails par jour, "
          "500 par semaine, suivi complet des réponses.", REG, None)],
        [("Sourcing et vérification de profils via APEC et LinkedIn ; invitations à "
          "rejoindre la plateforme FinStart.", REG, None)],
    ])

    d.t += 3.0
    d.entry("SKEMA Job Service Paris — Membre du bureau · RH & Partenariats", "09/2022 – 08/2023")
    d.context("CDD — missions de prospection.")
    d.bullets([
        [("Prospection et développement de partenariats pour l'offre de staffing "
          "étudiant : présentation de l'offre, qualification des besoins, "
          "entretiens et événements RH avec SKEMA, EY et le Stade de France.", REG, None)],
        [("Bilan collectif S1 2023 : 19 100 € de chiffre d'affaires, 125 étudiants "
          "recrutés pour 35 missions et 5 partenaires, dont 4 nouveaux (EY, Roadbook, "
          "Auverprime, CDEFM).", REG, None)],
    ])


def skills(d, marches):
    d.section("COMPÉTENCES TECHNIQUES & CERTIFICATIONS", gap=6.5)
    d.para([("Sales Desk :", BLD, None),
            (" prospection B2B, présentation de l'offre, qualification des besoins, suivi "
             "des réponses et gestion CRM.", REG, None)], 8.4, lead=11.4)
    d.para([("Marchés :", BLD, None), (" " + marches, REG, None)], 8.4, lead=11.4)
    d.para([("Outils :", BLD, None),
            (" Bloomberg Terminal (BQL) · Excel/VBA · Python (pandas, scikit-learn) · "
             "SQL (BigQuery) · R · JavaScript.", REG, None)], 8.4, lead=11.4)
    d.para([("Certifications :", BLD, None), (" " + CERTIFS, REG, None)], 8.4, lead=11.4)


def langues(d):
    d.section("LANGUES", gap=5.0)
    d.para([("Français (natif) · Anglais (professionnel) · Espagnol (B2) · "
             "Portugais (notions)", REG, None)], 8.4)


# ========================================================= CV BNP ============
def build_bnp():
    print("CV BNP (ShockDesk uniquement) :")
    d = Doc(os.path.join(HERE, "CV_Calvin_MINANG_ShockDesk.pdf"),
            "ShockDesk — Stage Front Office (vente / structuration) janv. 2027")
    header(d, [("github.com/Calvin29990", REG, GH), (" · ", REG, None),
               ("shockdesk.onrender.com", REG, DEMO)])

    d.section("PROFIL")
    d.para([("Étudiant en dernière année du Programme Grande École de SKEMA Business School "
             "et du MSc Corporate Financial Management. Reporting multi-actifs et suivi des "
             "marchés chez BPCE Assurances ; prospection B2B, CRM partenaires et "
             "développement commercial. Auteur de ", REG, None),
            ("ShockDesk", BLD, None),
            (", poste de trading complet (prévisions point-in-time, backtests avec coûts "
             "réels, attribution du P&L, pricer d'options et structures) ; certifié ", REG, None),
            ("Bloomberg Market Concepts (BMC)", BLD, None),
            (" ; membre ICAN du CFA Institute (CFA Level I en stage, sinon 2027). Cible : stage Front Office de 6 mois (vente ou structuration) à partir "
             "de janvier 2027.", REG, None)], 8.5, lead=11.0)

    formation(d)
    experience(d)

    d.section("PROJET PHARE", gap=6.5)
    d.entry("ShockDesk — Poste de trading & stress-testing", "Python · yfinance")
    d.para([("Poste de travail complet : prévisions point-in-time datées (révisions "
             "auditables, scorecard ex-post), backtests avec slippage et commissions "
             "facturés, attribution du P&L par ligne (alpha/bêta vs benchmark), pricer "
             "d'options (surface de volatilité, Greeks) et catalogue de structures "
             "(butterfly, iron condor, strangles).", REG, None)], 8.4, lead=10.9)
    d.para([("Cas pratique « Book choc pétrolier ShockLab » : scénario géopolitique "
             "Brent (type détroit d'Ormuz) sur l'univers global-macro — 42 barres "
             "yfinance (données réelles), 21 trades, stop calendaire fixé ex-ante.", REG, None)],
           8.4, lead=10.9)
    d.para([("Démo live :", BLD, None), (" shockdesk.onrender.com", REG, DEMO),
            (" — le book choc pétrolier rejoué en direct. Support de formation (57 pages) "
             "joint si utile.", REG, None)], 8.4, lead=10.9)

    skills(d, "FX (forwards, swaps) · taux · fixed income · dérivés actions · options et structures "
              "(butterfly, iron condor, strangles) · volatilité · risque de marché (VaR)")
    langues(d)
    d.save(d.t)


# ====================================================== CV général ===========
def build_general():
    print("CV général (3 projets) :")
    d = Doc(os.path.join(HERE, "CV_Calvin_MINANG.pdf"),
            "Global Markets Sales — CV Calvin MINANG")
    header(d, [("github.com/Calvin29990", REG, GH), (" · ", REG, None),
               ("calvin-minibloomberg.netlify.app", REG, DEMOX), (" · ", REG, None),
               ("shockdesk.onrender.com", REG, DEMO)])

    d.section("PROFIL")
    d.para([("Étudiant en dernière année du Programme Grande École de SKEMA Business School "
             "et du MSc Corporate Financial Management. Reporting multi-actifs et suivi des "
             "marchés ; prospection B2B, CRM partenaires et développement commercial. Certifié ", REG, None),
            ("Bloomberg Market Concepts (BMC)", BLD, None),
            (", auteur de trois projets marché : terminal cross-asset, pricer d'options et "
             "poste de trading ShockDesk. Cible : Global Markets Sales Desk — FX Sales, "
             "Rates Sales, Cross-Asset Sales et dérivés actions. Membre ICAN du CFA "
             "Institute.", REG, None)],
           8.5, lead=11.0)

    formation(d)
    experience(d)

    d.section("PROJETS SÉLECTIONNÉS", gap=6.5)
    d.entry("CalvinX — Tableau de bord de suivi cross-asset", "JavaScript")
    d.para([("Suivi du FX, des indices actions, des taux, des matières premières et "
             "de la volatilité ; estimateur de régime Risk-On/Risk-Off, export Excel. "
             "Démo :", REG, None),
            (" calvin-minibloomberg.netlify.app", REG, DEMOX)], 8.4, lead=10.9)
    d.t += 3.0
    d.entry("ShockDesk — Poste de trading & stress-testing", "Python · yfinance")
    d.para([("Prévisions point-in-time, backtests avec coûts réels, attribution du "
             "P&L par ligne, pricer d'options et structures (butterfly, iron condor, "
             "strangles). Démo :", REG, None),
            (" shockdesk.onrender.com", REG, DEMO)], 8.4, lead=10.9)
    d.t += 3.0
    d.entry("Pricer Black-Scholes — Options & Greeks", "Excel · VBA")
    d.para([("Calcul des prix d'options européennes et analyse des sensibilités Delta, "
             "Gamma et Vega avec Excel/VBA. Portfolio de projets détaillé :", REG, None),
            (" linkedin.com/in/calvin-minang", REG, LI)], 8.4, lead=10.9)

    skills(d, "FX (forwards, swaps) · taux · fixed income · dérivés actions · volatilité · "
              "suivi multi-actifs · risque de marché (VaR)")
    langues(d)
    d.save(d.t)


if __name__ == "__main__":
    build_bnp()
    build_general()
