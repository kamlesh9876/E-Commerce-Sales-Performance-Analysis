#!/usr/bin/env python3
"""
E-Commerce Business Analysis Script
This script provides comprehensive business insights from the e-commerce data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

def load_processed_data():
    """Load the processed e-commerce data"""
    
    print("E-Commerce Business Analysis")
    print("=" * 40)
    
    try:
        df = pd.read_csv('data/processed/ecommerce_processed.csv')
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        print("Processed data loaded successfully!")
        print(f"Dataset: {df.shape[0]} orders, {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print("Processed data not found. Please run 01_data_exploration.py first.")
        return None

def analyze_revenue_performance(df):
    """Analyze revenue trends and performance metrics"""
    
    print("\n💰 Revenue Performance Analysis")
    print("-" * 35)
    
    # Monthly revenue analysis
    monthly_revenue = df.groupby(df['Order Date'].dt.to_period('M')).agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count'
    }).rename(columns={'Order ID': 'Order_Count'})
    
    # Calculate growth rates
    monthly_revenue['Revenue_Growth_%'] = monthly_revenue['Sales'].pct_change() * 100
    monthly_revenue['Profit_Growth_%'] = monthly_revenue['Profit'].pct_change() * 100
    
    print("📈 Monthly Revenue Summary:")
    print(monthly_revenue.round(2))
    
    # Key metrics
    total_revenue = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    avg_order_value = df['Sales'].mean()
    total_orders = len(df)
    
    print(f"\n📊 Key Revenue Metrics:")
    print(f"  Total Revenue: ${total_revenue:,.2f}")
    print(f"  Total Profit: ${total_profit:,.2f}")
    print(f"  Average Order Value: ${avg_order_value:,.2f}")
    print(f"  Total Orders: {total_orders:,}")
    print(f"  Overall Profit Margin: {(total_profit/total_revenue)*100:.2f}%")
    
    # Create revenue visualization
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Monthly Revenue Trend
    monthly_revenue['Sales'].plot(kind='line', ax=ax1, marker='o', color='#2E86AB')
    ax1.set_title('Monthly Revenue Trend')
    ax1.set_ylabel('Revenue ($)')
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, alpha=0.3)
    
    # Monthly Profit Trend
    monthly_revenue['Profit'].plot(kind='line', ax=ax2, marker='s', color='#A23B72')
    ax2.set_title('Monthly Profit Trend')
    ax2.set_ylabel('Profit ($)')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3)
    
    # Order Count Trend
    monthly_revenue['Order_Count'].plot(kind='bar', ax=ax3, color='#F18F01')
    ax3.set_title('Monthly Order Count')
    ax3.set_ylabel('Number of Orders')
    ax3.tick_params(axis='x', rotation=45)
    
    # Average Order Value
    aov = monthly_revenue['Sales'] / monthly_revenue['Order_Count']
    aov.plot(kind='line', ax=ax4, marker='D', color='#C73E1D')
    ax4.set_title('Average Order Value Trend')
    ax4.set_ylabel('AOV ($)')
    ax4.tick_params(axis='x', rotation=45)
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('visualizations/revenue_performance.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Revenue performance chart saved to: visualizations/revenue_performance.png")
    
    return monthly_revenue

def analyze_product_performance(df):
    """Analyze product and category performance"""
    
    print("\n📦 Product Performance Analysis")
    print("-" * 35)
    
    # Category performance
    category_perf = df.groupby('Category').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count',
        'Profit_Margin_%': 'mean'
    }).rename(columns={'Order ID': 'Order_Count'}).sort_values('Sales', ascending=False)
    
    # Sub-category performance
    subcat_perf = df.groupby('Sub-Category').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count'
    }).rename(columns={'Order ID': 'Order_Count'}).sort_values('Sales', ascending=False)
    
    print("🏆 Category Performance:")
    print(category_perf.round(2))
    
    print(f"\n🔝 Top 10 Sub-Categories:")
    print(subcat_perf.head(10).round(2))
    
    # Create product visualizations
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Category Revenue
    category_perf['Sales'].plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_title('Revenue by Category')
    ax1.tick_params(axis='x', rotation=45)
    
    # Category Profit
    category_perf['Profit'].plot(kind='bar', ax=ax2, color='lightgreen')
    ax2.set_title('Profit by Category')
    ax2.tick_params(axis='x', rotation=45)
    
    # Top 10 Sub-categories
    subcat_perf.head(10)['Sales'].plot(kind='barh', ax=ax3, color='salmon')
    ax3.set_title('Top 10 Sub-Categories by Revenue')
    
    # Profit Margin by Category
    category_perf['Profit_Margin_%'].plot(kind='bar', ax=ax4, color='gold')
    ax4.set_title('Average Profit Margin by Category')
    ax4.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('visualizations/product_performance.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Product performance chart saved to: visualizations/product_performance.png")
    
    return category_perf, subcat_perf

def analyze_geographic_performance(df):
    """Analyze regional and city performance"""
    
    print("\n🌍 Geographic Performance Analysis")
    print("-" * 38)
    
    # Region performance
    region_perf = df.groupby('Region').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count',
        'Customer Name': 'nunique'
    }).rename(columns={'Order ID': 'Order_Count', 'Customer Name': 'Unique_Customers'})
    
    # City performance (top 15)
    city_perf = df.groupby('City').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count'
    }).rename(columns={'Order ID': 'Order_Count'}).sort_values('Sales', ascending=False).head(15)
    
    print("🌍 Regional Performance:")
    print(region_perf.round(2))
    
    print(f"\n🏙️ Top 15 Cities by Revenue:")
    print(city_perf.round(2))
    
    # Create geographic visualizations
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Region Revenue Pie Chart
    region_perf['Sales'].plot(kind='pie', ax=ax1, autopct='%1.1f%%', startangle=90)
    ax1.set_title('Revenue Distribution by Region')
    ax1.set_ylabel('')
    
    # Region Customer Count
    region_perf['Unique_Customers'].plot(kind='bar', ax=ax2, color='lightcoral')
    ax2.set_title('Unique Customers by Region')
    ax2.tick_params(axis='x', rotation=45)
    
    # Top Cities by Revenue
    city_perf['Sales'].plot(kind='bar', ax=ax3, color='mediumseagreen')
    ax3.set_title('Top 15 Cities by Revenue')
    ax3.tick_params(axis='x', rotation=45)
    
    # Region Profit
    region_perf['Profit'].plot(kind='bar', ax=ax4, color='royalblue')
    ax4.set_title('Profit by Region')
    ax4.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('visualizations/geographic_performance.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Geographic performance chart saved to: visualizations/geographic_performance.png")
    
    return region_perf, city_perf

def analyze_customer_behavior(df):
    """Analyze customer behavior and segmentation"""
    
    print("\n👥 Customer Behavior Analysis")
    print("-" * 32)
    
    # Customer statistics
    customer_stats = df.groupby('Customer Name').agg({
        'Sales': ['sum', 'mean'],
        'Order ID': 'count',
        'Order Date': ['min', 'max']
    }).round(2)
    
    # Flatten column names
    customer_stats.columns = ['Total_Sales', 'Avg_Order_Value', 'Order_Count', 'First_Order', 'Last_Order']
    
    # Calculate customer lifetime in days
    customer_stats['Customer_Lifetime_Days'] = (customer_stats['Last_Order'] - customer_stats['First_Order']).dt.days
    
    # Segment customers based on total sales
    customer_stats['Segment'] = pd.cut(customer_stats['Total_Sales'],
                                       bins=[0, 1000, 5000, 20000, float('inf')],
                                       labels=['Bronze', 'Silver', 'Gold', 'Platinum'])
    
    # Payment mode analysis
    payment_analysis = df.groupby('Payment Mode').agg({
        'Sales': 'sum',
        'Order ID': 'count',
        'Customer Name': 'nunique'
    }).rename(columns={'Order ID': 'Order_Count', 'Customer Name': 'Unique_Customers'})
    
    print("👥 Customer Segments:")
    segment_summary = customer_stats.groupby('Segment').agg({
        'Total_Sales': 'sum',
        'Order_Count': 'sum',
        'Customer Name': 'count'
    }).rename(columns={'Customer Name': 'Customer_Count'})
    print(segment_summary.round(2))
    
    print(f"\n💳 Payment Methods:")
    print(payment_analysis.round(2))
    
    print(f"\n📊 Customer Insights:")
    print(f"  Total Unique Customers: {len(customer_stats):,}")
    print(f"  Average Orders per Customer: {customer_stats['Order_Count'].mean():.1f}")
    print(f"  Average Customer Lifetime: {customer_stats['Customer_Lifetime_Days'].mean():.0f} days")
    print(f"  Average Customer Value: ${customer_stats['Total_Sales'].mean():,.2f}")
    
    # Create customer visualizations
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Customer Segments
    customer_stats['Segment'].value_counts().plot(kind='bar', ax=ax1, color='gold')
    ax1.set_title('Customer Segments Distribution')
    ax1.tick_params(axis='x', rotation=45)
    
    # Payment Methods
    payment_analysis['Order_Count'].plot(kind='bar', ax=ax2, color='lightblue')
    ax2.set_title('Orders by Payment Method')
    ax2.tick_params(axis='x', rotation=45)
    
    # Order Frequency Distribution
    customer_stats['Order_Count'].hist(bins=20, ax=ax3, color='lightgreen', alpha=0.7)
    ax3.set_title('Order Frequency Distribution')
    ax3.set_xlabel('Number of Orders')
    ax3.set_ylabel('Number of Customers')
    
    # Average Order Value by Segment
    customer_stats.groupby('Segment')['Avg_Order_Value'].mean().plot(kind='bar', ax=ax4, color='salmon')
    ax4.set_title('Average Order Value by Customer Segment')
    ax4.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('visualizations/customer_behavior.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Customer behavior chart saved to: visualizations/customer_behavior.png")
    
    return customer_stats, payment_analysis

def analyze_profitability(df):
    """Analyze profitability and discount impact"""
    
    print("\n💸 Profitability Analysis")
    print("-" * 28)
    
    # Discount impact analysis
    discount_impact = df.groupby(pd.cut(df['Discount'], bins=[0, 5, 10, 15, 20, 25, 30], 
                                     labels=['0-5%', '6-10%', '11-15%', '16-20%', '21-25%', '26-30%'])).agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count',
        'Profit_Margin_%': 'mean'
    }).rename(columns={'Order ID': 'Order_Count'})
    
    # Most and least profitable products
    product_profit = df.groupby('Product Name').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Order ID': 'count',
        'Profit_Margin_%': 'mean'
    }).rename(columns={'Order ID': 'Order_Count'})
    
    print("💰 Profitability Insights:")
    print(f"  Overall Profit Margin: {df['Profit_Margin_%'].mean():.2f}%")
    print(f"  Total Revenue: ${df['Sales'].sum():,.2f}")
    print(f"  Total Profit: ${df['Profit'].sum():,.2f}")
    print(f"  Profitable Orders: {len(df[df['Profit'] > 0]):,} ({len(df[df['Profit'] > 0])/len(df)*100:.1f}%)")
    print(f"  Unprofitable Orders: {len(df[df['Profit'] <= 0]):,} ({len(df[df['Profit'] <= 0])/len(df)*100:.1f}%)")
    
    print(f"\n📊 Discount Impact Analysis:")
    print(discount_impact.round(2))
    
    print(f"\n🏆 Top 10 Most Profitable Products:")
    print(product_profit.nlargest(10, 'Profit').round(2))
    
    print(f"\n📉 Bottom 10 Least Profitable Products:")
    print(product_profit.nsmallest(10, 'Profit').round(2))
    
    # Create profitability visualizations
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Discount Impact
    discount_impact['Profit_Margin_%'].plot(kind='bar', ax=ax1, color='orange')
    ax1.set_title('Profit Margin by Discount Range')
    ax1.tick_params(axis='x', rotation=45)
    
    # Category Profit Margins
    category_profit = df.groupby('Category')['Profit_Margin_%'].mean()
    category_profit.plot(kind='bar', ax=ax2, color='green')
    ax2.set_title('Average Profit Margin by Category')
    ax2.tick_params(axis='x', rotation=45)
    
    # Top 10 Most Profitable Products
    product_profit.nlargest(10, 'Profit')['Profit'].plot(kind='barh', ax=ax3, color='darkgreen')
    ax3.set_title('Top 10 Most Profitable Products')
    
    # Bottom 10 Least Profitable Products
    product_profit.nsmallest(10, 'Profit')['Profit'].plot(kind='barh', ax=ax4, color='red')
    ax4.set_title('Bottom 10 Least Profitable Products')
    
    plt.tight_layout()
    plt.savefig('visualizations/profitability_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Profitability analysis chart saved to: visualizations/profitability_analysis.png")
    
    return discount_impact, product_profit

def generate_business_recommendations(df):
    """Generate actionable business recommendations"""
    
    print("\n🎯 Business Recommendations")
    print("-" * 30)
    
    recommendations = []
    
    # Revenue Analysis
    monthly_trend = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
    if len(monthly_trend) > 1:
        if monthly_trend.iloc[-1] > monthly_trend.iloc[-2]:
            recommendations.append("✅ Revenue is growing month-over-month - continue current strategies")
        else:
            recommendations.append("⚠️ Revenue declined last month - investigate causes and implement recovery strategies")
    
    # Category Performance
    category_perf = df.groupby('Category')['Profit_Margin_%'].mean().sort_values(ascending=False)
    best_category = category_perf.index[0]
    worst_category = category_perf.index[-1]
    recommendations.append(f"🏆 {best_category} has highest profit margins ({category_perf.iloc[0]:.1f}%) - consider expanding this category")
    recommendations.append(f"📉 {worst_category} has lowest profit margins ({category_perf.iloc[-1]:.1f}%) - review pricing and costs")
    
    # Geographic Analysis
    region_perf = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    top_region = region_perf.index[0]
    recommendations.append(f"🌍 {top_region} generates most revenue (${region_perf.iloc[0]:,.0f}) - strengthen presence in this region")
    
    # Customer Analysis
    avg_orders_per_customer = df.groupby('Customer Name')['Order ID'].count().mean()
    if avg_orders_per_customer < 2:
        recommendations.append("👥 Low repeat purchase rate - implement customer retention programs")
    else:
        recommendations.append("👥 Good customer retention - maintain current loyalty programs")
    
    # Discount Analysis
    high_discount_orders = df[df['Discount'] > 15]
    if len(high_discount_orders) > len(df) * 0.3:
        recommendations.append("💸 High discount usage (>15%) - review discount strategy and impact on profitability")
    
    # Payment Methods
    payment_methods = df['Payment Mode'].value_counts()
    if 'UPI' in payment_methods.index and payment_methods['UPI'] > len(df) * 0.3:
        recommendations.append("💳 High UPI usage - ensure UPI infrastructure is robust")
    
    # Display recommendations
    for i, rec in enumerate(recommendations, 1):
    
# Discount Analysis
high_discount_orders = df[df['Discount'] > 15]
if len(high_discount_orders) > len(df) * 0.3:
    recommendations.append("High discount usage (>15%) - review discount strategy and impact on profitability")
    
# Payment Methods
payment_methods = df['Payment Mode'].value_counts()
if 'UPI' in payment_methods.index and payment_methods['UPI'] > len(df) * 0.3:
    recommendations.append("High UPI usage - ensure UPI infrastructure is robust")
    
# Display recommendations
for i, rec in enumerate(recommendations, 1):
    print(f"{i}. {rec}")
    
# Save recommendations to file
recommendations_df = pd.DataFrame({'Recommendation': recommendations})
recommendations_df.to_csv('../reports/business_recommendations.csv', index=False)
print(f"Recommendations saved to: ../reports/business_recommendations.csv")
    
return recommendations

def create_executive_summary(df):
    """Create executive summary with key metrics"""
    
print("\nCreating Executive Summary")
print("-" * 30)
    print("\n📋 Creating Executive Summary")
    print("-" * 30)
    
    # Calculate key metrics
    total_revenue = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    total_orders = len(df)
    unique_customers = df['Customer Name'].nunique()
    unique_products = df['Product Name'].nunique()
    avg_order_value = df['Sales'].mean()
    profit_margin = (total_profit / total_revenue) * 100
    
    # Create summary data
    summary_data = {
        'Metric': [
            'Total Revenue', 'Total Profit', 'Total Orders', 'Unique Customers',
            'Unique Products', 'Average Order Value', 'Profit Margin', 'Date Range Start', 'Date Range End'
        ],
        'Value': [
            f"${total_revenue:,.2f}",
            f"${total_profit:,.2f}",
            f"{total_orders:,}",
            f"{unique_customers:,}",
            f"{unique_products:,}",
            f"${avg_order_value:,.2f}",
            f"{profit_margin:.2f}%",
            str(df['Order Date'].min().date()),
            str(df['Order Date'].max().date())
        ]
    }
    
    summary_df = pd.DataFrame(summary_data)
    
    # Create reports directory if it doesn't exist
    os.makedirs('reports', exist_ok=True)
    
    # Save executive summary
    summary_df.to_csv('reports/executive_summary.csv', index=False)
    print("Executive summary saved to: reports/executive_summary.csv")
    
    # Print summary
    print("\n📊 Executive Summary:")
    print("-" * 20)
    for _, row in summary_df.iterrows():
        print(f"{row['Metric']}: {row['Value']}")
    
    return summary_df

def main():
    """Main function to run the complete business analysis"""
    
    # Load processed data
    df = load_processed_data()
    if df is None:
        return
    
    # Run all analyses
    analyze_revenue_performance(df)
    analyze_product_performance(df)
    analyze_geographic_performance(df)
    analyze_customer_behavior(df)
    analyze_profitability(df)
    
    # Generate recommendations
    generate_business_recommendations(df)
    
    # Create executive summary
    create_executive_summary(df)
    
    print("\n🎉 Business Analysis Complete!")
    print("=" * 35)
    print("📁 Generated Files:")
    print("   📊 Visualizations: ../visualizations/")
    print("   📋 Reports: ../reports/")
    print("   💾 Processed Data: ../data/processed/")
    print("\n🚀 Ready for business decision-making!")

if __name__ == "__main__":
    main()
