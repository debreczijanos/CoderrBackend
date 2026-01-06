from django.urls import path

from .view import ProjectsCreateView

urlpatterns = [
    path("", ProjectsCreateView.as_view(), name="projects-create"),
]
