from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont, ImageColor

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
OUT = ROOT / 'ubs-event-context-map.png'
W, H = 1600, 900
PAPER = '#FFFFFF'
LAND = '#E9EBEA'
BORDER = '#FFFFFF'
INK = '#183448'
MUTED = '#66747D'
GRID = '#D9DEDF'

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SERIF_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
_fonts = {}

def font(size, bold=False, serif=False):
    key = (size, bold, serif)
    if key not in _fonts:
        path = SERIF_BOLD if serif else (BOLD if bold else FONT)
        _fonts[key] = ImageFont.truetype(path, size)
    return _fonts[key]

def text(draw, xy, value, size, color=INK, bold=False, anchor=None, serif=False,
         stroke_width=0, stroke_fill=PAPER):
    draw.text(xy, value, font=font(size, bold, serif), fill=color, anchor=anchor,
              stroke_width=stroke_width, stroke_fill=stroke_fill)

def load_logo(filename, remove_light_bg=False):
    image = Image.open(ASSETS / filename).convert('RGBA')
    if remove_light_bg:
        px = image.load()
        for y in range(image.height):
            for x in range(image.width):
                r, g, b, a = px[x, y]
                if min(r, g, b) > 238 and max(r, g, b) - min(r, g, b) < 24:
                    px[x, y] = (r, g, b, 0)
    bbox = image.getchannel('A').point(lambda a: 255 if a > 10 else 0).getbbox()
    return image.crop(bbox) if bbox else image

def fit(image, max_width, max_height):
    scale = min(max_width / image.width, max_height / image.height)
    return image.resize((max(1, round(image.width * scale)), max(1, round(image.height * scale))), Image.Resampling.LANCZOS)

def paste_logo_floating(canvas, logo, center, max_size):
    """Place the logo directly on the map, with no badge, circle or keyline."""
    mark = fit(logo, *max_size)
    x = round(center[0] - mark.width / 2)
    y = round(center[1] - mark.height / 2)
    canvas.alpha_composite(mark, (x, y))
    return mark.size

im = Image.new('RGBA', (W, H), PAPER)
d = ImageDraw.Draw(im)

# Compact title area; the European map and city marks remain dominant.
text(d, (42, 22), 'MAJOR EUROPEAN TRADING LOSS EVENTS', 24, INK, bold=True)
text(d, (43, 56), 'Selected benchmark trading-loss events relevant to the UBS 2011 case', 13, MUTED)
d.line((42, 88, 1558, 88), fill=GRID, width=1)
page_under_map = im.copy()

# Light-grey Europe base, with discreet national borders.
# North-up, flat map projection, zoomed around the bank territories (no perspective or tilt).
mx, my, mw, mh = 350, 105, 900, 680
lon0, lon1 = -6.5, 10.5
lat0, lat1 = 42.5, 57.5

def xy(lon, lat):
    return (mx + (lon - lon0) / (lon1 - lon0) * mw,
            my + (lat1 - lat) / (lat1 - lat0) * mh)

geo_path = ASSETS / 'natural-earth-50m-western-europe-context.geojson'
with geo_path.open(encoding='utf-8') as handle:
    geo = json.load(handle)

def draw_geometry(geometry):
    polygons = geometry['coordinates'] if geometry['type'] == 'MultiPolygon' else [geometry['coordinates']]
    for polygon in polygons:
        ring = polygon[0]
        xs = [p[0] for p in ring]
        ys = [p[1] for p in ring]
        if max(xs) < lon0 or min(xs) > lon1 or max(ys) < lat0 or min(ys) > lat1:
            continue
        points = [xy(lon, lat) for lon, lat in ring]
        d.polygon(points, fill=LAND)
        d.line(points + [points[0]], fill=BORDER, width=2, joint='curve')

for feature in geo['features']:
    draw_geometry(feature['geometry'])

