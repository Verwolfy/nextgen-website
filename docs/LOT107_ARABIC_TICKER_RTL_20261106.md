# Lot 107 — Correctif du téléscripteur arabe RTL, 6 novembre 2026

## Incident confirmé
Capture utilisateur : version arabe affiche un bandeau d'actualité blanc/vide alors que la vidéo et le bouton sont présents.

## Diagnostic technique
Le conteneur complet est en RTL (nécessaire pour les commandes AR), tandis que la piste du téléscripteur avait `width:max-content` et un défilement CSS `translateX(-50%)` inversé par `animation-direction:reverse`. En RTL, la piste peut être initialement positionnée hors de la fenêtre `overflow:hidden`.

## Correction
- Géométrie de la fenêtre, de la piste et des groupes de news explicitement LTR, assurant que la première information reste dans le viewport dès le chargement.
- Chaque information conserve sa direction RTL et ses traductions quand la langue est arabe.
- Défilement uniforme pour les trois langues ; aucun lien d'actualité.
- Aucune modification aux données, sources et expirations du lot 106, vidéo, poster, commandes, catégories, noindex ou Cloudflare.
- Test navigateur dédié dans la recette Playwright : présence visible géométrique de l'item en FR/AR/EN sur 390 px, en mode reduced motion ; vérification non-cliquable.

## Validation et publication
CI build/sécurité, Playwright et Lighthouse avant fusion ; puis recontrôle après fusion. Publication Cloudflare à vérifier séparément sur SHA final. Tests CI ne prouvent pas à eux seuls la nouvelle version publiée sur le domaine officiel.
