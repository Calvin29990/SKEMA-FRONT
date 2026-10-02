#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — régénère les deux livrables publiés depuis les sources de skema-training :

  1. skema-training/standalone/index.html   version « fichier unique » (CSS + JS inlinés)
                                            -> sert au lien htmlpreview
  2. docs/                                  copie publique pour GitHub Pages
  3. /home/user/Assessment-Trainer-Calvin.zip  copie hors-ligne

Usage :  python3 skema-training/build.py
"""
import os, re, shutil, subprocess, zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
DOCS = os.path.join(REPO, 'docs')
STANDALONE = os.path.join(ROOT, 'standalone')
PUB = '/tmp/skema-pub'          # copie publique temporaire
JS = ['util.js', 'banks.js', 'drills.js', 'core.js', 'app.js']
PRIVATE = os.path.join(ROOT, 'perso')   # contenu personnel importé : JAMAIS publié

# ── 0. garde-fou : recenser le contenu personnel avant toute copie ─────
priv_files = []
if os.path.isdir(PRIVATE):
    for base, _dirs, files in os.walk(PRIVATE):
        priv_files += [os.path.join(base, f) for f in files if not f.startswith('.')]
print('contenu perso : %d fichier(s) dans perso/ (exclu des livrables)' % len(priv_files))

# ── 1. copie de travail ────────────────────────────────────────────────
if os.path.exists(PUB):
    shutil.rmtree(PUB)
shutil.copytree(ROOT, PUB, ignore=shutil.ignore_patterns('standalone', '.git', 'build.py', 'tools',
                                                         'perso', 'perso-*', '*.perso.json'))

# ── 2. fichiers techniques du dossier public ───────────────────────────
open(os.path.join(PUB, 'robots.txt'), 'w').write('User-agent: *\nDisallow: /\n')
open(os.path.join(PUB, '.nojekyll'), 'w').write('')

# ── 3. version fichier unique ──────────────────────────────────────────
idx = open(os.path.join(PUB, 'index.html'), encoding='utf-8').read()
css = open(os.path.join(PUB, 'assets/css/styles.css'), encoding='utf-8').read()
scripts = {f: open(os.path.join(PUB, 'assets/js', f), encoding='utf-8').read() for f in JS}
assert '</script' not in ''.join(scripts.values()), 'un script contient </script'
assert '</style' not in css, 'le CSS contient </style'
out = idx.replace('<link rel="stylesheet" href="assets/css/styles.css">', '<style>\n' + css + '\n</style>')
for f in JS:
    tag = '<script src="assets/js/%s"></script>' % f
    assert tag in out, 'balise absente : ' + tag
    out = out.replace(tag, '<script>\n' + scripts[f] + '\n</script>')
os.makedirs(STANDALONE, exist_ok=True)
open(os.path.join(STANDALONE, 'index.html'), 'w', encoding='utf-8').write(out)
print('standalone/index.html : %.1f Ko' % (len(out.encode()) / 1024))

# ── 4. dossier public docs/ ────────────────────────────────────────────
if os.path.exists(DOCS):
    shutil.rmtree(DOCS)
shutil.copytree(PUB, DOCS)
open(os.path.join(DOCS, 'README.md'), 'w', encoding='utf-8').write(
    "# Assessment Trainer\n\n"
    "Plateforme personnelle d'entraînement aux tests d'aptitude utilisés dans les processus\n"
    "de sélection (format cut-e / Aon) : comportements professionnels, motivations,\n"
    "raisonnement numérique, verbal, déductif, inductif et mécanique, concentration,\n"
    "multi-tâches, capacité d'apprentissage, traitement de l'information, compétences\n"
    "linguistiques anglais et français, switch challenge.\n\n"
    "## Chronomètres\n\n"
    "Durées de test officielles des formats Aon / cut-e : numérique 12:00 (37 tâches), verbal 12:00\n"
    "(49 tâches), déductif 6:00, inductif 6:00, concentration 2:00 (exemple 30 s), multi-tâches 5:00,\n"
    "apprentissage 5:00 (6 sections), traitement de l'information 15:00, langues 4:00 + 4:00 + 2:00,\n"
    "mécanique 15:00 (24 tâches), switchChallenge 6:00 ; comportements et motivations sans limite.\n\n"
    "## Utilisation\n\n"
    "Barre d'onglets Tâches / Progression / Feedback / Aide & réglages ; feedback en français\n"
    "(relecture question par question, filtre par épreuve) ; chronomètres standards sur toutes\n"
    "les épreuves sauf les questionnaires de personnalité ; feuilles de données et fiches de\n"
    "textes navigables librement ; banques extensibles : anglais / français, boîte de réception,\n"
    "déductif, inductif, concentration, multi-tâches et switch ne s'épuisent jamais.\n\n"
    "## Conformité\n\n"
    "Chaque épreuve reproduit le format réel décrit dans la documentation de référence :\n"
    "mêmes consignes, mêmes exemples, mêmes chronomètres, mêmes interactions\n"
    "(grille de navigation, pastilles 1-6, codes du switch challenge, boîte de réception…).\n"
    "Tout le contenu des questions est **original** (généré ou rédigé pour cette plateforme) :\n"
    "aucun item de test réel n'est reproduit.\n\n"
    "## Données\n\n"
    "Profils, historique horodaté, progression et feedback détaillé question par question\n"
    "(export CSV), sauvegarde JSON export/import. Tout est stocké localement dans le\n"
    "navigateur (`localStorage`) — aucune donnée n'est transmise.\n\n"
    "---\n\n*Espace personnel d'entraînement — Calvin MINANG.*\n")
print('docs/ : %d fichiers' % sum(len(f) for _, _, f in os.walk(DOCS)))

# ── 4bis. contrôle anti-fuite : aucune phrase du contenu perso dans les livrables ──
TEXTES = ('.json', '.md', '.txt', '.tsv', '.csv', '.html', '.js')
builtin = ''
try:
    suivis = subprocess.run(['git', '-C', REPO, 'ls-files'], capture_output=True, text=True).stdout.split()
except Exception:
    suivis = []
for rel in suivis:
    if not os.path.exists(os.path.join(REPO, rel)):
        continue
    if not rel.endswith(TEXTES) or rel.startswith(('skema-training/standalone/', 'docs/')):
        continue
    try:
        builtin += subprocess.run(['git', '-C', REPO, 'show', 'HEAD:' + rel],
                                  capture_output=True, text=True).stdout
    except Exception:
        pass

needles = []
for f in priv_files:
    if not f.endswith(TEXTES):
        continue
    try:
        raw = open(f, encoding='utf-8').read()
    except Exception:
        continue
    noms = [m.group(1).strip() for m in re.finditer(r'"((?:[^"\\]|\\.){24,})"', raw)]
    noms += [l.strip() for l in raw.splitlines() if len(l.strip()) > 40 and not l.strip().startswith(('#', '|', '-'))]
    for n in noms:
        if n and n not in needles and n not in builtin:
            needles.append(n)

if not priv_files:
    print('anti-fuite : rien à contrôler (perso/ vide)')
else:
    cibles = [os.path.join(STANDALONE, 'index.html'), os.path.join(DOCS, 'index.html')]
    cibles += [os.path.join(DOCS, 'assets', 'js', f) for f in JS]
    fuites = {}
    for c in cibles:
        try:
            txt = open(c, encoding='utf-8').read()
        except Exception:
            continue
        v = [n for n in needles if n in txt]
        if v:
            fuites[c] = v
    if fuites:
        raise SystemExit('ARRÊT : contenu perso détecté dans un livrable public -> %s' % fuites)
    print('anti-fuite : %d phrase(s) propre(s) au contenu perso vérifiée(s), aucune dans standalone/ ni docs/ ✔' % len(needles))

# ── 5. archive hors-ligne ──────────────────────────────────────────────
zip_path = '/home/user/Assessment-Trainer-Calvin.zip'
if os.path.exists(zip_path):
    os.remove(zip_path)
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in ('.git', 'perso')]
        for f in files:
            p = os.path.join(base, f)
            z.write(p, os.path.join('Assessment-Trainer', os.path.relpath(p, ROOT)))
print('ZIP : %.1f Ko' % (os.path.getsize(zip_path) / 1024))
