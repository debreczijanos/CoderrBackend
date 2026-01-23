from django.urls import path

from . import views

urlpatterns = [
    path("orders/", views.orders_collection, name="orders-collection"),
    path("orders/<int:order_id>/", views.order_detail, name="orders-detail"),
    path("order-count/<int:profile_id>/", views.order_count, name="orders-count"),
    path("completed-order-count/<int:profile_id>/", views.order_completed_count, name="orders-completed-count"),
]
