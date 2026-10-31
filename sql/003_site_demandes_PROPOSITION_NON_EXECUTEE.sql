-- PROPOSITION NON EXÉCUTÉE : validation explicite nécessaire pour PROD.
-- Données personnelles B2B. Ne pas appliquer sans notice de confidentialité
-- approuvée, registre des traitements et définition de la durée de conservation.
-- Le endpoint /api/lead est toujours désactivé par défaut.
BEGIN;
CREATE TABLE public.site_demandes (
    demande_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    type_demande text NOT NULL CHECK (type_demande IN ('quote','distributor')),
    entreprise text NOT NULL CHECK (length(entreprise) BETWEEN 1 AND 160),
    nom_contact text NOT NULL CHECK (length(nom_contact) BETWEEN 1 AND 160),
    telephone text NOT NULL CHECK (length(telephone) BETWEEN 7 AND 28),
    email text CHECK (email IS NULL OR length(email) <= 160),
    wilaya text NOT NULL CHECK (length(wilaya) BETWEEN 1 AND 160),
    commune text CHECK (commune IS NULL OR length(commune) <= 160),
    produit text CHECK (produit IS NULL OR length(produit) <= 160),
    conditionnement text CHECK (conditionnement IS NULL OR length(conditionnement) <= 160),
    quantite text CHECK (quantite IS NULL OR length(quantite) <= 160),
    activite text CHECK (activite IS NULL OR length(activite) <= 160),
    marques_distribuees text CHECK (marques_distribuees IS NULL OR length(marques_distribuees) <= 160),
    message text CHECK (message IS NULL OR length(message) <= 1500),
    consentement boolean NOT NULL CHECK (consentement IS TRUE),
    consent_notice_version text NOT NULL CHECK (length(consent_notice_version) BETWEEN 1 AND 128),
    consentement_le timestamptz NOT NULL DEFAULT now(),
    cree_le timestamptz NOT NULL DEFAULT now(),
    statut text NOT NULL DEFAULT 'nouveau' CHECK (statut IN ('nouveau','en_cours','clos')),
    source text NOT NULL DEFAULT 'nextgen_website' CHECK (source = 'nextgen_website'),
    CONSTRAINT site_demandes_form_kind CHECK (
      (type_demande='quote' AND activite IS NULL AND marques_distribuees IS NULL)
      OR (type_demande='distributor' AND produit IS NULL AND conditionnement IS NULL AND quantite IS NULL)
    )
);
ALTER TABLE public.site_demandes ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON public.site_demandes FROM PUBLIC, anon, authenticated;
GRANT SELECT, INSERT, UPDATE ON public.site_demandes TO service_role;
CREATE INDEX site_demandes_statut_cree_idx ON public.site_demandes(statut,cree_le DESC);
COMMENT ON TABLE public.site_demandes IS 'Demandes web privées — aucun accès public. Politique de conservation et accès opérateur à approuver avant activation.';
COMMIT;
