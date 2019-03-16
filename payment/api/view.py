import sys
import json

from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# from ..models import Organization
# from user.models import CustomUser
# from fest.models import Fest
from ..models import Payment

from .serializers import (
    PaymentSerializer,
)

class PaymentDetails(ListAPIView):
	""" Participant Details/Booked Ticket Details """
	serializer_class = PaymentSerializer

	def get_queryset(self):
		queryset = Payment.objects.all()
		# queryset = Payment.objects.annotate(foo=True)
		# fest_id = self.request.query_params.get('festid', None)
		# if fest_id is not None:
		# queryset = queryset.filter(id = fest_id)
		return queryset