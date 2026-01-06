from django.urls import path

from .view import OrdersCollectionView

urlpatterns = [
    path("", OrdersCollectionView.as_view(), name="orders-collection"),
]