# Colour the administrative territory associated with each bank city, not its label.
# Tints preserve legibility; outlines use the corresponding bank colour.
territory_styles = {
    'NATWEST': ('#C6ADBF', '#5E2750'),
    'BARCLAYS': ('#B6E3F1', '#00AEEF'),
    'LLOYDS': ('#B4D4BC', '#00843D'),
    'HSBC': ('#E98C94', '#DB0011'),
    'BNP': ('#A8D0BA', '#00965E'),
    'SG': ('#E98C94', '#E30613'),
    'CA': ('#9BC9BB', '#006B54'),
    'NATIXIS': ('#A783C9', '#6F2DA8'),
    'UBS': ('#B3B3B3', '#111111'),
    'CS': ('#A7CDEA', '#005EB8'),
    'JULIUS': ('#C0CEE2', '#4C6FA5'),
    'PICTET': ('#A1CBBF', '#006A52'),
}

region_path = ASSETS / 'france-regions.geojson'
with region_path.open(encoding='utf-8') as handle:
    france_regions = json.load(handle)
france_bank_regions = {
    'Hauts-de-France': 'BNP',
    'Île-de-France': 'SG',
    'Auvergne-Rhône-Alpes': 'CA',
    'Provence-Alpes-Côte d\'Azur': 'NATIXIS',
}
uk_region_path = ASSETS / 'uk-bank-regions.geojson'
with uk_region_path.open(encoding='utf-8') as handle:
    uk_regions = json.load(handle)
swiss_region_path = ASSETS / 'swiss-bank-cantons.geojson'
with swiss_region_path.open(encoding='utf-8') as handle:
    swiss_regions = json.load(handle)

territories = []
for feature in france_regions['features']:
    bank_key = france_bank_regions.get(feature['properties']['nom'])
    territories.append((feature, bank_key, True))
for feature in uk_regions['features']:
    bank_key = feature['properties']['bank_key']
    territories.append((feature, bank_key, feature['properties'].get('outline', True)))
for feature in swiss_regions['features']:
    territories.append((feature, feature['properties']['bank_key'], True))

def polygons_of(feature):
    geometry = feature['geometry']
    return geometry['coordinates'] if geometry['type'] == 'MultiPolygon' else [geometry['coordinates']]

# Fill only the bank-associated areas; every other country and region stays grey.
region_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
rd = ImageDraw.Draw(region_layer)
for feature, bank_key, _ in territories:
    if bank_key:
        fill = (*ImageColor.getrgb(territory_styles[bank_key][0]), 210)
    else:
        fill = LAND
    for polygon in polygons_of(feature):
        points = [xy(lon, lat) for lon, lat in polygon[0]]
        rd.polygon(points, fill=fill)
im.alpha_composite(region_layer)

# Restore clean national borders, then outline each administrative territory.
d = ImageDraw.Draw(im)
for feature in geo['features']:
    geometry = feature['geometry']
    polygons = geometry['coordinates'] if geometry['type'] == 'MultiPolygon' else [geometry['coordinates']]
    for polygon in polygons:
        points = [xy(lon, lat) for lon, lat in polygon[0]]
        d.line(points + [points[0]], fill=BORDER, width=2, joint='curve')
for feature, bank_key, outline in territories:
    if not outline:
        continue
    color = territory_styles[bank_key][1] if bank_key else '#FFFFFF'
    width = 3 if bank_key else 2
    for polygon in polygons_of(feature):
        points = [xy(lon, lat) for lon, lat in polygon[0]]
        d.line(points + [points[0]], fill=color, width=width, joint='curve')

# Clip geographic layers to the zoom window so no land spills into the title or footer.
map_crop = im.crop((mx, my, mx + mw, my + mh))
im = page_under_map.copy()
im.alpha_composite(map_crop, (mx, my))
d = ImageDraw.Draw(im)
d.rectangle((mx, my, mx + mw, my + mh), outline=GRID, width=1)

# Bank logos, one per requested city (12 total).
logos = {
    'HSBC': load_logo('hsbc-logo.png', True),
    'BARCLAYS': load_logo('barclays-logo.jpg', True),
    'LLOYDS': load_logo('lloyds-bank-logo.png'),
    'NATWEST': load_logo('natwest-logo.png', True),
    'SG': load_logo('societe-generale-logo.png'),
    'BNP': load_logo('bnp-paribas-logo.png', True),
    'CA': load_logo('credit-agricole-cib-logo.png'),
    'NATIXIS': load_logo('natixis-logo.png'),
    'UBS': load_logo('ubs-logo.png', True),
    'CS': load_logo('credit-suisse-logo.png'),
    'JULIUS': load_logo('julius-baer-logo.png'),
    'PICTET': load_logo('pictet-logo.png'),
}

