from rest_framework_mongoengine.routers import DefaultRouter

from festify.organization import views

router = DefaultRouter()
router.register(r'^v1', views.OrganizationViewSet, basename='organization')
urlpatterns = router.urls
