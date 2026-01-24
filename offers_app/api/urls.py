from django.urls import path

from .views import OfferDetailView, OffersCollectionView

urlpatterns = [
    path("offers/", OffersCollectionView.as_view(), name="offers-collection"),
    path("offers/<int:offer_id>/", OfferDetailView.as_view(), name="offers-detail"),
]
