from django.urls import path
from Event import views

urlpatterns = [
    path('', views.EventList.as_view(), name="get"),
    # path('<int:pk>', views.EventDetail.as_view(), name="put_delete_retrieve"),
    path('<int:pk>', views.EventDetail.trial, name="put_delete_retrieve"),
]
