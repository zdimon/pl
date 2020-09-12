from rest_framework import generics
from ij.models import Offer, Order
from ij.serializers import OfferSerializer
from rest_framework.permissions import IsAuthenticated
from ij.filters import OfferOrderFilter

class CreateOfferView(generics.CreateAPIView):
    '''
    
    Create a new Offer.

    __________________

    '''
    permission_classes = (IsAuthenticated,)
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_serializer(self, *args, **kwargs):
        """
        
        Add the request into serializer context

        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = {'request':self.request }
        return serializer_class(*args, **kwargs)


class UserOfferListView(generics.ListAPIView):
    '''
    
    Offer of the order.

    __________

    '''
    serializer_class = OfferSerializer
    queryset = Offer.objects.all().order_by('-id')
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.userprofile) 

class OrderOfferListView(generics.ListAPIView):
    '''
    
    Propositions of the current user.

    __________

    '''
    serializer_class = OfferSerializer
    queryset = Offer.objects.all().order_by('-id')
    permission_classes = (IsAuthenticated,)
    filterset_class = OfferOrderFilter
