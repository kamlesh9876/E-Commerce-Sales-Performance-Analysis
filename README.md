# 📊 E-Commerce Sales Performance Analysis - Data Analyst Portfolio 🌐 LIVE

## 🎯 **Project Overview**
This is a **Data Analyst focused** e-commerce sales analysis project that demonstrates end-to-end business intelligence capabilities. The project showcases core data analyst skills: data cleaning, SQL-style aggregations, KPI calculation, trend analysis, and business insights communication.

**🚀 Interactive Dashboard is LIVE and ready for viewing!**

## 🎓 **Data Analyst Skills Demonstrated**
- ✅ **Data Cleaning & Validation**: Systematic data quality assessment
- ✅ **SQL-Style Analysis**: Complex aggregations and window functions
- ✅ **KPI Calculation**: Revenue, profit, margin, and growth metrics
- ✅ **Trend Analysis**: Monthly, seasonal, and year-over-year patterns
- ✅ **Customer Segmentation**: RFM analysis and lifetime value
- ✅ **Business Intelligence**: Actionable insights and recommendations
- ✅ **Power BI Preparation**: Clean data model and DAX measures

## 📁 **Project Structure (Data Analyst Optimized)**
```
E_commerce_Sale/
├── 📄 README.md                    # Business-focused documentation
├── 📄 run_analysis.py              # Simple analysis runner
├── 📄 requirements.txt             # Python dependencies
│
├── 📁 scripts/                     # Core analysis scripts
│   ├── 📄 data_cleaning.py         # Data validation & feature engineering
│   ├── 📄 business_analysis.py    # KPIs & business insights
│   └── 📄 download_dataset.py      # Data acquisition
│
├── 📁 sql/                        # SQL equivalents for all analyses
│   ├── 📄 revenue_kpis.sql        # Revenue KPIs & trends
│   ├── 📄 customer_analysis.sql   # Customer segmentation & CLV
│   └── 📄 product_performance.sql  # Product profitability analysis
│
├── 📁 powerbi/                    # Power BI implementation guide
│   └── 📄 README.md               # Complete dashboard instructions
│
├── 📁 data/                       # Data management
│   ├── 📁 raw/                   # Original dataset
│   └── 📁 processed/             # Cleaned analysis data
│
└── 📁 reports/                    # Generated business reports
```

## 📊 **Dataset Information**
- **Source**: Kaggle E-Commerce Sales Dataset
- **Size**: 5,000 orders, 14 core columns, 22 engineered features
- **Time Period**: October 2023 – October 2025 (2 years)
- **Geography**: 4 regions across 25+ Indian cities
- **Products**: 3,835 unique products across 10 categories
- **Customers**: 4,844 unique customers

## 🔄 **Analysis Pipeline**

### **Step 1: Data Cleaning & Preparation**
```bash
python scripts/data_cleaning.py
```
- Data quality assessment (100% completeness)
- Business logic validation
- Feature engineering (time-based, business metrics)
- Memory optimization (2.75MB → 0.89MB)

### **Step 2: Business Analysis & KPIs**
```bash
python scripts/business_analysis.py
```
- Revenue performance analysis
- Category and product performance
- Customer segmentation (Bronze/Silver/Gold/Platinum)
- Geographic performance insights
- Profitability and discount impact

### **Step 3: Complete Pipeline**
```bash
python run_analysis.py
```
Runs both phases automatically and generates all outputs.

## 📈 **Key Business Metrics & Insights**

### **💰 Financial Performance**
- **Total Revenue**: $533,666,024.35
- **Total Profit**: $79,708,734.91
- **Profit Margin**: 14.94%
- **Average Order Value**: $106,733.20

### **🏆 Top Performers**
- **Categories**: Home Decor ($57.2M), Furniture ($56.6M), Clothing ($55.1M)
- **Region**: North ($143.6M revenue)
- **Cities**: Bangalore, Lucknow, Guwahati leading

### **👥 Customer Insights**
- **Unique Customers**: 4,844
- **Average Orders/Customer**: 1.0 (opportunity for retention)
- **Customer Value**: $110,170.53 average

### **🎯 Business Recommendations**
1. **Revenue Recovery**: Investigate declining monthly trend
2. **Category Expansion**: Focus on Electronics (15.4% margins)
3. **Pricing Review**: Optimize Beauty category (14.4% margins)
4. **Geographic Focus**: Strengthen North region presence
5. **Customer Retention**: Implement loyalty programs

## 🗃️ **SQL Analysis Files**

