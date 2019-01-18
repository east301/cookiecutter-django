#
#
#

import os


# ================================================================================
# directory
# ================================================================================

PACKAGE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ================================================================================
# security
# ================================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]


# ================================================================================
# application
# ================================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'compressor',
    'bootstrap4',
    'hamlpy',

    '{{cookiecutter.package_name}}.apps.account',
    '{{cookiecutter.package_name}}.apps.common',
    '{{cookiecutter.package_name}}.apps.notification'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    '{{cookiecutter.package_name}}.apps.common.middlewares.WSGIScriptNameMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]


# ================================================================================
# url
# ================================================================================

ROOT_URLCONF = '{{cookiecutter.package_name}}.urls'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = None
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'


# ================================================================================
# wsgi
# ================================================================================

WSGI_APPLICATION = '{{cookiecutter.package_name}}.wsgi.application'


# ================================================================================
# templates
# ================================================================================

print(os.path.join(PACKAGE_DIR, 'apps', 'common', 'templates'))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PACKAGE_DIR, 'apps', 'common', 'templates')
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                '{{cookiecutter.package_name}}.apps.common.context_processors.django_settings',
                '{{cookiecutter.package_name}}.apps.notification.context_processors.notification'
            ],
            'loaders': [
                'hamlpy.template.loaders.HamlPyFilesystemLoader',
                'hamlpy.template.loaders.HamlPyAppDirectoriesLoader'
            ]
        }
    }
]


# ================================================================================
# static
# ================================================================================

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
]


# ================================================================================
# i18n
# ================================================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
