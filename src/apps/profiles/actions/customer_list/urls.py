from django.urls import path

from .view import ProfilesCustomerListView

urlpatterns = [
    path("customer/", ProfilesCustomerListView.as_view(), name="profiles-customer-list"),
]
