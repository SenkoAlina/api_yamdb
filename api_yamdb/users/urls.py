from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

from .views import UserViewSet

app_name = 'users'

router_v1 = routers.DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')
urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('v1/', include('djoser.urls')),
    # path('v1/', include('djoser.urls.jwt')),
    path(
        'v1/auth/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'refresh-token/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
