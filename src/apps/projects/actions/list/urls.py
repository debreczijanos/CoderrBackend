from django.urls import path

from .view import ProjectsListView

urlpatterns = [
    path("", ProjectsListView.as_view(), name="projects-list"),
]
