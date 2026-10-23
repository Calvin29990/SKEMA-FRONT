# Audit critique de la carte — 23/10/2026

Objet : contester chaque donnée affichée sur `assets/10-carte-clubs-couleurs.png`, pas la valider.
Méthode : recoupement systématique de la source primaire (Sportune, 02/09/2026, d'après Transfermarkt)
avec L'Équipe, RMC Sport, la presse club, et les communiqués officiels des clubs et des fintechs.

---

## 1. Verdict en trois lignes

1. **Les soldes de transferts sont globalement solides** — mais **un est faux** (Lens), **un est trop précis** (Strasbourg) et **un mélange deux dates** (Lens encore).
2. **La couche « partenaire FX » est le point faible** : elle décrit la saison 2025/2026, pas 2026/2027. Trois des quatre partenariats affichés ne sont pas reconduits publiquement.
3. **Reims n'a rien à faire sur cette carte** : le club est en Ligue 2, et le partenariat Ebury date de 2023, pas de 2025.

**En l'état, je ne publierais pas.** Trois corrections suffisent à la rendre défendable (section 5).

---

## 2. Le point de départ : d'où viennent les montants

Le tableau de référence (Sportune, 02/09/2026, chiffres Transfermarkt) donne en clair :

| Club | Dépenses | Recettes | Solde |
|---|---|---|---|
| Paris Saint-Germain | 152,00 M€ | 334,30 M€ | **+182,30 M€** |
| LOSC Lille | 42,10 M€ | 162,50 M€ | **+120,40 M€** |
| RC Strasbourg | 99,40 M€ | 200,85 M€ | **+101,45 M€** |

Et en corps de texte : Monaco **+56 M€**, Marseille **+49,9 M€**, Lyon **+44 M€**.
La page 2 de l'article (tableau complet) n'est pas accessible en ligne : **huit clubs de la carte
reposent donc sur une source unique que je n'ai pas pu ouvrir directement**. C'est une limite de
l'audit, pas une validation.

---

## 3. Club par club

Légende confiance : 🟢 élevé · 🟠 moyen · 🔴 faible

| Club | Solde carte | Recoupement | Conf. | Partenaire affiché | Documentation | Conf. | Verdict |
|---|---|---|---|---|---|---|---|
| **PSG** | +182,3 M€ | Sportune 152,0/334,3 ; L'Équipe « 334 M€ de ventes, +182 M€ » ; Lensois.com même chiffre | 🟢 | aucun | QNB est partenaire banquier depuis 2011, mais jamais présenté comme partenaire FX | 🟠 | **Publier**, en précisant « bonus inclus » (Barcola 125 M€ + 20 M€ de bonus) |
| **LOSC** | +120,4 M€ | Sportune 42,1/162,5 ; L'Équipe 163 M€ de ventes ; sports.fr +120,4 | 🟢 | aucun | rien de public | 🟠 | **Publier** |
| **Strasbourg** | +101,5 M€ | Sportune 99,4/200,85. Mais L'Équipe « environ 100 », Alsa'Sports « environ 107 », Dicodusport 106, TV5 « près de 90 », Pronor +122,45 | 🟠 | aucun | rien de public | 🟠 | **Publier arrondi : « ≈ +100 M€ »**. Le demi-million est une fausse précision : la dispersion réelle est de ±10 M€ |
| **Paris FC** | −72,2 M€ | Sportune ; Pronor −72,20 (9 arrivées / 8 départs) ; L'Équipe « plus de 70 M€ » | 🟢 | aucun | rien de public | 🟠 | **Publier** — c'est même le chiffre le mieux corroboré de la carte |
| **OM** | +49,9 M€ | Sportune +49,9 ; RMC Sport « près de 50 M€ » ; 0 recrue confirmée par RMC, L'Équipe, Onze Mondial | 🟢 | Ebury | Communiqué OM 07/01/2026, La Provence 13/01, Sponsoring.fr : « fournisseur officiel » **saison 2025-2026** | 🟢 existence / 🔴 actualité | **Publier en datant** : « Ebury (2025/26) » |
| **OL** | +44,0 M€ | Sportune (texte) | 🟠 | Ebury | Communiqué OL 28/10/2025 : partenariat « au terme du 30 juin 2026 » | 🟢 existence / 🔴 actualité | **Publier en datant**. Aucune reconduction 2026/27 trouvée ; l'OL a signé XTB en août 2026, mais c'est un courtier, pas du change |
| **Monaco** | +56,0 M€ | Sportune +56 ; arithmétiquement cohérent (≈104 M€ de ventes − 48 M€ d'achats) | 🟢 | « Ebury · Sokin » | Ebury : saison **2024/2025** uniquement. Sokin : 3 ans **2021 → juin 2024** | 🔴 | **Retirer les deux.** Afficher Sokin à côté d'Ebury laisse croire à deux partenaires actifs : c'est un contrat mort depuis deux ans |
| **Lens** | +46,7 M€ | **Contredit** : RCLensois et Lensois.com (03/09) donnent 71,2 M€ de ventes / 27 M€ d'achats = **+44,2 M€** | 🔴 | aucun | rien de public | 🟠 | **Corriger en +44,2 M€.** Le +46,7 est la valeur au 11 août, avant la fin de la fenêtre |
| **Rennes** | +33,7 M€ | RMC : Jacquet 70 M€ à Liverpool ; Morning Foot : 36,8 M€ investis → ≈ +33,7 cohérent | 🟠 | aucun | rien de public | 🟠 | **Publier** — cohérent, mais à confirmer sur le tableau complet |
| **Nice** | +14,9 M€ | Source unique, non rouverte | 🟠 | aucun | rien de public | 🟠 | **Publier avec prudence** ou vérifier avant |
| **Toulouse** | +25,5 M€ | Source unique ; 59 M€ de ventes selon Alsa'Sports | 🟠 | Corpay | Communiqué TFC + Business Wire, 23/04/2026, **pluriannuel**, « Official FX Supplier » via SPORTFIVE | 🟢 | **Publier** : c'est le seul partenariat FX à la fois documenté et valide pour la saison en cours |
| **Reims** | n.d. | Sans objet | — | Ebury | Annonce du **10 août 2023** (pas juillet 2025), sponsor maillot saison 2023/24 ; depuis, Hexaom (mars 2026) puis Burger King (août 2026) | 🔴 | **Retirer.** Club en Ligue 2 depuis 2025-26, hors périmètre, et partenariat non actualisé |

---

## 4. Les quatre erreurs à ne pas publier

### 4.1 Lens : +46,7 M€ est périmé
Deux sources locales indépendantes donnent **71,2 M€ de ventes et 27 M€ d'achats, soit +44,2 M€**.
Le +46,7 correspond à un relevé au 11 août, avant la clôture. Écart faible (2,5 M€) mais c'est une
erreur de date, pas d'arrondi : sur une carte qui prétend refléter la clôture, c'est le genre de détail
qu'un supporter lensois relèvera en commentaire.

### 4.2 Strasbourg : +101,5 M€ est une fausse précision
Cinq estimations publiques s'échelonnent entre 90 et 122 M€. Publier 101,5 au dixième près, c'est
donner une autorité que la donnée n'a pas. Écrire « ≈ +100 M€ » est plus honnête et aussi plus lisible.

### 4.3 Reims : mauvais championnat, mauvaise date
Le club évolue en Ligue 2 depuis 2025-26 (17e de L1 en 2025, puis deux saisons de L2). Le fichier
source `data/clubs_partenaires_fx.csv` indique « 2025/2026 · 2025-07-09 » : **c'est faux**, l'annonce
Ebury date du 10 août 2023, pour la saison 2023/24. Depuis, le maillot rémois a porté Hexaom puis
Burger King. Afficher « Reims · Ebury » en 2026 est une erreur factuelle, pas une approximation.

### 4.4 Monaco : Sokin n'existe plus
Sokin a signé trois saisons à partir du 1er juillet 2021, donc jusqu'en juin 2024. Ebury a pris le
relais pour la seule saison 2024/25. En octobre 2026, **aucun des deux n'est documenté comme actif**.
Les afficher ensemble construit une continuité qui n'existe pas.

---

## 5. Corrections proposées avant publication

| Élément | Aujourd'hui | Proposition |
|---|---|---|
| Lens | +46,7 M€ | **+44,2 M€** |
| Strasbourg | +101,5 M€ | **≈ +100 M€** |
| Reims | logo + « n.d. » + Ebury | **supprimé** (hors L1, partenariat expiré) |
| Monaco | « Ebury · Sokin » | **« — »** ou mention « Ebury (2024/25) » si on veut garder la trace |
| OM / OL | « Ebury » | **« Ebury (2025/26) »** |
| Toulouse | « Corpay » | inchangé |
| Pied de page | Orbis · INSEE · sites des clubs et fintechs | **+ « Transfermarkt via Sportune / L'Équipe, 02/09/2026 »** — c'est la source réelle des montants, elle est absente |
| Note de bas de carte | « Montants = solde mercato été 2026 » | « Soldes arrêtés au 1er septembre 2026, bonus inclus selon sources » |

Résultat : **10 clubs au lieu de 12**, un chiffre corrigé, un chiffre arrondi, des partenariats datés.
La carte perd deux blasons et gagne en tenue.

---

## 6. Ce que je contesterais aussi, sans pouvoir trancher

- **Les « aucun partenaire FX identifié »** : c'est une affirmation négative, donc fragile par nature.
  Le PSG a QNB (banque, partenaire depuis 2011), l'OM a la CEPAC en partenaire premium. Aucun n'est
  présenté comme partenaire *FX*, mais la frontière dépend de la définition. La formulation actuelle
  (« identifié ») est la bonne : ne pas la durcir en « aucun partenaire ».
- **Le total de la Ligue 1** : 730 M€ selon L'Équipe et Lensois.com, 634,75 M€ selon Sportune,
  614,75 M€ selon Sport.fr. Trois chiffres pour un même mercato, à cause des prêts et des bonus.
  Si le post cite un total, il doit nommer sa source et sa méthode.
- **Les 18 clubs** : la carte n'en montre que 11 (plus Reims). Les sept absents (Auxerre, Le Havre,
  Lorient, Le Mans, Metz, Angers, Brest) doivent être annoncés comme tels, sinon la carte laisse
  croire à une exhaustivité qu'elle n'a pas.
- **La date Orbis (20/10/2026)** : valable pour la couche entreprises, sans rapport avec les montants
  de transferts. Ne pas laisser croire que les soldes viennent d'Orbis.

---

## 7. Ce qui tient très bien

- **Paris FC −72,2 M€** : trois sources convergent, c'est le chiffre le plus sûr de la carte.
- **PSG +182,3 M€** : deux rédactions indépendantes, même base Transfermarkt.
- **LOSC +120,4 M€** : idem, avec Bouaddi à 95-100 M€ selon les sources (écart assumé).
- **Toulouse / Corpay** : le seul partenariat FX documenté, pluriannuel et toujours valide.

---

## 8. Sources

- Sportune / 20 Minutes, « La balance des transferts des clubs de Ligue 1 », 02/09/2026
- L'Équipe, « Ventes records au mercato d'été : 730 M€ de balance positive », 02/09/2026
- L'Équipe, « Le Mans économe, Paris FC dépensier et Strasbourg mouvementé », 02/09/2026
- RMC Sport, bilan mercato OM (« près de 50 M€ »), 02/09/2026 ; RMC Sport, bilan Stade Rennais, 01/09/2026
- RCLensois et Lensois.com, bilan RC Lens (+44,2 M€), 03/09/2026
- Alsa'Sports, Dicodusport, TV5 Monde, Sport.fr, Pronor (fourchettes Strasbourg et PSG)
- ol.fr (28/10/2025), laprovence.com (13/01/2026), sponsoring.fr (07/01/2026), asmonaco.com (10/09/2024 et 08/06/2021), stade-de-reims.com (10/08/2023 et 02/08/2026), toulousefc.com et Business Wire (23/04/2026)
- psg.fr, « Les partenaires du Paris Saint-Germain » (QNB, partenaire depuis 2011)
