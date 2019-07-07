from rest_framework.permissions import IsAuthenticated
from rest_framework_mongoengine import viewsets

from AccountDetails.models import AccountDetails
from AccountDetails.serializers import AccountDetailsSerializer


class AccountDetailsViewSet(viewsets.ModelViewSet):
    # this trailing comma is very important without it, it won't work
    # permission_classes = IsAuthenticated,
    queryset = AccountDetails.objects.all()
    serializer_class = AccountDetailsSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(viewsets.ModelViewSet, self).get_serializer(*args, **kwargs)
