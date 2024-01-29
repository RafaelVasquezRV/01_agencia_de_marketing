from .settings import *
from .db import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG0')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEPLOY')

# Database
DATABASES = DB_POSTGRESQL

CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST_DEPLOY')
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_DEPLOY')