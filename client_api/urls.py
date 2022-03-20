from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import *

router = DefaultRouter()
router.register(r'adverts', AdvertViewSet, basename='adverts')

urlpatterns = [
    path('populate_json', populate_json, name='populate_json'),
    path('populate_database', populate_database, name='populate_database'),
    path('update_mongodb', up_to_date_mongo_db_view, name='update_mongodb')
]

urlpatterns += router.urls
