from pathlib import Path

import django

from environ import environ

SECRET_KEY = "fake"
SITE_ID = 1
BASE_DIR = Path(__file__).resolve(strict=True).parents[1]

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / '.env'))

DATABASES = {
    'default': env.db(
        'DATABASE_URL',
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3')
    )
}

USE_TZ = True
TIME_ZONE = 'UTC'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'taggit',
    'versatileimagefield',
    'foxtail_blog',
)

ROOT_URLCONF = 'tests.urls'
RECAPTCHA_ENABLED = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

BLOG_FEED_TITLE = "Chocolate"
BLOG_FEED_DESCRIPTION = "Ice Cream"
BLOG_COMMENTS = True

django.setup()
