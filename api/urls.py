from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('users/', include('api.users.urls', namespace='users')),
    path('dashboard/', include('api.dashboard.urls', namespace='dashboard')),
]
