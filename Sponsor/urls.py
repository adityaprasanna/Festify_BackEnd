from django.urls import path
from Sponsor import views

urlpatterns = [
    path('', views.SponsorList.as_view(), name="get"),
    path('<int:pk>', views.SponsorDetail.as_view(), name="put_delete_retrieve"),
]
