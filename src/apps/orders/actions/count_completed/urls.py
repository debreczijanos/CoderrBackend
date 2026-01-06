from django.urls import path

from .view import OrdersCountCompletedView

urlpatterns = [
    path("completed-order-count/<int:profile_id>/", OrdersCountCompletedView.as_view(), name="orders-count-completed"),
]
