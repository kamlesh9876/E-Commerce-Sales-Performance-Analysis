-- ============================================
-- E-Commerce Sales Analysis - Revenue KPIs
-- ============================================
-- SQL equivalent of Python analysis for Data Analyst demonstration

-- 1. Overall Revenue KPIs
SELECT 
    COUNT(DISTINCT `Order ID`) AS total_orders,
    COUNT(DISTINCT `Customer Name`) AS unique_customers,
    COUNT(DISTINCT `Product Name`) AS unique_products,
    SUM(Sales) AS total_revenue,
    SUM(Profit) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    MIN(`Order Date`) AS period_start,
    MAX(`Order Date`) AS period_end
FROM ecommerce_sales;

-- 2. Monthly Revenue Trends
SELECT 
    strftime('%Y-%m', `Order Date`) AS month,
    COUNT(`Order ID`) AS order_count,
    ROUND(SUM(Sales), 2) AS monthly_revenue,
    ROUND(SUM(Profit), 2) AS monthly_profit,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    LAG(SUM(Sales), 1) OVER (ORDER BY strftime('%Y-%m', `Order Date`)) AS prev_month_revenue,
    ROUND((SUM(Sales) - LAG(SUM(Sales), 1) OVER (ORDER BY strftime('%Y-%m', `Order Date`))) / 
          LAG(SUM(Sales), 1) OVER (ORDER BY strftime('%Y-%m', `Order Date`)) * 100, 2) AS revenue_growth_pct
FROM ecommerce_sales
GROUP BY strftime('%Y-%m', `Order Date`)
ORDER BY month;

-- 3. Category Performance Analysis
SELECT 
    Category,
    COUNT(`Order ID`) AS order_count,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    ROUND(SUM(Sales) * 100.0 / (SELECT SUM(Sales) FROM ecommerce_sales), 2) AS revenue_share_pct
FROM ecommerce_sales
GROUP BY Category
ORDER BY total_revenue DESC;

-- 4. Regional Performance
SELECT 
    Region,
    COUNT(DISTINCT `Customer Name`) AS unique_customers,
    COUNT(`Order ID`) AS order_count,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    ROUND(SUM(Sales) * 100.0 / (SELECT SUM(Sales) FROM ecommerce_sales), 2) AS revenue_share_pct
FROM ecommerce_sales
GROUP BY Region
ORDER BY total_revenue DESC;

-- 5. Top Performing Cities
SELECT 
    City,
    Region,
    COUNT(`Order ID`) AS order_count,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    ROUND(AVG(Sales), 2) AS avg_order_value
FROM ecommerce_sales
GROUP BY City, Region
ORDER BY total_revenue DESC
LIMIT 15;

-- 6. Payment Methods Analysis
SELECT 
    `Payment Mode`,
    COUNT(`Order ID`) AS order_count,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    ROUND(COUNT(`Order ID`) * 100.0 / (SELECT COUNT(*) FROM ecommerce_sales), 2) AS order_share_pct
FROM ecommerce_sales
GROUP BY `Payment Mode`
ORDER BY order_count DESC;

-- 7. Quarterly Performance with YoY Comparison
SELECT 
    strftime('%Y', `Order Date`) AS year,
    CASE 
        WHEN CAST(strftime('%m', `Order Date`) AS INTEGER) BETWEEN 1 AND 3 THEN 'Q1'
        WHEN CAST(strftime('%m', `Order Date`) AS INTEGER) BETWEEN 4 AND 6 THEN 'Q2'
        WHEN CAST(strftime('%m', `Order Date`) AS INTEGER) BETWEEN 7 AND 9 THEN 'Q3'
        ELSE 'Q4'
    END AS quarter,
    COUNT(`Order ID`) AS order_count,
    ROUND(SUM(Sales), 2) AS quarterly_revenue,
    ROUND(SUM(Profit), 2) AS quarterly_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct
FROM ecommerce_sales
GROUP BY year, quarter
ORDER BY year, quarter;
