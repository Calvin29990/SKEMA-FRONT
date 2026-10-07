# -*- coding: utf-8 -*-
"""Lettre recommandée — exposé de la situation 2019-2026, demandes, bordereau, pièces A à L.

Aucune couleur d'accentuation : quatre registres typographiques, un par acteur.
  gras noir   = Agence nationale des bourses du Gabon
  gras gris   = SKEMA Business School
  italique    = Campus France
  italique    = l'État gabonais, les textes qu'il prend
  romain noir = l'étudiant
Les actes sont narrés ; les mentions entre guillemets reproduisent le texte des pièces A à L.
"""
import os
import re
import sys
import tempfile

import pymupdf as fitz

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "outils"))
import md2pdf  # noqa: E402

FD = "/usr/share/fonts/truetype/dejavu/"
SER, SERB = FD + "DejaVuSerif.ttf", FD + "DejaVuSerif-Bold.ttf"
BASE14 = {"i": "tiit", "bi": "tibi"}          # Times italique : réservé aux courtes suites de mots
FONTS = {"r": fitz.Font(fontfile=SER), "b": fitz.Font(fontfile=SERB),
         "i": fitz.Font("tiit"), "bi": fitz.Font("tibi")}

W, H = 595.0, 842.0
ML, MR, MT, MB = 62.0, 52.0, 56.0, 58.0
AVAIL = W - ML - MR
OUT = os.path.join(BASE, "pdf")
PIECES = os.path.join(BASE, "pieces")

NOIR = (0.04, 0.04, 0.06)
GRIS = (0.38, 0.38, 0.40)
# clé de style -> (police, couleur)
STYLE = {"A": ("Fb", NOIR),      # ANBG
         "S": ("Fb", GRIS),      # SKEMA Business School
         "C": ("Fi", NOIR),      # Campus France
         "E": ("Fi", GRIS),      # État gabonais
         "T": ("Fb", NOIR),      # titre de section
         "-": ("Fr", NOIR)}      # récit
BASE14_NAMES = {"Fi": BASE14["i"], "Fbi": BASE14["bi"]}

MOTS = [  # le plus long d'abord ; les noms seuls portent le style
    ("Agence nationale des bourses du Gabon", "A"),
    ("Agence Nationale des Bourses du Gabon", "A"),
    ("Commission technique des bourses", "A"),
    ("Commission technique de l'Agence", "A"),
    ("la Commission technique", "A"),
    ("plateforme de l'Agence", "A"),
    ("la plateforme", "A"),
    ("l'Agence", "A"),
    ("ANBG", "A"),
    ("eBourse", "A"),
    ("SKEMA BUSINESS SCHOOL", "S"),
    ("SKEMA Business School", "S"),
    ("comptabilité de l'établissement", "S"),
    ("comptabilité étudiante", "S"),
    ("comptabilité étudiantes", "S"),
    ("registraire de l'établissement", "S"),
    ("le registraire", "S"),
    ("l'établissement", "S"),
    ("SKEMA", "S"),
    ("Service Financement et Bourses", "C"),
    ("Campus France", "C"),
    ("Chorus Pro", "C"),
    ("le SFO", "C"),
    ("SFO", "C"),
    ("Journal officiel", "E"),
    ("décret n° 0115/PR/MESRIT", "E"),
    ("décret n° 0065/PR/MESRSIT", "E"),
    ("décret 0115/PR/MESRIT", "E"),
    ("décret 0065/PR/MESRSIT", "E"),
    ("État gabonais", "E"),
    ("« ETAT », prénom « GABONAIS »", "E"),
]
RE = re.compile("|".join("(?:%s)" % re.escape(m).replace("\\ ", " ") for m, _ in MOTS), 0)
KEY = dict(MOTS)


class Feuille:
    def __init__(self):
        self.d = fitz.open()
        self.pg = None
        self.new()

    def new(self, header=False):
        self.pg = self.d.new_page(width=W, height=H)
        self.pg.insert_font(fontname="Fr", fontfile=SER)
        self.pg.insert_font(fontname="Fb", fontfile=SERB)
        self.y = MT

    def save(self, path):
        try:
            self.d.subset_fonts()
        except Exception:
            pass
        self.d.save(path, deflate=True, garbage=4, clean=True)


