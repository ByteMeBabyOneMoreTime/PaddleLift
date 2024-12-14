from pathlib import Path
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "cron",
    "jobs",
    'tinymce',
    #  TIny MCE
    "corsheaders",
    # cors headers handler
    'jazzmin', 
    # jazzmin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    # corsheaders middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware', 
    #whitenoise middleware1
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    #whitenoise middleware2
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


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

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# configured static

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Enable Gzip compression
WHITENOISE_USE_FINDERS = True

# Enable WhiteNoise's built-in static file compression (for .gzip, .br files)
WHITENOISE_MANIFEST_STRICT = False
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# django jazzmin config
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Emerging India Foundation",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Admin Panel",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Emerging India",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": 'logo.png',

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": 'logo_sm.png',

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "welcome to the admin panel",

    # Copyright on the footer
    "copyright": "Emerging India Foundation",
  
    "show_ui_builder": True,
  
    #############
    # Side Menu #
    #############

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    "topmenu_links": [
        {"name": "Home",  "url": "/", "permissions": ["auth.view_user"]},
        {"name": "Gallery Image Upload",  "url": "/gallery/upload", "permissions": ["auth.view_user",  "is_superuser"]},
        {"name": "Gallery News Upload",  "url": "/gallery/upload_news", "permissions": ["auth.view_user",  "is_superuser"]},
        {"name": "Download Data in Excel",  "url": "/forms/download", "permissions": ["auth.view_user",  "is_superuser"]},
        ],

}

# jazzmin UI config
JAZZMIN_UI_TWEAKS = {
    
    "theme": "superhero",
    
}

# TIny MCE config
TINYMCE_DEFAULT_CONFIG = {
    "height": 500,  # Editor height
    "width": 800,   # Editor width
    "plugins": (
        "advlist autolink lists link charmap print preview anchor "
        "searchreplace visualblocks code fullscreen "
        "insertdatetime media table paste codesample emoticons"
    ),  # Enable all plugins except file uploads
    "toolbar": (
        "undo redo | formatselect | bold italic underline strikethrough | "
        "alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | "
        "link charmap table codesample emoticons | fullscreen preview code"
    ),  # Define the toolbar buttons
    "menubar": "edit view insert format tools table help",  # Keep the menubar
    "file_picker_callback": "function(callback, value, meta) { return false; }",  # Disable file picker
    "image_uploadtab": False,  # Disable image upload tab
    "automatic_uploads": False,  # Disable automatic uploads
    "media_live_embeds": True,  # Keep embedding features like videos
    "promotion": False,
    "branding": False,
}
