# Lot 94 — Accessibilité clavier trilingue, suite refonte V3

Date : 2026-11-05. Dépôt `Verwolfy/nextgen-website`. Référence de départ : `main` `de38aa046f1bf350ab2ed85a767a515c351428d2`.

## Résultat précédent
- PR #92 (lots 91–93) a été fusionnée sur `main` pendant l'exécution d'une autre branche de travail.
- Elle couvre déjà le préchargement de l'affiche Nexo/Geno, le mode réduction des animations, Data Saver, décodage asynchrone des packshots, non-rognage des étiquettes et budgets médias/CSS.
- Ses tests build/sécurité et Chromium ont réussi ; `main` est resté à `de38aa046f1bf350ab2ed85a767a515c351428d2` au début de ce lot.
- L'ancienne PR #93, qui doublonnait ces modifications et était devenue non fusionnable, a été **fermée sans fusion**, afin de préserver la PR #92.
- Diagnostic réel du run build `42117935796` : MP4 180 900 octets, affiche 23 470, CSS V3 22 030 ; budgets source respectés. Ce ne sont **pas** des Core Web Vitals (LCP/INP/CLS).

## Modification spécifique (non couverte par #92)
- `src/layouts/Layout.astro` : le lien d'évitement s'affiche maintenant dans la langue courante avec un libellé entièrement localisé :
  - FR : « Aller au contenu principal ».
  - AR : « الانتقال إلى المحتوى الرئيسي ».
  - EN : « Skip to main content ».
- `scripts/check_browser_pages.py` : le test de navigation sans JavaScript contrôle à 320 px la position clavier du premier lien, sa visibilité au focus, la destination `#main`, le RTL et l'absence de débordement pour les trois langues ; vérifie également la cohérence du libellé sur la page Contact.
- `tests/test_lot94_keyboard_skip_a11y.py` : assertions de structure, styles focus et protections de publication.

## Protections
- Vidéo/affiche originales conservées, y compris Data Saver et reduced-motion.
- Aucune modification de `noindex`, `robots.txt`, formulaire, Cloudflare, DNS, Supabase, ERP, catalogue ou fiches techniques.
- Aucun nouveau service tiers.
- Un test de clavier réussi ne constitue pas un audit WCAG exhaustif.

## Reprise
1. Valider build/sécurité et Chromium sur PR, corriger tout échec.
2. Fusionner sur `main` avec contrôle SHA puis vérifier les deux CI post-fusion.
3. Poursuivre l'audit avec des mesures de terrain (Lighthouse/WCAG manuel), sans inventer de scores.
