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

Mise à jour du 09/10/2026 : + Bloomberg Market Concepts (BMC), + ShockDesk,
liens cliquables (tél., e-mail, LinkedIn, GitHub, démo).

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


class Doc:
    def __init__(self, out, subject):
        self.c = canvas.Canvas(out, pagesize=A4)
        self.c.setTitle("CV — Calvin MINANG")
        self.c.setAuthor("Calvin MINANG")
        self.c.setSubject(subject)
        self.c.setCreator("build_cv.py (reportlab)")

    def _baseline(self, top, size):
        return H - (top + KBASE * size)

    def text(self, x, top, segs, size, color=INK, align_right_to=None):
        """segs = [(texte, font, url|None), ...] — une seule ligne (non wrappée)."""
        if align_right_to is not None:
            total = sum(stringWidth(t, f, size) for t, f, _ in segs)
            x = align_right_to - total
        self.c.setFillColorRGB(*color)
        for text, font, url in segs:
            self.c.setFont(font, size)
            self.c.drawString(x, self._baseline(top, size), text)
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

    def para(self, top, segs, size, color=INK, first_x=None, cont_x=None, lead=None):
        """Paragraphe wrappé. Retourne le top de la dernière ligne."""
        first_x = X if first_x is None else first_x
        cont_x = X if cont_x is None else cont_x
        lead = lead if lead else size * 1.33
        t = top
        for i, words in enumerate(self._wrap(segs, size, first_x, cont_x)):
            x = first_x if i == 0 else cont_x
            self.c.setFillColorRGB(*color)
            for w, f, url in words:
                self.c.setFont(f, size)
                self.c.drawString(x, self._baseline(t, size), w)
                ww = stringWidth(w, f, size)
                if url:
                    self.c.linkURL(url, (x, H - (t + size), x + ww, H - t + size * 0.3),
                                   relative=0, thickness=0)
                x += ww + stringWidth(" ", REG, size)
            t += lead
        return t - lead

    def section(self, title, top):
        """Titre + filet. Retourne le top de la première ligne de contenu."""
        self.text(X0, top, [(title, BLD, None)], 9.4, color=NAVY)
        self.c.setStrokeColorRGB(*NAVY)
        self.c.setLineWidth(1.0)
        self.c.line(X0 + 0.5, H - (top + 13.9), RIGHT, H - (top + 13.9))
        return top + 17.0

    def bullet(self, top, segs, size=8.4):
        """Puce • puis paragraphe wrappé. Retourne le top de la dernière ligne."""
        self.text(X, top - 1.7, [("•", REG, None)], 10.0, color=INK)
        return self.para(top, segs, size, color=INK, first_x=XB, cont_x=XBC, lead=11.2)

    def entry(self, top, name, date, url=None):
        """Ligne d'entrée : nom (gras) + date (gras bleu, alignée droite)."""
        self.text(X0, top, [(name, BLD, url)], 9.0, color=INK)
        if date:
            self.text(0, top, [(date, BLD, None)], 8.4, color=BLUE, align_right_to=RIGHT)
        return top

    def save(self, bottom):
        print("  bas contenu : %.1f pt (limite ~ 800)" % bottom)
        self.c.showPage()
        self.c.save()
        print("  →", self.c._filename)


# ============================================================== contenu ======
TEL = "tel:+33752975809"
MAIL = "mailto:calvin.minang@skema.edu"
LI = "https://linkedin.com/in/calvin-minang"
GH = "https://github.com/Calvin29990"
DEMO = "https://shockdesk.onrender.com"
DEMOX = "https://calvin-minibloomberg.netlify.app"
GHSHOCK = "https://github.com/Calvin29990/shockdesk"

HDR2_BN = [([("github.com/Calvin29990", REG, GH), (" · ", REG, None),
             ("shockdesk.onrender.com", REG, DEMO)], 8.6, INK)]
HDR2_GE = [([("github.com/Calvin29990", REG, GH), (" · ", REG, None),
             ("calvin-minibloomberg.netlify.app", REG, DEMOX), (" · ", REG, None),
             ("shockdesk.onrender.com", REG, DEMO)], 8.6, INK)]


