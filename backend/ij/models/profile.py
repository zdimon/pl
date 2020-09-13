from django.contrib.auth.models import User
from django.db import models
from decimal import Decimal
from django.utils.safestring import mark_safe

class UserProfile(User):
    publicname = models.CharField(default='', max_length=250)
    account = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    is_online = models.BooleanField(default=False)
    phone = models.CharField(default='', max_length=250, null=True, blank=True)
    telegram = models.CharField(default='', max_length=250, null=True, blank=True)
    skype = models.CharField(default='', max_length=250, null=True, blank=True)
    photo = models.ImageField(upload_to="photos", null=True, blank=True)
    about = models.TextField(default='')
    is_master = models.BooleanField(default=False)

    @property
    def image_tag(self):
        try:
            return mark_safe('<img width="60" src="%s" />' % self.photo.url)
        except:
            return mark_safe('<img width="60" src="/static/images/nophoto.png" />')