def style(texte):
    """Découpe le récit en suites (texte, clé de style) : les noms d'acteurs sont stylés."""
    out, last = [], 0
    for m in RE.finditer(texte):
        if m.start() > last:
            out.append((texte[last:m.start()], "-"))
        out.append((m.group(0), KEY[m.group(0)]))
        last = m.end()
    if last < len(texte):
        out.append((texte[last:], "-"))
    return out


def para(f, texte, size=10.6, lead=15.2, space=7.5, width=None, justifier=True, style_runs=None):
    """Paragraphe : la ponctuation reste collée au mot, les noms d'acteurs gardent leur registre."""
    width = width or AVAIL
    ws = FONTS["r"].text_length(" ", size)
    runs = style_runs if style_runs is not None else style(texte)
    mots = []
    for txt, key in runs:
        fname, col = STYLE[key]
        fo = FONTS["b"] if fname == "Fb" else (FONTS["i"] if fname == "Fi" else FONTS["r"])
        for mot in txt.split():
            if mots and mot[0] in ",.;:!?»)" and mot not in (":", ";", "!", "?", "»", ")") \
                    and mots[-1][0][-1] not in "(«":
                prev = mots[-1][0] + mot
                mots[-1][0] = prev
                mots[-1][3] = mots[-1][4].text_length(prev, size)
                continue
            for part in _coupe(mot, size, width, fo):
                mots.append([part, fname, col, fo.text_length(part, size), fo])
    lignes, cur, cw = [], [], 0.0
    for m in mots:
        if cur and cw + m[3] > width:
            lignes.append((cur, cw))
            cur, cw = [m], m[3]
        else:
            cur.append(m)
            cw += m[3] + ws
    if cur:
        lignes.append((cur, cw))
    for i, (line, lw) in enumerate(lignes):
        if f.y + lead > H - MB:
            f.new()
        y = f.y + size * 0.83
        ecart = 0.0
        if justifier and i < len(lignes) - 1 and len(line) > 1:
            ecart = (width - lw) / (len(line) - 1)
        x = ML
        for mot, fname, col, wd, _fo in line:
            nom = BASE14_NAMES.get(fname, fname)
            if fname in BASE14_NAMES:
                f.pg.insert_text((x, y), mot, fontname=nom, fontsize=size, color=col)
            else:
                f.pg.insert_text((x, y), mot, fontname=fname, fontsize=size, color=col)
            x += wd + ws + ecart
        f.y += lead
    f.y += space


def _coupe(mot, size, width, fo):
    out = []
    while fo.text_length(mot, size) > width and len(mot) > 3:
        k = len(mot)
        while k > 2 and fo.text_length(mot[:k], size) > width:
            k -= 1
        out.append(mot[:k])
        mot = mot[k:]
    out.append(mot)
    return out


def ligne(f, texte, size=10.6, gras=False, col=NOIR, x=None, droite=False, lead=None):
    fo = FONTS["b"] if gras else FONTS["r"]
    xx = (W - MR - fo.text_length(texte, size)) if droite else (x if x is not None else ML)
    f.pg.insert_text((xx, f.y + size * 0.83), texte, fontname="Fb" if gras else "Fr",
                     fontsize=size, color=col)
    f.y += lead if lead else size + 4.0


def _lignes(texte, size, width, fo=None):
    fo = fo or FONTS["r"]
    ws = fo.text_length(" ", size)
    out, cur, cw = [], [], 0.0
    for mot in texte.split():
        w = fo.text_length(mot, size)
        if cur and cw + w > width:
            out.append(" ".join(cur))
            cur, cw = [mot], w
        else:
            cur.append(mot)
            cw += w + ws
    if cur:
        out.append(" ".join(cur))
    return out


# ------------------------------------------------------------------- en-tête
EXPED = ["Né le 2 mai 2002 à Libreville (Gabon)",
         "Étudiant — Programme Grande École, 2ᵉ année, n° 0305476",
         "Dossier ANBG / Campus France n° 110584Z"]

DEST = [("À la Direction générale de", True),
        ("l'Agence nationale des bourses du Gabon", False),
        ("et à la Commission technique des bourses", False),
        ("", False),
        ("À la Direction du Service Financement", True),
        ("et Bourses, Campus France,", False),
        ("", False),
        ("À la Direction générale de", True),
        ("SKEMA Business School,", False),
        ("service de la comptabilité étudiante", False),
        ("", False),
        ("Copie pour information à la Direction des", False),
        ("études et au service des relations", False),
        ("avec les entreprises", False)]


def entete(f):
    ligne(f, "Calvin B. MINANG", 12.0, gras=True, lead=16.0)
    for t in EXPED:
        ligne(f, t, 9.6, lead=12.6)
    f.y += 20
    x = 316.0
    for txt, tete in DEST:
        if not txt:
            f.y += 6
            continue
        fo = FONTS["b"] if tete else FONTS["r"]
        f.pg.insert_text((x, f.y + 9.0 * 0.83), txt, fontname="Fb" if tete else "Fr",
                         fontsize=9.0, color=NOIR)
        f.y += 11.8
    f.y += 16
    ligne(f, "Le 8 octobre 2026", 10.4, droite=True)
    f.y += 16
    para(f, "Lettre recommandée avec accusé de réception", size=10.5, lead=14.2, space=1.5,
         justifier=False, style_runs=[("Lettre recommandée avec accusé de réception", "T")])
    para(f, "Objet : Bourse d'État, prise en charge des frais de scolarité et facturation — "
            "exposé de la situation et demandes.", size=10.5, lead=14.2, space=1.5,
         justifier=False, style_runs=[("Objet : ", "T"),
                                      ("Bourse d'État, prise en charge des frais de scolarité et "
                                       "facturation — exposé de la situation et demandes.", "T")])
    para(f, "Un seul exemplaire par destinataire. Pièces jointes : douze, cotées A à L, bordereau "
            "en fin de lettre.", size=10.5, lead=14.2, space=1.5, justifier=False)
    f.pg.draw_line(fitz.Point(ML, f.y + 1), fitz.Point(W - MR, f.y + 1), width=0.6, color=NOIR)
    f.y += 17


