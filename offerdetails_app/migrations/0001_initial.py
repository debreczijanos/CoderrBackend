from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("offers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OfferDetail",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("revisions", models.IntegerField()),
                ("delivery_time_in_days", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("features", models.JSONField(blank=True, default=list)),
                (
                    "offer_type",
                    models.CharField(
                        choices=[("basic", "Basic"), ("standard", "Standard"), ("premium", "Premium")],
                        max_length=20,
                    ),
                ),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="details",
                        to="offers.offer",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="offerdetail",
            constraint=models.UniqueConstraint(fields=("offer", "offer_type"), name="uniq_offer_type"),
        ),
    ]
