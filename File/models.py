from mongoengine import fields, Document, EmbeddedDocument
from utilities.extendedModels import TimeStampedModel


class File(Document, TimeStampedModel):
    """ Model for Fest """

    file_name = fields.StringField(null=False, default=None, required=True)
    file_type = fields.StringField(null=True, default=None)
