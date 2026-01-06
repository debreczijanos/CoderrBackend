from django.urls import path

from .view import ReviewsCollectionView

urlpatterns = [
    path("", ReviewsCollectionView.as_view(), name="reviews-collection"),
]
