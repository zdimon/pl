from ij.models import Control
from rest_framework import serializers
from ij.serializers.option import OptionSerializer
from ij.serializers.subcategory import SubCategorySerializer

class ControlSerializer(serializers.ModelSerializer):
    option = OptionSerializer(many=True,source='option_set')
    subcategory = SubCategorySerializer(many=True)
    class Meta:
        model = Control
        fields = ['id', 'name', 'option' ,'subcategory']
