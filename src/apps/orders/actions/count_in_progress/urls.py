from django.urls import path

from .view import OrdersCountInProgressView

urlpatterns = [
    path("order-count/<int:profile_id>/", OrdersCountInProgressView.as_view(), name="orders-count-in-progress"),
]
