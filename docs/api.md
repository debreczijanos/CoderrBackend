# API

Base URL:
- http://127.0.0.1:8000/api/

## Auth
- POST /api/registration/
- POST /api/login/

## Profiles
- GET /api/profile/<id>/
- PATCH /api/profile/<id>/
- GET /api/profiles/business/
- GET /api/profiles/customer/

## Offers
- GET /api/offers/
- POST /api/offers/
- GET /api/offers/<id>/
- PATCH /api/offers/<id>/
- DELETE /api/offers/<id>/

## Offer details
- GET /api/offerdetails/<id>/

## Orders
- GET /api/orders/
- POST /api/orders/
- PATCH /api/orders/<id>/
- DELETE /api/orders/<id>/
- GET /api/order-count/<business_user_id>/
- GET /api/completed-order-count/<business_user_id>/

## Reviews
- GET /api/reviews/
- POST /api/reviews/
- PATCH /api/reviews/<id>/
- DELETE /api/reviews/<id>/

## Base info
- GET /api/base-info/
