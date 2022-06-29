# from django.conf import settings
# from django.core import validators
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase

from users.models import User
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer
from users.permissions import AdminPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AdminPermission, )

    @action(methods=['GET', 'PATCH'], detail=False, url_path='me')
    def user_detail_profile(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            print(request.data)
            print(type(request.data))
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_user_profile(self):

        pass


class CustomObtainPairView(TokenViewBase):
    serializer_class = CustomTokenObtainPairSerializer
