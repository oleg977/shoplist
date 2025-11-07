# shoplist/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.views.generic import RedirectView
from django.conf import settings # <--- Убедись, что импортирован
from django.conf.urls.static import static # <--- Убедись, что импортирован
# ...

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    # Изменим name='home' на что-то другое
    path('redirect-to-login/', lambda request: redirect('login'), name='login_redirect'),
    # И создадим новую "настоящую" главную страницу, например, перенаправляющую на список товаров
    path('', RedirectView.as_view(url='/products/', permanent=False), name='home'),
]

# --- ЭТА СТРОКА ОБЯЗАТЕЛЬНА ДЛЯ ЛОКАЛЬНОГО ОТЛАЖИВАНИЯ МЕДИАФАЙЛОВ ---
if settings.DEBUG: # <--- Убедись, что условие settings.DEBUG стоит
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# --- /ЭТА СТРОКА ---