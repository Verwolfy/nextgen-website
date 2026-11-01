/**
 * Cloudflare Pages Function — staged only, not enabled in production.
 * No personal information is processed until NEXTGEN_LEADS_ENABLED=true,
 * a reviewed consent notice, Turnstile and a private DB schema are configured.
 */
const MAX_BYTES = 8192;
const MAX_TEXT = 1500;
const MAX_FIELD = 160;
const accepted = new Set(['kind','business','contact','phone','email','wilaya','commune','product','package','quantity','message','activity','brands','consent','token','website']);
const privateFields = ['business','contact','phone','email','wilaya','commune','product','package','quantity','message','activity','brands'];

function reply(status, code) {
  return new Response(JSON.stringify({ ok: false, code }), {
    status, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store', 'x-content-type-options': 'nosniff' },
  });
}

async function readLimited(request) {
  if (!request.body) return null;
  const reader = request.body.getReader();
  const chunks = [];
  let size = 0;
  try {
    for (;;) {
      const { value, done } = await reader.read();
      if (done) break;
      size += value.length;
      if (size > MAX_BYTES) { await reader.cancel(); return null; }
      chunks.push(value);
    }
  } finally { reader.releaseLock(); }
  const buffer = new Uint8Array(size);
  let offset = 0;
  for (const chunk of chunks) { buffer.set(chunk, offset); offset += chunk.length; }
  return new TextDecoder('utf-8', { fatal: true }).decode(buffer);
}

function validate(input) {
  if (!input || typeof input !== 'object' || Array.isArray(input)) return null;
  if (Object.keys(input).some(k => !accepted.has(k))) return null;
  if (input.website !== undefined && input.website !== '') return null;
  if (!['quote', 'distributor'].includes(input.kind) || input.consent !== true) return null;
  if (typeof input.token !== 'string' || input.token.length < 8 || input.token.length > 2048) return null;
  const data = {};
  for (const key of privateFields) {
    const v = input[key] ?? '';
    if (typeof v !== 'string' || v.length > (key === 'message' ? MAX_TEXT : MAX_FIELD)) return null;
    data[key] = v.trim();
  }
  if (!data.business || !data.contact || !data.phone || !data.wilaya) return null;
  if (data.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) return null;
  if (!/^[+0-9(). \-]{7,28}$/.test(data.phone)) return null;
  if (input.kind === 'quote' && (data.activity || data.brands)) return null;
  if (input.kind === 'distributor' && (data.product || data.package || data.quantity)) return null;
  return { kind: input.kind, data, token: input.token };
}


/** Derive a stable, non-plaintext rate-limit key for a single contact. */
async function rateLimitKey(phone, secret) {
  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const signature = await crypto.subtle.sign('HMAC', key, enc.encode(phone.replace(/[^+0-9]/g, '')));
  return Array.from(new Uint8Array(signature), b => b.toString(16).padStart(2, '0')).join('');
}

