from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema

from ij.models import UserProfile
from ij.serializers import CheckEmailRequestSerializer, CheckEmailResponseSerializer
from email_validator import EmailNotValidError, validate_email

class CheckEmailView(APIView):
    '''

    Check email.

    __________________
    
    '''
    permission_classes = (AllowAny,)
    
    @swagger_auto_schema( 
        request_body = CheckEmailRequestSerializer, \
        responses={'200': CheckEmailResponseSerializer}
        )
    def post(self, request, format=None):
        email = request.data.get('email')
        print(email)
        try:
            validate_email(email)
        except EmailNotValidError as e:
            return Response(CheckEmailResponseSerializer({'status': 1, 'message': 'Wrong email!'}).data)
        
        try:
            user = UserProfile.objects.get(username=email)
            return Response(CheckEmailResponseSerializer({'status': 2, 'message': 'This email exists!'}).data)
        except:
            return Response(CheckEmailResponseSerializer({'status': 0, 'message': 'Ok'}).data)