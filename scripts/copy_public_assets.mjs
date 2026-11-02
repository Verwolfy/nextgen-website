import { copyFileSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { resolve, dirname } from 'node:path';
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const files = ['Logo1.jpg','Nexo.webp','Nexo-Geno.webp'];
mkdirSync(resolve(root, 'public/images'), { recursive: true });
for (const file of files) copyFileSync(resolve(root, 'supports/assets', file), resolve(root, 'public/images', file));
