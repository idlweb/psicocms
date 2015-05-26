from psicocms.psicocms.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [ 'formazione.psicologipuglia.it', ]

ADMINS = (
    ('Antonio Vangi', 'antonio.vangi.av@gmail.com')
)

WSGI_APPLICATION = 'psicocms.psicocms.wsgi_production.application'

MEDIA_ROOT = os.path.join(REPO_ROOT, "..", "public", "media" )
STATIC_ROOT = os.path.join(REPO_ROOT, "..", "public", "static" )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'psicocms',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}

CAS_SERVER_URL = 'http://ordine.psicologipuglia.it/cas/'

MAMA_CAS_ENABLE_SINGLE_SIGN_OUT = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
        'console_import':{
            'level':'WARNING',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
        'logfile': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': REPO_ROOT + "/log/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'webapp': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': REPO_ROOT + "/log/webapp.log",
            'maxBytes': 50000,
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        'import': {
            'handlers': ['console_import', 'logfile'],
            'level': 'DEBUG',
            'propagate': True,
            },
        'webapp': {
            'handlers': [ 'webapp', ],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


