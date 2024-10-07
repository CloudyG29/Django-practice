import os
from .settings import *
from .settings import BASE_DIR
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET')
ALLOWED_HOSTS = ['phoneshop-o27b.onrender.com']
DEBUG = True
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')





DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'), conn_max_age=600)
}