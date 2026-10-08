# -*- coding: utf-8 -*-
"""Une page : les trois points de litige et les demandes, rien d'autre.

C'est l'entrée du dossier — celle qu'on lit debout, au guichet comme dans un courriel.
L'exposé détaillé, le bordereau et les treize pièces restent dans `HISTORIQUE-DOCUMENTE-
2019-2026-MINANG.pdf` (lettre.py). Mêmes polices, mêmes marges, mêmes couleurs : ce fichier
importe `lettre.py` et ne redéfinit aucune règle de forme.

    python3 skema-litige/outils/lettre-une-page.py
"""
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "outils"))

import pymupdf as fitz                     # noqa: E402
import lettre as C                         # noqa: E402

LIGNE = C.ligne
PARA = C.para
STYLE = C.style
AVAIL = C.AVAIL
W, H = C.W, C.H
NOIR, GRIS = C.NOIR, C.GRIS

DEST = [("Le 8 octobre 2026", False),
        ("Lettre recommandée avec accusé de", False),
        ("réception ; remise en main propre,", False),
        ("contre récépissé, à Libreville", False)]

DESTIN = ("Destinataires : la Présidence de la République (Secrétariat général, Commission "
          "technique des bourses) ; la Direction générale de l'Agence nationale des bourses du "
          "Gabon ; le Service Financement et Bourses de Campus France ; SKEMA Business School "
          "(direction générale et comptabilité étudiante).")

ENTAME = ("Un seul courrier à quatre destinataires : les mêmes faits les engagent. Il tient en "
          "trois points, établis par les pièces cotées A à M jointes au présent envoi.")

POINTS = [
    ("1° La bourse a été supprimée pour une pièce impossible à produire.",
     "Le 25 septembre 2024 à 16:37, la plateforme eBourse de l'Agence nationale des bourses du "
     "Gabon (ANBG) a publié, sans signataire, sans visa ni référence à un texte : « suppression de "
     "votre bourse pour le motif suivant : abs de releve de notes / perception de la bourse ». Or "
     "l'année visée était une césure, sans examens, et la licence était validée : « a validé son "
     "année de Licence 3 (60 crédits obtenus) sur l'année scolaire 2022-2023 » (SKEMA Business "
     "School, 7 mai 2024). La fiche « Mon Cursus » du compte 110584Z porte « LICENCE OBTENUE » "
     "(2022-2023) et « ANNEE DE CESURE » (2023-2024), sans redoublement."),
    ("2° Les deux refus visent un texte abrogé, cinq minutes après la validation de la pièce.",
     "Le 17 février 2025 à 11:06, la plateforme a enregistré la validation du document demandé ; à "
     "11:11, le recours a été déclaré irrecevable pour « PARCOURS INSOUTENABLE (ARTICLE 4 DECRET "
     "065) », motif repris par l'avis défavorable du 10 novembre 2025 à 15:47. Le décret "
     "n° 0065/PR/MESRSIT du 12 février 2024 a pourtant été abrogé par le décret "
     "n° 0115/PR/MESRIT du 21 février 2025 (Journal officiel n° 56 bis du 26 février 2025)."),
    ("3° La somme réclamée n'est rattachée à aucun calcul.",
     "La mise en demeure de SKEMA Business School n° 2026-SK.D-0002, du 7 octobre 2026 à 15:04, "
     "réclame 14 840,00 € pour l'année 2025/2026 sous dix jours. Le seul contrat du cycle (Fall "
     "2022, dossier n° 2733904447) fixe les frais à « quarante six mille euros (46 000 €) » et "
     "l'État gabonais n'en garantit le paiement que soixante mois au maximum : les deux bons de "
     "commande de Campus France (15 000,00 € n° 677745, 16 000,00 € n° 721622) ajoutés aux "
     "15 000,00 € attestés le 21 septembre 2026 portent le total à ce plafond. Le blocage vient de "
     "la facture n° 1281253, rejetée le 25 septembre 2025 pour « Certificat de scolarité manquant "
     "ou non conforme », non d'un refus de payer."),
]

