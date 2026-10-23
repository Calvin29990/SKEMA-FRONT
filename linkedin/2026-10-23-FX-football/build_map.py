#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construit la carte interactive (GitHub Pages) + les jeux de données Excel / Power BI.

Sorties :
  docs/index.html                          -> carte interactive autonome (aucune dépendance externe)
  data/entreprises_par_region.csv          -> agrégé, sans nom d'entreprise (Excel / Power BI)
  data/clubs_partenaires_fx.csv            -> clubs nommés + partenaires FX publics (sourcés)
  data/carte-FX.xlsx                       -> les deux tables dans un classeur
"""
import csv
import json
import math
import os
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
ASSETS = os.path.join(HERE, "assets")
DOCS = os.path.join(REPO, "docs")
DATA = os.path.join(HERE, "data")
os.makedirs(DOCS, exist_ok=True)
os.makedirs(DATA, exist_ok=True)

# ------------------------------------------------------------------ données régions
# Classes de densité uniquement : aucune valeur exacte, aucun nom, aucune commune.
REGIONS = [
    # nom, code, classe (0..4), libellé de classe
    ("Île-de-France", "11", 4),
    ("Auvergne-Rhône-Alpes", "84", 3),
    ("Hauts-de-France", "32", 3),
    ("Occitanie", "76", 3),
    ("Provence-Alpes-Côte d'Azur", "93", 2),
    ("Grand Est", "44", 2),
    ("Nouvelle-Aquitaine", "75", 2),
    ("Pays de la Loire", "52", 2),
    ("Normandie", "28", 1),
    ("Bretagne", "53", 1),
    ("Bourgogne-Franche-Comté", "27", 1),
    ("Centre-Val de Loire", "24", 1),
    ("Corse", "94", 0),
]
CLASS_LABEL = {
    4: "> 10 000 sièges",
    3: "3 000 – 4 000 sièges",
    2: "2 000 – 3 000 sièges",
    1: "1 000 – 2 000 sièges",
    0: "< 1 000 sièges",
}

# ------------------------------------------------------------------ clubs + partenaires FX publics
# Règle : on ne cite que ce qui a été annoncé publiquement par le club ou par la fintech.
CLUBS = [
    {
        "club": "Olympique Lyonnais", "short": "OL", "city": "Lyon", "league": "Ligue 1",
        "lat": 45.7653, "lon": 4.9821,
        "partners": [{
            "fintech": "Ebury", "role": "Partenaire Officiel Fintech / FX",
            "season": "2025/2026", "date": "2025-10-28",
            "url": "https://www.ol.fr/fr/actualites/ebury-devient-partenaire-fintech-de-l-olympique-lyonnais-pour-2025-2026",
            "src": "ol.fr (communiqué du club)",
        }],
    },
    {
        "club": "AS Monaco", "short": "ASM", "city": "Monaco", "ldir": 1, "ldy": -1, "league": "Ligue 1",
        "lat": 43.7275, "lon": 7.4156,
        "partners": [
            {"fintech": "Ebury", "role": "Partenaire fintech / FX",
             "season": "2024/2025", "date": "2024-09-10",
             "url": "https://www.asmonaco.com/en/news/ebury-new-fintech-partner-of-as-monaco",
             "src": "asmonaco.com (communiqué du club)"},
            {"fintech": "Sokin", "role": "Official Global Payments & FX Money Transfer Partner",
             "season": "2021 – 2024 (3 saisons)", "date": "2021-06-08",
             "url": "https://www.asmonaco.com/en/news/sokin-nouveau-partenaire-officiel-de-las-monaco",
             "src": "asmonaco.com (communiqué du club)"},
        ],
    },
    {
        "club": "Olympique de Marseille", "short": "OM", "city": "Marseille", "ldir": -1, "ldy": 1, "league": "Ligue 1",
        "lat": 43.2697, "lon": 5.3959,
        "partners": [{
            "fintech": "Ebury", "role": "Fournisseur officiel (paiements internationaux, FX)",
            "season": "2025/2026", "date": "2026-01-07",
            "url": "https://www.laprovence.com/article/economie/60019635627413/la-fintech-ebury-frappe-un-grand-coup-en-devenant-le-fournisseur-officiel-de-lolympique-de-marseille",
            "src": "La Provence / communiqué OL-OM",
        }],
    },
    {
        "club": "Toulouse FC", "short": "TFC", "city": "Toulouse", "league": "Ligue 1",
        "lat": 43.5833, "lon": 1.4340,
        "partners": [{
            "fintech": "Corpay Cross-Border", "role": "Fournisseur officiel de services de change (FX)",
            "season": "pluriannuel, depuis 2025", "date": "2025-02-20",
            "url": "https://www.businesswire.com/news/home/20250220824657/fr",
            "src": "Business Wire (communiqué Corpay) + toulousefc.com",
        }],
    },
    {
        "club": "Stade de Reims", "short": "SDR", "city": "Reims", "league": "Ligue 2",
        "lat": 49.2465, "lon": 4.0500,
        "partners": [{
            "fintech": "Ebury", "role": "Partenaire Premium",
            "season": "2025/2026", "date": "2025-07-09",
            "url": "https://www.stade-de-reims.com/ebury-devient-partenaire-premium-du-sdr/",
            "src": "stade-de-reims.com (communiqué du club)",
        }],
    },
    {
        "club": "Paris Saint-Germain", "short": "PSG", "city": "Paris", "league": "Ligue 1",
        "lat": 48.8414, "lon": 2.2531, "partners": [],
    },
    {
        "club": "LOSC Lille", "short": "LOSC", "city": "Lille", "ldir": 1, "ldy": -1, "league": "Ligue 1",
        "lat": 50.6119, "lon": 3.1322, "partners": [],
    },
    {
        "club": "RC Lens", "short": "RCL", "city": "Lens", "ldir": -1, "ldy": 0, "league": "Ligue 1",
        "lat": 50.4327, "lon": 2.8151, "partners": [],
    },
    {
        "club": "Stade Rennais FC", "short": "SRFC", "city": "Rennes", "league": "Ligue 1",
        "lat": 48.1173, "lon": -1.6778, "partners": [],
    },
    {
        "club": "OGC Nice", "short": "OGCN", "city": "Nice", "ldir": -1, "ldy": 1, "league": "Ligue 1",
        "lat": 43.5610, "lon": 7.1926, "partners": [],
    },
    {
        "club": "RC Strasbourg Alsace", "short": "RCSA", "city": "Strasbourg", "league": "Ligue 1",
        "lat": 48.5601, "lon": 7.7553, "partners": [],
    },
    {
        "club": "Paris FC", "short": "PFC", "city": "Paris", "league": "Ligue 1",
        "lat": 48.8405, "lon": 2.2450, "ldir": -1, "ldy": -1, "partners": [],
    },
]

# accords hors France métropolitaine (liste, pas de point sur la carte)
HORS_CARTE = [
    {"club": "Servette FC", "pays": "Suisse", "fintech": "Ebury", "role": "Partenaire Gold",
     "date": "2024-07-19", "url": "https://servettefc.ch/ebury-devient-partenaire-gold-du-servette-fc/"},
    {"club": "Botafogo", "pays": "Brésil", "fintech": "Ebury", "role": "Partenaire officiel FX",
     "date": "2025-09", "url": "https://www.sportbuzzbusiness.fr/ebury-devient-partenaire-fintech-de-lolympique-lyonnais-pour-2025-2026.html"},
    {"club": "Parma Calcio", "pays": "Italie", "fintech": "Ebury", "role": "Official Payment & FX Partner",
     "date": "2024-09-26", "url": "https://www.parmacalcio1913.com/en/main-news/ebury-official-payment-foreign-exchange-partner/"},
    {"club": "FC Universitatea Cluj", "pays": "Roumanie", "fintech": "Ebury", "role": "Official FX Partner",
     "date": "2026-07-16", "url": "https://www.fcucluj.ro/stire/fc-universitatea-cluj-isi-uneste-fortele-cu-ebury-noul-official-fx-partner-al-clubului"},
    {"club": "Fulham FC · Aston Villa · Southampton · Rangers · PSV · FC Copenhague", "pays": "UK / NL / DK",
     "fintech": "Ebury", "role": "Clubs cités par Ebury Sports",
     "date": "2024-2026", "url": "https://ebury.com/solutions/by-industry/global-sports"},
    {"club": "Everton FC · Fulham FC", "pays": "Angleterre", "fintech": "Sokin", "role": "Official payments partner",
     "date": "2021", "url": "https://www.asmonaco.com/en/news/sokin-nouveau-partenaire-officiel-de-las-monaco"},
]

# ------------------------------------------------------------------ projection
LAT0 = 46.5
LON0 = 2.5
KX = math.cos(math.radians(LAT0))


def project(lon, lat):
    return ((lon - LON0) * KX, -(lat - LAT0))


def load_geojson():
    with open(os.path.join(ASSETS, "regions.geojson")) as f:
        return json.load(f)["features"]


def ring_to_path(ring):
    pts = [project(x, y) for x, y in ring]
    d = f"M{pts[0][0]:.3f},{pts[0][1]:.3f}"
    for x, y in pts[1:]:
        d += f"L{x:.3f},{y:.3f}"
    return d + "Z"


def build_geo():
    feats = load_geojson()
    by_code = {name_code[1]: name_code for name_code in REGIONS}
    out = []
    for f in feats:
        code = f["properties"]["code"]
        geom = f["geometry"]
        polys = [geom["coordinates"][0]] if geom["type"] == "Polygon" else [p[0] for p in geom["coordinates"]]
        d = "".join(ring_to_path(r) for r in polys)
        name = f["properties"]["nom"]
        cls = dict((c, k) for n, c, k in REGIONS).get(code, 0)
        out.append({"code": code, "name": name, "d": d, "cls": cls, "label": CLASS_LABEL[cls]})
    return out


# ------------------------------------------------------------------ HTML
def build_html(geo, clubs):
    data = {
        "regions": geo,
        "clubs": [
            {
                "club": c["club"], "short": c["short"], "city": c["city"], "league": c["league"],
                "ldir": c.get("ldir", 1), "ldy": c.get("ldy", 0),
                "x": round(project(c["lon"], c["lat"])[0], 3),
                "y": round(project(c["lon"], c["lat"])[1], 3),
                "partners": c["partners"],
            }
            for c in clubs
        ],
        "horsCarte": HORS_CARTE,
        "classes": CLASS_LABEL,
    }
    payload = json.dumps(data, ensure_ascii=False)

    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    html = tpl.replace("__DATA__", payload)
    with open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("ok docs/index.html")


# ------------------------------------------------------------------ exports
def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return s.lower().replace(" ", "-").replace("'", "-")


def write_csvs():
    p1 = os.path.join(DATA, "entreprises_par_region.csv")
    with open(p1, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["region", "code_region", "classe_densite", "libelle_classe",
                    "nom_entreprise_publie", "commune_publiee", "source", "date_extraction"])
        for name, code, cls in REGIONS:
            w.writerow([name, code, cls, CLASS_LABEL[cls], "non", "non",
                        "Orbis (Bureau van Dijk) + INSEE", "2026-10-20"])

    p2 = os.path.join(DATA, "clubs_partenaires_fx.csv")
    rows = []
    for c in CLUBS:
        if c["partners"]:
            for p in c["partners"]:
                rows.append([c["club"], c["league"], c["city"], c["lat"], c["lon"],
                             p["fintech"], p["role"], p["season"], p["date"], p["url"], p["src"]])
        else:
            rows.append([c["club"], c["league"], c["city"], c["lat"], c["lon"],
                         "aucun partenariat FX public identifie", "", "", "", "", "recherche personnelle 2026-10-23"])
    for h in HORS_CARTE:
        rows.append([h["club"], h["pays"], "", "", "", h["fintech"], h["role"], "", h["date"], h["url"], ""])

    with open(p2, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["club", "championnat_pays", "ville", "latitude", "longitude",
                    "fintech_ou_prestataire_fx", "role_annonce", "saison", "date_annonce",
                    "source_url", "source_nom"])
        w.writerows(rows)
    print("ok data/entreprises_par_region.csv")
    print("ok data/clubs_partenaires_fx.csv")
    return rows


def write_xlsx(rows):
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill, Alignment
        from openpyxl.utils import get_column_letter
    except ImportError:
        print("openpyxl absent : xlsx non généré")
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "Clubs & FX"
    head = ["club", "championnat_pays", "ville", "latitude", "longitude",
            "fintech_ou_prestataire_fx", "role_annonce", "saison", "date_annonce",
            "source_url", "source_nom"]
    ws.append(head)
    for r in rows:
        ws.append(r)
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="12624A")
        c.alignment = Alignment(wrap_text=True, vertical="center")
    widths = [34, 14, 14, 10, 10, 26, 42, 22, 12, 60, 34]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "A2"

    ws2 = wb.create_sheet("Entreprises (agrégé)")
    ws2.append(["region", "code_region", "classe_densite", "libelle_classe", "source", "date_extraction"])
    for name, code, cls in REGIONS:
        ws2.append([name, code, cls, CLASS_LABEL[cls], "Orbis (Bureau van Dijk) + INSEE", "2026-10-20"])
    for c in ws2[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="12624A")
    for i, w in enumerate([30, 12, 14, 24, 38, 14], 1):
        ws2.column_dimensions[get_column_letter(i)].width = w

    ws3 = wb.create_sheet("Lisez-moi")
    notes = [
        ["Carte FX & football — Calvin MINANG — 23/10/2026"],
        [""],
        ["Principe :", "les entreprises sont agrégées (aucun nom, aucune commune)."],
        ["", "Les clubs de football sont nommés : ce sont des partenariats annoncés publiquement."],
        [""],
        ["Onglet 'Clubs & FX'", "une ligne par club + partenaire. Latitude/longitude prêtes pour Excel 3D Maps ou Power BI."],
        ["Onglet 'Entreprises (agrégé)'", "une ligne par région, classe de densité uniquement."],
        [""],
        ["Excel 3D Maps", "Données > Carte 3D > Nouvelle visite > glisser 'latitude' en Y et 'longitude' en X."],
        ["Power BI", "Visuel 'Carte' (lat/lon) ou 'Carte choroplèthe' avec le champ region + classe_densite."],
        [""],
        ["Sources", "Orbis (Bureau van Dijk) 20/10/2026, INSEE, communiqués des clubs et des fintechs."],
        ["", "Aucune donnée client, aucune donnée confidentielle."],
    ]
    for row in notes:
        ws3.append(row)
    ws3.column_dimensions["A"].width = 32
    ws3.column_dimensions["B"].width = 100
    ws3["A1"].font = Font(bold=True, size=13)

    path = os.path.join(DATA, "carte-FX.xlsx")
    wb.save(path)
    print("ok data/carte-FX.xlsx")


if __name__ == "__main__":
    geo = build_geo()
    build_html(geo, CLUBS)
    rows = write_csvs()
    write_xlsx(rows)
