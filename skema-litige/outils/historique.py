#!/usr/bin/env python3
"""historique.py —Historique documenté 2019-2026, style note de synthèse.

Une seule table froide, triée par date, une couleur par acteur (ANBG, Campus France,
SKEMA Business School, étudiant, État gabonais). Aucune analyse, aucune consigne :
les faits, leurs dates, leurs auteurs, la pièce qui les établit.

  python3 skema-litige/outils/historique.py
  -> skema-litige/pdf/HISTORIQUE-DOCUMENTE-2019-2026-MINANG.pdf
"""
import os
import re
import sys
import tempfile

import pymupdf as fitz

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, ".."))
PIECES = os.path.join(BASE, "pieces")
OUT = os.path.join(BASE, "pdf")
sys.path.insert(0, HERE)
import md2pdf  # noqa: E402
from md2pdf import FONTS  # noqa: E402

FF = md2pdf.FFILE
W, H = fitz.paper_size("a4")
ML, MR, MT, MB = 46.0, 46.0, 46.0, 44.0
AVAIL = W - ML - MR

C = {
    "ANBG": (0.11, 0.40, 0.28),
    "CF": (0.13, 0.30, 0.50),
    "SKEMA": (0.68, 0.38, 0.09),
    "ÉTUD": (0.06, 0.06, 0.08),
    "ÉTAT": (0.34, 0.36, 0.42),
}
NOM = {"ANBG": "ANBG", "CF": "Campus France", "SKEMA": "SKEMA", "ÉTUD": "Étudiant", "ÉTAT": "État gabonais"}
GAP = 6.0
COLS = [("Date", 58.0), ("Acteur", 74.0), ("Fait établi par la pièce", None), ("Pièce", 30.0)]
FIXES = sum(c for c in [x[1] for x in COLS] if c)
COLS[2] = ("Fait établi par la pièce", AVAIL - FIXES - 3 * GAP)

