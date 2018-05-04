from django.urls import path
from apps.users.views import LoginView, UserCreateView

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', UserCreateView.as_view(), name='register'),
]
