# Coderr Backend

Django + DRF skeleton for a freelancer platform.

## Structure

- `src/config`: project settings and URLs
- `src/apps`: domain apps
- `src/apps/common`: shared utilities and base classes

## Quick start

1. Create a virtualenv and install requirements:
   - `python -m venv .venv`
   - `source .venv/bin/activate`
   - `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and adjust values.
3. Run migrations:
   - `python src/manage.py migrate`
4. Run the server:
   - `python src/manage.py runserver`

## API

- Health check: `GET /api/v1/health/`
