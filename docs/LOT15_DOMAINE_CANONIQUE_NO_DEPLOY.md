# Lot 15 — Domaine canonique NextGen, sans déploiement

Date : 1er novembre 2026.

## Constats
- L'utilisateur rapporte que `nextgen-buildingsolutions.com` et `www.nextgen-buildingsolutions.com` sont Active/SSL, et qu'une ancienne adresse Pages `nextgen-website-8te.pages.dev` existe. Ces états ne sont **pas vérifiés indépendamment** : les tentatives HTTP externes ici ne donnent pas de résultat exploitable et le conteneur ne résout pas les DNS concernés.
- La version précédente de `astro.config.mjs` fixait `site` à `https://www.nextgen-buildingsolutions.com`; `Layout.astro` utilisait `Astro.url.origin` pour canonical/hreflang. Ce problème est confirmé dans le code.

## Correction livrée
- Astro `site: 'https://nextgen-buildingsolutions.com'`.
- Canonical/hreflang issus de `Astro.site?.origin`, avec fallback même apex, plutôt que de l'URL de la requête (qui pourrait être `www` ou `pages.dev`).
- Tests unitaires `tests/test_lot15_canonical_domain.py` et garde-fous : `noindex,nofollow`, `robots.txt Disallow: /`, catalogue vide et aucun formulaire actif.

## Réglages non effectués
1. Dans Cloudflare, règle `www.nextgen-buildingsolutions.com/*` → `https://nextgen-buildingsolutions.com/${path}`, code **301**, préservation du chemin et de la query (préférer expression `concat("https://nextgen-buildingsolutions.com", http.request.uri.path)` avec `Preserve query string`). Cette modification DNS/Redirect Rules n'est pas réalisée dans le compte, faute de connecteur Cloudflare.
2. Protéger les hôtes `*.pages.dev` (en particulier l'hôte principal et les previews par hash), avec Access; ne pas supposer qu'une règle de redirection du domaine custom suffit. Prévoir la couverture du domaine apex également avant démonstration privée. Access peut nécessiter un traitement différent pour l'hôte principal Pages et les previews. Ne jamais laisser anonymement exposées les URL immuables.
3. Confirmer les MX/SPF/DKIM/DMARC et les alias (mail, autoconfig, autodiscover), sans écraser les enregistrements existants. Tester les réponses réellement reçues et envoyées.
4. N'effectuer aucun déploiement Cloudflare Pages non approuvé : `Active`/SSL ne valide ni la confidentialité ni la conformité des contenus.

## Email
Depuis le compte Gmail connecté `nextgen.build.solutions@gmail.com`, un **test d'envoi** vers `contact@nextgen-buildingsolutions.com` a été effectué le 01/11/2026 (ID Gmail `1a198ad43834f9d9`). L'envoi Gmail n'atteste ni arrivée côté Private Email ni réponse; cet aller-retour est à contrôler sur la boîte destinataire.

## Reproduction
```bash
npm ci
npm run build
python -m unittest discover -s tests -v
python scripts/check_built_pages.py
```
La CI de PR puis celle de `main` fournissent les preuves de compilation; elles ne prouvent pas un redéploiement Cloudflare.
