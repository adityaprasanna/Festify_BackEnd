from mongoengine import fields, CASCADE, Document
from utilities.extendedModels import TimeStampedModel
from File.models import File


class Sponsor(Document, TimeStampedModel):
    """ Fest, Single-Page Events and Mun use this model """

    sponsor_name = fields.StringField(max_length=50, required=True)
    sponsor_picture = fields.ReferenceField(File, null=True, on_delete=CASCADE)
    sponsor_caption = fields.StringField(max_length=200, null=True)

    def __str__(self):
        return self.sponsor_name
