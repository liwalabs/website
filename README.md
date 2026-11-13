# Liwa Labs website

The company site for Liwa Labs: Mulazim AI, Mulazim Studio and Assembly OS.

A single static page (`index.html`, inline CSS and JS, no build step) plus a
small Flask app (`app.py`) that serves it and sends the contact form by email.

```
index.html        the site
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

- Colours: ink `#0d1520`, blue `#0a71d4`, white. Dark mode is supported.
- Type (self-hosted in `assets/fonts/`, no Google requests): Archivo (headings), IBM Plex Sans (body), IBM Plex Mono (labels),
  Noto Nastaliq Urdu / Noto Naskh Arabic for Urdu and Sindhi.
- Logo source: `assets/brand/liwa-logo-source.jpg`.
