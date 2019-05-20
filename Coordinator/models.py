from django.db import models

from django_extensions.db.models import TimeStampedModel


class Coordinator(TimeStampedModel):
    coordinator_name = models.CharField(max_length=30, blank=False, null=False)
    coordinator_phone = models.CharField(max_length=20, blank=False, null=False)
    coordinator_email = models.EmailField(max_length=50, blank=True, null=True)

