# Lot 116 — Correctif final du poster de la vidéo d'accueil V4

Date : 2026-11-07. Dépôt `Verwolfy/nextgen-website`.

## État précédent
- PR #112 a installé directement via GitHub Actions le MP4 V4 optimisé (712241 octets, SHA256 `e7ac28368254aff457c57067c79adf2973584becbfc9e2375180e20301494a13`) et son poster WebP (26946 octets, SHA256 `7a4ba9144d9bde9844fb779b24eab728e408e11682c6ad5095be45756f3fd90b`).
- PR #113, fusionnée sur main `cc2f91f37ea301279bae8968622ba2cddefa0759`, retire les trois éléments : badge BTPH, pilule Découvrir FENEK, preuve/disclaimer sous boutons et active la nouvelle vidéo avec fallback si fichier absent, FR/AR/EN.
- Tous les tests PR #113 (build/sécurité, Chromium, Lighthouse) réussis.
- PR #114 concurrente fermée **sans fusion** pour ne pas réécrire le travail déjà fusionné.

## Compléments
- La vidéo V4 utilisait encore le poster ancien de la V3 pendant le chargement ; elle utilise désormais **le poster issu du nouveau film**, avec repli ancien si les nouveaux médias sont absents.
- `Layout.astro` précharge le bon poster uniquement sur les trois pages d'accueil FR/AR/EN.
- `scripts/check_browser_pages.py` attend le poster V4, y compris sans JavaScript, sur mobile et bureau.
- `src/styles/v3.css` supprime les CSS des éléments disparus et enlève la marge vide au-dessus du grand titre.
- Supprime `.github/workflows/install-welcome-v4.yml` et `scripts/install_welcome_v4.py` devenus inutiles après intégration binaire ; les fichiers .media-staging ont été supprimés automatiquement par le job d'installation.
- Tests de SHA256 des deux médias, d'intégrité des URL et de préservation du contenu existant.

## Invariants
- Titre, sous-titre, CTA Catalogue/Contact, fil d'actualités non cliquable, bouton pause et sens RTL arabe inchangés.
- 10 secondes, 1280×720 H.264 muet. Chargement lazy vidéo et contrôles Data Saver/reduced motion conservés.
- Noindex, Cloudflare Access, DNS, ERP/Supabase, formulaire et data conceptuelle non modifiés.
- Quota artifacts GitHub Actions saturé : PR #112 a rendu uniquement l'upload de rapports non critique ; tests restent strictement bloquants.

## Suivi
Confirmer CI post-fusion, puis commit déployé dans Cloudflare Pages. Pour une vérification visuelle réelle FR/AR/EN, une capture utilisateur reste utile si le domaine exige Cloudflare Access.
Les fichiers privés Google Drive utilisés comme relais (original et optimisé) doivent être supprimés après livraison ; ils n'ont pas été partagés publiquement.
