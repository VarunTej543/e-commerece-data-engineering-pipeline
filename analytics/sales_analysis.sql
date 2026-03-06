-- Total Revenue
SELECT SUM(total_amount) AS total_revenue
FROM fact_sales;

-- Top Selling Products
SELECT
    product_id,
    SUM(quantity) AS total_sold
FROM fact_sales
GROUP BY product_id
ORDER BY total_sold DESC;

-- Monthly Revenue
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(total_amount) AS revenue
FROM fact_sales
GROUP BY month
ORDER BY month;