from rest_framework_mongoengine.routers import DefaultRouter

from Organization import views

router = DefaultRouter()
router.register(r'^v1', views.OrganizationViewSet, basename='organization')
urlpatterns = router.urls
