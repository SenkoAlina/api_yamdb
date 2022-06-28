from rest_framework import serializers
# from rest_framework.validators import UniqueTogetherValidator
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        model = User
