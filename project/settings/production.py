from .settings import *
import os.path

PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../')
PARENT_ROOT = os.path.join(PROJECT_ROOT, '../')

DEBUG = False
TEMPLATE_DEBUG = False
DJANGO_SERVE_PUBLIC = False
PREPEND_WWW = True
SEND_BROKEN_LINK_EMAILS = True

APPEND_SLASH = True
FORCE_SCRIPT_NAME = ''
EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
DEFAULT_FROM_EMAIL = "noreply@gmail.com"
ADMINS = (
    ('admin', 'admin@admin.com'),
)
MANAGERS = ADMINS
INTERNAL_IPS = ('127.0.0.1',)
ROOT_URLCONF = 'urls'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": os.path.join(PARENT_ROOT, "database/database.db"), # Or path to database file if using sqlite3.
        "USER": "", # Not used with sqlite3.
        "PASSWORD": "", # Not used with sqlite3.
        "HOST": "", # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "", # Set to empty string for default. Not used with sqlite3.
        "OPTIONS": {"timeout": 30},
    }
}

MIDDLEWARE_CLASSES += (
    #'urlauth.middleware.AuthKeyMiddleware',
    #"django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
)

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

MEDIA_URL = "/media/"
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(PARENT_ROOT, "media")
STATIC_ROOT = os.path.join(PARENT_ROOT, "static")

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
]

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.comments',

)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },    
    'handlers': {
        'file_logging': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(PARENT_ROOT, 'logs/errors.log'),
        },
    },
    'loggers': {
        'django.db': {
            'level': 'ERROR',
            'handlers': ['file_logging'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file_logging'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# --------------------------------
#           APP SETTINGS
# --------------------------------
