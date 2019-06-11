from rest_framework_mongoengine.routers import DefaultRouter
from File import views


router = DefaultRouter()
router.register(r'^v1', views.FileViewSet, basename='file')
urlpatterns = router.urls
