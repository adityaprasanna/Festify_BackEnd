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
from fest.models import Event

from .serializers import (
    PaymentSerializer,
)

# class PaymentDetails(ListAPIView):
# 	""" Participant Details/Booked Ticket Details """
# 	serializer_class = PaymentSerializer

# 	def get_queryset(self):
# 		queryset = Payment.objects.all()
# 		fest_id = self.request.query_params.get('festid', None)
# 		if fest_id is not None:
# 		    queryset = queryset.filter(id = fest_id)
# 		ticket_booked_data = []
# 		for obj in queryset:
# 			get_event = Event.objects.get(id = obj.fest_id)
# 			event = {
# 				"id": get_event.id,
# 				"name": get_event.event_name,
# 				"ticket_price": get_event.ticket_price,
# 				# "booking_date": obj.created.strftime('%Y-%m-%d'),
# 			}
# 			ticket_booked_data.append(event)
# 		result_set = {
#             "queryset": queryset,
#             "booking_info": ticket_booked_data,
#         }
# 		return result_set

# class PaymentDetails(ListAPIView):
# 	""" Participant Details/Booked Ticket Details """
# 	serializer_class = PaymentSerializer

# 	def get_queryset(self):
# 		paymentset = Payment.objects.all()
		
# 		fest_id = self.request.query_params.get('festid', None)
# 	    	queryset = paymentset.filter(id = fest_id)
# 		print(queryset)
# 		payment_details_list = []
# 		for pay_obj in queryset:
# 			get_payment = Payment.objects.get(id = pay_obj.id)
# 			get_event = Event.objects.get(id=pay_obj.event_id)
# 			payment = {
# 				"id": get_payment.id,
# 				"first_name": get_payment.first_name,
# 				"last_name": get_payment.last_name,
# 				"email": get_payment.email,
# 				"phone": get_payment.phone,
# 				"login_type": get_payment.login_type,
# 				"fest_id": get_payment.fest_id,
# 				"event_id": get_payment.event_id,
# 				"event_name": get_event.event_name,
# 				"org_id": get_payment.org_id,
# 				"amount": get_payment.amount,
# 				"transaction_id": get_payment.transaction_id,
# 				"status": get_payment.status,
# 				"created": get_payment.created,
# 				"updated": get_payment.updated,
# 			}
# 			payment_details_list.append(payment)
# 		print(payment_details_list)

		# ticket_event_details = []
		# for obj in queryset:
		# 	eventset = Event.objects.id(id = obj.event_id)
		# 	event = {
		# 		"id": eventset.id,
		# 		"name": eventset.event_name,
		# 		"ticket_price": eventset.ticket_price,
		# 		"booking_date": obj.created.strftime('%Y-%m-%d'),
		# 	}
		# ticket_event_details.append(event)
		# result_set = {
		# 	"payment": payment_details_list,
		# }
		# return result_set

class PaymentDetails(ListAPIView):
	""" Participant Details/Booked Ticket Details """
	serializer_class = PaymentSerializer

	def get_queryset(self):
		queryset = Payment.objects.all()
		fest_id = self.request.query_params.get('festid', None)
		if fest_id is not None:
		    queryset = queryset.filter(id = fest_id)
		return queryset