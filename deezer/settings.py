"""
Django settings for deezer_ project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import datetime
import os
import logging

logger = logging.getLogger(__name__)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
JWT_REFRESH_SECRET_KEY = os.environ.get('JWT_REFRESH_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True if os.environ.get("DEBUG") == "TRUE" else False

ADMIN_ENABLED = True
if not DEBUG:
    ADMIN_ENABLED = False

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    '127.0.0.1',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'content-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-refresh-token',
]
CORS_EXPOSE_HEADERS = [
    'new_access_token'
]

FACEBOOK_APP_ID = '130632618976177'
FACEBOOK_APP_SECRET = '1f1b9b875bcd5a906ab2be0f483fcbb0'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'rest_framework_jwt',
    'corsheaders',
    'debug_toolbar',
    'django_filters',
    'user',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'deezer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), os.path.join(BASE_DIR, "user", "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'deezer.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DATABASE_NAME"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOST"),
        'PORT': os.environ.get("POSTGRES_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication'
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_THROTTLE_CLASSES': [],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
    },
}
AUTH_USER_MODEL = 'user.User'
JWT_ACCESS_TOKEN_EXPIRATION_TIME_IN_MINUTE = 15
JWT_REFRESH_TOKEN_EXPIRATION_TIME_IN_DAY = 7

JWT_AUTH = {
    'JWT_SECRET_KEY': JWT_SECRET_KEY,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=int(os.environ.get(
        'JWT_ACCESS_TOKEN_EXPIRATION_TIME_IN_MINUTE')) or JWT_ACCESS_TOKEN_EXPIRATION_TIME_IN_MINUTE),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(
        days=int(os.environ.get('JWT_REFRESH_TOKEN_EXPIRATION_TIME_IN_DAY')) or JWT_REFRESH_TOKEN_EXPIRATION_TIME_IN_DAY
    ),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_AUTH_COOKIE': 'ACCESS_TOKEN',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'deezer.custom_jwt_response_payload_handler.custom_jwt_response_handler',
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
LOGIN_REDIRECT_URL = ''

APPEND_SLASH = False
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["console"]},
    "formatters": {
        "verbose": {
            "format": (
                "[%(asctime)s] %(levelname)s %(name)s %(message)s [PID:%(process)d:%(threadName)s]"
            )
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.server": {"handlers": ["console"], "level": "INFO", "propagate": True},
    },
}
REFRESH_TOKEN_SECRET_KEY = os.environ.get("REFRESH_TOKEN_SECRET_KEY")
REFRESH_TOKEN_EXPIRED = datetime.timedelta(minutes=60 * 24 * 7)
REFRESH_TOKEN_COOKIE = 'REFRESH_TOKEN'
REFRESH_TOKEN_HEADER = 'HTTP_X_REFRESH_TOKEN'
ACCESS_TOKEN_HEADER = 'new_access_token'
COOKIE_SECURE = False
if os.environ.get('COOKIE_SECURE'):
    COOKIE_SECURE = os.environ.get('COOKIE_SECURE')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
