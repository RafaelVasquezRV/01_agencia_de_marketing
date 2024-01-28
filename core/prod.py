from .settings import *
from .db import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
DATABASES = DB_SQLITE3