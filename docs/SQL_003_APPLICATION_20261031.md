# NextGen — SQL 003 : application Supabase PROD

Date : 31 octobre 2026.

Autorisation exacte : **SQL 003 VALIDÉ**.

Source GitHub : `sql/003_site_demandes_PROPOSITION_NON_EXECUTEE.sql` (document historique).

Projet : `wenydirqtmkywbxbxfal` ; migration Supabase enregistrée : `20261031220121_nextgen_site_demandes_private_20261031`.

Réponse d'exécution : `success=true`.

État vérifié : `public.site_demandes` créée (20 colonnes), index `site_demandes_statut_cree_idx` créé, 0 ligne, RLS actif, aucune politique RLS pour `anon` ou `authenticated`. SELECT/INSERT/UPDATE/DELETE interdits à ces deux rôles ; `service_role` peut SELECT/INSERT/UPDATE.

**Écart de privilèges par défaut** : `service_role` conserve DELETE, TRUNCATE et d'autres privilèges via ACL initiales ; aucune correction supplémentaire de GRANT ou RLS n'a été appliquée. Préparer une revue de moindre privilège avant activation des formulaires.

Schéma : 90/90 tables `public` avec RLS ; 0 table `public` lisible par `anon` directement. 86 avis INFO Supabase sur les tables à RLS sans politique (pas de WARN/ERROR).

Le site public, les formulaires et les emails restent **désactivés**. La notice de confidentialité, la durée de conservation, la base légale, l'anti-bot et les tests REST avec les vrais secrets doivent être validés avant activation. La base TEST n'a pas été touchée.
