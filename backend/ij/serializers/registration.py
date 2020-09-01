from rest_framework import serializers
from ij.serializers.profile import UserProfileSerializer
from ij.models import UserProfile

class RegistrationRequestSerializer(serializers.Serializer):
    email = serializers.CharField()

    def validate_email(self, value):
        """
        Check that the email is unique.
        """
        error = False
        try:
            UserProfile.objects.get(username=value)
            error = True
        except:
            pass

        if error:
            raise serializers.ValidationError("This username is already exists!!!")
        return value


class RegistrationResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserProfileSerializer()