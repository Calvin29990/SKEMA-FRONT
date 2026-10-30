from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
OUT = ROOT / 'ubs-event-context-map.png'
W, H = 1600, 900

PAPER = '#FFFFFF'
INK = '#17364A'
MUTED = '#6B7780'
LAND = '#E6E8E8'
BORDER = '#FFFFFF'
GRID = '#D7DDE0'
JPM_BLUE = '#2476A8'
UBS_RED = '#D71935'
CS_TEAL = '#258675'
SG_RED = '#B51F3B'
BARINGS_GOLD = '#A9842E'

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SERIF_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
_font_cache = {}

def font(size, bold=False, serif=False):
    key = (size, bold, serif)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(SERIF_BOLD if serif else (BOLD if bold else FONT), size)
    return _font_cache[key]

def text(draw, xy, value, size, color=INK, bold=False, anchor=None, serif=False):
    draw.text(xy, value, font=font(size, bold, serif), fill=color, anchor=anchor)

def load_logo(filename, remove_light_bg=False):
    image = Image.open(ASSETS / filename).convert('RGBA')
    if remove_light_bg:
        pixels = image.load()
        for y in range(image.height):
            for x in range(image.width):
                r, g, b, a = pixels[x, y]
                if min(r, g, b) > 238 and max(r, g, b) - min(r, g, b) < 24:
                    pixels[x, y] = (r, g, b, 0)
    bbox = image.getchannel('A').point(lambda a: 255 if a > 10 else 0).getbbox()
    return image.crop(bbox) if bbox else image

def fit(image, max_width, max_height):
    scale = min(max_width / image.width, max_height / image.height)
    return image.resize((max(1, round(image.width * scale)), max(1, round(image.height * scale))), Image.Resampling.LANCZOS)

def paste_logo(canvas, logo, center, max_size):
    mark = fit(logo, *max_size)
    x = round(center[0] - mark.width / 2)
    y = round(center[1] - mark.height / 2)
    canvas.alpha_composite(mark, (x, y))
    return mark.size

# White, restrained dashboard layout: map + aligned event values + peer-bank context.
im = Image.new('RGBA', (W, H), PAPER)
d = ImageDraw.Draw(im)
text(d, (42, 23), 'MAJOR EUROPEAN TRADING LOSS EVENTS', 24, INK, bold=True)
text(d, (43, 57), 'Selected benchmark trading-loss events relevant to the UBS 2011 case', 13, MUTED)
skema = Image.open(ASSETS / 'skema-logo.png').convert('RGBA')
skema.thumbnail((48, 48), Image.Resampling.LANCZOS)
im.alpha_composite(skema, (1510, 15))
d.line((42, 88, 1558, 88), fill=GRID, width=1)

# Main map area: neutral countries, with only local banking hubs filled.
mx, my, mw, mh = 35, 105, 1025, 635
lon0, lon1 = -8.5, 13.5
lat0, lat1 = 42.0, 58.0

def xy(lon, lat):
    return (mx + (lon - lon0) / (lon1 - lon0) * mw,
            my + (lat1 - lat) / (lat1 - lat0) * mh)

geo_path = ASSETS / 'natural-earth-50m-western-europe-context.geojson'
with geo_path.open(encoding='utf-8') as handle:
    geo = json.load(handle)
geometries = {feature['properties']['name']: feature['geometry'] for feature in geo['features']}

def draw_country(name):
    geometry = geometries.get(name)
    if not geometry:
        return
    polygons = geometry['coordinates'] if geometry['type'] == 'MultiPolygon' else [geometry['coordinates']]
    for polygon in polygons:
        ring = polygon[0]
        xs = [point[0] for point in ring]
        ys = [point[1] for point in ring]
        if max(xs) < lon0 or min(xs) > lon1 or max(ys) < lat0 or min(ys) > lat1:
            continue
        points = [xy(lon, lat) for lon, lat in ring]
        d.polygon(points, fill=LAND)
        d.line(points + [points[0]], fill=BORDER, width=2, joint='curve')

countries = [
    'Portugal', 'Spain', 'Ireland', 'United Kingdom', 'France', 'Belgium',
    'Netherlands', 'Luxembourg', 'Germany', 'Denmark', 'Poland', 'Czechia',
    'Slovakia', 'Austria', 'Switzerland', 'Italy', 'Slovenia', 'Hungary'
]
for country in countries:
    draw_country(country)

