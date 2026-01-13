# 📊 E-Commerce Sales Performance Analysis

## 📌 Project Overview

This project is an end-to-end e-commerce sales analytics and business intelligence system that transforms raw transactional data into actionable insights. It simulates a real-world analytics workflow used by data analysts to evaluate revenue performance, product profitability, customer behavior, and regional trends.

The system combines Python-based data processing, analytical visualizations, and a lightweight interactive web dashboard to support data-driven business decisions.

## 🎯 Objectives

- Analyze sales performance and revenue trends over time
- Identify top and underperforming products and categories
- Understand customer purchasing behavior and value segments
- Evaluate regional performance across cities and regions
- Assess pricing, discounts, and profitability impact
- Present insights through professional charts and a web dashboard

## 🛠️ Tech Stack

### Data & Analytics
- **Python 3.11+**
- **Pandas** – data cleaning, transformation, aggregation
- **NumPy** – numerical computations
- **Matplotlib / Seaborn** – static visualizations

### Dashboard & Web
- **HTML5**
- **Tailwind CSS**
- **JavaScript**
- **Chart.js** – interactive charts
- **Python HTTP Server** – local dashboard hosting

### Data Source
- **Kaggle E-Commerce Sales Dataset** (prince7489/e-commerce-sales)

## 📁 Project Structure
```
E_commerce_Sale/
│
├── README.md
├── requirements.txt
├── run_analysis.py          # Menu-driven analysis runner
├── run_dashboard.py         # Dashboard server launcher
├── dashboard.html           # Interactive dashboard
│
├── data/
│   ├── raw/
│   │   └── Ecommerce_Sales_Data_2024_2025.csv
│   ├── processed/
│   │   ├── ecommerce_processed.csv
│   │   └── data_summary.csv
│   └── data_dictionary.md
│
├── scripts/
│   ├── 01_data_exploration.py
│   ├── 02_business_analysis.py
│   └── download_dataset.py
│
├── visualizations/
│   ├── sales_by_category.png
│   ├── profit_by_category.png
│   ├── monthly_sales_trend.png
│   └── payment_methods.png
│
└── reports/
```

## 📊 Dataset Information

### **Dataset Overview**
- **Source**: Kaggle E-Commerce Sales Dataset (`prince7489/e-commerce-sales`)
- **File**: `Ecommerce_Sales_Data_2024_2025.csv`
- **Size**: 5,000 orders, 14 core columns
- **Time Period**: October 2023 – October 2025 (2 years)
- **Geography**: 4 regions (North, South, East, West) across 25+ Indian cities
- **Products**: 3,835 unique products across 10 major categories
- **Customers**: 4,844 unique customers with purchase history

### **Core Data Schema**
| Column | Type | Description | Example |
|--------|------|-------------|---------|
| Order ID | Integer | Unique order identifier | 10001 |
| Order Date | Date | Transaction date | 2024-10-19 |
| Customer Name | String | Customer identifier | Kashvi Varty |
| Region | String | Geographic region | South |
| City | String | Specific city | Bangalore |
| Category | String | Product category | Books |
| Sub-Category | String | Product sub-category | Non-Fiction |
| Product Name | String | Specific product | Non-Fiction Ipsum |
| Quantity | Integer | Number of units ordered | 2 |
| Unit Price | Integer | Price per unit | 36294 |
| Discount | Integer | Discount percentage (0-30%) | 5 |
| Sales | Float | Total sale amount | 68958.6 |
| Profit | Float | Profit amount | 10525.09 |
| Payment Mode | String | Payment method | Debit Card |

### **Engineered Features**
- **Year, Month, Quarter, DayOfWeek**: Time-based analysis features
- **MonthName**: Human-readable month names
- **Profit_Margin_%**: Calculated profit margin percentage
- **Effective_Price**: Price after discount application
- **Order_Value_Category**: Order size classification (Small/Medium/Large)

### **Data Quality Metrics**
- **Completeness**: 100% (no missing values)
- **Accuracy**: Validated ranges and formats
- **Consistency**: Standardized categories and regions
- **Timeliness**: Recent data through October 2025

