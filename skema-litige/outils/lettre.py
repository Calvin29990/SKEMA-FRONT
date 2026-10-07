# -*- coding: utf-8 -*-
"""Lettre recommandée — exposé de la situation 2019-2026, demandes, bordereau, pièces A à L.

Police Lato, corps aéré. Pas d'italique : la couleur, sobre, marque seule l'auteur de l'acte.
  vert profond  = Agence nationale des bourses du Gabon
  bordeaux      = SKEMA Business School
  bleu nuit     = Campus France
  ardoise       = État gabonais et les textes qu'il prend
  noir adouci   = l'étudiant
Polices Lato (SIL Open Font License 1.1) dans skema-litige/polices/.
"""
import os
import re
import sys
import tempfile

import pymupdf as fitz

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "outils"))
import md2pdf  # noqa: E402

PO = os.path.join(BASE, "polices")
FFILE = {"r": os.path.join(PO, "Lato-Regular.ttf"), "b": os.path.join(PO, "Lato-Bold.ttf")}
FONTS = {k: fitz.Font(fontfile=v) for k, v in FFILE.items()}

W, H = 595.0, 842.0
ML, MR, MT, MB = 70.0, 60.0, 58.0, 58.0
AVAIL = W - ML - MR
OUT = os.path.join(BASE, "pdf")
PIECES = os.path.join(BASE, "pieces")

NOIR = (0.11, 0.12, 0.14)          # corps du texte
GRIS = (0.45, 0.46, 0.49)
COL = {"A": (0.05, 0.05, 0.07),    # Agence Nationale des Bourses du Gabon : noir
       "S": (0.45, 0.46, 0.49),     # SKEMA Business School : gris
       "C": (0.13, 0.24, 0.42),     # Campus France : bleu nuit
       "E": (0.58, 0.60, 0.63),     # État gabonais et ses textes : gris clair
       "T": NOIR,
       "-": NOIR}
PNAME = {k: "Fr" for k in COL}     # aucun italique, aucun gras dans le récit

MOTS = [  # les noms d'institutions sont écrits en entier ; seuls eux portent le registre
    ("Agence Nationale des Bourses du Gabon (ANBG)", "A"),
    ("Agence Nationale des Bourses du Gabon", "A"),
    ("Agence nationale des bourses du Gabon", "A"),
    ("Commission technique des bourses de l'ANBG", "A"),
    ("Commission technique des bourses", "A"),
    ("Commission technique de l'ANBG", "A"),
    ("la Commission technique", "A"),
    ("plateforme eBourse de l'ANBG", "A"),
    ("la plateforme eBourse", "A"),
    ("la plateforme de l'ANBG", "A"),
    ("plateforme eBourse", "A"),
    ("eBourse", "A"),
    ("ANBG", "A"),
    ("SKEMA BUSINESS SCHOOL", "S"),
    ("SKEMA Business School", "S"),
    ("SKEMA", "S"),
    ("Service Financement et Bourses", "C"),
    ("Campus France", "C"),
    ("Chorus Pro", "C"),
    ("Journal officiel de la République gabonaise", "E"),
    ("Journal officiel", "E"),
    ("décret n° 0115/PR/MESRIT", "E"),
    ("décret n° 0065/PR/MESRSIT", "E"),
    ("gouvernement gabonais", "E"),
    ("État gabonais", "E"),
    ("l'État", "E"),
]
RE = re.compile("|".join("(?:%s)" % re.escape(m) for m, _ in MOTS))
KEY = dict(MOTS)


class Feuille:
    def __init__(self):
        self.d = fitz.open()
        self.pg = None
        self.new()

    def new(self):
        self.pg = self.d.new_page(width=W, height=H)
        self.pg.insert_font(fontname="Fr", fontfile=FFILE["r"])
        self.pg.insert_font(fontname="Fb", fontfile=FFILE["b"])
        self.y = MT

    def save(self, path):
        try:
            self.d.subset_fonts()
        except Exception:
            pass
        self.d.save(path, deflate=True, garbage=4, clean=True)


