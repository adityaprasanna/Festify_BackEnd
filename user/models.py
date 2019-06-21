from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_extensions.db.models import TimeStampedModel


class CustomUser(AbstractUser):
    is_normaluser = models.BooleanField(default=True)
    is_organization = models.BooleanField(default=True)


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                related_name='user_profile')

    social_auth_login_choices = (
        ('Google', 'Google'),
        ('Facebook', 'Facebook'),
    )
    social_auth_login_type = models.CharField(
        max_length=10,
        choices=social_auth_login_choices,
        blank=True,
        default='',
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        if self.user.first_name:
            return '{self.user.first_name} {self.user.last_name}'.format(
                self=self).strip()
        return self.user.email


# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if instance.is_normaluser:
#         UserProfile.objects.get_or_create(user=instance)
#
#
# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.is_normaluser:
#         instance.user_profile.save()
