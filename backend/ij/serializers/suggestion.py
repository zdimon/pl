from ij.models import Suggestion
from rest_framework import serializers

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ['id', 'text', 'subcategory']
