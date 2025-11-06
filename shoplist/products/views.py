# products/views.py

from django.shortcuts import render, get_object_or_404
from django.db.models import Q # Импортируем Q для сложных запросов
from .models import Product

# Список товаров с поиском
def product_list(request):
    query = request.GET.get('q') # Получаем значение параметра 'q' из URL
    if query:
        # Фильтруем товары по названию (регистронезависимый поиск)
        products = Product.objects.filter(name__icontains=query)
    else:
        # Если параметра 'q' нет, показываем все товары
        products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'query': query})

# Детали товара
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Получаем товар по ID или возвращаем 404 ошибку
    return render(request, 'products/product_detail.html', {'product': product})