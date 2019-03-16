from django.urls import path, include
from .api import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('dislike/', views.FestDislike.as_view(), name='dislike')
]
