from django.db import models
from ij.models import Order, UserProfile
from ij.models.contact import Contact
from ij.models.chat import ChatRoom

class Offer(models.Model):
    desc = models.TextField(default='')
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    user =  models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

from django.db.models.signals import post_save

def keep_track_save(sender, instance, created, **kwargs):
    
    if created:
        # import pdb; pdb.set_trace()
        c = Contact()
        c.owner = instance.user
        c.contact = instance.order.user
        c.save()
        ChatRoom.get_or_create(instance.user,instance.order.user)

post_save.connect(keep_track_save, sender=Offer)