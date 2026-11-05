# Lots 76 à 78 — Déploiement, visuels et validations FENEK-PROOF

Date : 2026-11-05. Dépôt `Verwolfy/nextgen-website`. Objectif : exécution groupée **sans activer de publication non validée**.

## Lot 76 — Déploiement : constats et limites

- `main` avant ces lots : `84c64bb3b4cab40ba9ebe638873673f465387f7d`.
- Les CI de `site-check.yml` et `site-browser-recette.yml` sont des contrôles de compilation, sécurité et navigation, pas des preuves de déploiement.
- `site-check.yml` dépose une archive privée `dist` ; aucun appel Cloudflare de déploiement dans ce workflow.
- `sync-site.yml` reste bloqué par défaut via `NEXTGEN_SYNC_ENABLED`, n'est pas un déploiement Pages et ne doit pas être déclenché ici.
- Le runbook historique `docs/DEPLOIEMENT_CLOUDFLARE_RUNBOOK.md` contient la preuve précédente (lot 62–63) d'un HTTP 200 anonyme sur le domaine principal, en date du 5 novembre, **sans prouver que le commit courant y est publié**.
- La consultation directe du domaine depuis le moteur web disponible pendant cet audit a échoué ; impossible de conclure à une panne ni de vérifier le commit effectif.
- Décision utilisateur lot 63 : **laisser le domaine principal accessible publiquement** ; conserver `noindex,nofollow`, formulaires désactivés et protections des previews.
- Le commit réellement servi par Cloudflare doit être confronté aux déploiements Cloudflare (lecture seule) ou à un marqueur de build non sensible, une fois un accès Cloudflare autorisé. **Aucune modification DNS/Access/Cloudflare.**

## Lot 77 — Conformité des maquettes

- 11 références FENEK-PROOF sont associées à des numéros de maquette dans `src/lib/catalogue-projets.ts`.
- Référentiel de revue ajouté : `docs/catalogue-interne/audit_visuels_proof_11_20261105.json`. Il consigne exactement les codes, formats du catalogue, présentations du registre et chemins des visuels conceptuels existants.
- Les **11/11 images restent « NON VERIFIE »** pour la correspondance à l'emballage industriel réel. Une maquette attribuée à la bonne référence n'est pas un certificat de correspondance du format, du nombre de contenants ou de l'étiquette.
- Ne pas remplacer une maquette par un visuel générique présenté comme certifié ni retoucher les images pour masquer l'état de validation. Le site conserve ses avertissements de maquette éditoriale.
- Pour une validation future : photographie datée d'un échantillon réel et approbation d'étiquette par Qualité, Production et Commercial.

## Lot 78 — Registre des validations manquantes

- 11/11 références FENEK-PROOF ont un conditionnement nominal renseigné dans le catalogue depuis le lot 72.
- Pour chacune : **validations industrielle, commerciale, R&D et Qualité/HSE EN ATTENTE** ; validation de visuel physique NON VERIFIE ; autorisation de publication de FT/FDS et création SKU ERP absentes.
- Les chiffres des conditionnements déclarés ne prouvent pas un ratio de mélange, une composition chimique ou des propriétés d'usage.
- Test automatisé `tests/test_lots76_78_audit_deploiement_visuels.py` : synchronisation registre/code, correspondance des codes maquettes, aucun statut d'approbation inventé, protections noindex et absence de commande de déploiement non approuvée.

## Décisions et dépendances pour les lots suivants

1. Poursuivre le contrôle de cohérence des pages imprimables et de leurs avertissements.
2. Lorsque les preuves sont disponibles, examiner **en lecture seule** le commit Cloudflare publié ; ne pas promettre que la fusion sur GitHub actualise automatiquement le site.
3. Ne produire ni certificat, ni FDS, ni SKU sans pièces vérifiables et approbations explicitement documentées.
4. Les changements de publication, d'accès Cloudflare, de DNS, de formulaire, de Supabase et d'ERP sont hors périmètre.

## Commandes de validation

`python -m unittest discover -s tests -v` et les deux workflows CI du dépôt, suivis des deux CI post-fusion sur `main`.
