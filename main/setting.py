import os
import logging.config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ADMIN and MANAGERS configuration
ADMINS = [
	('Admin', 'admin@email.com'), 
]

MANAGERS = ADMINS

# Email sender setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 
EMAIL_USE_TLS = 
EMAIL_PORT = 
EMAIL_HOST_USER = 
EMAIL_HOST_PASSWORD = 

# # System logging enable even DEBUG = False
# LOGGING = {
    # 'version': 1,
    # 'disable_existing_loggers': False,
    # 'formatters': {
        # 'fmt1': {
            # 'format': '[FMT1] %(asctime)-15s %(message)s',
        # },
        # 'fmt2': {
            # 'format': '[FMT2] %(asctime)-15s %(message)s',
        # }
    # },
    # 'handlers': {
        # 'console1': {
            # 'level': 'INFO',
            # 'class': 'logging.StreamHandler',
            # 'formatter': 'fmt1',
        # },
        # 'console2': {
            # 'level': 'INFO',
            # 'class': 'logging.StreamHandler',
            # 'formatter': 'fmt2',
        # },
    # },
    # # First config for root logger: console1 -> fmt1
    # 'root': {
        # 'handlers': ['console1'],
        # 'level': 'DEBUG',
        # 'propagate': True,
    # },
    # 'loggers': {
        # # Second config for root logger: console2 -> fmt2
        # '': {
            # 'handlers': ['console2'],
            # 'level': 'DEBUG',
            # 'propagate': True,
        # },
    # },
# }

# logging.config.dictConfig(LOGGING)

# l1 = logging.getLogger()
# l2 = logging.getLogger('')
# root = logging.root

# l1.info("l1")
# l2.info("l2")
# root.info("root logger")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
	'localhost',
	'127.0.0.1'
]

# Application definition

INSTALLED_APPS = [
    'personal', 
	'ckeditor',
    'ckeditor_uploader',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

# STATICFILES_STORAGE = ['django.contrib.staticfiles.storage.ManifestStaticFilesStorage']
# STATICFILES_STORAGE = ['whitenoise.storage.CompressedManifestStaticFilesStorage']

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root').replace('\\', '/')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root').replace('\\', '/')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
]

# CKEDITOR CONFIGURATION ##
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
 
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
 
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

# Configure Django App for Heroku.
# import django_heroku
# django_heroku.settings(locals())

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
