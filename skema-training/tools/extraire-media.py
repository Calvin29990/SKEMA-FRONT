#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extraire-media.py — extrait le texte et les images d'un .docx (archive ZIP), hors ligne.

Usage :
    python3 tools/extraire-media.py "<fichier.docx>" [dossier de sortie]

Par défaut la sortie va dans perso/doc-media/ (dossier ignoré par git et par build.py).
Un .docx est un ZIP : les images sont dans word/media/, le texte dans word/document.xml.
"""
import os, re, sys, zipfile

DOCX = sys.argv[1] if len(sys.argv) > 1 else None
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'perso', 'doc-media')
IMG = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.emf', '.wmf', '.tif', '.tiff', '.webp')

if not DOCX or not os.path.isfile(DOCX):
    sys.exit('Usage : python3 tools/extraire-media.py "<fichier.docx>" [sortie]')

os.makedirs(OUT, exist_ok=True)
z = zipfile.ZipFile(DOCX)
noms = z.namelist()

# ── images ──
media = [n for n in noms if n.lower().startswith('word/media/') and n.lower().endswith(IMG)]
for n in media:
    cible = os.path.join(OUT, os.path.basename(n))
    with z.open(n) as src, open(cible, 'wb') as dst:
        dst.write(src.read())

# ── texte (paragraphes de word/document.xml) ──
txt = ''
if 'word/document.xml' in noms:
    xml = z.read('word/document.xml').decode('utf-8', 'ignore')
    xml = re.sub(r'</w:p>', '\n', xml)
    xml = re.sub(r'<w:tab[^>]*/>', '\t', xml)
    txt = re.sub(r'<[^>]+>', '', xml)
    txt = re.sub(r'\n{3,}', '\n\n', txt).strip()
    open(os.path.join(OUT, 'texte-extrait.txt'), 'w', encoding='utf-8').write(txt + '\n')

print('document    : %s (%.1f Mo)' % (os.path.basename(DOCX), os.path.getsize(DOCX) / 1e6))
print('images      : %d fichier(s) -> %s' % (len(media), OUT))
print('texte       : %d caractères' % len(txt))
if media:
    total = sum(os.path.getsize(os.path.join(OUT, os.path.basename(n))) for n in media)
    print('poids images: %.1f Mo' % (total / 1e6))
    print('premières   : %s' % ', '.join(os.path.basename(n) for n in media[:8]))
