from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token

from ij.serializers import  RegistrationRequestSerializer, \
                            RegistrationResponseSerializer, \
                            UserProfileSerializer \

from ij.models import UserProfile

class RegistrationView(APIView):
    '''
    User registration.
    __________________
    '''
    permission_classes = (AllowAny,)
    
    @swagger_auto_schema( 
        request_body = RegistrationRequestSerializer, \
        responses={'200': RegistrationResponseSerializer}
        )
    def post(self, request, format=None):
        print(request.data.get('email'))
        user = UserProfile()
        user.username = request.data.get('email')
        user.set_password('112233')
        user.email = request.data.get('email')
        user.is_active = True
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response( \
            RegistrationResponseSerializer( \
                { 'token':token.key, 'user':UserProfileSerializer(user).data }).data)