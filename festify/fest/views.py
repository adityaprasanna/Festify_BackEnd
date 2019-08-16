from rest_framework.permissions import IsAuthenticated
from rest_framework_mongoengine import viewsets

from festify.fest.serializers import FestSerializer
from festify.fest.models import Fest


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
