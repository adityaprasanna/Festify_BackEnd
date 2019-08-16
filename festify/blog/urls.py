from django.urls import path, re_path, include

from festify.blog.views import post_detail

urlpatterns = [
    path('details/', post_detail, name="details"),
]