from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles_app"
    label = "profiles"
    verbose_name = "Profiles"
