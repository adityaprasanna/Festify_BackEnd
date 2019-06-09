from rest_framework_mongoengine import serializers
from Coordinator.models import Coordinator


def age_restriction(phone_no):
    str_phone = str(phone_no)
    if len(str_phone) != 10:
        raise serializers.serializers.ValidationError("Phone number " + str_phone +
                                                      " invalid. It should be of 10 digits")
    return phone_no


class CoordinatorSerializer(serializers.DocumentSerializer):
    coordinator_phone = serializers.serializers.IntegerField(validators=[age_restriction])

    class Meta:
        model = Coordinator
        fields = '__all__'
