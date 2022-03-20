from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import *

router = DefaultRouter()
router.register(r'adverts', AdvertViewSet, basename='adverts')

urlpatterns = [
    # path('test', view, name='hello')
]

urlpatterns += router.urls
