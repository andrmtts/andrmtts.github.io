# personal-website

https://andrmtts.github.io/personal-website/

André de Mattos — personal CV / portfolio site. A single-page, plain-text-first site
built with plain HTML, CSS and JavaScript (no build step, no dependencies).

## Structure

```
index.html          Page content and structure
css/style.css        Design system (colors, type, layout)
js/main.js           Mobile menu, nav scroll-spy, footer year
assets/favicon.svg   Favicon
assets/fonts/        Self-hosted Source Serif 4 (OFL-licensed) used by both the site and the CV PDF
assets/CV_AndreDeMattos.pdf   Downloadable résumé, styled to match the site
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
- The downloadable CV PDF is generated from `scripts/build_resume.py` (reportlab), using the
  same self-hosted Source Serif 4 font and palette as the site. After editing the CV content,
  update the data in that script and re-run it:
  ```
  python3 scripts/build_resume.py
  ```
  This writes `CV_AndreDeMattos.pdf` in the current directory — move it into `assets/`.
