# Lot 186 — pilote semi-réaliste FENEK-PROOF ACR-RF

Date : 12 novembre 2026 · **BROUILLON / candidat visuel V4**, non approuvé pour publication.

## Constat d'audit de la page publique
- Source : https://nextgen-buildingsolutions.com/en/documentation/fenek-proof-acr-rf/
- Le WebP publié `/images/application-upgraded/fenek-proof-acr-rf-steps.webp` est un pictogramme plat de six étapes. Sa qualité est inférieure à celle de `BOND-C1T`.
- Erreurs graphiques : les étapes 4 et 6 représentent un outil cranté alors que la notice indique l'application d'un revêtement acrylique de toiture. Les étapes 1 à 6 ont peu de contexte de chantier. La sixième image est presque une répétition de la quatrième.
- Les titres et descriptions EN/FR/AR restent HTML ; aucune nouvelle information technique ne doit être inférée d'une illustration.

## Premier candidat produit en dehors du dépôt binaire
Une planche V4 a été extraite d'une maquette de guide d'application semi-réaliste produite dans la conversation, puis nettoyée de son habillage de page et composée à partir de six scènes en une planche WebP de 1620×720 pixels (six cases 540×360).

**Fichier à importer dans une étape ultérieure par accès binaire GitHub :**
`fenek-proof-acr-rf-steps-v4.webp`

**SHA-256 binaire :** `438694daefa3b97b2ca3d36f38d6bea78fbedb7070203f81b6e06ef3a76fa433`.

**Taille binaire :** 260976 octets.

Les six étapes sont liées à la notice V3 existante :
1. Réparer, nettoyer et sécher la toiture (ouvrier et brosse).
2. Porter des gants et lunettes (ouvrier équipé).
3. Homogénéiser le produit avant application (malaxeur et seau).
4. Appliquer une première couche régulière (rouleau sur toiture).
5. Armer joints et relevés (bande de renforcement sur relevé de toiture).
6. Recouvrir après séchage selon fiche (nouvelle couche au rouleau).

## Contrôles nécessaires avant intégration
- Examiner l'exactitude du geste 5 (renforcement à l'interface horizontal/vertical) par rapport aux FT/FDS approuvées.
- Les inscriptions `FENEK` sur les EPI et outils sont du contenu **généré** ; ne pas les utiliser comme preuve de logo, d'emballage, ou de marque officiellement homologuée. Vérifier/retoucher toute représentation non authentifiée.
- Aucun chiffre de dosage, taux, temps, température ou performance ne doit être ajouté.
- Vérifier à l'écran 360px et desktop le cadrage des six panneaux, et les textes AR/FR/EN restent en HTML.
- Il est impossible de considérer ce candidat comme présent dans le dépôt tant qu'un mécanisme de transfert binaire GitHub n'a pas été utilisé et que son SHA n'a pas été vérifié dans l'archive du dépôt.

## Protection anti-régression installée sur PR #140
Le site ne doit pas afficher automatiquement les 47 SVG schématiques en prépublication. Le manifeste porte `visualQualityApproved:false` pour eux. Dans `FenekApplicationGuide.astro`, le SVG n'est affiché que si `visualQualityApproved===true`. Le WebP existant reste la ressource principale, inchangée.

À l'étape d'import premium V4, utiliser un champ source **distinct** du SVG schématique et ne jamais surcharger `sprite` tant que le produit n'est pas visuellement vérifié. Garder l'ancienne empreinte SHA de WebP de repli. Ne pas mettre ce candidat en production par simple modification d'URL.

## Suite du lot
Procéder par les quatre références de membranes : `PROOF-ACR-RF` (pilote), `PROOF-PU-1K`, `PROOF-CM-O1P`, `PROOF-CM-O2P`. Suivent sept références PROOF époxy et systèmes de joints, cinq BOND restants, douze FLOW, huit PAINT intérieurs/techniques et trois façades intermédiaires.
