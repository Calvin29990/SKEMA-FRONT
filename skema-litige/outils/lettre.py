# -*- coding: utf-8 -*-
"""Lettre recommandée — historique 2019-2026, bordereau et pièces A à L.

Corps noir ; la couleur indique l'auteur de l'acte : rouge SKEMA Business School,
bleu ANBG, vert Campus France, gris État gabonais. Un seul PDF livré.
"""
import os
import sys
import tempfile

import pymupdf as fitz

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "outils"))
import md2pdf  # noqa: E402  (re-rendu du recours, du texte déjà rédigé)

FD = "/usr/share/fonts/truetype/dejavu/"
FFILE = {"r": FD + "DejaVuSerif.ttf", "b": FD + "DejaVuSerif-Bold.ttf",
         "i": FD + "DejaVuSerif-Italic.ttf", "bi": FD + "DejaVuSerif-BoldItalic.ttf"}
for _k, _v in list(FFILE.items()):
    if not os.path.exists(_v):
        FFILE[_k] = FD + "DejaVuSerif.ttf"
FONTS = {k: fitz.Font(fontfile=v) for k, v in FFILE.items()}

W, H = 595.0, 842.0
ML, MR, MT, MB = 62.0, 52.0, 56.0, 58.0
AVAIL = W - ML - MR
OUT = os.path.join(BASE, "pdf")
PIECES = os.path.join(BASE, "pieces")

NOIR = (0.04, 0.04, 0.06)
GRIS = (0.34, 0.34, 0.37)
COL = {"S": (0.66, 0.09, 0.08),   # SKEMA Business School
       "A": (0.08, 0.25, 0.60),   # ANBG
       "C": (0.05, 0.42, 0.29),   # Campus France
       "E": GRIS,                 # État gabonais
       "M": NOIR,                 # l'étudiant
       "B": NOIR}                 # noir, gras


class Feuille:
    def __init__(self):
        self.d = fitz.open()
        self.pg = None
        self.new()

    def new(self):
        self.pg = self.d.new_page(width=W, height=H)
        for st in FFILE:
            self.pg.insert_font(fontname="F" + st, fontfile=FFILE[st])
        self.y = MT

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


def _f(key):
    return "Fb" if key == "B" else "Fr"


PUNCT = (",", ".", ";", ":", "!", "?", ")", "»", "%", "’")
SEULS = {":", ";", "!", "?"}   # ponctuation précédée d'une espace fine en français


def para(f, runs, size=10.5, lead=14.8, space=7.0, width=None, justifier=True):
    """Paragraphe à runs colorés : les mots collés à la ponctuation ne prennent pas d'espace."""
    width = width or AVAIL
    ws = FONTS["r"].text_length(" ", size)
    mots = []
    for text, key in runs:
        fo = FONTS["b" if key == "B" else "r"]
        for mot in text.split():
            if (mots and mot[0] in PUNCT and mot not in SEULS
                    and mots[-1][0][-1] not in "(«“"):
                fp = FONTS["b"] if mots[-1][1] == "Fb" else FONTS["r"]
                mots[-1] = (mots[-1][0] + mot, mots[-1][1], mots[-1][2],
                            fp.text_length(mots[-1][0] + mot, size))
                continue
            for part in _coupe(mot, size, width, fo):
                mots.append((part, _f(key), COL.get(key, NOIR), fo.text_length(part, size)))
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
        for mot, fname, col, wd in line:
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


def ligne(f, texte, size=10.5, gras=False, col=NOIR, x=None, droite=False, lead=None):
    fo = FONTS["b" if gras else "r"]
    if droite or x is None:
        xx = W - MR - fo.text_length(texte, size) if droite else (x if x is not None else ML)
    else:
        xx = x
    f.pg.insert_text((xx, f.y + size * 0.83), texte, fontname="Fb" if gras else "Fr",
                     fontsize=size, color=col)
    f.y += lead if lead else size + 4.0