# (date, acteur, fait, pièce) — une ligne par fait, triée par date.
R = [
    ("ANNEE 2019-2021 — classes préparatoires, Casablanca (Maroc)",),
    ("2019-2020", "ANBG", "Attribution de la bourse nationale, session 2019-2020, dossier eBourse WEXQTG. Filière ECE, Groupe Scolaire La Résidence, Casablanca.", "E"),
    ("01/02/2021", "ANBG", "Commission Technique : maintien de la bourse nationale, catégorie C.", "B"),
    ("04/02/2021", "ANBG", "Attestation de maintien de paiement n° 100326-21-MAINTIEN : « Classes Préparatoires 2 au/en MAROC / CASABLANCA », « valable jusqu'au 30/09/2021 », « montant mensuel […] 165 000 FCFA ». Mention : la reconduction N+1 est conditionnée à la présentation des résultats annuels et de l'inscription sur la plateforme eBourse.", "B"),
    ("19/03/2021", "ÉTUD", "« Ma bourse n'a malheureusement toujours pas été renouvelée depuis septembre (bien que j'aie reçu l'attestation de maintien de bourse le mois dernier sur mon compte E-bourse). »", "—"),
    ("02/11/2021", "ANBG", "Attestation d'attribution n° 100057-22-ACCORD : année préparatoire CPE, établissement IPESUP, France/Paris, « pour une durée : 1 année(s), du 01/09/2021 au 31/08/2022 ».", "C"),

    ("ANNEE 2022 — entrée au Programme Grande École, caution enregistrée",),
    ("2022", "SKEMA", "Admission au Programme Grande École par le concours BCE, n° de candidat 21446.", "J"),
    ("18/08/2022", "ÉTUD", "Notification à l'établissement : le garant financier est l'État gabonais, la scolarité devant être prise en charge via l'ANBG et Campus France.", "J"),
    ("25/08/2022", "SKEMA", "Attestation de résultats d'admissibilité et d'admission BCE 2022. Le même jour : « Concernant la facturation, je transfère votre mail à la comptabilité étudiante. »", "J"),
    ("26/08/2022", "SKEMA", "Attestation des frais de scolarité 2022/2023, PGE L3, émise par la comptabilité étudiants (09:53).", "J"),
    ("26/08/2022", "SKEMA", "Dossier d'inscription n° 2733904447, formulaire d'acte de cautionnement : caution enregistrée sous le nom « ETAT », prénom « GABONAIS », adresse « 28 rue de la Grange aux Belles 75010 », courriel « anbg.boursiers@campusfrance.org », limite « quarante six mille euros (46 000 €) », durée « soixante (60) mois ».", "J"),
    ("01/09/2022", "SKEMA", "Entrée en PGE L3, rentrée Fall 2022, campus de Paris.", "J"),
    ("02/11/2022", "SKEMA", "La comptabilité demande le numéro de dossier et le bon de commande ; transmission immédiate du n° 110584Z.", "J"),

    ("ANNEE 2023 — premier bon de commande, règle de facturation posée par écrit",),
    ("10/01/2023 12:30", "ÉTUD", "« 110584Z - Bon de commande » : « Voici le devis 2022-2023 demandé », à l'attention de la boîte ANBG de Campus France.", "J"),
    ("24/01/2023 17:51", "CF", "Règle appliquée au dossier, importance haute : « Nous vous invitons à établir une facture à l'ordre de campus France et à la déposer sur Chorus Pro » ; « Dans l'hypothèse où l'étudiant aurait versé un acompte, merci de bien vouloir le faire apparaître clairement » ; « pouvez-vous me confirmer que l'étudiant peut de nouveau avoir accès aux cours ainsi qu'aux supports pédagogiques ? »", "J"),
    ("24/01/2023", "CF", "Bon de commande n° 677745 : dossier 110584Z, « FRAIS DE FORMATION 22/23 », fournisseur SKEMA BUSINESS SCHOOL n° 35025, 15 000,00 €, signé par le responsable du service Afrique.", "G"),
    ("25/01/2023 09:43", "SKEMA", "Accusé de réception du bon de commande par la comptabilité étudiants.", "J"),
    ("27/10/2023", "SKEMA", "« Votre demande pour effectuer la césure à partir de janvier 2024 a été acceptée. Je viens de mettre à jour votre dossier. »", "—"),
    ("17/10/2023", "SKEMA", "Certificat d'anglais ICIMS, score 67/100, requis pour la délivrance du diplôme ; validité jusqu'au 16/10/2025.", "—"),
    ("juil. 2023", "SKEMA", "Délibération du jury pour l'année 2022/2023 : semestres non validés en L3.", "—"),
    ("06/09/2023", "ANBG", "Attestation d'attribution de bourse MASTER, établissement SKEMA Business School, durée deux années, prise en charge du 01/09/2023 au 31/08/2025, avec prise en charge des frais de scolarité par l'État gabonais. La copie détenue par l'étudiant est dégradée.", "—"),

    ("ANNEE 2024 — césure en entreprise, deuxième bon de commande, suppression du dossier 1LMK24",),
    ("08/01/2024", "ÉTUD", "Signalement aux services administratifs et financiers de l'école : « Campus France ne réglera pas ma scolarité au-delà de 2025 quels que soient mes résultats. »", "—"),
    ("08/01/2024", "SKEMA", "« Calvin sera en expérience professionnelle ce semestre et commencera son année de M1 en septembre 2024. »", "—"),
    ("15/01/2024", "SKEMA", "« Je vous confirme par la présente que votre césure pour l'année 2024 a bien été acceptée. »", "—"),
    ("04/01/2024", "SKEMA", "Convention de stage « 23/24-PGE FI L3 RD Paris semestre Fall », établie entre SKEMA Business School (délégation de signature de la directrice générale) et BPCE VIE, 7 promenade Germaine Sablon, 75013 Paris : « Le stage se déroulera du 08/01/2024 au 05/07/2024 », cinq jours ouvrés par semaine. La convention met à la charge de l'entreprise la délivrance d'une attestation de stage reprenant les dates de la mission.", "H"),
    ("11/03/2024", "ÉTUD", "Courriel à l'Agence : « Urgence bon de commande contentieux avec SKEMA ».", "—"),
    ("06/05/2024", "CF", "Bon de commande n° 721622 : dossier 110584Z, fournisseur 35025 SKEMA Sophia Antipolis, ligne « POUR LE COMPTE DE L'ANBG FRAIS FORMATION 2023 2024 », 16 000,00 €, signé par le responsable Afrique ; facture à l'ordre de Campus France, dépôt Chorus Pro.", "G"),
    ("14/05/2024", "SKEMA", "Attestation du registraire : 2023/2024 PGE L3/M1, « Campus de Paris en Fall 23 (L3) / Césure en Spring 24 » ; 2024/2025 M1, « Césure Fall 24 / Raleigh Spring 25 » ; 2025/2026 PGE M2.", "F"),
    ("25/09/2024 16:37", "ANBG", "Décision du 1LMK24 : « suppression de votre bourse pour le motif suivant : abs de releve de notes / perception de la bourse ».", "E"),
    ("14/11/2024 12:17", "SKEMA", "« Rappel 1ère échéance – PGE M1 – Droits scolaires 2024/2025 », n° étudiant 22223500 : « sauf erreur, omission, cause légitime de votre part, cette somme n'a pas été enregistrée à ce jour […] somme de 12 000 € ».", "I"),
    ("17/12/2024", "SKEMA", "Certificat de scolarité 2024/2025, programme « PROGRAMME GRANDE ÉCOLE - M1 » : « Fall Semester : Césure », « Spring Semester : Campus Grand Paris (France) ».", "F"),

    ("ANNEE 2025 — relances de l'école, rejet du recours ANBG, facture de l'école rejetée par le payeur",),
    ("15/01/2025", "SKEMA", "Facture n° 22223502 : « Frais de scolarité année académique 2024/2025 », 15 000,00 €, intitulé « Programme Grande École Master 2 ». Le document n'est pas établi à l'ordre de Campus France.", "J"),
    ("17/01/2025 16:40", "SKEMA", "Échéance de 4 000,00 € au 20/02/2025 : « Le montant indiqué tient compte des remises et peut différer de celui de votre échéancier contractuel […] Un ajustement s'est établi sur votre dernière échéance de PGE M1. » Mention : « Message à transférer à la personne en charge du paiement de votre scolarité. »", "—"),
    ("17/01/2025 17:18", "ÉTUD", "« l'État gabonais s'est engagé à régler le programme Grande École en trois fois, car ma bourse s'achève en 2025. Dans mon cas, j'ai envoyé à SKEMA deux bons de commande qui ont théoriquement soldé les 2/3 de ma scolarité. S'agit-il d'une relance automatique ? Éprouvez-vous des difficultés à recevoir les fonds de Campus France ? »", "—"),
    ("20/01/2025 11:19", "SKEMA", "« Il s'agit d'une relance automatique. J'ai bien connaissance qu'il s'agit de Campus France pour le financement de vos frais de scolarité. Je me suis permise de les relancer car nous n'avons toujours rien reçu de leur part. »", "—"),
    ("20/01/2025 11:38", "ÉTUD", "À l'Agence et à Campus France : « J'ai bien reçu le bon de commande (en pièce jointe) mais je n'ai toujours pas eu confirmation de réception des fonds par skema depuis 7 mois […] pourriez-vous dans la mesure du possible communiquer à la comptabilité un délai ou une explication afin que mes accès ne soient pas bloqués. »", "—"),
    ("04/02/2025 11:46", "CF", "« Comme vous pouvez le voir ci-dessous, votre commande est à l'état facturée c'est-à-dire que vos frais de scolarité 2023-2024 ont bien été réglés. »", "—"),
    ("17/02/2025 11:06", "ANBG", "« Le document DOCUMENT RECOURS / PREUVE VALIDATION M1 a été validé par l'ANBG. »", "E"),
    ("17/02/2025 11:11", "ANBG", "« Le recours sur votre dossier de demande de bourse sous la référence 1LMK24 a été statué irrecevable pour le motif suivant : PARCOURS INSOUTENABLE (ARTICLE 4 DECRET 065). Votre dossier a été definitivement clôturé. »", "E"),
    ("21/02/2025", "ÉTAT", "Décret n° 0115/PR/MESRIT du 21 février 2025 (Journal officiel n° 56 bis du 26 février 2025) : abroge « toutes dispositions antérieures contraires, notamment celles du décret n° 0065/PR/MESRSIT du 12 février 2024 ».", "—"),
    ("23/07/2025 11:44", "ANBG", "« Le document RELEVÉ(S) DES NOTES DE(S) ANNÉE(S) PRÉCÉDENTE(S) a été validé par l'ANBG », dossier CA24B3.", "E"),
    ("02/09/2025 11:38", "ÉTUD", "Dépôt sur la plateforme, dossier CA24B3, onglet pièces justificatives, de la pièce « Facture coût de la scolarité » (269 ko).", "E"),
    ("25/09/2025 12:15", "CF", "« La facture N° 1281253 du fournisseur SKEMA BUSINESS SCHOOL N° 35025 est rejetée par le Service Financier Opérations sous Mandat pour le motif suivant : Certificat de scolarité manquant ou non conforme. Après vérification, vous devrez corriger les anomalies mentionnées et remettre le « Bon à payer ». »", "D"),
    ("06/10/2025 15:19", "CF", "« URGENT, Au plus vite, veuillez nous adresser : Il faut soit un relevé de note pour 2023-2024 soit un certificat de scolarité daté d'après le 1 septembre 2023 — Dossier 110584Z. »", "D"),
    ("06/10/2025 17:10", "ÉTUD", "Transmission de la pièce d'inscription 2023-2024 (réf. 2E4C0B, 225 ko).", "D"),
    ("29/10/2025 12:34", "CF", "« Le document demandé doit être daté de septembre 2023, or là il est daté du 26/07. Merci de nous envoyer le document conforme ou bien vos résultats définitifs 23/24. »", "D"),
    ("06/11/2025 12:01", "ÉTUD", "Transmission de trois attestations (absence de notes M1, attestation globale M1, relevé de notes M1) : « Je fais de mon mieux pour répondre à votre demande, mais l'école ne comprend pas pourquoi mon attestation est rejetée et peine à m'apporter une réponse claire. » Aucune suite n'est enregistrée depuis cette date.", "D"),
    ("10/11/2025 15:47", "ANBG", "« votre dossier n'a pas reçu un avis favorable pour le motif suivant : PARCOURS INSOUTENABLE (ARTICLE 4 DÉCRET 065). Toutefois, nous vous encourageons à renouveler votre demande l'année prochaine. »", "E"),
    ("09/12/2025", "SKEMA", "Attestation de la Direction de l'expérience étudiant : « Est régulièrement inscrit en Programme Grande Ecole pour l'année académique 2025-2026. L'étudiant est actuellement en Master 1. Suit régulièrement les cours sur le campus de Paris. L'étudiant est attendu sur le campus de SKEMA Belo Horizonte pour le semestre SPRING26. »", "F"),

    ("ANNEE 2026 — reprise du montant, passage au contentieux",),
    ("21/09/2026", "SKEMA", "Attestation de scolarité délivrée par la comptabilité clients.", "—"),
    ("22/09/2026", "ÉTUD", "Proposition écrite à la comptabilité : reconnaissance de dette de 7 500,00 €, échéancier de 300 € par mois sur vingt-cinq mois à compter de janvier 2027, contre émission du certificat de scolarité du semestre 5. Virement de 10,00 € le même jour (libellé MINANG 0305476).", "—"),
    ("26/09/2026", "ÉTUD", "Information de la comptabilité étudiants sur l'état des démarches de financement.", "—"),
    ("30/09/2026", "SKEMA", "Réclamation de 7 500,00 €, échéances annoncées des 20/10/2026 et 20/12/2026, annonce d'une possible cessation de scolarité.", "—"),
    ("05/10/2026", "SKEMA", "Édition du relevé de compte étudiant (Cegid).", "I"),
    ("07/10/2026 15:04", "SKEMA", "Mise en demeure, réf. 2026-SK.D-0002 : « votre compte étudiant présente à ce jour un solde débiteur de 14 840,00 €, correspondant aux frais de scolarité dus au titre de l'année académique 2025/2026 » ; « Le contrat de scolarité a été conclu entre vous et SKEMA et l'absence ou la cessation de prise en charge par un organisme tiers ne vous libère pas de votre obligation de paiement » ; « Cette démarche d'accompagnement ne saurait être interprétée comme une renonciation au paiement » ; règlement sous « dix (10) jours », à défaut procédure judiciaire « avec les frais, intérêts et dépens » et « cessation définitive de scolarité ». Échéance du délai : 19/10/2026.", "I"),
    ("07/10/2026 21:06", "ANBG", "Fiche de demande de bourse d'études, session 2025-2026, référence externe 110584Z, consultée sur l'espace étudiant : « DÉCISION : AVIS DÉFAVORABLE », « VOUS ÊTES NON BOURSIER », pays de la demande France, diplôme Master. Arborescence : CA24B3, 1LMK24, 2E4C0B, LDPMRC, PNPXWG, 4EO0OO, WEXQTG.", "E"),
    ("08/10/2026", "ÉTUD", "Recours gracieux formé contre les décisions des 25/09/2024 et 10/11/2025, remis en main propre contre accusé (pièce A).", "A"),
    ("Situation au 08/10/2026", "ÉTUD", "Fin de cycle prévue en décembre 2026. Titre de séjour arrivant à échéance le 30/01/2027 ; le renouvellement est subordonné au certificat de scolarité du semestre 5.", "—"),
]

