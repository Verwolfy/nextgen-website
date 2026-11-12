# Rapport d’audit visuel — modes d’emploi FENEK (50 produits)

**Date :** 12 novembre 2026 · **Référence visuelle :** FENEK-BOND C1T · **État :** audit visuel prépublication, non-validation technique.

## Résultat

- **50/50 pages anglophones publiques** consultées : chacune affiche un parcours de six étapes. 48 notices reproduisent les six titres du référentiel ; deux colles historiques (C1T/C1TE) utilisent leurs titres éditoriaux antérieurs, point à confirmer sans conclure à une erreur.
- **50/50 planches WebP GitHub/main examinées individuellement**. Les niveaux de rendu ne sont **pas homogènes**.
- **Niveau A (11)** : illustration semi-réaliste proche de C1T. **Niveau B (3)** : façade illustrée avec détails mais style moins abouti que C1T. **Niveau C (36)** : pictogrammes plats ne répondant pas au niveau C1T.
- **39/50 produits doivent être harmonisés** au standard graphique C1T (36 urgents + 3 façades à reprendre en dernière priorité).
- **42 empreintes WebP uniques pour 50 références** : cinq groupes de partage totalisant 13 références. Cette réutilisation peut cacher des gestes spécifiques et nécessite une revue métier.
- **PR #140 en brouillon** : 47 SVG techniques créés auparavant, mais ils sont schématiques et ne constituent pas une amélioration suffisante. Le lot 186 bloque leur activation tant que `visualQualityApproved` n’est pas explicitement validé.

## Échelle

| Niveau | Description | Décision |
|---|---|---|
| A | Semi-réaliste, scènes détaillées/personnages et vrais outils, proche de C1T | Conserver le média existant, vérifier seulement l’adéquation technique des gestes |
| B | Illustration de façade illustrée et lisible, mais rendu simplifié | Harmonisation secondaire |
| C | Pictogrammes plats, peu de contexte et outils simplifiés | Remplacement prioritaire |

## Audit individuel (média publié sur `main`)

