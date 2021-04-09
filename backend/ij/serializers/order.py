from ij.models import Order, Order2Control, Option, Control
from rest_framework import serializers
from ij.serializers import ControlSerializer
from ij.utils.account import get_or_create_user_by_email

class Order2ControlSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(read_only=True)
    type = serializers.CharField()
    class Meta:
        model = Order2Control
        fields = ['order', 'control', 'option', 'value', 'type']


class OrderCreateSerializer(serializers.ModelSerializer):
    controls = Order2ControlSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'title', 'desc', 'category', 'subcategory', 'controls', 'email']

    def save(self, *args, **kwargs): 
        # сохраняем заказ
        order = Order()
        order.title = self.validated_data['title']
        order.desc = self.validated_data['desc']
        order.category = self.validated_data['category']
        order.subcategory = self.validated_data['subcategory']

        if self.context['request'].user.is_authenticated:
            order.user = self.context['request'].user.userprofile
        else:
            try:
                user = get_or_create_user_by_email( self.validated_data['email'])
                order.user = user
            except Exception as e:
                print(e)
                import pdb; pdb.set_trace()

        order.save()
        # сохраняем контролы
        for cntrl in self.validated_data['controls']:
            print(cntrl)
            #ctrl = Control.objects.get(pk=cntrl['control'])
            if cntrl['type'] == 'NumericTextbox' or cntrl['type'] == 'Select':
                #import pdb; pdb.set_trace()
                ##opt = Option.objects.get(control=cntrl['control'],value=cntrl['value'])
                o2c = Order2Control()
                o2c.order = order
                o2c.control = cntrl['control']
                o2c.value = cntrl['value']
                o2c.save()
          
            #print(cntrl)

        #import pdb; pdb.set_trace()
        #print(self.validated_data)


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'title', 'desc', 'category', 'subcategory']
