from rest_framework import serializers


class CheckEmailRequestSerializer(serializers.Serializer):
    email = serializers.CharField()

class CheckEmailResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    status = serializers.IntegerField()