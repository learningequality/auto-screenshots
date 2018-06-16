"""
Django settings for HookCatcherProj project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY') or 'qwnj&01%5_q$j+&v**2o9mafh+zt9^y^ntgkr#wp+a125ky(ta'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'HookCatcher.apps.HookcatcherConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_rq',
    'channels',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HookCatcherProj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'HookCatcherProj.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

MEDIA_URL = '/media/'


# Leverage object file storage in s3 bucket
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID') or 'mingdaidev'
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY') or 'mingdaidev'
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME') or 'ming'
AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL') or 'http://minio'

# Using Loggers instead of print statements for console output!
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'WARN',
        },
        'HookCatcher': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}

# --- GET ALL THE OTHER ENV VARIABLES ---
# GIT_REPO = os.getenv('GIT_REPO')    # the Github Repository you are attempting to link to

# GIT_OAUTH = os.getenv('GIT_OAUTH')  # your Github Access Token

# # the name of the directory in the Git Repository that stores the state representation JSON files.
# STATES_FOLDER = os.getenv('STATES_FOLDER')

# # File to set what specific screenshot settings you want
# SCREENSHOT_CONFIG = os.getenv('SCREENSHOT_CONFIG')

# # browser stack api username
# BROWSERSTACK_USERNAME = os.getenv('BROWSERSTACK_USERNAME') or ''

# # browser stack api authentication *need subscription*
# BROWSERSTACK_OAUTH = os.getenv('BROWSERSTACK_OAUTH') or ''

# try to get the env variable for Postgres port
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
if not POSTGRES_PORT:
    POSTGRES_PORT = 5432
POSTGRES_HOST = os.getenv("POSTGRES_HOST") or "127.0.0.1"
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD") or "garnish"
POSTGRES_USER = os.getenv("POSTGRES_USER") or "garnish_user"
POSTGRES_DB_NAME = os.getenv("POSTGRES_DB_NAME") or "garnish_db"


# Load user specific settings saved in a separate file
try:
    execfile(os.path.join(BASE_DIR, "user_settings.py"), globals(), locals())
except NameError:
    with open(os.path.join(BASE_DIR, "user_settings.py")) as f:
        code = compile(f.read(), os.path.join(BASE_DIR, "user_settings.py"), 'exec')
        exec(code, globals(), locals())
except IOError:
    pass

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DB_NAME,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    }
}

REDIS_HOST = os.getenv("REDIS_HOST") or "127.0.0.1"
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD") or ''

# try to get the env variable for Redis port
REDIS_PORT = os.getenv('REDIS_PORT')
if not REDIS_PORT:
    REDIS_PORT = 6379

RQ_QUEUES = {
    'default': {
        'HOST': REDIS_HOST,
        'PORT': int(REDIS_PORT),
        'DB': 0,
        'PASSWORD': REDIS_PASSWORD,
        'DEFAULT_TIMEOUT': 360,
    },
}

REDIS_URL = os.getenv("REDIS_URL")
if not REDIS_URL:
    REDIS_URL = "redis://{1}:{2}/0".format(REDIS_PASSWORD,
                                           REDIS_HOST,
                                           REDIS_PORT)
# Django Channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(REDIS_URL)],
        },
        "ROUTING": "HookCatcherProj.routing.channel_routing",
    },
}
