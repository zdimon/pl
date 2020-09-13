from django.db import models
from ij.models import UserProfile

class Contact(models.Model):
    owner =  models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=True, blank=True, related_name='owner')
    contact =  models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=True, blank=True, related_name='contact')
    created_at = models.DateTimeField(auto_now_add=True)