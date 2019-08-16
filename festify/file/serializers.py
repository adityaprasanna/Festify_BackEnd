from rest_framework_mongoengine import serializers
from festify.file.models import File


class FileSerializer(serializers.DocumentSerializer):
    class Meta:
        model = File
        fields = "__all__"