# ------------------------------------------------------------------- en-tête
EXPED = ["Né le 2 mai 2002 à Libreville (Gabon)",
         "Étudiant — SKEMA Business School, Programme Grande École, 2ᵉ année",
         "MSc Corporate Financial Management — n° étudiant 0305476",
         "Dossier ANBG / Campus France n° 110584Z",
         "blanchardminang00@gmail.com"]

DEST = [("Monsieur le Directeur général", "A"), ("de l'Agence Nationale des Bourses du Gabon", "A"),
        ("Direction générale — Commission technique", "A"), ("c.ngari.anbg@gmail.com", "A"),
        ("", ""),
        ("Madame la Responsable du Service", "C"), ("Financement et Bourses — Campus France", "C"),
        ("anbg.boursiers@campusfrance.org", "C"),
        ("", ""),
        ("Madame Amandine Boucly, Legal Expert", "S"),
        ("Student Accounting Office", "S"),
        ("SKEMA Business School", "S"),
        ("amandine.boucly@skema.edu", "S"),
        ("studentaccountingoffice@skema.edu", "S"),
        ("", ""),
        ("Copie : beatrice.marino@skema.edu,", "M"), ("maxime.belloni@skema.edu", "M")]


def entete(f):
    ligne(f, "Calvin B. MINANG", 11.5, gras=True, lead=15.0)
    for t in EXPED:
        ligne(f, t, 9.5, lead=12.4)
    f.y += 18
    x = 300.0
    for txt, key in DEST:
        if txt:
            ligne(f, txt, 8.8, x=x, lead=11.4)
        else:
            f.y += 5
    f.y += 14
    ligne(f, "Le 8 octobre 2026", 10.2, droite=True)
    f.y += 16
    ligne(f, "Lettre recommandée avec accusé de réception", 10.4, gras=True, lead=14.0)
    para(f, [("Objet : ", "B"), ("Bourse d'État, prise en charge des frais de scolarité et "
              "facturation — historique 2019-2026 et demandes", "B")], size=10.4, lead=14.0,
         space=1.5, justifier=False)
    para(f, [("Un seul exemplaire par destinataire, valant communication du dossier complet. ", "M"),
             ("PJ : douze pièces cotées A à L, bordereau en fin de lettre.", "M")],
         size=10.4, lead=14.0, space=1.5, justifier=False)
    f.pg.draw_line(fitz.Point(ML, f.y + 2), fitz.Point(W - MR, f.y + 2), width=0.6, color=NOIR)
    f.y += 16


