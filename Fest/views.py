from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from Fest.serializers import FestSerializer
from Fest.models import Fest


class FestList(generics.ListCreateAPIView):
    queryset = Fest.objects.all()
    serializer_class = FestSerializer

    def post(self, request, **kwargs):
        print(request)
        request_data = request.data
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return self.get(request)


class FestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fest.objects.all()
    serializer_class = FestSerializer
