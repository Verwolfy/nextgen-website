# Lot 37 — Parcours B2B et contact produit contextualisé

Date : 2 novembre 2026. Base : `main` `f3a7c5ae23c3fb5dce6b0fce473001f6b78b39e2`.

## Objectif
Après l'audit du site, orienter les professionnels vers les contacts pertinents sans créer de fausses prestations ni réactiver les formulaires de collecte.

## Modifications
- Accueil FR/AR/EN : section à deux parcours explicites, **entreprises/projets** vers Contact et **distribution/partenariats** vers Distributeurs. Le texte rappelle que spécifications et disponibilité sont à confirmer auprès de NextGen.
- Fiches catalogue FR/AR/EN : action `mailto:` avec objet encodé comprenant la **référence effectivement consultée**. Le lien historique vers la page Contact est conservé. L'envoi appartient à l'application e-mail de l'utilisateur.
- Aucune nouvelle image et aucune promesse de certification, performance, prix, stock ou délai.
- Tests de code et contrôles Chromium mis à jour pour les trois langues, ordinateur/mobile.

## Restrictions
Les 50 références restent des présentations éditoriales ; `public/data/products.json=[]`. Aucun formulaire, CRM, piste client en base, script de suivi, cookie, modification Supabase, RLS, robots ou Cloudflare. Les pages juridiques restent à compléter avec des documents vérifiés.

## Validation requise
Deux workflows CI (build/sécurité et navigateur) verts sur la tête de PR, puis fusion GitHub `main`. Après fusion, contrôler la CI et la publication Cloudflare ; l'accès HTTP au domaine peut nécessiter une sonde externe distincte.

## Travaux suivants
Lot 38 : recherche/filtrage accessible des 50 fiches catalogue, sans indexation ni données de production. Revoir l'ergonomie mobile avec tests E2E. Lot juridique : attendre pièces réelles validées avant publication.
