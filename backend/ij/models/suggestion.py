from django.db import models
from ij.models import SubCategory

class Suggestion(models.Model):
    text = models.CharField(max_length=250, default='', unique=True, db_index=True)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.SET_NULL, null=True, blank=True)