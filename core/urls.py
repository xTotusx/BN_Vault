from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from inventario.views import dashboard_principal
from django.contrib.auth import views as auth_views # <-- Importamos el sistema de login seguro

urlpatterns = [
    # Dashboard Principal
    path('', dashboard_principal, name='dashboard'), 
    
    # --- NUEVAS RUTAS DE LOGIN Y LOGOUT 100% TUYAS ---
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    
    # El panel original (por si lo necesitas para cosas avanzadas)
    path('admin/', admin.site.urls),
    
    # Rutas PWA
    path('manifest.json', TemplateView.as_view(template_name='manifest.json', content_type='application/json'), name='manifest'),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/javascript'), name='sw'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)