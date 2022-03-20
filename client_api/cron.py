from .views import up_to_date_mongo_db


def my_scheduled_job():
    up_to_date_mongo_db()
