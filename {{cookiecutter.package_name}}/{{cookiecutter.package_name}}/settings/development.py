#
#
#

import os

from .common import *   # NOQA


# ================================================================================
# directory
# ================================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMP_DIR = os.path.join(BASE_DIR, 'temporary')

os.makedirs(TEMP_DIR, exist_ok=True)


# ================================================================================
# security
# ================================================================================

SECRET_KEY = 'zekl=5tm4a$a@z9z5@vjsb0gb^v%3-48m&*cxr^^dp&)^bv6c@'

DEBUG = True
ALLOWED_HOSTS = ['*']


# ================================================================================
# environment
# ================================================================================

ENVIRONMENT_NAME = 'Development'
ENVIRONMENT_COLOR = 'gray'


# ================================================================================
# application
# ================================================================================

INSTALLED_APPS += [     # NOQA
    'livereload'
]

MIDDLEWARE += [         # NOQA
    'livereload.middleware.LiveReloadScript'
]


# ================================================================================
# live reload
# ================================================================================

LIVERELOAD_HOST = os.environ.get('LIVERELOAD_HOST', '127.0.0.1')
LIVERELOAD_PORT = os.environ.get('LIVERELOAD_PORT', '35729')


# ================================================================================
# static
# ================================================================================

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(TEMP_DIR, 'static')


# ================================================================================
# database
# ================================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TEMP_DIR, 'db.sqlite3')
    }
}


# ================================================================================
# mail
# ================================================================================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
