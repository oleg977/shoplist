from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),  # <--- Добавлено
    path('', lambda request: redirect('login'), name='home'),  # временный редирект
]