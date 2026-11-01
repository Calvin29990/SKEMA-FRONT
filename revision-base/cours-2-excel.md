# Cours 2 : Excel avancé

## 1. Références de cellules

- **A1** : référence relative (change quand on copie la formule).
- **$A$1** : référence absolue (ne change pas).
- **$A1** ou **A$1** : référence mixte.
- Raccourci : **F4** alterne entre les types de référence.

## 2. Fonctions de recherche

- **RECHERCHEV(valeur; plage; n° colonne; FAUX)** : cherche une valeur dans la première colonne et renvoie une valeur de la même ligne. Le dernier argument **FAUX** impose une correspondance exacte.
- **INDEX(plage; ligne; colonne)** combiné à **EQUIV(valeur; plage; 0)** : alternative plus souple, qui permet de chercher à gauche.
- **XRECHERCHE** : version moderne, qui remplace RECHERCHEV.

## 3. Fonctions conditionnelles

- **SI(condition; valeur si vrai; valeur si faux)**.
- **SI imbriqués** : plusieurs conditions en cascade.
- **SOMME.SI(plage; critère; somme_plage)** : somme conditionnelle.
- **SOMME.SI.ENS(somme_plage; plage1; critère1; plage2; critère2)** : plusieurs critères.
- **NB.SI** et **NB.SI.ENS** : compter avec critères.
- **MOYENNE.SI** : moyenne avec critère.
- **SIERREUR(formule; valeur_si_erreur)** : masque les erreurs.

## 4. Fonctions de calcul utiles

- **SOMME**, **MOYENNE**, **MIN**, **MAX**, **NB** (compte des nombres), **NBVAL** (compte des cellules non vides).
- **ARRONDI(nombre; décimales)**.
- **SI.ERREUR** n'existe pas : utilisez **SIERREUR**.

## 5. Tableaux et données

- **Filtre automatique** : Ctrl + Maj + L.
- **Tableau croisé dynamique (TCD)** : Insertion > Tableau croisé dynamique. Permet de regrouper et de totaliser sans formule.
- **Tri** : trier par colonne, ou sur plusieurs niveaux.
- **Mise en forme conditionnelle** : mettre en évidence les valeurs selon une règle.

## 6. Raccourcis utiles

- **Ctrl + flèche** : aller au bout d'une plage de données.
- **Alt + =** : somme automatique.
- **Ctrl + ;** : insérer la date du jour.
- **Ctrl + Entrée** : valider une formule dans plusieurs cellules sélectionnées.
- **Ctrl + Maj + flèche** : sélectionner jusqu'au bout d'une plage.

## 7. Méthode en épreuve

- Lisez la question en entier avant de toucher au clavier.
- Vérifiez la cohérence du résultat (ordre de grandeur, signe).
- Quand la formule renvoie une erreur, identifiez la cause : #N/A (valeur introuvable), #DIV/0! (division par zéro), #VALEUR! (type incorrect).

## À retenir

Références absolues avec F4, RECHERCHEV ou INDEX/EQUIV, SOMME.SI.ENS, NB.SI.ENS, TCD, et les erreurs courantes.
