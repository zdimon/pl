from django_filters import FilterSet, NumberFilter
from ij.models import Control

class ControlCategoryFilter(FilterSet):
    category = NumberFilter()

    class Meta:
        model = Control
        fields = ['category']