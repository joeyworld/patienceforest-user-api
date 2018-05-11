import os
from shutil import copyfile
from patienceforest_user_api.settings.base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = os.environ['PF_USERAPI_SECRET_KEY']

src = os.path.join(BASE_DIR, 'db.sqlite3')
dist = '/tmp/db.sqlite3'
copyfile(src, dist)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': dist
    }
}
