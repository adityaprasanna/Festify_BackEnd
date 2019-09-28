import json

from django.http import JsonResponse
from mongoengine import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from rest_framework import status

from festify.fest.serializers import FestSerializer
from festify.fest.serializers import FestSerializerV2
from festify.fest.models import Fest
from festify.fest.models import FestV2


# class FestList(generics.ListCreateAPIView):
#     queryset = Fest.objects.all()
#     serializer_class = FestSerializer
#
#     def post(self, request, **kwargs):
#         print(request)
#         request_data = request.data
#         serializer = self.get_serializer(data=request_data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return self.get(request)
#
#
# class FestDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Fest.objects.all()
#     serializer_class = FestSerializer


class FestViewSet(viewsets.ModelViewSet):
	# this trailing comma is very important without it, it won't work
	# # permission_classes = IsAuthenticated,
	queryset = Fest.objects.all()
	serializer_class = FestSerializer


"""
	Steps to create Fest
	1. Create Coordinator get id's
	2. Create Organizer pass in the id of 1.
	3. Create Events pass in the id of 1.
	4. Create Sponsor
	if any one of them fails revert and don't create fest
"""


class FestViewSetV2(viewsets.ModelViewSet):
	queryset = FestV2.objects.all()
	serializer_class = FestSerializerV2
	
	# def create(self, request, *args, **kwargs):
	# 	try:
	# 		super().create(request, *args, **kwargs)
	# 		return Response({"message": "adding fest data successfully", "data": FestV2.objects.all()},
	# 		                status=status.HTTP_201_CREATED)
	# 	except Exception as x:
	# 		print(x)
	# 		return Response(data=x.__dict__, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	