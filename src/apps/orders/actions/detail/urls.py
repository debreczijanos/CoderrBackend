from django.urls import path

from .view import OrdersDetailView

urlpatterns = [
    path("<int:order_id>/", OrdersDetailView.as_view(), name="orders-detail"),
]
