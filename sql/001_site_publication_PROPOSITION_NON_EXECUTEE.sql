-- NEXTGEN / PROPOSITION - NE PAS EXECUTER SANS ACCORD EXPLICITE SUR LE SCHEMA PROD
-- Site en génération statique, aucun accès public à cette table ni à cette vue.
-- Aucun produit fictif de l'ERP courant ne peut être lié à la publication.
-- Valider la parité service_role, le déclencheur RLS existant et les droits avant exécution.
BEGIN;

CREATE TABLE public.site_produits (
    pf_id text PRIMARY KEY REFERENCES public.produits (pf_id) ON DELETE RESTRICT,
    slug text NOT NULL UNIQUE,
    gamme text NOT NULL CHECK (gamme IN ('bond', 'proof', 'flow', 'paint')),
    contenu jsonb NOT NULL DEFAULT '{}'::jsonb CHECK (jsonb_typeof(contenu) = 'object'),
    image_url text,
    modele_3d_url text,
    fiche_technique_url text,
    fds_url text,
    fiche_technique_validee boolean NOT NULL DEFAULT false,
    fds_validee boolean NOT NULL DEFAULT false,
    ordre integer NOT NULL DEFAULT 100,
    produit_reel_confirme boolean NOT NULL DEFAULT false,
    statut_technique text NOT NULL DEFAULT 'brouillon'
        CHECK (statut_technique IN ('brouillon', 'valide', 'refuse')),
    statut_commercial text NOT NULL DEFAULT 'brouillon'
        CHECK (statut_commercial IN ('brouillon', 'valide', 'refuse')),
    valide_technique_le timestamptz,
    valide_commercial_le timestamptz,
    publie boolean NOT NULL DEFAULT false,
    maj_le timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT site_slug_format CHECK (slug ~ '^[a-z0-9]+(-[a-z0-9]+)*$'),
    CONSTRAINT site_exclure_produits_test_20261031
        CHECK (pf_id NOT IN ('PF-001','PF-002','PF-003','PF-004','PF-005','PF-006')),
    CONSTRAINT site_publication_verrou
        CHECK (NOT publie OR (
            produit_reel_confirme
            AND statut_technique = 'valide'
            AND statut_commercial = 'valide'
            AND valide_technique_le IS NOT NULL
            AND valide_commercial_le IS NOT NULL
        )),
    CONSTRAINT site_doc_ft_interdit_sans_validation
        CHECK (fiche_technique_validee OR fiche_technique_url IS NULL OR NOT publie),
    CONSTRAINT site_doc_fds_interdit_sans_validation
        CHECK (fds_validee OR fds_url IS NULL OR NOT publie)
);

ALTER TABLE public.site_produits ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE public.site_produits FROM PUBLIC, anon, authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.site_produits TO service_role;

-- INVOKER : exige les autorisations de l'appelant sur toutes les tables concernées.
CREATE VIEW public.site_products WITH (security_invoker = true) AS
SELECT s.slug, p.nom, s.gamme, s.contenu, s.image_url, s.modele_3d_url,
       CASE WHEN s.fiche_technique_validee THEN s.fiche_technique_url ELSE NULL END AS fiche_technique_url,
       CASE WHEN s.fds_validee THEN s.fds_url ELSE NULL END AS fds_url,
       s.ordre, s.produit_reel_confirme, s.statut_technique, s.statut_commercial,
       COALESCE((SELECT json_agg(json_build_object(
           'format', k.format, 'poids_net', k.poids_net, 'unite', k.unite_vente)
            ORDER BY k.format)
          FROM public.sku_conditionnement k
          WHERE k.pf_id = p.pf_id
            AND UPPER(BTRIM(COALESCE(k.actif, ''))) = 'OUI'
        ), '[]'::json) AS conditionnements
FROM public.site_produits s
JOIN public.produits p ON p.pf_id = s.pf_id
WHERE s.publie IS TRUE
  AND s.produit_reel_confirme IS TRUE
  AND s.statut_technique = 'valide'
  AND s.statut_commercial = 'valide'
  AND s.valide_technique_le IS NOT NULL
  AND s.valide_commercial_le IS NOT NULL
  AND UPPER(BTRIM(COALESCE(p.actif, ''))) = 'OUI';

REVOKE ALL ON TABLE public.site_products FROM PUBLIC, anon, authenticated;
GRANT SELECT ON TABLE public.site_products TO service_role;
COMMENT ON VIEW public.site_products IS 'Export prive pour generation statique ; aucune permission anon';

COMMIT;
-- En cas de rollback futur : ne jamais DROP sans validation particulière.
