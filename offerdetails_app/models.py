from django.db import models

from offers_app.models import Offer


class OfferDetail(models.Model):
    TYPE_BASIC = "basic"
    TYPE_STANDARD = "standard"
    TYPE_PREMIUM = "premium"
    TYPE_CHOICES = [
        (TYPE_BASIC, "Basic"),
        (TYPE_STANDARD, "Standard"),
        (TYPE_PREMIUM, "Premium"),
    ]

    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="details")
    title = models.CharField(max_length=200)
    revisions = models.IntegerField()
    delivery_time_in_days = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.JSONField(default=list, blank=True)
    offer_type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["offer", "offer_type"], name="uniq_offer_type")
        ]

    def __str__(self) -> str:
        return f"{self.offer_id} - {self.offer_type}"
