# NextGen Site — Lot 14 : parcours Contact / Distributeurs

**Date :** 1er novembre 2026. **Statut :** code de démonstration privé, zéro publication Cloudflare, zéro formulaire actif.

## Problème

Le site affichait des formulaires de devis/distributeur dont tous les champs étaient désactivés mais visuellement dominants. Les canaux e-mail, téléphone et WhatsApp étaient dupliqués sur la page Contact et dans ces maquettes. Le lien « Devenir distributeur » menait vers un formulaire qu'il était impossible d'envoyer.

## Corrections

- `src/data/contact-channels.ts` : textes et avertissements FR/AR/EN.
- `src/components/ContactChannels.astro` : **trois cartes de contact direct** sur les deux parcours, liens `mailto:`, `tel:` et `https://wa.me/` construits depuis les coordonnées déjà présentes dans `brand`. WhatsApp s'ouvre dans une fenêtre externe avec `rel="noopener noreferrer"`. Téléphone et courriel restent directionnellement LTR même sur les pages arabes RTL.
- Les avertissements expliquent que ces liens ouvrent des applications tierces, et que **la réception effective des messages n'a pas été vérifiée**. Aucune promesse de délais, de disponibilité 24/7 ni de service opérationnel.
- `src/components/LeadForm.astro` et `src/data/lead-forms.ts` : les contrôles de formulaire, **tous désactivés**, sont maintenant placés derrière un `<details>` initialement fermé (consultable clavier/souris/tactile). Aucun `<form>`, script client, action d'envoi ou transport réseau.
- `src/pages/[lang]/[section].astro` : cartes de contact en premier sur Contact et Distributeurs ; lien d'ancrage « Contact » prioritaire chez les distributeurs et lien secondaire vers l'aperçu de candidature non fonctionnel. Introduction Contact recontextualisée dans les trois langues.
- `src/styles/site.css` : cartes adaptatives desktop/mobile, focus clavier, hiérarchie visuelle et éléments RTL.
- `scripts/check_browser_pages.py` : recette Chromium sur 390px et 320px, existence des trois liens, statut d'envoi désactivé, panneau fermé puis ouvert/refermé par l'utilisateur, absence de débordement, captures internes supplémentaires sur Contact et Distributeurs.
- `tests/test_lot14_contact_journey.py` et mise à jour de `tests/test_lead_forms.py` : aucun envoi ni produit non vérifié ; contrôles d'accès et sécurité inchangés.

## Critères de validation

```bash
node scripts/copy_public_assets.mjs
python -m unittest discover -s tests -v
npm ci && npm run build
python scripts/check_built_pages.py
python scripts/preprod_static_audit.py
python scripts/check_browser_pages.py
```

Les deux workflows GitHub Actions doivent réussir sur la PR avant fusion et être contrôlés ensuite sur le commit `main`.

## Garde-fous

- Pas de produit commercial réel ni de prix. `public/data/products.json` reste `[]`.
- Aucun envoi CRM, aucune collecte par le site, aucun Turnstile, API, secret ou cookie activé.
- Les applications tierces externes sont utilisées **uniquement après clic volontaire** de l'internaute ; aucune requête externe lancée par les pages.
- Aucune modification ERP, Supabase, SQL/RLS/GRANT, DNS, Cloudflare Access ou Pages. Lancement privé/public : **NO-GO** sans protection effective des domaines et approbation juridique/commerciale.
- Cette évolution facilite la prise de contact via les coordonnées affichées, mais **ne prouve pas** que leurs boîtes/numéros sont effectivement joignables.

## Étape suivante

Revoir les captures générées en CI, notamment FR/AR/EN en 320px et la présentation des panneaux repliés. Corriger des défauts si nécessaire, puis préparer les validations externes d'accès/mentions juridiques — sans déployer automatiquement.
