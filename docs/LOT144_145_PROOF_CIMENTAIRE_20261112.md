# Lots 144–145 — FENEK PROOF : deux systèmes d’étanchéité cimentaire

Date : 12 novembre 2026 · **BROUILLON — non validé techniquement**

## Objectif
Remplacer les anciens pictogrammes V3 remastérisés par deux séries de scènes métier originales et propres aux références :
- **Lot 144** : `PROOF-CM-O1P`, système cimentaire à une préparation de mélange selon FT ; ne pas déduire de ratio ou de formulation.
- **Lot 145** : `PROOF-CM-O2P`, système à deux composants selon FT ; représentation de deux contenants sans dosage inventé.

## Les six panneaux de chaque série
1. Nettoyage et humidification du support sans eau stagnante.
2. Equipements de protection mentionnés par les intitulés V3.
3. Gâchage selon FT (O1P) ou mélange des deux composants (O2P).
4. Renforcement des angles et joints.
5. Application de couches croisées.
6. Cure avant la pose / avant carrelage, sans durée affirmée.

## Sources et implémentation
- Source des étapes : `src/data/fenek-v3-manuals.json`. FR/AR/EN restent dans le HTML et non sur le dessin.
- Deux fichiers SVG `public/images/application-professional/fenek-proof-cm-o1p-steps.svg` et `...o2p-steps.svg`.
- Même format contrôlable : **1620 × 720**, 3 × 2 cellules de 540 × 360, chacune avec badge étape et code produit.
- `src/data/fenek-enhanced-artwork.json` : références exactes code/slug, statut `BROUILLON`, SHA-256, source vectorielle, dimensions, relation entre les gestes des deux produits. Les anciens WebP ne sont pas modifiés.
- `tests/test_lot144_145_cement_waterproofing.py` vérifie l’identité produit, les six intitulés, le SVG, les empreintes SHA, la distinction des fichiers O1P/O2P, les interdits de certification.
- `scripts/check_live_application_guides.py` doit vérifier la présence réelle des SVG et des liens sur les pages FR/AR/EN.

## Restrictions
Ce sont des **illustrations éditoriales indicatives**, non des FT/FDS, ni un mode opératoire engageant. Aucun dosage, durée de cure, rendement, certificat, résistance ni logo reconstitué n’est ajouté. Les deux séries et leurs notices restent au stade **BROUILLON**.

## Publication
Ne pas fusionner tant que le build Astro et les tests Python n’ont pas été exécutés avec succès ; GitHub Actions a échoué sans étapes dans les tentatives précédentes. Après fusion, vérifier les URLs publiques des SVG, les 50 WebP et les 150 fiches de documentation.
