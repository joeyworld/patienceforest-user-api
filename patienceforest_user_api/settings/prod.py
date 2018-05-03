import os
from patienceforest_user_api.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['*']
SECRET_KEY = os.environ['PF_USERAPI_SECRET_KEY']
