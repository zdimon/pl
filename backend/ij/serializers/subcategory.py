from rest_framework import serializers
from ij.models import Category, SubCategory 

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name']