# CodeAlpha Task 1: Simple URL Shortener

A small Flask + SQLite service that turns long URLs into short codes and redirects visitors to the original link. Includes a minimal web page for shortening links in the browser.

## Features

- `POST /api/shorten` creates a short code (random 6 characters, or a custom one)
- `GET /<code>` redirects (302) to the original URL and counts the click
- `GET /api/urls/<code>` returns the original URL, creation time and click count
- Same URL shortened twice returns the same code
- URL validation (http/https only, max 2048 characters)
- Simple frontend at `/`
- pytest suite

## Project structure

```
CodeAlpha-Task-1/
├── main.py            # entry point
├── config.py          # settings (env-overridable)
├── requirements.txt
├── src/
│   ├── __init__.py    # app factory
│   ├── database.py    # SQLite helpers
│   ├── routes.py      # API + redirect
│   ├── utils.py       # code generation and validation
│   └── templates/index.html
├── tests/test_app.py
└── screenshots/
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Open http://127.0.0.1:5000

## API

```bash
# Shorten
curl -X POST http://127.0.0.1:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/some/long/path"}'
# {"original_url": "...", "short_code": "aB3xYz", "short_url": "http://127.0.0.1:5000/aB3xYz"}

# Optional custom code
-d '{"url": "https://example.com", "custom_code": "my-link"}'

# Follow
curl -i http://127.0.0.1:5000/aB3xYz

# Stats
curl http://127.0.0.1:5000/api/urls/aB3xYz
```

| Status | Meaning |
|--------|---------|
| 201 | New short link created |
| 200 | URL already shortened, existing code returned |
| 400 | Invalid URL or custom code |
| 404 | Unknown short code |
| 409 | Custom code already taken |

## Configuration

Set via environment variables: `DATABASE`, `SHORT_CODE_LENGTH`, `HOST`, `PORT`, `FLASK_DEBUG`.

## Tests

```bash
pytest
```

## Screenshot

Add a screenshot of the running app as `screenshots/project-preview.png`.

---
Built for the CodeAlpha Backend Development internship.
