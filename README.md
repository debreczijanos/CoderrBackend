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
- Django REST Framework Token Authentication
- SQLite (development)
- CORS middleware

## Project Structure

- `core/` settings.py, URLs, WSGI/ASGI
- App folders are at the project root (accounts_app, profiles_app, offers_app, offerdetails_app, orders_app, reviews_app, base_info_app)
- `manage.py`

## Installation (Local Development)

Prerequisites: Python 3.12+

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
```

### Windows (PowerShell)

```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
```

## Local Testing with Demo Data (Recommended)

This project includes prepared demo data (users, profiles, offers, orders, reviews)
so the backend can be tested immediately after cloning.

### Steps

```bash
python manage.py migrate
python manage.py loaddata fixtures/demo_data.json
python manage.py runserver
```

### Demo Accounts

- **andrey** / `asdasd`
- **kevin** / `asdasd24`

> Note: Demo data is intended for local testing only.
> In production environments (e.g. MySQL), separate users and tokens are used.

API Base URLs:

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

## CORS (Development)

Allowed origins are configured via `CORS_ALLOWED_ORIGINS` in `.env`.
Defaults include:

- `http://127.0.0.1:5500`
- `http://localhost:5500`
