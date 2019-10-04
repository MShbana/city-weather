from .views import UserViewSet
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]
