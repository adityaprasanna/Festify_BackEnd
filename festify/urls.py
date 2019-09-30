from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = ('organization', 'fest', 'user', 'payment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/fest/', include(('festify.fest.urls', 'Fest'), namespace='fest')),
    path('api/user/', include(('festify.user.urls', 'user'), namespace='user')),
    path('api/payment/', include(('festify.payment.urls', 'payment'), namespace='payment')),
    path('api/blog/', include(('festify.blog.urls','blog'), namespace='blog')),

    path('api/organization/', include(('festify.organization.urls', 'Organization'), namespace='organization')),
    path('api/event/', include(('festify.event.urls','event'), namespace='event')),
    path('api/sponsor/', include(('festify.sponsor.urls','sponsor'), namespace='sponsor')),
    path('api/coordinator/', include(('festify.coordinator.urls','coordinator'), namespace='coordinator')),
    path('api/accountDetails/', include(('festify.accountDetails.urls','accountDetails'), namespace='accountDetails')),
    path('api/file/', include(('festify.file.urls','file'), namespace='file')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