def style(texte):
    """Découpe le récit en suites (texte, registre). L'élision reste collée au nom."""
    out, last = [], 0
    for m in RE.finditer(texte):
        if m.start() > last:
            out.append([texte[last:m.start()], "-"])
        out.append([m.group(0), KEY[m.group(0)]])
        last = m.end()
    if last < len(texte):
        out.append([texte[last:], "-"])
    for i in range(len(out) - 1):
        txt = out[i][0]
        if txt.rstrip() != txt or not txt:
            continue
        if txt.endswith(("'", "’")) and len(txt) > 1 and txt[-2].isalpha() \
                and out[i + 1][0][:1].isalpha():
            out[i + 1][0] = txt + out[i + 1][0]
            out[i][0] = ""
    return [(a, b) for a, b in out if a]


def para(f, texte, size=11.0, lead=16.4, space=8.0, width=None, justifier=True, runs=None,
         couleur=None):
    """Paragraphe aéré, justifié, ponctuation collée au mot, noms d'acteurs colorés."""
    width = width or AVAIL
    ws = FONTS["r"].text_length(" ", size)
    mots = []
    ouv = ""
    for txt, key in (runs if runs is not None else style(texte)):
        fname = PNAME[key]
        fo = FONTS["b"] if fname == "Fb" else FONTS["r"]
        col = couleur or COL[key]
        for mot in txt.split():
            if mot in ("(", "["):          # l'ouvrant se colle au mot suivant
                ouv = mot
                continue
            if ouv:
                mot, ouv = ouv + mot, ""
            if mots and mot[0] in ",.;:!?»)" and mot not in (":", ";", "!", "?", "»") \
                    and mots[-1][0][-1] not in "(«":
                mots[-1][0] += mot
                mots[-1][3] = mots[-1][4].text_length(mots[-1][0], size)
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
        y = f.y + size * 0.80
        ecart = 0.0
        if justifier and i < len(lignes) - 1 and len(line) > 1:
            ecart = (width - lw) / (len(line) - 1)
        x = ML
        for mot, fname, col, wd, _fo in line:
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


def ligne(f, texte, size=11.0, gras=False, col=NOIR, x=None, droite=False, lead=None):
    fo = FONTS["b"] if gras else FONTS["r"]
    xx = (W - MR - fo.text_length(texte, size)) if droite else (x if x is not None else ML)
    f.pg.insert_text((xx, f.y + size * 0.80), texte, fontname="Fb" if gras else "Fr",
                     fontsize=size, color=col)
    f.y += lead if lead else size + 4.2


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
         "Étudiant en 2ᵉ année de master — n° 0305476",
         "Dossier de bourse n° 110584Z"]

DEST = [("À la Direction générale de", True),
        ("l'Agence Nationale des Bourses du Gabon", False),
        ("et à la Commission technique des bourses", False),
        ("", False),
        ("À la Direction du Service Financement", True),
        ("et Bourses, Campus France,", False),
        ("", False),
        ("À la Direction générale de", True),
        ("SKEMA Business School,", False),
        ("service de la comptabilité étudiante", False),
        ("", False),
        ("Copie pour information à la Direction", False),
        ("des études", False)]


def entete(f):
    ligne(f, "Calvin B. MINANG", 12.6, gras=True, lead=17.0)
    for t in EXPED:
        ligne(f, t, 9.9, lead=13.4)
    f.y += 22
    x = 318.0
    for txt, tete in DEST:
        if not txt:
            f.y += 6
            continue
        f.pg.insert_text((x, f.y + 9.4 * 0.80), txt, fontname="Fb" if tete else "Fr",
                         fontsize=9.4, color=NOIR)
        f.y += 12.6
    f.y += 18
    ligne(f, "Le 8 octobre 2026", 10.6, droite=True)
    f.y += 16
    para(f, "", size=10.8, lead=15.0, space=1.5, justifier=False,
         runs=[("Lettre recommandée avec accusé de réception", "T")])
    para(f, "", size=10.8, lead=15.0, space=1.5, justifier=False,
         runs=[("Objet : ", "T"),
               ("Bourse d'État, prise en charge des frais de scolarité et facturation — exposé de "
                "la situation et demandes", "T")])
    para(f, "Un seul exemplaire par destinataire. Douze pièces jointes, cotées A à L, bordereau "
            "en fin de lettre.", size=10.8, lead=15.0, space=1.5, justifier=False)
    f.pg.draw_line(fitz.Point(ML, f.y + 2), fitz.Point(W - MR, f.y + 2), width=0.6, color=NOIR)
    f.y += 18


