from django_filters import FilterSet, CharFilter
from ij.models import Suggestion

class SuggestionFilter(FilterSet):
    text = CharFilter(lookup_expr='contains')

    class Meta:
        model = Suggestion
        fields = ['text']