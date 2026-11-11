# NEXTGEN — Lot 128 : déploiement V3 produit par produit (50 références)

Date : 11 novembre 2026. Source originale : `NEXTGEN_modes_emploi_V3.zip` fourni par l'utilisateur.

## Objectif
Enrichir la section « Étapes d'application » du site, avec association stricte des images au code et slug catalogue, contrôle visuel systématique, correction des images incohérentes, tests FR/AR/EN/mobile/nuit, sans publication de données non approuvées.

## État observé avant ce lot
- `src/data/catalogue-projets.json` contient 50 références au statut `presentation_provisoire` avec `certifie:false` et `commercialise:false`.
- Une première intégration V3 C1T déjà présente sur `main` : sprite `/images/application-v3/fenek-bond-c1t-steps.webp`, mapping strict `src/data/fenek-v3-reviewed.ts`, six légendes spécifiques au produit, maintien de l'ancien sprite pour les autres colles.
- Les autres 49 produits ne sont pas encore associés au nouveau dossier V3 ; les illustrations de la V2 et les icônes génériques sont conservées en attente de revue.

## Lot 128 — Référence 1/50 : FENEK-BOND C1T
- Référence validée dans le catalogue : `BOND-C1T` / `fenek-bond-c1t`.
- Examen visuel des six panneaux du ZIP V3 : préparation du support, EPI, eau sans dosage chiffré, repos/remalaxage conditionnel, spatule crantée, pose des carreaux.
- Les légendes source `fenek-bond-c1t/legendes.csv` AR/FR correspondent aux six gestes et au contexte de colle carrelage. Les délais/quantités restent `[LABO]` dans `valeurs_a_valider.txt`.
- Les six PNG originaux du ZIP sont publiés sans retouche à `public/images/application/v3/fenek-bond-c1t/`, format 2048 × 2048, couleurs `#1B365D` et `#009A44` + fond blanc. Contrôle palette exact : trois couleurs de pixels (deux encres + blanc).
- Les empreintes SHA256 exactes sont imposées par les tests unitaires et les tests de build. Poids total des six PNG ≈ 300 Ko.
- Sur les fiches `/fr/documentation/fenek-bond-c1t/`, `/ar/documentation/fenek-bond-c1t/`, `/en/documentation/fenek-bond-c1t/`, chaque image peut désormais être ouverte en grand format ; le sprite reste affiché dans les cartes pour préserver vitesse et ergonomie responsive.
- Aucun changement Supabase, RLS, publication, prix, valeurs techniques ou fiche certifiée.

## Contrôles
- `tests/test_lot128_c1t_v3_fullres.py` : identité code/slug, six SHA256, signatures et dimensions PNG, absence de diffusion accidentelle aux autres produits, sécurité, fonctionnalité d'agrandissement.
- `scripts/check_application_guides.py` : six images requises dans la sortie `dist`, 150 pages conservées, six liens présents pour les trois variantes linguistiques.
- CI GitHub Astro, tests Python, Chromium et Lighthouse. Vérifier l'exécution réelle avant fusion.
- Cloudflare live : le workflow doit confirmer déploiement du commit `main` avant d'affirmer mise en production.

## Avancement et ordre de travail
- **1/50 en haute résolution** : `BOND-C1T`, accès plein format ajouté à la V3 déjà intégrée. **2/50 revues** sur `main` : C1T et C1TE.
- **48/50** : à contrôler et intégrer l'un après l'autre, sans réutiliser arbitrairement des visuels correspondant à un autre produit.
- **Prochaine référence : `BOND-C2FT` / `fenek-bond-c2ft`**. Vérifier les six PNG/SVG du dossier `fenek-bond-c1te`, les légendes bilingues et les différenciations de procédé, puis incorporer les images et tester avant la suivante.
- Puis C2FT, C2TE, C2TE-S1, autres BOND, PROOF, FLOW, PAINT dans l'ordre du catalogue.

## Gestion des écarts
Si une image ne montre pas le bon procédé, si une phrase contient une valeur technique non approuvée, si un texte arabe est illisible ou si la palette sort des deux encres : marquer `À CORRIGER`, ne pas mettre le média en ligne, refaire le panneau, relancer audit visuel et CI, puis seulement publier.

## Limites
Le BAT flexographique reste à approuver par le laboratoire/HSE et l'imprimeur. Un contrôle technique source ne vaut pas validation du produit. Le lien « haute résolution » montre le PNG original validé graphiquement, mais aucune spécification chiffrée.
