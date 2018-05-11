from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from apps.users.models import User


class UnsupportedError(Exception):
    pass


class LoginSerializer(Serializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data['email'])
            return user
        except User.DoesNotExist:
            return User.objects.create_user(
                email=validated_data['email'],
                username=validated_data['username'],
                password=validated_data['password'],
            )

    def update(self, instance, validated_data):
        raise UnsupportedError('Update not supported!')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'email', 'username']
