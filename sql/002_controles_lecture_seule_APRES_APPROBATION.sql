-- AUDIT A EFFECTUER APRES APPLICATION APPROUVEE. LECTURE SEULE.
SELECT to_regclass('public.site_produits') AS table_publication,
       to_regclass('public.site_products') AS vue_export;
SELECT c.relname AS objet, c.relkind AS type, c.relrowsecurity AS rls,
       has_table_privilege('anon', c.oid, 'SELECT') AS anon_select,
       has_table_privilege('authenticated', c.oid, 'SELECT') AS authenticated_select,
       has_table_privilege('service_role', c.oid, 'SELECT') AS service_role_select
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname='public'
  AND c.relname IN ('site_produits', 'site_products');
SELECT (SELECT COUNT(*) FROM public.site_produits) AS brouillons_publication,
       (SELECT COUNT(*) FROM public.site_products) AS fiches_exportees;
-- Attendues avant ajout de produits REELS : 0 fiches exportees.