# ---------------------------------------------------------------------- récit
RIT = [
    "Je me permets de vous adresser un seul courrier à trois destinataires, parce que les mêmes faits "
    "engagent à la fois l'Agence Nationale des Bourses du Gabon (ANBG), qui m'a accordé la bourse, le "
    "Service Financement et Bourses de Campus France, qui règle les frais de scolarité, et SKEMA "
    "Business School, l'école où j'étudie, qui me réclame aujourd'hui 14 840,00 € pour l'année "
    "2025/2026. Je suis gabonais, boursier de l'État depuis 2019, et j'achève en décembre 2026 le "
    "Programme Grande École de SKEMA Business School (le diplôme principal de l'école, de niveau "
    "master, préparé en cinq années après le baccalauréat). Les faits rapportés ci-dessous sont ceux "
    "qu'enregistrent vos documents respectifs ; les passages entre guillemets en reproduisent "
    "exactement le texte, et les pièces A à L les accompagnent.",

    "Ce qui est en cause est la prise en charge des frais de scolarité, c'est-à-dire la somme versée à "
    "SKEMA Business School pour que l'étudiant s'inscrive, suive les cours et se présente aux examens. "
    "La bourse nationale comprend également une allocation mensuelle, destinée au logement et à la vie "
    "courante : je ne la sollicite pas, et ce courrier ne la concerne pas. Seule la question des frais "
    "de scolarité est posée, parce que ces frais, réglés directement par l'organisme payeur pour "
    "2022/2023 puis pour 2023/2024, sont aujourd'hui réclamés à l'étudiant pour 2025/2026.",

    "Tout a commencé par les classes préparatoires. Admis au Groupe Scolaire La Résidence de "
    "Casablanca, en filière économique et commerciale, j'ai obtenu la bourse nationale pour l'année "
    "2019-2020, sous la référence WEXQTG. Le 1er février 2021, la Commission technique des bourses de "
    "l'ANBG a confirmé cette bourse pour l'année suivante, en catégorie C (l'échelon qui fixe le "
    "montant mensuel versé à l'étudiant). L'attestation de maintien de paiement du 4 février 2021 "
    "porte « montant mensuel [...] 165 000 FCFA », mentionne « Classes Préparatoires 2 au/en MAROC / "
    "CASABLANCA » et « valable jusqu'au 30/09/2021 », et précise que le renouvellement est conditionné "
    "à la production des résultats de l'année. Le 2 novembre 2021, l'ANBG a accordé la bourse pour "
    "l'année 2021/2022, établissement IPESUP, France/Paris, « pour une durée : 1 année(s), du "
    "01/09/2021 au 31/08/2022 » — alors que les sessions suivantes, sur la même plateforme, portent "
    "« deux années » (pièces B, C, E).",

    "Admis à SKEMA Business School en 2022 par le concours BCE (le concours commun d'entrée en école "
    "de commerce), sous le numéro de candidat 21446, je me suis inscrit le 1er septembre 2022 en "
    "troisième année du cycle, notée L3 dans les documents de SKEMA Business School. Le dossier d'inscription "
    "n° 2733904447 comporte un acte de cautionnement : l'État gabonais s'y porte garant du paiement de "
    "mes études, pour un maximum de « quarante six mille euros (46 000 €) » et une durée de « soixante "
    "(60) mois », soit cinq ans, la durée normale du parcours jusqu'au master. Ce contrat de 2022 est "
    "le seul contrat signé pour l'ensemble du cycle ; son article 4.4 prévoit qu'il est rallongé si la "
    "scolarité se prolonge. Le 25 août 2022, SKEMA Business School écrivait déjà : « Concernant la "
    "facturation, je transfère votre mail à la comptabilité étudiante. » (pièce J).",

    "Encore faut-il expliquer comment SKEMA Business School est payée, puisque tout le reste en dépend. Pour les "
    "boursiers du gouvernement gabonais, l'étudiant ne paie pas : SKEMA Business School établit une "
    "facture à l'ordre de Campus France et la dépose sur Chorus Pro (le portail public par lequel les "
    "administrations reçoivent et règlent leurs factures) ; Campus France vérifie les pièces, puis "
    "engage le paiement au profit de SKEMA Business School. Cette règle a été écrite par Campus France le 24 "
    "janvier 2023 : « Nous vous invitons à établir une facture à l'ordre de campus France et à la "
    "déposer sur Chorus Pro », avec cette précision « Dans l'hypothèse où l'étudiant aurait versé un "
    "acompte, merci de bien vouloir le faire apparaître clairement ». Le même jour, Campus France a "
    "émis le bon de commande n° 677745 pour mon dossier, objet « FRAIS DE FORMATION 22/23 », "
    "fournisseur SKEMA BUSINESS SCHOOL n° 35025, d'un montant de 15 000,00 € ; la comptabilité "
    "étudiante de SKEMA Business School en a accusé réception le 25 janvier 2023 à 09:43. Un bon de "
    "commande est l'engagement de payer pris par l'organisme auprès de SKEMA Business School (pièces G, J).",

    "L'année 2022/2023 a été difficile : en juillet 2023, les examens de la troisième année n'ont pas "
    "été validés. J'ai alors demandé à effectuer une année de césure — c'est une période courante dans "
    "la plupart des écoles, où l'étudiant interrompt les cours une année pour faire un stage en "
    "entreprise, en restant inscrit et en acquittant les frais de scolarité. Le 27 octobre 2023, SKEMA "
    "Business School a écrit : « Votre demande pour effectuer la césure à partir de janvier 2024 a été "
    "acceptée. Je viens de mettre à jour votre dossier. » Cette année-là, je n'avais ni cours ni "
    "examens, donc pas de relevé de notes : une césure se valide par l'attestation de stage délivrée "
    "par l'entreprise. Le 4 janvier 2024, SKEMA Business School a signé avec BPCE VIE la convention de "
    "stage fixant la mission : « Le stage se déroulera du 08/01/2024 au 05/07/2024 », cinq jours ouvrés "
    "par semaine, à Paris ; l'entreprise m'a remis l'attestation de stage correspondante (pièce H).",

    "Le 14 mai 2024, le service de la scolarité de SKEMA Business School a certifié mon parcours par "
    "une attestation officielle : « 2023/2024 L3/M1 Paris Fall 23 / Césure Spring 24 ; 2024/2025 M1 "
    "Césure Fall 24 / Raleigh Spring 25 ; 2025/2026 PGE M2 ». Pour la lire : L3, M1 et M2 sont la "
    "troisième année du cycle et les deux années de master ; « Fall » et « Spring » désignent, dans les "
    "documents de SKEMA Business School, le premier semestre de l'année, de septembre à décembre, et le "
    "second, de janvier à mai ; « Césure » signale le semestre passé en entreprise. Cette attestation "
    "dit donc, en clair, que l'année 2023/2024 a été consacrée au stage et que j'étais bien inscrit "
    "cette année-là (pièce F).",

    "Campus France n'a d'ailleurs pas cessé de prendre en charge cette année de césure : le 6 mai "
    "2024, il a émis le bon de commande n° 721622, dossier 110584Z, objet « POUR LE COMPTE DE L'ANBG "
    "FRAIS FORMATION 2023 2024 », d'un montant de 16 000,00 €. Cet acte porte sur l'année 2023/2024 : "
    "il est donc postérieur de six mois et un jour à la décision de l'ANBG retirant la bourse pour "
    "cette même année (pièce G).",

    "Cette suppression est le point de départ du litige. Le 25 septembre 2024 à 16:37, la plateforme "
    "eBourse de l'ANBG (l'espace où l'étudiant dépose ses pièces et suit l'avancement de son dossier) a "
    "enregistré la suppression de ma bourse au motif « abs de releve de notes / perception de la "
    "bourse », c'est-à-dire l'absence de relevé de notes. Ce relevé ne pouvait pas exister, puisque "
    "l'année en cause était une année de césure certifiée par SKEMA Business School, sans examens. "
    "J'ai produit l'attestation du 14 mai 2024, puis les documents demandés en janvier 2025. Le 17 "
    "février 2025 à 11:06, la plateforme de l'ANBG a validé la pièce ; cinq minutes plus tard, à 11:11, "
    "elle enregistrait l'irrecevabilité de mon recours, sous le motif « PARCOURS INSOUTENABLE "
    "(ARTICLE 4 DECRET 065) ». Une irrecevabilité est un refus d'examiner le dossier sur le fond, pour "
    "un motif de forme ou de réglementation (pièces E, F).",

    "Le texte invoqué n'est plus en vigueur. Le décret n° 0065/PR/MESRSIT du 12 février 2024 a été "
    "abrogé par le décret n° 0115/PR/MESRIT du 21 février 2025, dont l'article 4 dispose qu'il "
    "« abroge[t] toutes dispositions antérieures contraires, notamment celles du décret n° 0065/"
    "PR/MESRSIT du 12 février 2024 » (Journal officiel de la République gabonaise n° 56 bis du 26 "
    "février 2025). La décision du 17 février 2025 a été prise la veille de cette abrogation ; en "
    "revanche, l'avis défavorable du 10 novembre 2025 à 15:47, référence CA24B3, qui reprend le même "
    "motif de parcours, vise un texte abrogé depuis huit mois, sans référence à celui alors en vigueur. "
    "Cet avis invitait du reste à renouveler la demande. Vingt-neuf jours plus tard, le 9 décembre "
    "2025, SKEMA Business School a certifié par écrit que j'avais assisté aux cours et aux examens de "
    "l'année (pièce F).",

    "Le dossier de facturation a buté sur la même difficulté, dans l'autre sens. La facture "
    "n° 1281253, établie par SKEMA Business School pour l'année 2024/2025, a été rejetée le 25 "
    "septembre 2025 à 12:15 par le Service Financement et Bourses de Campus France, motif « Certificat "
    "de scolarité manquant ou non conforme », avec injonction de « remettre le « Bon à payer » ». Le 6 "
    "octobre 2025 à 15:19, ce service a demandé « le relevé de notes de l'année 2023-2024 ou un "
    "certificat de scolarité daté d'après le 1er septembre 2023 » — le relevé de notes de l'année de "
    "césure ne pouvait pas davantage être produit en 2025 qu'en 2024. Le 29 octobre 2025 à 12:34, il a "
    "écarté « le document du 26/07 non conforme », sans indiquer la pièce attendue. J'ai répondu le 6 "
    "novembre 2025 à 12:01 en joignant trois attestations de SKEMA Business School, dont celle du 14 "
    "mai 2024 relative à la césure. Ce message n'a reçu aucune observation, et la facture n'est pas "
    "allée à son terme (pièce D).",

    "Pour l'année 2025/2026, la somme réclamée a changé cinq fois de montant. Le 14 novembre 2024, la "
    "comptabilité étudiante de SKEMA Business School a rappelé une première échéance de 12 000,00 € ; "
    "le 15 janvier 2025, la facture n° 22223502, intitulée « Master 2 », portait 15 000,00 € ; le 20 "
    "février 2025, une pièce comptable portait 4 000,00 € ; le 30 septembre 2026, 7 500,00 € ; le 5 "
    "octobre 2026, un document comptable portait 14 840,00 €. Le 7 octobre 2026 à 15:04, la mise en "
    "demeure n° 2026-SK.D-0002 — la relance formale qui fait courir un délai avant poursuites — a "
    "réclamé ce solde de 14 840,00 € « au titre de l'année 2025/2026 », avec paiement sous dix jours, "
    "en précisant que « l'absence ou la cessation de prise en charge par un organisme tiers ne vous "
    "libère pas », sous menace de procédure et de cessation définitive de scolarité. Aucun de ces "
    "montants n'est accompagné d'un calcul, et l'écart avec le plafond de 46 000,00 € prévu par le "
    "contrat de 2022 n'est justifié par aucune pièce (pièces I, J).",

    "Le 7 octobre 2026 à 21:06, la plateforme eBourse de l'ANBG affichait, pour la session 2025-2026 "
    "de mon dossier et la référence externe 110584Z : « DÉCISION : AVIS DÉFAVORABLE » et « VOUS ÊTES "
    "NON BOURSIER », avec l'arborescence des sessions CA24B3, 1LMK24, 2E4C0B, LDPMRC, PNPXWG, 4E0O00, "
    "WEXQTG. Ma situation vis-à-vis de la bourse est donc celle d'un non-boursier, alors que SKEMA "
    "Business School a émis et transmis les factures à Campus France, a certifié mon assiduité, et me "
    "scolarise pour l'année en cours (pièces E, F, I).",
]

