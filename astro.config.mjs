import { defineConfig } from 'astro/config';
export default defineConfig({
  site: 'https://nextgen-buildingsolutions.com',
  output: 'static',
  build: { inlineStylesheets: 'auto' }
});
