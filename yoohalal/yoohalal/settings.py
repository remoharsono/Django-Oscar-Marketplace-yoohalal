"""
Django settings for yoohalal project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from oscar.defaults import *
from django.utils.translation import ugettext_lazy as _

# Path helper
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '**vx6=*mn)al@4hjvb4c+qz*5$5^=8fvq7+hrh$t*j&r7r9wue'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
THUMBNAIL_DEBUG = True

ALLOWED_HOSTS = ['.yoohalal.com', '127.0.0.1', 'localhost', 'yoohalal.com']

from oscar import get_core_apps

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'compressor',
    'widget_tweaks',
    'easy_thumbnails',
    'robots',
    'meta',
    'django_markdown',
    'apps.banktransfer',
    'apps.confirmation',
    'apps.subscribe',
    'apps.slider',
    'apps.blog',
    'apps.career',
    'apps.social_media',
    'social_django',
] + get_core_apps([
    'apps.customer',
    'apps.payment',
    'apps.order',
    'apps.catalogue',
    'apps.checkout',
    'apps.shipping',
    'apps.search',
    'apps.address',
    'apps.partner',
    'apps.dashboard.partners',
    'apps.dashboard.catalogue',
    'apps.dashboard.orders',
    'apps.dashboard.promotions',
    'apps.promotions',
    ])

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'yoohalal.urls'

from oscar import OSCAR_MAIN_TEMPLATE_DIR

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ 
            os.path.join(BASE_DIR, 'templates'),
            OSCAR_MAIN_TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
                'apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'yoohalal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yoohalal_db',
        'USER': 'life',
        'PASSWORD': 'pass@word1',
        'HOST': 'localhost',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'id'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Includes all languages that have >50% coverage in Transifex
# Taken from Django's default setting for LANGUAGES
gettext_noop = lambda s: s
LANGUAGES = (
    ('id', gettext_noop('Bahasa Indonesia')),
)

# Locale Path
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)

LOCAL_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
# Search Backends

# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',    
#     },
# }
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': location('whoosh_index'),
    },
}

# Deﬁnes all the statuses an order

OSCAR_INITIAL_ORDER_STATUS = 'Belum Dibayar'
OSCAR_INITIAL_LINE_STATUS = 'Belum Dibayar'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Belum Dibayar': ('Telah Dibayar', 'Batal',),
    'Telah Dibayar': ('Terkirim', 'Batal',),
    'Terkirim': ('Barang Diterima', 'Batal',),
    'Barang Diterima': ('Selesai', 'Batal',),
    'Selesai': (),
    'Batal': (),
}

# Currency

OSCAR_DEFAULT_CURRENCY = 'IDR'

# Meta
# ====

OSCAR_SHOP_NAME = 'YooHalal'

OSCAR_SHOP_TAGLINE = 'Hidup Halal'

OSCAR_ALLOW_ANON_CHECKOUT = True

# Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'cs@yoohalal.com'
EMAIL_HOST_PASSWORD = 'tuhanku4JJ'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
OSCAR_FROM_EMAIL = 'Yoohalal<cs@yoohalal.com>'

# Add menu on dashboard
OSCAR_DASHBOARD_NAVIGATION += [
    {
        'label': _('Payment'),
        'icon': 'icon-money',
        'children': [
            {
                'label': _('Bank Transfer'),
                'url_name': 'banktransfer-transaction-list',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
            {
                'label': _('Payment Confirmations'),
                'url_name': 'confirmation-method-list',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
        ]
    },
    {
        'label': _('Blog'),
        'icon': 'icon-rss',
        'children': [
            {
                'label': _('Posts'),
                'url_name': 'post-list',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
            {
                'label': _('Category'),
                'url_name': 'category-list',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
        ]
    },
    {
        'label': _('Career'),
        'icon': 'icon-book',
        'children': [
            {
                'label': _('Career'),
                'url_name': 'career-list',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
            {
                'label': _('Departement'),
                'url_name': 'departement-list',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
            {
                'label': _('Applicant'),
                'url_name': 'applicant-list',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
        ]
    },
    {
        'label': _('Settings'),
        'icon': 'icon-cog',
        'children': [
            {
                'label': _('Slider'),
                'url_name': 'slider-list',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
            {
                'label': _('Social Media'),
                'url_name': 'link-list',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
            {
                'label': _('Subscribe'),
                'url_name': 'subscribe-list',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
        ]
    },
]

# google recaptcha key
GOOGLE_RECAPTCHA_SECRET_KEY = '6LfKLjQUAAAAADr8zve9jB6HSJGoIAvjm0_cE_Ge'

# shipping charge
from decimal import Decimal as D

SHIPPING_REGULER_CHARGE = D('10000')
SHIPPING_EXPRESS_CHARGE = D('18000')

# confirmation images folder
CONFIRMATION_IMAGE_FOLDER = 'images/confirmations/'

# slider images folder
SLIDER_IMAGE_FOLDER = 'images/sliders/'

# The number of products to paginate by
OSCAR_PRODUCTS_PER_PAGE = 21
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 21

# Bank Account
BANK_ACCOUNT_LIST = [
    {
        'label': 'Bank Muamalat',
        'slug': 'muamalat',
        'number': '105 000 5499',
        'name': 'Sukma Wijaya Saputra',
    },
]

# Catalogue produk status
PRODUCT_STATUS = (
    ('draft', _('Draft')),
    ('review', _('Review')),
    ('publish', _('Publish')),
    ('unpublish', _('Unpublish')),
    ('banned', _('Banned')),
)

# confirmation status
CONFIRMATION_STATUS = (
    ('pending', _('Pending')),
    ('reject', _('Reject')),
    ('accept', _('Accept')),
)

# 5MB - 5242880
MAX_UPLOAD_SIZE = 5242880

# career document folder
CAREER_DOCUMENT_FOLDER = 'document/career/'

# ROBOTS 
ROBOTS_USE_SCHEME_IN_HOST = True
ROBOTS_CACHE_TIMEOUT = 60*60*24

# META
META_SITE_PROTOCOL = 'https'
META_SITE_DOMAIN = 'yoohalal.com'
META_SITE_NAME = 'Yoohalal'
#META_FB_APPID = '1799271580104554'
META_USE_SITES = True
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_GOOGLEPLUS_PROPERTIES = True

# OAUTH2 LOGIN
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/accounts/profile/'

#SOCIAL_AUTH_FACEBOOK_KEY = '1799271580104554'
#SOCIAL_AUTH_FACEBOOK_SECRET = 'b94c6edbb574b2cee239fca743a7e2c1'
SOCIAL_AUTH_FACEBOOK_KEY = '1732425450186359'
SOCIAL_AUTH_FACEBOOK_SECRET = '86537fd8c00c0ed27477946b6ea99561'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email', 
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY =  '559529269257-n6vm1d5fbv793m75h9ak2j4g5u7uc1tj.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET =  'BIvjwCSHFWm2TgFKc0L59SIb'