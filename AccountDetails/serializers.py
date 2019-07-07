from rest_framework_mongoengine import serializers
from AccountDetails.models import AccountDetails


class AccountDetailsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = AccountDetails
        fields = '__all__'
