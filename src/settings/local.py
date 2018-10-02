# Settings for deployment

# These settings are KIT-specific and derive some parts of the settings
# from the directory name.
#
# If you are not deploying on praktomat.cs.kit.edu you need to rewrite this file.

from os.path import join, dirname, basename
import re

# PRAKTOMAT_PATH = dirname(dirname(dirname(__file__)))
PRAKTOMAT_PATH = '/var/www/Praktomat/'

PRAKTOMAT_ID = basename(dirname(PRAKTOMAT_PATH))

MIRROR = False
SITE_NAME = 'Praktomat Lehrstuhl Kesdogan'

# The URL where this site is reachable. 'http://localhost:8000/' in case of the
# developmentserver.
BASE_HOST = 'https://praktomat.itsec.ur.de'
BASE_PATH = '/'

ALLOWED_HOSTS = [ '*' ]

# URL to use when referring to static files.
STATIC_URL = BASE_PATH + 'static/'

STATIC_ROOT = join(dirname(PRAKTOMAT_PATH), "static")

TEST_MAXLOGSIZE=512

TEST_MAXFILESIZE=512

TEST_TIMEOUT=180

# Absolute path to the directory that shall hold all uploaded files as well as
# files created at runtime.

# Example: "/home/media/media.lawrence.com/"
UPLOAD_ROOT = join(dirname(PRAKTOMAT_PATH), "PraktomatSupport/")

SANDBOX_DIR = join('/srv/praktomat/sandbox/', PRAKTOMAT_ID)

ADMINS = [
  ('Praktomat', 'kesdogan.technik@ur.de')
]

SERVER_EMAIL = 'kesdogan.technik@ur.de'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
MAIL_HOST = "localhost"
EMAIL_PORT = 25

DEFAULT_FROM_EMAIL = "praktomat@itsec.ur.de"

DEBUG = MIRROR

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME':   'praktomat_default',
    }
}

# Private key used to sign uploded solution files in submission confirmation email
PRIVATE_KEY = '/srv/praktomat/mailsign/signer_key.pem'

# Enable Shibboleth:
SHIB_ENABLED = False
REGISTRATION_POSSIBLE = True

#SYSADMIN_MOTD_URL = "https://praktomat.itsec.ur.de/sysadmin_motd.html"

# Use a dedicated user to test submissions
USEPRAKTOMATTESTER = True

# Use docker to test submission
USESAFEDOCKER = False

# Various extra files and versions
CHECKSTYLEALLJAR = '/srv/praktomat/contrib/checkstyle-5.7-all.jar'
JPLAGJAR = '/srv/praktomat/contrib/jplag.jar'
#JAVA_BINARY = 'javac-sun-1.7'
#JVM = 'java-sun-1.7'

# Our VM has 4 cores, so lets try to use them
NUMBER_OF_TASKS_TO_BE_CHECKED_IN_PARALLEL = 6

# Finally load defaults for missing setttings.
import defaults
defaults.load_defaults(globals())
