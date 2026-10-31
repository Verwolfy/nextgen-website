import { copyFileSync, mkdirSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { resolve, dirname } from 'node:path';
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const files = ['Logo1.jpg','Nexo.webp','Nexo-Geno.webp'];
mkdirSync(resolve(root, 'public/images'), { recursive: true });
for (const file of files) copyFileSync(resolve(root, 'supports/assets', file), resolve(root, 'public/images', file));
console.log('Site brand assets copied from verified original sources.');

// Approved design-preview artifacts only. These are NOT catalogue products.
const demos = resolve(root, 'supports/3d/glb');
const pictures = resolve(root, 'supports/3d/previews');
const targetGlb = resolve(root, 'public/models-demo');
const targetImages = resolve(root, 'public/images/3d-demo');
mkdirSync(targetGlb, { recursive: true });
mkdirSync(targetImages, { recursive: true });
for (const name of readdirSync(demos).filter(v=>/^[a-z0-9-]+\.glb$/.test(v))) {
  copyFileSync(resolve(demos,name), resolve(targetGlb,name));
}
for (const name of readdirSync(pictures).filter(v=>/^[a-z0-9-]+\.webp$/.test(v))) {
  copyFileSync(resolve(pictures,name), resolve(targetImages,name));
}
console.log('Five non-contractual 3D packaging concepts copied for preview.');
