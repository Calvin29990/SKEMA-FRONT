# -*- coding: utf-8 -*-
"""Lettre courte, deux pages au plus : les trois points de litige, sans développement.

Destinée à la Présidence de la République — le courrier long, avec ses treize pièces et
son bordereau, reste le dossier déposé en même temps. Même moteur, mêmes polices, mêmes
règles de forme que `lettre.py`, dont ce fichier importe tout (aucun style dupliqué).

    python3 skema-litige/outils/lettre-courte.py
"""
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "outils"))

import pymupdf as fitz                     # noqa: E402
import lettre as C                          # noqa: E402

LIGNE = C.ligne
PARA = C.para
STYLE = C.style
AVAIL = C.AVAIL
ML, MR, MT, MB = C.ML, C.MR, C.MT, C.MB
W, H = C.W, C.H
NOIR, GRIS = C.NOIR, C.GRIS

DEST = [("À la Présidence de la République,", True),
        ("Secrétariat général,", False),
        ("Commission technique des bourses", False),
        ("", False),
        ("À la Direction générale de", True),
        ("l'Agence nationale des bourses du Gabon", False)]

COPIE = ("Copie : la Direction du Service Financement et Bourses de Campus France ; la Direction "
         "générale de SKEMA Business School, service de la comptabilité étudiante ; la Direction "
         "des études de SKEMA Business School.")

CORPS = [
    "Le courrier détaillé joint, avec ses treize pièces cotées A à M, se réduit à trois points. "
    "Ils sont exposés ici sans autre développement que les dates et les textes qui les établissent.",

    ("1° La bourse a été supprimée pour une pièce que l'année de césure rendait impossible à "
     "produire.",
     "Le 25 septembre 2024 à 16:37, la plateforme eBourse de l'Agence nationale des bourses du "
     "Gabon (ANBG) a publié, sans nom de signataire ni visa ni référence à un texte : « La "
     "Commission Technique […] est au regret de vous annoncer la suppression de votre bourse pour "
     "le motif suivant : abs de releve de notes / perception de la bourse ». Or l'année 2023/2024 "
     "était une année de césure, sans examens : SKEMA Business School l'a écrit les 7 et 14 mai "
     "2024, et l'attestation du 7 mai 2024 porte que la licence était validée — « a validé son "
     "année de Licence 3 (60 crédits obtenus) sur l'année scolaire 2022-2023 ». La fiche « Mon "
     "Cursus » du compte 110584Z, tenue par l'ANBG, porte « LICENCE OBTENUE » pour 2022-2023 et « "
     "ANNEE DE CESURE » pour 2023-2024, avec le statut « Boursier » sur ces deux lignes, et aucune de ces lignes ne mentionne un redoublement."),

    ("2° Les deux refus sont fondés sur un texte abrogé, après validation de la pièce réclamée.",
     "Le 17 février 2025 à 11:06, la plateforme a enregistré la validation du document demandé ; à 11:11, cinq minutes plus tard, le recours a été déclaré irrecevable au motif « PARCOURS "
     "INSOUTENABLE (ARTICLE 4 DECRET 065) ». L'avis défavorable du 10 novembre 2025 à 15:47, sur "
     "la session 2025-2026, reprend ce motif. Le décret n° 0065/PR/MESRSIT du 12 février 2024 a "
     "pourtant été abrogé par le décret n° 0115/PR/MESRIT du 21 février 2025 (Journal officiel de "
     "la République gabonaise n° 56 bis du 26 février 2025). S'y ajoute que la session 2023-2024 "
     "avait été accordée après validation, le 17 août 2023 à 09:25, des relevés de notes du cycle "
     "précédent : l'ANBG a donc connu ces relevés avant de statuer."),

    ("3° La somme réclamée par SKEMA Business School n'est rattachée à aucun calcul.",
     "La mise en demeure n° 2026-SK.D-0002, du 7 octobre 2026 à 15:04, réclame 14 840,00 € au "
     "titre de l'année 2025/2026, avec paiement sous dix jours. Le seul contrat d'inscription du "
     "cycle — Fall 2022, dossier n° 2733904447 — fixe les frais de scolarité à « quarante six mille "
     "euros (46 000 €) », l'État gabonais se portant garant pour soixante mois au maximum. Les bons "
     "de commande de Campus France, 15 000,00 € pour 2022/2023 (n° 677745) et 16 000,00 € pour "
     "2023/2024 (n° 721622), ajoutés aux 15 000,00 € que SKEMA Business School a attestés le 21 "
     "septembre 2026, portent le total à ce plafond : ce sont l'année de rattachement de cette "
     "dernière tranche et son échéancier que les pièces ne disent pas. Le blocage vient de la "
     "facture n° 1281253, établie par SKEMA Business School à l'ordre de Campus France et rejetée "
     "le 25 septembre 2025 pour « Certificat de scolarité manquant ou non conforme », non d'un "
     "refus de payer."),
]

