from patienceforest_user_api.settings.base import *

DEBUG = False
ALLOWED_HOSTS = [
    'b5tdgv7v9a.execute-api.ap-northeast-2.amazonaws.com'
]
SECRET_KEY = os.environ['PF_USERAPI_SECRET_KEY']
