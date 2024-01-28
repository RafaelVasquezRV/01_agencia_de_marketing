from .settings import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DB_SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}