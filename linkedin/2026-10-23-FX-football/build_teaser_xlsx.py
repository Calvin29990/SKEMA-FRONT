#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Classeur « teaser » : ce qui est public, et rien d'autre. Les champs du modèle
détaillé restent vides / marqués « non diffusé » — c'est volontaire."""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "teaser-FX-football.xlsx")

GREEN = "0E3A2B"
DARK = "0A1310"

# uniquement les accords annoncés publiquement
ROWS = [
    ["Olympique Lyonnais", "Ligue 1", "Lyon", "Ebury", "Partenaire Officiel Fintech / FX",
     "2025-10-28", "2025/2026", "ol.fr", "https://www.ol.fr/fr/actualites/ebury-devient-partenaire-fintech-de-l-olympique-lyonnais-pour-2025-2026"],
    ["AS Monaco", "Ligue 1", "Monaco", "Ebury", "Partenaire fintech / FX",
     "2024-09-10", "2024/2025", "asmonaco.com", "https://www.asmonaco.com/en/news/ebury-new-fintech-partner-of-as-monaco"],
    ["AS Monaco", "Ligue 1", "Monaco", "Sokin", "Official Global Payments & FX Partner",
     "2021-06-08", "2021-2024", "asmonaco.com", "https://www.asmonaco.com/en/news/sokin-nouveau-partenaire-officiel-de-las-monaco"],
    ["Olympique de Marseille", "Ligue 1", "Marseille", "Ebury", "Fournisseur officiel (paiements internationaux, FX)",
     "2026-01-07", "2025/2026", "La Provence", "https://www.laprovence.com/article/economie/60019635627413/la-fintech-ebury-frappe-un-grand-coup-en-devenant-le-fournisseur-officiel-de-lolympique-de-marseille"],
    ["Toulouse FC", "Ligue 1", "Toulouse", "Corpay Cross-Border", "Fournisseur officiel de services de change (FX)",
     "2025-02-20", "pluriannuel", "Business Wire", "https://www.businesswire.com/news/home/20250220824657/fr"],
    ["Stade de Reims", "Ligue 1", "Reims", "Ebury", "Partenaire Premium",
     "2025-07-09", "2025/2026", "stade-de-reims.com", "https://www.stade-de-reims.com/ebury-devient-partenaire-premium-du-sdr/"],
]

HEAD = ["club", "championnat", "ville", "partenaire_fx", "role_annonce", "date_annonce",
        "saison", "source", "source_url",
        "volumes_fx_estimes", "nb_echeances_transfert", "devises_principales", "score_priorite"]

PERIMETRE = [
    ["champ", "statut", "detail"],
    ["Nombre de sociétés du périmètre", "PUBLIC", "64 646 sociétés françaises ≥ 5 M€ de CA (Orbis, 20/10/2026)"],
    ["Sièges géolocalisés", "PUBLIC", "45 837 (géolocalisation INSEE)"],
    ["Répartition régionale", "PUBLIC", "5 classes de densité — voir la carte"],
    ["Clubs et partenaires FX annoncés", "PUBLIC", "6 accords, 5 clubs — onglet « Clubs couverts »"],
    ["Volumes FX par club", "NON DIFFUSÉ", "Modèle interne, non publiable"],
    ["Échéanciers de transfert", "NON DIFFUSÉ", "Modèle interne, non publiable"],
    ["Devises par club", "PARTIEL", "Déduites des marchés de transfert, non vérifiées club par club"],
    ["Score de priorité commerciale", "NON DIFFUSÉ", "Résultat du scoring, non publiable"],
    ["Noms d'entreprises / communes", "NON DIFFUSÉ", "Conformément à la licence Orbis et par choix"],
]


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = "Clubs couverts"
    ws.append(HEAD)
    for r in ROWS:
        ws.append(r + ["non communiqué", "non communiqué", "non communiqué", "non diffusé"])
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF", size=10)
        c.fill = PatternFill("solid", fgColor=GREEN)
        c.alignment = Alignment(wrap_text=True, vertical="center")
    for i, w in enumerate([26, 12, 12, 22, 44, 13, 12, 20, 62, 20, 20, 20, 16], 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:M{ws.max_row}"

    ws2 = wb.create_sheet("Périmètre")
    for r in PERIMETRE:
        ws2.append(r)
    for c in ws2[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=GREEN)
    for i, w in enumerate([38, 18, 90], 1):
        ws2.column_dimensions[get_column_letter(i)].width = w
    for row in ws2.iter_rows(min_row=2):
        if row[1].value == "NON DIFFUSÉ":
            row[1].font = Font(bold=True, color="C0392B")

    ws3 = wb.create_sheet("Lisez-moi")
    for line in [
        ["Le change caché du foot français — C. Minang — 23/10/2026"],
        [""],
        ["Ce fichier est volontairement incomplet."],
        ["Il contient uniquement ce qui est vérifiable publiquement : les accords FX annoncés par les clubs et les fintechs."],
        ["Les colonnes de modélisation (volumes, échéanciers, scoring) sont marquées « non diffusé »."],
        [""],
        ["Pourquoi :", "les données nominatives et les montants par entreprise relèvent d'une licence Orbis"],
        ["", "et d'un travail d'analyse qui n'a pas vocation à circuler sans contexte."],
        [""],
        ["Comment vérifier", "chaque ligne renvoie à la source primaire (communiqué du club ou de la fintech)."],
        [""],
        ["Aucune donnée client. Aucune donnée confidentielle."],
    ]:
        ws3.append(line)
    ws3["A1"].font = Font(bold=True, size=13)
    ws3.column_dimensions["A"].width = 24
    ws3.column_dimensions["B"].width = 105

    wb.save(OUT)
    print("ok", OUT)


if __name__ == "__main__":
    main()
