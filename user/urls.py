from django.urls import path, include
from .api import views
from user import views as v2
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('login/v2/', obtain_auth_token, name='login_v2'),
    path('logout/v2/', v2.UserLogout.as_view(), name='logout_v2'),
    path('dislike/', views.FestDislike.as_view(), name='dislike')
]
