# products/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price', 'shop_addresses']
        # Указываем виджет для JSONField, чтобы он был более читаемым
        widgets = {
            'shop_addresses': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Введите адреса магазинов в формате JSON, например: ["ул. Ленина, 1", "пр. Мира, 5"]'}),
        }

    # Метод clean_shop_addresses УДАЛЁН, так как он вызывает TypeError
    # при использовании с ModelForm и JSONField.
    # Валидация JSON происходит автоматически на уровне JSONField.