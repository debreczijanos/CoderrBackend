from django.urls import path

from . import views

urlpatterns = [
    path("offerdetails/<int:detail_id>/", views.offer_detail, name="offerdetails-detail"),
]
