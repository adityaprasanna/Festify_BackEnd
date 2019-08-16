from django.urls import path
# from .api import views
from festify.user import views

urlpatterns = [
    # path('login/', views.UserLogin.as_view(), name='login'),

    path('login/v2/', views.UserLogin.as_view(), name='login_v2'),
    path('logout/v2/', views.UserLogout.as_view(), name='logout_v2'),
    path('create/v1/', views.Users.as_view(), name='create_user'),

    # path('dislike/', views.FestDislike.as_view(), name='dislike')
]
