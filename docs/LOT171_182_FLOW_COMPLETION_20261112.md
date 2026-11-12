# Lots 171 à 182 — FENEK FLOW, illustrations des douze produits

12 novembre 2026 — **BROUILLON** (illustrations indicatives, non validées par laboratoire).

## Matériaux de référence
Les six étapes de chaque produit proviennent de `src/data/fenek-v3-manuals.json` ; les titres FR/AR/EN restent en HTML et ne sont pas gravés dans les images. Chaque référence possède sa propre planche SVG de 1620 × 720, découpée en six scènes 540 × 360, avec numéro d'étape et code produit.

## Dix adjuvants — lots 171 à 180
Les cinq premières scènes sont identiques dans les notices : contrôle de compatibilité des matériaux, gants/lunettes, dosage selon FT sans chiffre, incorporation au malaxeur et malaxage. La scène 6 est spécifique à la référence :

| Lot | Code | Contrôle 6 représenté de façon indicative |
|---|---|---|
| 171 | FLOW-WR-N | Consistance, sans résultat inventé |
| 172 | FLOW-SP-HR | Consistance, sans résultat inventé |
| 173 | FLOW-SP-RT | Maintien de consistance |
| 174 | FLOW-SP-PF | Résistances par essais (aucune valeur) |
| 175 | FLOW-RT | Temps de prise (aucune durée) |
| 176 | FLOW-AC | Prise et compatibilité des armatures |
| 177 | FLOW-AE | Air du béton frais, cadran sans graduation numérique |
| 178 | FLOW-WP | Vibration du béton et protection de cure |
| 179 | FLOW-VMA | Étalement/stabilité |
| 180 | FLOW-CI | Durabilité par essais, sans verdict |

Les produits `FLOW-WR-N` et `FLOW-SP-HR` ont la même séquence source de six intitulés, mais chacun possède son propre SVG, libellé du code exact.

## Deux guides de mise en œuvre distincts — lots 181 et 182
- **FLOW-CURE** : disparition du ressuage, EPI de pulvérisation, préparation sans dilution non autorisée, pulvérisation sur béton frais, couverture uniforme, protection et vérification avant revêtement.
- **FLOW-LAT** : nettoyage/humidification sans eau stagnante, EPI, préparation de la solution selon fiche, brossage du pont d'adhérence, mortier frais sur frais, cure.

## Fichiers et contrôles
- Fichiers `public/images/application-professional/fenek-flow-<suffix>-steps.svg`, un par produit.
- Entrées associées dans `src/data/fenek-enhanced-artwork.json` via `code + slug`, dimensions, statut `BROUILLON` et SHA-256 exact.
- Les 50 anciens sprites WebP remastérisés sont conservés comme repli, sans modification.
- Test créé : `tests/test_lot171_182_flow_professional_svg.py` (six étapes FR exactes, titres AR/EN présents, intégrité SVG, dix contrôles finaux et deux workflows spécifiques, SHA, unicité, interdiction de contenu non fiable).
- Contrôle statique GitHub réalisé : fichiers relus, 6 panneaux et 6 étiquettes par produit, balises équilibrées, SHA conformes, pas de liens externes/scripts/images embarquées.

## Résultat catalogue
**47 SVG professionnels** (282 scènes) plus les **3 références façade PAINT-FAC-M, PAINT-FAC-EL, PAINT-FAC-SX**, déjà modernisées en WebP professionnel au lot 138. Les **50/50 références ont un média amélioré**, mais ce n'est pas une validation technique, un rendu photoréaliste généralisé, ni une preuve de mise en production.

## Conditions pour publication
GitHub Actions continue d'échouer avant l'exécution des étapes, sans runner attribué. Ne pas déclarer le build Astro, les tests Python, le rendu navigateur ou le déploiement Cloudflare validés. Garder PR #140 en brouillon. Après résolution du runner, exécuter le build, les suites Python, contrôler le rendu mobile FR/AR/EN et les SHA servis, puis fusionner.
