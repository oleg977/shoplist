from django.urls import path
from . import views

urlpatterns = [
    # Главная страница с товарами
    path('', views.product_list, name='product_list'),

    # Страница деталей товара
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]