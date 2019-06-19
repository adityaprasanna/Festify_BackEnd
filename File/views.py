import json

from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from File.models import File
from File.serializers import FileSerializer
from rest_framework_mongoengine import viewsets

from colevents import settings


class FileViewSet(viewsets.ModelViewSet):
    # this trailing comma is very important without it, it won't work
    # permission_classes = IsAuthenticated,
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        for key, value in kwargs.items():
            print ("%s == %s" %(key, value))
        serializer = self.get_serializer(instance)
        print(serializer)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        uploaded_file = None
        h = None
        try:
            file_list = request.FILES.getlist('file_name')
        except MultiValueDictKeyError:
            return Response(data={"message": "'file' in post parameters form-data not found "},
                            status=status.HTTP_400_BAD_REQUEST)

        if file_list is not None:
            for file in file_list:
                fs = FileSystemStorage(location=settings.UPLOADS_DIR)
                if fs.exists(file.name):
                    fs.delete(file.name)
                fs.save(file.name, file)

                try:
                    uploaded_file = File(file_name='/uploads/' + file.name.replace(" ", "_"), file_type=file.content_type).save()
                    uploaded_file = self.get_serializer(uploaded_file)

                except Exception as e:
                    print(e)
                    return Response({"message": 'Error while uploading, please try again..'},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({"message": "All files upload successfully", "data": uploaded_file.data},
                status=status.HTTP_201_CREATED, content_type="application/json")

        return Response({"message": 'Error while uploading, please try again'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
