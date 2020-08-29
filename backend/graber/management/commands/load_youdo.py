from django.core.management.base import BaseCommand, CommandError
import json
import requests
import re
from backend.settings import FIXTURE_DIR
from ij.models import Category, SubCategory
from os.path import join, isfile

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
category_file = join(FIXTURE_DIR,'category.json')
subcategory_file = join(FIXTURE_DIR,'subcategory.json')

def get_categories():
    url = 'https://youdo.com/js/cacheddata?zone=RU&v=3001360'
    req = requests.get(url, headers=headers)
    result = re.search(r'YouDo\.Global\.CachedData\.Categories =(.*?)\}\}\];', req.text)
    tmpstr = result.group(1)
    ready = tmpstr+'}}]'
    with open(category_file,'w') as f:
        f.write(ready)

    print('Saving '+category_file)

def get_subcategory():
    url = 'https://youdo.com/js/changeabledata?zone=RU'
    req = requests.get(url, headers=headers)
    result = re.search(r'YouDo\.Global\.CachedData\.SubCategories =(.*?)\}\]\}\];', req.text)
    tmpstr = result.group(1)
    ready = tmpstr+'}]}]'
    with open(subcategory_file,'w') as f:
        f.write(ready)
 
    print('Saving '+subcategory_file)

def save_category():
    Category.objects.all().delete()
    with open(category_file, 'r') as f:
        strdt = f.read()
    jsdata = json.loads(strdt)
    for i in jsdata:
        Category.objects.create(name=i['Text'],youdo_id=i['Id'])
        print(i['Text'])

def save_subcategory():
    SubCategory.objects.all().delete()
    with open(subcategory_file, 'r') as f:
        strdt = f.read()
    jsdata = json.loads(strdt)
    for i in jsdata:
        cat = Category.objects.get(youdo_id=i['Category'])
        SubCategory.objects.create(name=i['Name'],category=cat)
        print(i['Name'])
class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Grabber')
        if not isfile(subcategory_file):
            get_subcategory()
        if not isfile(category_file):
            get_categories()
        save_category()
        save_subcategory()


