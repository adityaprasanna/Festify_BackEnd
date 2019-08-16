from rest_framework_mongoengine import serializers
from festify.organization.models import Organization


class OrganizationSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Organization
        fields = "__all__"
