from django.urls import path

from .view import ProjectsDeleteView

urlpatterns = [
    path("<int:pk>/", ProjectsDeleteView.as_view(), name="projects-delete"),
]
