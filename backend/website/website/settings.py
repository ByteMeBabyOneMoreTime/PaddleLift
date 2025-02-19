from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _

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
    # cron job
    
    "jobs",
    'cloud',
    'home_page_content',
    'tinymce',
    #  TIny MCE
    "corsheaders",
    # cors headers handler
    'import_export',
    "unfold",  # before django.contrib.admin
    # "unfold.contrib.filters",  # optional, if special filters are needed
    # "unfold.contrib.forms",  # optional, if special form elements are needed
    # "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    # "unfold.contrib.guardian",  # optional, if django-guardian package is used
    # "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    'image_uploader_widget',
    # Image field
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

UNFOLD = {
    "SITE_HEADER": _("PaddleLift Admin"),
    "SITE_TITLE": _("PaddleLift Admin"),
    "SITE_SYMBOL": "settings",
    "SITE_URL": "/",
    # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
    "SITE_ICON": {
        "light": lambda request: static("Plogo.svg"),  # light mode
        "dark": lambda request: static("Plogo.svg"),  # dark mode
    },
    # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
    "SITE_LOGO": {
        "light": lambda request: static("Paddlelite Logo.png"),  # light mode
        "dark": lambda request: static("Paddlelite Logo.png"),  # dark mode
    },
    "SCRIPTS": [
        lambda request: static("loader.js"),
    ],
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("favicon.svg"),
        },
    ],
    "SHOW_HISTORY": True, # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True, # show/hide "View on site" button, default: True
    
    "BORDER_RADIUS": "0px",
    "COLORS": {
        "base": {
            "50": "249 250 251",
            "100": "243 244 246",
            "200": "229 231 235",
            "300": "209 213 219",
            "400": "156 163 175",
            "500": "107 114 128",
            "600": "75 85 99",
            "700": "55 65 81",
            "800": "31 41 55",
            "900": "17 24 39",
            "950": "3 7 18",
        },
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",  # text-base-500
            "subtle-dark": "var(--color-base-400)",  # text-base-400
            "default-light": "var(--color-base-600)",  # text-base-600
            "default-dark": "var(--color-base-300)",  # text-base-300
            "important-light": "var(--color-base-900)",  # text-base-900
            "important-dark": "var(--color-base-100)",  # text-base-100
        },
    },
    
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
}

# Google Drive Config
SCOPES = ['https://www.googleapis.com/auth/drive']
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_CLIENT_EMAIL = os.getenv("GCP_CLIENT_EMAIL")
GCP_PRIVATE_KEY_ID = os.getenv("GCP_PRIVATE_KEY_ID")
GCP_CLIENT_ID = os.getenv("GCP_CLIENT_ID")
GCP_CLIENT_X509_CERT_URL = os.getenv("GCP_CLIENT_X509_CERT_URL")
SERPAPIKEY = os.getenv("SERPAPIKEY")

CV_FOLDER=os.getenv('CV_FOLDER')
HOME_PAGE_CONTENT_FOLDER = os.getenv('HOME_PAGE_CONTENT_FOLDER')