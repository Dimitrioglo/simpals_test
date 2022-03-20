from mongoengine import *


class CategoriesChild(EmbeddedDocument):
    url = StringField()
    id = StringField()
    title = StringField()


class Categories(EmbeddedDocument):
    category = EmbeddedDocumentField(CategoriesChild)
    subcategory = EmbeddedDocumentField(CategoriesChild)


class BlockReasons(EmbeddedDocument):
    type = StringField()
    title = StringField()


class AutoRepublisherInfo(EmbeddedDocument):
    daily_price = StringField(null=True)
    next_republish_date = DateTimeField(null=True)


class AutoRepublisher(EmbeddedDocument):
    info = EmbeddedDocumentField(AutoRepublisherInfo)
    interval = IntField()
    enabled = BooleanField()
    weekdays = ListField(IntField())
    times = ListField(StringField())
    from_hour = IntField()
    to_hour = IntField()


class Advert(Document):
    republished = DateTimeField()
    views_counter = IntField()
    expire = DateTimeField()
    advert_id = StringField()
    categories = EmbeddedDocumentField(Categories)
    posted = DateTimeField()
    block_reasons = ListField(EmbeddedDocumentField(BlockReasons))
    autorepublisher = EmbeddedDocumentField(AutoRepublisher)
    title = StringField()
    state = StringField()
    type = StringField()
    entry_hash = StringField()