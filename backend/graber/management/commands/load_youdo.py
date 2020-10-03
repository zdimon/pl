from django.core.management.base import BaseCommand, CommandError
import json
import requests
import re
from backend.settings import FIXTURE_DIR
from ij.models import Category, SubCategory, Control, Option
from os.path import join, isfile
import sys

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
category_file = join(FIXTURE_DIR,'category.json')
subcategory_file = join(FIXTURE_DIR,'subcategory.json')
controls_file = join(FIXTURE_DIR,'controls.json')

def get_controls():
    url = 'https://youdo.com/js/cacheddata?zone=RU&v=3001360'
    req = requests.get(url, headers=headers)
    result = re.search(r'YouDo\.Global\.CachedData\.CategoriesControls =(.*?)\}\}\]\}\};', req.text)
    tmpstr = result.group(1)
    ready = tmpstr+'}}]}}'
    with open(controls_file,'w') as f:
        f.write(ready)
 
    print('Saving '+controls_file)

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
        Category.objects.create(name=i['Text'],youdo_id=i['Id'],youdo_key=i['Key'])
        print(i['Text'])

def save_subcategory():
    SubCategory.objects.all().delete()
    with open(subcategory_file, 'r') as f:
        strdt = f.read()
    jsdata = json.loads(strdt)
    for i in jsdata:
        cat = Category.objects.get(youdo_id=i['Category'])
        SubCategory.objects.create(name=i['Name'],category=cat, youdo_id=i['Id'])
        print(i['Name'])


def save_controls():
    Control.objects.all().delete()
    with open(controls_file, 'r') as f:
        strdt = f.read()
    jsdata = json.loads(strdt)
    for i in jsdata:  
        cat = Category.objects.get(youdo_key=i)  
        #print(i) 
        #print(jsdata[i]['Controls']) 
        for contrl in jsdata[i]['Controls']:
            
            print('Save...%s' % contrl['Text'])
            try:
                nc = Control.objects.get(alias=contrl['PropertyName'])
            except:
                nc = Control.objects.create( \
                    name = contrl['Text'], \
                    category = cat, \
                    type = contrl['Type'], \
                    alias = contrl['PropertyName']
                )
            for subcat_id in contrl['Subcategories']:
                try:
                    sc = SubCategory.objects.get(youdo_id=subcat_id)
                except:
                    print('Error in searching subcategory')
                nc.subcategory.add(sc)
            try:
                for opt in contrl['Values']:
                    obj = Option()
                    obj.control = nc
                    obj.text = opt['Text']
                    obj.value = opt['Value']
                    obj.input_text = opt['InputText']
                    obj.save()
            except:
                print('No options')

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Grabber')

        if not isfile(subcategory_file):
            get_subcategory()

        if not isfile(category_file):
            get_categories()

        if not isfile(controls_file):
            get_controls()

            
        save_category()
        save_subcategory()
        save_controls()


