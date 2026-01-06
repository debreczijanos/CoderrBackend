from django.urls import path

from .view import OfferdetailsDetailView

urlpatterns = [
    path("<int:detail_id>/", OfferdetailsDetailView.as_view(), name="offerdetails-detail"),
]
