from rest_framework import serializers

from Event.models import Event
from Fest.models import Fest
from Organization.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'org_name')


class FestSerializer(serializers.ModelSerializer):
    # fest_events = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # fest_image = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # fest_sponsor = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # fest_coordinator = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    organizers = OrganizationSerializer(many=True, read_only=True)
    # organizers = serializers.SlugRelatedField(
    #     many=True,
    #     queryset=Organization.objects.all(),
    #     slug_field='id'
    # )

    class Meta:
        model = Fest
        fields = ('id', 'organizers')
