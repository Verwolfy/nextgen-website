# Lot 90 — Vérification de la refonte V3 sur le domaine public

Date : 2026-11-05, repo `Verwolfy/nextgen-website`.

## Besoin
Confirmer sur `https://nextgen-buildingsolutions.com` que l'accueil V3, les trois langues et la véritable vidéo Nexo/Geno sont effectivement servis. La réussite des CI GitHub ne constitue pas en elle-même une preuve de publication Cloudflare.

## Action
- `scripts/check_live_v3_motion_readonly.py` vérifie en lecture seule les pages `/fr/`, `/ar/` et `/en/`, leurs deux titres V3 par langue, le statut provisoire, 3 cartes FENEK, `noindex,nofollow`, et l'identification de la vidéo Nexo/Geno.
- Lorsque les trois pages sont cohérentes, contrôle HTTP + SHA-256 de la vidéo MP4 et du poster WebP réels face aux fichiers de `public/videos/`.
- Utilise le même client HTTP restreint que le contrôle du lot 80 ; aucune authentification, aucun token ni appel API Cloudflare.
- 4 lectures max, espacées de 30 s, pour absorber un déploiement Cloudflare automatique légèrement décalé.
- Rapports GitHub Actions : résumé et fichier JSON privé pendant 7 jours.
- Workflow `.github/workflows/live-v3-motion-readonly.yml` déclenché par modification de l'accueil/script/workflow sur `main`, ou manuellement ; jamais de déploiement par ce job.

## Limitations
- Ce diagnostic prouve la présence du **contenu V3 et des fichiers médias exacts**, mais **pas le commit SHA précis** exécuté sur Cloudflare.
- En cas d'échec, cela signifie « non confirmé depuis le runner », non nécessairement une panne publique.
- Ne pas changer DNS, Access, `noindex`, `robots.txt`, cache, ERP, Supabase, formulaires ni dossiers techniques.
- Les 50 fiches restent des présentations provisoires.

## État code et suite
- PR #88 : accueil V3/animation fusionné à `main` ; tests réussis.
- PR #89 : catalogue/gammes/fiches V3 fusionné ; tests réussis.
- PR #90 : pages institutionnelles/B2B V3 fusionné ; tests PR réussis.
- Lot suivant : audit performance réel sur plusieurs appareils et rationnalisation des CSS/visuels, sans inventer des métriques LCP/CLS.
