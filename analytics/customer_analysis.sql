-- Top Customers
SELECT
    c.name,
    SUM(f.total_amount) AS total_spent
FROM fact_orders f
JOIN dim_customers c
ON f.customer_id = c.customer_id
GROUP BY c.name
ORDER BY total_spent DESC;

-- Orders per Customer
SELECT
    c.name,
    COUNT(f.order_id) AS orders_count
FROM fact_orders f
JOIN dim_customers c
ON f.customer_id = c.customer_id
GROUP BY c.name
ORDER BY orders_count DESC;