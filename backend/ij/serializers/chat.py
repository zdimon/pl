# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework import serializers
from ij.models import ChatRoom, ChatRoom2User, ChatMessage
from ij.serializers import UserProfileSerializer

class GetRoomRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

class ChatRoomSerializer(serializers.ModelSerializer):
    
    user_list = serializers.SerializerMethodField()
    abonent = serializers.SerializerMethodField()

    def get_user_list(self, obj):
        out = []  
        for u2r in ChatRoom2User.objects.filter(room=obj):
            out.append(UserProfileSerializer(u2r.user).data)
        return out  

    def get_abonent(self, obj):
        return self.context['abonent']
       

    class Meta:
        model = ChatRoom
        fields = [
            'id',
            'token',
            'created_at',
            'user_list',
            'abonent'
        ]

class ChatRoomMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMessage
        fields = [
            'id',
            'user',
            'created_at',
            'message',
            'token',
            'is_readed'
        ]

class GetRoomMessageListSerializer(serializers.Serializer):
    room_id = serializers.IntegerField()
    messages = ChatRoomMessageSerializer(read_only=True, many=True)