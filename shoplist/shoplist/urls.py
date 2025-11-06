# shoplist/urls.py
from django.contrib import admin
from django.urls import path, include
# Импортируем RedirectView для простого перенаправления
from django.views.generic import RedirectView
# --- НОВОЕ ---
from django.conf import settings
from django.conf.urls.static import static
# --- /НОВОЕ ---

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    # Изменим name='home' на что-то другое
    path('redirect-to-login/', lambda request: redirect('login'), name='login_redirect'),
    # И создадим новую "настоящую" главную страницу, например, перенаправляющую на список товаров
    path('', RedirectView.as_view(url='/products/', permanent=False), name='home'),
    # Или можно создать view для index и указать её: path('', views.index, name='index'),
]

# --- НОВОЕ ---
# Обслуживание медиафайлов только в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# --- /НОВОЕ ---