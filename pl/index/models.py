from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(default='undefined')
    image = models.ImageField(upload_to='pages')

    def __str__(self):
        return self.title