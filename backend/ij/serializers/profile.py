from rest_framework import serializers
from ij.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 
                  'publicname',
                  'username', 
                  'phone', 
                  'email', 
                  'telegram', 
                  'skype', 
                  'photo',
                  'is_master',
                  'about']