# ---------------------------------------------------------------------- récit
RIT = [
    "Je me permets de vous adresser en un seul courrier l'exposé de ma situation et les demandes "
    "qui en découlent, les trois services étant intéressés aux mêmes faits. Boursier de l'État "
    "gabonais depuis la session 2019-2020, inscrit au Programme Grande École depuis le 1er "
    "septembre 2022, je vois aujourd'hui la scolarité de l'année 2025/2026 réclamée pour 14 840,00 "
    "€ par mise en demeure du 7 octobre 2026, alors que la prise en charge de mes frais de scolarité "
    "a été engagée par l'organisme payeur sur les deux années précédentes et que la décision qui m'a "
    "retiré la bourse vise un texte abrogé le lendemain de sa signature. Les faits rapportés ci-"
    "dessous sont ceux qu'enregistrent vos documents respectifs ; les mentions entre guillemets en "
    "sont tirées textuellement, et les pièces A à L les accompagnent.",

    "C'est par la bourse nationale que j'ai pu poursuivre mes études. Admis en classes "
    "préparatoires, filière ECE, au Groupe Scolaire La Résidence de Casablanca, j'obtiens la bourse "
    "d'État au titre de la session 2019-2020, dossier eBourse WEXQTG. Le 1er février 2021, la "
    "Commission technique de l'Agence maintient cette bourse en catégorie C, et le 4 février 2021 "
    "délivre l'attestation de maintien de paiement n° 100326-21-MAINTIEN : « Classes Préparatoires "
    "2 au/en MAROC / CASABLANCA », « valable jusqu'au 30/09/2021 », « montant mensuel [...] 165 000 "
    "FCFA », avec la mention que la reconduction en N+1 est conditionnée à la présentation des "
    "résultats annuels. Le 2 novembre 2021, l'attestation d'attribution n° 100057-22-ACCORD accorde "
    "la bourse pour l'année 2021/2022, établissement IPESUP, France/Paris, « pour une durée : 1 année(s), du "
    "01/09/2021 au 31/08/2022 » ; les sessions suivantes seront portées à deux années (pièces B, C, "
    "E).",

    "Admis au Programme Grande École par le concours BCE sous le numéro de candidat 21446, je "
    "m'inscris en L3 du cycle pour la rentrée de septembre 2022, campus de Paris, en préparant la "
    "sortie du cycle dans les délais que le régime de la bourse autorise. Le 25 août 2022, "
    "l'établissement écrit : « Concernant la facturation, je transfère votre mail à la comptabilité "
    "étudiante. » Le 26 août 2022, le dossier d'inscription n° 2733904447 comporte le formulaire "
    "d'acte de cautionnement enregistré au nom de « ETAT », prénom « GABONAIS », 28 rue de la Grange "
    "aux Belles, 75010 Paris, avec le courriel de l'Agence comme adresse de notification, pour une "
    "limite de « quarante six mille euros (46 000 €) » et une durée de « soixante (60) mois ». Ce "
    "contrat de Fall 2022 est le seul contrat d'inscription du cycle ; son article 4.4 prévoit son "
    "rallongement en cas de prolongation de scolarité (pièce J).",

    "La règle de facturation a été posée par écrit le 24 janvier 2023 : « Nous vous invitons à "
    "établir une facture à l'ordre de campus France et à la déposer sur Chorus Pro », avec cette "
    "précision « Dans l'hypothèse où l'étudiant aurait versé un acompte, merci de bien vouloir le "
    "faire apparaître clairement », et cette question « pouvez-vous me confirmer que l'étudiant peut "
    "de nouveau avoir accès aux cours ainsi qu'aux supports pédagogiques ? ». Le même jour, "
    "Campus France émet le bon de commande n° 677745 sur le dossier 110584Z, objet « FRAIS DE "
    "FORMATION 22/23 », fournisseur SKEMA BUSINESS SCHOOL n° 35025, pour 15 000,00 € ; la "
    "comptabilité de l'établissement en accuse réception le 25 janvier 2023 à 09:43 (pièces G, J). "
    "Les montants qui me sont réclamés depuis lors s'inscrivent dans ce cadre : la facture est "
    "établie à l'ordre de Campus France et déposée sur Chorus Pro, l'organisme payeur demeurant "
    "seul débiteur de la prise en charge.",

    "L'année 2023 a été marquée par la délibération du jury de l'établissement en juillet, qui "
    "n'a pas validé les semestres de L3 — un seul échec dans le cycle, à ce jour — puis par "
    "l'acceptation de la césure, le 27 octobre 2023 : « Votre demande pour effectuer la césure à "
    "partir de janvier 2024 a été acceptée. Je viens de mettre à jour votre dossier. » Le 4 janvier "
    "2024, l'établissement a signé la convention de stage « 23/24-PGE FI L3 RD Paris semestre Fall » "
    "avec BPCE VIE : « Le stage se déroulera du 08/01/2024 au 05/07/2024 », cinq jours ouvrés par "
    "semaine. Le 14 mai 2024, le registraire certifie le parcours : « 2023/2024 L3/M1 Paris Fall 23 / "
    "Césure Spring 24 ; 2024/2025 M1 Césure Fall 24 / Raleigh Spring 25 ; 2025/2026 PGE M2 » "
    "(pièces F, H). L'attestation de stage correspondante m'a été délivrée par l'entreprise.",

    "La prise en charge n'a pas été interrompue pour autant sur cette année de césure : le 6 mai "
    "2024, Campus France émet le bon de commande n° 721622, dossier 110584Z, objet « POUR LE COMPTE "
    "DE L'ANBG FRAIS FORMATION 2023 2024 », pour 16 000,00 € (pièce G). Le 25 septembre 2024 à "
    "16:37, la plateforme de l'Agence enregistre pourtant la suppression de la bourse au motif « abs "
    "de releve de notes / perception de la bourse », alors que l'année en cause était, depuis le 27 "
    "octobre 2023, une année de césure certifiée par l'établissement, sans relevé de notes à "
    "produire (pièces E, F).",

    "Les échéances ont suivi leur cours du côté de l'établissement : le 14 novembre 2024, rappel de "
    "la première échéance des droits scolaires 2024/2025 pour 12 000,00 € ; le 15 janvier 2025, "
    "facture n° 22223502 intitulée « Master 2 » pour 15 000,00 € ; le 20 février 2025, une pièce "
    "comptable pour 4 000,00 € ; le 17 décembre 2024, certificat de scolarité pour 2024/2025 "
    "(pièces F, I). Le 17 février 2025, la pièce que j'avais déposée est validée par l'Agence à "
    "11:06, et l'irrecevabilité du recours est enregistrée à 11:11 sous le motif « PARCOURS "
    "INSOUTENABLE (ARTICLE 4 DECRET 065) » : cinq minutes séparent la validation de la décision qui "
    "la rendait nécessaire. Le lendemain, 21 février 2025, le décret n° 0115/PR/MESRIT (Journal "
    "officiel n° 56 bis du 26 février 2025) dispose en son article 4 qu'« abroge[t] toutes "
    "dispositions antérieures contraires, notamment celles du décret n° 0065/PR/MESRSIT du 12 "
    "février 2024 ». Le 10 novembre 2025 à 15:47, la Commission technique émet l'avis défavorable "
    "référence CA24B3 sur la demande, en m'invitant à la renouveler ; le 9 décembre 2025, soit "
    "vingt-neuf jours après, l'établissement certifie mon assiduité (pièces E, F).",

    "S'agissant du dossier de facturation, la facture n° 1281253 a été rejetée le 25 septembre 2025 "
    "à 12:15 par le Service Financement et Bourses, motif « Certificat de scolarité manquant ou non "
    "conforme », avec injonction de « remettre le « Bon à payer » ». Le 6 octobre 2025 à 15:19, il "
    "est demandé « le relevé de notes de l'année 2023-2024 ou un certificat de scolarité daté d'après "
    "le 1er septembre 2023 » ; le 29 octobre 2025 à 12:34, le service écarte le document « du 26/07 "
    "non conforme » ; le 6 novembre 2025 à 12:01, je réponds en produisant trois attestations de "
    "l'établissement, dont l'attestation du registraire du 14 mai 2024 établissant que l'année "
    "2023/2024 était une année de césure. Aucune observation n'a suivi ce message, ni depuis (pièce "
    "D).",

    "L'année 2025/2026 a été facturée et réclamée sans que la prise en charge fût remise en cause "
    "par écrit : le 30 septembre 2026, la comptabilité de l'établissement porte la somme à 7 500,00 "
    "€ ; le 5 octobre 2026, un document comptable la porte à 14 840,00 € ; le 7 octobre 2026 à "
    "15:04, la mise en demeure n° 2026-SK.D-0002 réclame ce solde « au titre de l'année 2025/2026 » "
    "avec paiement sous dix jours, en précisant que « l'absence ou la cessation de prise en charge "
    "par un organisme tiers ne vous libère pas », sous menace de procédure et de cessation définitive "
    "de scolarité. Le même jour à 21:06, la plateforme de l'Agence affiche, pour la session 2025-2026 "
    "et la référence externe 110584Z : « DÉCISION : AVIS DÉFAVORABLE », « VOUS ÊTES NON BOURSIER », "
    "pays de la demande France, diplôme Master, arborescence CA24B3, 1LMK24, 2E4C0B, LDPMRC, PNPXWG, "
    "4E0O00, WEXQTG (pièces E, I).",

    "La fin du cycle est prévue en décembre 2026 et le titre de séjour arrive à échéance le 30 "
    "janvier 2027, son renouvellement étant subordonné au certificat de scolarité du semestre 5. Je "
    "n'ai sollicité aucune allocation directe : seule est en cause la prise en charge des frais de "
    "scolarité, déjà engagée par l'organisme payeur pour 2022/2023 et pour 2023/2024 aux termes des "
    "deux bons de commande. Les montants successivement réclamés pour la même période d'études — 12 "
    "000,00 €, puis 4 000,00 €, puis 15 000,00 €, puis 7 500,00 €, puis 14 840,00 € — ne sont "
    "assortis d'aucune pièce de calcul, et l'écart avec le contrat de Fall 2022, de 46 000,00 € pour "
    "une durée pouvant atteindre soixante mois, n'est établi par aucune pièce.",
]

