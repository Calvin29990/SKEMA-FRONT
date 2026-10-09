#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_cv.py — Régénère les CV de Calvin (documents/)

  1. CV_Calvin_MINANG.pdf          — CV général (finance de marché / risk / dérivés & FX)
  2. CV_Calvin_MINANG_ShockDesk.pdf — CV différent, 100 % centré ShockDesk
                                      (package BNP : démo + mail en deux parties)

Mise à jour du 09/10/2026 :
  + Certification Bloomberg Market Concepts (BMC — Bloomberg for Education, 2026)
  + Projet ShockDesk (poste de trading & book choc pétrolier « ShockLab »)
  + Variante ShockDesk : projet phare unique, ciblée stage Front Office
    (Vente / Structuration) janv. 2027 — pour l'approche Wiam Qadouri (BNP CIB)

Design reproduit à l'identique du CV d'origine (A4, Helvetica, #17375E).

Usage :  python3 build_cv.py        (depuis le dossier documents/)
Dépendance : pip install reportlab
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth

# ---------------------------------------------------------------- design ----
NAVY = (0x17 / 255.0, 0x37 / 255.0, 0x5E / 255.0)   # #17375E (titres + filets)
INK = (0x11 / 255.0, 0x11 / 255.0, 0x11 / 255.0)    # #111111 (corps principal)
GRAY = (0x3D / 255.0, 0x3D / 255.0, 0x3D / 255.0)   # #3D3D3D (puces)

W, H = A4                       # 595.27 x 841.89
ML = 48.5                       # marge gauche
RIGHT = 546.76                  # bord droit des filets / du texte
LEAD = 11.76                    # interligne (points)
BASE = 1.116                    # baseline = box_top + size * BASE (rendu Chrome)

REG, BLD, OBL = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"

HERE = os.path.dirname(os.path.abspath(__file__))


class Doc:
    """Page A4 avec curseur vertical (haut de la prochaine ligne, en points)."""

    def __init__(self, out, subject):
        self.out = out
        self.c = canvas.Canvas(out, pagesize=A4)
        self.c.setTitle("CV — Calvin MINANG")
        self.c.setAuthor("Calvin MINANG")
        self.c.setSubject(subject)
        self.c.setCreator("build_cv.py (reportlab)")
        self.t = 0.0

    # ---- rendu ----
    def _wrap(self, segs, size, first_x, cont_x):
        words = []
        for text, font in segs:
            for w in text.split(" "):
                if w:
                    words.append((w, font))
        lines, cur, cur_w, first = [], [], 0.0, True
        for w, font in words:
            ww = stringWidth(w, font, size)
            sp = stringWidth(" ", font, size)
            limit = RIGHT - (first_x if first else cont_x)
            if cur and cur_w + sp + ww > limit:
                lines.append(cur)
                cur, cur_w, first = [], 0.0, False
            if cur:
                cur_w += sp
            cur.append((w, font))
            cur_w += ww
        if cur:
            lines.append(cur)
        return lines

    def line(self, segs, size=9.2, color=INK, first_x=None, cont_x=None,
             center=False):
        first_x = ML if first_x is None else first_x
        cont_x = ML if cont_x is None else cont_x
        for i, words in enumerate(self._wrap(segs, size, first_x, cont_x)):
            if center:
                total = sum(stringWidth(w, f, size) for w, f in words) + \
                    stringWidth(" ", REG, size) * (len(words) - 1)
                x = (W - total) / 2.0
            else:
                x = first_x if i == 0 else cont_x
            self.c.setFillColorRGB(*color)
            for w, f in words:
                self.c.setFont(f, size)
                self.c.drawString(x, H - (self.t + size * BASE), w)
                x += stringWidth(w, f, size) + stringWidth(" ", REG, size)
            self.t += LEAD

    def section(self, title):
        self.t += 6.1
        self.c.setFillColorRGB(*NAVY)
        self.c.setFont(BLD, 10.4)
        self.c.drawString(ML, H - (self.t + 10.4 * BASE), title)
        rule_t = self.t + 15.2
        self.c.setStrokeColorRGB(*NAVY)
        self.c.setLineWidth(0.7)
        self.c.line(ML + 0.02, H - rule_t, RIGHT, H - rule_t)
        self.t += 16.5

    def entry_gap(self):
        self.t += 3.0

    def bullet(self, segs, size=9.2):
        self.c.setFillColorRGB(*GRAY)
        self.c.setFont(REG, 10.0)
        self.c.drawString(ML, H - (self.t + size * BASE), "•")
        self.line(segs, size=size, color=GRAY, first_x=58.0, cont_x=57.5)

    # ---- blocs partagés ----
    def header(self, tagline):
        self.t = 37.3
        self.line([("CALVIN MINANG", BLD)], size=18.0, color=NAVY, center=True)
        self.t = 60.9
        self.line([(tagline, BLD)], size=9.8, color=INK, center=True)
        self.t = 75.9
        self.line([("+33 7 52 97 58 09 | calvin.minang@skema.edu | France (mobilité Paris / Londres)", REG)],
                  size=9.1, color=INK, center=True)
        self.t = 88.3
        self.line([("linkedin.com/in/calvin-minang | github.com/Calvin29990 | Démo : calvin-minibloomberg.netlify.app", REG)],
                  size=9.1, color=INK, center=True)

    def formation(self):
        self.section("FORMATION")
        self.line([("SKEMA Business School", BLD),
                   (" — Programme Grande École (grade de Master, M2) & double diplôme MSc Corporate Financial "
                    "Management | 2022 – 2026", REG)])
        self.line([("Cours principaux : Market Risk (VaR), Produits dérivés (Black-Scholes-Merton), Fixed Income, "
                    "Options & Greeks", REG)])
        self.line([("IPESUP, Paris", BLD),
                   (" — Classe préparatoire ECE (prépa HEC : mathématiques et économie intensives) | 2021 – 2022", REG)])
        self.line([("Baccalauréat général scientifique", BLD), (" (spécialité mathématiques) | 2021", REG)])

    def experience(self, bpce_bullets):
        self.section("EXPÉRIENCE PROFESSIONNELLE")
        self.line([("BPCE Assurances — Analyste Reporting Multi-Actifs (stage), Paris | 01/2024 – 05/2024", BLD)])
        for b in bpce_bullets:
            self.bullet([(b, REG)])
        self.entry_gap()
        self.line([("FinStart — Analyste Sales & Recrutement (stage), Paris | 06/2023 – 08/2023", BLD)])
        self.bullet([("Veille macroéconomique et recherches sur les crises financières pour des campagnes ciblant les "
                      "professionnels de la finance (clients : banques et cabinets de conseil).", REG)])
        self.bullet([("Sourcing de candidats, campagnes d'e-mailing et gestion de bases de données clients/candidats.", REG)])

    def langues(self):
        self.section("LANGUES")
        self.line([("Français (natif) | Anglais (professionnel, B2/C1) | Espagnol (B2)", REG)])

    def save(self):
        print("  bas de la dernière ligne : %.1f pt (limite utile ~ 801.9)" % self.t)
        self.c.showPage()
        self.c.save()
        print("  →", self.out)


# =========================================================== CV GÉNÉRAL =====
def build_general():
    print("CV général :")
    d = Doc(os.path.join(HERE, "CV_Calvin_MINANG.pdf"),
            "Finance de Marché | Market Risk | Dérivés & FX")
    d.header("Finance de Marché | Market Risk | Dérivés & FX — Stages / Off-Cycle & Graduate Programmes 2026")

    d.section("PROFIL")
    d.line([("Étudiant en dernière année à SKEMA Business School (Programme Grande École + MSc Corporate Financial "
             "Management) et candidat FRM, orienté finance de marché et produits dérivés. Expérience en reporting "
             "multi-actifs à forte volumétrie (FX majors, indices actions, taux, spreads) chez BPCE Assurances, avec "
             "Bloomberg (BQL) et automatisation Excel/VBA. Auteur de trois projets marché : un terminal cross-asset "
             "type desk de trading, un pricer d'options Black-Scholes et un poste de trading complet (stratégies, "
             "backtests, stress-testing) basé sur du machine learning. Recherche : stages (off-cycle / été) et "
             "graduate programmes 2026 en sales & trading, marchés et risque de marché.", REG)])

    d.formation()
    d.experience([
        "Production quotidienne de reportings multi-actifs à forte volumétrie (FX majors, indices actions, "
        "courbes de taux, spreads) alimentant les comités d'investissement.",
        "Construction et exploitation de courbes Bloomberg via BQL (forwards, swaps, taux non standards) "
        "pour éclairer les décisions obligataires.",
        "Automatisation de tâches répétitives sous Excel (XLOOKUP, macros VBA) : accélération significative "
        "du reporting.",
        "Réalisation de slides de marché (tendances, volatilité) à destination de managers et directeurs.",
    ])

    d.section("PROJETS SÉLECTIONNÉS")
    d.line([("CalvinX Market Terminal — Dashboard cross-asset type desk (JavaScript) |", BLD)])
    d.line([("github.com/Calvin29990/calvinx-market-terminal", BLD)])
    d.bullet([("Terminal style Bloomberg (FX, indices, matières premières, volatilité) : estimateur de régime "
               "Risk-On/Risk-Off, analytics de volatilité côté client, export Excel. Démo : "
               "calvin-minibloomberg.netlify.app", REG)])
    d.entry_gap()
    d.line([("ShockDesk — Poste de trading & stress-testing (Python · yfinance) |", BLD)])
    d.line([("github.com/Calvin29990/shockdesk · Démo : shockdesk.onrender.com", BLD)])
    d.bullet([("Poste de recherche complet : prévisions publiées point-in-time (révisions datées, scorecard ex-post), "
               "moteur de backtest avec slippage et commissions, attribution du P&L par ligne (alpha/bêta vs "
               "benchmark), pricer d'options (surface de volatilité, Greeks) et structures (butterfly, iron condor, "
               "strangles).", REG)])
    d.bullet([("Book choc pétrolier « ShockLab » : scénario géopolitique Brent (type détroit d'Ormuz) sur l'univers "
               "global-macro (Brent, S&P 500, TLT, or, dollar, crédit HY) — 42 barres, 21 trades, données réelles ; "
               "stress-test de portefeuille par analogues de marché + ML interprétable (régression logistique).", REG)])
    d.entry_gap()
    d.line([("Pricing d'options & Greeks — Pricer Black-Scholes (Excel / VBA)", BLD)])
    d.bullet([("Pricer (prix, Delta, Gamma, Vega) ; localisation du « pic de gamma » d'un livre d'options lors d'un "
               "choc pétrolier (cas Petrobras), validé sur le krach de mars 2020 (mécanisme short-gamma).", REG)])

    d.section("COMPÉTENCES TECHNIQUES & CERTIFICATIONS")
    d.bullet([("Technique :", BLD),
              (" Excel avancé (VBA, XLOOKUP), Bloomberg (BQL), Python (pandas, scikit-learn), SQL (BigQuery), R, "
               "JavaScript, data visualisation.", REG)])
    d.bullet([("Marchés :", BLD),
              (" risque de marché (VaR), pricing de dérivés (BSM), Greeks, fixed income, FX, analyse de volatilité, "
               "stress testing, backtesting.", REG)])
    d.bullet([("Certifications :", BLD),
              (" FRM (candidat, GARP) ; Bloomberg Market Concepts (BMC — Bloomberg for Education, 2026) ; AMF (en "
               "cours) ; Citi Markets Sales & Trading (Forage) ; QuantInsti (Python for Trading ; Options Trading "
               "Strategies in Python ; ML for Trading) ; Kaggle (Intro to SQL).", REG)])

    d.langues()
    d.save()


# ====================================================== CV SHOCKDESK ========
def build_shockdesk():
    print("CV ShockDesk (package BNP) :")
    d = Doc(os.path.join(HERE, "CV_Calvin_MINANG_ShockDesk.pdf"),
            "ShockDesk — Stage Front Office (Vente / Structuration) janv. 2027")
    d.header("Finance de Marché | Produits Structurés & Dérivés — Stage Front Office 6 mois (Vente / Structuration) — janv. 2027")

    d.section("PROFIL")
    d.line([("Étudiant en dernière année à SKEMA Business School (Programme Grande École + MSc Corporate Financial "
             "Management), candidat FRM et certifié Bloomberg Market Concepts (BMC). Rigueur d'analyse financière "
             "(VaR, Black-Scholes-Merton, Greeks, fixed income) éprouvée en reporting multi-actifs chez BPCE "
             "Assurances (Bloomberg BQL, Excel/VBA). Auteur de ", REG),
            ("ShockDesk", BLD),
            (", un poste de trading complet en Python : prévisions point-in-time, backtests avec coûts d'exécution, "
             "attribution du P&L par ligne, pricer d'options et structures (butterfly, iron condor, strangles). "
             "Recherche : stage Front Office de 6 mois à partir de janvier 2027 à Paris (vente ou structuration).", REG)])

    d.formation()
    d.experience([
        "Production quotidienne de reportings multi-actifs à forte volumétrie (FX majors, indices actions, "
        "courbes de taux, spreads) alimentant les comités d'investissement.",
        "Construction et exploitation de courbes Bloomberg via BQL (forwards, swaps, taux non standards) "
        "pour éclairer les décisions obligataires.",
        "Automatisation de tâches répétitives sous Excel (XLOOKUP, macros VBA) : accélération significative "
        "du reporting.",
    ])

    d.section("PROJET PHARE — SHOCKDESK")
    d.line([("ShockDesk — Poste de trading & stress-testing (Python · yfinance) |", BLD)])
    d.line([("github.com/Calvin29990/shockdesk · Démo live : shockdesk.onrender.com", BLD)])
    d.bullet([("Un poste de travail complet, inspiré du métier : on publie une vue datée (révisions numérotées, "
               "auditables, scorecard ex-post), on la dimensionne, on la backteste, on l'explique ligne par ligne, "
               "on la corrige par révision.", REG)])
    d.bullet([("Moteur de backtest : slippage et commissions facturés, attribution du P&L par ligne, comparaison "
               "alpha/bêta au benchmark — un backtest sans attribution ne se commente pas.", REG)])
    d.bullet([("Côté produits structurés : pricer Black-Scholes, surface de volatilité, Greeks, catalogue de "
               "structures (butterfly, iron condor, strangles) avec prime nette, points morts, pertes et gains "
               "max ; le lien prévision → structure est explicite.", REG)])
    d.bullet([("Cas pratique « Book choc pétrolier ShockLab » : scénario géopolitique Brent (type détroit d'Ormuz) "
               "sur univers global-macro (Brent, S&P 500, TLT, or, dollar, crédit HY) ; 42 barres yfinance, "
               "21 trades, données réelles ; entrée à la publication du scénario, stop calendaire fixé ex-ante.", REG)])
    d.bullet([("Supports : démo live de 15 minutes, code source (GitHub), cours pratique de 57 pages / 19 modules "
               "rédigé pour le projet — disponible sur demande.", REG)])

    d.section("COMPÉTENCES TECHNIQUES & CERTIFICATIONS")
    d.bullet([("Technique :", BLD),
              (" Python (pandas, scikit-learn), Excel avancé (VBA, XLOOKUP), Bloomberg (BQL), SQL (BigQuery), "
               "JavaScript, R, data visualisation.", REG)])
    d.bullet([("Marchés :", BLD),
              (" pricing de dérivés (BSM), Greeks, surface de volatilité, structures d'options, risque de marché "
               "(VaR), fixed income, FX, stress testing, backtesting.", REG)])
    d.bullet([("Certifications :", BLD),
              (" Bloomberg Market Concepts (BMC — Bloomberg for Education, 2026) ; FRM (candidat, GARP) ; AMF (en "
               "cours) ; Citi Markets Sales & Trading (Forage) ; QuantInsti (Python for Trading ; Options ; ML for "
               "Trading).", REG)])

    d.langues()
    d.line([("Autres projets (CalvinX Market Terminal, pricer Black-Scholes) : détaillés dans le portfolio ci-joint "
             "et sur linkedin.com/in/calvin-minang", REG)], size=8.5, color=GRAY)
    d.save()


if __name__ == "__main__":
    build_general()
    build_shockdesk()
