from django.core.management.base import BaseCommand, CommandError
from cabinet.models import UserProfile
from course.models import Subscription

class Command(BaseCommand):
  
    def handle(self, *args, **options):
        
        for u in UserProfile.objects.all():
            print('add %s' % u.email)
            try:
                s = Subscription()
                s.email = u.email
                s.is_subscribed = True
                s.save()
            except:
                pass
       