DEMANDES = [
    ("À l'Agence nationale des bourses du Gabon",
     "réexamen sur le fond, par la Commission technique des bourses, des décisions des 25 septembre "
     "2024 et 10 novembre 2025 ; copie de la décision écrite de suppression, avec sa date, son "
     "signataire et son visa ; confirmation écrite, à SKEMA Business School et à Campus France, de "
     "ce qui reste pris en charge pour 2025/2026."),
    ("Au Service Financement et Bourses de Campus France",
     "état de la facture n° 1281253 dans Chorus Pro, désignation écrite de la pièce attendue et "
     "émission du bon de commande 2024/2025, comme pour les deux années précédentes."),
    ("À SKEMA Business School",
     "décompte des 14 840,00 € ; suspension des effets de la mise en demeure pendant l'examen du "
     "recours ; certificat de scolarité 2025/2026, le titre de séjour devant être renouvelé avant le "
     "30 janvier 2027 ; à défaut de réponse avant le 19 octobre 2026, échéancier de 300,00 € par "
     "mois à compter de janvier 2027, sans reconnaissance de dette."),
]

FIN = ("Je n'ai sollicité aucune somme pour moi-même et ne conteste aucune décision pédagogique. "
       "Le cycle, engagé le 1er septembre 2022, s'achève en décembre 2026 ; la bourse de l'État "
       "gabonais date de 2019 (référence WEXQTG) et les mesures de maîtrise des coûts annoncées en "
       "juillet 2025 visent les nouvelles attributions.")

PIED = ("Exposé détaillé de six pages, bordereau en page 7 et pièces A à M reproduites sans "
        "annotation : joints au présent envoi.")


def main():
    f = C.Feuille()
    LIGNE(f, "Calvin B. MINANG", 12.4, gras=True, lead=15.4)
    for t in C.EXPED:
        LIGNE(f, t, 9.6, lead=12.0)
    x = 318.0
    for txt, tete in DEST:
        f.pg.insert_text((x, f.y - 12.0 * (len(C.EXPED) + 1) + 12.6), txt,
                         fontname="Fb" if tete else "Fr", fontsize=8.8, color=NOIR)
    PARA(f, DESTIN, size=9.4, lead=12.4, space=1.4, justifier=False)
    f.pg.draw_line(fitz.Point(C.ML, f.y + 1.0), fitz.Point(W - C.MR, f.y + 1.0), width=0.6,
                   color=NOIR)
    f.y += 9
    PARA(f, "", size=10.5, lead=14.0, space=5.0, justifier=False,
         runs=[("Objet : ", "T"),
               ("bourse de l'État gabonais et frais de scolarité — trois points de litige et "
                "demandes", "T")])
    PARA(f, "Mesdames, Messieurs,", size=10.4, lead=14.0, space=4.0, justifier=False)
    PARA(f, ENTAME, size=10.3, lead=13.5, space=4.4)
    for titre, texte in POINTS:
        PARA(f, "", runs=[(titre, "T")], size=10.3, lead=13.4, space=1.0)
        PARA(f, texte, size=10.3, lead=13.4, space=3.2)
    for titre, texte in DEMANDES:
        PARA(f, "", runs=STYLE(titre) + [(" : ", "-"), (texte, "-")], size=10.3, lead=13.4,
             space=2.8)
    PARA(f, FIN, size=10.3, lead=13.4, space=2.4)
    if f.y + 21.0 > H - C.MB:
        print("! déborde : resserrer")
    LIGNE(f, "Calvin B. MINANG", 10.8, gras=True, droite=True, lead=12.4)
    LIGNE(f, "né le 2 mai 2002 à Libreville — n° étudiant 0305476 — dossier ANBG n° 110584Z",
          9.0, droite=True, lead=10.6, col=GRIS)
    if f.d.page_count != 1:
        print("! ", f.d.page_count, "pages au lieu d'une")
    dest = os.path.join(C.OUT, "LETTRE-UNE-PAGE-LITIGE-MINANG.pdf")
    f.save(dest)
    print(os.path.basename(dest), "—", f.d.page_count, "page,",
          round(os.path.getsize(dest) / 1024), "Ko,", round(f.y - C.MT), "pt occupés sur",
          round(H - C.MT - C.MB))
    f.d.close()


if __name__ == "__main__":
    main()
