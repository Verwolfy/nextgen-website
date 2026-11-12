# Lot 133 — lisibilité des illustrations sources sur 9 produits du lot 2

Date : 12 novembre 2026. Objet : supprimer les légendes fixes AR/FR incrustées dans les sprites V3 pour éviter leur doublon avec les légendes HTML localisées, sans toucher aux dessins et sans changer les 50 modes d'emploi.

## Résultat
Neuf références : BOND-GR-HR, BOND-GP-CSII, BOND-OC-CSIII, BOND-M5, BOND-M10, PROOF-CM-O1P, PROOF-CM-O2P, PROOF-PU-1K, PROOF-ACR-RF.

Les six images PNG de chacune des neuf références ont été extraites et examinées dans `NEXTGEN_modes_emploi_V3.zip` : **54 images source**. Les légendes sont dans `legendes.csv`, toutes au statut BROUILLON. Les régions supérieures contiennent l'illustration; la partie inférieure porte les légendes AR/FR incrustées. Fraction de cadre à rendre visible : **0,78** (du haut vers le bas), sans recadrage horizontal. Les titres FR, AR et EN déjà présents en HTML restent intacts.

## Réalisation côté site
- Fichier `src/data/fenek-v3-source-crop-qa.json` : 9 lignes, code + slug + fraction d'affichage. Aucun autre produit ne peut recevoir la règle.
- `FenekApplicationGuide.astro` : la règle CSS de présentation `fenek-v3-source-crop-figure` n'est activée que si le code/slug correspond à l'une des neuf sources et si aucun WebP amélioré n'est disponible. Ancien sprite et SHA-256 restent inchangés.
- CSS mobile explicitement adapté ; le conteneur de l'image masque uniquement les légendes incrustées tout en conservant les six vignettes de procédure.
- Tests statiques `tests/test_lot133_source_crop_qa.py` : 9 codes, 54 étapes, mapping unique et absence de collision avec les 11 produits améliorés.

## Limite honnête
Ceci est une **amélioration de lisibilité/presentation des sources existantes**, et non un remplacement par de nouvelles images photoréalistes. Ne pas compter ces neuf références comme « illustrations modernisées ». Les illustrations générées automatiquement ne correspondant pas aux gestes décrits ont été écartées avant publication.

## À poursuivre
Pour ces neuf produits, produire six nouvelles scènes de haute qualité qui respectent exactement leurs légendes et leur usage, contrôler visuellement et seulement ensuite remplacer chaque WebP dans `public/images/application-upgraded/`, un produit à la fois. Statut de modernisation avec cette PR : **11/50** (pas 20/50).
