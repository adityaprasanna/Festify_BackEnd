from rest_framework_mongoengine import serializers

from festify.coordinator.serializers import CoordinatorSerializer
from festify.fest.models import Fest
from festify.event.serializers import EventSerializer
from festify.file.serializers import FileSerializer
from festify.organization.serializers import OrganizationSerializer
from festify.sponsor.serializers import SponsorSerializer


class FestSerializer(serializers.DocumentSerializer):
    fest_events = EventSerializer
    fest_image = FileSerializer
    fest_sponsor = SponsorSerializer
    fest_coordinator = CoordinatorSerializer
    fest_organizer = OrganizationSerializer

    class Meta:
        model = Fest
        fields = "__all__"