def header(d, hdr2):
    d.text(X, 33.1, [("CALVIN MINANG", BLD, None)], 18.0, color=NAVY)
    d.text(X, 54.2, [("GLOBAL MARKETS SALES | FX, RATES & EQUITIES", BLD, None)], 9.6, color=BLUE)
    d.text(X, 67.2, [("Disponible à partir de mi-décembre 2026 · Paris, France", OBL, None)], 8.8, color=GRAY)
    d.c.setStrokeColorRGB(*LIGHT)
    d.c.setLineWidth(0.7)
    d.c.line(X, H - 84.5, 549.6, H - 84.5)
    d.text(X, 86.9, [("+33 7 52 97 58 09", REG, TEL), (" · ", REG, None),
                     ("calvin.minang@skema.edu", REG, MAIL), (" · ", REG, None),
                     ("linkedin.com/in/calvin-minang", REG, LI)], 8.6, color=INK)
    segs, size, color = hdr2[0]
    d.text(X, 97.9, segs, size, color=color)


def formation(d, t0):
    t = d.section("FORMATION", t0)
    d.entry(t, "SKEMA Business School", "07/2022 – 12/2026")
    t = d.para(t + 11.5, [("Programme Grande École (M2 CFM) — Double diplôme : MSc Corporate "
                           "Financial Management", REG, None)], 8.4, lead=10.8)
    t = d.para(t + 10.8, [("Campus Belo Horizonte, Brésil — Cours : FX & arbitrage · Fixed Income · "
                           "Valuation & Risk Management · Market Risk", REG, None)], 8.4, lead=10.8)
    t = d.bullet(t + 9.0, [("Mentions :", BLD, None),
                           (" International Finance 14/20 · Sustainable and Climate Risk 17/20 · "
                            "Risk Mgmt & Investment Mgmt (F1 117) 14/20 · Advanced Financial "
                            "Analysis (S2 220) 14/20", REG, None)])
    t = d.entry(t + 15.2, "Ipesup — Classe préparatoire aux grandes écoles de commerce (CPGE)", "08/2021 – 08/2022")
    t = d.bullet(t + 11.5, [("Concours BCE :", BLD, None),
                            (" dissertation culture générale 17/20 · mathématiques 2 16/20 · "
                             "dissertation ESH 2022 18/20 · épreuve d'entretien SKEMA 19/20", REG, None)])
    return t


def experience(d, t0):
    t = d.section("EXPÉRIENCE PROFESSIONNELLE", t0)

    t = d.entry(t, "BPCE Assurances — Analyste Reporting Multi-Actifs (stage)", "01/2024 – 05/2024")
    t = d.para(t + 11.5, [("Périmètre : 103 Md€ d'actifs d'assurance-vie en gestion directe "
                           "(données groupe, fin 2024)", OBL, None)], 7.9, color=GRAY, lead=10.6)
    t = d.bullet(t + 10.2, [("Production quotidienne de reportings multi-actifs pour les comités "
                             "d'investissement : paires de change, indices actions, taux et spreads "
                             "de crédit.", REG, None)])
    t = d.bullet(t, [("Construction d'extractions Bloomberg BQL sur les forwards et swaps ; suivi "
                      "des courbes de taux €STR et SOFR.", REG, None)])
    t = d.bullet(t, [("Automatisation Excel/VBA et supports de marché sur les tendances et la "
                      "volatilité.", REG, None)])

    t = d.entry(t + 15.2, "SKEMA Business School — Assistant CRM & données partenaires", "10/2025 – 12/2025")
    t = d.para(t + 11.5, [("Direction Executive Education / Marketing & Communication — lien avec "
                           "la direction générale du campus.", OBL, None)], 7.9, color=GRAY, lead=10.6)
    t = d.bullet(t + 10.2, [("Nettoyage, dé-doublonnage et validation de la base de données "
                             "partenaires.", REG, None)])
    t = d.bullet(t, [("Mise à jour de 537 fiches contacts et 102 fiches entreprises pour les campus "
                      "de Dubaï et Belo Horizonte.", REG, None)])

    t = d.entry(t + 15.2, "FinStart.io — Sales (stage)", "06/2023 – 08/2023")
    t = d.bullet(t + 11.5, [("Prospection B2B auprès de consultants indépendants en finance, "
                             "comptabilité, risque et conformité : environ 100 e-mails par jour, "
                             "500 par semaine, suivi complet des réponses.", REG, None)])
    t = d.bullet(t, [("Sourcing et vérification de profils via APEC et LinkedIn ; invitations à "
                      "rejoindre la plateforme FinStart.", REG, None)])

    t = d.entry(t + 15.2, "SKEMA Job Service Paris — Membre du bureau · RH & Partenariats", "09/2022 – 08/2023")
    t = d.para(t + 11.5, [("CDD — missions de prospection.", OBL, None)], 7.9, color=GRAY, lead=10.6)
    t = d.bullet(t + 10.2, [("Prospection et développement de partenariats pour l'offre de staffing "
                             "étudiant : présentation de l'offre, qualification des besoins, "
                             "entretiens et événements RH avec SKEMA, EY et le Stade de France.", REG, None)])
    t = d.bullet(t, [("Bilan collectif S1 2023 : 19 100 € de chiffre d'affaires, 125 étudiants "
                      "recrutés pour 35 missions et 5 partenaires, dont 4 nouveaux (EY, Roadbook, "
                      "Auverprime, CDEFM).", REG, None)])
    return t


