#!/usr/bin/env python3
"""
E-Commerce Sales Analysis - Data Analyst Workflow
"""

import os
import sys
import subprocess
from datetime import datetime

def run_script(script_name):
    """Run a Python script and handle errors"""
    
    print(f"🔄 Running {script_name}...")
    print("=" * 50)
    
    try:
        result = subprocess.run([sys.executable, f'scripts/{script_name}'], 
                              cwd=os.path.dirname(os.path.abspath(__file__)),
                              capture_output=False, text=True)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Failed to run {script_name}: {e}")
        return False

def check_data_exists():
    """Check if the raw dataset exists"""
    
    data_path = 'data/raw/Ecommerce_Sales_Data_2024_2025.csv'
    if os.path.exists(data_path):
        print(f"✅ Dataset found: {data_path}")
        return True
    else:
        print(f"❌ Dataset not found: {data_path}")
        print("Please run download_dataset.py first")
        return False

def show_results():
    """Show available analysis results"""
    
    print("📊 Analysis Results:")
    print("=" * 30)
    
    if os.path.exists('data/processed/ecommerce_cleaned.csv'):
        print("✅ Cleaned Data: data/processed/ecommerce_cleaned.csv")
    
    if os.path.exists('reports'):
        reports = [f for f in os.listdir('reports') if f.endswith('.csv')]
        if reports:
            print("📋 Business Reports:")
            for report in reports:
                print(f"   - reports/{report}")
    
    if os.path.exists('sql'):
        sql_files = [f for f in os.listdir('sql') if f.endswith('.sql')]
        if sql_files:
            print("🗃️ SQL Analysis Files:")
            for sql_file in sql_files:
                print(f"   - sql/{sql_file}")
    
    if os.path.exists('powerbi/README.md'):
        print("📊 Power BI Guide: powerbi/README.md")

def main():
    """Main analysis workflow"""
    
    print("📊 E-Commerce Sales Analysis")
    print("Data Analyst Focused Workflow")
    print("=" * 40)
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if not check_data_exists():
        return
    
    print("\n🔄 Running Analysis Pipeline:")
    
    if not run_script('data_cleaning.py'):
        print("❌ Data cleaning failed. Stopping pipeline.")
        return
    
    if not run_script('business_analysis.py'):
        print("❌ Business analysis failed.")
        return
    
    show_results()
    
    print(f"\n🎉 Analysis Complete!")
    print("📁 Key Outputs:")
    print("   - Cleaned data: data/processed/")
    print("   - Business reports: reports/")
    print("   - SQL queries: sql/")
    print("   - Power BI guide: powerbi/")
    print("\n🚀 Ready for Power BI dashboard creation!")

if __name__ == "__main__":
    main()
