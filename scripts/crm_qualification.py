#!/usr/bin/env python3
"""NextGen B2B lead triage: read-only inventory and offline CRM proposal.

Never creates clients, interactions or edits site_demandes. No request-personal
information is printed by the default inventory command. Keep the service-role
key in server-only environment variables; never add it to a GitHub Actions log.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
import os
import re
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen

PUBLIC_COLUMNS = 'demande_id,type_demande,statut,cree_le'
ALLOWED_STATUS = {'nouveau', 'en_cours', 'clos'}
ALLOWED_KINDS = {'quote', 'distributor'}


def valid_server_url(value: str) -> str:
    if not isinstance(value, str):
        raise ValueError('SUPABASE_URL absent')
    parts = urlsplit(value)
    if (parts.scheme != 'https' or parts.username or parts.password or parts.port
            or parts.query or parts.fragment or parts.path not in ('', '/')
            or not re.fullmatch(r'[a-z0-9-]+\.supabase\.co', parts.hostname or '')):
        raise ValueError('SUPABASE_URL doit être un domaine projet Supabase en HTTPS')
    return f'https://{parts.hostname}'


def read_pending_summary(url: str, key: str, limit: int = 200) -> dict:
    """Read only unidentifying metadata using allowlisted PostgREST columns."""
    if not isinstance(key, str) or len(key) < 10:
        raise ValueError('SUPABASE_SERVICE_ROLE_KEY non configurée')
    origin = valid_server_url(url)
    if limit < 1 or limit > 200:
        raise ValueError('limit hors bornes')
    query = urlencode({'select': PUBLIC_COLUMNS, 'order': 'cree_le.desc', 'limit': limit})
    request = Request(f'{origin}/rest/v1/site_demandes?{query}', headers={
        'apikey': key,
        'Authorization': f'Bearer {key}',
        'Accept': 'application/json',
    }, method='GET')
    with urlopen(request, timeout=10) as response:
        if response.status != 200:
            raise RuntimeError('Accès privé refusé')
        body = response.read(128000)
        if response.read(1):
            raise ValueError('Réponse trop volumineuse')
    data = json.loads(body)
    if not isinstance(data, list) or len(data) > limit:
        raise ValueError('Réponse serveur inattendue')
    kinds, statuses = Counter(), Counter()
    for row in data:
        if not isinstance(row, dict) or set(row) != set(PUBLIC_COLUMNS.split(',')):
            raise ValueError('Champs non attendus dans la réponse')
        if row['type_demande'] not in ALLOWED_KINDS or row['statut'] not in ALLOWED_STATUS:
            raise ValueError('Valeur CRM non reconnue')
        kinds[row['type_demande']] += 1
        statuses[row['statut']] += 1
    return {
        'scanned': len(data),
        'limited_to': limit,
        'possibly_truncated': len(data) == limit,
        'by_type': dict(kinds),
        'by_status': dict(statuses),
        'mode': 'READ_ONLY',
    }


def propose_crm_draft(request: dict) -> dict:
    """Pure mapping; returns an *uncommitted* draft, never issues database writes.

    Must be executed only inside an authenticated ERP review screen. It should
    not be dumped to public logs, repositories or analytics (contains PII).
    """
    if not isinstance(request, dict) or request.get('statut') != 'nouveau':
        raise ValueError('Seule une demande nouvelle peut être proposée')
    kind = request.get('type_demande')
    if kind not in ALLOWED_KINDS:
        raise ValueError('Type de demande inconnu')
    if not all(isinstance(request.get(x), str) and request[x].strip()
               for x in ('demande_id', 'entreprise', 'nom_contact', 'telephone', 'wilaya')):
        raise ValueError('Informations essentielles manquantes')
    # IDs, deduplication and approval remain ERP responsibilities.
    client = {
        'nom': request['entreprise'].strip(),
        'nom_contact': request['nom_contact'].strip(),
        'mobile_contact': request['telephone'].strip(),
        'email_contact': (request.get('email') or '').strip() or None,
        'wilaya': request['wilaya'].strip(),
        'pays': 'Algérie',
    }
    interaction = {
        'type_action': 'Demande de devis web' if kind == 'quote' else 'Candidature distributeur web',
        'notes': f"Demande site NextGen {request['demande_id']} — à qualifier manuellement",
    }
    return {
        'source_request_id': request['demande_id'],
        'requires_human_approval': True,
        'not_committed': True,
        'candidate_client': client,
        'candidate_interaction': interaction,
    }


def main() -> None:
    cli = argparse.ArgumentParser(description='NextGen — consultation non nominative des demandes B2B')
    cli.add_argument('--limit', type=int, default=200, help='Maximum de lignes consultées (200 au maximum)')
    args = cli.parse_args()
    report = read_pending_summary(
        os.environ.get('SUPABASE_URL', ''),
        os.environ.get('SUPABASE_SERVICE_ROLE_KEY', ''),
        limit=args.limit,
    )
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
