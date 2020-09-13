from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import generics

from ij.serializers import GetRoomRequestSerializer, ChatRoomSerializer, ChatRoomMessageSerializer
from ij.filters import ChatMessageFilter
# from backend.serializers.noauth import NoAuthSerializer
from ij.models import ChatRoom, ChatMessage
from ij.models import UserProfile

class GetRoomView(APIView):
    '''
    
    Get or create a new chat room.

    ______________________________

    '''

    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        responses={200: ChatRoomSerializer} )
    def get(self, request, user_id):
        user_one = request.user.userprofile
        user_two = UserProfile.objects.get(pk=user_id)
        room = ChatRoom.get_or_create(user_one,user_two)
        # print(user_id)
        return Response(ChatRoomSerializer(room,context={'abonent': user_two.id}).data)

class GetRoomMessageView(generics.ListAPIView):
    '''
    
    Get room messages.

    __________________

    '''
    serializer_class = ChatRoomMessageSerializer
    filterset_class = ChatMessageFilter
    queryset = ChatMessage.objects.all().order_by('-id')


class CreateRoomMessageView(generics.CreateAPIView):
    '''
    
    Create a new message in the room.

    _________________________________

    '''
    queryset = ChatMessage.objects.all()
    serializer_class = ChatRoomMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        room = ChatRoom.objects.get(token=serializer.validated_data['token'])
        serializer.save(user=self.request.user.userprofile, room=room)