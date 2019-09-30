# from django_extensions.mongodb.models import TimeStampedModel
from mongoengine import fields, Document
from utilities.extendedModels import TimeStampedModel


class AccountDetails(Document, TimeStampedModel):
    account_number = fields.StringField(max_length=30, required=True)
    account_ifsc = fields.StringField(max_length=11, required=True)
    account_bank_name = fields.StringField(max_length=50, required=False, null=True)
    account_holder_name = fields.StringField(max_length=50, required=False, null=True)