# ---------------------------------------------------------------------- corps
FAITS = [
    [("2019-2020. ", "B"),
     ("Inscrit en classes préparatoires, filière ECE, Groupe Scolaire La Résidence, Casablanca, "
      "j'obtiens la bourse nationale d'études au titre de la session 2019-2020, dossier eBourse ",
      "M"), ("WEXQTG.", "A"), (" Pièce ", "M"), ("E.", "B")],

    [("1er février 2021. ", "B"),
     ("La Commission technique de l'Agence maintient la bourse nationale, catégorie C.", "A"),
     (" Le ", "M"), ("4 février 2021", "B"),
     (", l'Agence délivre l'attestation de maintien de paiement n° 100326-21-MAINTIEN : "
      "« Classes Préparatoires 2 au/en MAROC / CASABLANCA », « valable jusqu'au 30/09/2021 », "
      "« montant mensuel [...] 165 000 FCFA », avec la mention que la reconduction en N+1 est "
      "conditionnée à la présentation des résultats annuels.", "A"), (" Pièce B.", "M")],

    [("2 novembre 2021. ", "B"),
     ("L'Agence attribue la bourse par l'attestation n° 100057-22-ACCORD, établissement "
      "IPESUP, France/Paris, « pour une durée : 1 année(s), du 01/09/2021 au 31/08/2022 ».", "A"),
     (" La durée portée sur la plateforme est d'une année ; les dossiers suivants en porteront "
      "deux.", "M"), (" Pièce C.", "M")],

    [("2022. ", "B"),
     ("Admis au Programme Grande École par le concours BCE (n° de candidat 21446), j'inscris "
      "l'année de préparation à la sortie du cycle comme le permet le régime de la bourse. Le ",
      "M"), ("25 août 2022", "B"), (", l'établissement écrit : « Concernant la facturation, "
      "je transfère votre mail à la comptabilité étudiante. »", "S"), (" Le ", "M"),
     ("26 août 2022", "B"),
     (", le dossier d'inscription n° 2733904447 comporte un formulaire d'acte de cautionnement "
      "au nom de ", "M"), ("« ETAT », prénom « GABONAIS »", "E"),
     (", courriel de notification anbg.boursiers@campusfrance.org, limite « quarante six mille "
      "euros (46 000 €) », durée « soixante (60) mois ».", "S"),
     (" Entrée en PGE le ", "M"), ("1er septembre 2022", "B"), (", campus de Paris. Pièce J.", "M")],

    [("Novembre 2022 - janvier 2023. ", "B"),
     ("La comptabilité de l'établissement demande le numéro de dossier et le bon de commande "
      "(", "S"), ("2 novembre 2022", "B"), (") ; je transmets la demande de devis le ", "M"),
     ("10 janvier 2023", "B"), (" à ", "M"), ("12:30", "B"), (".", "M")],

    [("24 janvier 2023. ", "B"), ("Campus France pose la règle de facturation par écrit : "
      "« Nous vous invitons à établir une facture à l'ordre de campus France et à la déposer sur "
      "Chorus Pro » ; « Dans l'hypothèse où l'étudiant aurait versé un acompte, merci de bien "
      "vouloir le faire apparaître clairement » ; « pouvez-vous me confirmer que l'étudiant peut "
      "de nouveau avoir accès aux cours ainsi qu'aux supports pédagogiques ? »", "C"),
     (" Le même jour est émis le ", "M"), ("bon de commande n° 677745", "B"),
     (", dossier 110584Z, « FRAIS DE FORMATION 22/23 », fournisseur SKEMA BUSINESS SCHOOL "
      "n° 35025, ", "C"), ("15 000,00 €", "B"), (", signé par le responsable du service Afrique.",
      "C"), (" L'accusé de réception de la comptabilité étudiantes suit le ", "M"),
     ("25 janvier 2023", "B"), (" à ", "M"), ("09:43", "B"), (". Pièce G.", "M")],

    [("Juillet 2023. ", "B"),
     ("Le jury de l'établissement délibère pour l'année 2022/2023 : les semestres ne sont pas "
      "validés en L3.", "S"),
     (" C'est le seul échec enregistré à ce jour dans le cycle.", "M")],

    [("27 octobre 2023. ", "B"), ("L'établissement accepte la césure : « Votre demande pour "
      "effectuer la césure à partir de janvier 2024 a été acceptée. Je viens de mettre à jour "
      "votre dossier. »", "S"),
     (" Le ", "M"), ("17 octobre 2023", "B"), (", le certificat d'anglais iCIMS (67/100) est "
      "valable jusqu'au 16/10/2025 pour la délivrance du diplôme.", "S")],

    [("2024, année de césure. ", "B"),
     ("L'établissement signe le 4 janvier 2024 la convention de stage « 23/24-PGE FI L3 RD Paris "
      "semestre Fall » avec BPCE VIE : « Le stage se déroulera du 08/01/2024 au 05/07/2024 », "
      "cinq jours ouvrés par semaine, l'entreprise devant délivrer une attestation reprenant ces "
      "dates.", "S"), (" Cette attestation ne m'a jamais été remise ; la demande n'a pas été "
      "renouvelée depuis. Pièce H.", "M"),
     (" Le ", "M"), ("6 mai 2024", "B"), (", ", "M"), ("Campus France émet le bon de commande "
      "n° 721622", "C"), (" sur le dossier 110584Z, fournisseur 35025, objet « POUR LE COMPTE DE "
      "L'ANBG FRAIS FORMATION 2023 2024 », montant ", "C"), ("16 000,00 €", "B"),
     (". La prise en charge de l'année 2023/2024, année de césure, est donc engagée par l'organisme "
      "payeur. Pièce G.", "M"), (" Le ", "M"), ("14 mai 2024", "B"),
     (", le registraire de l'établissement certifie le parcours : « 2023/2024 L3/M1 Paris Fall 23 / "
      "Césure Spring 24 ; 2024/2025 M1 Césure Fall 24 / Raleigh Spring 25 ; 2025/2026 PGE M2 ».", "S"),
     (" Pièce F.", "M")],

    [("25 septembre 2024, 16:37. ", "B"), ("La plateforme de l'Agence enregistre la suppression "
      "de la bourse au motif « abs de releve de notes / perception de la bourse ».", "A"),
     (" Le relevé demandé portait sur une année dont l'établissement certifiait qu'elle était "
      "une année de césure, sans notes à produire. Pièce E.", "M")],

    [("14 novembre 2024. ", "B"), ("L'établissement rappelle la première échéance des droits "
      "scolaires 2024/2025 : ", "S"), ("12 000,00 €", "B"), (", virement BNP Paribas (n° étudiant "
      "22223500).", "S"), (" Le ", "M"), ("15 janvier 2025", "B"), (", la facture n° 22223502 est "
      "intitulée « Master 2 » pour ", "S"), ("15 000,00 €", "B"), (" ; le ", "M"),
     ("20 février 2025", "B"), (", une pièce comptable porte ", "S"), ("4 000,00 €", "B"),
     (". Pièce I.", "M"), (" Le ", "M"), ("17 décembre 2024", "B"),
     (", l'établissement délivre un certificat de scolarité pour 2024/2025.", "S")],

    [("17 février 2025. ", "B"),
     ("Les relevés de notes déposés les 15, 17 et 20 janvier 2025 sont validés par l'Agence à ", "A"),
     ("11:06", "B"), (" ; la décision d'irrecevabilité est enregistrée à ", "A"), ("11:11", "B"),
     (", pour « PARCOURS INSOUTENABLE (ARTICLE 4 DECRET 065) ».", "A"), (" Cinq minutes séparent "
      "la validation de la pièce et l'irrecevabilité du recours formé contre la suppression.", "M")],

    [("21 février 2025. ", "B"), ("Le décret n° 0115/PR/MESRIT du 21 février 2025 (Journal "
      "officiel n° 56 bis du 26 février 2025) dispose en son article 4 qu'« abroge[t] toutes "
      "dispositions antérieures contraires, notamment celles du décret n° 0065/PR/MESRSIT du 12 "
      "février 2024 ».", "E"), (" Le texte visé par la décision du 17 février 2025 a donc été "
      "abrogé le jour suivant ; celui du 10 novembre 2025 le vise encore.", "M")],

    [("25 septembre - 6 novembre 2025. ", "B"), ("La facture n° 1281253 est rejetée par le "
      "Service Financement et Bourses le ", "C"), ("25/09/2025 à 12:15", "B"),
     (", motif « Certificat de scolarité manquant ou non conforme », avec injonction de « remettre "
      "le « Bon à payer » ».", "C"), (" Le ", "M"), ("6 octobre 2025, 15:19", "B"), (", ", "C"),
     ("le service demande « le relevé de notes de l'année 2023-2024 ou un certificat de scolarité "
      "daté d'après le 1er septembre 2023 »", "C"), (" ; le ", "M"), ("29 octobre 2025, 12:34", "B"),
     (", il écarte le document « du 26/07 » comme « non conforme ».", "C"), (" Je réponds le ", "M"),
     ("6 novembre 2025, 12:01", "B"), (", en produisant trois attestations de l'établissement. "
      "Aucune suite n'a été donnée à ce message, ni depuis.", "M"), (" Pièce D.", "M")],

    [("10 novembre 2025, 15:47. ", "B"), ("La Commission technique de l'Agence émet un avis "
      "défavorable (référence CA24B3) sur la demande, en m'invitant à la renouveler.", "A"),
     (" Le ", "M"), ("9 décembre 2025", "B"), (", soit vingt-neuf jours après, l'établissement "
      "certifie mon assiduité.", "S"), (" Pièces E et F.", "M")],

    [("2026. ", "B"), ("Le ", "M"), ("30 septembre 2026", "B"), (", la comptabilité de "
      "l'établissement porte la somme à ", "S"), ("7 500,00 €", "B"), (" ; le ", "M"),
     ("5 octobre 2026", "B"), (", un document comptable porte ", "S"), ("14 840,00 €", "B"), (". Le ",
      "M"), ("7 octobre 2026 à 15:04", "B"), (", la mise en demeure n° 2026-SK.D-0002 réclame le "
      "solde de ", "S"), ("14 840,00 € « au titre de l'année 2025/2026 »", "B"),
     (", avec paiement sous dix jours, en précisant que « l'absence ou la cessation de prise en "
      "charge par un organisme tiers ne vous libère pas », sous menace de procédure et de cessation "
      "définitive de scolarité.", "S"), (" Le même jour à ", "M"), ("21:06", "B"),
     (", la plateforme de l'Agence affiche, pour la session 2025-2026, référence externe 110584Z : "
      "« DÉCISION : AVIS DÉFAVORABLE », « VOUS ÊTES NON BOURSIER », pays de la demande France, "
      "diplôme Master, arborescence CA24B3, 1LMK24, 2E4C0B, LDPMRC, PNPXWG, 4E0O00, WEXQTG.", "A"),
     (" Pièces E et I.", "M")],

    [("Situation au 8 octobre 2026. ", "B"),
     ("Le contrat d'inscription de Fall 2022 est le seul contrat du cycle : 46 000,00 € pour une "
      "durée pouvant atteindre soixante mois, l'article 4.4 prévoyant son rallongement en cas de "
      "prolongation de scolarité. La fin de cycle est prévue en décembre 2026 et le titre de séjour "
      "arrive à échéance le 30 janvier 2027, son renouvellement étant subordonné au certificat de "
      "scolarité du semestre 5.", "M")],
]

