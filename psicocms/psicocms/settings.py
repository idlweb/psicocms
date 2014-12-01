"""
Django settings for cms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os

# site ID
SITE_ID = 1

CONFIG_ROOT = os.path.abspath(os.path.dirname((os.path.dirname(__file__))))
PROJECT_ROOT = os.path.abspath(os.path.dirname(CONFIG_ROOT))
REPOSITORY_ROOT = os.path.abspath(os.path.dirname(PROJECT_ROOT))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2@+%rc*(+s5fwj(y*%hl4=9$(mox8190+zf!x2(*d(if(e09y#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    #'django.contrib.staticfiles',
    #-----da zinnia
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django_comments',
    'django.contrib.sitemaps',
    'django_cas',
    'mama_cas',
    'django_extensions',
    'south',
    'mptt',
    'tagging',
    'zinnia_foundation', # BEFORE the "zinnia" app
    'zinnia',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'zinnia.context_processors.version',  # Optional
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_cas.middleware.CASMiddleware',
)

ZINNIA_ENTRY_CONTENT_TEMPLATES = [
	('zinnia/fullwidth_entry_detail.html','Fullwidth template'),
	('zinnia/_short_entry_detail.html','Short entry template'),
]

ROOT_URLCONF = 'psicocms.psicocms.urls'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join( REPOSITORY_ROOT, 'media').replace('\\','/')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = os.path.join(REPOSITORY_ROOT, 'sitestatic')

CAS_IGNORE_REFERER = False
CAS_LOGOUT_COMPLETELY = True
CAS_SERVER_URL = '' # this must be set in the settings of your deploy

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
