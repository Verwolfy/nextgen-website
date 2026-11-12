# Lots 139-140 — illustrations professionnelles des peintures FENEK

12 novembre 2026 — **BROUILLON, non valide techniquement**.

## Perimetre
- **Lot 139, trois peintures interieures** : PAINT-INT-M, PAINT-INT-S, PAINT-INT-WA.
- **Lot 140, deux primaires** : PAINT-PRIM-A et PAINT-PRIM-FX.
- Chaque reference obtient sa propre planche SVG 1620 x 720, soit six cases 540 x 360, dans `public/images/application-professional/`.
- Toutes les scenes sont des dessins vectoriels originaux et editables, sans photographie ou logo reconstitue et sans chiffres de performance. Le code produit distingue les planches d'une sequence de geste partagee.
- Les six titres et descriptions continuent de provenir de `src/data/fenek-v3-manuals.json` en francais, arabe et anglais ; aucune legende technique n'est incrustee dans le dessin.

## Correspondance des scenes

### Peintures interieures
1. Reparation et preparation du mur, avec couteau a enduire.
2. Gants, lunettes et aeration de la piece.
3. Application d'une sous-couche au rouleau.
4. Homogeneisation en seau, sans indication de dilution.
5. Application reguliere de peinture au rouleau.
6. Visualisation du recouvrement apres sechage, sans delai chiffre.

### Primaires
1. Nettoyage et depoussierage du support.
2. Gants et lunettes.
3. Preparation/homogeneisation du primaire, sans formule inventee.
4. Application uniforme.
5. Controle visuel de l'absorption sans flaques.
6. Recouvrement apres sechage prescrit, sans delai chiffre.

## Integrite et integration
- Le registre `src/data/fenek-enhanced-artwork.json` conserve les **50 WebP deja publies** comme repli, avec leurs SHA-256 inchanges.
- Les cinq nouvelles valeurs `professionalSvg`, `professionalSvgSha256` et `professionalSvgDimensions` designent les dessins professionnels.
- `FenekApplicationGuide.astro` privilegie le SVG professionnel quand il existe ; sinon, il affiche le WebP remasterise, puis la source V3.
- `tests/test_lot139_140_paint_professional_svg.py` controle le code et le slug, le plan 3 x 2, les six titres, la structure SVG, les SHA et l'absence de references externes.
- `scripts/check_live_application_guides.py` ajoute l'audit en ligne des cinq SVG et de leur association sur 150 fiches trilingues.
- Les images ne constituent **ni une fiche technique, ni une validation du laboratoire, ni une certification**. Les notices et les images restent provisoires.

## Critere de livraison
1. Tests unitaires et compilation Astro executes avec succes.
2. Verification visuelle sur mobile de la composition, du contraste et des six correspondances metier.
3. Verification du commit deploye, des cinq SHA servis sur le domaine et des 150 pages FR/AR/EN.
4. Maintien de la mention provisoire tant que les fiches techniques et fiches de securite ne sont pas validees.

## Suite
Moderniser ensuite, par reference et par gestes, les autres planches encore issues des PNG V3 : peinture texture/sol/enduit, puis les familles Proof, Bond et Flow. Conserver les originaux et les SHA pour le repli.
