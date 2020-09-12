import json
from ij.models import Category, SubCategory, Control, Option

def get_rand_control_value(control):
    if control.type == 'Select' or control.type == 'Checkbox':
        rand_val = Option.objects.filter(control=control).order_by('?')[0]
        return {"value": rand_val.value, "control": control.id, "option": rand_val.id}
    return None


def generate_test_order_json():
    random_cat = Category.objects.all().order_by('?')[0]
    random_subcat = SubCategory.objects.filter(category=random_cat).order_by('?')[0]
    ctrls = []
    for ctrl in Control.objects.filter(category=random_cat):
        c = get_rand_control_value(ctrl)
        if c:
            ctrls.append(c)
    json_data = {
        "title": "Test order", 
        "desc": "Description",
        "category": random_cat.pk,
        "subcategory": random_subcat.pk,
        "controls": ctrls
    }
    print(json_data)
    return json_data