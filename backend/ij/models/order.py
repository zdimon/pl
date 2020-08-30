from django.db import models
from ij.models import SubCategory, Category, UserProfile

class Order(models.Model):
    title = models.CharField(max_length=250, default='')
    desc = models.TextField(default='')
    subcategory = models.ForeignKey(SubCategory,on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)
    user =  models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)