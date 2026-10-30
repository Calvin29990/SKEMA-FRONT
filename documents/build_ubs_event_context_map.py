from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

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
# Zoomed regional view centred on France, with the UK and Switzerland retained for context.
mx, my, mw, mh = 190, 105, 1220, 680
lon0, lon1 = -7.5, 14.0
lat0, lat1 = 41.5, 57.0

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

# France remains grey except for the two requested administrative areas.
regions_path = ASSETS / 'france-regions.geojson'
with regions_path.open(encoding='utf-8') as handle:
    regions = json.load(handle)
region_style = {
    'Île-de-France': ('#E98C94', '#E30613'),
    'Provence-Alpes-Côte d\'Azur': ('#A783C9', '#6F2DA8'),
}
region_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
rd = ImageDraw.Draw(region_layer)
for feature in regions['features']:
    geometry = feature['geometry']
    polygons = geometry['coordinates'] if geometry['type'] == 'MultiPolygon' else [geometry['coordinates']]
    name = feature['properties']['nom']
    fill = region_style.get(name, (LAND, '#FFFFFF'))[0]
    for polygon in polygons:
        ring = polygon[0]
        points = [xy(lon, lat) for lon, lat in ring]
        rd.polygon(points, fill=fill)
im.alpha_composite(region_layer)
# Keep boundaries legible and give the two highlighted territories a clear coloured edge.
d = ImageDraw.Draw(im)
for feature in regions['features']:
    geometry = feature['geometry']
    polygons = geometry['coordinates'] if geometry['type'] == 'MultiPolygon' else [geometry['coordinates']]
    name = feature['properties']['nom']
    outline = region_style.get(name, (LAND, '#FFFFFF'))[1]
    width = 3 if name in region_style else 2
    for polygon in polygons:
        ring = polygon[0]
        points = [xy(lon, lat) for lon, lat in ring]
        d.line(points + [points[0]], fill=outline, width=width, joint='curve')

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
        paste_logo_floating(im, logos[key], (center[0] - 19, center[1]), (32, 29))
        d = ImageDraw.Draw(im)
        text(d, (center[0] + 18, center[1]), 'LLOYDS', 11, '#00843D', bold=True,
             anchor='mm', stroke_width=1)
    else:
        paste_logo_floating(im, logos[key], center, logo_size)

# UK
place_bank('NATWEST', -3.1883, 55.9533, (80, 24))
place_bank('BARCLAYS', -2.2426, 53.4808, (68, 31))
place_bank('LLOYDS', -1.8904, 52.4862, (78, 30), lloyds=True)
place_bank('HSBC', -0.1276, 51.5072, (82, 25))
# France
place_bank('BNP', 3.0573, 50.6292, (74, 34))
place_bank('SG', 2.3522, 48.8566, (91, 32))
place_bank('CA', 4.8357, 45.7640, (88, 24), dx=-57, dy=23)
place_bank('NATIXIS', 5.3698, 43.2965, (100, 30), dx=20, dy=-20)
# Switzerland
place_bank('CS', 6.1432, 46.2044, (88, 25), dx=6, dy=-24)
place_bank('JULIUS', 7.59, 47.56, (84, 25), dx=-33, dy=-39)
place_bank('UBS', 8.5417, 47.3769, (108, 40), dx=34, dy=3)
place_bank('PICTET', 8.95, 46.0, (88, 25), dx=5, dy=3)

# Event highlights use floating type only, without circles or containers.
def event_text(x, y, label, amount, color, label_size, amount_size):
    global d
    d = ImageDraw.Draw(im)
    text(d, (x, y), label, label_size, color, bold=True, stroke_width=3)
    text(d, (x, y + label_size + 5), amount, amount_size, color, bold=True, stroke_width=3)

# Barings 1995 — third in the visual hierarchy, with gold event type near London.
event_text(425, 365, 'BARINGS · 1995', 'USD -1.4bn', '#9A7000', 16, 30)
# Kerviel 2008 — second-largest red event emphasis beside the Paris / SG marker.
event_text(560, 520, 'KERVIEL · 2008', 'EUR -4.9bn', '#C1272D', 18, 38)
# Adoboli 2011 — largest callout, with the requested UBS-red accent by Zurich.
event_text(1205, 455, 'ADOBOLI · 2011', 'USD -2.3bn', '#E00000', 19, 42)

# Minimal footnote retains the factual distinction between Zurich HQ and the London desk.
d.line((42, 806, 1558, 806), fill=GRID, width=1)
text(d, (45, 815), "UBS's USD 2.3bn trading loss ranks among the most significant banking trading-loss events in Europe and illustrates how control failures can rapidly escalate into material financial and liquidity-management consequences.", 10, INK, bold=True)
text(d, (45, 841), "Source notes: FINMA · Société Générale · RBA / BoE inquiry. Adoboli's desk was London; Zurich is UBS group HQ. Barings is shown at its London home; Leeson's operation was Singapore.", 8, MUTED)

im.convert('RGB').save(OUT)
print(OUT)
