from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  # <-- Here

from Coordinator.models import Coordinator
from Coordinator.serializers import CoordinatorSerializer


class CoordinatorList(generics.ListCreateAPIView):
    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorSerializer

    # this trailing comma is very important witout it it won't work
    # permission_classes = IsAuthenticated,

    def create_and_save(self, data):
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def post(self, request, **kwargs):
        request_data = request.data
        if isinstance(request.data, list):
            for data in request_data:
                self.create_and_save(data)
        else:
            self.create_and_save(request_data)
        return self.get(request)


class CoordinatorDetail(generics.RetrieveUpdateDestroyAPIView):
    # this trailing comma is very important witout it it won't work
    # permission_classes = IsAuthenticated,

    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorSerializer
