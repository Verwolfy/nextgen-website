# Lot 6 — Conditions de préproduction (2026-11-01)

**Statut actuel : NO-GO collecte publique.** Aucun formulaire, email, synchronisation ou DNS activé.

## Livré et vérifié
- ERP : PR #31 puis PR #32 fusionnées ; onglet Demandes NextGen désactivé tant que les deux secrets booléens crm_inbox_read_enabled et privacy_review_approved ne valent pas strictement true.
- Site Cloudflare Pages : NEXTGEN_LEADS_ENABLED absent/faux => HTTP 503 sans collecte.
- Rate-limiter obligatoire : NEXTGEN_RATE_LIMITER et NEXTGEN_RATE_LIMIT_SALT (32+ caractères). Clé HMAC-SHA256 du téléphone normalisé ; échec/absence => HTTP 503, limitation => HTTP 429, avant tout INSERT.
- URL Supabase : variable NEXTGEN_SUPABASE_PROJECT_REF requise, URL HTTPS racine identique à ce projet. Un autre domaine/projet est refusé avant requête externe.
- Base Supabase PRODUCTION : site_demandes privée et RLS actif ; aucune écriture réalisée dans ce lot.
- Streamlit : URL https://nextgent-erp.streamlit.app/ ; observation HTTP anonyme depuis GitHub CI : 303. Cela ne démontre ni déploiement GitHub ni session ERP fonctionnelle.

## Conditions bloquantes avant GO
1. Revue juridique du traitement de demandes : base, finalités, registre, responsable, sous-traitants, droits, notice FR/AR/EN et durée de conservation. Ne pas inventer de délai.
2. Étudier les transferts potentiels de données vers les services Supabase et Cloudflare ; obtenir validation conforme au droit algérien.
3. Vérifier la configuration effective du binding rate-limiter Cloudflare et du WAF, avec tests en préproduction protégée et sans données réelles.
4. Autoriser séparément toute réduction ACL SQL (service_role a encore DELETE/TRUNCATE hérités). Aucun SQL nouveau réalisé.
5. Vérifier dans le tableau Streamlit Cloud l'application, le dépôt, main, app.py et les journaux, puis l'onglet après authentification.
6. Obtenir l'autorisation spécifique de déploiement Cloudflare et de changement DNS avant site public.

## Références de travail
- Portail du droit algérien (loi 18-07 modifiée 25-11) : https://droit.mjustice.gov.dz/fr/content/codes-0
- Journal officiel 25-11 : https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025048.pdf
- Cloudflare Rate Limiting : https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/
- Turnstile Siteverify : https://developers.cloudflare.com/turnstile/get-started/server-side-validation/

**Ces éléments sont des références de revue, non une certification de conformité.**
