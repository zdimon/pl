from ij.models import Offer
from rest_framework import serializers


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'order', 'user', 'desc']

    def save(self, *args, **kwargs): 
        obj = super(OfferSerializer, self).save(*args, **kwargs)
        obj.user = self.context['request'].user.userprofile
        obj.save()
