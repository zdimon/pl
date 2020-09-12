from django_filters import FilterSet, NumberFilter, CharFilter
from ij.models import Order

class OrderListFilter(FilterSet):
    category = NumberFilter()
    subcategory = NumberFilter()
    title = CharFilter(lookup_expr='contains')

    class Meta:
        model = Order
        fields = ['category', 'subcategory']