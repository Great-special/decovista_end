"""
Django settings for decovista_end project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# import cloudinary
# import cloudinary.uploader
# import cloudinary.api
from pathlib import Path
from datetime import timedelta
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a8g(uiq$j_v@21f5=i#)3z*vt%=&@276653vwsdy7w$nd2!3i!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1', '.circumeo-apps.net']

CSRF_TRUSTED_ORIGINS = [
    'https://a2w-creative-ampere.circumeo-apps.net',
    "https://decovista-api.vercel.app",
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'djoser',
    # 'cloudinary',
    # 'cloudinary_storage',
    
    # Our apps
    'appointment.apps.AppointmentConfig',
    'blog.apps.BlogConfig',
    'cart.apps.CartConfig',
    'payment.apps.PaymentConfig',
    'product.apps.ProductConfig',
    'users.apps.UsersConfig'
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'decovista_end.urls'

AUTH_USER_MODEL = "users.User"

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

WSGI_APPLICATION = 'decovista_end.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# django-environ
# env = environ.Env(
#     DEBUG=(bool, False)
# )

# reading .env file
# environ.Env.read_env(BASE_DIR/'.env')
#  replace config with env

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

#  Media Files
# cloudinary.config = {
#     'CLOUD_NAME': config('CLOUD_NAME'),
#     'API_KEY': config('API_KEY'),
#     'API_SECRET': config('API_SECRET'),
# }


# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR/'static_files'


# MEDIA_BASE_URL = 'https://res.cloudinary.com/' + config('CLOUD_NAME')
MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR/'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Setting Up User Authentication with Djoser and JWT

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default backend
    'users.backends.EmailOrUsernameModelBackend',  # Custom backend
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticated',
    ],
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=4),
}


DJOSER = {
    'LOGIN_FIELD':'username',
    'USER_CREATE_PASSWORD_RETYPE': False,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': False,
    
    'SERIALIZERS': {
        'user_create': 'users.serializers.CustomUserCreateSerializer',
        'user': 'users.serializers.CustomUserSerializer',
        'current_user': 'users.serializers.CustomUserSerializer',
    },
}



# CORS_ALLOWED_ORIGINS = [
#     "https://decovista-api.vercel.app",
#     "https://a2w-creative-ampere.circumeo-apps.net",  # If you have a production domain
# ]

CORS_ALLOW_ALL_ORIGINS = True
