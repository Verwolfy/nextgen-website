/**
 * Install user-supplied tile application illustrations from a lossless
 * repository-safe base64 WebP archive before Astro copies public/ to dist/.
 * Fails closed on wrong payload rather than rendering a broken illustration.
 */
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { createHash } from 'node:crypto';
const b64=(await readFile('src/assets/tile-application-6.webp.base64','utf8')).trim();
if (!/^[A-Za-z0-9+/]+={0,2}$/.test(b64)) throw Error('Invalid image archive encoding');
const bytes=Buffer.from(b64,'base64');
const sha=createHash('sha256').update(bytes).digest('hex');
const expected='55197582655ba03f9de8d933047236e63efbd5df27a1acde136c5fc342059b1c';
if (bytes.length!==5902||sha!==expected||bytes.toString('ascii',0,4)!=='RIFF'||
    bytes.toString('ascii',8,12)!=='WEBP')
  throw Error('FENEK application illustrations corrupt or mismatched');
await mkdir('public/images/application',{recursive:true});
await writeFile('public/images/application/tile-application-6.webp',bytes);
console.log('PASS: six user-supplied application illustrations verified; WebP',bytes.length,'bytes');
