from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users import views
from .views import UserViewSet

app_name = 'users'

router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('v1/auth/signup/', views.create_user, name='register'),
    path('v1/auth/token/', views.create_token, name='token'),
    path('v1/', include(router_v1.urls))
]