PIECES_INDEX = [
    ("A", "08/10/2026", "Étudiant", "Recours gracieux signé, avec procuration (K) et accusé de remise (L)", "ÉTUD"),
    ("B", "04/02/2021", "ANBG", "Attestation de maintien de paiement n° 100326-21-MAINTIEN", "ANBG"),
    ("C", "02/11/2021", "ANBG", "Attestation d'attribution n° 100057-22-ACCORD", "ANBG"),
    ("D", "25/09 → 06/11/2025", "Campus France", "Filet « TR: Facture rejetée SFO N° 1281253 », quatre messages", "CF"),
    ("E", "25/09/2024 → 07/10/2026", "ANBG", "Notifications et validations de la plateforme eBourse, horodatées", "ANBG"),
    ("F", "14/05/2024 et 09/12/2025", "SKEMA", "Attestation du registraire ; attestation d'assiduité", "SKEMA"),
    ("G", "24/01/2023 et 06/05/2024", "Campus France", "Bons de commande n° 677745 et n° 721622", "CF"),
    ("H", "04/01/2024", "SKEMA", "Convention de stage SKEMA / BPCE, 08/01/2024 → 05/07/2024", "SKEMA"),
    ("I", "14/11/2024 et 07/10/2026", "SKEMA", "Rappel de droits scolaires 2024/2025 ; mise en demeure 2026-SK.D-0002", "SKEMA"),
    ("J", "2022-2025", "SKEMA", "Contrat d'inscription Fall 2022, dossier d'inscription et acte de cautionnement", "SKEMA"),
    ("K", "08/10/2026", "Étudiant", "Procuration donnée au porteur du dossier", "ÉTUD"),
    ("L", "08/10/2026", "Étudiant", "Accusé de remise du recours, deux exemplaires", "ÉTUD"),
]

