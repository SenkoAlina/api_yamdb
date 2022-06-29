# from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
# from rest_framework.validators import UniqueTogetherValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role', 'password'
        )
        model = User

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Данное имя использовать запрещено!'
            )
        return value


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password']
        self.fields['email'] = serializers.CharField()

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user'] = str(user.username)
        token['confirmation_code'] = str(user.email)
        return token

    def validate(self, attrs):
        user = User.objects.get(
            username=attrs['username'],
            confirmation_code=attrs['confirmation_code']
        )
        return self.get_token(user)
