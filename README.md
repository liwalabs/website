# Liwa Labs website

The company site for Liwa Labs: AI, fintech and Web3 products and services, with the Mulazim platform (Mulazim AI, Mulazim Studio) as the flagship.

Static pages plus a small Flask app (`app.py`) that serves them and sends the
contact form by email.

```
index.html        the home page
projects.html     every project in brief (generated)
projects/*.html   one page per project: intro video, then the details (generated)
tools/build_site.py  the project content and the generator for the pages above
assets/site.css, assets/site.js  shared styles and behaviour
assets/           logo marks (light/dark), favicon, team photos, brand source
app.py            Flask: serves index.html + assets/, POST /submit-contact
about.html …      redirects from the old multi-page URLs to the new sections
```

## Run locally

```bash
pip install flask flask-mail python-dotenv gunicorn
python main.py            # http://localhost:5000
```

Opening `index.html` directly also works; only the contact form needs the app.

## Projects

Project content lives in `tools/build_site.py`. Edit it, then run
`python3 tools/build_site.py` to regenerate `projects.html` and `projects/*.html`.

Intro videos: put the file at `assets/video/<slug>.mp4` (optionally a poster
image at `assets/video/<slug>.jpg`) and run the script again. Until a video is
there, the page shows an "Intro video coming soon" panel in its place.

## Contact form email

Set these in `.env` (never commit it):

| Var | Example |
|---|---|
| `SMTP_HOST` | `smtp.gmail.com` |
| `SMTP_PORT` | `587` |
| `SMTP_USER` | the sending mailbox |
| `SMTP_PASS` | an app password for that mailbox |
| `RECIPIENT_EMAIL` | where enquiries arrive, e.g. `info@liwalabs.com` |

If sending fails, the page tells the visitor to write to info@liwalabs.com.

## Deploy

`Dockerfile` and `Procfile` both run `gunicorn app:app` on `$PORT` (default 5000).
The app serves only `index.html`, the redirect pages and `assets/`; source files
and `.env` are never served.

## Brand

- Colours: white background, ink `#0d1520`, blue `#0866c0`. Light theme only, by design.
- Type (self-hosted in `assets/fonts/`, no Google requests): Archivo (headings), IBM Plex Sans (body), IBM Plex Mono (labels),
  Noto Nastaliq Urdu / Noto Naskh Arabic for Urdu and Sindhi.
- Logo source: `assets/brand/liwa-logo-source.jpg`.
