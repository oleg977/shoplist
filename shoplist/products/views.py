# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Product
from .forms import ProductForm


def is_sales_executive_or_admin(user):
    return user.role in ['sales_executive', 'admin'] or user.is_superuser


# ... другие функции (product_list, product_detail, product_create, product_edit) ...

@login_required
@user_passes_test(is_sales_executive_or_admin)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        # Сохраняем имя товара для сообщения
        product_name = product.name
        # Удаляем товар
        product.delete()
        # Показываем сообщение об успешном удалении
        messages.success(request, f'Товар "{product_name}" успешно удалён.')
        # Перенаправляем на страницу со списком товаров
        return redirect('product_list')

    # GET запрос - показываем страницу подтверждения
    return render(request, 'products/product_confirm_delete.html', {'product': product})