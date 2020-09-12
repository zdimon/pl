from ij.models import City
from ij.serializers import CitySerializer
from rest_framework import generics

class CityListView(generics.ListAPIView):
    '''
    
    City list.

    ___________

    '''
    serializer_class = CitySerializer
    queryset = City.objects.all().order_by('-id')

    