DEMANDES = [
    ("À l'Agence Nationale des Bourses du Gabon (ANBG)", "A", [
        "la transmission du présent dossier à la Commission technique des bourses, pour qu'il soit "
        "réexaminé sur le fond ;",
        "la prise en compte du fait que mon cycle est engagé depuis le 1er septembre 2022, et que les "
        "mesures de maîtrise des coûts concernent les nouvelles attributions ;",
        "la communication de la pièce, de la date et de la signature qui fondent l'avis défavorable du "
        "10 novembre 2025, ainsi que le détail du calcul des frais de scolarité pris en charge pour "
        "2024/2025 et pour 2025/2026 ;",
        "la confirmation écrite, à SKEMA Business School et à Campus France, de ce qui reste pris en "
        "charge pour l'année 2025/2026 ;",
        "la copie certifiée au guichet de la décision indiquant pour combien d'années la bourse du "
        "cycle de master a été accordée, la plateforme portant « 1 année(s) » pour 2021 et « deux "
        "années » pour 2023."]),
    ("Au Service Financement et Bourses de Campus France", "C", [
        "l'état de la facture n° 1281253 dans Chorus Pro à la date de votre réponse et, si elle doit "
        "être représentée, la désignation écrite de la pièce exacte attendue : les trois attestations "
        "envoyées le 6 novembre 2025 n'ont appelé aucune observation ;",
        "l'émission du bon de commande 2024/2025, les années 2022/2023 et 2023/2024 ayant donné lieu "
        "aux bons n° 677745 et n° 721622, ce dernier portant « POUR LE COMPTE DE L'ANBG FRAIS "
        "FORMATION 2023 2024 » ;",
        "une attestation adressée à SKEMA Business School rappelant la règle posée le 24 janvier 2023 "
        "— facture à l'ordre de Campus France, déposée sur Chorus Pro — et l'état des paiements faits à "
        "SKEMA Business School pour le dossier 110584Z ;",
        "que les demandes de pièces adressées à SKEMA Business School le soient en même temps qu'à "
        "l'étudiant, et non après le rejet."]),
    ("À SKEMA Business School", "S", [
        "la communication de la pièce qui fonde 14 840,00 € au titre de l'année 2025/2026, et le "
        "rapprochement avec le contrat de 2022, de 46 000,00 € pour une durée de soixante mois ;",
        "la suspension des effets de la mise en demeure — interruption de scolarité et rétention des "
        "documents — pendant l'examen du recours par l'ANBG ;",
        "à défaut de réponse avant le 19 octobre 2026, date d'expiration du délai de dix jours, la "
        "fixation d'un échéancier de 300,00 € par mois à compter de janvier 2027, sans reconnaissance "
        "de dette ;",
        "la délivrance du certificat de scolarité de l'année 2025/2026, nécessaire au renouvellement de "
        "mon titre de séjour avant son expiration, le 30 janvier 2027."]),
]

