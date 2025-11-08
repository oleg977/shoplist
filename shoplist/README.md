# 🛒 ShopList: Витрина товаров для розничной торговли

Сайт для локальных сетей розничной торговли, позволяющий публиковать ассортимент, цены и адреса магазинов для удобного просмотра на мобильных устройствах.

## 🚀 1. Стек технологий

* **Backend:** Django 5.2.7
* **Database:** PostgreSQL (Production), SQLite (Development)
* **Hosting:** Render.com (Production-ready)
* **UI/Frontend:** Bootstrap 5 (Адаптивный дизайн)
* **Environment:** Gunicorn, WhiteNoise, `python-dotenv`

## 📦 2. Установка и запуск проекта

### 2.1. Требования

* Python 3.10+
* Git

### 2.2. Установка

1.  **Клонирование репозитория:**
    ```bash
    git clone [https://github.com/ВАШ_НИК/shoplist.git](https://github.com/ВАШ_НИК/shoplist.git)
    cd shoplist
    ```

2.  **Создание и активация виртуального окружения:**
    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Установка зависимостей:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Настройка переменных окружения:**
    Создайте файл `.env` в корне проекта и добавьте базовые переменные:
    ```
    # .env
    SECRET_KEY='ваш_секретный_ключ'
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    ```

5.  **Миграции и создание суперпользователя:**
    ```bash
    python manage.py makemigrations users products 
    python manage.py migrate
    python manage.py createsuperuser 
    ```

### 2.3. Запуск

```bash
python manage.py runserver