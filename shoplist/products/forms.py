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

    def clean_shop_addresses(self):
        """
        Опциональная валидация JSON-строки.
        Проверяет, что введённая строка является корректным JSON-массивом строк.
        """
        shop_addresses_str = self.cleaned_data.get('shop_addresses')
        import json
        try:
            addresses = json.loads(shop_addresses_str)
            if not isinstance(addresses, list):
                raise forms.ValidationError('Адреса магазинов должны быть массивом (списком).')
            if not all(isinstance(addr, str) for addr in addresses):
                raise forms.ValidationError('Каждый адрес в списке должен быть строкой.')
        except json.JSONDecodeError:
            raise forms.ValidationError('Введите корректный JSON.')
        return shop_addresses_str