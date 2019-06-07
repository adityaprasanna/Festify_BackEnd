import json
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from user.models import CustomUser, UserProfile


class UserLogout(APIView):

    def get(self, request):
        # simply delete the token to force a login
        request.user.auth_token.delete()

        return Response(status=status.HTTP_200_OK)


class UserLogin(APIView):

    def post(self, request):

        # UserProfile.objects.get_or_create(user=get_user)
        requested_data = json.loads(request.body)
        if 'authToken' in requested_data:
            print(requested_data)
        else:
            try:
                username = requested_data['email']
                print(requested_data)
            except:
                Response({"msg":"Error in request data"}, status=status.HTTP_400_BAD_REQUEST)

