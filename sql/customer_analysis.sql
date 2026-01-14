-- ============================================
-- E-Commerce Sales Analysis - Customer Analysis
-- ============================================
-- SQL equivalent of Python customer segmentation analysis

-- 1. Customer Lifetime Value (CLV) Analysis
SELECT 
    `Customer Name`,
    COUNT(`Order ID`) AS total_orders,
    MIN(`Order Date`) AS first_order_date,
    MAX(`Order Date`) AS last_order_date,
    ROUND(JULIANDAY(MAX(`Order Date`)) - JULIANDAY(MIN(`Order Date`)), 0) AS customer_lifetime_days,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    ROUND(SUM(Sales) / COUNT(`Order ID`), 2) AS revenue_per_order,
    ROUND(SUM(Profit) / COUNT(`Order ID`), 2) AS profit_per_order,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    CASE 
        WHEN SUM(Sales) < 1000 THEN 'Bronze'
        WHEN SUM(Sales) < 5000 THEN 'Silver'
        WHEN SUM(Sales) < 20000 THEN 'Gold'
        ELSE 'Platinum'
    END AS customer_segment
FROM ecommerce_sales
GROUP BY `Customer Name`
ORDER BY total_revenue DESC;

-- 2. Customer Segmentation Summary
SELECT 
    customer_segment,
    COUNT(*) AS customer_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customer_segments), 2) AS segment_share_pct,
    ROUND(SUM(total_orders), 0) AS total_orders,
    ROUND(SUM(total_revenue), 2) AS segment_revenue,
    ROUND(SUM(total_profit), 2) AS segment_profit,
    ROUND(AVG(avg_order_value), 2) AS avg_order_value,
    ROUND(AVG(customer_lifetime_days), 0) AS avg_lifetime_days
FROM (
    SELECT 
        `Customer Name`,
        COUNT(`Order ID`) AS total_orders,
        ROUND(SUM(Sales), 2) AS total_revenue,
        ROUND(SUM(Profit), 2) AS total_profit,
        ROUND(AVG(Sales), 2) AS avg_order_value,
        ROUND(JULIANDAY(MAX(`Order Date`)) - JULIANDAY(MIN(`Order Date`)), 0) AS customer_lifetime_days,
        CASE 
            WHEN SUM(Sales) < 1000 THEN 'Bronze'
            WHEN SUM(Sales) < 5000 THEN 'Silver'
            WHEN SUM(Sales) < 20000 THEN 'Gold'
            ELSE 'Platinum'
        END AS customer_segment
    FROM ecommerce_sales
    GROUP BY `Customer Name`
) customer_segments
GROUP BY customer_segment
ORDER BY segment_revenue DESC;

-- 3. Repeat Purchase Analysis
SELECT 
    `Customer Name`,
    COUNT(`Order ID`) AS order_count,
    CASE 
        WHEN COUNT(`Order ID`) = 1 THEN 'One-time'
        WHEN COUNT(`Order ID`) BETWEEN 2 AND 3 THEN 'Occasional'
        WHEN COUNT(`Order ID`) BETWEEN 4 AND 6 THEN 'Regular'
        ELSE 'Frequent'
    END AS purchase_frequency,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    MIN(`Order Date`) AS first_order,
    MAX(`Order Date`) AS last_order
FROM ecommerce_sales
GROUP BY `Customer Name`
ORDER BY order_count DESC, total_revenue DESC;

-- 4. Customer Geographic Distribution
SELECT 
    Region,
    COUNT(DISTINCT `Customer Name`) AS unique_customers,
    COUNT(`Order ID`) AS total_orders,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    ROUND(SUM(Sales) / COUNT(DISTINCT `Customer Name`), 2) AS revenue_per_customer,
    ROUND(COUNT(`Order ID`) * 1.0 / COUNT(DISTINCT `Customer Name`), 2) AS orders_per_customer
FROM ecommerce_sales
GROUP BY Region
ORDER BY total_revenue DESC;

-- 5. High-Value Customers (Top 10%)
WITH customer_revenue AS (
    SELECT 
        `Customer Name`,
        SUM(Sales) AS total_revenue,
        COUNT(`Order ID`) AS order_count,
        AVG(Sales) AS avg_order_value,
        PERCENT_RANK() OVER (ORDER BY SUM(Sales) DESC) AS revenue_percentile
    FROM ecommerce_sales
    GROUP BY `Customer Name`
)
SELECT 
    `Customer Name`,
    ROUND(total_revenue, 2) AS total_revenue,
    order_count,
    ROUND(avg_order_value, 2) AS avg_order_value,
    ROUND(revenue_percentile * 100, 2) AS percentile_rank
FROM customer_revenue
WHERE revenue_percentile <= 0.1  -- Top 10%
ORDER BY total_revenue DESC;

-- 6. Customer Payment Preferences
SELECT 
    `Customer Name`,
    `Payment Mode`,
    COUNT(`Order ID`) AS order_count,
    ROUND(SUM(Sales), 2) AS total_spent,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    ROUND(COUNT(`Order ID`) * 100.0 / total_orders, 2) AS payment_preference_pct
FROM (
    SELECT 
        `Customer Name`,
        `Payment Mode`,
        `Order ID`,
        Sales,
        COUNT(*) OVER (PARTITION BY `Customer Name`) AS total_orders
    FROM ecommerce_sales
) customer_payments
GROUP BY `Customer Name`, `Payment Mode`, total_orders
ORDER BY `Customer Name`, payment_preference_pct DESC;
