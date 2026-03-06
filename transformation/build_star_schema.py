import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Earthly009#@localhost:5432/ecommerce_db")

# Load raw tables
customers = pd.read_sql("SELECT * FROM customers", engine)
products = pd.read_sql("SELECT * FROM products", engine)
orders = pd.read_sql("SELECT * FROM orders", engine)

# -----------------------------
# Dimension Table: Customers
# -----------------------------
dim_customers = customers.copy()

dim_customers.to_sql(
    "dim_customers",
    engine,
    if_exists="replace",
    index=False
)

# -----------------------------
# Dimension Table: Products
# -----------------------------
dim_products = products.copy()

dim_products.to_sql(
    "dim_products",
    engine,
    if_exists="replace",
    index=False
)

# -----------------------------
# Dimension Table: Date
# -----------------------------
orders["order_date"] = pd.to_datetime(orders["order_date"])

dim_date = pd.DataFrame()
dim_date["date"] = orders["order_date"]
dim_date["year"] = dim_date["date"].dt.year
dim_date["month"] = dim_date["date"].dt.month
dim_date["day"] = dim_date["date"].dt.day

dim_date = dim_date.drop_duplicates()

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False
)

# -----------------------------
# Fact Table: Sales
# -----------------------------
fact_sales = orders.merge(products, on="product_id")

fact_sales = fact_sales[
    [
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "price"
    ]
]

fact_sales["total_amount"] = fact_sales["quantity"] * fact_sales["price"]

fact_sales.to_sql(
    "fact_sales",
    engine,
    if_exists="replace",
    index=False
)

print("✅ Star Schema Created Successfully")