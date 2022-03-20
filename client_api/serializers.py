from rest_framework import serializers
from .models import *


class AdvertSerializer(serializers.Serializer):
    class Meta:
        model = Advert
        exclude = []
