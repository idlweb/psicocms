from psicocms.psicocms.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [ 'www.psicologipuglia.it', ]

WSGI_APPLICATION = 'psicocms.psicocms.wsgi_staging.application'

STATIC_ROOT = ( os.path.join(REPOSITORY_ROOT, "public", "static" ))

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

CAS_SERVER_URL = 'http://%s/cas/' % ALLOWED_HOSTS[0] # this is the url of local service
