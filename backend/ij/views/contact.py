from ij.models import Contact
from ij.serializers import ContactSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from rest_framework.response import Response

class ContactListView(generics.ListAPIView):
    '''
    
    Contact list.
    
    ____________

    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = ContactSerializer
    queryset = Contact.objects.all().order_by('-id')

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user.userprofile)

class ContactDeleteView(generics.DestroyAPIView):
    '''
    
    Delete contact.
    
    ____________

    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = ContactSerializer
    queryset = Contact.objects.all().order_by('-id')

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != self.request.user.userprofile:
            raise APIException('Not allowed!')
        else:
            self.perform_destroy(obj)
            return Response({'message': 'Deleted!'})
