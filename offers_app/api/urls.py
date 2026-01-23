from django.urls import path

from . import views

urlpatterns = [
    path("offers/", views.offers_collection, name="offers-collection"),
    path("offers/<int:offer_id>/", views.offer_detail, name="offers-detail"),
]
