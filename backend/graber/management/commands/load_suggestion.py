from django.core.management.base import BaseCommand, CommandError
import json
import requests
import re
from backend.settings import FIXTURE_DIR
from ij.models import SubCategory, Suggestion
from os.path import join, isfile
import sys
import os

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
suggestion_dir = join(FIXTURE_DIR,'suggestions')

VAVL = ['а','о','у','е','ы','и','э','о','я','ю']
CONS = ['ц','к','н','г','ш','щ','з','ф','в','п','р','л','д','ж','ч','с','м','б']

def get_suggestion(key):
    url = 'https://youdo.com/api/tasks/suggest/?query=%s' % key
    req = requests.get(url, headers=headers)
    filename = '%s.json' % key
    fpath = join(suggestion_dir,filename)
    with open(fpath,'w') as f:
        f.write(req.text)
    #print('Saving '+fpath)

def save_suggestions():
    for subdir, dirs, files in os.walk(suggestion_dir):
        for file in files:
            print(file)
            fp = join(suggestion_dir,file)
            with open(fp,'r') as f:
                ts = f.read()
            data = json.loads(ts)
            for item in data["ResultObject"]:
                sc = SubCategory.objects.get(youdo_id=item['SubcategoryId'])
                try:
                    Suggestion.objects.create(subcategory=sc,text=item['Text'])
                    print(item['Text'])
                except:
                    print('Exist!!!')

class Command(BaseCommand):

    def handle(self, *args, **options):
        Suggestion.objects.all().delete()
        
        for c in CONS:
            for v in VAVL:
                key = '%s%s' % (c,v)
                filename = '%s.json' % key
                fpath = join(suggestion_dir,filename)
                if not isfile(fpath):
                    print(key)
                    get_suggestion(key)
        save_suggestions()


