# shoplist/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
# Импортируем RedirectView для простого перенаправления
from django.views.generic import RedirectView

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