from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:Earthly009#@localhost:5432/ecommerce_db")

with engine.connect() as conn:

    conn.execute(text("DROP TABLE IF EXISTS dim_customers"))
    conn.execute(text("""
    CREATE TABLE dim_customers AS
    SELECT DISTINCT customer_id, name, city, state, device_type
    FROM customers
    """))

    conn.execute(text("DROP TABLE IF EXISTS dim_products"))
    conn.execute(text("""
    CREATE TABLE dim_products AS
    SELECT DISTINCT product_id, category, price
    FROM products
    """))

    conn.execute(text("DROP TABLE IF EXISTS fact_sales"))
    conn.execute(text("""
    CREATE TABLE fact_sales AS
    SELECT order_id, customer_id, product_id, order_date, quantity, total_amount
    FROM orders
    """))

    conn.commit()

print("Star schema created successfully")