from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.response import Response

from File.models import File
from File.serializers import FileSerializer
from rest_framework_mongoengine import generics

from colevents import settings


class FileList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def post(self, request, **kwargs):

        try:
            file_list = request.FILES.getlist('file')
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
                    File(file_name='/uploads/' + file.name, file_type=file.content_type).save()
                except Exception:
                    return Response({"message": 'Error while uploading, please try again..'},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({"message": "All files uploaded successfully"}, status=status.HTTP_201_CREATED)

        return Response({"message": 'Error while uploading, please try again'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FileDetail(generics.RetrieveDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
