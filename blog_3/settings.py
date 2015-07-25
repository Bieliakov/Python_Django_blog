"""
Django settings for blog_3 project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
# import file for getting secret keys information (for security reasons)
#from blog_secret_keys import SECRET_KEY, SOCIAL_AUTH_FACEBOOK_KEY, SOCIAL_AUTH_FACEBOOK_SECRET
SECRET_KEY = 'si9v7yn-zd@4uj&ohua8eh5@f-hu@i4uync2#4e)14r1zo$bvf'


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    #'social.apps.django_app.default',
)
# 'social.apps.django_app.default' - is for registration via social networks

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'blog_3.urls'

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

# http://artandlogic.com/2014/04/tutorial-adding-facebooktwittergoogle-authentication-to-a-django-application/
# for registration via social networks:
#TEMPLATE_CONTEXT_PROCESSORS = (
#   'django.contrib.auth.context_processors.auth',
#   'django.core.context_processors.debug',
#  'django.core.context_processors.i18n',
#   'django.core.context_processors.media',
#   'django.core.context_processors.static',
#   'django.core.context_processors.tz',
#   'django.contrib.messages.context_processors.messages',
#   'social.apps.django_app.context_processors.backends',
#   'social.apps.django_app.context_processors.login_redirect',
#)
#
#AUTHENTICATION_BACKENDS = (
#   'social.backends.facebook.FacebookOAuth2',
#   'social.backends.google.GoogleOAuth2',
#   'social.backends.twitter.TwitterOAuth',
#   'django.contrib.auth.backends.ModelBackend',
#)

# here goes importing SOCIAL_AUTH_FACEBOOK_KEY and SOCIAL_AUTH_FACEBOOK_SECRET

# next two lines is under question
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)
#print(TEMPLATE_PATH)
#c:\Users\Zboch\projects\blog_3\templates
#print(BASE_DIR)
#c:\Users\Zboch\projects\blog_3

WSGI_APPLICATION = 'blog_3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# in my.cnf file is stored mysql database properties
DATABASES = {
    'default': {
		'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'ENGINE': 'django.db.backends.mysql',
        #'OPTIONS': {
        #    'read_default_file': 'c:/Program Files/MySQL/MySQL Server 5.5/my.cnf',
        #    'init_command': 'SET storage_engine=INNODB',
        #},
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_PATH,
    '',
)

#MEDIA_URL = '/images/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'images') # Absolute path to the images directory

