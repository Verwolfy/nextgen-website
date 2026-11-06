# Lot 108 — Sens inverse du téléscripteur arabe — 6 novembre 2026

## Demande
L'utilisateur veut que le défilement du bandeau arabe soit dans le sens opposé du français.

## Modification
- Français et anglais : piste continue de droite vers la gauche (direction d'animation normale).
- Arabe : piste continue de gauche vers la droite (direction d'animation inversée).
- La géométrie de la piste reste LTR pour éviter le bandeau vide corrigé au lot 107 ; le texte de chaque élément reste RTL pour l'arabe.
- L'animation se déplace de la largeur d'un groupe exactement. Les deux groupes jumeaux préservent le bouclage sans coupure. L'élément visuel peut provenir du groupe dupliqué mais celui-ci reste masqué aux technologies d'assistance.
- Le mode mouvement réduit ne défile pas ; sources, dates et expiration des faits, absence de liens, vidéo et boutons restent identiques.

## Tests
Recette Playwright FR/AR/EN sur mobile à 390px avec et sans réduction de mouvement : la présence visuelle de n'importe quelle information, absence de lien, et calcul de la variation réelle X à deux instants d'animation (arabe positif, autres négatif).

## Déploiement
Ne fusionner qu'après succès build/sécurité, Chromium et Lighthouse. Vérifier le SHA Cloudflare séparément après fusion.
