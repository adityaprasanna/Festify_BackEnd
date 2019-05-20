from django.urls import path
from Coordinator import views

urlpatterns = [
    path('', views.CoordinatorList.as_view(), name="get"),
    path('<int:pk>', views.CoordinatorDetail.as_view(), name="put_delete_retrieve"),
]
