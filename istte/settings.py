from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-change-me'

DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ckeditor_5',
    'webapp',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'istte.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'istte.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'istte_db',
        'USER': 'istte_user',
        'PASSWORD': 'David21a',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


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


LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

STATIC_ROOT = BASE_DIR / 'staticfiles'


MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==========================================
# CONFIGURACIÓN DE CKEDITOR 5
# ==========================================

customColorPalette = [
    {'color': 'hsl(4, 90%, 58%)', 'label': 'Rojo'},
    {'color': 'hsl(120, 75%, 60%)', 'label': 'Verde'},
    {'color': 'hsl(209, 88%, 54%)', 'label': 'Azul'},
]


CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading',
            '|',
            'bold',
            'italic',
            'link',
            'bulletedList',
            'numberedList',
            'blockQuote'
        ],
    },

    'extends': {
        'blockToolbar': [
            'paragraph',
            'heading1',
            'heading2',
            'heading3',
            'bulletedList',
            'numberedList',
            'blockQuote',
        ],

        'toolbar': [
            'heading',
            '|',
            'bold',
            'italic',
            'underline',
            'strikethrough',
            'code',
            'subscript',
            'superscript',
            'highlight',
            '|',
            'link',
            'uploadImage',
            'blockQuote',
            'insertTable',
            'mediaEmbed',
            'codeBlock',
            '|',
            'bulletedList',
            'numberedList',
            'todoList',
            '|',
            'undo',
            'redo'
        ],

        'image': {
            'toolbar': [
                'imageTextAlternative',
                'toggleImageCaption',
                'imageStyle:inline',
                'imageStyle:block',
                'imageStyle:side'
            ]
        },

        'table': {
            'contentToolbar': [
                'tableColumn',
                'tableRow',
                'mergeTableCells'
            ]
        },

        'heading': {
            'options': [
                {
                    'model': 'paragraph',
                    'title': 'Párrafo',
                    'class': 'ck-heading_paragraph'
                },
                {
                    'model': 'heading1',
                    'view': 'h1',
                    'title': 'Título 1',
                    'class': 'ck-heading_heading1'
                },
                {
                    'model': 'heading2',
                    'view': 'h2',
                    'title': 'Título 2',
                    'class': 'ck-heading_heading2'
                },
                {
                    'model': 'heading3',
                    'view': 'h3',
                    'title': 'Título 3',
                    'class': 'ck-heading_heading3'
                }
            ]
        }
    }
}