def draw_region_feature(feature, fill, stroke=PAPER, width=1):
    geometry = feature['geometry']
    polygons = geometry['coordinates'] if geometry['type'] == 'MultiPolygon' else [geometry['coordinates']]
    for polygon in polygons:
        for ring in polygon[:1]:
            if not ring:
                continue
            xs = [pt[0] for pt in ring]
            ys = [pt[1] for pt in ring]
            if max(xs) < lon0 or min(xs) > lon1 or max(ys) < lat0 or min(ys) > lat1:
                continue
            points = [xy(lon, lat) for lon, lat in ring]
            d.polygon(points, fill=fill)
            d.line(points + [points[0]], fill=stroke, width=width, joint='curve')

# Accurate French administrative regions: IDF in Société Générale red,
# Hauts-de-France in Crédit Agricole green, all other regions neutral grey.
france_regions = json.loads((ASSETS / 'france-regions.geojson').read_text(encoding='utf-8'))
for feature in france_regions['features']:
    region = feature['properties']['nom']
    fill = SG_RED if region == 'Île-de-France' else ('#16804A' if region == 'Hauts-de-France' else LAND)
    draw_region_feature(feature, fill, PAPER, 2)

# London is the only UK region coloured (Barclays sky blue); the rest of the UK remains grey.
uk_london = json.loads((ASSETS / 'uk-london-region.geojson').read_text(encoding='utf-8'))
for feature in uk_london['features']:
    draw_region_feature(feature, '#69C6EA', PAPER, 2)

# Barings is also a London-headquartered event: a small brown/gold hub patch sits within London.
def hub_patch(points, color):
    polygon = [xy(lon, lat) for lon, lat in points]
    d.polygon(polygon, fill=color)
    d.line(polygon + [polygon[0]], fill=PAPER, width=1, joint='curve')
hub_patch([(-0.30, 51.48), (-0.24, 51.59), (-0.09, 51.63), (0.02, 51.56), (-0.05, 51.43), (-0.22, 51.40)], BARINGS_GOLD)

# Zurich: the two Swiss main-bank hubs are shown as separate, small patches.
hub_patch([(7.82, 47.10), (7.95, 47.53), (8.18, 47.78), (8.48, 47.70), (8.58, 47.43), (8.42, 47.13), (8.12, 47.00)], UBS_RED)
hub_patch([(8.58, 47.43), (8.62, 47.72), (8.94, 47.80), (9.24, 47.62), (9.32, 47.30), (9.09, 47.04), (8.78, 47.08), (8.55, 47.25)], CS_TEAL)

# City and regional labels: compact, legible, and tied to the coloured admin areas.
text(d, xy(-0.12, 51.05), 'LONDON', 9, INK, bold=True, anchor='mm')
text(d, xy(-0.12, 51.88), 'BARINGS', 8, BARINGS_GOLD, bold=True, anchor='mm')
text(d, xy(0.03, 51.24), 'BARCLAYS', 7, '#1478A6', bold=True, anchor='mm')
text(d, xy(2.35, 47.72), 'PARIS', 9, INK, bold=True, anchor='mm')
text(d, xy(2.45, 48.70), 'ÎLE-DE-FRANCE', 7, PAPER, bold=True, anchor='mm')
text(d, xy(2.8, 50.55), 'CA CIB', 8, PAPER, bold=True, anchor='mm')
text(d, xy(8.54, 46.82), 'ZURICH', 9, INK, bold=True, anchor='mm')
text(d, xy(-4.1, 54.0), 'UNITED KINGDOM', 8, MUTED, bold=True, anchor='mm')
text(d, xy(0.0, 45.8), 'FRANCE', 8, MUTED, bold=True, anchor='mm')
text(d, xy(8.2, 46.2), 'SWITZERLAND', 7, MUTED, bold=True, anchor='mm')

# Event data panel: bank marks and large reported loss figures, in a simple aligned grid.
px, py, pw, ph = 1080, 105, 478, 635
d.rounded_rectangle((px, py, px + pw, py + ph), radius=3, fill='#FAFBFB', outline=GRID, width=1)
d.rectangle((px, py, px + pw, py + 42), fill='#F0F3F4')
text(d, (px + 16, py + 13), 'ÉVÉNEMENTS DE PERTES RETENUS', 12, INK, bold=True)
text(d, (px + pw - 14, py + 15), 'MONTANT RAPPORTÉ', 8, MUTED, bold=True, anchor='ra')
d.line((px + 12, py + 43, px + pw - 12, py + 43), fill=GRID, width=1)

