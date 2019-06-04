from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from Organization.models import Organization
from Organization.serializers import OrganizationSerializer
from rest_framework import generics, status


class OrganizationList(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationLogin(APIView):
    """
    POST:
    SignIn/LogIn Organization.
    """

    def post(self, request, format=None):
        userid = request.data['email']
        password = request.data['password']
        user = authenticate(username=userid, password=password)
        if not user:
            return Response({"error": "Login failed"},
                            status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)

        auth_data = {
            "user": user.username,
            "token": token.key
        }

        return Response(auth_data, status=status.HTTP_200_OK)
