# from djongo import models
# from django import forms
#
#
# # class AdvertCategoriesCategory(models.Model):
# #     url = models.CharField(max_length=100)
# #     id = models.CharField(max_length=40)
# #     title = models.CharField(max_length=40)
# #
# #     class Meta:
# #         abstract = True
# #
# #
# # class AdvertCategories(models.Model):
# #     category = models.EmbeddedField(
# #         model_container=AdvertCategoriesCategory
# #     )
# #     subcategory = models.EmbeddedField(
# #         model_container=AdvertCategoriesCategory
# #     )
# #
# #     class Meta:
# #         abstract = True
# #
#
#
# class AdvertBlockReasons(models.Model):
#     type = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#
#     class Meta:
#         abstract = True
#
#
# class AdvertBlockReasonsForm(forms.ModelForm):
#     class Meta:
#         model = AdvertBlockReasons
#         fields = (
#             'type', 'title'
#         )
#
#
# class Advert(models.Model):
#     republished = models.DateTimeField()
#     views_counter = models.IntegerField()
#     expire = models.DateTimeField()
#     advertid = models.CharField(max_length=40)
#     # categories = models.EmbeddedField(
#     #     model_container=AdvertCategories
#     # )
#     posted = models.DateTimeField()
#     block_reasons = models.ArrayField(
#         model_container=AdvertBlockReasons,
#         model_form_class=AdvertBlockReasonsForm
#     )
#     options = models.JSONField()


from mongoengine import *

class Page(Document):
    title = StringField(max_length=200, required=True)
    date_modified = DateTimeField()
    options = ListField(IntField)