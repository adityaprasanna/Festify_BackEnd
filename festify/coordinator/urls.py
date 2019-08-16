from rest_framework_mongoengine.routers import DefaultRouter

from festify.coordinator import views


router = DefaultRouter()
router.register(r'^v1', views.CoordinatorViewSet, basename='coordinator')
urlpatterns = router.urls
