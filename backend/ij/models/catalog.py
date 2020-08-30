from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250, default='')
    youdo_id = models.IntegerField(default=0)
    youdo_key = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):
    name = models.CharField(max_length=250, default='')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)
    youdo_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'