"""
Django settings for alx_travel_app project.
"""

from pathlib import Path
import os
import environ # 1. Import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment variables
env = environ.Env()
# Reads the .env file in the base directory
# Assuming your .env file is now in the same directory as settings.py
environ.Env.read_env(os.path.join(Path(__file__).resolve().parent, '.env')) 

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))



# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR is one level up in the "flat" structure (alx_travel_app folder)
BASE_DIR = Path(__file__).resolve().parent 


# Quick-start development settings - unsuitable for production
SECRET_KEY = env('SECRET_KEY') # 1. Get SECRET_KEY from .env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = ['*'] # Allows all hosts for development

# Application definition

INSTALLED_APPS = [
    # Django standard apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 2. Third-party apps required for the project
    'rest_framework',
    'corsheaders',
    'drf_yasg', # For Swagger documentation
    'django_cleanup.apps.CleanupConfig', # Optional, but good practice if you handle files

    # 2.custom app
    'listings', 
]

MIDDLEWARE = [
    # 4. CORS Middleware must be placed as high as possible
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'alx_travel_app.urls'

# ... (TEMPLATES and WSGI_APPLICATION remain the same) ...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'alx_travel_app.wsgi.application'


# 3. Database Configuration (Use MySQL via DATABASE_URL)
DATABASES = {
    # Read the DATABASE_URL from .env. The default is SQLite for local fallback
    'default': env.db(default='sqlite:///db.sqlite3'), 
}

# 4. CORS Headers Configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    # Add any other required domains here
]

# ... (Password Validators remain the same) ...

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 5. DRF-YASG (Swagger) Settings
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic'
        }
    }
}