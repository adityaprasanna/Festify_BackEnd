from django.db import models
from django_extensions.db.models import TimeStampedModel

from File.models import File
from Coordinator.models import Coordinator


class Event(TimeStampedModel):
    """ Events under a fest are stored in this model. Not to be confused with Single-Page Event """

    event_name = models.CharField("event_name", max_length=50, blank=False, null=False)
    event_type = models.CharField(max_length=30, default='')
    event_category = models.CharField(max_length=30, default='')
    event_description = models.TextField("event_description", default='')
    event_coordinator = models.ForeignKey(Coordinator, related_name="event_coordinators", on_delete=models.CASCADE,
                                          null=False)
    event_date_time = models.CharField(max_length=20, blank=True, null=True)
    event_venue = models.CharField(max_length=100, blank=True, null=True)
    ticket_price = models.DecimalField("ticket_price", max_digits=19,
                                       decimal_places=10, default=0.0)
    total_payable = models.DecimalField("total_payable", max_digits=19,
                                        decimal_places=10, default=0.0)
    total_slots = models.IntegerField(default=10)
    available_slots = models.IntegerField(default=10)

    event_images = models.ForeignKey(File, related_name="event_files", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.event_name