logos = {
    'JPM': load_logo('jpmorgan-chase-logo.png'),
    'SG': load_logo('societe-generale-logo.png'),
    'UBS': load_logo('ubs-logo.png', remove_light_bg=True),
    'CS': load_logo('credit-suisse-logo.png'),
    'BNP': load_logo('bnp-paribas-logo.png', remove_light_bg=True),
    'CA': load_logo('credit-agricole-cib-logo.png'),
    'NATIXIS': load_logo('natixis-logo.png'),
    'HSBC': load_logo('hsbc-logo.png', remove_light_bg=True),
    'BARCLAYS': load_logo('barclays-logo.jpg', remove_light_bg=True),
    'LLOYDS': load_logo('lloyds-bank-logo.png'),
    'NATWEST': load_logo('natwest-logo.png', remove_light_bg=True),
}
barings = Image.new('RGBA', (460, 100), (255, 255, 255, 0))
ImageDraw.Draw(barings).text((8, 3), 'BARINGS', font=font(68, bold=True, serif=True), fill=BARINGS_GOLD)
barings = barings.crop(barings.getchannel('A').getbbox())
logos['BARINGS'] = barings

def event_row(y, logo_key, value, name, year, hub, accent, logo_width=112):
    d.rectangle((px + 12, y, px + 16, y + 60), fill=accent)
    paste_logo(im, logos[logo_key], (px + 80, y + 27), (logo_width, 31))
    text(d, (px + 151, y + 5), value, 22, INK, bold=True)
    text(d, (px + 151, y + 32), f'{name} · {year}', 10, MUTED)
    text(d, (px + pw - 15, y + 35), hub, 9, MUTED, anchor='ra')
    d.line((px + 18, y + 62, px + pw - 14, y + 62), fill=GRID, width=1)

event_row(py + 54, 'JPM', 'USD 6.2bn', 'London Whale', '2012', 'UK · London', JPM_BLUE, 124)
event_row(py + 120, 'BARINGS', '~USD 1.4bn', 'Barings', '1995', 'UK · London HQ¹', BARINGS_GOLD, 112)
event_row(py + 186, 'SG', 'EUR 4.9bn', 'Société Générale', '2008', 'France · Paris', SG_RED, 118)
event_row(py + 252, 'UBS', 'USD 2.3bn', 'UBS Delta One', '2011', 'London desk²', UBS_RED, 82)
event_row(py + 318, 'CS', 'USD 5.5bn', 'Credit Suisse / Archegos', '2021', 'Zurich HQ³', CS_TEAL, 114)

# Peer banks are shown as institutional context only; no unsourced loss values are assigned.
peer_y = py + 395
d.line((px + 14, peer_y, px + pw - 14, peer_y), fill=GRID, width=1)
text(d, (px + 16, peer_y + 12), 'BANQUES CIB / GRANDES BANQUES DE CONTEXTE', 10, INK, bold=True)
text(d, (px + 16, peer_y + 28), 'Logos de référence · aucun chiffre de perte ajouté sans cas comparable retenu', 8, MUTED)

# French CIB peers: BNP Paribas, Crédit Agricole CIB and Natixis (Société Générale is above).
fr_y = peer_y + 53
text(d, (px + 16, fr_y + 10), 'FR CIB', 8, MUTED, bold=True)
for key, cx in [('BNP', px + 111), ('CA', px + 244), ('NATIXIS', px + 375)]:
    paste_logo(im, logos[key], (cx, fr_y + 14), (105, 25))

# UK banking peers shown in a compact logo row.
uk_y = fr_y + 39
text(d, (px + 16, uk_y + 13), 'UK', 8, MUTED, bold=True)
uk_marks = [('HSBC', px + 92), ('BARCLAYS', px + 195), ('LLOYDS', px + 300), ('NATWEST', px + 407)]
for key, cx in uk_marks:
    paste_logo(im, logos[key], (cx, uk_y + 15), (74, 25))
text(d, (px + 300, uk_y + 29), 'Lloyds Bank', 7, MUTED, anchor='mm')

# Footer with source/method notes and the requested executive takeaway.
d.line((42, 764, 1558, 764), fill=GRID, width=1)
text(d, (45, 774), 'TAKEAWAY', 8, SG_RED, bold=True)
text(d, (45, 790), "UBS's USD 2.3bn trading loss ranks among the most significant banking trading-loss events in Europe and illustrates how control failures can rapidly escalate into material financial and liquidity-management consequences.", 10, INK, bold=True)
text(d, (45, 817), '¹ Leeson traded in Singapore. ² UBS loss-making desk: London; Zurich is group HQ. ³ Credit Suisse shown at Zurich HQ; Archegos was a counterparty exposure.', 7, MUTED)
text(d, (45, 839), 'Sources: FINMA [1] · Credit Suisse Board Special Committee [2] · U.S. Senate PSI [3] · Société Générale [4] · RBA / BoE inquiry [5].', 7, MUTED)
text(d, (1552, 839), 'Hub patches are schematic, not administrative or ownership boundaries.', 7, MUTED, anchor='ra')

im.convert('RGB').save(OUT)
print(OUT)
