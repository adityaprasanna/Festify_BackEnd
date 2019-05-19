from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from fest.api.serializers import FestSerializer
from fest.models import Fest


class FestList(generics.ListCreateAPIView):
    queryset = Fest.objects.all()
    serializer_class = FestSerializer


class FestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fest.objects.all()
    serializer_class = FestSerializer


# # @csrf_exempt
# class Decide(APIView):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         print(self)
#
#     def get(self, request):
#         # data = JSONParser().parse(request)
#         data = 1
#         print(request.method, data)
#         return FestList.get(self=self, request=request)
#         # return JsonResponse(data, safe=False)
