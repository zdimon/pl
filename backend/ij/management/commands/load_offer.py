from django.core.management.base import BaseCommand, CommandError
from ij.models import Offer, Order, UserProfile
from ij.utils.order import get_user_token
from backend.settings import DOMAIN
from django.urls import reverse
import requests

from ij.utils.proposition import generate_test_proposition_json

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Load proposition...')
        Offer.objects.all().delete()
        url = '%s%s' % (DOMAIN,reverse('create_offer'))

        ## authorized user
        for user in UserProfile.objects.all():
            headers={'Authorization': 'Token %s' % get_user_token(user)}
            for cnt in range(3):
                order = Order.objects.exclude(user=user).order_by('?')[0]
                data = generate_test_proposition_json(order)
                rez = requests.post(url,json=data,headers=headers)
                print(rez.status_code)   
                print(rez.text)             


