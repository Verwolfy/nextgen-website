# Lots 155–159 — FENEK BOND, mortiers-colles pour carrelage
12 novembre 2026 · **BROUILLON**, non validé par laboratoire

## Livrables
Cinq références couvertes : `BOND-C1T`, `BOND-C1TE`, `BOND-C2TE`, `BOND-C2TE-S1`, `BOND-C2FT`. Chacune dispose de six illustrations vectorielles propres sous `public/images/application-professional/<slug>-steps.svg`, 1620×720, 3 colonnes × 2 lignes, 540×360 par case.

## Source et cohérence métier
Référentiel unique : `src/data/fenek-v3-manuals.json`; titres/descriptions FR, AR, EN affichés en HTML dans `FenekApplicationGuide.astro`. Six scènes par produit :
1. Nettoyage/contrôle du support ;
2. Gants, lunettes, masque ;
3. Ajout de l'eau suivant fiche technique (aucune quantité) ;
4. Repos/remalaxage pour C1T, C1TE, C2TE, C2TE-S1 ; remalaxage sans repos ajouté pour C2FT ;
5. Peignage à la spatule crantée ; cas C2TE-S1 : double encollage seulement si nécessaire, représenté conditionnellement ;
6. Pose et pression ; indication graphique d'un temps ouvert sans valeur chiffrée lorsque l'intitulé V3 le mentionne.

Les scènes sont partageables uniquement lorsque le geste V3 est identique ; chaque planche a son code exact. Les catégories C1/C2, T/E/F/S1 ne sont pas interprétées comme certifications supplémentaires. Aucun dosage, épaisseur, durée, rendement ou résistance n'est inventé.

## Intégration et QA
- `src/data/fenek-enhanced-artwork.json` associe cinq nouveaux SVG par code + slug, dimensions, type de source, SHA-256 et références de gestes communs.
- Les WebP antérieurs et les illustrations V3 restent présents, comme repli non modifié.
- `tests/test_lot155_159_bond_tile_professional_svg.py` vérifie les 6 titres exacts, les codes et langues, le statut BROUILLON, les 6 panneaux, les 6 badges, les SHA et l'absence de contenu externe ; distinction conditionnelle de C2TE-S1.
- Vérification statique des cinq SVG effectuée en lecture via GitHub : 6 panneaux, 6 codes produits, structure de balises équilibrée, SHA recalculé conforme.

## Gate de publication
Ne pas fusionner la PR #140 tant que le runner GitHub Actions ne fonctionne pas et que build Astro, tests Python, revue visuelle des scènes et contrôle trilingue ne réussissent pas. La CI précédente échouait avant les étapes ; ce défaut ne démontre ni succès ni échec des tests.

## Suite
Lots 160+ : joints C1/C2, ragréage, mortiers de réparation, coulis, enduits et maçonnerie FENEK BOND ; conserver les sources et éviter toute donnée technique non approuvée.