DEMANDES = [
    [("À l'Agence nationale des bourses du Gabon", "A"),
     (", je demande : 1° la transmission du présent dossier à la Commission technique et son "
      "réexamen au titre des étudiants dont le cycle est engagé depuis le 1er septembre 2022, le "
      "retour à « coûts soutenables » portant sur les nouvelles attributions ; 2° la communication "
      "de la pièce, de la date et de la signature qui fondent l'avis défavorable du 10 novembre "
      "2025, ainsi que le détail du calcul des frais de scolarité pris en charge pour 2024/2025 et "
      "2025/2026 ; 3° la confirmation écrite à SKEMA Business School et à Campus France du maintien "
      "de la prise en charge pour 2025/2026 ; 4° la copie certifiée au guichet de la décision "
      "indiquant que la bourse du cycle Master a été attribuée pour deux années, la plateforme "
      "portant pour 2021 « 1 année(s) » et pour 2023 « deux années ».", "M")],
    [("Au Service Financement et Bourses de Campus France", "C"),
     (", je demande : 1° l'état de la facture n° 1281253 dans Chorus Pro à la date de réponse, et, "
      "si elle doit être représentée, la désignation de la pièce exacte attendue — les trois "
      "attestations produites le 6 novembre 2025 n'ayant appelé aucune observation ; 2° l'émission "
      "du bon de commande 2024/2025, les années 2022/2023 et 2023/2024 ayant donné lieu aux bons "
      "n° 677745 et n° 721622 ; 3° une attestation adressée à SKEMA Business School rappelant la "
      "règle posée le 24 janvier 2023, à savoir que la facturation est établie à l'ordre de Campus "
      "France et déposée sur Chorus Pro ; 4° que les demandes de pièces adressées à l'établissement "
      "le soient simultanément, et non plus après rejet.", "M")],
    [("À SKEMA Business School", "S"),
     (", je demande : 1° la communication de la pièce qui fonde 14 840,00 € au titre de 2025/2026, "
      "le barème de l'établissement étant de 1/3 en deçà de trois mois, 2/3 en deçà de six mois et "
      "100 % au-delà, et le contrat de Fall 2022 étant de 46 000,00 € pour soixante mois ; 2° à "
      "défaut de réponse avant le 19 octobre 2026, la fixation d'un échéancier de 300,00 € par "
      "mois à compter de janvier 2027, sans reconnaissance de dette ; 3° la suspension des effets "
      "de la mise en demeure — cessation de scolarité, rétention des documents — pendant l'examen "
      "du recours par l'Agence ; 4° l'écrit rappelant à BPCE VIE la délivrance de l'attestation de "
      "stage du 8 janvier au 5 juillet 2024 prévue par la convention signée par l'établissement, et "
      "la délivrance du certificat de scolarité du 17 décembre 2024 à nouveau nécessaire au "
      "renouvellement du titre de séjour.", "M")],
]


