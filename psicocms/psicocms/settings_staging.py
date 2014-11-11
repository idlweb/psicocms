from psicocms.psicocms.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

WSGI_APPLICATION = 'psicocms.psicocms.wsgi_staging.application'

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
