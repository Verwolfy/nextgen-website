# Lot 187 — passage premium sécurisé et revue du pilote ACR-RF

Date : 12 novembre 2026 · Statut **BROUILLON / NON PUBLIÉ**.

## Résultat de l'exécution
Le WebP ACR-RF a été intégré sur la branche de PR #140 et revérifié par SHA (Git blob `2e3b418324ed3f5100225063d09022af518477a4`, SHA-256 `438694daefa3b97b2ca3d36f38d6bea78fbedb7070203f81b6e06ef3a76fa433`, 260976 octets).

La revue locale des pixels du pilote WebP détecte 6 cases de 540 × 360 dans 1620 × 720, sans changement de dimensions, avec une entropie de luminance des cases comprise entre **7,54 et 7,90 bits** et des différences visibles d'images et de gestes. Il s'agit d'indicateurs purement graphiques, **pas de validation technique ni de garantie de qualité universelle**.

| Étape ACR-RF | Concordance visuelle indicative | À confirmer avant publication |
|---:|---|---|
| 1 | Nettoyage à la brosse sur toiture | Etat sec/sain selon FT |
| 2 | Gants, lunettes et protections | EPI exacts selon FDS |
| 3 | Homogénéisation au malaxeur dans seau | Compatibilité du mode de malaxage selon FT |
| 4 | Première couche au rouleau | Outil effectivement recommandé |
| 5 | Bande d'armature à l'angle mur-sol / relevé | Détails de renfort et pose validés par FT |
| 6 | Application d'une couche ultérieure au rouleau | Respect du séchage prescrit par FT |

**Anomalie éditoriale ouverte :** inscriptions de marque `FENEK` générées sur casques, gants et seaux. Ces marques ne constituent pas un logo officiel. Elles doivent être supprimées, remplacées par les fichiers d'identité authentiques fournis, ou validées avant publication. La planche n'est **pas approuvée**.

## Intégration future, mais interdite tant que non approuvée
Le composant `src/components/FenekApplicationGuide.astro` possède maintenant trois couches CSS de même cadrage : `--v4-premium` au-dessus de `--v3-professional`, au-dessus du WebP `--v3-sprite`.

La couche premium est activée seulement si :
- `premiumVisualApproved===true`,
- `premiumTechnicalApproved===true`,
- `premiumApprovalRecord` est une chaîne non vide après retrait des espaces.

Le pilote `PROOF-ACR-RF` a les deux approbations à **false** et le dossier d'approbation à **null**. La présence du fichier dans `public/` sur la PR ne signifie donc pas affichage sur une page ; la PR est en brouillon et aucune mise en production n'a été faite.

Les contrôles `scripts/check_professional_artwork_built.py` et `scripts/check_live_application_guides.py` vérifient à la fois le SHA du WebP premium et l'absence du média dans le HTML tant que les approbations sont absentes ; une activation future ne sera acceptée que pour le produit et le SHA exacts.

## Lot 187 — trois autres produits
`PROOF-PU-1K`, `PROOF-CM-O1P` et `PROOF-CM-O2P` ont chacun un storyboard de six plans liés aux titres exacts du référentiel V3 : `docs/LOT187_PROOF_CIM_PU_STORYBOARDS_20261112.json`. Le script `scripts/assemble_premium_application_sprite.py` monte six vraies scènes distinctes en WebP 3×2 de 1620×720, avec un manifeste d'empreintes. Tests `tests/test_lot187_proof_storyboards.py`.

**Important :** les 18 visuels premium finaux des trois produits **n'ont pas été obtenus**. Les générations produites lors de cet essai étaient des tableaux de bord de suivi, et incluaient des mentions de conformité/progression non étayées ; elles ont été **écartées** et ne doivent pas être utilisées comme matière première de photos de produit ou comme preuve de progression.

## Porte de sortie
1. Générer ou acquérir **six véritables images de chantier par produit** au niveau C1T, sans logos ou valeurs techniques inventés.
2. Vérifier scène par scène les gestes source et les FT/FDS. Ne pas confondre `premiumVisualApproved` avec `premiumTechnicalApproved`.
3. Assembler en WebP, calculer SHA-256 et Git SHA, transférer l'objet Git binaire et relire son empreinte.
4. Rétablir GitHub Actions, exécuter les tests Python, Astro et audit `dist/`, puis tester les six cases sur mobile et desktop FR/AR/EN.
5. **Ne fusionner ni déployer aucun lot** avant ces contrôles ; conserver les 50 WebP historiques.

## Blocage GitHub Actions
Sur la PR #140, les 4 workflows continuent de se terminer en `failure` sans exécution de tests démontrée. Les endpoints de permissions et runners du dépôt ne sont pas exposés au connecteur GitHub utilisé (erreur d'autorisation de type d'URL), donc **aucune cause exacte n'est identifiée** et aucune modification des paramètres du dépôt n'a été tentée.
