from django.urls import path

from .view import ReviewsListView

urlpatterns = [
    path("", ReviewsListView.as_view(), name="reviews-list"),
]
