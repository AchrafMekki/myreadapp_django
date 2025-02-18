from .base import *
import environs


env = environs.Env()

env.read_env(str(BASE_DIR / '.env'))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str('DB_NAME'),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PWD"),
        #"PORT": env.str("DB_PORT"),
        #"HOST": env.str("DB_HOST")
    }
}