def corps(f):
    base = f.y + 10.5 * 0.83
    f.pg.insert_text((ML, base), "Madame,", fontname="Fr", fontsize=10.5)
    f.pg.insert_text((W - MR - FONTS["r"].text_length("Monsieur,", 10.5), base), "Monsieur,",
                     fontname="Fr", fontsize=10.5)
    f.y += 10.5 + 9.0
    for runs in FAITS:
        para(f, runs)
    f.y += 2
    para(f, [("Je n'ai sollicité aucune allocation directe : la prise en charge des frais de "
              "scolarité est seule en cause, la créance de l'établissement étant, aux écrits "
              "produits, engagée par l'organisme payeur sur les années 2022/2023 et 2023/2024. "
              "Les montants successifs réclamés pour la même période d'études — 12 000,00 €, puis "
              "4 000,00 €, puis 15 000,00 €, puis 7 500,00 €, puis 14 840,00 € — ne sont assortis "
              "d'aucune pièce de calcul.", "M")])
    f.y += 6
    para(f, [("Mes demandes.", "B")])
    for runs in DEMANDES:
        para(f, runs)
    f.y += 2
    para(f, [("Dans l'attente de vos réponses, que je souhaite recevoir avant le ", "M"),
             ("19 octobre 2026", "B"), (", date d'expiration du délai de dix jours, je vous prie "
             "d'agréer, Madame, Monsieur, l'expression de mes considérations distinguées.", "M")])
    f.y += 22
    ligne(f, "Calvin B. MINANG", 10.5, gras=True, droite=True, lead=13.0)
    ligne(f, "né le 2 mai 2002 à Libreville — n° étudiant 0305476", 9.2, droite=True, lead=11.5,
          col=GRIS)


