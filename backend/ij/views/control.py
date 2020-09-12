from ij.models import Control
from ij.serializers import ControlSerializer
from rest_framework import generics
from ij.filters import ControlCategoryFilter

class ControlListView(generics.ListAPIView):
    '''
    
    Control list.
    
    ____________

    '''
    serializer_class = ControlSerializer
    queryset = Control.objects.all().order_by('-id')
    filterset_class = ControlCategoryFilter
    
