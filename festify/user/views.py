import json

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_mongoengine import generics

from festify.user.models import CustomUser
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_409_CONFLICT
)

from festify.user.serializers import UserSerializer


class UserLogout(APIView):

    def get(self, request):
        # simply delete the token to force a login
        request.user.auth_token.delete()

        return Response(status=status.HTTP_200_OK)


class UserLogin(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token_key, _ = Token.objects.get_or_create(user=user)
        token = Token.objects.get(key=token_key)
        user = CustomUser.objects.filter(id=token.user_id).values()
        return Response({'token': token.key, 'user': user[0]},
                        status=HTTP_200_OK)


class Users(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)

        existing_user = CustomUser.objects.filter(username=username)
        if len(existing_user) > 0:
            return Response({'error': 'Username ' + username + ' already exists'},
                            status=HTTP_409_CONFLICT)

        serialized = UserSerializer(data=request.data)
        create_user = None
        if serialized.is_valid():
            create_user = CustomUser.objects.create_user(username=username, password=password)
            create_user.set_password(password)
            create_user.save()

        return Response(UserSerializer(instance=create_user).data, status=status.HTTP_201_CREATED)
