from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="profiles/"),
        ),
        migrations.AddField(
            model_name="profile",
            name="location",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="profile",
            name="tel",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="profile",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="working_hours",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
