from rest_framework.permissions import IsAuthenticated
from rest_framework_mongoengine import viewsets

from Coordinator.models import Coordinator
from Coordinator.serializers import CoordinatorSerializer


class CoordinatorViewSet(viewsets.ModelViewSet):
    # this trailing comma is very important without it, it won't work
    # permission_classes = IsAuthenticated,
    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)
