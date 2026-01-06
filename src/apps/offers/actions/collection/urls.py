from django.urls import path

from .view import OffersCollectionView

urlpatterns = [
    path("", OffersCollectionView.as_view(), name="offers-collection"),
]
