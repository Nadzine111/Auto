# Sales Data Processing

Проект для автоматизации обработки данных о продажах. Включает генерацию тестовых данных и загрузку их в PostgreSQL базу данных.

## Структура проекта

```
auto/
├── src/                   # Исходный код
│   ├── pgdb.py           # Модуль для работы с базой данных
│   ├── load_sales.py     # Скрипт загрузки данных
│   └── generate_csv.py   # Скрипт генерации CSV файлов
├── data/                  # Папка для CSV файлов
├── config.ini            # Файл конфигурации (необходимо создать)
└── requirements.txt      # Зависимости проекта
```

## Установка

1. Клонируйте репозиторий:
```bash
git clone [URL репозитория]
cd auto
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
venv\Scripts\activate  # для Windows
source venv/bin/activate  # для Linux/Mac
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `config.ini` на основе примера:
```ini
[DATABASE]
HOST = localhost
DATABASE = sales_db
USER = your_user
PASSWORD = your_password

[VARS]
SHOPS = {"1": [1, 2, 3], "2": [1, 2]}
PRODUCTS = {"item": ["Молоко", "Хлеб", "Сыр"], "category": ["Молочка", "Выпечка", "Молочка"], "price": [100, 50, 200]}
```

## Использование

1. Генерация тестовых данных (выполняется по рабочим дням):
```bash
python src/generate_csv.py
```

2. Загрузка данных в базу:
```bash
python src/load_sales.py
```

## База данных

Структура таблицы sales:
```sql
CREATE TABLE sales (
    dt DATE,
    store VARCHAR(10),
    cash VARCHAR(10),
    doc_id VARCHAR(50),
    item VARCHAR(255),
    category VARCHAR(255),
    amount NUMERIC,
    price NUMERIC,
    discount NUMERIC
);
``` 