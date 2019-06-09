from mongoengine import fields, Document
from utilities.extendedModels import TimeStampedModel


class File(Document, TimeStampedModel):
    """ Model for Fest """

    file_name = fields.StringField(null=True, default=None)
    file_type = fields.StringField(null=True, default=None)
