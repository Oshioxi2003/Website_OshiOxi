"""
URL configuration for oshioxi_backend project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/blog/', include('apps.blog.urls')),
    path('api/v1/services/', include('apps.services.urls')),
    path('api/v1/contact/', include('apps.contact.urls')),
    path('api/v1/pages/', include('apps.pages.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)