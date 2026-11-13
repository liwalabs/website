#!/usr/bin/env python3
"""Local entry point: runs the Flask app (static pages + contact form).

Production uses gunicorn (see Procfile / Dockerfile).
"""
import os

from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
