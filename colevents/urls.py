from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


app_name = ('organization', 'Fest', 'user', 'payment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/fest/', include(('Fest.urls', 'Fest'), namespace='fest')),
    path('api/user/', include(('user.urls', 'user'), namespace='user')),
    path('api/payment/', include(('payment.urls', 'payment'), namespace='payment')),
    path('api/blog/', include(('blog.urls','blog'), namespace='blog')),

    path('api/organization/', include(('Organization.urls', 'Organization'), namespace='organization')),
    path('api/event/', include(('Event.urls','event'), namespace='event')),
    path('api/sponsor/', include(('Sponsor.urls','sponsor'), namespace='sponsor')),
    path('api/coordinator/', include(('Coordinator.urls','coordinator'), namespace='coordinator')),
    path('api/file/', include(('File.urls','file'), namespace='file')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
