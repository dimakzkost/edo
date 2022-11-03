from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from edo.view import IndexPageView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include('users.urls')),
    path('', include('lk.urls')),
]
