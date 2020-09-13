from ij.models import Offer
from rest_framework import serializers


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'order', 'user', 'desc']

    def save(self, *args, **kwargs): 
        obj = Offer()
        obj.desc = self.validated_data['desc']
        obj.order = self.validated_data['order']
        #obj = super(OfferSerializer, self).save(*args, **kwargs, commit=False)
        obj.user = self.context['request'].user.userprofile
        obj.save()
