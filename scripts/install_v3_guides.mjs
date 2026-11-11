/**
 * Lot 128 — fail-closed release of 45 independently audited V3 guide sprites.
 * Each archive is validated, every product basename is allow-listed by its
 * unique catalogue slug, and each resulting WebP is checked by SHA-256.
 * Does not publish any private PDF, FDS, Supabase content or numerical claims.
 */
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {resolve} from 'node:path';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const root=process.cwd();
const entries=JSON.parse(readFileSync(resolve(root,'src/data/fenek-v3-verified-45.json'),'utf8'));
const expected=new Map();
for(const p of entries){
 if(!/^fenek-(bond|proof|flow|paint)-[a-z0-9-]+$/.test(p.slug)
    || p.code!==p.slug.slice(6).toUpperCase()
    || !/^[a-f0-9]{64}$/.test(p.sha256)
    || p.status!=='BROUILLON'
    || p.steps.length!==6
    || expected.has(p.slug+'-steps.webp'))throw Error('Invalid V3 product manifest '+p.slug);
 expected.set(p.slug+'-steps.webp',p);
}
if(expected.size!==45)throw Error('Lot 128 requires 45 unique V3 products');
const archives=[
 ['fenek-v3-bond-11.tar.gz','a08f82b9d54f1dedd3250811bf1c7f4ac7de5eebb33de991a7d2ca6f91ae1ce0'],
 ['fenek-v3-proof-11.tar.gz','eeee3a447f50c4bf2d9b43e5b2e4dd4bd7d3dfe5874559562ffcd807ee7acc62'],
 ['fenek-v3-flow-12.tar.gz','7611f1b8a5b071e881d33aa2ef1664ef207805d52456ee1d32b2191ee6bec5f6'],
 ['fenek-v3-paint-11.tar.gz','39696b97c02086c5c2262ddd4ceb4086c7886271d9bd1fbbd7a9c97c81ce3a57']
];
const sha=data=>createHash('sha256').update(data).digest('hex');
const seen=new Set(),dest=resolve(root,'public/images/application-v3');
mkdirSync(dest,{recursive:true});
for(const [archive,digest] of archives){
 const input=readFileSync(resolve(root,'src/assets',archive));
 if(sha(input)!==digest)throw Error('Corrupt V3 archive '+archive);
 const tar=gunzipSync(input);
 let pos=0,number=0;
 while(pos+512<=tar.length){
   const header=tar.subarray(pos,pos+512);
   const name=header.subarray(0,100).toString('utf8').split('\0')[0];
   if(!name)break;
   const sizeText=header.subarray(124,136).toString('ascii').replace(/\0/g,'').trim();
   const size=parseInt(sizeText,8);
   const type=header[156];
   if(!Number.isSafeInteger(size)||size<=0||size>2_000_000||(type!==0 && type!==48))
      throw Error('Unsafe V3 archive entry '+name);
   if(!/^[a-z0-9-]+-steps\.webp$/.test(name)||!expected.has(name)||seen.has(name))
      throw Error('Unapproved V3 product file '+name);
   const start=pos+512,end=start+size;
   if(end>tar.length)throw Error('Truncated V3 '+name);
   const bytes=tar.subarray(start,end);
   const item=expected.get(name);
   if(sha(bytes)!==item.sha256
      ||bytes.subarray(0,4).toString('ascii')!=='RIFF'
      ||bytes.subarray(8,12).toString('ascii')!=='WEBP')
      throw Error('V3 image mismatch for '+item.code);
   writeFileSync(resolve(dest,name),bytes);
   seen.add(name);number++;
   pos=start+Math.ceil(size/512)*512;
 }
 console.log('PASS '+archive+': '+number+' reference-specific V3 sprites');
}
if(seen.size!==expected.size)throw Error('Missing V3 product images: '+[...expected.keys()].filter(k=>!seen.has(k)).join(','));
console.log('PASS: 45 independently matched V3 sprites; C1T/C1TE and three tile guide sprites are preserved');
