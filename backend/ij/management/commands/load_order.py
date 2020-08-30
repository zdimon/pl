from django.core.management.base import BaseCommand, CommandError
from ij.models import City, UserProfile
from backend.settings import FIXTURE_DIR
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Load orders...')
