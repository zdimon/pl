from rest_framework import serializers
from ij.models import UserProfile
from ij.serializers.profile import UserProfileSerializer

class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class LoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserProfileSerializer()