from django.core.management.base import BaseCommand, CommandError
from ij.models import City, UserProfile
from backend.settings import FIXTURE_DIR
import json
from backend.settings import DOMAIN
from django.urls import reverse
import requests

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Load google users...')
        url = '%s%s' % (DOMAIN,reverse('google_auth'))
        for u in range(5):
            data = {
                'id': u,
                'name': 'user%s' % u,
                'email': 'google%s@gmail.com' % u,
                'photoUrl': 'test%s' % u,
                'firstName': 'test%s' % u,
                'authToken': 'test%s' % u,
                'provider': 'google',
                'socket_id': 'test%s' % u,
            }
            rez = requests.post(url,json=data)
            if rez.status_code != 200:
                raise Exception('Google registration Error')
            else:
                print('User %s was created status 200' % json.loads(rez.text)['user']['username'])             
