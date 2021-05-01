from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import Logout, current_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('current-user/', current_user, name='current_user'),
    url(r'^logout/', Logout.as_view()),
    url(r'^weather/', include('weather.urls')),
]
