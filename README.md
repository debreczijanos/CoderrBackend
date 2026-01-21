# Coderr Backend

Lightweight Django REST API for a freelancer platform (Coderr).

## Overview

- Token-based auth (registration + login)
- Profiles for customer and business users
- Offers with 3-tier details (basic/standard/premium)
- Orders based on offer details
- Reviews for business users
- Aggregated base info stats for landing page

## Tech Stack

- Python 3.12+
- Django 5
- Django REST Framework
- TokenAuth
- SQLite (dev)
- CORS middleware

## Project Structure

- `src/config/` settings, URLs, WSGI/ASGI
- `src/apps/` domain apps (accounts, profiles, offers, offerdetails, orders, reviews)
- `src/apps/common/` shared utilities
- `src/manage.py`

## Installation

Prerequisites: Python 3.12+

Mac/Linux

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/manage.py migrate
python src/manage.py createsuperuser  # optional
python src/manage.py runserver
```

Windows (PowerShell)

```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/manage.py migrate
python src/manage.py createsuperuser  # optional
python src/manage.py runserver
```

## Lokales Testen mit Demo-Daten (empfohlen)

Dieses Projekt enthält vorbereitete Demo-Daten (User, Profile, Offers, Orders, Reviews),
damit das Backend nach dem Klonen sofort getestet werden kann.

### Schritte

```bash
python src/manage.py migrate
python src/manage.py loaddata fixtures/demo_data.json
python src/manage.py runserver
```

### Demo-Zugänge

- **andrey** / `asdasd`
- **kevin** / `asdasd24`

> Hinweis: Die Demo-Daten sind für lokale Tests gedacht.  
> In der Produktionsumgebung (z. B. mit MySQL) werden eigene Benutzer und Tokens verwendet.

API Base:

- `http://127.0.0.1:8000/api/`
- `http://127.0.0.1:8000/api/v1/`

## Auth

All protected endpoints require:

```
Authorization: Token <token>
```

## API Endpoints (short)

Auth

- `POST /api/registration/`
- `POST /api/login/`

Profiles

- `GET /api/profile/<id>/`
- `PATCH /api/profile/<id>/`
- `GET /api/profiles/business/`
- `GET /api/profiles/customer/`

Offers

- `GET /api/offers/` (filters: creator_id, min_price, max_delivery_time, search, ordering, page_size)
- `POST /api/offers/`
- `GET /api/offers/<id>/`
- `PATCH /api/offers/<id>/`
- `DELETE /api/offers/<id>/`

Offer Details

- `GET /api/offerdetails/<id>/`

Orders

- `GET /api/orders/`
- `POST /api/orders/`
- `PATCH /api/orders/<id>/`
- `DELETE /api/orders/<id>/` (staff only)
- `GET /api/order-count/<business_user_id>/`
- `GET /api/completed-order-count/<business_user_id>/`

Reviews

- `GET /api/reviews/?business_user_id=&reviewer_id=&ordering=`
- `POST /api/reviews/`
- `PATCH /api/reviews/<id>/`
- `DELETE /api/reviews/<id>/`

Base Info

- `GET /api/base-info/`

## CORS (dev)

Allowed origins are configured via `CORS_ALLOWED_ORIGINS` in `.env`.
Defaults include:

- `http://127.0.0.1:5500`
- `http://localhost:5500`
