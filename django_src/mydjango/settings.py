"""
Django settings for mydjango project.

Generated by 'django-admin startproject' using Django 3.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k($w_=ll!4%&xr*vxb-7d&pf)^^@6k=u$85%7^ufqwp8hr1s4('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "172.30.1.15",
    "14.39.38.10",
    "127.0.0.1",
    "0.0.0.0"
]


# Application definition

INSTALLED_APPS = [
    'channels',
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',

    'widget_tweaks',
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

ROOT_URLCONF = 'mydjango.urls'

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

ASGI_APPLICATION = "mydjango.routing.application"
WSGI_APPLICATION = 'mydjango.wsgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    # 'default': {
    #  'ENGINE': 'django.db.backends.mysql',
    #  'NAME': 'poor_db',  # DB명
    #  'USER': 'python',  # 데이터베이스 계정
    #  'PASSWORD': 'python',   # 계정 비밀번호
    #  'HOST': 'localhost',  # 데이테베이스 IP
    #  'PORT': '3306',  # 데이터베이스 port
    #  }

    'default': {
     'ENGINE': 'django.db.backends.mysql',
     'NAME': 'poor_db',  # DB명
     'USER': 'django',  # 데이터베이스 계정
     'PASSWORD': 'poordjango',   # 계정 비밀번호
     'HOST': 'poordb.cubqrb9xgtzf.us-east-1.rds.amazonaws.com',  # 데이테베이스 IP
     'PORT': '3306',  # 데이터베이스 port
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

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'sass_processor_finders.CssFinder',

]

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL)

SASS_ROOT = os.path.join(BASE_DIR, STATIC_URL)
SASS_PROCESSOR = True
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, STATIC_ROOT)
SASS_OUTPUT_STYLE = 'compact'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL='/'


AUTH_USER_MODEL = 'blog.User'


