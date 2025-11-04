from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')  # Поля, которые будут отображаться в списке товаров
    search_fields = ('name',)  # Поля для поиска
    list_filter = ('price',)  # Фильтры