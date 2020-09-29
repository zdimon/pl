from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ij.serializers import NoAuthSerializer
from ij.models import UserProfile, SubCategory, CatFilter

class CatFilterView(APIView):
    '''
    
    Set filter of the subcategories 


    '''

    permission_classes = (IsAuthenticated,)
    def get(self, request, id, format=None):
        user = request.user.userprofile
        subcat = SubCategory.objects.get(pk=id)
        try:
            s2u = CatFilter.objects.get(user=user, subcategory=subcat)
            s2u.delete()
            message = 'Filter was deleted'
        except:
            s2u = CatFilter.objects.create(user=user, subcategory=subcat)
            message = 'Filter was created'
        return Response({'message': message})


        