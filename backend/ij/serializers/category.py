from rest_framework import serializers
from ij.models import Category, SubCategory
from .subcategory import SubCategorySerializer

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    subcategory = serializers.SerializerMethodField()

    def get_subcategory(self,obj):
        out = []
        for item in SubCategory.objects.filter(category=obj):
            out.append(SubCategorySerializer(item).data)
        return out

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategory']