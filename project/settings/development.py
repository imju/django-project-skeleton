from .production import *

DEBUG = True
TEMPLATE_DEBUG = True
DJANGO_SERVE_PUBLIC = True
PREPEND_WWW = False
SEND_BROKEN_LINK_EMAILS = False
SESSION_ENGINE = 'django.contrib.sessions.backends.file'

# APP: debug_toolbar
MIDDLEWARE_CLASSES += (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

INSTALLED_APPS += (
    "debug_toolbar",
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

TEMPLATE_CONTEXT_PROCESSORS += [
    'django.core.context_processors.debug'
]

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
            'level': 'DEBUG',
            'handlers': ['file_logging'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file_logging'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