def skills(d, t0, marches, certifs):
    t = d.section("COMPÉTENCES TECHNIQUES & CERTIFICATIONS", t0)
    t = d.para(t, [("Sales Desk :", BLD, None),
                   (" prospection B2B, présentation de l'offre, qualification des besoins, suivi "
                    "des réponses et gestion CRM.", REG, None)], 8.4, lead=11.4)
    t = d.para(t + 11.4, [("Marchés :", BLD, None), (" " + marches, REG, None)], 8.4, lead=11.4)
    t = d.para(t + 11.4, [("Outils :", BLD, None),
                          (" Bloomberg Terminal (BQL) · Excel/VBA · Python (pandas, scikit-learn) · "
                           "SQL (BigQuery) · R · JavaScript.", REG, None)], 8.4, lead=11.4)
    t = d.para(t + 11.4, [("Certifications :", BLD, None), (" " + certifs, REG, None)], 8.4, lead=11.4)
    return t


def langues(d, t0):
    t = d.section("LANGUES", t0)
    return d.para(t, [("Français (natif) · Anglais (professionnel) · Espagnol (B2) · "
                       "Portugais (notions)", REG, None)], 8.4)


CERTIFS = ("Bloomberg Market Concepts (BMC — Bloomberg for Education, 2026) · candidat FRM (GARP) · "
           "AMF en cours · Citi Markets Sales & Trading (Forage) · QuantInsti (Python for Trading ; "
           "Options Trading Strategies in Python)")


# ========================================================= CV BNP ============
def build_bnp():
    print("CV BNP (ShockDesk uniquement) :")
    d = Doc(os.path.join(HERE, "CV_Calvin_MINANG_ShockDesk.pdf"),
            "ShockDesk — Stage Front Office (vente / structuration) janv. 2027")
    header(d, HDR2_BN)

    t = d.section("PROFIL", 113.9)
    t = d.para(t, [("Étudiant en dernière année du Programme Grande École de SKEMA Business School "
                    "et du MSc Corporate Financial Management. Reporting multi-actifs et suivi des "
                    "marchés chez BPCE Assurances ; prospection B2B, CRM partenaires et "
                    "développement commercial. Auteur de ", REG, None),
                   ("ShockDesk", BLD, None),
                   (", poste de trading complet (prévisions point-in-time, backtests avec coûts "
                    "réels, attribution du P&L, pricer d'options et structures) ; certifié ", REG, None),
                   ("Bloomberg Market Concepts (BMC)", BLD, None),
                   (". Cible : stage Front Office de 6 mois (vente ou structuration) à partir de "
                    "janvier 2027.", REG, None)], 8.5, lead=11.0)

    t = formation(d, t + 17.0)
    t = experience(d, t + 19.0)

    t = d.section("PROJET PHARE", t + 19.0)
    t = d.entry(t, "ShockDesk — Poste de trading & stress-testing", "Python · yfinance",
                url=GHSHOCK)
    t = d.para(t + 11.5, [("Poste de travail complet : prévisions point-in-time datées (révisions "
                           "auditables, scorecard ex-post), backtests avec slippage et commissions "
                           "facturés, attribution du P&L par ligne (alpha/bêta vs benchmark), pricer "
                           "d'options (surface de volatilité, Greeks) et catalogue de structures "
                           "(butterfly, iron condor, strangles).", REG, None)], 8.4, lead=10.9)
    t = d.para(t + 10.9, [("Cas pratique « Book choc pétrolier ShockLab » : scénario géopolitique "
                           "Brent (type détroit d'Ormuz) sur l'univers global-macro — 42 barres "
                           "yfinance (données réelles), 21 trades, stop calendaire fixé ex-ante.", REG, None)],
              8.4, lead=10.9)
    t = d.para(t + 10.9, [("Démo live :", BLD, None), (" shockdesk.onrender.com", REG, DEMO),
                          (" · Code source :", BLD, None), (" github.com/Calvin29990/shockdesk", REG, GHSHOCK),
                          (" · Cours de 57 pages disponible sur demande.", REG, None)], 8.4, lead=10.9)

    t = skills(d, t + 19.0,
               "FX (forwards, swaps) · taux · fixed income · dérivés actions · options et structures "
               "(butterfly, iron condor, strangles) · volatilité · risque de marché (VaR)",
               CERTIFS)
    t = langues(d, t + 17.0)
    d.save(t)