# pièces matérielles : lettre -> [(fichier, pages)], type spécial éventuel
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
TITRE_ANNEXE = {
    "A": "Recours gracieux — décisions des 25/09/2024 et 10/11/2025",
    "B": "Attestation de maintien de paiement de bourse n° 100326-21-MAINTIEN",
    "C": "Attestation d'attribution de bourse n° 100057-22-ACCORD",
    "D": "Filet de courriels « Facture rejetée SFO n° 1281253 »",
    "E": "Notifications de la plateforme eBourse (à imprimer depuis l'espace étudiant)",
    "F": "Attestation du registraire du 14/05/2024 ; attestation d'assiduité du 09/12/2025",
    "G": "Bons de commande Campus France n° 677745 et n° 721622",
    "H": "Convention de stage SKEMA Business School / BPCE du 04/01/2024",
    "I": "Rappel de droits scolaires 2024/2025 ; mise en demeure 2026-SK.D-0002",
    "J": "Contrat d'inscription Fall 2022 ; dossier d'inscription et acte de cautionnement",
    "K": "Procuration donnée au porteur du dossier",
    "L": "Accusé de remise du recours — deux exemplaires",
}


def _split_long(words, size, width, f):
    """Coupe les tokens plus larges que la colonne (URL, références longues)."""
    out = []
    for w in words:
        while f.text_length(w, size) > width and len(w) > 3:
            k = len(w)
            while k > 2 and f.text_length(w[:k], size) > width:
                k -= 1
            out.append(w[:k])
            w = w[k:]
        out.append(w)
    return out


