# Cours 2 : Produits dérivés et grecs

Un produit dérivé tire sa valeur d'un actif sous-jacent (action, indice, taux, change, matière première).

## 1. Contrats à terme (forwards et futures)

- **Forward** : engagement d'acheter ou vendre à une date future, à un prix fixé aujourd'hui.
- **Prix forward** (sans dividende) : F = S × (1 + r)^T.
- **Future** : forward standardisé, coté en bourse, avec appels de marge quotidiens.

## 2. Options

- **Call** : droit d'acheter le sous-jacent au prix d'exercice K.
- **Put** : droit de vendre le sous-jacent au prix K.
- **Valeur intrinsèque** : gain si on exerçait tout de suite. Call : max(S − K, 0). Put : max(K − S, 0).
- **Valeur temps** : prix de l'option − valeur intrinsèque.
- **Dans la monnaie (ITM)**, **à la monnaie (ATM)**, **hors de la monnaie (OTM)** : position de S par rapport à K.

## 3. Parité call-put (sans dividende)

**C − P = S − K × e^(−rT)**

Cette relation permet de vérifier la cohérence d'un prix d'option.

## 4. Black-Scholes

- C = S × N(d1) − K × e^(−rT) × N(d2)
- P = K × e^(−rT) × N(−d2) − S × N(−d1)
- d1 = [ln(S/K) + (r + σ²/2) × T] / (σ × √T)
- d2 = d1 − σ × √T

Où N est la fonction de répartition de la loi normale centrée réduite, σ la volatilité, T l'échéance.

## 5. Les grecs

| Grec | Mesure | Signe et ordre de grandeur |
|---|---|---|
| **Delta** | Sensibilité au sous-jacent | Call : entre 0 et 1. Put : entre −1 et 0. |
| **Gamma** | Variation du delta | Toujours positif pour une option achetée. Maximal à la monnaie. |
| **Vega** | Sensibilité à la volatilité | Positif pour une option achetée. Mesuré pour +1 % de volatilité. |
| **Theta** | Érosion du temps | Généralement négatif pour une option achetée. |
| **Rho** | Sensibilité aux taux | Positif pour un call, négatif pour un put. |

**Point clé** : une option achetée a un gamma et un vega positifs, et un theta négatif.

## 6. Swaps de taux

- **Swap de taux** : échange d'un taux fixe contre un taux variable (par exemple EURIBOR) sur un nominal.
- **Valeur à la conclusion** : proche de 0.
- **Valeur ultérieure** : valeur de la jambe fixe moins celle de la jambe variable (ou l'inverse selon la position).

## 7. CDS (Credit Default Swap)

- Protection contre le défaut d'un émetteur.
- L'acheteur de protection paie une **prime** (spread) périodique. Le vendeur paie en cas de défaut.

## 8. Options exotiques

- **Barrière** : l'option s'active (knock-in) ou se désactive (knock-out) si le sous-jacent touche un niveau.
- **Digitale (binaire)** : paiement fixe si la condition est remplie, sinon zéro.
- **Asiatique** : basée sur la moyenne du sous-jacent.
- **Lookback** : basée sur le maximum ou le minimum atteint pendant la vie de l'option.

## À retenir

Parité call-put, forme de Black-Scholes, signe des grecs, valeur intrinsèque et valeur temps.
