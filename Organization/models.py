from django.db import models
from django_extensions.db.models import TimeStampedModel

from File.models import File
from Coordinator.models import Coordinator


class Organization(TimeStampedModel):
    """ Model for organization """
    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    org_type = models.CharField("organization_type", max_length=20, default='')
    org_category = models.CharField("organization_category", max_length=20, default='')
    org_name = models.CharField("organization_name", max_length=20, default='')
    org_address = models.TextField("organization_address", default='')
    org_image = models.ForeignKey(File, related_name="org_files", on_delete=models.SET_NULL, null=True)
    org_description = models.TextField("organization_description", max_length=120, default='')
    org_website = models.URLField()

    org_coordinator = models.ForeignKey(Coordinator, related_name="org_coordinators", on_delete=models.CASCADE,
                                        null=True)

    org_isLive = models.BooleanField(default=False)

    def __str__(self):
        return self.org_name
