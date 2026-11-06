# Lots 101–103 — Favicon, Lighthouse bonnes pratiques et audit public V3

Date : 2026-11-06. Dépôt : `Verwolfy/nextgen-website`.
Base de la branche : `main` au commit `94ec0308fc8ee585ddd53fa0e0eb742e2994f2a2`.

## Source précise du défaut (lot 101)

Dans l’artefact brut Lighthouse du lot 98–100, `lighthouse-fr-home.json` :
- Catégorie `best-practices` : 96/100.
- Audit échoué : `errors-in-console`, score 0.
- Ressource à l’origine de l’erreur : `http://127.0.0.1:8765/favicon.ico` → HTTP 404.
- Ce diagnostic est issu du **build local** de GitHub Actions, et n’atteste pas un défaut sur le domaine public à lui seul.

Solution : ajouter `public/favicon.svg` avec monogramme NextGen bleu nuit/vert et le déclarer dans `src/layouts/Layout.astro` pour toutes les routes FR/AR/EN.
Aucun changement de logo officiel, de média Nexo/Geno, ni de charte générale.

## Lot 102 — Diagnostics et non-régression

- `scripts/summarize_v3_lighthouse.py` expose désormais les **audits Bonnes pratiques échoués**, leurs titres et URLs des ressources en cause ; scores restent informatifs, sans seuil arbitraire.
- `scripts/check_browser_pages.py` : vérification du lien `rel=icon` et du HTTP 200 de `/favicon.svg` sur les trois langues.
- `tests/test_lots101_103_favicon_public_audit.py` : SVG autonome, source Lighthouse 404 simulée, résultats de diagnostic, 9 pages simulées, redirects rejetés, protection de publication.
- Audit Lighthouse sur `/fr/`, `/ar/`, `/fr/catalogue/` et `/en/catalogue/fenek-proof-ep-anc/`.
- La valeur 100/100 en Bonnes pratiques sera rapportée **uniquement** si elle est confirmée par les runs d’Actions, sans convertir cela en métrique terrain ou en preuve de conformité WCAG globale.

## Lot 103 — Preuve du contenu public en lecture seule

- `scripts/check_live_v3_fullsite_readonly.py` : HTTP GET anonyme, aucune redirection suivie, aucune API Cloudflare ; contrôle SHA-256 de `/favicon.svg`.
- Vérifie 9 routes `/{fr,ar,en}/{catalogue,a-propos,contact}/` : HTTP 200, présence de respectivement 50 cartes de catalogue, 3 étapes de démarche ou 3 canaux de contact ; `noindex`, absence de formulaire actif et déclaration du favicon.
- Enregistre une preuve JSON privée conservée 7 jours.
- Le workflow existant `.github/workflows/live-v3-motion-readonly.yml` lance désormais le contrôle complet après la vérification de la vraie vidéo Nexo/Geno.
- Le contrôle se déclenche lors d’un push `main` touchant l’icône ou la mise en page.
- Une publication de contenu sur le domaine peut être attestée, **mais pas le SHA GitHub exact réellement déployé sur Cloudflare**.
- En cas de CDN non actualisé, le workflow signale une différence : pas de déploiement forcé et pas de changement DNS/Access.

## Protection permanente

- Les 50 références sont **provisoires** : ni `certifie`, ni `commercialise` ; ne pas fusionner la PR #50 sans validation R&D/Qualité/HSE.
- `noindex,nofollow`, `robots.txt`, formulaires inactifs, URL des 3 langues et original MP4/WebP Nexo/Geno inchangés.
- Aucune opération Supabase, ERP, Cloudflare, DNS, login, envoi de données ou service tiers.

## Reprise et contrôle final

1. Lancer les trois CI PR : compilation/sécurité, Chromium, Lighthouse ; corriger toute régression.
2. Comparer la catégorie Bonnes pratiques et ses audits avec le run 98–100, confirmer disparition de `errors-in-console` avant fusion.
3. Fusionner avec le SHA de branche attendu, vérifier les CI post-fusion et le contrôle public lecture seule.
4. Si la preuve publique échoue, indiquer explicitement les URLs/HTTP non conformes sans déclarer le déploiement réussi.
5. Prochain lot uniquement sur constats mesurés : autres pages, mobile, budgets d’images, accessibilité manuelle et données terrain. Aucun score Lighthouse de laboratoire ne prouve à lui seul des Core Web Vitals visiteurs.
