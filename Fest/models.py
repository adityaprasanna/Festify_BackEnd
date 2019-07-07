from AccountDetails.models import AccountDetails
from utilities.extendedModels import TimeStampedModel
from mongoengine import fields, CASCADE, NULLIFY, Document, DynamicDocument, EmbeddedDocument

from Event.models import Event
from File.models import File
from Sponsor.models import Sponsor
from Organization.models import Organization
from Coordinator.models import Coordinator


class Fest(DynamicDocument, TimeStampedModel):
    """ Model for Fest """

    fest_name = fields.StringField(max_length=50, null=False, required=True)
    fest_type_choices = (
        ("Annual", 'Annual'),
        ("Cultural", 'Cultural'),
        ("Commerce", 'Commerce'),
        ("Tech", 'Tech'),
        ("Dance", 'Dance'),
        ("Conference", 'Conference'),
        ("Entrepreneurship", 'Entrepreneurship'),
        ("Literary", 'Literary'),
        ("Media", 'Media')
    )
    fest_type = fields.StringField(max_length=30, default='Annual', choices=fest_type_choices, required=True)
    fest_category_choices = (
        ("Fest", "Fest"),
        ("Single Page Event", "Single Page Event"),
        ("Mun", "Mun"),
    )
    fest_category = fields.StringField(max_length=30, default='Fest', required=True, choices=fest_category_choices)
    fest_venue = fields.StringField(default='')
    fest_description = fields.StringField(default='', required=True)
    fest_start_date = fields.StringField(null=True)
    fest_end_date = fields.StringField(null=True)
    fest_website = fields.URLField(null=True, default='')
    fest_is_live = fields.BooleanField(default=False)

    fest_image = fields.ListField(fields.ReferenceField(File, on_delete=CASCADE, null=False))
    fest_organizer = fields.ReferenceField(Organization, blank=False, on_delete=CASCADE, required=True)
    fest_events = fields.ListField(fields.ReferenceField(Event, blank=False, on_delete=CASCADE))
    fest_sponsor = fields.ListField(fields.ReferenceField(Sponsor, on_delete=NULLIFY, null=True, default=''))
    fest_coordinator = fields.ListField(fields.ReferenceField(Coordinator, on_delete=CASCADE, default=''))
    fest_accountDetails = fields.ListField(fields.ReferenceField(AccountDetails, on_delete=CASCADE, default=''))

    def __str__(self):
        return self.fest_name


class SingleEvent(Document, TimeStampedModel):
    """ Model for Single-Page Event """

    # sevent_name = fields.StringField("event name", max_length=50, default='')
    # sevent_type = fields.StringField(max_length=30, default='')
    # sevent_category = fields.StringField(max_length=30, default='')
    # sevent_description = fields.StringField("event description", default='')
    # sevent_coordinator = fields.StringField("event coordinator", default='')
    # sevent_date = fields.DateTimeField(null=True)
    # sevent_time = fields.TimeField()
    # sevent_amount = fields.DecimalField("ticket price", max_digits=19,
    #                                     decimal_places=10, default=0.0)
    # total_payable = fields.DecimalField("total price", max_digits=19,
    #                                     decimal_places=10, default=0.0)
    # total_slots = fields.IntegerField()
    # available_slots = fields.IntegerField()
    #
    # # sevent_sponsor = fields.ManyToManyField(Sponsor, related_name='fest_sponsor')
    #
    # created = fields.DateTimeField(auto_now_add=True)
    # updated = fields.DateTimeField(auto_now=True)
    #
    # def __str__(self):
    #     return self.sevent_name


class Mun(Document, TimeStampedModel):
    """ Model for MUN """

    # mun_name = fields.StringField("mun name", max_length=50, default='')
    # mun_description = fields.StringField("event description", default='')
    # mun_venue = fields.StringField("venue", max_length=50, default='')
    # mun_coordinator = fields.StringField("event coordinator", default='')
    #
    # start_date = fields.DateTimeField(null=True)
    # end_date = fields.DateTimeField(null=True)
    # mun_time = fields.TimeField()
    #
    # mun_amount = fields.DecimalField("ticket price", max_digits=19,
    #                                  decimal_places=10, default='')
    # total_payable = fields.DecimalField("total price", max_digits=19,
    #                                     decimal_places=10, default='')
    # total_slots = fields.IntegerField()
    # available_slots = fields.IntegerField()
    #
    # # mun_sponsor = fields.ManyToManyField(Sponsor, related_name='fest_sponsor')
    #
    # created = fields.DateTimeField(auto_now_add=True)
    # updated = fields.DateTimeField(auto_now=True)
    #
    # def __str__(self):
    #     return self.mun_name
