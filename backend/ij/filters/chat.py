from django_filters import FilterSet, NumberFilter, CharFilter
from ij.models import ChatMessage


class ChatMessageFilter(FilterSet):
    token = CharFilter()
    class Meta:
        model = ChatMessage
        fields = ['token']