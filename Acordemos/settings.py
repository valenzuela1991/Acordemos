import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g-b-oi&r#k#1e$$km1)+3eedljkzsdrtmb2#5w!5v@tg^&0)%n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["acordemos.datoslab.cl","142.93.206.11"]

# Application definition
INSTALLED_APPS = [ 'django.contrib.admin',
                   'django.contrib.auth',
                   'django.contrib.contenttypes',
                   'django.contrib.sessions',
                   'django.contrib.messages',
                   'django.contrib.staticfiles',
                   #mi aplicacion
                    'Apps.Acordemos',
                    # Apps necesaria para ingresar con redes sociales
                   'social_django',
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

ROOT_URLCONF = 'Acordemos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Python Social Auth Context Processors ( Necesaria para logearse con redes sociales)
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'Acordemos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'GestorAcuerdos.sqlite3',
        'USER': 'root',
        'PASSWORD:':'',
        'HOST:':'',
        'PORT:':'',

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

#Modificar el lenguaje a espanol Chile
LANGUAGE_CODE = 'es-cl'

#Modificar el horario a America, Santiago de chile
TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#Backends de autentificacion de Login Gmail
AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication

    'django.contrib.auth.backends.ModelBackend',
)

#Necesario para redirigir al usuario en las autentificaciones
#Utilizadas en el archivo "urls.py" de nuestra aplicacion
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

#ID del Cliente
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '361785313928-ju8i0f53s741fvqhncplgaif9f4l5vjq.apps.googleusercontent.com'
#Secreto de Cliente
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Hi7FMN1GdVHygd7_z_IkA9EF'

#Direccion donde se almacenaran los archivos
MEDIA_ROOT = 'C:\Acordemos\static\media'
MEDIA_URL = '\static/media/'

# Static files (CSS, JavaScript, Images, Archivos en general)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = '/static/'

#Para mandar correo
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'acordemos.app@gmail.com'
EMAIL_HOST_PASSWORD = 'acordemos1234'

STATIC_ROOT = os.path.join(BASE_DIR,'static/')