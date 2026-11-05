# Lots 87–89 — Refonte V3 des pages institutionnelles et parcours B2B

Date : 2026-11-05. Dépôt : Verwolfy/nextgen-website. Base : `main` après lots 84–86.

## Résultat des lots précédents
- PR #88 fusionnée (commit `daa17fed9519abd8d9bffed22c9ddb3612b75b49`) ; tests Astro/sécurité, Chromium et HTTP V2 post-fusion verts. MP4 Nexo/Geno original conservé.
- PR #89 fusionnée (commit `1d6f7e3ece4db5257a2ec24d16681b690ebb8873`) ; tests PR Astro/sécurité et Chromium réussis. CI post-fusion en cours lors du début du présent lot.

## Lot 87 — Pages Entreprise & Solutions
- La présentation `AboutStory.astro` et ses 3 étapes industrielles restent intactes, avec conservation de Nexo/Geno.
- Le CSS V3 donne aux pages institutionnelles une en-tête premium bleu nuit/vert sobre et réduit visuellement la mascotte pour laisser la place à la démarche industrielle.
- Les cartes `RangeOverview` conservent les 4 gammes, les termes FR/AR/EN et les avertissements réglementaires.

## Lot 88 — Distribution & Contact
- Le lien Contact de la navigation reçoit un traitement visuel CTA sans altérer les URLs ou le menu mobile.
- Les trois canaux email/WhatsApp/téléphone sont mieux mis en avant, en conservant les applications externes et l'absence d'envoi sur le site.
- La page distributeurs et ses canaux restent compatibles avec la même présentation.

## Lot 89 — Ressources
- Deux blocs Ressources plus lisibles : descriptifs produits et données de sécurité sur demande. Les PDF/FT/FDS non validés ne sont pas activés.
- Contrastes, fonds, boutons, états focus et mode sombre harmonisés.

## Détail technique
- Modification `src/styles/v3.css` uniquement pour le rendu, sans changement d'API ni de contenu commercial.
- Test `tests/test_v3_lots87_89_institutional_b2b.py` : navigation, protections SEO, désactivation des formulaires, deux cartes ressources, liens B2B externes.
- Tous les textes restent trilingues, existants et validés comme présentations provisoires.
- Pas de modification Cloudflare, DNS, Supabase, ERP, mail, réseaux ni formulaire.

## Prochaines actions
1. Tester la PR en Astro/sécurité puis Chromium ; corriger tout échec avant fusion.
2. Fusionner avec vérification du SHA de tête et vérifier CI post-fusion.
3. Audit HTTP de la présence V3 sur les pages publiques via GitHub Actions en lecture seule, sans déploiement manuel ni modification d'accès.
4. Lot suivant : qualité des images / performance (LCP/CLS), parcours mobile RTL et rationalisation du CSS. Garder `noindex` jusqu'à validation explicite.
