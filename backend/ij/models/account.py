from django.contrib.auth.models import User
from django.db import models
from decimal import Decimal

class UserProfile(User):
    publicname = models.CharField(default='', max_length=250)
    account = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    is_online = models.BooleanField(default=False)
    phone = models.CharField(default='', max_length=250)