from django.urls import path, include

from Organization import views

urlpatterns = [
    path('auth/login/', views.OrganizationLogin.as_view(), name="login"),
    path('', views.OrganizationList.as_view(), name="get"),
    path('<int:pk>', views.OrganizationDetail.as_view(), name="put_delete_retrieve"),
    # path('dashboard/', views.OrganizationDashboard.as_view(), name="dashboard")
]
