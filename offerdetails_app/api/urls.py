from django.urls import path

from .views import OfferDetailView

urlpatterns = [
    path("offerdetails/<int:detail_id>/", OfferDetailView.as_view(), name="offerdetails-detail"),
]
