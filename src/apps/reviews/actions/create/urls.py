from django.urls import path

from .view import ReviewsCreateView

urlpatterns = [
    path("", ReviewsCreateView.as_view(), name="reviews-create"),
]