DEMANDES = [
    ("À l'Agence nationale des bourses du Gabon", "A", [
        "1° la transmission du présent dossier à la Commission technique et son réexamen au titre "
        "des étudiants dont le cycle est engagé depuis le 1er septembre 2022, le retour à « coûts "
        "soutenables » portant sur les nouvelles attributions ;",
        "2° la communication de la pièce, de la date et de la signature qui fondent l'avis "
        "défavorable du 10 novembre 2025, ainsi que le détail du calcul des frais de scolarité pris "
        "en charge pour 2024/2025 et pour 2025/2026 ;",
        "3° la confirmation écrite, à l'établissement et au Service Financement et Bourses, du "
        "maintien de la prise en charge des frais de scolarité pour 2025/2026 ;",
        "4° la copie certifiée au guichet de la décision portant que la bourse du cycle Master a été "
        "attribuée pour deux années, la plateforme portant « 1 année(s) » pour 2021 et « deux "
        "années » pour 2023 ;",
        "5° la mention au dossier du recours gracieux ci-joint, enregistré en main propre contre "
        "accusé (pièces A, K, L)."]),
    ("Au Service Financement et Bourses de Campus France", "C", [
        "1° l'état de la facture n° 1281253 dans Chorus Pro à la date de votre réponse et, si elle "
        "doit être représentée, la désignation de la pièce exacte attendue : les trois attestations "
        "produites le 6 novembre 2025 n'ont appelé aucune observation ;",
        "2° l'émission du bon de commande 2024/2025, les années 2022/2023 et 2023/2024 ayant donné "
        "lieu aux bons n° 677745 et n° 721622, objet « POUR LE COMPTE DE L'ANBG FRAIS FORMATION 2023 "
        "2024 » ;",
        "3° une attestation adressée à l'établissement rappelant la règle posée le 24 janvier 2023, "
        "aux termes de laquelle la facture est établie à votre ordre et déposée sur Chorus Pro, et "
        "l'état d'avancement des paiements au profit de SKEMA Business School pour le compte du "
        "dossier 110584Z ;",
        "4° que les demandes de pièces adressées à l'établissement le soient simultanément, et non "
        "plus après rejet."]),
    ("À SKEMA Business School", "S", [
        "1° la communication de la pièce qui fonde 14 840,00 € au titre de l'année 2025/2026, et le "
        "rapprochement avec le contrat d'inscription de Fall 2022, de 46 000,00 € pour une durée "
        "pouvant atteindre soixante mois ;",
        "2° la suspension des effets de la mise en demeure — cessation de scolarité et rétention des "
        "documents — pendant l'examen du recours par l'Agence ;",
        "3° à défaut de réponse avant le 19 octobre 2026, date d'expiration du délai de dix jours, "
        "la fixation d'un échéancier de 300,00 € par mois à compter de janvier 2027, sans "
        "reconnaissance de dette ;",
        "4° la délivrance sans délai du certificat de scolarité de l'année 2025/2026, requis pour le "
        "renouvellement du titre de séjour."]),
]


