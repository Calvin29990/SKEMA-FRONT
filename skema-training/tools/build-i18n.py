#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-i18n.py — reconstruit assets/js/i18n.js depuis les sources de traduction.

Sources (à éditer à la main) :
  i18n/strings.tsv   clé française | english | español | português
  i18n/rules.tsv     langue | expression régulière | remplacement   (phrases dynamiques)
  tools/i18n.template.js   moteur (placeholders __DICT__ / __RAW__)

Usage :  python3 tools/build-i18n.py
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(ROOT, 'i18n', 'strings.tsv')
RULES = os.path.join(ROOT, 'i18n', 'rules.tsv')
TPL = os.path.join(ROOT, 'tools', 'i18n.template.js')
OUT = os.path.join(ROOT, 'assets', 'js', 'i18n.js')


def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u00a0', ' ')
    return re.sub(r'\s+', ' ', s).strip()


DICT = {'en': {}, 'es': {}, 'pt': {}}
dups = 0
for line in open(TSV, encoding='utf-8'):
    line = line.rstrip('\n')
    if not line.strip() or line.startswith('#'):
        continue
    parts = line.split('|')
    if len(parts) != 4:
        print('⚠ ligne ignorée (%d champs) : %s' % (len(parts), line[:70]))
        continue
    fr, en, es, pt = [p.replace('¦', '|').strip() for p in parts]
    key = norm(fr)
    if key in DICT['en']:
        dups += 1
    for lang, val in (('en', en), ('es', es), ('pt', pt)):
        if val and norm(val) != key:
            DICT[lang][key] = val

RAW = {'en': [], 'es': [], 'pt': []}
for line in open(RULES, encoding='utf-8'):
    line = line.rstrip('\n')
    if not line.strip() or line.startswith('#'):
        continue
    lang, rx, to = line.split('|')
    RAW[lang.strip()].append({'re': rx, 'to': to})

tpl = open(TPL, encoding='utf-8').read()
js = tpl.replace('__DICT__', json.dumps(DICT, ensure_ascii=False).replace('\n', '')) \
        .replace('__RAW__', json.dumps(RAW, ensure_ascii=False).replace('\n', ''))
open(OUT, 'w', encoding='utf-8').write(js)

print('i18n.js reconstruit : %.1f Ko' % (os.path.getsize(OUT) / 1024))
for lang in DICT:
    print('  %s : %d chaînes · %d règles' % (lang, len(DICT[lang]), len(RAW[lang])))
if dups:
    print('  (%d clé(s) en doublon — la dernière gagne)' % dups)
