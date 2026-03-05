import psycopg2

def initialize_database():
    conn = psycopg2.connect(
    host="localhost",
    database="ecommerce_db",
    user="postgres",
    password="Earthly009#",
    port="5432"
)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INT PRIMARY KEY,
        name TEXT,
        city TEXT,
        state TEXT,
        signup_date DATE,
        device_type TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INT PRIMARY KEY,
        category TEXT,
        price FLOAT,
        brand TEXT,
        rating FLOAT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT PRIMARY KEY,
        customer_id INT,
        product_id INT,
        order_date DATE,
        quantity INT,
        payment_method TEXT,
        order_status TEXT
    );
    """)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    initialize_database()