def corps(f):
    base = f.y + 10.6 * 0.83
    f.pg.insert_text((ML, base), "Madame,", fontname="Fr", fontsize=10.6)
    f.pg.insert_text((W - MR - FONTS["r"].text_length("Monsieur,", 10.6), base), "Monsieur,",
                     fontname="Fr", fontsize=10.6)
    f.y += 10.6 + 10.0
    for texte in RIT:
        para(f, texte)
    f.y += 2
    para(f, "Mes demandes.", size=10.6, style_runs=[("Mes demandes.", "T")], space=6.0)
    for titre, key, items in DEMANDES:
        para(f, "", style_runs=style(titre) + [(", je demande :", "-")], space=3.0,
             justifier=False)
        for it in items:
            para(f, it, size=10.2, lead=14.4, space=3.0, width=AVAIL - 20)
            f.y -= 0.5
        f.y += 3.0
    para(f, "Dans l'attente de vos réponses, je vous prie d'agréer, Madame, Monsieur, l'expression "
            "de mes considérations distinguées.", size=10.6)
    f.y += 24
    ligne(f, "Calvin B. MINANG", 10.6, gras=True, droite=True, lead=13.5)
    ligne(f, "né le 2 mai 2002 à Libreville — n° étudiant 0305476", 9.0, droite=True, lead=11.5,
          col=GRIS)


