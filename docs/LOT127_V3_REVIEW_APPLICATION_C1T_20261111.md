# NextGen — Lot 127 : modes d'emploi V3, intégration contrôlée produit par produit

Date : 11 novembre 2026 — dépôt `Verwolfy/nextgen-website`. Branche `feat/lot127-v3-guides-product-by-product-c1t-20261111`.

## Objectif utilisateur
Enrichir les 50 fiches produit avec le lot d'illustrations `NEXTGEN_modes_emploi_V3.zip` (50 dossiers, 300 PNG et 300 SVG, `index.csv`), mais **contrôler chaque référence et chaque geste avant publication** ; corriger ou bloquer les illustrations non conformes. L'ancien rendu V2 a été rejeté. Les V3 restent des illustrations éditoriales **BROUILLON**, non des FT/FDS approuvées.

## Référence intégrée : 1/50 — BOND-C1T
- Source du ZIP : `fenek-bond-c1t`, `pf_id=BOND-C1T`, 6 PNG + 6 SVG + `legendes.csv`, `sources.txt`, `valeurs_a_valider.txt`.
- Concordance exacte avec `src/data/catalogue-projets.json` : code `BOND-C1T`, slug `fenek-bond-c1t`, gamme `bond`.
- Étapes auditées : 01 support, 02 EPI, 03 gâchage sans chiffres, 04 repos/remalaxage conditionnel, 05 encollage cranté, 06 pose.
- Sécurité : illustrations de gants/lunettes/masque, mais la FDS définitive doit confirmer les EPI. Le dosage, le poids de référence, la durée de repos et le temps ouvert sont **[LABO]**, absents des légendes.
- 6 images 2048x2048 ; palette exacte écran #1B365D / #009A44 / réserve blanche. Légendes bilingues AR/FR déjà dans l'art original. Une courte explication localisée FR/AR/EN est placée sous chaque image.
- Sprite WebP destiné au **site** : 2160×1440 en grille 3×2 ; **211 998 octets**, SHA-256 `9ba666ddca06c036e4f84c19416b03ea5f75e51d2ea55129d3527d58a4e166e3`. Le ZIP V3 original reste inchangé.
- Chemin GitHub : `public/images/application-v3/fenek-bond-c1t-steps.webp`.

## Modifications code
- `src/data/fenek-v3-reviewed.ts` : **registre explicite** des références revues ; le code et le slug sont contrôlés. Pour le moment, seule `BOND-C1T` est éligible.
- `src/components/FenekApplicationGuide.astro` : reprend les 6 illustrations du sprite V3 uniquement si la référence est enregistrée ; conserve les pictogrammes et anciens dessins pour les 49 autres. Affichage 3 colonnes desktop, 2 colonnes tablette et cartes lisibles pleine largeur sur mobile. Aria-label détaillé, mode nuit et RTL conservés.
- `scripts/check_application_guides.py` : contrôle 150 pages et empêche qu'un produit non revu reçoive un visuel V3.
- `scripts/check_live_application_guides.py` : vérifie le sprite et les 6 étapes C1T en Cloudflare **après comparaison du SHA déployé**.
- `tests/test_lot127_v3_c1t_review.py` : intégrité SHA, bonnes légendes, sécurité non-certifiée, absence de dosage inventé, aucun autre produit modifié.
- `scripts/check_browser_pages.py` : contrôle Chromium mobile/desktop FR/AR/EN, lisibilité, sprite, débordements, capture et absence de fuite de V3 vers C1TE.

## Anomalies détectées dans le lot non encore publié
- **BOND-R4, étape 04** : la pastille du visuel affiche **« 3 »** au lieu de **« 4 »**. Doit être corrigée avant publication du R4.
- Certains panneaux montrent des opérations génériques hors contexte ; auditer par produit la séquence visuelle, la légende et les exigences HSE avant d'activer la référence.
- Les images portent des légendes **AR/FR incrustées**. En page EN, une description anglaise est ajoutée sous les images ; aucune traduction dans l'illustration source n'est inventée.

## Protection des données
- Pas d'écriture Supabase et pas de changement de catalogue commercial ou de statut `certifie` / `commercialise`.
- Pages `noindex`, Pagefind conservé, avis `BROUILLON` et FDS/FT non validées conservés.
- Ne pas réutiliser un dessin d'un code produit différent même si le geste est identique sans l'avoir explicitement revu.
- Aucune revendication de certification flexographique ; les valeurs Pantone réelles et le BAT sont à valider par l'imprimeur.

## Recette et prochaine référence
1. PR et CI GitHub : build/sécurité, tests 50×3, navigateur, Lighthouse, Cloudflare smoke (étape PR hors-ligne).
2. Fusion sur `main` seulement après succès des tests applicables ; vérifier Cloudflare live indépendamment.
3. Ensuite traiter **BOND-C1TE**, puis la liste des 48 restantes suivant l'ordre du catalogue.
4. Contrôler visuellement les six dessins de chaque référence, leurs légendes, leur numérotation, leur cohérence technique et l'absence de valeurs [LABO] chiffrées.
