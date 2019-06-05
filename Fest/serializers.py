from rest_framework import serializers
from Fest.models import Fest


class FestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fest
        fields = "__all__"
