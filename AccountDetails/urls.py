from rest_framework_mongoengine.routers import DefaultRouter

from AccountDetails import views


router = DefaultRouter()
router.register(r'^v1', views.AccountDetailsViewSet, basename='accountDetails')
urlpatterns = router.urls
