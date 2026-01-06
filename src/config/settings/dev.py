from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

if os.getenv("DJANGO_USE_SQLITE", "1") == "1":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
