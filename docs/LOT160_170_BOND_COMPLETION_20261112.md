# Lots 160 à 170 — fin des illustrations FENEK BOND

12 novembre 2026 · **BROUILLON**. Les pictogrammes améliorés précédents sont conservés en repli.

## Périmètre
- Lots 160–161 : BOND-CG1 et BOND-CG2WA, deux mortiers de jointoiement avec six scènes cohérentes (nettoyage des joints, EPI, gâchage, remplissage diagonal, éponge, essuyage du voile).
- Lot 162 : BOND-CT-C25-F5, ragréage autolissant (support/ primaire, EPI, gâchage, versement, répartition à la lisseuse, débullage et protection).
- Lots 163–165 : BOND-R2/R3/R4, réparation de béton avec représentations individualisées de purge, traitement conditionnel des armatures, humidification, préparation et application du mortier, protection de cure.
- Lot 166 : BOND-GR-HR, coulis de scellement sous coffrage : coffrage, humidification, préparation, coulage d'un seul côté, contrôle du remplissage et cure.
- Lots 167–168 : BOND-GP-CSII et BOND-OC-CSIII, enduits de mur et de façade : préparation, EPI, mélange, application manuelle/projetée selon l'intitulé, dressage/finition, protection du frais.
- Lots 169–170 : BOND-M5 et BOND-M10, mortiers de maçonnerie : humidification conditionnelle, EPI, gâchage, lit de mortier, pose et alignement des blocs, joints et protection.

## Implémentation
- Chaque référence dispose d'une planche SVG unique de six panneaux 540 × 360 (image 1620 × 720), avec code produit dans chaque case.
- Registre et SHA : `src/data/fenek-enhanced-artwork.json`.
- Les titres/descriptions de six étapes restent dérivés de `fenek-v3-manuals.json` en FR/AR/EN, sans instructions incrustées dans le SVG.
- Tests : `tests/test_lot160_162_bond_grout_leveling_svg.py` et `tests/test_lot163_170_remaining_bond_svg.py`.
- **16 références BOND sur 16** ont désormais des SVG professionnels dans la branche, en plus des 50 WebP existants.

## Interdits et contrôle de diffusion
Aucune norme, quantité, durée, épaisseur, valeur de performance, certification, logo ou procédé industriel non confirmé n'est inventé. Les scènes sont indicatives et ne remplacent pas une FT/FDS approuvée.

L'intégrité statique des SVG et SHA est enregistrée ; ne pas déclarer la CI ou le déploiement validés tant que les workflows GitHub Actions ne se sont pas réellement exécutés, suivis du build Astro, des tests unitaires et de l'audit visuel trilingue.

## À suivre
Créer les 12 séries Fenek-Flow, puis réexaminer les 3 peintures de façade déjà dotées des WebP professionnels du lot 138. Conserver toutes les sources d'origine.