### **revenue_kpis.sql**
- Overall KPI calculations
- Monthly revenue trends with growth rates
- Category performance rankings
- Geographic distribution analysis
- Payment method breakdown

### **customer_analysis.sql**
- Customer lifetime value (CLV) analysis
- RFM segmentation (Bronze/Silver/Gold/Platinum)
- Purchase frequency patterns
- Geographic customer distribution
- High-value customer identification

### **product_performance.sql**
- Product profitability ranking
- Category and sub-category analysis
- Discount impact on margins
- Seasonal product performance
- Product affinity analysis

## 📊 **Power BI Integration**

### **Data Model Structure**
- **Fact Tables**: Sales transactions
- **Dimension Tables**: Customers, Products, Geography, Calendar
- **Relationships**: Star schema design

### **Key DAX Measures**
```dax
Total Revenue = SUM(Sales[Sales])
Profit Margin % = DIVIDE([Total Profit], [Total Revenue]) * 100
Customer Segment = SWITCH(TRUE(), 
    [Total Revenue] < 1000, "Bronze",
    [Total Revenue] < 5000, "Silver",
    [Total Revenue] < 20000, "Gold",
    "Platinum"
)
```

### **Dashboard Pages**
1. **Executive Overview**: KPIs and trends
2. **Product Analysis**: Category and product performance
3. **Customer Insights**: Segmentation and behavior
4. **Geographic Analysis**: Regional and city performance

## 🌐 **Live Demo**

**🚀 View the Interactive Dashboard**: https://kamlesh9876.github.io/E-Commerce-Sales-Performance-Analysis/dashboard.html

### **Dashboard Features**
- ✅ Real-time business KPIs and metrics
- ✅ Interactive charts and visualizations
- ✅ Customer segmentation insights
- ✅ Geographic performance analysis
- ✅ Mobile-responsive design
- ✅ Downloadable reports

**Perfect for showcasing data analysis skills to recruiters and employers!**

## 🚀 **How to Use**

### **Quick Start**
```bash
# Install dependencies
pip install -r requirements.txt

# Run complete analysis
python run_analysis.py

# View results
ls data/processed/ reports/ sql/
```

### **Power BI Setup**
1. Load `data/processed/ecommerce_cleaned.csv` into Power BI
2. Use SQL queries for complex measures
3. Follow `powerbi/README.md` for dashboard creation

## 💼 **Business Value & Impact**

### **Decision Support**
- **Revenue Optimization**: Focus on high-performing categories
- **Customer Retention**: Strategies to increase repeat purchases
- **Geographic Expansion**: Target high-performing regions
- **Product Strategy**: Promote profitable items, review underperformers

### **Operational Efficiency**
- **Data-Driven Planning**: Replace assumptions with insights
- **Cost Optimization**: Identify discount impact on profitability
- **Inventory Planning**: Seasonal and geographic demand patterns

## 📋 **What This Project Demonstrates**

### **✅ Data Analyst Core Competencies**
- End-to-end data processing workflow
- SQL and Python analytical skills
- Business KPI calculation and interpretation
- Data visualization and storytelling
- Clear communication of insights

### **✅ Technical Skills**
- **Python**: Pandas, NumPy, data manipulation
- **SQL**: Complex queries, window functions, aggregations
- **Power BI**: Data modeling, DAX measures, dashboard design
- **Data Validation**: Quality assessment and business logic verification

### **✅ Business Acumen**
- Revenue and profitability analysis
- Customer segmentation and lifetime value
- Geographic and product performance insights
- Actionable recommendation generation

## ⚠️ **Limitations & Assumptions**
- Static historical dataset (no real-time data)
- Synthetic e-commerce data for demonstration
- Analysis limited to 2-year period
- Customer retention based on order frequency only

## 🎯 **Future Enhancements**
- **Time Series Forecasting**: Predictive revenue modeling
- **Advanced Segmentation**: Machine learning customer clustering
- **Real-time Dashboard**: Live data integration
- **A/B Testing**: Discount and pricing impact analysis

## 📌 **Conclusion**

This project demonstrates a complete **Data Analyst workflow** from raw data to actionable business insights. It showcases the ability to transform complex datasets into clear, actionable intelligence that drives business decisions.

**Perfect for Data Analyst portfolio and interview preparation!**

---

**Repository**: https://github.com/kamlesh9876/E-Commerce-Sales-Performance-Analysis  
**🌐 Live Dashboard**: https://kamlesh9876.github.io/E-Commerce-Sales-Performance-Analysis/dashboard.html  
**Status**: ✅ Complete and Deployed - Live on GitHub Pages  
**Last Updated**: January 2026
