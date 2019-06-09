from rest_framework_mongoengine import serializers
from Event.models import Event


class EventSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Event
        fields = "__all__"
