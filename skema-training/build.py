#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — régénère les deux livrables publiés depuis les sources de skema-training :

  1. skema-training/standalone/index.html   version « fichier unique » (CSS + JS inlinés)
                                            -> sert au lien htmlpreview / githack
  2. docs/                                  copie publique assainie pour GitHub Pages
  3. /home/user/Assessment-Trainer-Calvin.zip  copie hors-ligne

Usage :  python3 skema-training/build.py
"""
import json, os, re, shutil, zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
DOCS = os.path.join(REPO, 'docs')
STANDALONE = os.path.join(ROOT, 'standalone')
PUB = '/tmp/skema-pub'          # copie publique temporaire
JS = ['util.js', 'banks.js', 'drills.js', 'numverb.js', 'core.js', 'i18n.js', 'app.js']
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
shutil.copytree(ROOT, PUB, ignore=shutil.ignore_patterns('standalone', '.git', 'build.py', 'i18n', 'tools',
                                                         'perso', 'perso-*', '*.perso.json'))

# ── 2. assainissement pour la version publique ─────────────────────────
def edit(path, pairs):
    full = os.path.join(PUB, path)
    s = open(full, encoding='utf-8').read()
    for a, b in pairs:
        if a not in s:
            print('   ⚠ non trouvé dans %s : %s' % (path, a[:50]))
        s = s.replace(a, b)
    open(full, 'w', encoding='utf-8').write(s)

edit('assets/js/app.js', [
    ("'<p class=\"tiny dim sp\">Test cible (BNP Paribas) : du 7 au 9 octobre — ' +", "'<p class=\"tiny dim sp\">Prochaine échéance : ' +"),
    ("Importez ici les captures du dossier Drive <i>« DOC IMPORTANT base Entretien front »</i>. ", "Importez ici vos captures d’écran de référence. "),
    ("<div class=\"card-t\">Méthode — rappel du dossier source</div>", "<div class=\"card-t\">Méthode</div>"),
])
# dictionnaire de traduction : mêmes remplacements (les clés doivent correspondre au texte affiché)
edit('assets/js/i18n.js', [
    ("Test cible (BNP Paribas) : du 7 au 9 octobre", "Prochaine échéance"),
    ("Test cible \\\\(BNP Paribas\\\\) : du 7 au 9 octobre", "Prochaine échéance"),
    ("Variante « capacité de concentration » du dossier SKEMA.", "Variante « capacité de concentration »."),
    ("Format proche de Morgan Stanley.", ""),
    ("Importez ici les captures du dossier Drive", "Importez ici vos captures d’écran de référence"),
    ("DOC IMPORTANT base Entretien front", "Référence"),
])
edit('assets/js/core.js', [
    ("Variante « capacité de concentration » du dossier SKEMA.", "Variante « capacité de concentration »."),
    ("Format proche de Morgan Stanley.", ""),
    ("dossier source", "repères de méthode"),
])
open(os.path.join(PUB, 'robots.txt'), 'w').write('User-agent: *\nDisallow: /\n')
open(os.path.join(PUB, '.nojekyll'), 'w').write('')

# ── 3. version fichier unique ──────────────────────────────────────────
idx = open(os.path.join(PUB, 'index.html'), encoding='utf-8').read()
css = open(os.path.join(PUB, 'assets/css/styles.css'), encoding='utf-8').read()
scripts = {f: open(os.path.join(PUB, 'assets/js', f), encoding='utf-8').read() for f in JS}
assert '</script' not in ''.join(scripts.values()), 'un script contient </script'
assert '</style' not in css, 'le CSS contient </style'
out = idx.replace('<link rel="stylesheet" href="assets/css/styles.css">', '<style>\n' + css + '\n</style>')
for f, code in scripts.items():
    tag = '<script src="assets/js/%s"></script>' % f
    assert tag in out, 'balise absente : ' + tag
    out = out.replace(tag, '<script>\n' + code + '\n</script>')
os.makedirs(STANDALONE, exist_ok=True)
open(os.path.join(STANDALONE, 'index.html'), 'w', encoding='utf-8').write(out)
print('standalone/index.html : %.1f Ko' % (len(out.encode()) / 1024))

# ── 4. dossier public docs/ ────────────────────────────────────────────
if os.path.exists(DOCS):
    shutil.rmtree(DOCS)
shutil.copytree(PUB, DOCS)
open(os.path.join(DOCS, 'README.md'), 'w', encoding='utf-8').write(
    "# Assessment Trainer\n\n"
    "Plateforme d'entraînement aux tests d'aptitude utilisés dans les processus de sélection bancaires :\n"
    "raisonnement numérique et verbal, déductif et inductif, switch challenge, concentration, efficacité\n"
    "d'apprentissage, mémoire de travail, traitement de l'information, raisonnement mécanique,\n"
    "questionnaires de comportement professionnel et de motivation.\n\n"
    "## Accès\n\nCode d'accès + prénom. Historique horodaté, progression et feedback detaille, conserves\n"
    "uniquement dans le navigateur de l'appareil.\n\n"
    "## Contenu personnel\n\nLa tache Numerical Reasoning accepte un fichier JSON local (bouton\n"
    "« Ouvrir mon fichier ») : il est lu sur l'appareil, jamais envoye ni publie.\n\n"
    "## Langues\n\nInterface et feedback en **français, anglais, espagnol et portugais** (sélecteur en haut à droite).\n\n"
    "## Contenu\n\n- 13 sections + 1 simulation complète en conditions d'examen\n"
    "- Banques figées (mêmes items à chaque session) et batterie anglaise illimitée\n"
    "- Feedback détaillé question par question (réponse donnée, réponse correcte, temps, heure, explication) + export CSV\n"
    "- Progression : sessions, précision, tendances, heatmap 30 jours, export JSON\n\n"
    "## Confidentialité\n\nTout est stocké localement dans le navigateur (`localStorage` + `IndexedDB`). Aucune donnée transmise.\n\n"
    "---\n\n*Espace personnel d'entraînement.*\n")
print('docs/ : %d fichiers' % sum(len(f) for _, _, f in os.walk(DOCS)))

# ── 4bis. contrôle anti-fuite : aucune phrase du contenu perso dans les livrables ──
#     Sont ignorées les tournures déjà présentes dans la banque intégrée (sources du dépôt) :
#     seules les phrases absentes du contenu de base comptent comme une fuite.
TEXTES = ('.json', '.md', '.txt', '.tsv', '.csv', '.html', '.js')
builtin = ''
# liste blanche = sources écrites à la main, telles que COMMITÉES (une injection locale ne peut
# donc pas se blanchir elle-même) ; standalone/ et docs/ sont exclus : ce sont des livrables.
import subprocess
try:
    suivis = subprocess.run(['git', '-C', REPO, 'ls-files'], capture_output=True, text=True).stdout.split()
except Exception:
    suivis = []
for rel in suivis:
    if not os.path.exists(os.path.join(REPO, rel)):   # supprimé du dépôt -> hors liste blanche
        continue
    if os.path.basename(rel).startswith('verbal-reel'):
        continue
    if not rel.endswith(TEXTES) or rel.startswith(('standalone/', 'docs/')):
        continue
    try:
        builtin += subprocess.run(['git', '-C', REPO, 'show', 'HEAD:' + rel],
                                  capture_output=True, text=True).stdout
    except Exception:
        pass

def leaks_in(path):
    try:
        txt = open(path, encoding='utf-8').read()
    except Exception:
        return []
    return [n for n in needles if n in txt]

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
        if n and n not in needles and n not in builtin:   # absent de la banque intégrée
            needles.append(n)

if not priv_files:
    print('anti-fuite : rien à contrôler (perso/ vide)')
else:
    cibles = [os.path.join(STANDALONE, 'index.html'), os.path.join(DOCS, 'index.html')]
    cibles += [os.path.join(DOCS, 'assets', 'js', f) for f in JS]
    fuites = {c: leaks_in(c) for c in cibles}
    fuites = {c: v for c, v in fuites.items() if v}
    refs = [n for n in needles if any(n in open(c, encoding='utf-8', errors='ignore').read() for c in cibles)]
    if fuites or refs:
        raise SystemExit('ARRÊT : contenu perso détecté dans un livrable public -> %s' % (fuites or refs[:3]))
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
