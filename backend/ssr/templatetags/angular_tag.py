from django import template 
register = template.Library() 

from bs4 import BeautifulSoup
from backend.settings import BASE_DIR
import os
from django.utils.html import mark_safe

@register.simple_tag 
def ng_web_tags(app): 
    path = os.path.join(BASE_DIR, 'static','front_dist',app,'index.html')
    print(path)
    with open(path,'r') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    out_html = ''
    for js in soup.find_all('script'):
        script_item = []
        try:
            type = js['type']
            script_item.append(' type="%s"' % js['type'])
        except:
            pass

        try:
            type = js['defer']
            script_item.append(' defer ')
        except:
            pass

        try:
            type = js['nomodule']
            script_item.append(' nomodule ')
        except:
            pass

        script_item.append('src="%s"' % js['src'])
        out_html = out_html+'<script'+' '.join(script_item)+'></script>'

    return mark_safe(out_html)