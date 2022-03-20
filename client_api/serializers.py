from .models import *
from rest_framework_mongoengine.serializers import DocumentSerializer


class AdvertSerializer(DocumentSerializer):

    class Meta:
        model = Advert
        depth = 2
        exclude = []
