from django.core.management.base import BaseCommand, CommandError
from ij.models import UserProfile
from backend.settings import FIXTURE_DIR
import json
from backend.settings import DOMAIN
from django.urls import reverse
import requests
from ij.utils.order import get_user_token
from random import randrange
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Test editing users...')
        
        for user in UserProfile.objects.all():
            url = '%s%s' % (DOMAIN,reverse('profile_edit', kwargs={'pk':user.id}))
            headers={'Authorization': 'Token %s' % get_user_token(user)}
            data = {
                'phone': 'phone edited',
                'email': 'email.edited@gmail.com',
                'telegram': 'telegram-edited',
                'skype': 'skype-edited',
                'about': 'about-edited'
            }
            ## add photo
            filepath = os.path.join(FIXTURE_DIR, 'images','users', '%s.png' % randrange(1,13))
            files = {'photo': open(filepath,'rb')}
            rez = requests.patch(url,data=data,headers=headers, files=files,)
            if rez.status_code != 200:
                print(rez.text)
                raise Exception('Edit user profile Error. Status %s' % rez.status_code)
            else:
                print('User %s was updated with status 200' % json.loads(rez.text)['username'])             
