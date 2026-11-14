# Lot 36 — Audit des pages légales et galeries (02/11/2026)

## Sources inspectées dans main
- `src/pages/[lang]/[section].astro`
- `src/data/site.ts`
- `src/layouts/Layout.astro`
- `src/pages/[lang]/maquettes.astro`
- `src/pages/[lang]/emballages.astro`
- `src/pages/[lang]/emballages/[slug].astro`
- `src/data/showcase.ts`, `src/data/editorial.ts`, `src/data/contact-channels.ts`

## Constats
1. Les pages `/fr|en|ar/mentions-legales/` et `/fr|en|ar/confidentialite/` sont générées par `[section].astro`. Il n'existe pas de pages Astro dédiées à ces routes. Leur contenu actuel est une brève description, une localisation/raison commerciale (légal) ou une adresse de contact (confidentialité).
2. Le code ne fournit pas de registre de commerce, NIF/NIS, entité responsable juridiquement vérifiée, responsable du traitement, finalités et durées de conservation étayés. Ne pas inventer ces champs.
3. Les six pages Contact/Distributeurs ont fait l'objet d'une sonde externe documentée réussie (Actions #41519955455, PR diagnostic #30 fermée sans fusion). Le site ne propose plus de formulaires de démonstration actifs.
4. `maquettes.astro` présente 46 illustrations par langue comme visuels graphiques, et non fiches techniques. `emballages.astro` présente cinq maquettes GLB, sans promesse de disponibilité ou certification. Cette qualification doit être maintenue tant qu'aucune validation de produit n'est acquise.
5. `Layout.astro` conserve `noindex,nofollow`. Il ne faut pas lever l'exclusion des robots sans qualification des contenus juridiques/produits.
6. La revue de texte source ne vérifie pas les avertissements éventuellement **imprimés dans les pixels** des WebP/affiches 3D ; un audit visuel image par image reste nécessaire.

## Actions recommandées, sans invention
- Obtenir auprès du responsable légal les champs exacts des mentions obligatoires et leur preuve officielle, puis rédiger des pages FR/EN/AR cohérentes.
- Formaliser les flux de données réels (hébergement, journaux techniques, e-mail/WhatsApp externes, cookies, durées, droits) avant la rédaction de la politique de confidentialité.
- Réaliser un contrôle visuel des 46 WebP et des cinq posters GLB, et ne remplacer que les ressources éditoriales approuvées.
- Maintenir la séparation du site NextGen avec les données ERP/Supabase ; aucun formulaire/CRM ni collecte ne doit être activé sur la base de ce seul audit.

## Limites et statut
Audit **source seulement**, sans build Astro, test navigateur ni nouvelle sonde HTTP exécutés lors de ce lot. Aucun changement de pages publiques, de RLS, de base Supabase ni de données de produits. Statut : **audit documenté, corrections légales à qualifier**.
