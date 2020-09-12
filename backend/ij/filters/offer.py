from django_filters import FilterSet, NumberFilter, CharFilter
from ij.models import Offer

class OfferOrderFilter(FilterSet):
    order = NumberFilter()
   
    class Meta:
        model = Offer
        fields = ['order']