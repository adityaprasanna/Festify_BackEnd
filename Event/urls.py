from rest_framework_mongoengine.routers import DefaultRouter

from Event import views

router = DefaultRouter()
router.register(r'^v1', views.EventViewSet, basename='event')
urlpatterns = router.urls