export async function onRequestPost({ request, env }) {
  // Explicit server-side fail-closed gate, independent of the disabled UI.
  if (env?.NEXTGEN_LEADS_ENABLED !== 'true') return reply(503, 'LEADS_NOT_ACTIVE');
  if (!env.TURNSTILE_SECRET_KEY || !env.SUPABASE_SERVICE_ROLE_KEY || !env.SUPABASE_URL || !env.NEXTGEN_PRIVACY_NOTICE_VERSION || !env.NEXTGEN_EXPECTED_HOSTNAME || !env.NEXTGEN_TURNSTILE_ACTION) return reply(503, 'NOT_CONFIGURED');
  if (typeof env.NEXTGEN_SUPABASE_PROJECT_REF !== 'string' || !/^[a-z0-9]{20}$/.test(env.NEXTGEN_SUPABASE_PROJECT_REF)) return reply(503, 'PROJECT_NOT_CONFIGURED');
  // A Worker Rate Limiting binding is mandatory before any future activation.
  // No rate limiter, weak salt or error => never persist personal information.
  if (typeof env.NEXTGEN_RATE_LIMIT_SALT !== 'string' || env.NEXTGEN_RATE_LIMIT_SALT.length < 32 ||
      typeof env.NEXTGEN_RATE_LIMITER?.limit !== 'function') return reply(503, 'RATE_LIMIT_NOT_CONFIGURED');

  const requestURL = new URL(request.url);
  const origin = requestURL.origin;
  // Host binding ensures a preview or rogue hostname cannot reuse production secrets.
  if (requestURL.protocol !== 'https:' || requestURL.hostname !== env.NEXTGEN_EXPECTED_HOSTNAME) return reply(403, 'INVALID_HOST');
  if (request.headers.get('origin') !== origin) return reply(403, 'INVALID_ORIGIN');
  if (!/^application\/json(?:;|$)/i.test(request.headers.get('content-type') || '')) return reply(415, 'JSON_REQUIRED');
  const length = Number(request.headers.get('content-length') || 0);
  if (!Number.isFinite(length) || length > MAX_BYTES || length < 0) return reply(413, 'REQUEST_TOO_LARGE');
  let input;
  try { const body = await readLimited(request); input = body ? JSON.parse(body) : null; }
  catch { return reply(400, 'INVALID_JSON'); }
  const parsed = validate(input);
  if (!parsed) return reply(400, 'INVALID_REQUEST');

  let url;
  try { url = new URL(env.SUPABASE_URL); } catch { return reply(503, 'INVALID_STORAGE_CONFIG'); }
  if (url.protocol !== 'https:' || url.hostname !== `${env.NEXTGEN_SUPABASE_PROJECT_REF}.supabase.co` || url.username || url.password || url.port || url.pathname !== '/' || url.search || url.hash) return reply(503, 'INVALID_STORAGE_CONFIG');

  let verified;
  try {
    const response = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
      method: 'POST', headers: { 'content-type': 'application/x-www-form-urlencoded' },
      signal: AbortSignal.timeout(8000),
      body: new URLSearchParams({ secret: env.TURNSTILE_SECRET_KEY, response: parsed.token }),
    });
    if (!response.ok) return reply(503, 'VERIFICATION_UNAVAILABLE');
    verified = await response.json();
  } catch { return reply(503, 'VERIFICATION_UNAVAILABLE'); }
  // A token issued for another website must not authorize this site's API.
  if (verified?.success !== true || verified.hostname !== env.NEXTGEN_EXPECTED_HOSTNAME || verified.action !== env.NEXTGEN_TURNSTILE_ACTION) return reply(403, 'VERIFICATION_FAILED');

  // Rate limiting occurs only after Turnstile: challenge failures cannot spend quotas.
  // A keyed digest avoids sending a phone number in clear to the limiter.
  try {
    const key = await rateLimitKey(parsed.data.phone, env.NEXTGEN_RATE_LIMIT_SALT);
    const permitted = await env.NEXTGEN_RATE_LIMITER.limit({ key });
    if (permitted?.success !== true) return reply(429, 'RATE_LIMITED');
  } catch { return reply(503, 'RATE_LIMIT_UNAVAILABLE'); }

  const payload = {
    type_demande: parsed.kind,
    entreprise: parsed.data.business,
    nom_contact: parsed.data.contact,
    telephone: parsed.data.phone,
    email: parsed.data.email || null,
    wilaya: parsed.data.wilaya,
    commune: parsed.data.commune || null,
    produit: parsed.kind === 'quote' ? (parsed.data.product || null) : null,
    conditionnement: parsed.kind === 'quote' ? (parsed.data.package || null) : null,
    quantite: parsed.kind === 'quote' ? (parsed.data.quantity || null) : null,
    activite: parsed.kind === 'distributor' ? (parsed.data.activity || null) : null,
    marques_distribuees: parsed.kind === 'distributor' ? (parsed.data.brands || null) : null,
    message: parsed.data.message || null,
    consentement: true,
    consent_notice_version: env.NEXTGEN_PRIVACY_NOTICE_VERSION,
    source: 'nextgen_website',
  };
  try {
    const stored = await fetch(`${url.origin}/rest/v1/site_demandes`, {
      method: 'POST',
      signal: AbortSignal.timeout(8000),
      headers: { 'apikey': env.SUPABASE_SERVICE_ROLE_KEY, 'authorization': `Bearer ${env.SUPABASE_SERVICE_ROLE_KEY}`, 'content-type': 'application/json', 'prefer': 'return=minimal' },
      body: JSON.stringify(payload),
    });
    if (stored.status !== 201) return reply(503, 'PERSISTENCE_UNAVAILABLE');
  } catch { return reply(503, 'PERSISTENCE_UNAVAILABLE'); }
  // No email or auto-response is sent in this staged implementation.
  return new Response(JSON.stringify({ ok: true }), {status:201,headers:{'content-type':'application/json; charset=utf-8','cache-control':'no-store'}});
}
export const onRequestGet = () => reply(405, 'METHOD_NOT_ALLOWED');