### **Dataset Summary**
- **Total Orders**: 5,000
- **Time Period**: Oct 2023 – Oct 2025
- **Regions**: North, South, East, West
- **Cities**: 25+ Indian cities including Bangalore, Delhi, Mumbai, Kolkata, Pune, etc.
- **Products**: 3,800+ unique products
- **Customers**: 4,800+ unique customers
- **Categories**: 10 major categories (Books, Kitchen, Furniture, Home Decor, Clothing, Sports, Toys, Electronics, Groceries, Beauty)
- **Payment Methods**: 5 types (Net Banking, COD, Debit Card, Credit Card, UPI)

## 🔄 Data Pipeline
```
Raw CSV (Kaggle) → Data Cleaning & Validation → Feature Engineering → Business KPI Analysis → Visualizations (PNG) → Interactive Web Dashboard
```

## 📋 Business Questions Answered

### 💰 Revenue Performance
- Are sales increasing or declining over time?
- What are the seasonal and monthly trends?
- What is the average order value?

### 📦 Product Performance
- Which products and categories generate the most revenue?
- Which products are underperforming?
- Which categories have the highest profit margins?

### 👥 Customer Behavior
- Who are the most valuable customers?
- How frequently do customers purchase?
- How can customer retention be improved?

### 🌍 Geographic Analysis
- Which regions and cities perform best?
- Where should marketing efforts be focused?

### 💸 Pricing & Profitability
- How do discounts impact profit?
- Which products are most profitable?
- What is the overall profit margin?

## 📈 Key Metrics & Insights

### **Business Performance**
- **Total Revenue**: $533.7M
- **Total Profit**: $79.7M
- **Overall Profit Margin**: 14.92%
- **Average Order Value**: $106,733

### **Top Performers**
- **Top Region**: North ($143.6M revenue)
- **Top Categories**: Home Decor ($57.2M), Furniture ($56.6M), Clothing ($55.1M)
- **Top Cities**: Bangalore, Lucknow, Guwahati, Chandigarh

### **Customer Insights**
- **Unique Customers**: 4,844
- **Customer Retention**: High repeat purchase rate
- **Payment Distribution**: Balanced across all 5 payment methods (~20% each)

## 📊 Visual Outputs

### **Generated Charts**
- **Revenue by Category**: Bar chart showing sales distribution
- **Profit by Category**: Bar chart showing profit margins
- **Monthly Sales Trend**: 24-month trend line analysis
- **Payment Method Distribution**: Pie chart of payment preferences

All charts are stored in the `visualizations/` directory as high-quality PNG files.

## 🌐 Interactive Dashboard

The project includes a responsive web dashboard that displays:

- **Key KPIs**: Revenue, Profit, Average Order Value, Customer Count
- **Interactive Charts**: Chart.js powered visualizations
- **Top Performers**: Categories and regions ranking
- **Business Insights**: Strategic recommendations
- **Download Links**: Access to processed data and charts

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run Complete Analysis
```bash
python run_analysis.py
```
Select Option 1 to execute the full pipeline.

### 3️⃣ Launch Dashboard
```bash
python run_dashboard.py
```
Open browser at: http://localhost:8000/dashboard.html

## 💼 Business Value

- Enables data-driven pricing and inventory decisions
- Identifies high-value customers and profitable products
- Supports strategic planning through trend analysis
- Demonstrates real-world analytics and BI workflows

## ⚠️ Limitations

- Dataset is static and historical
- No real-time data ingestion
- No authentication or role-based access
- SQL logic is simulated using Pandas aggregations

## 🎯 Future Enhancements

- SQL database integration (PostgreSQL/MySQL)
- Time-series forecasting capabilities
- Power BI / Tableau dashboard integration
- Automated report generation
- Real-time data ingestion pipeline

## 📌 Conclusion

This project demonstrates a complete analytics lifecycle, from raw data ingestion to executive-ready insights. It reflects real-world data analyst responsibilities and showcases strong skills in Python, data analysis, visualization, and business intelligence.

---

**Project Status**: ✅ Complete and Ready for Production Use
**Last Updated**: January 2026
**Dataset**: 5,000 orders (2023-2025)
**Dashboard**: Interactive web interface available
