// Saturday Slate — build the shareable standalone page from the artifact fragment.
// Usage (from repo root):  node saturday-slate/build.mjs
// Reads  saturday-slate/fragment.html  (the artifact fragment: <title>, fonts, <style>, markup, <script>)
// Writes saturday-slate.html           (repo root: a full standalone HTML document)
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const FRAG = join(here, 'fragment.html');
const SITE = join(here, '..', 'saturday-slate.html');

const f = readFileSync(FRAG, 'utf8');
const marker = '</style>';
const idx = f.indexOf(marker);
if (idx === -1) { console.error('ERROR: no </style> found in fragment.html'); process.exit(1); }
const head = f.slice(0, idx + marker.length);
const body = f.slice(idx + marker.length);

const favicon = 'data:image/svg+xml,' + encodeURIComponent(
  '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#152238"/>' +
  '<path d="M6 16c0-5 4-9 10-9s10 4 10 9-4 9-10 9S6 21 6 16Z" fill="none" stroke="#E7B44E" stroke-width="2"/>' +
  '<path d="M12 12l8 8M20 12l-8 8" stroke="#E7B44E" stroke-width="1.6"/></svg>');

const reset = `<style>
  :root{color-scheme:light dark; padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px)}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:#faf9f7}
  img{max-width:100%}
  [hidden]{display:none!important}
</style>`;

const out = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="A weekly, shareable football guide — College, NFL and Iowa high school.">
<meta name="theme-color" content="#152238">
<link rel="icon" href="${favicon}">
${reset}
${head}
</head>
<body>
${body}
</body>
</html>`;

writeFileSync(SITE, out);
console.log('Built', SITE, `(${out.length} bytes)`);
