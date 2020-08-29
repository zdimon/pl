from django.core.management.base import BaseCommand, CommandError
from ij.models import City
from backend.settings import FIXTURE_DIR

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Load cities...')
        path = FIXTURE_DIR+'/cities.txt'
        City.objects.all().delete()
        with open(path,'r') as f:
            for line in f:
                c = City()
                c.name = line
                c.save()