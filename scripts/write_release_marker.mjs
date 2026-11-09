/**
 * Lot 120: public, non-sensitive deployment identifier for Cloudflare Pages.
 * CF_PAGES_COMMIT_SHA is provided by Cloudflare's build environment.
 * This does NOT query Supabase, write secrets, or change routing.
 */
import { writeFile } from 'node:fs/promises';
import { join } from 'node:path';

const raw = process.env.CF_PAGES_COMMIT_SHA || process.env.GITHUB_SHA || '';
if (!raw) {
  console.log('NextGen release marker skipped: no CI commit SHA available.');
  process.exit(0);
}
if (!/^[a-f0-9]{40}$/i.test(raw)) {
  throw new Error('Invalid build commit SHA; refusing to write release marker');
}
const branch = process.env.CF_PAGES_BRANCH || process.env.GITHUB_REF_NAME || 'unknown';
if (!/^[a-zA-Z0-9._/-]{1,120}$/.test(branch)) {
  throw new Error('Invalid build branch identifier');
}
const marker = {
  application: 'nextgen-website',
  commit: raw.toLowerCase(),
  branch,
};
await writeFile(join('dist', 'deployment.json'), JSON.stringify(marker) + '\n', { flag: 'w', mode: 0o644 });
console.log('NextGen public deployment marker:', marker.branch, marker.commit.slice(0, 10));
