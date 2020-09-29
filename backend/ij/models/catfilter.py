from django.db import models
from ij.models import UserProfile, SubCategory


class CatFilter(models.Model):
    user =  models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=True, blank=True, related_name='user')
    subcategory =  models.ForeignKey(SubCategory,on_delete=models.CASCADE, null=True, blank=True, related_name='contact')
    created_at = models.DateTimeField(auto_now_add=True)