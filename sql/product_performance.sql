-- ============================================
-- E-Commerce Sales Analysis - Product Performance
-- ============================================
-- SQL equivalent of Python product analysis

-- 1. Top Performing Products by Revenue
SELECT 
    `Product Name`,
    Category,
    `Sub-Category`,
    COUNT(`Order ID`) AS order_count,
    ROUND(SUM(Quantity), 0) AS total_quantity_sold,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    ROUND(AVG(`Unit Price`), 2) AS avg_unit_price,
    ROUND(AVG(Discount), 2) AS avg_discount_pct
FROM ecommerce_sales
GROUP BY `Product Name`, Category, `Sub-Category`
ORDER BY total_revenue DESC
LIMIT 20;

-- 2. Bottom Performing Products (Low Revenue)
SELECT 
    `Product Name`,
    Category,
    `Sub-Category`,
    COUNT(`Order ID`) AS order_count,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    ROUND(AVG(Sales), 2) AS avg_order_value
FROM ecommerce_sales
GROUP BY `Product Name`, Category, `Sub-Category`
HAVING COUNT(`Order ID`) >= 2  -- Products with at least 2 orders
ORDER BY total_revenue ASC
LIMIT 20;

-- 3. Category Performance Summary
SELECT 
    Category,
    COUNT(DISTINCT `Product Name`) AS unique_products,
    COUNT(DISTINCT `Sub-Category`) AS unique_subcategories,
    COUNT(`Order ID`) AS total_orders,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    ROUND(SUM(Sales) * 100.0 / (SELECT SUM(Sales) FROM ecommerce_sales), 2) AS revenue_share_pct,
    ROUND(SUM(Quantity), 0) AS total_quantity_sold
FROM ecommerce_sales
GROUP BY Category
ORDER BY total_revenue DESC;

-- 4. Sub-Category Performance within Categories
SELECT 
    Category,
    `Sub-Category`,
    COUNT(DISTINCT `Product Name`) AS unique_products,
    COUNT(`Order ID`) AS order_count,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    ROUND(SUM(Sales) * 100.0 / (SELECT SUM(Sales) FROM ecommerce_sales), 2) AS revenue_share_pct
FROM ecommerce_sales
GROUP BY Category, `Sub-Category`
ORDER BY Category, total_revenue DESC;

-- 5. High Margin Products (Profitability Analysis)
SELECT 
    `Product Name`,
    Category,
    `Sub-Category`,
    COUNT(`Order ID`) AS order_count,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    ROUND(AVG(`Unit Price`), 2) AS avg_unit_price,
    ROUND(AVG(Discount), 2) AS avg_discount_pct
FROM ecommerce_sales
GROUP BY `Product Name`, Category, `Sub-Category`
HAVING COUNT(`Order ID`) >= 3 AND profit_margin_pct > 20
ORDER BY profit_margin_pct DESC, total_revenue DESC
LIMIT 20;

-- 6. Discount Impact on Product Performance
SELECT 
    CASE 
        WHEN Discount BETWEEN 0 AND 5 THEN '0-5%'
        WHEN Discount BETWEEN 6 AND 10 THEN '6-10%'
        WHEN Discount BETWEEN 11 AND 15 THEN '11-15%'
        WHEN Discount BETWEEN 16 AND 20 THEN '16-20%'
        WHEN Discount BETWEEN 21 AND 25 THEN '21-25%'
        ELSE '26%+'
    END AS discount_range,
    COUNT(`Order ID`) AS order_count,
    COUNT(DISTINCT `Product Name`) AS unique_products,
    ROUND(SUM(Sales), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS profit_margin_pct,
    ROUND(AVG(Sales), 2) AS avg_order_value,
    ROUND(AVG(Discount), 2) AS avg_discount_pct
FROM ecommerce_sales
GROUP BY discount_range
ORDER BY MIN(Discount);

-- 7. Product Affinity Analysis (Products Frequently Bought Together)
WITH product_pairs AS (
    SELECT 
        o1.`Product Name` AS product_1,
        o2.`Product Name` AS product_2,
        o1.Category AS category_1,
        o2.Category AS category_2
    FROM ecommerce_sales o1
    JOIN ecommerce_sales o2 ON o1.`Order ID` = o2.`Order ID` 
        AND o1.`Product Name` < o2.`Product Name`
)
SELECT 
    product_1,
    product_2,
    category_1,
    category_2,
    COUNT(*) AS times_bought_together,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM product_pairs), 2) AS affinity_percentage
FROM product_pairs
GROUP BY product_1, product_2, category_1, category_2
HAVING COUNT(*) >= 5
ORDER BY times_bought_together DESC
LIMIT 20;

-- 8. Seasonal Product Performance
SELECT 
    Category,
    CASE 
        WHEN CAST(strftime('%m', `Order Date`) AS INTEGER) BETWEEN 3 AND 5 THEN 'Spring'
        WHEN CAST(strftime('%m', `Order Date`) AS INTEGER) BETWEEN 6 AND 8 THEN 'Summer'
        WHEN CAST(strftime('%m', `Order Date`) AS INTEGER) BETWEEN 9 AND 11 THEN 'Fall'
        ELSE 'Winter'
    END AS season,
    COUNT(`Order ID`) AS order_count,
    ROUND(SUM(Sales), 2) AS seasonal_revenue,
    ROUND(SUM(Sales) * 100.0 / total_category_revenue, 2) AS seasonal_share_pct
FROM (
    SELECT 
        Category,
        `Order Date`,
        `Order ID`,
        Sales,
        SUM(Sales) OVER (PARTITION BY Category) AS total_category_revenue
    FROM ecommerce_sales
) seasonal_data
GROUP BY Category, season, total_category_revenue
ORDER BY Category, seasonal_revenue DESC;
