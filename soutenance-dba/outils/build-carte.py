#!/usr/bin/env python3
"""
Génère medias/gabon.svg — carte des neuf provinces du Gabon.

Données   : data/gab_adm1.geojson
            geoBoundaries — GAB ADM1, version GAUL 2001 (CC BY 4.0).
Projection: équirectangulaire ajustée en longitude par cos(latitude moyenne),
            cadrage automatique sur l'emprise du pays.
Sortie    : medias/gabon.svg (aucune dépendance externe).

Usage : python3 outils/build-carte.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "gab_adm1.geojson"
OUT = ROOT / "medias" / "gabon.svg"

W, H, PAD = 640, 700, 50

# Noms affichés (orthographe accentuée)
LABEL = {
    "Estuaire": "Estuaire",
    "Haut-Ogooue": "Haut-Ogooué",
    "Moyen-Ogooue": "Moyen-Ogooué",
    "Ngounie": "Ngounié",
    "Nyanga": "Nyanga",
    "Ogooue-Ivindo": "Ogooué-Ivindo",
    "Ogooue-lolo": "Ogooué-Lolo",
    "Ogooue-Maritime": "Ogooué-Maritime",
    "Woleu-Ntem": "Woleu-Ntem",
}

# Positions manuelles des étiquettes (x, y) pour éviter les chevauchements
LABEL_POS = {
    "Woleu-Ntem": (350, 148),
    "Ogooué-Ivindo": (440, 232),
    "Moyen-Ogooué": (243, 303),
    "Ogooué-Maritime": (139, 437),
    "Ngounié": (300, 411),
    "Ogooué-Lolo": (378, 356),
    "Haut-Ogooué": (522, 363),
    "Nyanga": (279, 541),
}
HIGHLIGHT = "Estuaire"          # province du siège (Libreville, Sablière)

CITIES = [                       # (nom, lon, lat, dx, dy, ancre, sous-titre)
    ("Libreville", 9.45, 0.39, 18, 4, "start", "siège de l'UPL"),
    ("Port-Gentil", 8.78, -0.72, 10, 4, "start", ""),
    ("Franceville", 13.58, -1.63, 10, 8, "start", ""),
]


def load_rings(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    provinces = []
    for feature in data["features"]:
        name = LABEL.get(feature["properties"]["ADM1_NAME"], feature["properties"]["ADM1_NAME"])
        rings = []
        for polygon in feature["geometry"]["coordinates"]:
            for ring in polygon:
                rings.append([(float(lon), float(lat)) for lon, lat in ring])
        provinces.append((name, rings))
    return provinces


def main() -> None:
    provinces = load_rings(SRC)

    lons = [lon for _, rings in provinces for ring in rings for lon, _ in ring]
    lats = [lat for _, rings in provinces for ring in rings for _, lat in ring]
    minx, maxx, miny, maxy = min(lons), max(lons), min(lats), max(lats)

    k = math.cos(math.radians((miny + maxy) / 2))
    scale = min((W - 2 * PAD - 30) / ((maxx - minx) * k), (H - 2 * PAD - 10) / (maxy - miny))
    ox = (W - (maxx - minx) * k * scale) / 2
    oy = (H - (maxy - miny) * scale) / 2

    def project(lon: float, lat: float):
        return (round((lon - minx) * k * scale + ox, 1),
                round((maxy - lat) * scale + oy, 1))

    paths = []
    for name, rings in provinces:
        d = "".join(
            "M" + "L".join("%s %s" % project(lon, lat) for lon, lat in ring) + "Z"
            for ring in rings
        )
        paths.append((name, d))

    lib = project(9.45, 0.39)
    eq_y = project(minx, 0.0)[1]

    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 700" width="640" height="700" role="img" aria-labelledby="gt gd">',
        '<title id="gt">Carte du Gabon</title>',
        '<desc id="gd">Les neuf provinces du Gabon, avec Libreville (siège de l\'UPL), Port-Gentil et Franceville. '
        "Fond de carte geoBoundaries, GAB ADM1 (GAUL 2001), CC BY 4.0.</desc>",
        "<defs>",
        '<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#E0BE79" stop-opacity=".55"/>'
        '<stop offset="1" stop-color="#E0BE79" stop-opacity="0"/></radialGradient>',
        '<style>'
        ".pv{fill:#16202A;stroke:#C79A3E;stroke-opacity:.30;stroke-width:1}"
        ".pv.hi{fill:#2A2318;stroke:#E0BE79;stroke-opacity:.85;stroke-width:1.4}"
        '.lb{font:600 11px "Segoe UI",system-ui,sans-serif;fill:#93A5B4;letter-spacing:.08em;text-anchor:middle}'
        '.ct{font:700 13px "Segoe UI",system-ui,sans-serif;fill:#F4EFE4}'
        '.ct.sm{font:600 10.5px "Segoe UI",system-ui,sans-serif;fill:#B9C6D2}'
        '.nb{font:600 10px "Segoe UI",system-ui,sans-serif;fill:#5F7182;letter-spacing:.22em}'
        '.eq{font:600 9px "Segoe UI",system-ui,sans-serif;fill:#5F7182;letter-spacing:.2em}'
        "</style>",
        "</defs>",
        # pays voisins et océan
        '<text class="nb" x="352" y="66">CAMEROUN</text>',
        '<text class="nb" x="16" y="330" transform="rotate(-90 26 330)">GUINÉE ÉQUATORIALE</text>',
        '<text class="nb" x="556" y="596">CONGO</text>',
        '<text class="nb" x="60" y="636" transform="rotate(-90 70 636)">GOLFE DE GUINÉE</text>',
        # équateur
        '<line x1="26" y1="%s" x2="614" y2="%s" stroke="#8FA0AF" stroke-opacity=".18" stroke-dasharray="2 6"/>' % (eq_y, eq_y),
    ]

    for name, d in paths:
        cls = "pv hi" if name == HIGHLIGHT else "pv"
        svg.append('<path class="%s" d="%s"/>' % (cls, d))

    for name, _ in paths:
        pos = LABEL_POS.get(name)
        if pos:
            svg.append('<text class="lb" x="%s" y="%s">%s</text>' % (pos[0], pos[1], name.upper()))

    for name, lon, lat, dx, dy, anchor, sub in CITIES:
        x, y = project(lon, lat)
        if name == "Libreville":
            svg.append('<circle cx="%s" cy="%s" r="26" fill="url(#glow)"/>' % (x, y))
            svg.append('<circle cx="%s" cy="%s" r="10" fill="none" stroke="#E0BE79" stroke-opacity=".55"/>' % (x, y))
            svg.append('<circle cx="%s" cy="%s" r="4.2" fill="#E0BE79"/>' % (x, y))
            svg.append('<text class="ct" x="%s" y="%s">%s</text>' % (x + dx, y + dy, name))
            if sub:
                svg.append('<text class="ct sm" x="%s" y="%s">%s</text>' % (x + dx, y + dy + 16, sub))
        else:
            svg.append('<circle cx="%s" cy="%s" r="3.4" fill="#F4EFE4" fill-opacity=".8"/>' % (x, y))
            svg.append('<text class="ct sm" x="%s" y="%s" text-anchor="%s">%s</text>'
                       % (x + dx, y + dy, anchor, name))

    svg.append("</svg>")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(svg) + "\n", encoding="utf-8")
    print("écrit : %s (%d octets, %d provinces)" % (OUT.relative_to(ROOT), OUT.stat().st_size, len(paths)))


if __name__ == "__main__":
    main()
