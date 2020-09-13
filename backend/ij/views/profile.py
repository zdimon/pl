from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ij.models import UserProfile
from ij.serializers import UserProfileSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class ProfileEditView(generics.UpdateAPIView):
    '''
    
    Update user profile.

    __________________

    '''
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    parser_classes = (MultiPartParser,FormParser)