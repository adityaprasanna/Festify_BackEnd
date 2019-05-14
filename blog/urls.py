from django.urls import path, re_path, include
from .views import post_detail


urlpatterns = [
    path('details/', post_detail, name="details"),
]