from django.urls import include, path
from rest_framework import routers

from users.views import CustomObtainPairView

from .views import UserViewSet

app_name = 'users'

router_v1 = routers.DefaultRouter()
router_v1.register('users', UserViewSet, basename='user')
router_v1.register(
    r'users(?P<username>[\w.@+-]+)/', UserViewSet, basename='user'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('v1/', include('djoser.urls')),
    path(
        'v1/auth/token/',
        CustomObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
]
