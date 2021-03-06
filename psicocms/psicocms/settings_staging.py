from psicocms.psicocms.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [ 'formazione.psicologipuglia.it', ]

WSGI_APPLICATION = 'psicocms.psicocms.wsgi_staging.application'

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
