from psicocms.psicocms.settings import *

DEBUG = True
TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

CAS_SERVER_URL = 'http://localhost:8000/cas/' # this must be the local url for the project with CAS authentication

ALLOWED_HOSTS = [ 'localhost', ]

ROOT_URLCONF = 'psicocms.psicocms.urls_local'
