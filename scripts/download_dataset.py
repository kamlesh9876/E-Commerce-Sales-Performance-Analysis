#!/usr/bin/env python3
"""
Script to download e-commerce sales dataset from Kaggle
"""

import kagglehub
import os
import shutil
import pandas as pd
from pathlib import Path

def download_ecommerce_dataset():
    """Download e-commerce sales dataset from Kaggle"""
    
    print("Downloading E-Commerce Sales Dataset from Kaggle...")
    print("Dataset: prince7489/e-commerce-sales")
    
    try:
        # Download latest version
        path = kagglehub.dataset_download("prince7489/e-commerce-sales")
        
        print(f"Dataset downloaded successfully!")
        print(f"Path to dataset files: {path}")
        
        # List downloaded files
        print("Downloaded files:")
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            size = os.path.getsize(file_path) / (1024 * 1024)  # Size in MB
            print(f"  - {file} ({size:.2f} MB)")
        
        return path
        
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        print("Possible solutions:")
        print("1. Make sure you have internet connection")
        print("2. Check if Kaggle API credentials are set up")
        print("3. Verify dataset name is correct")
        return None

def move_dataset_to_project(source_path, project_root):
    """Move downloaded dataset to project data/raw directory"""
    
    raw_data_dir = os.path.join(project_root, "data", "raw")
    
    print(f"Moving dataset to: {raw_data_dir}")
    
    try:
        # Ensure the raw data directory exists
        os.makedirs(raw_data_dir, exist_ok=True)
        
        # Copy all files from download to data/raw
        files_copied = []
        for file in os.listdir(source_path):
            source_file = os.path.join(source_path, file)
            dest_file = os.path.join(raw_data_dir, file)
            
            if os.path.isfile(source_file):
                shutil.copy2(source_file, dest_file)
                files_copied.append(file)
                print(f"Copied: {file}")
        
        print(f"Successfully copied {len(files_copied)} files to data/raw/")
        return True
        
    except Exception as e:
        print(f"Error moving dataset: {e}")
        return False

def explore_dataset_files(raw_data_dir):
    """Explore the downloaded dataset files"""
    
    print("Exploring dataset structure...")
    
    try:
        # Look for CSV files
        csv_files = [f for f in os.listdir(raw_data_dir) if f.endswith('.csv')]
        
        if not csv_files:
            print(f"No CSV files found in the dataset")
            return
        
        print(f"Found {len(csv_files)} CSV files:")
        
        for csv_file in csv_files:
            file_path = os.path.join(raw_data_dir, csv_file)
            
            try:
                # Read first few rows to understand structure
                df = pd.read_csv(file_path, nrows=5)
                file_size = os.path.getsize(file_path) / (1024 * 1024)  # Size in MB
                
                print(f"{csv_file}")
                print(f"Size: {file_size:.2f} MB")
                print(f"Shape: {df.shape} (showing first 5 rows)")
                print(f"Columns: {list(df.columns)}")
                print("Sample data:")
                print(df.head(3).to_string(index=False))
                
            except Exception as e:
                print(f"Error reading {csv_file}: {e}")
        
    except Exception as e:
        print(f"Error exploring dataset: {e}")

def main():
    """Main function to download and setup dataset"""
    
    # Get project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print("E-Commerce Sales Dataset Downloader")
    print("=" * 50)
    
    # Download dataset
    download_path = download_ecommerce_dataset()
    
    if download_path:
        # Move to project directory
        success = move_dataset_to_project(download_path, project_root)
        
        if success:
            # Explore the dataset
            raw_data_dir = os.path.join(project_root, "data", "raw")
            explore_dataset_files(raw_data_dir)
            
            print("Dataset setup complete!")
            print(f"Data location: {raw_data_dir}")
            print("Next step: Open notebooks/01_data_exploration.ipynb to start analysis")
        
        # Clean up download directory
        try:
            shutil.rmtree(download_path)
            print("Cleaned up temporary download directory")
        except:
            pass
    
    else:
        print("Failed to download dataset. Please check the error messages above.")

if __name__ == "__main__":
    main()
