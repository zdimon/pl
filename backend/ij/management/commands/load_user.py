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

        for item in data:
            print(item)
            user = UserProfile()
            user.publicname = item['publicname']
            user.username = item['username']
            user.set_password(item['password'])
            user.save()