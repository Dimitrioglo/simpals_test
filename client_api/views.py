from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from .models import *
from .serializers import *
import requests
import hashlib
import json

SIMPALS_AUTH_TOKEN = 'apuUo-UF6yhfoNVVTKWrb5Z8ecru'


class AdvertViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    serializer_class = AdvertSerializer

    def get_queryset(self):
        return Advert.objects.all()


@api_view(['GET'])
def populate_json(request):
    adverts = get_adverts()
    json_object = json.dumps(adverts, indent=4, ensure_ascii=True)

    with open("user_adverts.json", "w") as outfile:
        outfile.write(json_object)

    return Response({"data": adverts, "message": "Data was stored in file successfully"}, status=200)


@api_view(['GET'])
def populate_database(request):
    adverts = get_adverts()
    for advert in adverts:
        entry_hash = get_object_hash(advert)
        # name change id => advert_id when creating an object, an id in database will be created
        advert['advert_id'] = advert.pop('id')
        advert['entry_hash'] = entry_hash
        serializer = AdvertSerializer(data=advert)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    return Response({"data": adverts, "message": "Data was stored in MongoDB successfully"}, status=200)


@api_view(['GET'])
def up_to_date_mongo_db_view(request):
    adverts = up_to_date_mongo_db()
    return Response({"data": adverts, "message": "Data was updated in MongoDB successfully"}, status=200)


def up_to_date_mongo_db():
    adverts = get_adverts()
    adverts_ids = []
    for advert in adverts:
        entry_hash = get_object_hash(advert)
        advert_id = advert.get('id')
        adverts_ids.append(advert_id)
        db_advert = Advert.objects.filter(advert_id=advert_id).first()
        advert['advert_id'] = advert.pop('id')
        advert['entry_hash'] = entry_hash
        if not db_advert:
            serializer = AdvertSerializer(data=advert)
            serializer.is_valid()
            serializer.save()
        else:
            if db_advert.entry_hash != str(entry_hash):
                # name change id => advert_id when creating an object, an id in database will be created
                serializer = AdvertSerializer(db_advert, data=advert, partial=True)
                serializer.is_valid()
                serializer.save()
    database_adverts = Advert.objects.all()
    # clear old database adverts
    for database_advert in database_adverts:
        if database_advert.advert_id not in adverts_ids:
            database_advert.delete()
    return adverts


def get_adverts():
    url = 'https://partners-api.999.md/adverts'
    adverts = []

    def get_page_and_store(page=1):
        """ iterating through apis with multiple pages """
        query_params = {'page': page}
        response = requests.get(url=url, auth=(SIMPALS_AUTH_TOKEN, ''), params=query_params).json()
        adverts_list = response.get('adverts')
        adverts.extend(adverts_list)
        return get_page_and_store(page=page+1) if adverts_list else response

    get_page_and_store()
    return adverts


def get_object_hash(entry):
    json_entry = json.dumps(entry, sort_keys=True)
    return hashlib.md5(json_entry.encode("utf-8")).hexdigest()
