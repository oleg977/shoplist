from django.contrib import admin  # <--- Эта строка обязательна
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', lambda request: redirect('login'), name='home'),  # временный редирект
]