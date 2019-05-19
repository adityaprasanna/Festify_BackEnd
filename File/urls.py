from django.urls import path
from File import views

urlpatterns = [
    path('', views.FileList.as_view(), name="get"),
    path('<int:pk>', views.FileDetail.as_view(), name="put_delete_retrieve"),
]
