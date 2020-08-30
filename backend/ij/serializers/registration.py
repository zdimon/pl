from rest_framework import serializers
from ij.serializers.profile import UserProfileSerializer

class RegistrationRequestSerializer(serializers.Serializer):
    email = serializers.CharField()


class RegistrationResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserProfileSerializer()