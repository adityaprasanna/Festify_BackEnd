from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from Organization.models import Organization
from Organization.serializers import OrganizationSerializer
from rest_framework_mongoengine import viewsets

from user.models import CustomUser
from user.serializers import UserSerializer
from user.views import Users
import rest_framework.request


class OrganizationViewSet(viewsets.ModelViewSet):
    # this trailing comma is very important without it, it won't work
    # permission_classes = IsAuthenticated,
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    # def create(self, request, *args, **kwargs):
    #     requested_data = json.loads(request.body)
    #     username = requested_data['username']
    #     password = requested_data['password']
    #
    #     # auth_token = str(request.META.get("HTTP_AUTHORIZATION")).replace("Token ", "")
    #     # token  = Token.get(auth_token)
    #     # print(auth_token)
    #
    #     # print(requested_data['org_user'])
    #     # print(request.headers['User-Agent'])
    #     # Users.post(request, *args, **kwargs)
    #     # user = CustomUser.objects.filter(username=username)
    #     # if len(user) > 0:
    #     #     return Response({"message": "Username " + username + " already taken"}, status=status.HTTP_400_BAD_REQUEST)
    #     #
    #     # manager = get_user_model()._default_manager
    #     # print(manager)
    #     # user = manager.create_superuser(username, password)
    #
    #     if username is None or password is None:
    #         return Response({'error': 'Please provide both username and password'},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #
    #     existing_user = CustomUser.objects.filter(username=username)
    #     if len(existing_user) > 0:
    #         return Response({'error': 'Username ' + username + ' already exists'},
    #                         status=status.HTTP_409_CONFLICT)
    #
    #     serialized = UserSerializer(data=request.data)
    #     if serialized.is_valid():
    #         create_user = CustomUser.objects.create_user(username=username, password=password)
    #         create_user.set_password(password)
    #         create_user.save()
    #
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