# ---------------------------------------------------------------- bordereau
PIECES_INDEX = [
    ("A", "08/10/2026", "Étudiant", "Recours gracieux contre les décisions des 25/09/2024 et "
     "10/11/2025, procuration et accusé de remise", "M"),
    ("B", "04/02/2021", "ANBG", "Attestation de maintien de paiement n° 100326-21-MAINTIEN", "A"),
    ("C", "02/11/2021", "ANBG", "Attestation d'attribution n° 100057-22-ACCORD", "A"),
    ("D", "25/09 → 06/11/2025", "Campus France", "Filet de courriels « TR: Facture rejetée SFO "
     "N° 1281253 », quatre messages", "C"),
    ("E", "2024 → 2026", "ANBG", "Notifications et validations de la plateforme "
     "eBourse, horodatées — à imprimer depuis l'espace étudiant", "A"),
    ("F", "2024 et 2025", "SKEMA", "Attestation du registraire ; attestation "
     "d'assiduité", "S"),
    ("G", "2023 et 2024", "Campus France", "Bons de commande n° 677745 et n° 721622",
     "C"),
    ("H", "04/01/2024", "SKEMA", "Convention de stage SKEMA / BPCE, 08/01/2024 → 05/07/2024", "S"),
    ("I", "2024 et 2026", "SKEMA", "Rappel de droits scolaires 2024/2025 ; mise en "
     "demeure 2026-SK.D-0002", "S"),
    ("J", "2022 → 2025", "SKEMA", "Contrat d'inscription Fall 2022, dossier d'inscription et acte "
     "de cautionnement", "S"),
    ("K", "08/10/2026", "Étudiant", "Procuration donnée au porteur du dossier", "M"),
    ("L", "08/10/2026", "Étudiant", "Accusé de remise du recours, deux exemplaires", "M"),
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


def bordereau(f):
    f.new()
    f.pg.draw_line(fitz.Point(ML, MT + 1.0), fitz.Point(W - MR, MT + 1.0), width=0.6, color=NOIR)
    f.y = MT + 14
    ligne(f, "Bordereau des pièces jointes", 11.5, gras=True, lead=16.0)
    for ln in _lignes("Les pièces sont reproduites dans l'ordre des lettres, sans annotation ; les "
                      "mentions entre guillemets de la lettre en sont tirées textuellement.", 9.0, AVAIL):
        ligne(f, ln, 9.0, lead=11.6, col=GRIS)
    f.y += 13
    entetes = [("Cote", ML), ("Date", ML + 34), ("Émetteur", ML + 128), ("Pages", ML + 222),
               ("Objet", ML + 268)]
    for txt, x in entetes:
        f.pg.insert_text((x, f.y), txt, fontname="Fb", fontsize=8.2, color=GRIS)
    f.pg.draw_line(fitz.Point(ML, f.y + 5), fitz.Point(W - MR, f.y + 5), width=0.5, color=NOIR)
    f.y += 15
    del LIGNE_BORD[:]
    wobj = W - MR - (ML + 268)
    for cote, date, emet, objet, key in PIECES_INDEX:
        ln_obj = _lignes(objet, 8.6, wobj)
        hh = max(1, len(ln_obj)) * 10.6 + 4.6
        if f.y + hh > H - MB:
            f.new()
        pgn = f.d.page_count - 1
        base = f.y + 8.6 * 0.83
        f.pg.insert_text((ML, base), cote, fontname="Fb", fontsize=9.4, color=NOIR)
        f.pg.insert_text((ML + 34, base), date, fontname="Fr", fontsize=8.6)
        f.pg.insert_text((ML + 128, base), emet, fontname="Fr", fontsize=8.6)
        for i, ln in enumerate(ln_obj):
            f.pg.insert_text((ML + 270, base + i * 10.6), ln, fontname="Fr", fontsize=8.6)
        LIGNE_BORD.append([cote, pgn, base])
        f.y += hh
        f.pg.draw_line(fitz.Point(ML, f.y - 3.0), fitz.Point(W - MR, f.y - 3.0), width=0.25,
                       color=(0.62, 0.62, 0.65))
    return ML + 222


LIGNE_BORD = []


def _lignes(texte, size, width):
    fo = FONTS["r"]
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


# --------------------------------------------------------------------- annexe
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
            fin = len(actes)
            a, b = {"recours": (ix["1. RECOURS GRACIEUX"], ix["2. PROCURATION"]),
                    "procuration": (ix["2. PROCURATION"], ix["3. ACCUSÉ DE REMISE"]),
                    "recepisse": (ix["3. ACCUSÉ DE REMISE"], fin)}[spec]
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
    # pagination reportée sur le bordereau
    for k, (cote, pgn, y0) in enumerate(LIGNE_BORD):
        a = debut[cote]
        b = f.d.page_count if k == len(LIGNE_BORD) - 1 else debut[LIGNE_BORD[k + 1][0]] - 1
        if b < a:
            txt, col = "non jointe", NOIR
        elif b == a:
            txt, col = f"p. {a}", GRIS
        else:
            txt, col = f"p. {a} à {b}", GRIS
        f.d[pgn].insert_text((xcol, y0), txt, fontname="Fr", fontsize=8.6, color=col)
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
