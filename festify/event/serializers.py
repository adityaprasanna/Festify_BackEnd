from rest_framework_mongoengine import serializers

from festify.coordinator.serializers import CoordinatorSerializer
from festify.event.models import Event
from festify.file.serializers import FileSerializer


class EventSerializer(serializers.DocumentSerializer):
    event_images = FileSerializer
    event_coordinator = CoordinatorSerializer

    class Meta:
        model = Event
        fields = "__all__"
