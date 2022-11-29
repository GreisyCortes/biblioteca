from .base import *
from pathlib import Path

from unipath import Path
import os
BASE_DIR = Path(__file__).ancestor(3)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbbiblioteca',
        'USER': 'admin',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
#MEDIA_ROOT = BASE_DIR.child('media')
