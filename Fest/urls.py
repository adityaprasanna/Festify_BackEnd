from django.urls import path, re_path, include
from rest_framework_mongoengine.routers import DefaultRouter

from .api import views
from Fest import views as newView


# urlpatterns = [
#
#     # path('home/', views.HomePage.as_view(), name="home"),
#     # path('create/', views.FestCreate.as_view(), name="create"),
#     # path('update/', views.FestUpdate.as_view(), name="update"),
#     # path('delete/', views.FestDelete.as_view(), name="delete"),
#     # path('event/delete/', views.EventDelete.as_view(), name="eventDelete"),
#     # path('sponsor/delete/', views.SponsorDelete.as_view(), name="sponsorDelete"),
#     # path('details/', views.FestDetails.as_view(), name="details"),
#     # path('liked/', views.FestLiked.as_view(), name="liked"),
#
#
#     # path('v2/', v2.FestList.as_view(), name="getAll_create"),
#     # path('v2/<int:pk>', v2.FestDetail.as_view(), name="getAll_create")
#     # path('v2/', v2.Decide.as_view(), name="getAll_create")
# ]


router = DefaultRouter()
router.register(r'^v1', newView.FestViewSet, basename='fest')
urlpatterns = router.urls
