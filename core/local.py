from .settings import *
from .db import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG1')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEV')

# Database
DATABASES = DB_SQLITE3

CORS_ORIGIN_WHITELIST =env.list('CORS_ORIGIN_WHITELIST_DEV')
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_DEV')