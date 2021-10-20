from .models import User
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from django.contrib.auth import authenticate, login


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'address',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class LoginSerializers(Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)

    def authenticate_user(self, email, password):
        user = authenticate(email=email, password=password)
        if user is not None:
            return user, True
        else:
            return None, False
