import { defineConfig } from 'astro/config';
export default defineConfig({
  site: 'https://www.nextgen-buildingsolutions.com',
  output: 'static',
  build: { inlineStylesheets: 'auto' }
});
