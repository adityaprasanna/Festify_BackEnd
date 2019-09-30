from utilities.extendedModels import TimeStampedModel
from mongoengine import fields, CASCADE, Document

from festify.file.models import File
from festify.coordinator.models import Coordinator


class Event(Document, TimeStampedModel):
    """ Events under a fest are stored in this model. Not to be confused with Single-Page Event """

    event_name = fields.StringField(max_length=50, required=True)
    event_type = fields.StringField(max_length=30, required=True)
    event_category = fields.StringField(max_length=30, required=True)
    event_description = fields.StringField(required=True)

    event_date_time = fields.StringField(null=True)
    event_venue = fields.StringField(max_length=100, null=True)
    ticket_price = fields.FloatField(max_digits=19, decimal_places=10, default=0.0)
    total_payable = fields.FloatField(max_digits=19,decimal_places=10, default=0.0)
    total_slots = fields.IntField(default=10)
    available_slots = fields.IntField(default=10)

    event_images = fields.ListField(fields.ReferenceField(File, on_delete=CASCADE, null=True))
    # event_coordinator = fields.ListField(fields.ReferenceField(Coordinator,  reverse_delete_rule=CASCADE, null=False))
    event_coordinator = fields.StringField(required=False)

    def __str__(self):
        return self.event_name
