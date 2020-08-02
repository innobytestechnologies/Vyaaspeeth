import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '@pzqp#x^+#(olu#wy(6=mi9&a8n+g&x#af#apn07@j=5oin=xb'

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_elasticsearch_dsl',
    'drf_yasg',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'jobsapp',
    'accounts',
    'booking',
    'checkout',
    'stripe',
    'dashboard',
    'contact',
    'crispy_forms',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dal',
    'dal_select2',
    'todo',
    'dashboard_live',
    'contact_live',
    'checkout_live',
    'booking_live',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'jobs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'jobs.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'ghuyhfun',
    #     'USER': 'ghuyhfun',
    #     'PASSWORD': 'ZMp3Pi11S9RJ7DVmovpo2aPo3rYiWlm3',
    #     'HOST': 'baasu.db.elephantsql.com',
    #     'PORT': '5432',
    # }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
# ALLOWED_HOSTS = ['django-portal.herokuapp.com', 'localhost', 'jobs.manjurulhoque.com', '127.0.0.1', 'localhost:3000']
# cors config
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']
SITE_ID = 1
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

AUTH_USER_MODEL = "accounts.user"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/debug.log"),
            "when": "D",  # this specifies the interval
            "interval": 1,  # defaults to 1, only necessary for other values
            "backupCount": 100,  # how many backup file to keep, 10 days
        }
    },
    "loggers": {
        "django": {"handlers": ["file"], "level": "INFO", "propagate": True},
        "project": {"handlers": ["file"], "level": "INFO", "propagate": True},
        "": {"handlers": ["file"], "level": "INFO", "propagate": True},
    },
}

ELASTIC_HOST_NAME = os.environ.get('ELASTIC_HOST_NAME', 'localhost')
ELASTIC_HOST_PORT = os.environ.get('ELASTIC_HOST_PORT', '9200')
# ELASTIC_URL = os.environ.get('ELASTIC_URL', 'http://localhost:9200')


ELASTICSEARCH_DSL = {
    'default': {
        'hosts': ELASTIC_HOST_NAME + ':' + ELASTIC_HOST_PORT,
    },
}

# Documentation
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
}

STRIPE_PUBLISHABLE_KEY='pk_test_yKmlZXk05TQsuCzvKBr7uNJs'
STRIPE_SECRET_KEY ='sk_test_TcuxME2xfjNgdYwzKPFrNYtu'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/' #The url(here HOME) where the user is redirected after logging in.

ACCOUNT_AUTHENTICATION_METHOD = 'username_email' #implies both username ans email are valid for login.
ACCOUNT_CONFIRM_EMAIL_ON_GET =False #email verified or not is not checked when he logs/logged in.
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL #Anonymous user to be redirected fromm emailverification link.
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL =None #Redirect signed in uers to home page.
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_REQUIRED =False #Email not required for signup.
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "mD ecommerce" #default email subject on the verification link email.
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True #when user confirms email,he's automat" logged in.
ACCOUNT_LOGOUT_ON_GET = False #Pompt for asking "ARE you sure to Logout."
ACCOUNT_LOGOUT_REDIRECT_URL ="/" #Where the user is redirected after logging out.

ACCOUNT_SIGNUP_FORM_CLASS =None #Custom field for authentication.
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE =False
ACCOUNT_UNIQUE_EMAIL = True #No 2 accounts can have same email.

ACCOUNT_USER_MODEL_EMAIL_FIELD ="email" #"email" is default, if not: we need custom user model for field where the user inputs his email.
ACCOUNT_USER_MODEL_USERNAME_FIELD ="username"

ACCOUNT_USERNAME_MIN_LENGTH = 6
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE =False #password not shown when typed.
ACCOUNT_PASSWORD_MIN_LENGTH = 6

# Restrict access to ALL todo lists/views to `is_staff` users.
# If False or unset, all users can see all views (but more granular permissions are still enforced
# within views, such as requiring staff for adding and deleting lists).
TODO_STAFF_ONLY = False

# If you use the "public" ticket filing option, to whom should these tickets be assigned?
# Must be a valid username in your system. If unset, unassigned tickets go to "Anyone."
TODO_DEFAULT_ASSIGNEE = 'johndoe'

# If you use the "public" ticket filing option, to which list should these tickets be saved?
# Defaults to first list found, which is probably not what you want!
TODO_DEFAULT_LIST_SLUG = 'tickets'

# If you use the "public" ticket filing option, to which *named URL* should the user be
# redirected after submitting? (since they can't see the rest of the ticket system).
# Defaults to "/"
TODO_PUBLIC_SUBMIT_REDIRECT = 'dashboard'

# Enable or disable file attachments on Tasks
# Optionally limit list of allowed filetypes
TODO_ALLOW_FILE_ATTACHMENTS = True
TODO_ALLOWED_FILE_ATTACHMENTS = [".jpg", ".gif", ".csv", ".pdf", ".zip"]
TODO_MAXIMUM_ATTACHMENT_SIZE = 5000000  # In bytes

# additionnal classes the comment body should hold
# adding "text-monospace" makes comment monospace
TODO_COMMENT_CLASSES = []


from todo.mail.producers import imap_producer
from todo.mail.consumers import tracker_consumer
from todo.mail.delivery import smtp_backend, console_backend

# email notifications configuration
# each task list can get its own delivery method
TODO_MAIL_BACKENDS = {
    # mail-queue is the name of the task list, not the worker name
    "mail-queue": smtp_backend(
        host="smtp.example.com",
        port=465,
        use_ssl=True,
        username="test@example.com",
        password="foobar",
        # used as the From field when sending notifications.
        # a username might be prepended later on
        from_address="test@example.com",
        # additionnal headers
        headers={}
    ),
}

# incoming mail worker configuration
TODO_MAIL_TRACKERS = {
    # configuration for worker "test_tracker"
    "test_tracker": {
        "producer": imap_producer(
            host="imap.example.com",
            username="text@example.com",
            password="foobar",
            # process_all=False, # by default, only unseen emails are processed
            # preserve=False, # delete emails if False
            # nap_duration=1, # duration of the pause between polling rounds
            # input_folder="INBOX", # where to read emails from
        ),
        "consumer": tracker_consumer(
            group="Mail Queuers",
            task_list_slug="mail-queue",
            priority=1,
            task_title_format="[TEST_MAIL] {subject}",
        )
    }
}


VIDEOSTREAM_SIZE = "320x240"

VIDEOSTREAM_THUMBNAIL_SIZE = "320x240"

VIDEOSTREAM_FEED_TITLE = "Video Feeds"

VIDEOSTREAM_FEED_DESCRIPTION = "Video Feeds"

VIDEOSTREAM_FEED_LINK = ""

