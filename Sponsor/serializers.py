from rest_framework_mongoengine import serializers
from Sponsor.models import Sponsor


class SponsorSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"
