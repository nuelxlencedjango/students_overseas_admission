"""
Django settings for educational project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""






from pathlib import Path

import os

import dj_database_url


#import django_heroku

#import cloudinary_storage
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=os.environ.get('SECRET_KEY')
#SECRET_KEY="django-insecure-^l)m&0ryr*fgyyy#zoxmsx^#03odx)55-sxpy&^%#_5ldqs9@s"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['127.0.0.1','web-production-cbed.up.railway.app']


# Application definition


  


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'core_app',
    'partners',

    'cloudinary',
     'django_countries',
    'crispy_forms',
    'django_filters',
     'widget_tweaks',
     'mathfilters',
     #'django_celery_results',
    # 'django_celery_beat',
      'fontawesomefree'
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

ROOT_URLCONF = 'educational.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR ,'templates')],
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

WSGI_APPLICATION = 'educational.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
 #   'default': {
  #      'ENGINE':'django.db.backends.postgresql',
   #     'NAME': 'educational',
    ##   'PASSWORD':'admin',
    #}
#}

DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'HOST' :os.environ.get('DATABASE_HOST'),
        'PORT':os.environ.get('DATABASE_PORT'),
        'USER' :os.environ.get('DATABASE_USER'),
        'PASSWORD' :os.environ.get('DATABASE_PASSWORD'),

    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'



STATICFILES_DIRS = [os.path.join(BASE_DIR ,'static') ]
STATIC_ROOT =os.path.join(BASE_DIR ,'assets')  

MEDIA_URL ='/media/'
MEDIA_ROOT =os.path.join(BASE_DIR ,'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


cloudinary.config( 
  cloud_name=os.environ.get('CLOUD_NAME'),
  api_key=os.environ.get('API_KEY'), 
  api_secret=os.environ.get('API_SECRET'), 
)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER =''
EMAIL_HOST_PASSWORD  = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'


CSRF_TRUSTED_ORIGINS=['https://*.127.0.0.1','https://web-production-cbed.up.railway.app']


#django_heroku.settings(locals())

#if os.getcwd() == '/app':
 #   SECURE_PROXY_SSL_HEADER =('HTTP_X_FORWARDED_PROTO', 'https')
 #   SECURE_SSL_REDIRECT =True
 #   DEBUG = False