# ------------------------------------------------------------------ bordereau
PIECES_INDEX = [
    ("A", "08/10/2026", "Étudiant", "Recours gracieux contre les décisions des 25/09/2024 et "
     "10/11/2025, avec procuration et accusé de remise", "A"),
    ("B", "04/02/2021", "ANBG", "Attestation de maintien de paiement n° 100326-21-MAINTIEN", "A"),
    ("C", "02/11/2021", "ANBG", "Attestation d'attribution n° 100057-22-ACCORD", "A"),
    ("D", "25/09 → 06/11/2025", "Campus France", "Filet de courriels « TR: Facture rejetée SFO "
     "N° 1281253 », quatre messages", "C"),
    ("E", "2024 → 2026", "ANBG", "Notifications et validations de la plateforme eBourse, "
     "horodatées — à imprimer depuis l'espace étudiant", "A"),
    ("F", "2024 et 2025", "SKEMA", "Attestation du registraire du 14/05/2024 ; attestation "
     "d'assiduité du 09/12/2025", "S"),
    ("G", "2023 et 2024", "Campus France", "Bons de commande n° 677745 et n° 721622", "C"),
    ("H", "04/01/2024", "SKEMA", "Convention de stage SKEMA / BPCE, 08/01/2024 → 05/07/2024", "S"),
    ("I", "2024 et 2026", "SKEMA", "Rappel de droits scolaires 2024/2025 ; mise en demeure "
     "2026-SK.D-0002", "S"),
    ("J", "2022 → 2025", "SKEMA", "Contrat d'inscription Fall 2022, dossier d'inscription et acte "
     "de cautionnement", "S"),
    ("K", "08/10/2026", "Étudiant", "Procuration donnée au porteur du dossier", "-"),
    ("L", "08/10/2026", "Étudiant", "Accusé de remise du recours, deux exemplaires", "-"),
]

ANNEX = {
    "A": ([], "recours"),
    "B": ([("attestation-anbg-maintien-2021.pdf", None)], None),
    "C": ([("attestation-anbg-attribution-2021-2022.pdf", None)], None),
    "D": ([("contradiction-campus-france.pdf", None)], None),
    "E": ([], "à produire"),
    "F": ([("attestation-PGE.pdf", None), ("attestation-assiduite-09-12-2025.pdf", None)], None),
    "G": ([("bon-de-commande-M1.pdf", None)], None),
    "H": ([("convention-stage-bpce-2024.pdf", [0, 1, 2])], None),
    "I": ([("relance-skema-M1.pdf", [0]), ("mise-en-demeure.pdf", [0])], None),
    "J": ([("contrat-signé.pdf", None), ("dossier-campus-caution.pdf", [0, 1, 2])], None),
    "K": ([], "procuration"),
    "L": ([], "recepisse"),
}

LIGNE_BORD = []


def bordereau(f):
    f.new()
    f.pg.draw_line(fitz.Point(ML, MT + 1.0), fitz.Point(W - MR, MT + 1.0), width=0.6, color=NOIR)
    f.y = MT + 14
    ligne(f, "Bordereau des pièces jointes", 11.5, gras=True, lead=16.0)
    for ln in _lignes("Les pièces sont reproduites dans l'ordre des lettres, sans annotation ; les "
                      "mentions entre guillemets de la lettre en sont tirées textuellement.", 9.0,
                      AVAIL):
        ligne(f, ln, 9.0, lead=11.6, col=GRIS)
    f.y += 13
    xs = {"cote": ML, "date": ML + 34, "emet": ML + 128, "pag": ML + 222, "obj": ML + 268}
    for txt, x in (("Cote", xs["cote"]), ("Date", xs["date"]), ("Émetteur", xs["emet"]),
                   ("Pages", xs["pag"]), ("Objet", xs["obj"])):
        f.pg.insert_text((x, f.y), txt, fontname="Fb", fontsize=8.2, color=GRIS)
    f.pg.draw_line(fitz.Point(ML, f.y + 5), fitz.Point(W - MR, f.y + 5), width=0.5, color=NOIR)
    f.y += 15
    del LIGNE_BORD[:]
    wobj = W - MR - xs["obj"]
    for cote, date, emet, objet, key in PIECES_INDEX:
        ln_obj = _lignes(objet, 8.6, wobj)
        hh = max(1, len(ln_obj)) * 10.6 + 4.6
        if f.y + hh > H - MB:
            f.new()
        base = f.y + 8.6 * 0.83
        f.pg.insert_text((xs["cote"], base), cote, fontname="Fb", fontsize=9.4, color=NOIR)
        f.pg.insert_text((xs["date"], base), date, fontname="Fr", fontsize=8.6)
        f.pg.insert_text((xs["emet"], base), emet, fontname="Fr", fontsize=8.6)
        for i, ln in enumerate(ln_obj):
            f.pg.insert_text((xs["obj"], base + i * 10.6), ln, fontname="Fr", fontsize=8.6)
        LIGNE_BORD.append([cote, f.d.page_count - 1, base])
        f.y += hh
        f.pg.draw_line(fitz.Point(ML, f.y - 3.0), fitz.Point(W - MR, f.y - 3.0), width=0.25,
                       color=(0.62, 0.62, 0.65))
    return xs["pag"]


