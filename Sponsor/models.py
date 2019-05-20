from django.db import models
from django_extensions.db.models import TimeStampedModel

from File.models import File


class Sponsor(TimeStampedModel):
    """ Fest, Single-Page Events and Mun use this model """

    sponsor_name = models.CharField("event_sponsor_name", max_length=50, blank=True, null=True, default='')
    sponsor_picture = models.OneToOneField(File, blank=True, null=True, on_delete=models.CASCADE,
                                           related_name='sponsor_image')
    sponsor_caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.sponsor_name
