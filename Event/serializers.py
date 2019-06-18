from rest_framework_mongoengine import serializers

from Coordinator.serializers import CoordinatorSerializer
from Event.models import Event
from File.serializers import FileSerializer


class EventSerializer(serializers.DocumentSerializer):
    event_images = FileSerializer
    event_coordinator = CoordinatorSerializer

    class Meta:
        model = Event
        fields = "__all__"
