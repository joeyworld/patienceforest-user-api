from django.urls import path
from api.users.views import LoginView, UserView

app_name = 'users'
urlpatterns = [
    path('', UserView.as_view(), name='user'),
    path('login/', LoginView.as_view(), name='login'),
]
