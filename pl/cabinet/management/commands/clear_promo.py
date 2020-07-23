from django.core.management.base import BaseCommand, CommandError
from cabinet.models import Promocode

class Command(BaseCommand):
  
    def handle(self, *args, **options):
        print('Clear promo')
        Promocode.objects.all().delete()
       