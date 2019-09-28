from mongoengine import fields, NULLIFY, CASCADE, Document
from utilities.extendedModels import TimeStampedModel

from festify.file.models import File
from festify.coordinator.models import Coordinator


class Organization(Document, TimeStampedModel):
    """ Model for organization """
    org_type_choices = (
        ("University", 'University'),
        ("Pre-University", 'Pre-University')
    )
    org_type = fields.StringField(max_length=20, default='University', choices=org_type_choices)
    org_category_choices = (
        ("Arts", 'Arts'),
        ("Medical", 'Medical'),
        ("Engineering", 'Engineering'),
        ("Architecture", 'Architecture'),
        ("Commerce", 'Commerce'),
        ("Law", 'Law'),
        ("Liberal Arts", 'Liberal Arts'),
    )
    org_category = fields.StringField(max_length=20, default='', choices=org_category_choices, required=True)
    org_name = fields.StringField(max_length=20, default='')
    org_address = fields.StringField(default='')
    org_image = fields.ReferenceField(File, on_delete=NULLIFY, null=True)
    org_description = fields.StringField(max_length=120, default='')
    org_website = fields.URLField()

    org_coordinator = fields.ListField(fields.ReferenceField(Coordinator, on_delete=CASCADE, null=True))

    org_is_live = fields.BooleanField(default=False)
    org_user = fields.IntField(null=False, required=True)

    def __str__(self):
        return self.org_name
