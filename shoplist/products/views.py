from django.shortcuts import render, get_object_or_404
from .models import Product

# Список товаров
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Детали товара
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Получаем товар по ID или возвращаем 404 ошибку
    return render(request, 'products/product_detail.html', {'product': product})