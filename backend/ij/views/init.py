from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from ij.models import CatFilter
from ij.serializers import InitSerializer
from ij.serializers import NoAuthSerializer

class InitView(APIView):
    '''
    
    Initialization request.

    Runs after initialisation of the Angular app (APP_INITIALIZER) or F5.

    Returns data about authorized user. 


    '''

    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        responses={200: InitSerializer, 401: NoAuthSerializer} )
    def get(self, request, format=None):
        token, created = Token.objects.get_or_create(user=request.user)
        filter = []
        for it in CatFilter.objects.filter(user=request.user.userprofile):
            filter.append(it.subcategory.id)
        data = {
            'token': token.key,
            'user': request.user.userprofile,
            'filter': filter

        }
        return Response(InitSerializer(data).data)


        