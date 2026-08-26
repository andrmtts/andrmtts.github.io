# personal-website

André de Mattos — personal CV / portfolio site. A single-page, plain-text-first site
built with plain HTML, CSS and JavaScript (no build step, no dependencies).

## Structure

```
index.html          Page content and structure
css/style.css        Design system (colors, type, layout)
js/main.js           Mobile menu, nav scroll-spy, footer year
assets/favicon.svg   Favicon
assets/fonts/        Self-hosted Source Serif 4 (OFL-licensed) used by both the site and the CV PDF
assets/CV_AndreDeMattos.pdf   Downloadable résumé — André's own CV file, supplied directly
scripts/build_resume.py       Unused for now: generates a site-styled PDF from reportlab (see below)
```

## Running locally

No build tools required — just serve the folder statically, e.g.:

```
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Deploying

Static site — deploy as-is to GitHub Pages, Netlify, Vercel, or any static host.
For GitHub Pages: Settings → Pages → Deploy from branch → `main` / root.

## Updating content

- CV content lives directly in `index.html` (About, Experience, Skills, Education, Contact).
- `assets/CV_AndreDeMattos.pdf` is André's own CV file (his own template/formatting) — replace it
  directly with a new export whenever he updates it. **Do not run `scripts/build_resume.py`** to
  regenerate this file — that script produces a differently-styled PDF (matching the site's own
  design) that André decided not to use in favor of his own CV format; running it would overwrite
  the file with that other version. The script is kept only as a fallback in case a site-styled
  PDF is wanted again in the future.
