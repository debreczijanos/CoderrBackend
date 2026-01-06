from django.urls import path

from .view import ProjectsUpdateView

urlpatterns = [
    path("<int:pk>/", ProjectsUpdateView.as_view(), name="projects-update"),
]
