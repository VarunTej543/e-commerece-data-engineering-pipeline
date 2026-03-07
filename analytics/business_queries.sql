-- Total Revenue
SELECT SUM(total_amount) AS total_revenue
FROM fact_sales;

-- Total Orders
SELECT COUNT(order_id) AS total_orders
FROM fact_sales;

-- Top Products
SELECT
    product_id,
    SUM(quantity) AS total_sales
FROM fact_sales
GROUP BY product_id
ORDER BY total_sales DESC;

-- Revenue by Month
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(total_amount) AS revenue
FROM fact_sales
GROUP BY month
ORDER BY month;