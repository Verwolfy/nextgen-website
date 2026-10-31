# Lot 2 — site Astro trilingue (développement, publication interdite)

- Pages statiques FR/AR/EN, sens RTL arabe, gammes Fenek, catalogue privé synchronisé et fiches générées uniquement depuis `public/data/products.json`.
- Les 6 références ERP existantes étant fictives, `public/data/products.json` vaut `[]`; aucune fiche fictive publiée.
- Contact par e-mail et WhatsApp uniquement : aucun formulaire ni enregistrement de données sans contrôle juridique.
- Site protégé contre indexation : `noindex,nofollow` et `robots.txt` Disallow /. À retirer seulement après GO public et validation légale.
- Assets `public/images` dérivés du logo exact JPG, de Nexo et du duo Nexo/Geno fourni ; pas de redessin.
- `package.json` Astro 6.4.6 fixé mais **pas de package-lock.json ni de preuve de build** tant que l'installation npm n'est pas accessible. Ne pas déployer avant CI et test mobile / SEO.
- Hébergement prévu : Cloudflare Pages, `npm run build`, `dist`; connexion DNS non autorisée à ce stade.

- Synchronisation sur GitHub volontairement suspendue par défaut : variable `NEXTGEN_SYNC_ENABLED` à activer seulement après configuration des secrets, tests d'accès et validation de l'exploitation.
- Workflow dédié `lockfile.yml` : génération puis commit du lockfile npm en CI, sans accès à Supabase ; vérifier la réussite et la présence de `package-lock.json`.
