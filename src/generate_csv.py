import random
import pandas as pd
import configparser
import os
from datetime import datetime

config = configparser.ConfigParser()
# Получаем путь к корневой папке проекта
script_dir = os.path.dirname(os.path.dirname(__file__))
config_path = os.path.join(script_dir, "config.ini")
config.read(config_path)
today = datetime.today()


def generate_doc():
    s = "0123456789qwertyuioplkjhgfdsazxcvbnm"
    doc = ""
    for _ in range(8):
        doc += random.choice(s)
    return doc


def generate_report():
    doc = []
    products = eval(config["VARS"]["PRODUCTS"])
    # для количества чеков в отчете
    for _ in range(random.randint(1, 10)):
        doc_id = generate_doc()
        # для количества строк в чеке
        for _ in range(random.randint(1, 5)):
            # номер товара
            n = random.randint(0, len(products["item"]) - 1)
            ch = (
                doc_id,
                products["item"][n],
                products["category"][n],
                random.randint(1, 5),
                products["price"][n],
                random.randint(0, 3),
            )
            doc.append(ch)
    return doc


shops = eval(config["VARS"]["SHOPS"])
data_dir = os.path.join(script_dir, "data")
os.makedirs(data_dir, exist_ok=True)

if 0 <= today.weekday() <= 5:
    for shop, cash in shops.items():
        for c in cash:
            df = pd.DataFrame(
                generate_report(),
                columns=["doc_id", "item", "category", "amount", "price", "discount"],
            )
            df.to_csv(
                os.path.join(data_dir, f"{shop}_{c}.csv"),
                index=False,
                encoding="cp1251",
            )
