from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import generics, status


from Event.models import Event
from Event.serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def post(self, request, **kwargs):
        request_data = request.data
        if isinstance(request.data, list):
            for data in request_data:
                serializer = self.get_serializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        return self.get(request)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def func(self, request):
        print(request.query_params.get('festid', None))
        r = EventDetail.get(self, request=request)
        return []
        # return request

    @csrf_exempt
    def trial(request):
        data = JSONParser().parse(request)
        print(request.method, data)

        return JsonResponse(data, safe=False)
