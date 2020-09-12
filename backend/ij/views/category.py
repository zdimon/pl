from rest_framework import serializers
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework import viewsets

from ij.models import Category, SubCategory
from ij.serializers import CategorySerializer

class CategoryListView(ListAPIView):
    '''

    List of categories.

    ___________________

    '''
    serializer_class = CategorySerializer
    pagination_class = None

    def get_queryset(self):
        return Category.objects.all().order_by('-id')


class CategoryViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to read and modify categories.
    """   
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  
    http_method_names = ['get', 'post']