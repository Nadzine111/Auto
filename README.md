# Sales Data Processing

Проект для автоматизации обработки данных о продажах. Включает генерацию тестовых данных и загрузку их в PostgreSQL базу данных.

## Структура проекта

```
Auto/
├── src/                   # Исходный код
│   ├── pgdb.py           # Модуль для работы с базой данных
│   ├── load_sales.py     # Скрипт загрузки данных
│   └── generate_csv.py   # Скрипт генерации CSV файлов
├── data/                  # Папка для CSV файлов
├── SQL/                   # SQL скрипты
│   └── ddl_sales.sql     # Структура таблицы sales
├── config.ini            # Файл конфигурации
└── requirements.txt      # Зависимости проекта
```

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Nadzine111/Auto
cd Auto
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

### Ручной запуск

1. Генерация тестовых данных:
```bash
python src/generate_csv.py
```

2. Загрузка данных в базу:
```bash
python src/load_sales.py
```

### Автоматический запуск через Планировщик задач Windows

1. Создать 2 файла с расширением .bat в которых нужно указать:
    - путь до питона в виртуальном окружении: /путь до папки с проектом/Auto/venv/Scripts/python.exe
    - путь до запускаемого скрипта:
             /путь до папки с проектом/Auto/src/generate_csv.py 
             или
             /путь до папки с проектом/Auto/src/load_sales.py 

2. Откройте "Планировщик задач Windows" (Task Scheduler)

3. Создайте 2 новые задачи:

   - Общие:
     * Выполнять с наивысшими правами: ✓
     * Выполнять независимо от регистрации пользователя: ✓

   - Триггеры:
     * Создайте расписание по вашим требованиям (например, ежедневно в определенное время)

   - Действия:
     * Программа: `C:\Windows\System32\cmd.exe`
     * Аргументы: `/c "путь до папки с проектом\Auto\generate_data.bat"` или `/c "путь до папки с проектом\Auto\load_data.bat"` 
     * Рабочая папка: `путь до папки с проектом\Auto`

## База данных

Для создания таблицы sales запустите скрипт из файла SQL/ddl_sales.sql. 

Структура таблицы sales:
```sql
CREATE TABLE public.sales (
    id serial4 NOT NULL,
    dt date NULL,
    store varchar(20) NULL,
    cash varchar(20) NULL,
    doc_id varchar(20) NULL,
    item varchar(100) NULL,
    category varchar(30) NULL,
    amount numeric NULL,
    price numeric NULL,
    discount numeric NULL,
    CONSTRAINT sales_pkey PRIMARY KEY (id)
);
``` 