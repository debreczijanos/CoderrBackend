from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts_app"
    label = "accounts"
    verbose_name = "Accounts"
