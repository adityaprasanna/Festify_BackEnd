from rest_framework import serializers
from Coordinator.models import Coordinator


class CoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinator
        fields = "__all__"
