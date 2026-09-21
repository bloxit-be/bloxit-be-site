# Blox-It website

Bilingual static company website for GitHub Pages. English is the default; Dutch browser language is detected on the English homepage. Explicit EN/NL links override detection. No cookies, analytics, accounts, comments, forms or external font requests.

## Build locally

Requires Python 3.10+ only. Run `python3 build.py`, then `python3 -m http.server 8000 --directory _site`.

## Publish

In repository Settings → Pages, choose **GitHub Actions** as the source. Pushes to `main` build and deploy via `.github/workflows/pages.yml`.

## Content

Edit English and Dutch content in `build.py`; presentation and small language enhancement are in `assets/`. The original Blox-It logo is preserved unchanged.

## Domain

The initial deployment uses the repository's GitHub Pages address. No DNS or existing bloxit.be WordPress changes have been made. Configure a custom domain in Pages only when ready to replace the existing site. The workflow derives canonical URLs and sitemap from the Pages URL.
