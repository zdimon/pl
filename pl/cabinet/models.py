from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(User):
    publicname = models.CharField(default='',  max_length=250, verbose_name=_(u'ФИО'))
    account = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00), verbose_name=_(u'Счет'))
    phone = models.CharField(default='', max_length=250, verbose_name=_(u'Телефон'))
    telegram = models.CharField(default='', max_length=250, verbose_name=_(u'Телеграм'))
    skype = models.CharField(default='', max_length=250, verbose_name=_(u'Скайп'))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(pk=instance.pk)
