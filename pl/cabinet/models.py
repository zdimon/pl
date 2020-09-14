from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse

class UserProfile(User):
    publicname = models.CharField(default='',  max_length=250, verbose_name=_(u'ФИО'))
    account = models.IntegerField(default=6)
    phone = models.CharField(default='', max_length=250, verbose_name=_(u'Телефон'))
    telegram = models.CharField(default='', max_length=250, verbose_name=_(u'Телеграм'))
    skype = models.CharField(default='', max_length=250, verbose_name=_(u'Скайп'))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        UserProfile.objects.create(pk=instance.pk)

from course.models import Course, LessonPayments

class Promocode(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=_(u'User'), on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(default='', max_length=250, verbose_name=_(u'Код'), unique=True)
    course = models.ForeignKey(Course, verbose_name=_(u'User'), on_delete=models.CASCADE)
    is_activated = models.BooleanField(verbose_name=_('Is activated?'), default=False)

    def get_absolute_url(self):
        return reverse('promo_activate', kwargs={'slug': self.code })

    def activate(self,user):
        for lesson in self.course.lesson_set.all():
            lp = LessonPayments()
            lp.lesson = lesson
            lp.is_paid = True
            lp.user = user
            lp.save()
        self.is_activated = True
        self.save()

class ReplCredit(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=_(u'User'), on_delete=models.CASCADE, null=True, blank=True)
    ammount = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)