from mongoengine import fields, NULLIFY, CASCADE, Document
from utilities.extendedModels import TimeStampedModel
from File.models import File
from Coordinator.models import Coordinator


class Organization(Document, TimeStampedModel):
    """ Model for organization """
    org_type = fields.StringField(max_length=20, default='')
    org_category = fields.StringField(max_length=20, default='')
    org_name = fields.StringField(max_length=20, default='')
    org_address = fields.StringField(default='')
    org_image = fields.ReferenceField(File, on_delete=NULLIFY, null=True)
    org_description = fields.StringField(max_length=120, default='')
    org_website = fields.URLField()

    org_coordinator = fields.ReferenceField(Coordinator, on_delete=CASCADE, null=True)

    org_isLive = fields.BooleanField(default=False)

    def __str__(self):
        return self.org_name
