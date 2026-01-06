from django.urls import path

from .view import ReviewsRetrieveView

urlpatterns = [
    path("<int:pk>/", ReviewsRetrieveView.as_view(), name="reviews-retrieve"),
]
