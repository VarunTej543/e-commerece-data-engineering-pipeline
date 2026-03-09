import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Earthly009#@localhost:5432/ecommerce_db")

# -----------------------------
# Extract
# -----------------------------

customers = pd.read_sql("SELECT * FROM customers", engine)
products = pd.read_sql("SELECT * FROM products", engine)
orders = pd.read_sql("SELECT * FROM orders", engine)

print("Data extracted successfully")

# -----------------------------
# Transform - Data Cleaning
# -----------------------------

customers.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
orders.drop_duplicates(inplace=True)

orders["order_date"] = pd.to_datetime(orders["order_date"])

print("Data cleaned")

# -----------------------------
# Load Dimension Tables
# -----------------------------

customers.to_sql("dim_customers", engine, if_exists="replace", index=False)

products.to_sql("dim_products", engine, if_exists="replace", index=False)

# Date dimension
dim_date = pd.DataFrame()
dim_date["date"] = orders["order_date"]
dim_date["year"] = dim_date["date"].dt.year
dim_date["month"] = dim_date["date"].dt.month
dim_date["day"] = dim_date["date"].dt.day

dim_date.drop_duplicates(inplace=True)

dim_date.to_sql("dim_date", engine, if_exists="replace", index=False)

print("Dimension tables created")

# -----------------------------
# Create Fact Table
# -----------------------------

fact_sales = orders.merge(products, on="product_id")

fact_sales["total_amount"] = fact_sales["quantity"] * fact_sales["price"]

fact_sales = fact_sales[
    [
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "total_amount"
    ]
]

fact_sales.to_sql("fact_sales", engine, if_exists="replace", index=False)

print("Fact table created successfully")