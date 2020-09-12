import json
from ij.models import Category, SubCategory, Control, Option, Suggestion, UserProfile
from rest_framework.authtoken.models import Token

def get_user_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token.key
    

def get_rand_control_value(control):
    if control.type == 'Select' or control.type == 'Checkbox':
        rand_val = Option.objects.filter(control=control).order_by('?')[0]
        return {"value": rand_val.value, "control": control.id, "option": rand_val.id}
    return None


def generate_test_order_json(cnt=0):
    random_cat = Category.objects.all().order_by('?')[0]
    random_subcat = SubCategory.objects.filter(category=random_cat).order_by('?')[0]
    ctrls = []
    for ctrl in Control.objects.filter(category=random_cat):
        c = get_rand_control_value(ctrl)
        if c:
            ctrls.append(c)
    try:
        title = Suggestion.objects.filter(subcategory=random_subcat).order_by('?')[0].text
    except:
        title = random_cat.name
    json_data = {
        "title": title, 
        "desc": "Description - %s" % random_subcat.name,
        "category": random_cat.pk,
        "subcategory": random_subcat.pk,
        "controls": ctrls
    }
    if(cnt>0):
        json_data['email']='email%s@google.com' % cnt

    print(json_data)
    return json_data