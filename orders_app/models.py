from django.conf import settings
from django.db import models


class Order(models.Model):
    """Order created from an offer detail between customer and business."""
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_COMPLETED = "completed"
    STATUS_CANCELLED = "cancelled"
    STATUS_CHOICES = [
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    customer_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customer_orders"
    )
    business_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="business_orders"
    )
    title = models.CharField(max_length=200)
    revisions = models.IntegerField()
    delivery_time_in_days = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.JSONField(default=list, blank=True)
    offer_type = models.CharField(max_length=20)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_IN_PROGRESS
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Order {self.id} ({self.status})"
