#!/usr/bin/env python3
"""
E-Commerce Sales Business Analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

def load_cleaned_data():
    """Load cleaned data for business analysis"""
    
    print("📊 E-Commerce Business Analysis")
    print("=" * 40)
    
    try:
        df = pd.read_csv('data/processed/ecommerce_cleaned.csv')
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        print(f"✅ Cleaned data loaded: {df.shape}")
        return df
    except FileNotFoundError:
        print("❌ Cleaned data not found. Please run data_cleaning.py first.")
        return None

def calculate_revenue_kpis(df):
    """Calculate and analyze revenue performance KPIs"""
    
    print(f"\n💰 Revenue Performance Analysis")
    print("-" * 35)
    
    total_revenue = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    total_orders = len(df)
    avg_order_value = df['Sales'].mean()
    profit_margin = (total_profit / total_revenue) * 100
    
    print(f"📈 Key Performance Indicators:")
    print(f"  Total Revenue: ${total_revenue:,.2f}")
    print(f"  Total Profit: ${total_profit:,.2f}")
    print(f"  Total Orders: {total_orders:,}")
    print(f"  Average Order Value: ${avg_order_value:,.2f}")
    print(f"  Profit Margin: {profit_margin:.2f}%")
    
    monthly_revenue = df.groupby(df['Order Date'].dt.to_period('M')).agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count'
    }).rename(columns={'Order ID': 'Order_Count'})
    
    monthly_revenue['Revenue_Growth_%'] = monthly_revenue['Sales'].pct_change() * 100
    monthly_revenue['Profit_Growth_%'] = monthly_revenue['Profit'].pct_change() * 100
    
    print(f"\n📅 Monthly Revenue Summary:")
    print(f"  Average Monthly Revenue: ${monthly_revenue['Sales'].mean():,.2f}")
    print(f"  Revenue Growth Trend: {'Increasing' if monthly_revenue['Revenue_Growth_%'].mean() > 0 else 'Decreasing'}")
    
    return monthly_revenue

def analyze_category_performance(df):
    """Analyze product and category performance"""
    
    print(f"\n📦 Category Performance Analysis")
    print("-" * 35)
    
    category_perf = df.groupby('Category').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count',
        'Profit_Margin_%': 'mean'
    }).rename(columns={'Order ID': 'Order_Count'}).sort_values('Sales', ascending=False)
    
    print(f"🏆 Top 5 Categories by Revenue:")
    for i, (category, row) in enumerate(category_perf.head().iterrows(), 1):
        print(f"  {i}. {category}: ${row['Sales']:,.2f} ({row['Profit_Margin_%']:.1f}% margin)")
    
    print(f"\n📉 Bottom 3 Categories by Revenue:")
    for i, (category, row) in enumerate(category_perf.tail(3).iterrows(), 1):
        print(f"  {category}: ${row['Sales']:,.2f} ({row['Profit_Margin_%']:.1f}% margin)")
    
    subcat_perf = df.groupby('Sub-Category').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count'
    }).rename(columns={'Order ID': 'Order_Count'}).sort_values('Sales', ascending=False)
    
    print(f"\n🔝 Top 5 Sub-Categories:")
    for i, (subcategory, row) in enumerate(subcat_perf.head().iterrows(), 1):
        print(f"  {i}. {subcategory}: ${row['Sales']:,.2f}")
    
    return category_perf, subcat_perf

def analyze_customer_behavior(df):
    """Analyze customer behavior and segmentation"""
    
    print(f"\n👥 Customer Behavior Analysis")
    print("-" * 30)
    
    try:
        customer_stats = df.groupby('Customer Name').agg({
            'Sales': ['sum', 'mean'],
            'Order ID': 'count',
            'Order Date': ['min', 'max']
        }).round(2)
        
        customer_stats.columns = ['Total_Sales', 'Avg_Order_Value', 'Order_Count', 'First_Order', 'Last_Order']
        customer_stats['Customer_Lifetime_Days'] = (customer_stats['Last_Order'] - customer_stats['First_Order']).dt.days
        customer_stats['Segment'] = pd.cut(customer_stats['Total_Sales'],
                                           bins=[0, 1000, 5000, 20000, float('inf')],
                                           labels=['Bronze', 'Silver', 'Gold', 'Platinum'])
        
        segment_summary = customer_stats.groupby('Segment').agg({
            'Total_Sales': 'sum',
            'Order_Count': 'sum',
            'Customer Name': 'count'
        }).rename(columns={'Customer Name': 'Customer_Count'})
        
        print(f"🎯 Customer Segments:")
        for segment, row in segment_summary.iterrows():
            print(f"  {segment}: {row['Customer_Count']} customers, ${row['Total_Sales']:,.2f} revenue")
        
        print(f"\n📊 Customer Insights:")
        print(f"  Total Unique Customers: {len(customer_stats):,}")
        print(f"  Average Orders per Customer: {customer_stats['Order_Count'].mean():.1f}")
        print(f"  Average Customer Lifetime: {customer_stats['Customer_Lifetime_Days'].mean():.0f} days")
        print(f"  Average Customer Value: ${customer_stats['Total_Sales'].mean():,.2f}")
        
        return customer_stats, segment_summary
        
    except Exception as e:
        print(f"❌ Error in customer analysis: {e}")
        print(f"\n📊 Basic Customer Insights:")
        print(f"  Total Unique Customers: {df['Customer Name'].nunique():,}")
        print(f"  Average Orders per Customer: {len(df) / df['Customer Name'].nunique():.1f}")
        print(f"  Average Customer Value: ${df['Sales'].sum() / df['Customer Name'].nunique():,.2f}")
        return None, None

def analyze_geographic_performance(df):
    """Analyze regional and geographic performance"""
    
    print(f"\n🌍 Geographic Performance Analysis")
    print("-" * 38)
    
    region_perf = df.groupby('Region').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count',
        'Customer Name': 'nunique'
    }).rename(columns={'Order ID': 'Order_Count', 'Customer Name': 'Unique_Customers'})
    
    print(f"🗺️ Regional Performance:")
    for region, row in region_perf.iterrows():
        print(f"  {region}: ${row['Sales']:,.2f} ({row['Unique_Customers']} customers)")
    
    city_perf = df.groupby('City').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count'
    }).rename(columns={'Order ID': 'Order_Count'}).sort_values('Sales', ascending=False)
    
    print(f"\n🏙️ Top 10 Cities by Revenue:")
    for i, (city, row) in enumerate(city_perf.head(10).iterrows(), 1):
        print(f"  {i}. {city}: ${row['Sales']:,.2f}")
    
    return region_perf, city_perf

def analyze_profitability(df):
    """Analyze profitability and discount impact"""
    
    print(f"\n💸 Profitability Analysis")
    print("-" * 28)
    
    total_revenue = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    overall_margin = (total_profit / total_revenue) * 100
    
    print(f"💰 Overall Profitability:")
    print(f"  Total Revenue: ${total_revenue:,.2f}")
    print(f"  Total Profit: ${total_profit:,.2f}")
    print(f"  Profit Margin: {overall_margin:.2f}%")
    
    discount_impact = df.groupby(pd.cut(df['Discount'], bins=[0, 5, 10, 15, 20, 25, 30], 
                                     labels=['0-5%', '6-10%', '11-15%', '16-20%', '21-25%', '26-30%'])).agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count',
        'Profit_Margin_%': 'mean'
    }).rename(columns={'Order ID': 'Order_Count'})
    
    print(f"\n🎯 Discount Impact Analysis:")
    for discount_range, row in discount_impact.iterrows():
        print(f"  {discount_range}: {row['Profit_Margin_%']:.1f}% margin, {row['Order_Count']} orders")
    
    product_profit = df.groupby('Product Name').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count',
        'Profit_Margin_%': 'mean'
    }).rename(columns={'Order ID': 'Order_Count'})
    
    print(f"\n🏆 Top 5 Most Profitable Products:")
    top_products = product_profit.nlargest(5, 'Profit')
    for i, (product, row) in enumerate(top_products.iterrows(), 1):
        print(f"  {i}. {product}: ${row['Profit']:,.2f} ({row['Profit_Margin_%']:.1f}% margin)")
    
    return discount_impact, product_profit

def generate_business_recommendations(df):
    """Generate actionable business recommendations"""
    
    print(f"\n🎯 Business Recommendations")
    print("-" * 30)
    
    recommendations = []
    
    monthly_trend = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
    if len(monthly_trend) > 1:
        if monthly_trend.iloc[-1] > monthly_trend.iloc[-2]:
            recommendations.append("✅ Revenue is growing month-over-month - continue current strategies")
        else:
            recommendations.append("⚠️ Revenue declined last month - investigate causes and implement recovery strategies")
    
    category_perf = df.groupby('Category')['Profit_Margin_%'].mean().sort_values(ascending=False)
    best_category = category_perf.index[0]
    worst_category = category_perf.index[-1]
    recommendations.append(f"🏆 {best_category} has highest profit margins ({category_perf.iloc[0]:.1f}%) - consider expanding this category")
    recommendations.append(f"📉 {worst_category} has lowest profit margins ({category_perf.iloc[-1]:.1f}%) - review pricing and costs")
    
    region_perf = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    top_region = region_perf.index[0]
    recommendations.append(f"🌍 {top_region} generates most revenue (${region_perf.iloc[0]:,.0f}) - strengthen presence in this region")
    
    avg_orders_per_customer = df.groupby('Customer Name')['Order ID'].count().mean()
    if avg_orders_per_customer < 2:
        recommendations.append("👥 Low repeat purchase rate - implement customer retention programs")
    else:
        recommendations.append("👥 Good customer retention - maintain current loyalty programs")
    
    for i, rec in enumerate(recommendations, 1):
        print(f"  {i}. {rec}")
    
    return recommendations

def create_executive_summary(df):
    """Create executive summary with key metrics"""
    
    print(f"\n📋 Executive Summary")
    print("-" * 22)
    
    total_revenue = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    total_orders = len(df)
    unique_customers = df['Customer Name'].nunique()
    unique_products = df['Product Name'].nunique()
    avg_order_value = df['Sales'].mean()
    profit_margin = (total_profit / total_revenue) * 100
    
    print(f"📊 Key Business Metrics:")
    print(f"  Total Revenue: ${total_revenue:,.2f}")
    print(f"  Total Profit: ${total_profit:,.2f}")
    print(f"  Total Orders: {total_orders:,}")
    print(f"  Unique Customers: {unique_customers:,}")
    print(f"  Unique Products: {unique_products:,}")
    print(f"  Average Order Value: ${avg_order_value:,.2f}")
    print(f"  Profit Margin: {profit_margin:.2f}%")
    print(f"  Analysis Period: {df['Order Date'].min().date()} to {df['Order Date'].max().date()}")

def save_analysis_results(monthly_revenue, category_perf, customer_stats, recommendations):
    """Save analysis results to CSV files"""
    
    print(f"\n💾 Saving Analysis Results...")
    
    import os
    os.makedirs('reports', exist_ok=True)
    
    monthly_revenue.to_csv('reports/monthly_revenue_analysis.csv')
    category_perf.to_csv('reports/category_performance.csv')
    
    if customer_stats is not None:
        customer_stats.groupby('Segment').size().to_csv('reports/customer_segments.csv')
    
    recommendations_df = pd.DataFrame({'Recommendation': recommendations})
    recommendations_df.to_csv('reports/business_recommendations.csv', index=False)
    
    print(f"✅ Analysis results saved to reports/ directory:")
    print(f"  - monthly_revenue_analysis.csv")
    print(f"  - category_performance.csv")
    print(f"  - customer_segments.csv")
    print(f"  - business_recommendations.csv")

def main():
    """Main business analysis pipeline"""
    
    try:
        df = load_cleaned_data()
        if df is None:
            return
        
        monthly_revenue = calculate_revenue_kpis(df)
        category_perf, subcat_perf = analyze_category_performance(df)
        customer_stats, segment_summary = analyze_customer_behavior(df)
        region_perf, city_perf = analyze_geographic_performance(df)
        discount_impact, product_profit = analyze_profitability(df)
        recommendations = generate_business_recommendations(df)
        create_executive_summary(df)
        
        if customer_stats is not None:
            save_analysis_results(monthly_revenue, category_perf, customer_stats, recommendations)
        else:
            print("⚠️ Skipping detailed report generation due to analysis issues")
        
        print(f"\n🎉 Business Analysis Completed Successfully!")
        print(f"📁 Reports generated in reports/ directory")
        print(f"🚀 Ready for business decision-making!")
        
    except Exception as e:
        print(f"❌ Error in business analysis: {e}")

if __name__ == "__main__":
    main()
