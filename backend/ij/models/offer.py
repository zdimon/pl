from django.db import models
from ij.models import Order, UserProfile

class Offer(models.Model):
    desc = models.TextField(default='')
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    user =  models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)