MOIS = {"janv": 1, "févr": 2, "fevr": 2, "mars": 3, "avr": 4, "mai": 5, "juin": 6,
        "juil": 7, "juill": 7, "août": 8, "aout": 8, "sept": 9, "oct": 10, "nov": 11, "déc": 12, "dec": 12}


def sortkey(d):
    """Clé de tri : date précise, sinon calage sur la période évoquée."""
    s = d.strip()
    m = re.search(r"(\d{1,2})/(\d{1,2})/(\d{4})", s)
    if m:
        return (int(m.group(3)), int(m.group(2)), int(m.group(1)), s)
    m = re.search(r"(\d{4})/(\d{4})", s)
    if m:
        return (int(m.group(1)), 9, 1, s)
    m = re.search(r"(\d{4})\s*$", s)
    y = int(m.group(1)) if m else 9999
    mo = 0
    low = s.lower()
    for k, v in MOIS.items():
        if k in low:
            mo = v
            break
    if "1er semestre" in low:
        mo = 1
    if "2nd semestre" in low or "second semestre" in low:
        mo = 7
    if "rentrée" in low:
        mo = max(mo, 9)
    return (y, mo or 6, 0, s)


def pline(p, x, y, text, size, fname="DJr", color=(0, 0, 0), width=None):
    """Ligne d'en-tête : reprise à la ligne automatique si elle dépasse la page."""
    f = FONTS["b"] if fname == "DJb" else FONTS["r"]
    w = width or (W - MR - x)
    for ln in wrap(text, size, w, f):
        p.insert_text((x, y), ln, fontname=fname, fontsize=size, color=color)
        y += size + 3.4
    return y


def wrap(text, size, width, f):
    out, cur, cw = [], [], 0.0
    for w in _split_long(text.split(), size, width, f):
        ww = f.text_length(w, size)
        if cur and cw + ww > width:
            out.append(" ".join(cur))
            cur, cw = [w], ww
        else:
            cur.append(w)
            cw += ww + f.text_length(" ", size)
    if cur:
        out.append(" ".join(cur))
    return out


