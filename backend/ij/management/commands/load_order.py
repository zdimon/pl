from django.core.management.base import BaseCommand, CommandError
from ij.models import City, UserProfile
from backend.settings import FIXTURE_DIR
import json
import requests
from django.urls import reverse
from ij.utils.order import generate_test_order_json
from backend.settings import DOMAIN
from ij.models import Order

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Load orders...')
        Order.objects.all().delete()
        url = '%s%s' % (DOMAIN,reverse('create_order'))
        for i in range(10):
            data = generate_test_order_json()
            rez = requests.post(url,json=data)
            print(rez.status_code)
        #print(rez.text)
