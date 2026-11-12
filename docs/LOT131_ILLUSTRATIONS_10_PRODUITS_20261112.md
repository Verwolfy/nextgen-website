# Lot 131 — illustrations FENEK de meilleure qualité, 10 références (12 novembre 2026)

## Objectif
La génération de visuels ne vaut PAS publication : ce lot connecte de véritables fichiers WebP de haute qualité au composant Astro, dans chacune des six étapes de la référence exacte.

## Produits / ordre
BOND-C1T, BOND-C1TE, BOND-C2FT, BOND-C2TE, BOND-C2TE-S1, BOND-CG1, BOND-CG2WA, BOND-CT-C25-F5, BOND-R2, BOND-R3.

## Réalisation
- 10 planches générées puis contrôlées, découpées en **60 scènes sans titres intégrés** et assemblées en 10 sprites 3×2 de 1620×720, soit 540×360 par illustration ; format WebP optimisé, environ 1,12 Mo au total.
- Fichiers réels dans `public/images/application-upgraded/<slug>-steps.webp`.
- Le nouveau registre `src/data/fenek-enhanced-artwork.json` impose code, slug, sha256, statut BROUILLON.
- `FenekApplicationGuide.astro` choisit l'image améliorée **uniquement** en présence d'une correspondance exacte code+slug avec un guide V3 existant.
- CSS adapté au format paysage 3:2, y compris mobile. Les légendes HTML FR/AR/EN restent sélectionnables et ne sont pas intégrées dans le raster.
- Les 50 sprites V3 historiques, leurs SHA-256, les notices et mentions de prudence sont conservés, ce qui protège les 40 références encore non améliorées.
- **BOND-C2TE, étape 4 :** une proposition générée contenait « 3–5 min » non documenté. Cette sous-image a été écartée et remplacée par le dessin de malaxage sans valeur chiffrée, sans changer la notice spécifique.
- Tests : correspondance code/slug, 10 fichiers WebP et SHA, 60 étapes, exactitude de l'insertion ; navigateur vérifie l'image réellement peinte et ses proportions pour mobile/ordinateur.

## Statut
Code et médias livrés sur une branche/PR : ne déclarer le lot en production qu'une fois les contrôles CI réussis, la PR fusionnée, le déploiement Cloudflare achevé et le site public contrôlé.

## Suite
Traiter par lot les 40 autres produits en suivant les mêmes critères. **Une image générée seule ne compte pas comme un produit corrigé sur le site**.