DEMANDES = [
    ("À la Présidence de la République, pour la Commission technique des bourses, et à la Direction "
     "générale de l'Agence nationale des bourses du Gabon", [
        "le réexamen sur le fond des décisions des 25 septembre 2024 et 10 novembre 2025, et la "
        "copie de la décision écrite portant suppression, avec sa date, son signataire et son visa ;",
        "la confirmation écrite, à SKEMA Business School et à Campus France, de ce qui reste pris "
        "en charge pour l'année 2025/2026, le cycle étant engagé depuis le 1er septembre 2022 et "
        "son terme fixé à décembre 2026."]),
    ("Au Service Financement et Bourses de Campus France", [
        "l'état de la facture n° 1281253 dans Chorus Pro et la désignation écrite de la pièce "
        "attendue — les trois attestations envoyées le 6 novembre 2025 n'ont appelé aucune "
        "observation ; l'émission du bon de commande 2024/2025, comme pour les deux années "
        "précédentes."]),
    ("À SKEMA Business School", [
        "le décompte des 14 840,00 €, la suspension des effets de la mise en demeure pendant "
        "l'examen du recours, et la délivrance du certificat de scolarité de l'année 2025/2026, "
        "nécessaire au titre de séjour avant le 30 janvier 2027 ;",
        "à défaut de réponse avant le 19 octobre 2026, la fixation d'un échéancier de 300,00 € par "
        "mois à compter de janvier 2027, sans reconnaissance de dette."]),
]

FIN = ("Je n'ai sollicité aucune somme pour moi-même et ne conteste aucune décision pédagogique. "
       "Les mesures de maîtrise des coûts annoncées en juillet 2025 portent sur les nouvelles "
       "attributions : ma bourse de l'État gabonais date de 2019 (session 2019-2020, référence "
       "WEXQTG) et mon cycle du 1er septembre 2022. Chaque point est établi par les pièces cotées A à M, dont le bordereau figure en page 7 du "
       "dossier joint. Je vous prie d'agréer, Mesdames, Messieurs, l'expression de mes "
       "considérations distinguées.")


def entete(f):
    LIGNE(f, "Calvin B. MINANG", 12.6, gras=True, lead=17.0)
    for t in C.EXPED:
        LIGNE(f, t, 9.9, lead=13.4)
    x = 318.0
    for txt, tete in DEST:
        if not txt:
            f.y += 6
            continue
        f.pg.insert_text((x, f.y + 9.4 * 0.80), txt, fontname="Fb" if tete else "Fr",
                         fontsize=9.4, color=NOIR)
        f.y += 12.6
    f.y = max(f.y, C.MT + 92.0)
    f.y += 10
    LIGNE(f, "Le 8 octobre 2026", 10.6, droite=True)
    f.y += 15
    PARA(f, "", size=10.6, lead=15.0, space=1.2, justifier=False,
         runs=[("Lettre recommandée avec accusé de réception ; remise en main propre, contre récépissé, à Libreville", "T")])
    PARA(f, "", size=10.6, lead=15.0, space=1.2, justifier=False,
         runs=[("Objet : ", "T"),
               ("dossier de bourse n° 110584Z — trois points de litige, bourse de l'État gabonais et frais "
               "de scolarité", "T")])
    f.pg.draw_line(fitz.Point(ML, f.y + 1.0), fitz.Point(W - MR, f.y + 1.0), width=0.6, color=NOIR)
    f.y += 12
    PARA(f, COPIE, size=9.6, lead=13.0, space=1.0, justifier=False, couleur=GRIS)
    f.y += 6


def corps(f):
    PARA(f, "", runs=[("Mesdames, Messieurs de la Présidence de la République, de l'Agence "
            "nationale des bourses du Gabon, du Service Financement et Bourses de Campus France et de "
            "SKEMA Business School,", "-")], size=10.8, lead=15.4, space=7.0, justifier=False)
    for i, bloc in enumerate(CORPS):
        if isinstance(bloc, tuple):
            titre, texte = bloc
            PARA(f, "", runs=[("%s " % titre, "T")], size=10.8, lead=15.0, space=1.6)
            PARA(f, texte, size=10.7, lead=15.0, space=6.4)
        else:
            PARA(f, bloc, lead=15.7, space=7.0)
    PARA(f, "", runs=[("Mes demandes.", "T")], size=10.8, lead=15.0, space=4.0)
    for titre, items in DEMANDES:
        PARA(f, "", runs=STYLE(titre) + [(" : ", "-")], size=10.7, lead=14.6, space=2.0)
        for n, it in enumerate(items):
            PARA(f, "", runs=[("%d° " % (n + 1), "-"), (it, "-")], size=10.6, lead=14.4,
                 space=1.8, width=AVAIL - 22)
        f.y += 2.6
    PARA(f, FIN, size=10.7, lead=14.8, space=5.0)
    if f.y + 30.0 > H - MB:
        f.new()
    else:
        f.y += min(22.0, H - MB - f.y - 26.0)
    LIGNE(f, "Calvin B. MINANG", 11.0, gras=True, droite=True, lead=14.0)
    LIGNE(f, "né le 2 mai 2002 à Libreville — n° étudiant 0305476 — dossier ANBG n° 110584Z",
          9.2, droite=True, lead=12.0, col=GRIS)


def main():
    f = C.Feuille()
    entete(f)
    corps(f)
    if f.d.page_count > 2:
        print("! la version courte dépasse deux pages :", f.d.page_count)
    dest = os.path.join(C.OUT, "LETTRE-COURTE-LITIGE-MINANG.pdf")
    f.save(dest)
    print(os.path.basename(dest), "—", f.d.page_count, "pages,",
          round(os.path.getsize(dest) / 1024), "Ko")
    f.d.close()


if __name__ == "__main__":
    main()
