from rest_framework.permissions import IsAuthenticated
from rest_framework_mongoengine import viewsets

from festify.event.models import Event
from festify.event.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    # permission_classes = IsAuthenticated,
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)
