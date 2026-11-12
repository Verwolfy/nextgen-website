# Lot 132 — BOND-R4 : transfert sémantique contrôlé du rendu R3

Date : 12 novembre 2026. Projet NextGen Building Solutions.

## Source et validation
La séquence source des six gestes de `BOND-R4`, tirée de `NEXTGEN_modes_emploi_V3.zip/fenek-bond-r4/legendes.csv`, est pratiquement identique à celle de `BOND-R3`. Chaque panneau du sprite BOND-R3 a été contrôlé individuellement contre la légende exacte BOND-R4 :

1. Purger et préparer les bords : purge mécanique du béton altéré.
2. Nettoyer et protéger les aciers si requis : brossage des armatures apparentes.
3. Humidifier le support puis ressuyer : pulvérisateur pour humidifier le support.
4. Porter les EPI et gâcher selon fiche : gants et malaxeur dans le mortier, aucune durée/dose.
5. Serrer et talocher le mortier : truelle de réparation sur la cavité.
6. Protéger du dessèchement précoce : feuille de protection transparente.

Les différences d'usage R3/R4 ne sont **pas** présentées comme des performances certifiées. Le sprite est générique à la réparation du béton, volontairement partagé : le fichier BOND-R4 a **son URL produit dédiée** mais son contenu et son SHA-256 sont identiques au rendu R3 déjà publié. Le champ `sharedArtworkFrom:BOND-R3` rend cette réutilisation explicite et auditée. Les captions R4 FR/AR/EN restent celles de BOND-R4 dans le HTML. **Ce n'est pas une illustration R4 nouvellement générée**.

Les 9 autres produits envisagés pour le lot 2 ne doivent pas utiliser des images générées incorrectes : plusieurs propositions montraient des étapes de pose de carrelage au lieu de coulage de grout, enduit, maçonnerie ou étanchéité. Aucune de ces images n'est publiée.

## Protection et contrôles
- Les 50 anciens sprites V3 restent inchangés.
- Correspondance stricte `code+slug` par `FenekApplicationGuide.astro`.
- Le test de contrôle 11/50 intègre la vérification d'origine partage R3/R4.
- Prérequis de clôture : fusion et marqueur Cloudflare sur le commit attendu, fichier BOND-R4 public et guide trois langues.

## Prochaine suite
Produits encore attendus : BOND-GR-HR, GP-CSII, OC-CSIII, M5, M10 ; PROOF-CM-O1P, CM-O2P, PU-1K, ACR-RF ; puis les autres références. Générer les six scènes correctes individuellement, vérifier visuellement les gestes, ne jamais inventer ratios/durées/propriétés, importer via blobs SHA, ajouter au manifeste et vérifier la production.
