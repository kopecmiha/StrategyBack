from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = "username", "email"
        extra_kwargs = {'password': {'write_only': True}}


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = "username", "avatar", "email"
        extra_kwargs = {"email": {'read_only': True}}
