from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# Вспомогательная функция для проверки роли
def is_sales_executive_or_admin(user):
    return user.role in ['sales_executive', 'admin'] or user.is_superuser

# Список товаров (просматривать может любой)
def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'query': query})

# Детали товара (просматривать может любой)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})
# products/views.py (Обновленные функции)

# ... (Вспомогательная функция is_sales_executive_or_admin остается без изменений) ...


# Создание товара
@login_required
# 🚨 ИСПРАВЛЕНИЕ: Удалено 'raise_exception=True'
@user_passes_test(is_sales_executive_or_admin)
def product_create(request):
    if request.method == 'POST':
        # ... (остальной код) ...
        pass
    else:
        # ... (остальной код) ...
        pass
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Создать товар'})

# Редактирование товара
@login_required
# 🚨 ИСПРАВЛЕНИЕ: Удалено 'raise_exception=True'
@user_passes_test(is_sales_executive_or_admin)
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # ... (остальной код) ...
    pass
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Редактировать товар'})

# Удаление товара
@login_required
# 🚨 ИСПРАВЛЕНИЕ: Удалено 'raise_exception=True'
@user_passes_test(is_sales_executive_or_admin)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # ... (остальной код) ...
    pass
    return render(request, 'products/product_confirm_delete.html', {'product': product})