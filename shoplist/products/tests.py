# products/tests.py
import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from decimal import Decimal
import json

# Импорты ваших моделей
from .models import Product

User = get_user_model()

# --- КОНСТАНТЫ РОЛЕЙ И URL ---
ROLE_MANAGER = 'sales_executive'
ROLE_USER = 'user'
# Путь к странице входа из settings.py
LOGIN_URL_PATH = '/users/login/'


# --- КЛАСС НАСТРОЙКИ ---

class ProductTestSetup(TestCase):
    """Базовый класс для настройки тестовых данных и объектов."""

    # Тест обновлён 08.11.2025
    # products/tests.py (Внутри class ProductTestSetup(TestCase): )
    # products/tests.py (Внутри class ProductTestSetup(TestCase): )

    def setUp(self):
        # 1. Создание тестового клиента
        self.client = Client()

        # 2. Создание тестовых пользователей
        self.user_manager = User.objects.create(
            username='manager', email='mgr@test.com', role=ROLE_MANAGER
        )
        self.user_manager.set_password('testpassword')
        self.user_manager.save()

        self.user_regular = User.objects.create(
            username='user', email='user@test.com', role=ROLE_USER
        )
        self.user_regular.set_password('testpassword')
        self.user_regular.save()

        # 🚨 ОБЯЗАТЕЛЬНАЯ ПРОВЕРКА: Создание фиктивного файла
        # Должно быть ТОЛЬКО ЗДЕСЬ, чтобы быть доступным через self.

        # Создаем фиктивный файл для поля ImageField
        image_content = b'R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=='
        self.image_file = SimpleUploadedFile(
            name='test_image.gif',
            content=image_content,
            content_type='image/gif'
        )

        # 3. Создание тестового товара
        self.product = Product.objects.create(
            name="Тестовый Ноутбук X1",
            description="Отличное устройство для работы.",
            price=Decimal('999.99'),
            image=self.image_file,
            shop_addresses=["ул. Ленина, 1", "ул. Мира, 5"],
        )

        # 4. URL-адреса
        self.product_list_url = reverse('product_list')
        self.product_detail_url = reverse('product_detail', args=[self.product.id])
        self.product_create_url = reverse('product_create')
        self.product_delete_url = reverse('product_delete', args=[self.product.id])

        self.login_url = '/users/login/'

        return super().setUp()

        # --- ТЕСТЫ МОДЕЛИ (2/10) ---
        import tempfile


# --- ТЕСТЫ КОНТРОЛЯ ДОСТУПА (5/10) ---

class AccessControlTest(ProductTestSetup):
    # products/tests.py (Внутри class ProductTestSetup(TestCase): )

    def setUp(self):
        # 1. Создание тестового клиента
        self.client = Client()

        # 2. Создание тестовых пользователей
        self.user_manager = User.objects.create(
            username='manager', email='mgr@test.com', role=ROLE_MANAGER
        )
        self.user_manager.set_password('testpassword')
        self.user_manager.save()

        self.user_regular = User.objects.create(
            username='user', email='user@test.com', role=ROLE_USER
        )
        self.user_regular.set_password('testpassword')
        self.user_regular.save()

        # 🚨 ОБЯЗАТЕЛЬНАЯ ПРОВЕРКА: Создание фиктивного файла
        # Должно быть ТОЛЬКО ЗДЕСЬ, чтобы быть доступным через self.

        # Создаем фиктивный файл для поля ImageField
        image_content = b'R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=='
        self.image_file = SimpleUploadedFile(
            name='test_image.gif',
            content=image_content,
            content_type='image/gif'
        )

        # 3. Создание тестового товара
        self.product = Product.objects.create(
            name="Тестовый Ноутбук X1",
            description="Отличное устройство для работы.",
            price=Decimal('999.99'),
            image=self.image_file,
            shop_addresses=["ул. Ленина, 1", "ул. Мира, 5"],
        )

        # 4. URL-адреса
        self.product_list_url = reverse('product_list')
        self.product_detail_url = reverse('product_detail', args=[self.product.id])
        self.product_create_url = reverse('product_create')
        self.product_delete_url = reverse('product_delete', args=[self.product.id])

        self.login_url = '/users/login/'

        return super().setUp()


# --- ТЕСТЫ ОТОБРАЖЕНИЯ (3/10) ---

class ProductViewTest(ProductTestSetup):

    def test_homepage_shows_product_and_price_format(self):
        """Главная страница должна отображать товар с корректным форматом цены."""
        response = self.client.get(self.product_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
        # Ищем формат, который был в вашем HTML
        self.assertContains(response, '999,99')
        self.assertContains(response, 'руб')
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_product_detail_view(self):
        """Страница деталей товара должна отображать информацию."""
        response = self.client.get(self.product_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.description)
        self.assertContains(response, "ул. Ленина, 1")  # Проверка адресов

    def test_product_search_functionality(self):
        """Проверка работы поиска по названию товара."""
        Product.objects.create(name="Пылесос", price=Decimal('100.00'), shop_addresses=[])

        search_url = f"{self.product_list_url}?q=Ноутбук"
        response = self.client.get(search_url)

        self.assertContains(response, "Тестовый Ноутбук X1")
        self.assertNotContains(response, "Пылесос")
