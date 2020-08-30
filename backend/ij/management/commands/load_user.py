from django.core.management.base import BaseCommand, CommandError
from ij.models import City, UserProfile
from backend.settings import FIXTURE_DIR
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Load users...')
        path = FIXTURE_DIR+'/users.json'
        UserProfile.objects.all().delete()
        with open(path,'r') as f:
            tmpstr = f.read()
            data = json.loads(tmpstr)

        # admin
        user = UserProfile()
        user.publicname = 'admin'
        user.username = 'admin'
        user.set_password('admin')
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()

        for item in data:
            print('Creating user .... %s' % item['publicname'])
            user = UserProfile()
            user.publicname = item['publicname']
            user.username = item['username']
            user.set_password(item['password'])
            user.save()