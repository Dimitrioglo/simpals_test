from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import *


class AdvertViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


    # def create(self, request, *args, **kwargs):
    #     print('yesss')
    #     return Response({"message": "ok"})








@api_view(['GET'])
def view(request):



    return Response({"message": "YESSSSS"})