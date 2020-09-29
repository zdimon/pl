from rest_framework import serializers
from ij.serializers import UserProfileSerializer


class InitSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserProfileSerializer()
    filter = serializers.ListField()