from rest_framework import serializers

from festify.payment.models import Payment
from festify.fest.models import Event

class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
	    model = Payment
	    fields = "__all__"



