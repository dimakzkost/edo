from rest_framework import routers
from django.urls import path, include
from lk.views import lkViewSet, lk

app_name = 'lk'

router = routers.DefaultRouter()
router.register(r'api/v1/lk', lkViewSet, basename='lk')


urlpatterns = [
    path('', include(router.urls)),
    path('lk/', lk, name='lk'),
    ]
