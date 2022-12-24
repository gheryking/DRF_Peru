from .base import *

# TODO ->
SECRET_KEY = 'Sistemas123'

# SECURITY WARNING: don't run with debug turned on in production!
# TODO ->
DEBUG = True

# TODO ->
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field