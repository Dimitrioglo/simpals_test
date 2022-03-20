# Generated by Django 4.0.3 on 2022-03-19 19:31

import client_api.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('republished', models.DateTimeField()),
                ('views_counter', models.IntegerField()),
                ('expire', models.DateTimeField()),
                ('advertid', models.CharField(max_length=40)),
                ('posted', models.DateTimeField()),
                ('block_reasons', djongo.models.fields.ArrayField(model_container=client_api.models.AdvertBlockReasons, model_form_class=client_api.models.AdvertBlockReasonsForm)),
            ],
        ),
    ]
