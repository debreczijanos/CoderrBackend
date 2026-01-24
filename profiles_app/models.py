from django.conf import settings
from django.db import models


class Profile(models.Model):
    """User profile metadata for business or customer accounts."""
    TYPE_BUSINESS = "business"
    TYPE_CUSTOMER = "customer"
    TYPE_CHOICES = [
        (TYPE_BUSINESS, "Business"),
        (TYPE_CUSTOMER, "Customer"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    file = models.FileField(upload_to="profiles/", blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    tel = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    working_hours = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} ({self.type})"
