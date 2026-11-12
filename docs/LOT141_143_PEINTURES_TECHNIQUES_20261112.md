# Lots 141 à 143 — peintures FENEK : six illustrations professionnelles par référence

Date : 12 novembre 2026 · **BROUILLON — non validé par le laboratoire**

## Situation de départ
Les lots 134–137 avaient déjà livré 50 séries de pictogrammes V3 remastérisés. Le lot 138 a modernisé trois peintures de façade. Les lots 139–140 portent sur cinq peintures et primaires supplémentaires. Les trois nouvelles références ci-dessous n'avaient encore que des pictogrammes remastérisés.

## Réalisations nouvelles
| Lot | Code | Sujet | Illustrations |
| --- | --- | --- | ---: |
| 141 | PAINT-TXT-F | Revêtement de façade texturé | 6 |
| 142 | PAINT-SOL-A | Peinture de sol | 6 |
| 143 | PAINT-ENT-L | Enduit de lissage | 6 |

Chaque produit possède maintenant son fichier vectoriel, sous `public/images/application-professional/<slug>-steps.svg`, avec **six panneaux** (3 colonnes × 2 rangées), 1620 × 720 px au total. Le texte des instructions et ses traductions FR/AR/EN restent dans le HTML, séparément de l'illustration.

### PAINT-TXT-F
1. Nettoyage et primaire du mur
2. Gants et lunettes
3. Homogénéisation de la pâte
4. Application à la lisseuse inox
5. Structuration à la taloche
6. Protection du revêtement pendant le séchage

### PAINT-SOL-A
1. Préparation d'un sol sain et sec
2. EPI et ventilation
3. Application éventuelle d'un primaire
4. Homogénéisation suivant la fiche technique
5. Application régulière au rouleau sur sol
6. Protection et marquage seulement après cure

### PAINT-ENT-L
1. Préparation et réparation du support
2. Gants et lunettes
3. Homogénéisation de la pâte si nécessaire
4. Lissage du support à la lisseuse
5. Ponçage après séchage
6. Dépoussiérage avant finition

## Traçabilité et sécurité
- Les scènes sont des **dessins vectoriels originaux** et non des photos de l'usine ou de chantiers réels.
- Aucun logo officiel n'est généré ni reconstruit par IA ; seules les références produit figurent sur les visuels.
- Aucun taux, dosage, épaisseur, rendement, délai, résistance, norme ni certification n'est représenté.
- Le statut `BROUILLON` reste obligatoire. Une FT/FDS qualifiée et approuvée est nécessaire avant une instruction technique engageante.
- `src/data/fenek-enhanced-artwork.json` associe chaque référence par code/slug au nouveau SVG et à son SHA-256 ; les 50 anciens WebP restent inchangés et disponibles.
- Le composant `FenekApplicationGuide.astro` affiche le SVG professionnel lorsqu'il existe, sans modifier les titres AR/FR/EN.
- Tests ajoutés : `tests/test_lot141_143_professional_paint.py` (code/slug, étapes de source, structure 3 × 2, 6 étiquettes produit, SHA-256, absence de liens ou allégations externes).
- Le moniteur live `scripts/check_live_application_guides.py` contrôle les nouveaux fichiers et leur association aux pages trilingues.

## Vérifications à faire avant fusion
- `npm ci && npm run build`
- `python -m unittest discover -s tests -q`
- Vérification visuelle des 18 panneaux sur écrans 360 px et desktop, lecture FR/AR/EN.
- Après déploiement : correspondance SHA des huit SVG professionnels, 50 WebP d'origine et 150 pages de documentation.
- Ne pas affirmer que la CI est verte : le runner GitHub Actions de la PR a précédemment échoué avant les étapes.

## Prochain groupe
Poursuivre les séries PROOF puis les références BOND et FLOW, en privilégiant une scène métier fidèle à chaque étape plutôt qu'un pictogramme générique. Maintenir les rendus antérieurs en repli.
