from django.db import models
from ij.models import SubCategory, Category, UserProfile, Option, Control

class Order(models.Model):
    title = models.CharField(max_length=250, default='')
    desc = models.TextField(default='')
    subcategory = models.ForeignKey(SubCategory,on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)
    user =  models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    controls = models.ManyToManyField('Control', through='Order2Control')


class Order2Control(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    control = models.ForeignKey(Control,on_delete=models.CASCADE)
    option = models.ForeignKey(Option,on_delete=models.CASCADE, null=True, blank=True)
    value = models.TextField(default='')
