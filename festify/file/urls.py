from rest_framework_mongoengine.routers import DefaultRouter

from festify.file import views

router = DefaultRouter()
router.register(r'^v1', views.FileViewSet, basename='file')
urlpatterns = router.urls