# ====================================================== CV général ===========
def build_general():
    print("CV général (3 projets) :")
    d = Doc(os.path.join(HERE, "CV_Calvin_MINANG.pdf"),
            "Global Markets Sales — CV Calvin MINANG")
    header(d, HDR2_GE)

    t = d.section("PROFIL", 113.9)
    t = d.para(t, [("Étudiant en dernière année du Programme Grande École de SKEMA Business School "
                    "et du MSc Corporate Financial Management. Reporting multi-actifs et suivi des "
                    "marchés ; prospection B2B, CRM partenaires et développement commercial. Certifié ", REG, None),
                   ("Bloomberg Market Concepts (BMC)", BLD, None),
                   (", auteur de trois projets marché : terminal cross-asset, pricer d'options et "
                    "poste de trading ShockDesk. Cible : Global Markets Sales Desk — FX Sales, "
                    "Rates Sales, Cross-Asset Sales et dérivés actions.", REG, None)], 8.5, lead=11.0)

    t = formation(d, t + 17.0)
    t = experience(d, t + 19.0)

    t = d.section("PROJETS SÉLECTIONNÉS", t + 19.0)
    t = d.entry(t, "CalvinX — Tableau de bord cross-asset", "JavaScript", url=DEMOX)
    t = d.para(t + 11.5, [("Suivi du FX, des indices actions, des taux, des matières premières et "
                           "de la volatilité ; estimateur de régime Risk-On/Risk-Off, export Excel. "
                           "Démo :", REG, None),
                          (" calvin-minibloomberg.netlify.app", REG, DEMOX)], 8.4, lead=10.9)
    t = d.entry(t + 14.9, "ShockDesk — Poste de trading & stress-testing", "Python · yfinance",
                url=GHSHOCK)
    t = d.para(t + 11.5, [("Prévisions point-in-time, backtests avec coûts réels, attribution du "
                           "P&L par ligne, pricer d'options et structures (butterfly, iron condor, "
                           "strangles). Démo :", REG, None),
                          (" shockdesk.onrender.com", REG, DEMO)], 8.4, lead=10.9)
    t = d.entry(t + 14.9, "Pricer Black-Scholes — Options & Greeks", "Excel · VBA")
    t = d.para(t + 11.5, [("Calcul des prix d'options européennes et analyse des sensibilités Delta, "
                           "Gamma et Vega avec Excel/VBA. Portfolio de projets détaillé :", REG, None),
                          (" linkedin.com/in/calvin-minang", REG, LI)], 8.4, lead=10.9)

    t = skills(d, t + 19.0,
               "FX (forwards, swaps) · taux · fixed income · dérivés actions · volatilité · "
               "suivi multi-actifs · risque de marché (VaR)",
               CERTIFS)
    t = langues(d, t + 17.0)
    d.save(t)


if __name__ == "__main__":
    build_bnp()
    build_general()
