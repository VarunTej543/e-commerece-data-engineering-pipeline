-- Total Revenue
SELECT SUM(total_amount) AS total_revenue
FROM fact_orders;

-- Revenue by Product
SELECT
    p.product_name,
    SUM(f.total_amount) AS revenue
FROM fact_orders f
JOIN dim_products p
ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC;

-- Revenue by City
SELECT
    c.city,
    SUM(f.total_amount) AS revenue
FROM fact_orders f
JOIN dim_customers c
ON f.customer_id = c.customer_id
GROUP BY c.city
ORDER BY revenue DESC;