| # | Référence | Niveau | Média partagé avec | Action |
|---:|---|:---:|---|---|
| 1 | [BOND-C1T](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-c1t/) | A | — | Préserver |
| 2 | [BOND-C1TE](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-c1te/) | A | — | Préserver |
| 3 | [BOND-C2FT](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-c2ft/) | A | — | Préserver |
| 4 | [BOND-C2TE](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-c2te/) | A | — | Préserver |
| 5 | [BOND-C2TE-S1](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-c2te-s1/) | A | — | Préserver |
| 6 | [BOND-CG1](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-cg1/) | A | — | Préserver |
| 7 | [BOND-CG2WA](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-cg2wa/) | A | — | Préserver |
| 8 | [BOND-CT-C25-F5](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-ct-c25-f5/) | A | — | Préserver |
| 9 | [BOND-R2](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-r2/) | A | — | Préserver |
| 10 | [BOND-R3](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-r3/) | A | BOND-R4 | Préserver |
| 11 | [BOND-R4](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-r4/) | A | BOND-R3 | Préserver |
| 12 | [BOND-GR-HR](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-gr-hr/) | C | — | Refaire en semi-réaliste |
| 13 | [BOND-GP-CSII](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-gp-csii/) | C | — | Refaire en semi-réaliste |
| 14 | [BOND-OC-CSIII](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-oc-csiii/) | C | — | Refaire en semi-réaliste |
| 15 | [BOND-M5](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-m5/) | C | — | Refaire en semi-réaliste |
| 16 | [BOND-M10](https://nextgen-buildingsolutions.com/en/documentation/fenek-bond-m10/) | C | — | Refaire en semi-réaliste |
| 17 | [PROOF-CM-O1P](https://nextgen-buildingsolutions.com/en/documentation/fenek-proof-cm-o1p/) | C | — | Refaire en semi-réaliste |
| 18 | [PROOF-CM-O2P](https://nextgen-buildingsolutions.com/en/documentation/fenek-proof-cm-o2p/) | C | — | Refaire en semi-réaliste |
| 19 | [PROOF-PU-1K](https://nextgen-buildingsolutions.com/en/documentation/fenek-proof-pu-1k/) | C | — | Refaire en semi-réaliste |
| 20 | [PROOF-ACR-RF](https://nextgen-buildingsolutions.com/en/documentation/fenek-proof-acr-rf/) | C | — | Refaire en semi-réaliste |
| 21 | [PROOF-EP-PRIM](https://nextgen-buildingsolutions.com/en/documentation/fenek-proof-ep-prim/) | C | — | Refaire en semi-réaliste |
| 22 | [PROOF-EP-SR](https://nextgen-buildingsolutions.com/en/documentation/fenek-proof-ep-sr/) | C | — | Refaire en semi-réaliste |
| 23 | [PROOF-EP-SB](https://nextgen-buildingsolutions.com/en/documentation/fenek-proof-ep-sb/) | C | — | Refaire en semi-réaliste |
| 24 | [PROOF-EP-INJ](https://nextgen-buildingsolutions.com/en/documentation/fenek-proof-ep-inj/) | C | — | Refaire en semi-réaliste |
| 25 | [PROOF-EP-ANC](https://nextgen-buildingsolutions.com/en/documentation/fenek-proof-ep-anc/) | C | — | Refaire en semi-réaliste |
| 26 | [PROOF-PU-INJ](https://nextgen-buildingsolutions.com/en/documentation/fenek-proof-pu-inj/) | C | — | Refaire en semi-réaliste |
| 27 | [PROOF-PU-SEAL](https://nextgen-buildingsolutions.com/en/documentation/fenek-proof-pu-seal/) | C | — | Refaire en semi-réaliste |
| 28 | [FLOW-WR-N](https://nextgen-buildingsolutions.com/en/documentation/fenek-flow-wr-n/) | C | FLOW-SP-HR | Refaire en semi-réaliste |
| 29 | [FLOW-SP-HR](https://nextgen-buildingsolutions.com/en/documentation/fenek-flow-sp-hr/) | C | FLOW-WR-N | Refaire en semi-réaliste |
| 30 | [FLOW-SP-RT](https://nextgen-buildingsolutions.com/en/documentation/fenek-flow-sp-rt/) | C | FLOW-SP-PF, FLOW-RT, FLOW-AC | Refaire en semi-réaliste |
| 31 | [FLOW-SP-PF](https://nextgen-buildingsolutions.com/en/documentation/fenek-flow-sp-pf/) | C | FLOW-SP-RT, FLOW-RT, FLOW-AC | Refaire en semi-réaliste |
| 32 | [FLOW-RT](https://nextgen-buildingsolutions.com/en/documentation/fenek-flow-rt/) | C | FLOW-SP-RT, FLOW-SP-PF, FLOW-AC | Refaire en semi-réaliste |
| 33 | [FLOW-AC](https://nextgen-buildingsolutions.com/en/documentation/fenek-flow-ac/) | C | FLOW-SP-RT, FLOW-SP-PF, FLOW-RT | Refaire en semi-réaliste |
| 34 | [FLOW-AE](https://nextgen-buildingsolutions.com/en/documentation/fenek-flow-ae/) | C | — | Refaire en semi-réaliste |
| 35 | [FLOW-WP](https://nextgen-buildingsolutions.com/en/documentation/fenek-flow-wp/) | C | — | Refaire en semi-réaliste |
| 36 | [FLOW-VMA](https://nextgen-buildingsolutions.com/en/documentation/fenek-flow-vma/) | C | — | Refaire en semi-réaliste |
| 37 | [FLOW-CI](https://nextgen-buildingsolutions.com/en/documentation/fenek-flow-ci/) | C | — | Refaire en semi-réaliste |
| 38 | [FLOW-CURE](https://nextgen-buildingsolutions.com/en/documentation/fenek-flow-cure/) | C | — | Refaire en semi-réaliste |
| 39 | [FLOW-LAT](https://nextgen-buildingsolutions.com/en/documentation/fenek-flow-lat/) | C | — | Refaire en semi-réaliste |
| 40 | [PAINT-INT-M](https://nextgen-buildingsolutions.com/en/documentation/fenek-paint-int-m/) | C | PAINT-INT-S, PAINT-INT-WA | Refaire en semi-réaliste |
| 41 | [PAINT-INT-S](https://nextgen-buildingsolutions.com/en/documentation/fenek-paint-int-s/) | C | PAINT-INT-M, PAINT-INT-WA | Refaire en semi-réaliste |
| 42 | [PAINT-INT-WA](https://nextgen-buildingsolutions.com/en/documentation/fenek-paint-int-wa/) | C | PAINT-INT-M, PAINT-INT-S | Refaire en semi-réaliste |
| 43 | [PAINT-FAC-M](https://nextgen-buildingsolutions.com/en/documentation/fenek-paint-fac-m/) | B | — | Améliorer après les pictogrammes |
| 44 | [PAINT-FAC-EL](https://nextgen-buildingsolutions.com/en/documentation/fenek-paint-fac-el/) | B | — | Améliorer après les pictogrammes |
| 45 | [PAINT-FAC-SX](https://nextgen-buildingsolutions.com/en/documentation/fenek-paint-fac-sx/) | B | — | Améliorer après les pictogrammes |
| 46 | [PAINT-PRIM-A](https://nextgen-buildingsolutions.com/en/documentation/fenek-paint-prim-a/) | C | PAINT-PRIM-FX | Refaire en semi-réaliste |
| 47 | [PAINT-PRIM-FX](https://nextgen-buildingsolutions.com/en/documentation/fenek-paint-prim-fx/) | C | PAINT-PRIM-A | Refaire en semi-réaliste |
| 48 | [PAINT-TXT-F](https://nextgen-buildingsolutions.com/en/documentation/fenek-paint-txt-f/) | C | — | Refaire en semi-réaliste |
| 49 | [PAINT-SOL-A](https://nextgen-buildingsolutions.com/en/documentation/fenek-paint-sol-a/) | C | — | Refaire en semi-réaliste |
| 50 | [PAINT-ENT-L](https://nextgen-buildingsolutions.com/en/documentation/fenek-paint-ent-l/) | C | — | Refaire en semi-réaliste |

## Priorité par lot

1. **186 — PROOF-ACR-RF** : pilote de six scènes toiture semi-réalistes, source exacte de la notice, WebP V4 pilote maintenant importé sur la branche via GitHub Git Blob, SHA vérifié, encore non approuvé.
2. **187 — PROOF-ACR-RF / PU-1K / CM-O1P / CM-O2P** : montage du lot des étanchéités membranes et cimentaires, contrôle des gestes, EPI, rendu et crop.
3. **188 — autres PROOF** (7 références) : époxy, joints, injection et scellements, scènes spécifiques.
4. **189 — BOND restants** (5 références) : coulis, enduits et maçonnerie.
5. **190 — FLOW** (12 références) : scènes de malaxeur, dosage, béton, essais de consistance/résistance non chiffrés, maintien et cure.
6. **191 — PAINT** (8 pictogrammes) puis **192 — les 3 façades**, si les nouveaux visuels constituent un progrès réel.

## Garanties de publication

- Ne pas reproduire des logos officiels ou emballages réels non fournis. Les captures d'illustration générées par IA sont éditoriales, jamais des photos de chantier.
- Conserver `BROUILLON` jusqu’à FT/FDS approuvées, et ne créer aucune donnée de dosage, temps, épaisseur, norme, résistance ou certification.
- Pour chaque référence : six scènes individuelles, format 3×2, axe graphique commun, SHA-256, vérification du geste source FR/AR/EN, crop mobile, pas de texte incrusté autre que numéros.
- Une illustration ne peut remplacer le WebP de base que si un vrai média correspondant existe, a été revu et que son statut `visualQualityApproved` est vrai. Ne pas activer les anciens SVG schématiques automatiquement.
- PR #140 : exécution CI Astro/Python et revue navigateur encore bloquées ; ne pas fusionner ou publier sans contrôles réels.

## Source et limites

Site public lu par navigateur et extraction web ; médias WebP lus dans GitHub/main. Les 50 pages ont été vérifiées quant à la présence du guide, mais la comparaison chiffrée des hashes servis par Cloudflare et le rendu mobile de chaque langue restent à exécuter. Les scores A/B/C décrivent la **qualité graphique** et non l’exactitude métier ou la certification.
