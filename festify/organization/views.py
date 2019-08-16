from rest_framework.permissions import IsAuthenticated

from festify.organization.models import Organization
from festify.organization.serializers import OrganizationSerializer
from rest_framework_mongoengine import viewsets


class OrganizationViewSet(viewsets.ModelViewSet):
    # this trailing comma is very important without it, it won't work
    # permission_classes = IsAuthenticated,
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
