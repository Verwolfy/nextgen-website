# Lot 138 — peintures de façade FENEK : six illustrations propres par référence
12 novembre 2026 · statut BROUILLON

## Motivation
Le rendu précédent des modes d'emploi PAINT-FAC manquait de clarté (objets sans perspective, façades schématiques). Les trois peintures de façade ont les mêmes six intitulés source FR/AR, vérifiés individuellement contre `NEXTGEN_modes_emploi_V3.zip` et le manifeste publié ; un visuel professionnel commun est acceptable uniquement avec les bonnes étiquettes de produit.

## Travaux livrés
- `PAINT-FAC-M`, `PAINT-FAC-EL`, `PAINT-FAC-SX` : six scènes métier chacune, illustrations professionnelles vectorielles détaillées.
- Scènes : préparation/réparation de la façade ; EPI + météo ; application du primaire sur un mur vertical ; mélange de peinture ; rouleau de peinture sur la façade ; protection pendant le séchage.
- Trois WebP dédiés de 1620×720 (trois colonnes × deux rangées, chaque cellule 540×360), sans légende AR/FR incrustée : le HTML conserve les titres accessibles et les traductions EN.
- La marque, l'étiquette du seau de mélange et le code FAC-M/FAC-EL/FAC-SX correspondent à chaque produit, et les images n'ajoutent aucun dosage, durée, certificat ou performance.
- Registre `src/data/fenek-enhanced-artwork.json` : sha256 propre à chaque produit, `sourceType=illustration-professionnelle-façade-6-scènes`, `sharedSceneWorkflowWith` trace la séquence commune.
- Assets historiques V3 conservés pour repli, autres références inchangées. Association au site par `code+slug` existante dans `FenekApplicationGuide.astro`.

## Contrôles
- Test d'intégrité des 50 médias modifié pour reconnaître la nouvelle source professionnelle sur ces trois seuls produits.
- Test ciblé `tests/test_lot138_facade_art.py` vérifie code/slug, six titres, format, statut, médias, sha256 et composant Astro.
- Les GitHub Actions doivent être contrôlés indépendamment ; si le runner échoue avant les tests, ne pas qualifier la CI de succès.
- Déploiement à vérifier via `https://nextgen-buildingsolutions.com/deployment.json`, médias publics et documentation FR/AR/EN.

## Suite
Moderniser les 36 illustrations qui restent issues des pictogrammes V3 remastérisés, produit par produit et sans compromettre l'exactitude des gestes. Les 11 produits BOND initiaux restent les autres références avec rendu haut de gamme. Aucun produit ne doit être qualifié de certifié sans validation de la FT/FDS.
