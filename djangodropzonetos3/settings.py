"""
Django settings for djangodropzonetos3 project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hp@uj0)$tf)*q-e)6t6hj(t2(y-ixo7z174cj*gz-5!u*z^gz6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'storages',
    'dropzone',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangodropzonetos3.urls'

WSGI_APPLICATION = 'djangodropzonetos3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_TITLE = "My S3 Bucket Uploader"
CONTACT_EMAIL = 'user@myserver.com'
# If ANNONYMOUS_UPLOADS is true, users will be prompted for the SHARED_KEY prior to being allowed to upload
ALLOWED_FILE_MIME_TYPES = ['image/jpeg', 'image/png', 'image/gif']
ANNONYMOUS_UPLOADS = False
SHARED_KEY = 'shared_key'

# Modify these variables to configure the connection to your AWS S3 bucket
AWS_ACCESS_KEY_ID = 'aws_access_key'
AWS_SECRET_ACCESS_KEY = 'aws_secret_access_key'
AWS_STORAGE_BUCKET_NAME = 'aws-storage-bucket-name'
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = '/static/'
MEDIA_DIRECTORY = '/media/'
MEDIA_ROOT = 'media/'
MEDIA_URL = S3_URL + MEDIA_DIRECTORY
