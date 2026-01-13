#!/usr/bin/env python3
"""
E-Commerce Sales Analysis - Main Runner Script
This script runs the complete analysis pipeline from data loading to business insights.
"""

import os
import sys
import subprocess
from datetime import datetime

def check_requirements():
    """Check if required packages are installed"""
    
    print("Checking Requirements...")
    
    required_packages = [
        'pandas', 'numpy', 'matplotlib', 'seaborn'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"  {package}")
    
    if missing_packages:
        print(f"Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("All requirements met!")
    return True

def run_script(script_name):
    """Run a Python script and handle errors"""
    
    print(f"Running {script_name}...")
    print("=" * 50)
    
    try:
        result = subprocess.run([sys.executable, f'scripts/{script_name}'], 
                              cwd=os.path.dirname(os.path.abspath(__file__)),
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print(result.stdout)
            print(f"{script_name} completed successfully!")
            return True
        else:
            print(f"Error in {script_name}:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"Failed to run {script_name}: {e}")
        return False

def check_data_exists():
    """Check if the dataset exists"""
    
    data_path = 'data/raw/Ecommerce_Sales_Data_2024_2025.csv'
    
    if os.path.exists(data_path):
        print(f"Dataset found: {data_path}")
        return True
    else:
        print(f"Dataset not found: {data_path}")
        print("Please run the download script first:")
        print("python scripts/download_dataset.py")
        return False

def show_menu():
    """Display analysis options menu"""
    
    print("E-Commerce Sales Analysis Options:")
    print("=" * 45)
    print("1. Run Complete Analysis Pipeline")
    print("2. Data Exploration Only")
    print("3. Business Analysis Only")
    print("4. Download Dataset")
    print("5. View Generated Reports")
    print("6. Launch Interactive Dashboard")
    print("7. Exit")
    print("=" * 45)

def launch_dashboard():
    """Launch the interactive dashboard"""
    
    print("Launching Interactive Dashboard...")
    print("=" * 40)
    
    # Check if dashboard.html exists
    if not os.path.exists('dashboard.html'):
        print("Dashboard file not found. Creating it...")
        return False
    
    try:
        # Import the dashboard runner
        import subprocess
        result = subprocess.run([sys.executable, 'run_dashboard.py'], 
                              cwd=os.path.dirname(os.path.abspath(__file__)),
                              capture_output=False)
        return result.returncode == 0
    except Exception as e:
        print(f"Failed to launch dashboard: {e}")
        print("You can manually open: dashboard.html")
        return False

def view_reports():
    """Show available reports and visualizations"""
    
    print("Generated Reports and Visualizations:")
    print("=" * 45)
    
    # Check processed data
    if os.path.exists('data/processed/ecommerce_processed.csv'):
        print("Processed Data: data/processed/ecommerce_processed.csv")
    
    # Check reports
    reports_dir = 'reports'
    if os.path.exists(reports_dir):
        reports = [f for f in os.listdir(reports_dir) if f.endswith('.csv')]
        if reports:
            print("Reports:")
            for report in reports:
                print(f"  - {reports_dir}/{report}")
    
    # Check visualizations
    viz_dir = 'visualizations'
    if os.path.exists(viz_dir):
        visualizations = [f for f in os.listdir(viz_dir) if f.endswith('.png')]
        if visualizations:
            print("Visualizations:")
            for viz in visualizations:
                print(f"  - {viz_dir}/{viz}")
    
    if not os.path.exists('reports') and not os.path.exists('visualizations'):
        print("No reports or visualizations found yet.")
        print("Run the analysis first to generate reports.")

def main():
    """Main function with menu interface"""
    
    print("E-Commerce Sales Performance Analysis")
    print("=" * 50)
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check requirements
    if not check_requirements():
        return
    
    while True:
        show_menu()
        
        try:
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == '1':
                # Run complete pipeline
                if not check_data_exists():
                    print("Downloading dataset first...")
                    if not run_script('download_dataset.py'):
                        continue
                
                print("Running Complete Analysis Pipeline...")
                success = True
                success &= run_script('01_data_exploration.py')
                if success:
                    success &= run_script('02_business_analysis.py')
                
                if success:
                    print("Complete analysis finished successfully!")
                    view_reports()
                else:
                    print("Analysis pipeline failed. Check errors above.")
            
            elif choice == '2':
                # Data exploration only
                if not check_data_exists():
                    print("Dataset not found. Please download first (option 4).")
                    continue
                
                run_script('01_data_exploration.py')
            
            elif choice == '3':
                # Business analysis only
                if not os.path.exists('data/processed/ecommerce_processed.csv'):
                    print("Processed data not found. Please run data exploration first (option 2).")
                    continue
                
                run_script('02_business_analysis.py')
            
            elif choice == '4':
                # Download dataset
                run_script('download_dataset.py')
            
            elif choice == '5':
                # View reports
                view_reports()
            
            elif choice == '6':
                launch_dashboard()
            elif choice == '7':
                print("Thank you for using E-Commerce Sales Analysis!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1-7.")
        
        except KeyboardInterrupt:
            print("Analysis interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
