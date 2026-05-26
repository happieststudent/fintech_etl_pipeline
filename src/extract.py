# src/extract.py
import yfinance as yf
import pandas as pd

def get_stock_data():
    # Download Apple data from Jan 2022 to Jan 2024
    print("Fetching AAPL data...")
    df = yf.download("AAPL", start="2022-01-01", end="2024-01-01")
    
    # Display the first 5 rows to ensure it worked
    print(df.head())
    return df

if __name__ == "__main__":
    get_stock_data()
    git config --global user.email "maikhelcn70@gmail.com"
git config --global user.name "Maikhel"

git commit -m "Phase 1: Added basic yfinance data extraction"