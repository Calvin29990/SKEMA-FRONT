#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
perso-fetch.py — récupère le document source et en extrait les images, en une commande.

Le document est récupéré depuis le dépôt (objet déjà envoyé par l'utilisateur), puis
décompressé dans perso/ (dossier ignoré par git et par build.py).

Usage :  python3 tools/perso-fetch.py [empreinte-du-blob]
"""
import os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = 'Calvin29990/SKEMA-FRONT'
BLOB = sys.argv[1] if len(sys.argv) > 1 else '25661ab617403d810ff3390945b77506ffb3aa0d'
DOCX = os.path.join(ROOT, 'perso', 'DOC-IMPORTANT.docx')

os.makedirs(os.path.dirname(DOCX), exist_ok=True)
if not os.path.isfile(DOCX) or os.path.getsize(DOCX) < 1000:
    print('récupération du document depuis le dépôt (blob %s...)' % BLOB[:12])
    with open(DOCX, 'wb') as out:
        r = subprocess.run(['gh', 'api', 'repos/%s/git/blobs/%s' % (REPO, BLOB),
                            '-H', 'Accept: application/vnd.github.raw'], stdout=out)
    if r.returncode != 0:
        sys.exit('échec de la récupération (gh api).')
    print('  -> %s (%.1f Mo)' % (DOCX, os.path.getsize(DOCX) / 1e6))
else:
    print('document déjà présent : %.1f Mo' % (os.path.getsize(DOCX) / 1e6))

subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'extraire-media.py'), DOCX], check=True)