class Doc:
    def __init__(self):
        self.d = fitz.open()
        self.pg = None
        self.n = 0
        self.new(cover=True)

    def new(self, cover=False):
        self.n = self.d.page_count + 1          # numéro = page physique, annexes comprises
        self.pg = self.d.new_page(width=W, height=H)
        for st, nm in (("r", "DJr"), ("b", "DJb"), ("i", "DJi")):
            self.pg.insert_font(fontname=nm, fontfile=FF[st])
        self.y = MT
        if not cover:
            self.pg.draw_line(fitz.Point(ML, H - 30), fitz.Point(W - MR, H - 30), width=0.3, color=(0.72, 0.73, 0.76))
            self.pg.insert_text((ML, H - 19), "Calvin B. MINANG — dossier 110584Z — historique documenté, établi le 8 octobre 2026 sur pièces A à L", fontname="DJr", fontsize=6.6, color=(0.45, 0.47, 0.52))
            self.pg.insert_text((W - MR - 24, H - 19), str(self.n), fontname="DJr", fontsize=7.4, color=(0.30, 0.32, 0.36))

    def need(self, h):
        if self.y + h > H - MB:
            self.new()
            return True
        return False

    def save(self, path):
        try:
            self.d.subset_fonts()
        except Exception:
            pass
        self.d.save(path, deflate=True, garbage=4, clean=True)


def header(doc):
    p = doc.pg
    p.draw_line(fitz.Point(ML, MT + 1.5), fitz.Point(W - MR, MT + 1.5), width=1.5, color=(0.08, 0.09, 0.13))
    y = MT + 20
    y = pline(p, ML, y, "HISTORIQUE DOCUMENTÉ — BOURSE D'ÉTAT, PRISE EN CHARGE ET FACTURATION SCOLAIRE", 10.4, "DJb", (0.07, 0.08, 0.11))
    y += 1
    g = (0.20, 0.22, 0.26)
    y = pline(p, ML, y, "MINANG Calvin Blanchard — né le 02/05/2002 à Libreville (Gabon) — SKEMA Business School, Programme Grande École, 2ᵉ année de Master (MSc Corporate Financial Management), n° étudiant 0305476", 8.2, color=g)
    y = pline(p, ML, y, "Dossier ANBG / Campus France n° 110584Z — sept dossiers eBourse de 2019-2020 à 2025-2026", 8.2, color=g)
    y = pline(p, ML, y, "Créance de 14 840,00 € au titre de l'année 2025/2026, mise en demeure du 07/10/2026, délai de dix jours : 19/10/2026", 8.2, color=g)
    y += 3
    x = ML
    for k, col in C.items():
        p.draw_rect(fitz.Rect(x, y - 6.4, x + 8.5, y + 1.4), color=None, fill=col)
        lab = NOM[k]
        p.insert_text((x + 13, y), lab, fontname="DJr", fontsize=7.6, color=col)
        x += 13 + FONTS["r"].text_length(lab, 7.6) + 16
    p.insert_text((x, y), "— acteur, en marge", fontname="DJr", fontsize=7.6, color=(0.36, 0.38, 0.42))
    y += 11
    y = pline(p, ML, y, "Les mentions entre guillemets reproduisent le texte de la pièce citée ; la dernière colonne renvoie à la pièce jointe qui l'établit.", 7.6, color=(0.36, 0.38, 0.42))
    doc.y = y + 2
    col_header(doc)


def col_header(doc):
    p = doc.pg
    x = ML
    doc.tab = []
    for name, wd in COLS:
        doc.tab.append((x, wd))
        p.draw_line(fitz.Point(x, doc.y + 3), fitz.Point(x + wd, doc.y + 3), width=0.6, color=(0.20, 0.22, 0.28))
        tx = x + (wd - FONTS["b"].text_length(name.upper(), 6.9)) if name == "Pièce" else x
        p.insert_text((tx, doc.y - 3.5), name.upper(), fontname="DJb", fontsize=6.9, color=(0.32, 0.34, 0.40))
        x += wd + GAP
    doc.y += 7.5


def row_year(doc, label):
    doc.need(19)
    p = doc.pg
    p.draw_rect(fitz.Rect(ML - 6, doc.y, W - MR + 6, doc.y + 14.5), color=None, fill=(0.93, 0.935, 0.945))
    p.insert_text((ML, doc.y + 10), label.upper(), fontname="DJb", fontsize=7.5, color=(0.16, 0.18, 0.24))
    doc.y += 18.5


