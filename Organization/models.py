from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel
from rest_framework.authtoken.models import Token

from File.models import File
from user.models import CustomUser
from Coordinator.models import Coordinator


class Organization(TimeStampedModel):
    """ Model for organization """

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

    class Meta:
        verbose_name = 'organizer'
        verbose_name_plural = 'organizers'

    def __str__(self):
        return self.name

#
# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if instance.is_organization:
#         Organization.objects.get_or_create(user=instance)
#         token, created = Token.objects.get_or_create(user=instance)
#         print(token.key)
#
#
# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.is_organization:
#         instance.organization_profile.save()
