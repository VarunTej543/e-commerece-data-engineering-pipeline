import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:Earthly009#@localhost:5432/ecommerce_db")

# Use forward slashes ✅
customers = pd.read_csv("../data/customers.csv")
products = pd.read_csv("../data/products.csv")
orders = pd.read_csv("../data/orders.csv")

price_map = dict(zip(products.product_id, products.price))

with engine.connect() as conn:

    # Customers
    for _, row in customers.iterrows():
        conn.execute(text("""
        INSERT INTO customers VALUES (:customer_id, :name, :city, :state, :signup_date, :device_type)
        ON CONFLICT (customer_id) DO NOTHING
        """), dict(row))

    # Products
    for _, row in products.iterrows():
        conn.execute(text("""
        INSERT INTO products VALUES (:product_id, :category, :price)
        ON CONFLICT (product_id) DO NOTHING
        """), dict(row))

    # Orders
    for _, row in orders.iterrows():
        total_amount = row["quantity"] * price_map.get(row["product_id"], 0)

        conn.execute(text("""
        INSERT INTO orders VALUES (:order_id, :customer_id, :product_id, :order_date, :quantity, :total_amount)
        ON CONFLICT (order_id) DO NOTHING
        """), {
            "order_id": row["order_id"],
            "customer_id": row["customer_id"],
            "product_id": row["product_id"],
            "order_date": row["order_date"],
            "quantity": row["quantity"],
            "total_amount": total_amount
        })

    conn.commit()

print("Data loaded successfully")