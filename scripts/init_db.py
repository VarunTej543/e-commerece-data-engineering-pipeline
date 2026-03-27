import psycopg2

def initialize_database():
    conn = psycopg2.connect(
        host="localhost",
        database="ecommerce_db",
        user="postgres",
        password="Earthly009#"
    )
    cur = conn.cursor()

    # Customers
    cur.execute("""
    DROP TABLE IF EXISTS customers;
    CREATE TABLE customers (
        customer_id INT PRIMARY KEY,
        name TEXT,
        city TEXT,
        state TEXT,
        signup_date DATE,
        device_type TEXT
    );
    """)

    # Products
    cur.execute("""
    DROP TABLE IF EXISTS products;
    CREATE TABLE products (
        product_id INT PRIMARY KEY,
        category TEXT,
        price FLOAT
    );
    """)

    # Orders
    cur.execute("""
    DROP TABLE IF EXISTS orders;
    CREATE TABLE orders (
        order_id INT PRIMARY KEY,
        customer_id INT,
        product_id INT,
        order_date DATE,
        quantity INT,
        total_amount FLOAT
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("Database initialized")

if __name__ == "__main__":
    initialize_database()