#!/usr/bin/env python3
"""
E-Commerce Sales Data Exploration Script
This script performs initial data exploration and preprocessing.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

def load_and_explore_data():
    """Load and explore the e-commerce dataset"""
    
    print("E-Commerce Sales Data Exploration")
    print("=" * 50)
    
    # Load the dataset
    try:
        df = pd.read_csv('data/raw/Ecommerce_Sales_Data_2024_2025.csv')
        print("Data loaded successfully!")
        print(f"Dataset shape: {df.shape}")
        print(f"Date range: {df['Order Date'].min()} to {df['Order Date'].max()}")
    except FileNotFoundError:
        print("Dataset not found. Please run download_dataset.py first.")
        return None
    
    return df

def analyze_dataset_structure(df):
    """Analyze the dataset structure and basic statistics"""
    
    print("Dataset Structure Analysis")
    print("-" * 30)
    
    print(f"Dataset Shape: {df.shape}")
    print(f"\nColumns: {list(df.columns)}")
    
    print(f"\nData Types:")
    print(df.dtypes)
    
    print(f"\nMissing Values:")
    missing = df.isnull().sum()
    for col, count in missing.items():
        if count > 0:
            print(f"  {col}: {count} ({count/len(df)*100:.1f}%)")
        else:
            print(f"  {col}: {count}")
    
    print(f"\nFirst 5 rows:")
    print(df.head())
    
    print(f"\nBasic Statistics:")
    numeric_cols = ['Quantity', 'Unit Price', 'Discount', 'Sales', 'Profit']
    print(df[numeric_cols].describe())
    
    print(f"\nCategorical Variables Summary:")
    categorical_cols = ['Region', 'City', 'Category', 'Sub-Category', 'Payment Mode']
    for col in categorical_cols:
        print(f"\n{col}:")
        print(df[col].value_counts().head(10))

def preprocess_data(df):
    """Preprocess the data and create additional features"""
    
    print("Data Preprocessing")
    print("-" * 25)
    
    # Convert Order Date to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    
    # Extract time-based features
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['Quarter'] = df['Order Date'].dt.quarter
    df['DayOfWeek'] = df['Order Date'].dt.day_name()
    df['MonthName'] = df['Order Date'].dt.month_name()
    
    # Calculate profit margin
    df['Profit_Margin_%'] = (df['Profit'] / df['Sales']) * 100
    
    # Calculate effective price after discount
    df['Effective_Price'] = df['Unit Price'] * (1 - df['Discount']/100)
    
    # Create order value categories
    df['Order_Value_Category'] = pd.cut(df['Sales'], 
                                       bins=[0, 100, 500, 1000, 5000, float('inf')],
                                       labels=['Small', 'Medium', 'Large', 'Very Large', 'Enterprise'])
    
    print("Data preprocessing completed!")
    print(f"New features added: Year, Month, Quarter, DayOfWeek, MonthName, Profit_Margin_%, Effective_Price, Order_Value_Category")
    
    return df

def save_processed_data(df):
    """Save the processed data for further analysis"""
    
    print("Saving Processed Data")
    print("-" * 25)
    
    # Create processed data directory if it doesn't exist
    os.makedirs('data/processed', exist_ok=True)
    
    # Save processed data
    df.to_csv('data/processed/ecommerce_processed.csv', index=False)
    print("Processed data saved to: data/processed/ecommerce_processed.csv")
    
    # Save data summary
    summary = {
        'total_orders': len(df),
        'total_revenue': df['Sales'].sum(),
        'total_profit': df['Profit'].sum(),
        'avg_order_value': df['Sales'].mean(),
        'avg_profit_margin': df['Profit_Margin_%'].mean(),
        'unique_customers': df['Customer Name'].nunique(),
        'unique_products': df['Product Name'].nunique(),
        'date_range_start': df['Order Date'].min(),
        'date_range_end': df['Order Date'].max()
    }
    
    summary_df = pd.DataFrame([summary])
    summary_df.to_csv('data/processed/data_summary.csv', index=False)
    print("Data summary saved to: data/processed/data_summary.csv")

def create_basic_visualizations(df):
    """Create basic exploratory visualizations"""
    
    print("Creating Basic Visualizations")
    print("-" * 35)
    
    # Create visualizations directory
    os.makedirs('visualizations', exist_ok=True)
    
    # Set up the plotting style
    plt.style.use('seaborn-v0_8')
    
    # 1. Sales by Category
    plt.figure(figsize=(12, 6))
    category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    category_sales.plot(kind='bar', color='skyblue')
    plt.title('Total Sales by Category', fontsize=16, fontweight='bold')
    plt.xlabel('Category')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/sales_by_category.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Profit by Category
    plt.figure(figsize=(12, 6))
    category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
    category_profit.plot(kind='bar', color='lightgreen')
    plt.title('Total Profit by Category', fontsize=16, fontweight='bold')
    plt.xlabel('Category')
    plt.ylabel('Total Profit ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/profit_by_category.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Monthly Sales Trend
    plt.figure(figsize=(12, 6))
    monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
    monthly_sales.plot(kind='line', marker='o', color='orange')
    plt.title('Monthly Sales Trend', fontsize=16, fontweight='bold')
    plt.xlabel('Month')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('visualizations/monthly_sales_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Payment Methods
    plt.figure(figsize=(10, 6))
    payment_counts = df['Payment Mode'].value_counts()
    plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Payment Methods Distribution', fontsize=16, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('visualizations/payment_methods.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Visualizations saved to: visualizations/")
    print("   - sales_by_category.png")
    print("   - profit_by_category.png") 
    print("   - monthly_sales_trend.png")
    print("   - payment_methods.png")

def print_key_insights(df):
    """Print key insights from the data"""
    
    print("Key Data Insights")
    print("-" * 20)
    
    print(f"Total Orders: {len(df):,}")
    print(f"Total Revenue: ${df['Sales'].sum():,.2f}")
    print(f"Total Profit: ${df['Profit'].sum():,.2f}")
    print(f"Average Order Value: ${df['Sales'].mean():,.2f}")
    print(f"Average Profit Margin: {df['Profit_Margin_%'].mean():.2f}%")
    print(f"Unique Customers: {df['Customer Name'].nunique():,}")
    print(f"Unique Products: {df['Product Name'].nunique():,}")
    
    print("Top 3 Categories by Revenue:")
    top_categories = df.groupby('Category')['Sales'].sum().sort_values(ascending=False).head(3)
    for i, (category, sales) in enumerate(top_categories.items(), 1):
        print(f"  {i}. {category}: ${sales:,.2f}")
    
    print("Top 3 Regions by Revenue:")
    top_regions = df.groupby('Region')['Sales'].sum().sort_values(ascending=False).head(3)
    for i, (region, sales) in enumerate(top_regions.items(), 1):
        print(f"  {i}. {region}: ${sales:,.2f}")
    
    print("Payment Methods:")
    payment_methods = df['Payment Mode'].value_counts()
    for method, count in payment_methods.items():
        percentage = (count / len(df)) * 100
        print(f"  {method}: {count} orders ({percentage:.1f}%)")

def main():
    """Main function to run the data exploration"""
    
    # Load and explore data
    df = load_and_explore_data()
    if df is None:
        return
    
    # Analyze dataset structure
    analyze_dataset_structure(df)
    
    # Preprocess data
    df = preprocess_data(df)
    
    # Save processed data
    save_processed_data(df)
    
    # Create basic visualizations
    create_basic_visualizations(df)
    
    # Print key insights
    print_key_insights(df)
    
    print("Data Exploration Complete!")
    print("=" * 40)
    print("Next Steps:")
    print("   1. Run '02_business_analysis.py' for detailed business insights")
    print("   2. Check 'visualizations/' for generated charts")
    print("   3. Review 'data/processed/' for cleaned data")

if __name__ == "__main__":
    main()
