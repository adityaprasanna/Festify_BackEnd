# from django_extensions.mongodb.models import TimeStampedModel
from mongoengine import fields, Document
from utilities.extendedModels import TimeStampedModel


class Coordinator(Document, TimeStampedModel):
    coordinator_name = fields.StringField(max_length=30, blank=False, null=False)
    coordinator_phone = fields.IntField(max_length=10, blank=False, null=False)
    coordinator_email = fields.StringField(max_length=10, blank=False, null=False)
