from django.db import models
from django_extensions.db.models import TimeStampedModel

from Event.models import Event
from File.models import File
from Sponsor.models import Sponsor
from Organization.models import Organization


# class FestOld(models.Model):
#     """ Model for Fest """
#
#     organizer = models.ForeignKey(Organization, default='', related_name="fest_yo", on_delete=models.CASCADE)
#     name = models.CharField("fest name", max_length=50, default='')
#     description = models.TextField(default='')
#     fest_type = models.CharField(max_length=30, default='')
#     image = models.TextField()
#     start_date = models.DateTimeField(blank=True, null=True)
#     end_date = models.DateTimeField(blank=True, null=True)
#     website = models.URLField(blank=True, null=True, default='')
#     social_media_pages = models.URLField(blank=True, null=True, default='')
#     promo_video = models.TextField(blank=True, null=True)
#     promo_video_thumbnail = models.TextField(blank=True, null=True,
#                                              help_text='An image that will be used as a thumbnail.')
#
#     events = models.ForeignKey(Event, related_name='fest_events', blank=True, on_delete=models.CASCADE)
#     sponsor = models.ManyToManyField(Sponsor, blank=True, related_name='fest_sponsor')
#
#     """ Fest Manager """
#     manager_name = models.CharField("primary manager name", max_length=50, default='')
#     manager_phone = models.CharField("primary manager contact", max_length=20, default='')
#     manager_email = models.EmailField("primary manager email", default='')
#
#     sec_manager_name = models.CharField("secondary manager name", max_length=50, default='')
#     sec_manager_phone = models.CharField("secondary manager contact", max_length=20, default='')
#
#     """ Account Details of Manager for Payment """
#     account_holder_name = models.CharField("account holder name", max_length=50, default='')
#     account_number = models.CharField("account number", max_length=50, default='')
#     IFSC = models.CharField("IFSC code", max_length=50, default='')
#
#     total_likes = models.IntegerField("total likes", blank=True, null=True)
#     fest_delete = models.BooleanField(default=False)
#
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name


class Fest(TimeStampedModel):
    """ Model for Fest """

    fest_name = models.CharField("fest name", max_length=50, default='')
    fest_type_choices = (
        ("Annual", 'Annual'),
        ("Cultural", 'Cultural'),
        ("Commerce", 'Commerce'),
        ("Tech", 'Tech'),
        ("Dance", 'Dance'),
        ("Conference", 'Conference'),
        ("Entrepreneurship", 'Entrepreneurship'),
        ("Literary", 'Literary'),
        ("Media", 'Media'),
        ("Mun", 'Mun')
    )
    fest_type = models.CharField(max_length=30, default='', blank=True, null=True, choices=fest_type_choices)
    # TODO: Ask Adi about category choices ??
    fest_category = models.CharField(max_length=30, default='')
    fest_venue = models.TextField(default='')
    fest_description = models.TextField(default='')
    fest_start_date = models.DateTimeField(blank=True, null=True)
    fest_end_date = models.DateTimeField(blank=True, null=True)
    fest_website = models.URLField(blank=True, null=True, default='')
    fest_is_live = models.BooleanField(blank=True, default=False)

    fest_image = models.ForeignKey(File, related_name="fest_files", on_delete=models.SET_NULL, null=True)
    fest_organizer = models.ForeignKey(Organization, default='', related_name="fest_organizer",
                                       on_delete=models.CASCADE)
    fest_events = models.ForeignKey(Event, related_name='fest_events', blank=True, on_delete=models.CASCADE)
    fest_sponsor = models.ForeignKey(Sponsor, blank=True, related_name='fest_sponsor', on_delete=models.SET_NULL,
                                     null=True)

    def __str__(self):
        return self.fest_name


class SingleEvent(models.Model):
    """ Model for Single-Page Event """

    sevent_name = models.CharField("event name", max_length=50, default='')
    sevent_type = models.CharField(max_length=30, default='')
    sevent_category = models.CharField(max_length=30, default='')
    sevent_description = models.TextField("event description", default='')
    sevent_coordinator = models.TextField("event coordinator", default='')
    sevent_date = models.DateTimeField(blank=True, null=True)
    sevent_time = models.TimeField()
    sevent_amount = models.DecimalField("ticket price", max_digits=19,
                                        decimal_places=10, default=0.0)
    total_payable = models.DecimalField("total price", max_digits=19,
                                        decimal_places=10, default=0.0)
    total_slots = models.IntegerField()
    available_slots = models.IntegerField()

    # sevent_sponsor = models.ManyToManyField(Sponsor, blank=True, related_name='fest_sponsor')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sevent_name


class Mun(models.Model):
    """ Model for MUN """

    mun_name = models.CharField("mun name", max_length=50, default='')
    mun_description = models.TextField("event description", default='')
    mun_venue = models.CharField("venue", max_length=50, default='')
    mun_coordinator = models.TextField("event coordinator", default='')

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    mun_time = models.TimeField()

    mun_amount = models.DecimalField("ticket price", max_digits=19,
                                     decimal_places=10, default='')
    total_payable = models.DecimalField("total price", max_digits=19,
                                        decimal_places=10, default='')
    total_slots = models.IntegerField()
    available_slots = models.IntegerField()

    # mun_sponsor = models.ManyToManyField(Sponsor, blank=True, related_name='fest_sponsor')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mun_name
