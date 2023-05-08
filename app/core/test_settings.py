# flake8: noqa F403
from .settings import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
