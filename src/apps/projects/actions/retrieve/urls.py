from django.urls import path

from .view import ProjectsRetrieveView

urlpatterns = [
    path("<int:pk>/", ProjectsRetrieveView.as_view(), name="projects-retrieve"),
]
