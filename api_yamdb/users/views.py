# from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
# from django.conf import settings
# from django.core import validators
from users.models import User
from users.serializers import UserSerializer
from users.permissions import AdminPermission


class CreateViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    ):
    pass


class UserViewSet(CreateViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AdminPermission, )
