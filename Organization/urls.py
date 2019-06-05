from django.urls import path, include

from Organization import views

urlpatterns = [
    path('', views.OrganizationList.as_view(), name="get"),
    path('<int:pk>', views.OrganizationDetail.as_view(), name="put_delete_retrieve"),
]
