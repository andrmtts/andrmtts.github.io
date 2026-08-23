# personal-website

André de Mattos — personal CV / portfolio site. A single-page, editorial-style site
built with plain HTML, CSS and JavaScript (no build step, no dependencies).

## Structure

```
index.html        Page content and structure
css/style.css     Design system (colors, type, layout, animations)
js/main.js        Nav scroll-spy, reveal-on-scroll, animated stats, mobile menu
assets/           Favicon and downloadable résumé (CV_AndreDeMattos.pdf)
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

- CV content lives directly in `index.html` (Experience, Skills, Education, Contact).
- To regenerate the downloadable résumé PDF after content changes, rebuild it from
  the CV source and drop it in `assets/CV_AndreDeMattos.pdf`.