# Bank logos float directly on the map; city-name labels are intentionally omitted.
def place_bank(key, lon, lat, logo_size, dx=0, dy=0, lloyds=False):
    global d
    anchor = xy(lon, lat)
    center = (anchor[0] + dx, anchor[1] + dy)
    if lloyds:
        paste_logo_floating(im, logos[key], (center[0] - 23, center[1]), (40, 35))
        d = ImageDraw.Draw(im)
        text(d, (center[0] + 22, center[1]), 'LLOYDS', 12, '#00843D', bold=True,
             anchor='mm', stroke_width=1)
    else:
        paste_logo_floating(im, logos[key], center, logo_size)

# UK
place_bank('NATWEST', -3.1883, 55.9533, (90, 28))
place_bank('BARCLAYS', -2.2426, 53.4808, (82, 36))
place_bank('LLOYDS', -1.8904, 52.4862, (88, 32), lloyds=True)
place_bank('HSBC', -0.1276, 51.5072, (92, 28), dy=-20)
# France
place_bank('BNP', 3.0573, 50.6292, (90, 40))
place_bank('SG', 2.3522, 48.8566, (105, 36))
place_bank('CA', 4.8357, 45.7640, (100, 30), dx=-120, dy=-27)
place_bank('NATIXIS', 5.3698, 43.2965, (105, 32), dx=20, dy=-20)
# Switzerland
place_bank('CS', 6.1432, 46.2044, (88, 25), dx=-4, dy=-38)
place_bank('JULIUS', 7.59, 47.56, (88, 25), dx=-50, dy=-25)
place_bank('UBS', 8.5417, 47.3769, (105, 38), dx=14)
place_bank('PICTET', 8.95, 46.0, (82, 24), dx=34, dy=12)

# An angular red plot marks the actual London desk location of the Adoboli event.
def event_plot(lon, lat, color, size=9):
    global d
    px, py = xy(lon, lat)
    d = ImageDraw.Draw(im)
    outer = [(px, py-size), (px+size, py), (px, py+size), (px-size, py)]
    inner = [(px, py-size+2), (px+size-2, py), (px, py+size-2), (px-size+2, py)]
    d.polygon(outer, fill=PAPER)
    d.polygon(inner, fill=color)

event_plot(-0.1276, 51.5072, '#E00000')

# Event highlights use floating type only, without boxes or bank-territory fills.
def event_text(x, y, label, amount, color, label_size, amount_size):
    global d
    d = ImageDraw.Draw(im)
    text(d, (x, y), label, label_size, color, bold=True, stroke_width=1)
    text(d, (x, y + label_size + 4), amount, amount_size, color, bold=True, stroke_width=1)

# Compact event callouts remain distinct from bank territory fills.
event_text(610, 403, 'BARINGS · 1995', 'USD -1.4bn', '#9A7000', 14, 26)
event_text(760, 520, 'KERVIEL · 2008', 'EUR -4.9bn', '#C1272D', 14, 30)
event_text(745, 332, 'ADOBOLI · 2011 · UBS', 'USD -2.3bn', '#E00000', 14, 32)

# Minimal footnote retains the factual distinction between Zurich HQ and the London desk.
d.line((42, 806, 1558, 806), fill=GRID, width=1)
text(d, (45, 815), "UBS's USD 2.3bn trading loss ranks among the most significant banking trading-loss events in Europe and illustrates how control failures can rapidly escalate into material financial and liquidity-management consequences.", 10, INK, bold=True)
text(d, (45, 841), "Source notes: FINMA · Société Générale · RBA / BoE inquiry. Adoboli's desk was London; Zurich is UBS group HQ. Barings is shown at its London home; Leeson's operation was Singapore.", 8, MUTED)

im.convert('RGB').save(OUT)
print(OUT)
