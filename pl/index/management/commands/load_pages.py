from django.core.management.base import BaseCommand, CommandError
from index.models import Page

class Command(BaseCommand):
  
    def handle(self, *args, **options):
        print('Start command')
        Page.objects.all().delete()
        p = Page()
        p.title = 'title 1'
        p.content = 'content '
        p.save()