import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

// News-image entry for make.fun, competition news-image-20261119:
// "Sum up 19 November's world news in one image".
//
// The image is a newspaper-style infographic drawn at build time by
// generate_image.py (Pillow, DejaVu Sans, every letter drawn with a
// real font) and shipped as entry.png beside this file; the program
// only copies it to the output directory, so it runs with no network
// and writes identical bytes on every run.
//
// Run it locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(
  new URL('./entry.png', import.meta.url),
  join(outDir, 'entry.png'),
);
