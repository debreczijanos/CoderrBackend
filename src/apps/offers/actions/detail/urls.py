from django.urls import path

from .view import OffersDetailView

urlpatterns = [
    path("<int:offer_id>/", OffersDetailView.as_view(), name="offers-detail"),
]
