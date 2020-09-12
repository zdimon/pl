from ij.models import Suggestion
from ij.serializers import SuggestionSerializer 
from rest_framework import generics
from ij.filters import SuggestionFilter

class SuggestionListView(generics.ListAPIView):
    '''
    
    Suggestion list.

    ________________


    '''
    serializer_class = SuggestionSerializer
    queryset = Suggestion.objects.all().order_by('-id')
    filterset_class = SuggestionFilter
    