# ---------------------------------------------------------------------- annexes
def annexes(f, xcol):
    rtmp = os.path.join(tempfile.gettempdir(), "actes-lettre.pdf")
    src = open(os.path.join(BASE, "PARENTS-ANBG", "RECOURS-GRACIEUX-ANBG.md"), encoding="utf-8").read()
    a0 = src.index("# 1. RECOURS GRACIEUX")
    a1 = src.index("# 4. CHEMISE") if "# 4. CHEMISE" in src else len(src)
    md2pdf.render(src[a0:a1].rstrip() + "\n", rtmp, "")
    actes = fitz.open(rtmp)
    ix = {}
    for k in ("1. RECOURS GRACIEUX", "2. PROCURATION", "3. ACCUSÉ DE REMISE"):
        j = next((i for i, pg in enumerate(actes) if k in pg.get_text()), None)
        if j is None:
            print("  ! section introuvable dans le recours :", k)
            j = 0
        ix[k] = j
    ordre = [c for c, _p, _y in LIGNE_BORD]
    debut = {}
    for cote in ordre:
        debut[cote] = f.d.page_count + 1
        fichiers, spec = ANNEX[cote]
        if spec == "à produire":
            continue
        if spec:
            a, b = {"recours": (ix["1. RECOURS GRACIEUX"], ix["2. PROCURATION"]),
                    "procuration": (ix["2. PROCURATION"], ix["3. ACCUSÉ DE REMISE"]),
                    "recepisse": (ix["3. ACCUSÉ DE REMISE"], len(actes))}[spec]
            f.d.insert_pdf(actes, from_page=a, to_page=max(a, b - 1))
            continue
        for fn, keep in fichiers:
            path = os.path.join(PIECES, fn)
            if not os.path.exists(path):
                print("  ! pièce absente :", fn)
                continue
            s = fitz.open(path)
            if keep:
                s.select([i for i in keep if i < s.page_count])
            f.d.insert_pdf(s)
            s.close()
    while f.d and not f.d[-1].get_text().strip() and not f.d[-1].get_images():
        f.d.delete_page(-1)
    for k, (cote, pgn, y0) in enumerate(LIGNE_BORD):
        a = debut[cote]
        b = f.d.page_count if k == len(LIGNE_BORD) - 1 else debut[LIGNE_BORD[k + 1][0]] - 1
        if b < a:
            txt = "non jointe"
        elif b == a:
            txt = f"p. {a}"
        else:
            txt = f"p. {a} à {b}"
        f.d[pgn].insert_text((xcol, y0), txt, fontname="Fr", fontsize=8.6, color=NOIR)
    actes.close()
    os.remove(rtmp)


def main():
    os.makedirs(OUT, exist_ok=True)
    f = Feuille()
    entete(f)
    corps(f)
    xcol = bordereau(f)
    annexes(f, xcol)
    dest = os.path.join(OUT, "HISTORIQUE-DOCUMENTE-2019-2026-MINANG.pdf")
    f.save(dest)
    print(os.path.basename(dest), "—", f.d.page_count, "pages,",
          round(os.path.getsize(dest) / 1024), "Ko")
    f.d.close()


if __name__ == "__main__":
    main()
