from django.urls import path

from .views import (
    OrderCompletedCountView,
    OrderCountView,
    OrderDetailView,
    OrdersCollectionView,
)

urlpatterns = [
    path("orders/", OrdersCollectionView.as_view(), name="orders-collection"),
    path("orders/<int:order_id>/", OrderDetailView.as_view(), name="orders-detail"),
    path("order-count/<int:profile_id>/", OrderCountView.as_view(), name="orders-count"),
    path(
        "completed-order-count/<int:profile_id>/",
        OrderCompletedCountView.as_view(),
        name="orders-completed-count",
    ),
]
