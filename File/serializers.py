from rest_framework_mongoengine import serializers
from File.models import File


class FileSerializer(serializers.DocumentSerializer):
    class Meta:
        model = File
        fields = "__all__"
