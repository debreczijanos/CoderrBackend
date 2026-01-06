from django.urls import path

from . import views

urlpatterns = [
    path("reviews/", views.reviews_collection, name="reviews-collection"),
    path("reviews/<int:review_id>/", views.review_detail, name="reviews-detail"),
]
