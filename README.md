# NextGen Building Solutions — Site B2B (FR · AR · EN)

> **Statut au 1er novembre 2026 : préproduction technique préparée — NON DÉPLOYÉ SUR CLOUDFLARE.**
> Le catalogue public ne contient aucun produit réel approuvé. Les formulaires et l'API de réception sont désactivés.

## Dépôts et architecture

- **Site** : dépôt privé `Verwolfy/nextgen-website`, branche `main`. Astro 6, 3 langues dont arabe RTL, pages statiques et visionneuse de conditionnements 3D indicatifs.
- **ERP** : `Verwolfy/erp-mortier` — dépôt séparé. L'onglet CRM « Demandes NextGen » est présent mais reste désactivé par deux verrous serveur.
- **Supabase PROD** : `wenydirqtmkywbxbxfal` ; les migrations site 001 et 003 sont **déjà appliquées**, ne pas les rejouer. Tables privées `site_produits`, `site_demandes`, vue `site_products`.

## Tester le site sans déployer

```bash
npm ci
npm run build
python -m unittest discover -s tests -q
python scripts/check_built_pages.py
python scripts/preprod_static_audit.py
node --test tests/lead_endpoint.test.mjs
```

Recette navigateur Chromium (locale/CI) : `python scripts/check_browser_pages.py` après installation isolée de Playwright et Chromium. La CI GitHub exécute ces vérifications automatiquement.

## Sécurité et publication

- **Aucun navigateur ne reçoit** la clé Supabase service-role. L'export de catalogue est effectué uniquement par un processus serveur privé.
- Les produits fictifs ERP `PF-001` à `PF-006`, coûts, prix, recettes et documents fictifs ne doivent jamais être publiés.
- Les cinq GLB d'emballages sont uniquement des maquettes portant un avertissement de simulation et ne sont pas une homologation technique.
- `public/robots.txt`, la balise HTML robots et `public/_headers` bloquent l'indexation des pages **sans constituer un mécanisme de confidentialité**.
- `functions/api/lead.js` renvoie `503` tant que `NEXTGEN_LEADS_ENABLED` n'est pas exactement `true`. Turnstile, hostname, référence Supabase et rate-limit serveur/HMAC sont ensuite obligatoires, mais **ne sont pas configurés ni activés**.
- `.github/workflows/preprod-build-only.yml` effectue uniquement une vérification et publie un manifeste SHA-256 **interne à GitHub Actions**, jamais sur Cloudflare.
- Les previews Cloudflare Pages sont **publiques par défaut**. Avant toute création ou liaison du projet, établir Cloudflare Access et vérifier que le domaine principal `*.pages.dev` n'est pas accessible anonymement. Ne pas connecter le dépôt à Pages sans accord de publication ciblé.
- Les mentions légales, la durée de conservation, les transferts internationaux, la notice de confidentialité FR/AR/EN et le registre B2B exigent revue juridique : ne pas présenter les brouillons comme validés.

## Documentation de référence

- `docs/ETAT_AVANCEMENT.md` — journal et décisions historiques.
- `docs/LOT8_CLOUDFLARE_PREPROD.md` — protocole de préproduction sans déploiement.
- `docs/LOT6_PREPRODUCTION_GATE.md` et `docs/LOT7_REGISTRE_DONNEES_ET_VALIDATION.md` — décisions de conformité encore ouvertes.
- `docs/LOT7_RECETTE_NAVIGATION.md` — tests FR/AR/EN, mobile et captures.
- `sql/` — sources historiques de migrations déjà exécutées, **pas des scripts à rejouer**.

## Démarrage public : NO-GO

Aucun changement DNS, accès Internet Cloudflare, activation de formulaires, e-mail automatique, nouveau droit RLS/GRANT ou publication de produit n'a été autorisé dans ce lot. La vérification de la version réellement déployée dans Streamlit Cloud reste non confirmée (réponse HTTP anonyme 303).
