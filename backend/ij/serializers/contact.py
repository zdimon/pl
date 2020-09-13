from ij.models import Contact
from rest_framework import serializers
from ij.serializers import UserProfileSerializer

class ContactSerializer(serializers.ModelSerializer):
    contact = UserProfileSerializer()
    class Meta:
        model = Contact
        fields = ['id', 'contact']
