from rest_framework import generics
from ij.models import Order
from ij.serializers import OrderSerializer

class CreateOrderView(generics.CreateAPIView):
    '''
    Owners photo
    '''
    queryset = Order.objects.all()
    serializer_class = OrderSerializer