FIN = [
    "Je n'ai sollicité aucune somme pour moi-même : ce dossier porte uniquement sur l'argent qui doit "
    "être versé à SKEMA Business School. Le terme du cycle est prévu en décembre 2026. En vous "
    "remerciant de l'attention portée à cet exposé, je vous prie d'agréer, Madame, Monsieur, "
    "l'expression de mes considérations distinguées.",
]


def corps(f):
    base = f.y + 11.0 * 0.80
    f.pg.insert_text((ML, base), "Madame,", fontname="Fr", fontsize=11.0, color=NOIR)
    f.pg.insert_text((W - MR - FONTS["r"].text_length("Monsieur,", 11.0), base), "Monsieur,",
                     fontname="Fr", fontsize=11.0, color=NOIR)
    f.y += 11.0 + 11.0
    for texte in RIT:
        para(f, texte)
    f.y += 2
    para(f, "", runs=[("Mes demandes.", "T")], space=7.0)
    for titre, key, items in DEMANDES:
        para(f, "", runs=style(titre) + [(",", key), (" je demande :", "-")], lead=15.4, space=3.5)
        for n, it in enumerate(items):
            para(f, "", runs=[("%d° " % (n + 1), "-"), (it, "-")], size=10.7, lead=15.4,
                 space=2.5, width=AVAIL - 22)
        f.y += 4.0
    for texte in FIN:
        para(f, texte)
    f.y += 26
    ligne(f, "Calvin B. MINANG", 11.0, gras=True, droite=True, lead=14.0)
    ligne(f, "né le 2 mai 2002 à Libreville — n° étudiant 0305476", 9.2, droite=True, lead=12.0,
          col=GRIS)


