# Lots 91 à 93 — Performance, accessibilité et sobriété CSS de la V3

Date : 2026-11-05. Dépôt : `Verwolfy/nextgen-website`. Base main : `ccb7f59bbfda5b7a7b5c9c98b6398cf92e040df2`.

## État précédent confirmé
- PR #88 (lots 81–83), #89 (84–86), #90 (87–89), #91 (90) fusionnées.
- CI de `main` après PR #91 : build/sécurité run `42115764253` **success** ; Chromium run `42115764258` **success**.
- HTTP anonyme externe `42115764162` **success** : accueils V3 en FR/AR/EN, affiche et MP4 identiques à la source, `noindex` maintenu. Le SHA Cloudflare exact n'a pas été prouvé.

## Lot 91 — Médias, performance de démarrage
- `src/layouts/Layout.astro` : précharge le poster original de 23 470 octets seulement sur `/fr/`, `/ar/`, `/en/`; `fetchpriority="high"`. Le MP4 est inchangé (180 900 octets), non préchargé, toujours assigné via `IntersectionObserver` lorsque nécessaire.
- `src/components/HeroWelcomeVideo.astro` : respecte `prefers-reduced-motion` et le signal facultatif `navigator.connection.saveData`. Dans ces cas le poster reste visible jusqu'au clic explicite sur Lecture. Lecture/pause manuelle, fermeture onglet et contexte d'intersection conservent les protections existantes.
- Aucune garantie chiffrée LCP n'est revendiquée : il faut une mesure navigateur distincte.

## Lot 92 — Mobile et accessibilité
- `scripts/check_browser_pages.py` : nouvelles recettes FR/AR/EN à **320 px**, réduction des animations, contrôle de débordement, contrôle de l'affiche chargée et bouton de lecture ; simulation Data Saver avec démarrage exclusivement manuel.
- `src/styles/v3.css` : les images packshot des cartes et fiches sont montrées avec `object-fit:contain` pour éviter les étiquettes coupées ; focus en contrastes forcés ; survol réduit si préférence d'animations réduites.
- `ConceptCatalogue.astro` et `catalogue/[slug].astro` : `decoding="async"` ajouté aux visuels chargés paresseusement, sans changement de contenu ni de source.

## Lot 93 — Mesures statiques et garde-fou CSS
- `scripts/check_v3_static_payload.py` relève le poids source de la vidéo, de l'affiche, du CSS V3, le nombre et poids cumulés des WebP de catalogue, et dans `dist`, les tailles (et estimation gzip) des trois accueils et des feuilles CSS compilées.
- Budgets source : MP4 ≤ 250 Kio ; affiche ≤ 30 Kio ; CSS source V3 ≤ 24 Kio. Ce sont des limites de prévention de régression, **pas des mesures Lighthouse ni des scores Core Web Vitals**.
- `.github/workflows/site-check.yml` exécute cet audit après compilation et archive un JSON léger dans les artefacts privés 7 jours.
- Trois variables CSS V3 inutilisées supprimées ; ne pas fusionner les styles de fiches imprimables avec le thème écran.
- Nouveau test `tests/test_lots91_93_v3_performance_accessibility.py`.

## Contraintes non négociables
- Garder les fichiers MP4/WebP originaux et leurs empreintes ; traductions FR/AR/EN et mise en page RTL.
- 50 références FENEK provisoires (non certifiées / non commercialisées), sans donnée technique ajoutée.
- Conserver `noindex,nofollow`, `robots.txt`, absence de formulaire actif, ni écriture ERP/Supabase.
- Aucun changement Cloudflare, DNS ou accès public. La CI réussie n'est pas un certificat de déploiement Cloudflare.
- Distinguer poids de fichier, mesure navigateur et métriques terrain (LCP/INP/CLS).

## Suite
1. Vérifier Astro/sécurité et Chromium sur la PR, corriger tout échec ; ne fusionner qu'après les deux résultats verts.
2. Vérifier les CI post-fusion sur `main`.
3. Relever les chiffres de l'artefact JSON et préparer un audit Lighthouse mesuré depuis un navigateur/runner autorisé (pas de chiffres inventés).
4. Prochain bloc : documentation des performances et audit accessibilité approfondi WCAG, sans lever les protections de publication.