def row(doc, date, act, fait, piece):
    col = C[act]
    body = doc.tab[2][1] - 4
    lines = wrap(fait, 7.9, body - 4, FONTS["r"])
    dlines = wrap(date, 7.9, doc.tab[0][1] - 2, FONTS["b"])
    h = max(len(lines), len(dlines)) * 10.3 + 4.2
    if doc.y + h > H - MB:
        doc.new()
        doc.pg.insert_text((ML, MT - 6), "Historique documenté — suite", fontname="DJr", fontsize=7.0, color=(0.45, 0.47, 0.52))
        doc.y = MT + 8
        col_header(doc)
    p = doc.pg
    top = doc.y
    p.draw_rect(fitz.Rect(ML - 6, top, ML - 3.2, top + h - 1.5), color=None, fill=col)
    p.draw_line(fitz.Point(ML - 6, top + h - 0.6), fitz.Point(W - MR + 6, top + h - 0.6), width=0.22, color=(0.80, 0.81, 0.84))
    yy = top + 7.6
    for i, ln in enumerate(dlines):
        p.insert_text((doc.tab[0][0], yy), ln, fontname="DJb", fontsize=7.9)
        yy += 10.3
    p.insert_text((doc.tab[1][0], top + 7.6), NOM[act], fontname="DJb", fontsize=7.3, color=col)
    yy = top + 7.6
    for ln in lines:
        p.insert_text((doc.tab[2][0], yy), ln, fontname="DJr", fontsize=7.9, color=(0.10, 0.11, 0.14))
        yy += 10.3
    p.insert_text((doc.tab[3][0] + doc.tab[3][1] - FONTS["r"].text_length(piece, 7.9), top + 7.6), piece, fontname="DJr", fontsize=7.6, color=(0.30, 0.32, 0.36))
    doc.y = top + h


def pieces(doc):
    doc.new()
    p = doc.pg
    p.draw_line(fitz.Point(ML, MT + 1.5), fitz.Point(W - MR, MT + 1.5), width=1.5, color=(0.08, 0.09, 0.13))
    p.insert_text((ML, MT + 18), "PIÈCES JOINTES", fontname="DJb", fontsize=10.4)
    y = pline(p, ML, MT + 28, "Reproduites à la suite de l'historique, dans l'ordre des lettres. Les pièces B, C, E sont établies par l'ANBG, D et G par Campus France, F, H, I, J par SKEMA Business School, A, K, L par l'étudiant.", 7.9, color=(0.24, 0.26, 0.30))
    y += 8
    hdr = [(0, "Lettre"), (52, "Date"), (168, "Émetteur"), (266, "Objet")]
    for x0, t in hdr:
        p.insert_text((ML + x0, y), t.upper(), fontname="DJb", fontsize=6.9, color=(0.32, 0.34, 0.40))
    p.draw_line(fitz.Point(ML, y + 4), fitz.Point(W - MR, y + 4), width=0.6, color=(0.20, 0.22, 0.28))
    y += 15.5
    for lettre, date, emet, objet, act in PIECES_INDEX:
        lines = wrap(objet, 7.9, W - MR - (ML + 266), FONTS["r"])
        hh = max(1, len(lines)) * 10.2 + 4.0
        if y + hh > H - MB:
            doc.new()
            y = MT + 8
        p = doc.pg
        p.draw_rect(fitz.Rect(ML - 6, y - 8, ML - 3.2, y + hh - 5), color=None, fill=C[act])
        p.draw_line(fitz.Point(ML - 6, y + hh - 4.5), fitz.Point(W - MR + 6, y + hh - 4.5), width=0.22, color=(0.80, 0.81, 0.84))
        p.insert_text((ML, y), lettre, fontname="DJb", fontsize=8.2, color=C[act])
        p.insert_text((ML + 52, y), date, fontname="DJr", fontsize=7.9)
        p.insert_text((ML + 168, y), emet, fontname="DJr", fontsize=7.9)
        for i, ln in enumerate(lines):
            p.insert_text((ML + 266, y + i * 10.2), ln, fontname="DJr", fontsize=7.9, color=(0.10, 0.11, 0.14))
        y += hh + 1.5
    doc.y = y


def annex_divider(doc, lettre):
    """Feuillet séparateur ; renvoie (index de page, x, y) pour la pagination stampée après coup."""
    doc.new()
    p = doc.pg
    col = C[PIECES_INDEX[[r[0] for r in PIECES_INDEX].index(lettre)][4]]
    p.draw_rect(fitz.Rect(ML - 6, MT + 10, ML - 2.2, MT + 26), color=None, fill=col)
    p.draw_line(fitz.Point(ML, MT + 1.5), fitz.Point(W - MR, MT + 1.5), width=1.5, color=(0.08, 0.09, 0.13))
    p.insert_text((ML, MT + 22), f"PIÈCE {lettre}", fontname="DJb", fontsize=9.6, color=col)
    y = MT + 42
    for ln in wrap(TITRE_ANNEXE[lettre], 11.6, AVAIL - 20, FONTS["b"]):
        p.insert_text((ML, y), ln, fontname="DJb", fontsize=11.6)
        y += 15.0
    y += 6
    ent = next(r for r in PIECES_INDEX if r[0] == lettre)
    em = {"SKEMA": "SKEMA Business School"}.get(ent[2], ent[2])
    if ANNEX[lettre][1] == "à produire":
        phr = f"Cette pièce n'est pas jointe : à imprimer depuis l'espace étudiant, {ent[1]}, et à glisser dans le dossier avant remise."
    else:
        phr = f"Établie par {em} — {ent[1]}. Pièce reproduite sans annotation ; les extraits cités dans l'historique en sont tirés textuellement."
    for ln in wrap(phr, 8.4, AVAIL - 20, FONTS["r"]):
        p.insert_text((ML, y), ln, fontname="DJr", fontsize=8.4, color=(0.30, 0.32, 0.36))
        y += 11.0
    p.draw_line(fitz.Point(ML, y + 4), fitz.Point(W - MR, y + 4), width=0.4, color=(0.62, 0.64, 0.68))
    doc.y = y + 18
    return doc.d.page_count - 1, ML, y + 16


