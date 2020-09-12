from rest_framework import generics
from ij.models import Order
from ij.serializers import OrderCreateSerializer, OrderListSerializer
from ij.filters import OrderListFilter

class CreateOrderView(generics.CreateAPIView):
    '''
    
    Create a new order.

    __________________

    '''
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def get_serializer(self, *args, **kwargs):
        """
        
        Add the request into serializer context

        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = {'request':self.request }
        return serializer_class(*args, **kwargs)


class OrderListView(generics.ListAPIView):
    '''
    
    Order list.

    __________

    '''
    serializer_class = OrderListSerializer
    queryset = Order.objects.all().order_by('-id')
    filterset_class = OrderListFilter

