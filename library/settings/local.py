from .base import *
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql', #'django.db.backends.sqlite3'
        'NAME': 'library', #'NAME': BASE_DIR / 'db.sqlite3'
        'USER': 'esteban',
        'PASSWORD': 'Sopra2020*-*',
        'HOST': '192.168.5.85',
        'PORT': '3306',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'