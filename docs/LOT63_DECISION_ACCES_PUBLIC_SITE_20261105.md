# Lot 63 — Décision d'accès public au site NextGen

Date : 2026-11-05
Dépôt : `Verwolfy/nextgen-website`

## Décision explicite du propriétaire

En réponse à la question « souhaites-tu que nextgen-buildingsolutions.com reste accessible publiquement, ou qu'il devienne une préproduction privée protégée par Cloudflare Access ? », l'utilisateur a répondu : **« reste accessible publiquement »**.

**Décision enregistrée : le domaine principal `https://nextgen-buildingsolutions.com` doit rester accessible sans authentification Cloudflare Access.** Aucune action de restriction d'accès sur le domaine principal ne doit être entreprise pour ce motif.

Cette décision concerne **l'accessibilité publique**, pas l'autorisation de :
- supprimer les protections `noindex,nofollow`, `X-Robots-Tag` et `robots.txt` ;
- activer les formulaires ou la collecte de données ;
- publier des tarifs, certifications, FT/FDS officielles ou valeurs techniques non validées ;
- exposer des produits en attente de validation juridique, commerciale, industrielle et HSE ;
- désactiver Cloudflare Access sur les hôtes `pages.dev` ou de prévisualisation.

Le site peut donc être publiquement **consultable** tout en restant **non indexable** pour l'instant. La décision de lancer son référencement commercial sera traitée séparément.

## État technique vérifié

Contrôle HTTP anonyme GitHub Actions du 2026-11-05 à 15:22 UTC, run `42054220008` :
- `https://nextgen-buildingsolutions.com/fr/` : **200** anonyme ; marqueur V2 présent ;
- MP4 Nexo/Geno V2 : **200**, **181 635 octets**, SHA-256 attendu ;
- poster WebP V2 : **200**, **17 244 octets**, SHA-256 attendu ;
- `www.nextgen-buildingsolutions.com` : redirection **301** vers le domaine principal ;
- `nextgen-website-8te.pages.dev` : redirection **302** vers Cloudflare Access.

Ces constats ne prouvent pas l'autorisation des contenus ou la version intégrale de chaque route. Le dernier code vérifié avant cette note est `main` commit `204e106bb22b5c4d6e9ce052d858244d8e7be276`; les deux workflows post-fusion (compilation/sécurité et Chromium) sont **success**.

## Actions appliquées

1. Décision enregistrée dans la documentation GitHub.
2. **Aucune modification** des accès Cloudflare, DNS, certificats, URLs, médias, code de présentation, robots, API ou Supabase : le domaine principal est déjà accessible conformément au choix.
3. Aucun changement des politiques distinctes de protection des previews `pages.dev`.

## Prochaines étapes sûres

1. Maintenir les tests et contrôles HTTP en lecture seule de la version V2.
2. Préparer séparément la revue juridique/commerciale de lancement, la politique de confidentialité et le contrôle des contenus avant toute levée éventuelle de `noindex`.
3. Continuer la qualification des **sept kits FENEK-PROOF** (lot 57), sans déduire leurs contenances de documents tiers.
4. Avant toute activation de formulaires, exiger consentement et vérifications techniques HSE, sécurité, confidentialité et stockage.

**Important :** ne pas interpréter cette décision d'accès public comme une validation de publication des données produits.
