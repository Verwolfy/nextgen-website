# NextGen site — Lot 13 : revue visuelle et véracité de l'accueil

Date : 1er novembre 2026. **Code privé uniquement — pas de déploiement Cloudflare.**

## Base de l'audit visuel

- Dernier code `main` avant ce lot : `adbbf07d67282d9f0a364dd91637a8ed86d34cc7`, ses deux CI étaient `completed/success`.
- Artefact de captures du run navigateur [41331800296](https://github.com/Verwolfy/nextgen-website/actions/runs/41331800296) : `nextgen-lot7-internal-browser-screenshots`, ID `13093227397`.
- **21 captures** récupérées et examinées dans un montage interne : accueil et contact sur desktop FR/AR/EN ; accueil, gammes, à-propos, ressources et contact sur mobile 390 px FR/AR/EN.
- Constats fondés sur les captures : navigation mobile visible, contenu des trois hubs lisible ; **mascottes sur des rectangles blancs abrupts** dans la bannière sombre, nom de pays **Algérie** resté en français en arabe/anglais et section `LAB · FIELD · TRAINING` pouvant évoquer des prestations déjà opérantes. **Aucune inspection automatique ne prouve une conformité WCAG complète**, ni les apparences sur appareils physiques.
- La recette Chromium précédente n'a signalé aucun débordement horizontal significatif aux formats testés ; ce constat ne garantit pas tous les téléphones.

## Corrections du lot

1. **Présentoir mascottes** : encadrement clair et volontaire en CSS (`hero-mascot-card`), rayon et ombre, portrait secondaire harmonisé. **Les assets de marque originaux ne sont pas modifiés** et aucun nouveau visuel n'est généré.
2. **Étiquettes FR/AR/EN** : nom de pays localisé sur le héros ; statut explicite **site en préparation, aucun produit réel approuvé pour publication**. Bouton secondaire de l'accueil renommé **Nous contacter / تواصل معنا / Contact us** et conservé sur la page Contact, où les canaux directs sont accessibles.
3. **Démarche non homologuée** : remplacer sur l'accueil la liste marketing `LAB · FIELD · TRAINING` par les trois étapes de travail déjà décrites sur `À propos`, accompagnées de la réserve explicite qu'aucun produit, service ou résultat laboratoire n'est encore attesté comme disponible ou certifié.
4. **Contrôle** : nouveau `tests/test_lot13_home_visual.py`, contrôles du bloc d'accueil dans `scripts/check_browser_pages.py`, plus **3 captures mobiles 320 px** supplémentaires dans les artefacts privés.

## Sécurité et portée

- Pas de changement `public/data/products.json` : le catalogue reste vide.
- Formulaires, réception `/api/lead` et synchronisation de données non activés.
- Aucune affirmation nouvelle de tarif, performance, certification, FT/FDS, disponibilité fournisseur ou juridique.
- Aucun changement à Supabase, ERP, SQL, RLS/GRANT, Secrets, DNS, Cloudflare Pages ou Access.
- Les tests sur captures sont locaux, et ne constituent pas une publication ou un contrôle d'accès cloud.

## Validation

```bash
node scripts/copy_public_assets.mjs
python -m unittest discover -s tests -v
npm ci && npm run build
python scripts/check_built_pages.py
python scripts/preprod_static_audit.py
python scripts/check_browser_pages.py
```

Le dernier contrôle utilise Playwright/Chromium isolé dans la CI ; les deux workflows de PR doivent réussir avant fusion. Une fois fusionné, vérifier les deux workflows du dernier SHA `main`, sans confondre tests GitHub et mise en ligne réelle.

## Suite

Revoir les nouvelles captures 320/390 px et corriger tout défaut avéré. Une démonstration Cloudflare reste **NO-GO** tant que l'authentification et les politiques Access des domaines Pages principal, previews et URL permanentes ne sont pas vérifiées avant déploiement, et tant que les validations juridiques et commerciales ne sont pas obtenues.
