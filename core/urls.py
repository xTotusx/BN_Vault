"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path
# Importaciones necesarias para servir archivos media en desarrollo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# ESTO ES CRUCIAL: Solo sirve archivos media si DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)