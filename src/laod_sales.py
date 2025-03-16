from pgdb import PGDatabase
import os
import configparser
import pandas as pd
import glob
from datetime import datetime


def is_folder_empty(folder_path):
    # Возвращает True если папка пустая
    return len(os.listdir(folder_path)) == 0


try:
    today = datetime.today().strftime("%Y-%m-%d")

    # Получаем путь к корневой папке проекта
    script_dir = os.path.dirname(os.path.dirname(__file__))

    config = configparser.ConfigParser()
    config_path = os.path.join(script_dir, "config.ini")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Конфигурационный файл не найден: {config_path}")

    config.read(config_path)
    DATABASE_CREDS = config["DATABASE"]

    # Путь к папке с данными теперь в корне проекта
    data_dir = os.path.join(script_dir, "data")

    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Папка с данными не найдена: {data_dir}")

    # Если папка пуста, просто завершаем работу
    if is_folder_empty(data_dir):
        exit(0)

    # Ищем CSV файлы
    files = glob.glob(os.path.join(data_dir, "[0-9]*_[0-9]*.csv"))

    # Создаем подключение к базе данных
    database = PGDatabase(
        host=DATABASE_CREDS["HOST"],
        database=DATABASE_CREDS["DATABASE"],
        user=DATABASE_CREDS["USER"],
        password=DATABASE_CREDS["PASSWORD"],
    )

    for sales_file in files:
        try:
            # Получаем shop и cash из имени файла
            filename = os.path.basename(sales_file)
            shop, cash = filename.replace(".csv", "").split("_")

            # Читаем CSV файл
            df = pd.read_csv(sales_file, encoding="cp1251")

            failed = False
            for i, row in df.iterrows():
                # Преобразуем строковые значения из cp1251 в utf-8
                item = row["item"].encode("cp1251").decode("utf-8")
                category = row["category"].encode("cp1251").decode("utf-8")

                # Формируем запрос, используя параметризацию для предотвращения SQL-инъекций
                query = """
                INSERT INTO sales(dt, store, cash, doc_id, item, category, amount, price, discount)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                params = (
                    today,
                    shop,
                    cash,
                    row["doc_id"],
                    item,
                    category,
                    float(row["amount"]),
                    float(row["price"]),
                    float(row["discount"]),
                )

                if not database.post(query, params):
                    failed = True
                    break

            if not failed:
                # Удаляем файл только если все строки были успешно обработаны
                os.remove(sales_file)

        except Exception:
            continue

except Exception:
    exit(1)
finally:
    if "database" in locals():
        database.close()
