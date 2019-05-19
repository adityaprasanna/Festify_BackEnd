from django.db import models
from django_extensions.db.models import TimeStampedModel

from colevents import settings


class File(TimeStampedModel):
    """ Model for Fest """

    file_name = models.FilePathField("file_name", blank=True, null=True, default=None, path=settings.UPLOADS_DIR)
    file_type = models.CharField("file_type", blank=True, null=True, default='', max_length=25)
