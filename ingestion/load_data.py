import pandas as pd
from sqlalchemy import create_engine
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

customers_path = os.path.join(BASE_DIR, "data", "customers.csv")
products_path = os.path.join(BASE_DIR, "data", "products.csv")
orders_path = os.path.join(BASE_DIR, "data", "orders.csv")

customers = pd.read_csv(customers_path)
products = pd.read_csv(products_path)
orders = pd.read_csv(orders_path)

engine = create_engine("postgresql://postgres:Earthly009#@localhost:5432/ecommerce_db")

customers.to_sql("customers", engine, if_exists="append", index=False)
products.to_sql("products", engine, if_exists="append", index=False)
orders.to_sql("orders", engine, if_exists="append", index=False)

print("✅ Data successfully loaded!")

print(customers_path)