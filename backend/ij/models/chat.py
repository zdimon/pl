from django.db import models
from ij.models import UserProfile
import uuid 
from rest_framework.authtoken.models import Token

class ChatRoom(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=250,  default='', db_index=True)
    search_key = models.CharField(max_length=250, db_index=True)

    def get_participants(self):
        out = []
        c2us = ChatRoom2User.objects.filter(room=self) 
        for c2u in c2us:
            out.append(c2u.user)
        return out

    @staticmethod
    def get_or_create(user_one, user_two):
        search_key = '%s-%s' % (user_one.id, user_two.id)
        try:
            room = ChatRoom.objects.get(search_key__contains = search_key)
        except:
            search_key = '%s-%s|%s-%s' % (user_one.id, user_two.id, user_two.id, user_one.id)
            room = ChatRoom()
            room.search_key = search_key
            room.token = uuid.uuid1()
            room.save()
            r2u = ChatRoom2User()
            r2u.user = user_one
            r2u.room = room
            r2u.save()
            r2u = ChatRoom2User()
            r2u.user = user_two
            r2u.room = room
            r2u.save()
        return room

class ChatRoom2User(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

class ChatMessage(models.Model):
    token = models.CharField(max_length=250,  default='', db_index=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message =  models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_readed = models.BooleanField(default=False)

