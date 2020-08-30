from ij.models import Option
from rest_framework import serializers

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'value', 'input_text']
