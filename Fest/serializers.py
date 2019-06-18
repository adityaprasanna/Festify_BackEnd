from rest_framework_mongoengine import serializers

from Coordinator.serializers import CoordinatorSerializer
from Fest.models import Fest
from Event.serializers import EventSerializer
from File.serializers import FileSerializer
from Organization.serializers import OrganizationSerializer
from Sponsor.serializers import SponsorSerializer


class FestSerializer(serializers.DocumentSerializer):
    fest_events = EventSerializer
    fest_image = FileSerializer
    fest_sponsor = SponsorSerializer
    fest_coordinator = CoordinatorSerializer
    fest_organizer = OrganizationSerializer

    class Meta:
        model = Fest
        fields = "__all__"