def stamp(doc, spots):
    """Renseigne sur chaque feuillet la plage de pages effectivement occupée par la pièce."""
    for idx, x, y, a, b in spots:
        p = doc.d[idx]
        b = min(b, doc.d.page_count)
        if b < a:
            continue
        lab = f"pages {a} à {b} du dossier" if b > a else f"page {a} du dossier"
        p.insert_text((x, y), lab, fontname="DJb", fontsize=8.0, color=(0.26, 0.28, 0.34))


def main():
    os.makedirs(OUT, exist_ok=True)
    doc = Doc()
    header(doc)
    groupe = []

    def vider():
        for it in sorted(groupe, key=lambda x: sortkey(x[0])):
            row(doc, *it)
        del groupe[:]

    for r in R:
        if len(r) == 1:
            vider()
            row_year(doc, r[0])
        else:
            groupe.append(r)
    vider()
    pieces(doc)

    # annexes matérielles
    rtmp = os.path.join(tempfile.gettempdir(), "actes.pdf")
    src = open(os.path.join(BASE, "PARENTS-ANBG", "RECOURS-GRACIEUX-ANBG.md"), encoding="utf-8").read()
    a0 = src.index("# 1. RECOURS GRACIEUX")
    a1 = src.index("# 4. CHEMISE") if "# 4. CHEMISE" in src else len(src)
    md2pdf.render(src[a0:a1].rstrip() + "\n", rtmp, "")
    actes = fitz.open(rtmp)
    ix = {}
    for k in ("1. RECOURS GRACIEUX", "2. PROCURATION", "3. ACCUSÉ DE REMISE"):
        j = next((i for i, pg in enumerate(actes) if k in pg.get_text()), None)
        if j is None:
            print(f"  ! section introuvable dans le recours : {k}")
            j = 0
        ix[k] = j
    spots = []
    for lettre in "ABCDEFGHIJKL":
        idx, x, y = annex_divider(doc, lettre)
        debut = doc.d.page_count + 1      # 1-based : première page de pièce
        fichiers, spec = ANNEX[lettre]
        if spec == "à produire":
            spots.append((idx, x, y, debut, debut - 1))
            continue
        if spec:
            fin = len(actes)
            a, b = {"recours": (ix["1. RECOURS GRACIEUX"], ix["2. PROCURATION"]),
                    "procuration": (ix["2. PROCURATION"], ix["3. ACCUSÉ DE REMISE"]),
                    "recepisse": (ix["3. ACCUSÉ DE REMISE"], fin)}[spec]
            doc.d.insert_pdf(actes, from_page=a, to_page=max(a, b - 1))
            doc.pg = doc.d[-1]
            spots.append((idx, x, y, debut, doc.d.page_count))
            continue
        for fn, keep in fichiers:
            path = os.path.join(PIECES, fn)
            if not os.path.exists(path):
                print(f"  ! pièce absente : {fn}")
                continue
            s = fitz.open(path)
            if keep:
                s.select([i for i in keep if i < s.page_count])
            doc.d.insert_pdf(s)
            s.close()
            doc.pg = doc.d[-1]
        spots.append((idx, x, y, debut, doc.d.page_count))
    while doc.d and not doc.d[-1].get_text().strip() and not doc.d[-1].get_images():
        doc.d.delete_page(-1)
    stamp(doc, spots)
    actes.close()
    os.remove(rtmp)

    dest = os.path.join(OUT, "HISTORIQUE-DOCUMENTE-2019-2026-MINANG.pdf")
    doc.save(dest)
    print(f"HISTORIQUE-DOCUMENTE-2019-2026-MINANG.pdf — {doc.d.page_count} pages, {os.path.getsize(dest)/1024:.0f} Ko")
    doc.d.close()


if __name__ == "__main__":
    main()
