import os
import environ
from .base import *
from pathlib import Path

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(str, ',')
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

allowed_hosts = env('ALLOWED_HOSTS')
ALLOWED_HOSTS = allowed_hosts.split(',') 
DEBUG = False
STATIC_ROOT = env('STATIC_ROOT')

# ==================================================
# becareful when using these settings especially  ||
# SECURE_HSTS_SECONDS related settings            ||
# ==================================================

# SESSION_COOKIE_SECURE=True
# CSRF_COOKIE_SECURE=True
# SECURE_SSL_REDIRECT=True
# SECURE_HSTS_SECONDS=60
# SECURE_HSTS_PRELOAD=True
# SECURE_HSTS_INCLUDE_SUBDOMAINS=True
