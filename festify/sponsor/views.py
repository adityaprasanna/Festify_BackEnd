from rest_framework.permissions import IsAuthenticated
from rest_framework_mongoengine import viewsets

from festify.sponsor.models import Sponsor
from festify.sponsor.serializers import SponsorSerializer


class SponsorViewSet(viewsets.ModelViewSet):
    # this trailing comma is very important without it, it won't work
    # permission_classes = IsAuthenticated,
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)

