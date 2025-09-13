from .base import *


ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3',
    }
}

# Development-specific settings
INSTALLED_APPS += [
    'django.contrib.staticfiles',
    'debug_toolbar',
]

MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE

# Debug toolbar settings
INTERNAL_IPS = [
    '127.0.0.1',
]