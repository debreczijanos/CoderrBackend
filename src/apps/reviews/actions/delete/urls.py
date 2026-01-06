from django.urls import path

from .view import ReviewsDeleteView

urlpatterns = [
    path("<int:pk>/", ReviewsDeleteView.as_view(), name="reviews-delete"),
]