# ------------------------------------------------------------------ bordereau
PIECES_INDEX = [
    ("A", "08/10/2026", "Étudiant", "Recours gracieux contre les décisions des 25/09/2024 et "
     "10/11/2025, avec procuration et accusé de remise", "A"),
    ("B", "04/02/2021", "ANBG", "Attestation de maintien de paiement n° 100326-21-MAINTIEN", "A"),
    ("C", "02/11/2021", "ANBG", "Attestation d'attribution de bourse n° 100057-22-ACCORD", "A"),
    ("D", "25/09 → 06/11/2025", "Campus France", "Échanges autour de la facture n° 1281253 rejetée, "
     "quatre messages", "C"),
    ("E", "2024 → 2026", "ANBG", "Notifications et validations de la plateforme eBourse, avec date "
     "et heure — à imprimer depuis l'espace étudiant", "A"),
    ("F", "2024 et 2025", "SKEMA Business School", "Attestation du service de la scolarité du "
     "14/05/2024 ; attestation d'assiduité du 09/12/2025", "S"),
    ("G", "2023 et 2024", "Campus France", "Bons de commande n° 677745 du 24/01/2023 et "
     "n° 721622 du 06/05/2024",
     "C"),
    ("H", "04/01/2024", "SKEMA Business School", "Convention de stage avec BPCE VIE, du 08/01/2024 "
     "au 05/07/2024", "S"),
    ("I", "2024 et 2026", "SKEMA Business School", "Rappel de frais de scolarité du "
     "14/11/2024 ; mise en demeure n° 2026-SK.D-0002 du 07/10/2026", "S"),
    ("J", "2022 → 2025", "SKEMA Business School", "Contrat d'inscription, dossier d'inscription et "
     "acte de cautionnement de l'État", "S"),
    ("K", "08/10/2026", "Étudiant", "Procuration donnée à la personne qui remet le dossier", "-"),
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
    f.y = MT + 15
    ligne(f, "Bordereau des pièces jointes", 12.0, gras=True, lead=17.5)
    for ln in _lignes("Les pièces suivent, dans l'ordre des lettres, reproduites sans annotation. Les "
                      "passages entre guillemets de la lettre en sont tirés textuellement.", 9.4,
                      AVAIL, FONTS["r"]):
        ligne(f, ln, 9.4, lead=12.4, col=GRIS)
    f.y += 12
    xs = {"cote": ML, "date": ML + 30, "emet": ML + 122, "pag": ML + 226, "obj": ML + 272}
    for txt, x in (("Cote", xs["cote"]), ("Date", xs["date"]), ("Établie par", xs["emet"]),
                   ("Pages", xs["pag"]), ("Objet", xs["obj"])):
        f.pg.insert_text((x, f.y), txt, fontname="Fb", fontsize=8.5, color=GRIS)
    f.pg.draw_line(fitz.Point(ML, f.y + 5), fitz.Point(W - MR, f.y + 5), width=0.5, color=NOIR)
    f.y += 16
    del LIGNE_BORD[:]
    wobj = W - MR - xs["obj"]
    for cote, date, emet, objet, key in PIECES_INDEX:
        ln_obj = _lignes(objet, 8.9, wobj, FONTS["r"])
        hh = max(1, len(ln_obj)) * 11.2 + 5.0
        if f.y + hh > H - MB:
            f.new()
        base = f.y + 8.9 * 0.80
        f.pg.insert_text((xs["cote"], base), cote, fontname="Fb", fontsize=9.6, color=NOIR)
        f.pg.insert_text((xs["date"], base), date, fontname="Fr", fontsize=8.9, color=NOIR)
        f.pg.insert_text((xs["emet"], base), emet, fontname="Fr", fontsize=8.9, color=COL.get(key, NOIR))
        for i, ln in enumerate(ln_obj):
            f.pg.insert_text((xs["obj"], base + i * 11.2), ln, fontname="Fr", fontsize=8.9,
                             color=NOIR)
        LIGNE_BORD.append([cote, f.d.page_count - 1, base])
        f.y += hh
        f.pg.draw_line(fitz.Point(ML, f.y - 3.2), fitz.Point(W - MR, f.y - 3.2), width=0.25,
                       color=(0.66, 0.68, 0.71))
    return xs["pag"]


# ---------------------------------------------------------------------- annexes
def annexes(f, xcol):
    # le recours, la procuration et l'accusé sont rendus dans la même police que la lettre
    md2pdf.FFILE = {"r": FFILE["r"], "b": FFILE["b"], "i": FFILE["r"], "bi": FFILE["b"]}
    md2pdf.FONTS = {"r": FONTS["r"], "b": FONTS["b"], "i": FONTS["r"], "bi": FONTS["b"]}
    rtmp = os.path.join(tempfile.gettempdir(), "actes-lettre.pdf")
    src = open(os.path.join(BASE, "PARENTS-ANBG", "RECOURS-GRACIEUX-ANBG.md"), encoding="utf-8").read()
    a0 = src.index("# 1. RECOURS GRACIEUX")
    a1 = src.index("# 4. CHEMISE") if "# 4. CHEMISE" in src else len(src)
    md2pdf.render(src[a0:a1].rstrip() + "\n", rtmp, "")
    actes = fitz.open(rtmp)
    ix = {}
    for k in ("1. RECOURS GRACIEUX", "2. PROCURATION", "3. ACCUSÉ DE REMISE"):
        j = next((i for i, pg in enumerate(actes)
                  if k in pg.get_text().replace("\xa0", " ")), None)
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
        txt = "non jointe" if b < a else (f"p. {a}" if b == a else f"p. {a} à {b}")
        f.d[pgn].insert_text((xcol, y0), txt, fontname="Fr", fontsize=8.9, color=NOIR)
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
