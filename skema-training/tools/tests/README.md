# Harnais de test (Chromium headless)

Ces tests pilotent la vraie plateforme dans un navigateur. Ils ne sont **jamais publiés**
(`tools/` est exclu de la version publique par `build.py`).

## Préparation (une fois par bac à sable, `/tmp` n'est pas conservé)

```bash
mkdir -p /tmp/jstest && cd /tmp/jstest
npm install --no-audit --no-fund puppeteer-core @sparticuz/chromium brotli
node -e "require('@sparticuz/chromium').default.executablePath().then(p=>console.log(p))"
# extraire le binaire + les bibliothèques al2023 (voir build_numverb/build history)
cp <ce dossier>/*.js .            # les trois harnais
mkdir -p fixtures && cp <ce dossier>/fixtures/*.json fixtures/
```

Serveur (racine = `skema-training/`) : `python3 -m http.server 8080 --bind 0.0.0.0`

## Exécution

```bash
export LD_LIBRARY_PATH=/tmp/al2023/lib:/tmp/al2023
node nv.js      # numerical au format réel : 6 onglets, 37 énoncés, 12 min, bascule auto
node perso.js   # chargeur de fichier local : validation, session, aucun envoi réseau
node e2e.js     # non-régression complète : accès, verbal, feedback, CSV, progression, i18n, livrables
```

## Ce que garantit chaque harnais

- **nv.js** — 16 vérifications : 6 onglets, true/false/cannot say, chrono global qui décompte
  (jamais remis à 12:00), bascule automatique sur l'onglet de chaque question, consultation
  manuelle d'un autre onglet, résumé de 37 lignes avec l'onglet, tentative horodatée, variante QCM.
- **perso.js** — 14 vérifications : fichier incomplet refusé avec la liste des erreurs, fichier
  valide chargé (onglets, énoncés, durée repris du fichier), session complète, tentative marquée
  `content: 'perso'`, **aucune requête réseau sortante**, retour à la banque intégrée.
- **e2e.js** — 34 vérifications : accès code + prénom, refus du mauvais code, voile modal,
  numerical, QCM Paper B, verbal + feedback, CSV, horodatage, progression, persistance après
  rechargement, EN/ES/PT/FR, thème sombre, standalone sans ressource externe, copie `docs/`
  sans contenu perso.

Les fixtures (`fixtures/perso-test.json`, `fixtures/mauvais.json`) sont des données inventées :
elles ne contiennent aucun contenu de test réel.
