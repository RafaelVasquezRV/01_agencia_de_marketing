from .settings import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DB_SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DB_POSTGRESQL = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get('DB_NAME'),
        "USER": os.environ.get('USER'),
        "PASSWORD": os.environ.get('PASSWORD'),
        "HOST": os.environ.get('HOST'),
        "PORT": os.environ.get('PORT'),
    }
}

DB_POSTGRESQL["default"]["ATOMIC_REQUESTS"] = True